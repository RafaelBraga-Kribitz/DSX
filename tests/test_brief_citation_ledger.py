"""brief.md section 7 keeps the citation ledger it was extended with (D-17).

Regression guard folded in from the retired one-shot verifier
``scripts/check_brief_refs.py`` (v2.0.0 phase 07, 07-02-PLAN task 1), so the
unittest run in scripts/check.sh and CI now covers it:

1. Section 7 names each required source (six added, the re-pinned/re-cited
   existing entries).
2. "unverified" appears at least three times — the Kish section locator, the
   Gelman/Simpson/Betancourt typeset-version caveat and the Gelman and Hill
   chapter locator are flagged, not asserted.
3. Lohr and Little and Rubin are each pinned to their third edition, near the
   entry itself rather than anywhere in the section.
4. "Conley" is absent: Conley (1999) was deliberately excluded because only a
   training-knowledge attribution was available for it.

The extraction tolerates CRLF line endings (a Windows checkout).
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRIEF = ROOT / "brief.md"

REQUIRED_SUBSTRINGS = (
    "E9(R1)",
    "Hernan and Robins (2016)",
    "Popper",
    "Kish (1965)",
    "Cochrane Handbook",
    "Cronbach and Meehl (1955)",
    "Lohr (2021)",
    "Little and Rubin (2019)",
    "White and Carlin (2010)",
    "Cameron and Miller (2015)",
)
FORBIDDEN_SUBSTRINGS = ("Conley",)
MIN_UNVERIFIED_COUNT = 3
# The edition marker must sit near the entry it pins; one edition anywhere in
# the section would otherwise vouch for both.
EDITION_WINDOW = 250


def section_7() -> str:
    """Body of '## 7. Reference sources' up to the next '---', whitespace-collapsed.

    The brief hard-wraps flowing paragraphs, so a citation can straddle a line
    break ("White and\\nCarlin (2010)"); collapsing runs of whitespace keeps the
    wrap from reading as missing content.
    """
    text = BRIEF.read_text(encoding="utf-8")
    match = re.search(r"##\s*7\.\s*Reference sources\r?\n\r?\n(.*?)\r?\n\r?\n---", text, re.DOTALL)
    if match is None:
        raise AssertionError("could not locate '## 7. Reference sources' in brief.md")
    return re.sub(r"\s+", " ", match.group(1))


class TestBriefCitationLedger(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.section = section_7()

    def test_required_sources_present(self):
        missing = [s for s in REQUIRED_SUBSTRINGS if s not in self.section]
        self.assertEqual(missing, [], f"brief.md section 7 lost citations: {missing}")

    def test_excluded_sources_absent(self):
        present = [s for s in FORBIDDEN_SUBSTRINGS if s in self.section]
        self.assertEqual(present, [], f"brief.md section 7 cites excluded sources: {present}")

    def test_unverified_locators_flagged(self):
        count = self.section.count("unverified")
        self.assertGreaterEqual(
            count, MIN_UNVERIFIED_COUNT,
            f"'unverified' appears {count} times in section 7, need >= {MIN_UNVERIFIED_COUNT}",
        )

    def test_third_editions_pinned_near_their_entries(self):
        for needle in ("Lohr (2021)", "Little and Rubin (2019)"):
            with self.subTest(entry=needle):
                pos = self.section.find(needle)
                self.assertNotEqual(pos, -1, f"{needle} missing")
                nearby = self.section[pos:pos + EDITION_WINDOW]
                self.assertTrue(
                    "3rd ed." in nearby or "third edition" in nearby,
                    f"no '3rd ed.' / 'third edition' within {EDITION_WINDOW} chars of {needle}",
                )


if __name__ == "__main__":
    unittest.main()
