"""Direct regex-table tests for dsx/pct_base.py (audit L11).

The two regexes (``_REL_PCT_RE``, ``_BASE_NEAR_RE``) drive DSX-CLM-070 and
DSX-NAR-040; until now they were only exercised through those checks'
fixtures, so a regex edit could shift behaviour with no direct signal.

Run:  python3 -m unittest tests.test_pct_base -v
"""

from __future__ import annotations

import unittest

from dsx.pct_base import (
    claim_supplies_base,
    has_nearby_base_language,
    has_relative_percent,
    normalize_ws,
    relative_percent_without_base,
)

# (text, has_relative_percent, has_nearby_base_language)
TABLE = [
    # Relative percentages with no base.
    ("Activation rose 12%", True, False),
    ("Revenue grew by 3.5%", True, False),
    ("40% of users churned", True, False),
    ("rose 4 % week on week", True, False),
    # Relative percentages with a base nearby.
    ("Conversion increased 12% from 10.0% to 11.2%", True, True),
    ("Up 12% (n=4,000)", True, True),
    ("up 12% of 5,000 users", True, True),
    ("up 12% among 1,200 customers", True, True),
    ("base_n: 500, up 7%", True, True),
    ("denominator 800; fell 9%", True, True),
    # "out of N" forms: a numeric N is a base, a symbolic one is not.
    ("up 12%, 450 out of 3,750", True, True),
    ("up 12%, 450 out of N", True, False),
    # CI / confidence levels are not relative lifts.
    ("95% CI [1, 3]", False, False),
    ("a 95% confidence interval", False, False),
    ("90 % interval", False, False),
    ("12 %CI", False, False),
    # Percentage points are absolute differences, not relative ones.
    ("rose 3 percentage points", False, False),
    ("up 2.1 % pp", False, False),
    ("widened 2.1%, i.e. 2.1 pp", False, False),
    # Allocation targets are not lifts...
    ("ramped to 100%", False, False),
    ("allocated at 50%", False, False),
    # ...unless a change verb says they are.
    ("traffic rose to 50%", True, False),
    # Nothing to find.
    ("no numbers here", False, False),
    ("", False, False),
]


class TestRegexTable(unittest.TestCase):
    def test_has_relative_percent(self):
        for text, expected, _base in TABLE:
            with self.subTest(text=text):
                self.assertIs(expected, has_relative_percent(text))

    def test_has_nearby_base_language(self):
        for text, _rel, expected in TABLE:
            with self.subTest(text=text):
                self.assertIs(expected, has_nearby_base_language(text))

    def test_relative_percent_without_base_is_the_conjunction(self):
        for text, rel, base in TABLE:
            with self.subTest(text=text):
                self.assertIs(rel and not base, relative_percent_without_base(text))


class TestClaimSuppliesBase(unittest.TestCase):
    def test_claim_fields(self):
        cases = [
            (None, False),
            ({}, False),
            ({"base_n": 0}, True),  # zero is a (bad) base, not an absent one
            ({"base_n": 500}, True),
            ({"base_n": ""}, False),
            ({"base_n": None}, False),
            ({"from_value": 0, "to_value": 1}, True),
            ({"from_value": 1}, False),
            ({"to_value": 1}, False),
        ]
        for claim, expected in cases:
            with self.subTest(claim=claim):
                self.assertIs(expected, claim_supplies_base(claim))

    def test_claim_base_discharges_a_bare_relative_percent(self):
        self.assertTrue(relative_percent_without_base("rose 12%"))
        self.assertFalse(relative_percent_without_base("rose 12%", {"base_n": 500}))
        self.assertFalse(
            relative_percent_without_base("rose 12%", {"from_value": 0.1, "to_value": 0.112})
        )


class TestNormalizeWs(unittest.TestCase):
    def test_collapses_and_strips(self):
        self.assertEqual("a b", normalize_ws("  a \n\t b  "))
        self.assertEqual("", normalize_ws(""))
        self.assertEqual("", normalize_ws(None))


if __name__ == "__main__":
    unittest.main()
