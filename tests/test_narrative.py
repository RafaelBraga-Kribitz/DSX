"""Unit tests for dsx/checks/narrative.py — one positive and one negative case
per DSX-NAR code, the ship-only DSX-NAR-001 branch, and the optional
FORBIDDEN-CLAIMS pattern file's failure paths (audit L21, L67).

Run:  python3 -m unittest tests.test_narrative -v
"""

from __future__ import annotations

import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from dsx.checks import narrative

CLAIM = "Onboarding checklist users activated 1.4 pp more often within 7 days."


def _spec(**sections) -> dict:
    spec: dict = {"claims": [{"text": CLAIM}]}
    spec.update(sections)
    return spec


class _Base(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def write(self, name: str, text: str) -> None:
        (self.root / name).write_text(text, encoding="utf-8")

    def run_check(self, spec: dict, gate_point: str | None = None):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            report = narrative.check(spec, str(self.root), gate_point=gate_point)
        return report, stderr.getvalue()

    def codes(self, spec: dict, gate_point: str | None = None) -> list[str]:
        return [f.code for f in self.run_check(spec, gate_point)[0].findings]


class TestNar001MissingPathAtShip(_Base):
    def test_fires_at_ship_when_claims_have_no_narrative_path(self):
        self.assertIn("DSX-NAR-001", self.codes(_spec(), gate_point="ship"))

    def test_ship_only_silent_at_every_other_gate_point(self):
        for point in (None, "plan", "execute", "verify"):
            with self.subTest(point=point):
                self.assertNotIn("DSX-NAR-001", self.codes(_spec(), gate_point=point))

    def test_silent_at_ship_when_no_claims(self):
        self.assertNotIn("DSX-NAR-001", self.codes({"claims": []}, gate_point="ship"))

    def test_silent_at_ship_when_path_declared(self):
        self.write("NARRATIVE.md", CLAIM)
        spec = _spec(narrative={"path": "NARRATIVE.md"})
        self.assertNotIn("DSX-NAR-001", self.codes(spec, gate_point="ship"))


class TestNar010PathMissing(_Base):
    def test_fires_when_declared_path_does_not_exist(self):
        spec = _spec(narrative={"path": "NOPE.md"})
        self.assertIn("DSX-NAR-010", self.codes(spec))

    def test_silent_when_path_exists(self):
        self.write("NARRATIVE.md", CLAIM)
        spec = _spec(narrative={"path": "NARRATIVE.md"})
        self.assertNotIn("DSX-NAR-010", self.codes(spec))


class TestNar020ClaimMissingFromNarrative(_Base):
    def test_fires_when_claim_text_absent(self):
        self.write("NARRATIVE.md", "An unrelated paragraph.")
        spec = _spec(narrative={"path": "NARRATIVE.md"})
        self.assertIn("DSX-NAR-020", self.codes(spec))

    def test_silent_when_claim_present_modulo_whitespace(self):
        self.write("NARRATIVE.md", "# Result\n\n" + CLAIM.replace(" ", "\n  ", 3) + "\n")
        spec = _spec(narrative={"path": "NARRATIVE.md"})
        self.assertNotIn("DSX-NAR-020", self.codes(spec))


class TestNar030ForbiddenWording(_Base):
    def test_fires_on_universal_pattern_in_narrative(self):
        self.write("NARRATIVE.md", CLAIM + "\nThe data proves the checklist works.")
        spec = _spec(narrative={"path": "NARRATIVE.md"})
        self.assertIn("DSX-NAR-030", self.codes(spec))

    def test_fires_on_universal_pattern_in_claim_text(self):
        spec = {"claims": [{"text": "We know this with high confidence."}]}
        self.assertIn("DSX-NAR-030", self.codes(spec))

    def test_silent_on_negated_correction(self):
        spec = {"claims": [{"text": "The data does not prove causation."}]}
        self.assertNotIn("DSX-NAR-030", self.codes(spec))

    def test_phase_local_pattern_file_adds_patterns(self):
        self.write(
            "FORBIDDEN-CLAIMS.yaml",
            "patterns:\n  - id: guaranteed\n    regex: '(?i)guaranteed'\n",
        )
        spec = {"claims": [{"text": "Uplift is guaranteed."}]}
        report, err = self.run_check(spec)
        hits = [f for f in report.findings if f.code == "DSX-NAR-030"]
        self.assertEqual(["guaranteed"], [f.data.get("pattern_id") for f in hits])
        self.assertEqual("", err)


class TestNar040RelativePercentWithoutBase(_Base):
    def test_fires_on_bare_relative_percent(self):
        self.write("NARRATIVE.md", CLAIM + "\nRevenue rose 12% after launch.")
        spec = _spec(narrative={"path": "NARRATIVE.md"})
        self.assertIn("DSX-NAR-040", self.codes(spec))

    def test_silent_when_base_is_stated(self):
        self.write("NARRATIVE.md", CLAIM + "\nRevenue rose 12% (n=4,000).")
        spec = _spec(narrative={"path": "NARRATIVE.md"})
        self.assertNotIn("DSX-NAR-040", self.codes(spec))


class TestNar050DashboardPath(_Base):
    def test_fires_when_dashboard_path_missing(self):
        self.assertIn("DSX-NAR-050", self.codes({"dashboard": {"path": "dash/README.md"}}))

    def test_silent_when_dashboard_path_exists(self):
        self.write("DASHBOARD.md", "# Dashboard")
        self.assertNotIn("DSX-NAR-050", self.codes({"dashboard": {"path": "DASHBOARD.md"}}))

    def test_silent_when_no_dashboard_declared(self):
        self.assertNotIn("DSX-NAR-050", self.codes({}))


class TestBrokenPatternFile(_Base):
    """A broken optional pattern file is non-fatal, but no longer invisible."""

    def _assert_universal_pack_still_applies(self, err_fragment: str) -> None:
        spec = {"claims": [{"text": "The data proves it."}, {"text": "with high confidence"}]}
        report, err = self.run_check(spec)
        self.assertIn("DSX-NAR-030", [f.code for f in report.findings])
        self.assertIn("FORBIDDEN-CLAIMS.yaml", err)
        self.assertIn(err_fragment, err)
        # Loaded once per check, so the warning prints once — not once per claim.
        self.assertEqual(1, err.count("dsx: warning:"))

    def test_unparseable_file_warns_and_is_skipped(self):
        self.write("FORBIDDEN-CLAIMS.yaml", "patterns: [unclosed\n  - : :\n")
        self._assert_universal_pack_still_applies("could not be parsed")

    def test_non_mapping_file_warns_and_is_skipped(self):
        self.write("FORBIDDEN-CLAIMS.yaml", "- just\n- a list\n")
        self._assert_universal_pack_still_applies("is not a mapping")

    def test_invalid_regex_entry_warns_and_is_skipped(self):
        self.write(
            "FORBIDDEN-CLAIMS.yaml",
            "patterns:\n  - id: broken\n    regex: '(unclosed'\n",
        )
        self._assert_universal_pack_still_applies("'broken' is not a valid regex")

    def test_valid_file_prints_nothing(self):
        self.write("FORBIDDEN-CLAIMS.yaml", "patterns: []\n")
        _report, err = self.run_check({"claims": [{"text": "fine"}]})
        self.assertEqual("", err)


if __name__ == "__main__":
    unittest.main()
