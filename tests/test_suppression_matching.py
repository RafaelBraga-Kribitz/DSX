"""Suppression matching and bad-row surfacing (audit L37, M20).

L37: a suppression's ``chart_id`` matches a finding's ``where`` only as a whole
identifier token, never as a bare substring.

M20: DSX-SPEC-071 (invalid shape) and DSX-SPEC-072 (unknown code) are reachable
through the CLI: when the ``spec`` check ran, ``apply_suppressions`` skips the
bad row and the catalogued finding fails the gate (exit 1); when it did not,
the row still aborts the run (exit 2).

Run:  python3 -m unittest tests.test_suppression_matching -v
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from dsx.findings import CheckError, Report
from dsx.suppressions import _contains_token, apply_suppressions

ROOT = Path(__file__).resolve().parent.parent


def _report(*findings: tuple[str, str, str]) -> Report:
    report = Report(check="t")
    for code, title, where in findings:
        report.add(code, "HIGH", title, where=where)
    return report


def _row(code: str, chart_id: str | None = None) -> dict:
    row = {"code": code, "reason": "accepted by ADR", "authority": "docs/ADR-1.md"}
    if chart_id is not None:
        row["chart_id"] = chart_id
    return row


class TestChartIdTokenMatch(unittest.TestCase):
    def test_short_chart_id_does_not_substring_match(self):
        # 'fig' is a substring of 'spec.figures[0]' and 'a' of almost anything;
        # neither row targets this finding, so it must survive.
        report = _report(("DSX-VIZ-030", "dual axis", "spec.figures[0].dual_axis"))
        for chart_id in ("fig", "a", "dual"):
            with self.subTest(chart_id=chart_id):
                out = apply_suppressions(
                    {"suppressions": [_row("DSX-VIZ-030", chart_id)]}, report
                )
                self.assertEqual(["DSX-VIZ-030"], [f.code for f in out.findings])

    def test_chart_id_as_whole_token_still_matches(self):
        report = _report(("DSX-VIZ-030", "dual axis", "chart a3_vol.dual_axis"))
        out = apply_suppressions({"suppressions": [_row("DSX-VIZ-030", "a3_vol")]}, report)
        self.assertEqual([], out.findings)
        self.assertEqual(1, len(out.context["suppressions_applied"]))

    def test_prefix_of_a_longer_chart_id_does_not_match(self):
        report = _report(("DSX-VIZ-030", "dual axis", "chart a3_vol_weekly.dual_axis"))
        out = apply_suppressions({"suppressions": [_row("DSX-VIZ-030", "a3_vol")]}, report)
        self.assertEqual(["DSX-VIZ-030"], [f.code for f in out.findings])

    def test_visual_index_match_still_works(self):
        spec = {
            "visuals": [{"chart_id": "c1", "name": "Revenue"}],
            "suppressions": [_row("DSX-VIZ-030", "c1")],
        }
        report = _report(("DSX-VIZ-030", "dual axis", "spec.visuals[0].dual_axis"))
        self.assertEqual([], apply_suppressions(spec, report).findings)

    def test_contains_token_table(self):
        cases = [
            ("chart fig.svg", "fig", True),
            ("spec.figures[0]", "fig", False),
            ("x-fig", "fig", False),
            ("fig_2", "fig", False),
            ("[fig]", "fig", True),
            ("anything", "", False),
        ]
        for text, token, expected in cases:
            with self.subTest(text=text, token=token):
                self.assertIs(expected, _contains_token(text, token))


class TestBadRowSurfacing(unittest.TestCase):
    def test_unknown_code_skipped_when_spec_check_reported_it(self):
        report = _report(
            ("DSX-SPEC-072", "unknown", "spec.suppressions[0].code"),
            ("DSX-VIZ-030", "dual axis", "spec.visuals[0].dual_axis"),
        )
        out = apply_suppressions({"suppressions": [_row("DSX-FAKE-999")]}, report)
        self.assertEqual(["DSX-SPEC-072", "DSX-VIZ-030"], [f.code for f in out.findings])

    def test_invalid_shape_skipped_when_spec_check_reported_it(self):
        report = _report(("DSX-SPEC-071", "bad shape", "spec.suppressions[0].code"))
        out = apply_suppressions({"suppressions": [_row("not-a-code")]}, report)
        self.assertEqual(["DSX-SPEC-071"], [f.code for f in out.findings])

    def test_unknown_code_raises_without_spec_check(self):
        with self.assertRaises(CheckError):
            apply_suppressions({"suppressions": [_row("DSX-FAKE-999")]}, Report(check="t"))

    def test_invalid_shape_raises_without_spec_check(self):
        with self.assertRaisesRegex(CheckError, "invalid shape"):
            apply_suppressions({"suppressions": [_row("nope")]}, Report(check="t"))

    def test_finding_for_another_row_does_not_excuse_this_row(self):
        report = _report(("DSX-SPEC-072", "unknown", "spec.suppressions[0].code"))
        spec = {"suppressions": [_row("DSX-FAKE-999"), _row("DSX-FAKE-998")]}
        with self.assertRaisesRegex(CheckError, r"suppressions\[1\]"):
            apply_suppressions(spec, report)

    def test_spec_072_cannot_itself_be_suppressed(self):
        report = _report(("DSX-SPEC-072", "unknown", "spec.suppressions[0].code"))
        spec = {"suppressions": [_row("DSX-FAKE-999"), _row("DSX-SPEC-072")]}
        out = apply_suppressions(spec, report)
        self.assertEqual(["DSX-SPEC-072"], [f.code for f in out.findings])


class TestAuditCli(unittest.TestCase):
    """End to end: ``dsx audit`` on the good example plus one bad suppression row."""

    def _audit(self, extra_yaml: str) -> subprocess.CompletedProcess:
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, True)
        examples = tmp / "examples"
        shutil.copytree(ROOT / "examples", examples)
        spec = examples / "good-ANALYSIS-SPEC.yaml"
        spec.write_text(spec.read_text(encoding="utf-8") + extra_yaml, encoding="utf-8")
        return subprocess.run(
            [sys.executable, "-m", "dsx", "audit", "--spec", str(spec), "--json"],
            cwd=str(tmp),
            env={**os.environ, "PYTHONPATH": str(ROOT)},
            capture_output=True,
            text=True,
            check=False,
        )

    def test_unknown_suppression_code_reports_spec_072_exit_1(self):
        proc = self._audit(
            "\nsuppressions:\n"
            "  - code: DSX-FAKE-999\n"
            "    reason: \"typo in the code\"\n"
            "    authority: \"docs/ADR-1.md\"\n"
        )
        self.assertEqual(1, proc.returncode, proc.stderr)
        # A blocking report's JSON goes to stderr, a passing one's to stdout.
        payload = json.loads(proc.stdout.strip() or proc.stderr)
        codes = [f["code"] for f in payload["findings"]]
        self.assertIn("DSX-SPEC-072", codes)

    def test_good_example_baseline_passes(self):
        proc = self._audit("")
        self.assertEqual(0, proc.returncode, proc.stdout + proc.stderr)


if __name__ == "__main__":
    unittest.main()
