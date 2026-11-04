"""Tests for `dsx stats --inspect` — the decision-trail failure inspector.

Run:  python -m unittest tests.test_inspector -v
"""

from __future__ import annotations

import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dsx import cli
from dsx.decisions import DecisionRecord, InvocationHeader, append
from dsx.inspector import category_of, fired_codes, inspect_trails


def _seed(trail: Path, inv: str, digest: str, point: str, choices: list[tuple[str, bool]]) -> None:
    append(trail, InvocationHeader(invocation_id=inv, gate_point=point,
                                   dsx_version="test", frame_digest=digest))
    for n, (choice, escalate) in enumerate(choices, start=1):
        append(trail, DecisionRecord(id=f"DEC-{n:03d}", invocation_id=inv,
                                     layer="deterministic", choice=choice, escalate=escalate))


class FiredCodesTest(unittest.TestCase):
    def test_fired_and_cleared(self):
        self.assertEqual(fired_codes({"choice": "DSX-ML-041 fired: imbalance"}), ["DSX-ML-041"])
        self.assertEqual(fired_codes({"choice": "DSX-PRE-010 clear: one branch"}), [])
        self.assertEqual(fired_codes({"choice": "DSX-ADM-020 x", "escalate": True}), ["DSX-ADM-020"])
        self.assertEqual(fired_codes({"choice": "unit triad: passed"}), [])
        self.assertEqual(fired_codes({"choice": None}), [])

    def test_categories(self):
        self.assertEqual(category_of("DSX-SQL-003"), "data_joins_and_metrics")
        self.assertEqual(category_of("DSX-ML-041"), "ml_and_leakage")
        self.assertEqual(category_of("DSX-ZZZ-001"), "uncategorised")
        self.assertEqual(category_of("nothing"), "uncategorised")


class InspectTrailsTest(unittest.TestCase):
    def test_dedup_by_frame_and_recurring(self):
        with tempfile.TemporaryDirectory() as tmp:
            t1 = Path(tmp) / "p1" / "DECISIONS.jsonl"
            t2 = Path(tmp) / "p2" / "DECISIONS.jsonl"
            t1.parent.mkdir()
            t2.parent.mkdir()
            # Same frame run twice: DSX-SQL-003 counts once.
            _seed(t1, "INV-0001", "aaa", "plan", [("DSX-SQL-003 fired: fan-out", False)])
            _seed(t1, "INV-0002", "aaa", "ship", [("DSX-SQL-003 fired: fan-out", False),
                                                  ("DSX-CLM-011 fired: causal verb", True)])
            _seed(t2, "INV-0001", "bbb", "verify", [("DSX-SQL-003 fired: fan-out", False),
                                                    ("DSX-PRE-010 clear: ok", False)])
            _seed(t2, "INV-0002", "ccc", "plan", [("unit triad: passed", False)])
            res = inspect_trails([t1, t2])
        self.assertEqual(res["status"], "ok")
        self.assertEqual(res["distinct_frames"], 3)
        self.assertEqual(res["frames_with_a_fired_code"], 2)
        data = res["categories"]["data_joins_and_metrics"]
        self.assertEqual(data["frames"], 2)
        self.assertAlmostEqual(data["share_of_frames"], 2 / 3)
        self.assertEqual(data["top_codes"], [{"code": "DSX-SQL-003", "frames": 2}])
        self.assertEqual(res["categories"]["claims_and_reporting"]["escalations"], 1)
        self.assertNotIn("design_and_identification", res["categories"])
        self.assertEqual(
            res["recurring"],
            [{"code": "DSX-SQL-003", "category": "data_joins_and_metrics", "frames": 2,
              "gate_points": ["plan", "ship", "verify"]}],
        )

    def test_empty(self):
        self.assertEqual(inspect_trails([])["status"], "no_history")


class InspectCliTest(unittest.TestCase):
    def _capture(self, argv: list[str]) -> tuple[int, str]:
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = cli.main(argv)
        return code, out.getvalue()

    def test_cli_reads_operator_trails_and_skips_examples(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "phase").mkdir()
            (root / "examples").mkdir()
            _seed(root / "phase" / "DECISIONS.jsonl", "INV-0001", "aaa", "plan",
                  [("DSX-STA-001 fired: x", False)])
            _seed(root / "examples" / "DECISIONS.jsonl", "INV-0001", "zzz", "plan",
                  [("DSX-ML-001 fired: x", False)])
            code, text = self._capture(["stats", "--inspect", "--root", tmp, "--json"])
            self.assertEqual(code, 0)
            res = json.loads(text)["inspect"]
            self.assertEqual(res["distinct_frames"], 1)
            self.assertEqual(list(res["categories"]), ["statistical_inference"])
            code, text = self._capture(["stats", "--inspect", "--root", tmp])
            self.assertEqual(code, 0)
            self.assertIn("statistical_inference", text)

    def test_cli_no_history(self):
        with tempfile.TemporaryDirectory() as tmp:
            code, text = self._capture(["stats", "--inspect", "--root", tmp])
        self.assertEqual(code, 0)
        self.assertIn("no operator history yet", text)

    def test_default_report_unchanged(self):
        with tempfile.TemporaryDirectory() as tmp:
            _, text = self._capture(["stats", "--root", tmp, "--json"])
        self.assertNotIn("inspect", json.loads(text))


if __name__ == "__main__":
    unittest.main()
