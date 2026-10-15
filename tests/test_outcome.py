"""Tests for the outcome-experiment scorer (dsx/outcome.py) and the exact
binomial helpers it uses (dsx/mathx.py).

Reference values: Clopper-Pearson one-sided 95% upper bounds 1 - 0.05**(1/n)
for zero events and 0.2161 for 1/20 (Clopper & Pearson 1934 tables); exact
McNemar p for (3, 12) is 2 * 576 / 2**15.

Run:  python -m unittest tests.test_outcome -v
"""

from __future__ import annotations

import io
import json
import math
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dsx import cli
from dsx.findings import CheckError
from dsx.mathx import (
    binom_cdf,
    clean_examples_needed,
    clopper_pearson_upper,
    mcnemar_exact,
    paired_diff_ci,
    wilson_interval,
)
from dsx.outcome import is_correct, read_jsonl, score

FIX = Path(__file__).resolve().parent / "fixtures" / "outcome"


class BinomialHelpersTest(unittest.TestCase):
    def test_clopper_pearson(self):
        self.assertAlmostEqual(clopper_pearson_upper(0, 15), 1 - 0.05 ** (1 / 15), places=9)
        self.assertAlmostEqual(clopper_pearson_upper(0, 15), 0.1810, places=4)
        self.assertAlmostEqual(clopper_pearson_upper(1, 20), 0.2161, places=4)
        self.assertEqual(clopper_pearson_upper(5, 5), 1.0)
        with self.assertRaises(ValueError):
            clopper_pearson_upper(3, 2)

    def test_clean_examples_needed(self):
        self.assertEqual(clean_examples_needed(0.05), 59)
        n = clean_examples_needed(0.05)
        self.assertLessEqual(clopper_pearson_upper(0, n), 0.05)
        self.assertGreater(clopper_pearson_upper(0, n - 1), 0.05)

    def test_mcnemar_exact(self):
        self.assertAlmostEqual(mcnemar_exact(3, 12), 2 * 576 / 2**15)
        self.assertEqual(mcnemar_exact(0, 0), 1.0)
        self.assertEqual(mcnemar_exact(5, 5), 1.0)
        self.assertEqual(mcnemar_exact(3, 12), mcnemar_exact(12, 3))

    def test_binom_cdf(self):
        self.assertAlmostEqual(binom_cdf(2, 4, 0.5), 11 / 16)
        self.assertEqual(binom_cdf(-1, 4, 0.5), 0.0)
        self.assertEqual(binom_cdf(4, 4, 0.5), 1.0)

    def test_wilson(self):
        lo, hi = wilson_interval(0, 10)
        self.assertEqual(lo, 0.0)
        self.assertAlmostEqual(hi, 0.2775, places=4)
        lo, hi = wilson_interval(10, 10)
        self.assertEqual(hi, 1.0)

    def test_paired_ci(self):
        lo, hi = paired_diff_ci(3, 12, 100)
        self.assertAlmostEqual((lo + hi) / 2, 0.09)
        self.assertLess(lo, 0.09)
        with self.assertRaises(ValueError):
            paired_diff_ci(60, 60, 100)


class MatchingTest(unittest.TestCase):
    def test_scalar_and_string(self):
        self.assertTrue(is_correct(42, "42"))
        self.assertTrue(is_correct(42, 42.0))
        self.assertTrue(is_correct("Lisbon", " lisbon "))
        self.assertTrue(is_correct(0.3127, "0.31272"))
        self.assertFalse(is_correct(0.3127, 0.29))
        self.assertTrue(is_correct(1234567, "1,234,567"))
        self.assertFalse(is_correct(0, 1e-9))

    def test_tables_ignore_row_and_column_order(self):
        gold = {"columns": ["region", "revenue"], "rows": [["north", 1200.5], ["south", 800]]}
        ans = {"columns": ["revenue", "region"], "rows": [[800, "SOUTH"], [1200.5, "north"]]}
        self.assertTrue(is_correct(gold, ans))
        self.assertTrue(is_correct([[1, "a"], [2, "b"]], [[2, "b"], [1, "a"]]))
        doubled = {"columns": ["region", "revenue"], "rows": [["north", 2401.0], ["south", 800]]}
        self.assertFalse(is_correct(gold, doubled))
        # Rows are a multiset: a duplicated row is wrong.
        self.assertFalse(is_correct([[1], [2]], [[1], [1], [2]]))


class ScoreTest(unittest.TestCase):
    def setUp(self):
        self.res = score(
            read_jsonl(FIX / "key.jsonl", what="key"),
            read_jsonl(FIX / "control.jsonl", what="control"),
            read_jsonl(FIX / "treatment.jsonl", what="treatment"),
        )

    def test_primary_metric_counts_unanswered_as_wrong(self):
        self.assertEqual(self.res["n_tasks"], 5)
        self.assertEqual(self.res["control"]["accuracy"]["correct"], 3)
        self.assertEqual(self.res["treatment"]["accuracy"]["correct"], 3)
        self.assertEqual(self.res["treatment"]["selective_accuracy"]["n"], 3)
        self.assertEqual(self.res["treatment"]["selective_accuracy"]["accuracy"], 1.0)
        self.assertEqual(self.res["treatment"]["statuses"],
                         {"answered": 3, "blocked": 1, "missing": 1})

    def test_paired_and_blocked(self):
        paired = self.res["paired"]
        self.assertEqual(paired["discordant"], {"control_only": 2, "treatment_only": 2})
        self.assertEqual(paired["difference"], 0.0)
        self.assertEqual(paired["mcnemar_p"], 1.0)
        self.assertEqual(self.res["treatment_blocked"], {"n": 1, "control_correct_on_them": 1})
        self.assertEqual(self.res["stray_task_ids"], ["t9"])
        self.assertEqual(sorted(self.res["categories"]), ["document", "join", "single_table"])

    def test_deterministic(self):
        again = score(
            read_jsonl(FIX / "key.jsonl", what="key"),
            read_jsonl(FIX / "control.jsonl", what="control"),
            read_jsonl(FIX / "treatment.jsonl", what="treatment"),
        )
        self.assertEqual(json.dumps(again, sort_keys=True), json.dumps(self.res, sort_keys=True))
        self.assertFalse(math.isnan(self.res["paired"]["ci"][0]))

    def test_bad_input(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "bad.jsonl"
            bad.write_text('{"task_id": "a"}\n{"task_id": "a"}\n', encoding="utf-8")
            with self.assertRaises(CheckError):
                read_jsonl(bad, what="arm")
            bad.write_text('{"task_id": "a", "status": "skipped"}\n', encoding="utf-8")
            with self.assertRaises(CheckError):
                read_jsonl(bad, what="arm")
            bad.write_text("not json\n", encoding="utf-8")
            with self.assertRaises(CheckError):
                read_jsonl(bad, what="arm")
        with self.assertRaises(CheckError):
            score({}, {}, {})


class OutcomeCliTest(unittest.TestCase):
    def test_cli(self):
        argv = ["outcome", "--key", str(FIX / "key.jsonl"), "--control", str(FIX / "control.jsonl"),
                "--treatment", str(FIX / "treatment.jsonl")]
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            self.assertEqual(cli.main([*argv, "--json"]), 0)
        self.assertEqual(json.loads(out.getvalue())["n_tasks"], 5)
        out = io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            self.assertEqual(cli.main(argv), 0)
        self.assertIn("exact McNemar", out.getvalue())
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            self.assertEqual(cli.main(["outcome", "--key", "/nope.jsonl", "--control", "x",
                                       "--treatment", "y"]), 2)


if __name__ == "__main__":
    unittest.main()
