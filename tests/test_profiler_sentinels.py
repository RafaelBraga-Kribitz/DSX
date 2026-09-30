"""Profiler sentinel matching and the two edge-case numeric fixtures
(2026-09-30 audit items H1, L8, L13, M22/M38).

- One matching cell counts once per sentinel key: an exact string match no
  longer also fires the numeric-comparison fallback (H1, L8).
- `sentinels_found` keys are the raw strings the user typed; numeric
  equivalents in the data (`-1.0` for `-1`) still match (L13).
- `numeric_n1.csv` and `numeric_zeros_negatives.csv` are profiled through
  `profile_csv`, against hand-computed values (M22/M38).

Run:  python3 -m unittest tests.test_profiler_sentinels -v
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
from dsx.profiler import _sentinel_matches, _sentinel_number, profile_csv

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "profiler"


def _numbers(*keys: str) -> dict[str, float | None]:
    return {k: _sentinel_number(k) for k in keys}


class TestSentinelMatches(unittest.TestCase):
    def test_exact_numeric_match_counts_once(self):
        # Before the fix, '-1' matched literally AND via isclose: two hits.
        self.assertEqual(_sentinel_matches("-1", _numbers("-1")), ["-1"])

    def test_numeric_equivalent_matches_under_the_raw_key(self):
        self.assertEqual(_sentinel_matches("-1.0", _numbers("-1")), ["-1"])
        self.assertEqual(_sentinel_matches("-1", _numbers("-1.0")), ["-1.0"])
        self.assertEqual(_sentinel_matches("1000", _numbers("1e3")), ["1e3"])

    def test_two_equal_keys_each_match_once(self):
        self.assertEqual(_sentinel_matches("-1", _numbers("-1", "-1.0")), ["-1", "-1.0"])

    def test_string_sentinel_is_exact_only(self):
        self.assertEqual(_sentinel_matches("UNKNOWN", _numbers("UNKNOWN")), ["UNKNOWN"])
        self.assertEqual(_sentinel_matches("unknown", _numbers("UNKNOWN")), [])

    def test_float_only_spellings_are_not_numbers(self):
        # float() accepts these; a sentinel comparison must not.
        self.assertIsNone(_sentinel_number("1_000"))
        self.assertIsNone(_sentinel_number("inf"))
        self.assertIsNone(_sentinel_number("nan"))
        self.assertEqual(_sentinel_matches("1_000", _numbers("1000")), [])

    def test_non_match(self):
        self.assertEqual(_sentinel_matches("3", _numbers("-1", "abc")), [])


class TestSentinelsThroughProfile(unittest.TestCase):
    CSV = "x,y\n-1,abc\n-1.0,ok\n3,ok\n1000,ok\n1_000,ok\n"

    def _profile(self, sentinels):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "s.csv"
            path.write_text(self.CSV, encoding="utf-8")
            return profile_csv(path, sentinels=sentinels)

    def test_keys_are_the_raw_strings(self):
        self.assertEqual(self._profile(["-1"])["sentinels_found"], ["-1"])
        self.assertEqual(self._profile(["-1.0"])["sentinels_found"], ["-1.0"])
        self.assertEqual(self._profile(["1e3"])["sentinels_found"], ["1e3"])
        self.assertEqual(self._profile(["abc", "zzz"])["sentinels_found"], ["abc"])

    def test_programmatic_numbers_still_work(self):
        self.assertEqual(self._profile([-1])["sentinels_found"], ["-1"])

    def test_cli_reports_what_the_user_typed(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "s.csv"
            path.write_text(self.CSV, encoding="utf-8")
            out, err = io.StringIO(), io.StringIO()
            with redirect_stdout(out), redirect_stderr(err):
                code = cli.main(
                    [
                        "profile", str(path), "--out", str(Path(tmp) / "p.yaml"),
                        "--sentinel=-1.0", "--sentinel=1e3", "--json",
                    ]
                )
            self.assertEqual(code, 0, err.getvalue())
            summary = json.loads(out.getvalue())
            self.assertEqual(summary["sentinels_found"], ["-1.0", "1e3"])


class TestEdgeFixtures(unittest.TestCase):
    def test_numeric_n1(self):
        # value = 7, one row: every quantile is 7, sd is undefined (null).
        profile = profile_csv(FIXTURES / "numeric_n1.csv")
        self.assertEqual(profile["row_count"], 1)
        col = profile["columns"]["value"]
        self.assertEqual(col["dtype"], "integer")
        self.assertEqual(col["null_rate"], 0.0)
        self.assertEqual(col["n_unique"], 1)
        self.assertNotIn("categorical", col)
        self.assertEqual(
            col["numeric"],
            {
                "min": 7.0, "q1": 7.0, "median": 7.0, "q3": 7.0, "max": 7.0,
                "mean": 7.0, "sd": None, "n_zero": 0, "n_negative": 0, "n": 1,
            },
        )

    def test_numeric_zeros_negatives(self):
        # Cells: -2.0, -0, 0, 0.0, 5. Integers and floats mixed -> dtype float.
        # -0 is a zero, not a negative: n_zero = 3, n_negative = 1.
        # Sorted: -2, 0, 0, 0, 5; type-7 quantiles land on indices 1, 2, 3 -> 0.
        # mean = 3 / 5 = 0.6; squared deviations 6.76 + 3 * 0.36 + 19.36 = 27.2,
        # / (n - 1) = 6.8, sd = sqrt(6.8).
        profile = profile_csv(FIXTURES / "numeric_zeros_negatives.csv")
        self.assertEqual(profile["row_count"], 5)
        col = profile["columns"]["value"]
        self.assertEqual(col["dtype"], "float")
        self.assertEqual(col["n_unique"], 5)
        self.assertNotIn("categorical", col)
        num = col["numeric"]
        self.assertEqual(num["n"], 5)
        self.assertEqual(num["n_zero"], 3)
        self.assertEqual(num["n_negative"], 1)
        self.assertEqual(num["min"], -2.0)
        self.assertEqual(num["max"], 5.0)
        self.assertEqual((num["q1"], num["median"], num["q3"]), (0.0, 0.0, 0.0))
        self.assertAlmostEqual(num["mean"], 0.6, places=12)
        self.assertAlmostEqual(num["sd"], math.sqrt(6.8), places=12)


if __name__ == "__main__":
    unittest.main()
