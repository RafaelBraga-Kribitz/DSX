"""Roadmap check 2026-08-20, item 6: field documentation stays true.

Three fields that the gate reads were undocumented where an operator looks:
``validity_frame.exclusions`` (template), ``model.selection_ledger`` and
``results.model_score_source`` / ``results.fold_scores`` (build-model skill and
the integrity auditor). These tests pin that the names appear, that the
commented ``exclusions`` example in the template is valid (no DSX-SPEC-083) and
fires DSX-VAL-080 only when its justification is blank, and that the accepted
values quoted in the skill match ``dsx/checks/ml.py``.

CRLF-tolerant: every split uses ``\\r?\\n``.

Run:  python -m unittest tests.test_field_documentation -v
"""

from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from dsx import spec as spec_mod  # noqa: E402
from dsx.checks import ml  # noqa: E402
from dsx.frame import val  # noqa: E402
from dsx.loader import load, loads  # noqa: E402

_LINE = re.compile(r"\r?\n")
_TEMPLATE = ROOT / "templates" / "ANALYSIS-SPEC.yaml"
_SKILL = ROOT / "skills" / "dsx-build-model" / "SKILL.md"
_AUDITOR = ROOT / "agents" / "dsx-ml-integrity-auditor.md"
_GOOD = ROOT / "examples" / "good-ANALYSIS-SPEC.yaml"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _documented_exclusions_example() -> dict:
    """Uncomment the ``# exclusions:`` block in the template and parse it."""
    lines = _LINE.split(_read(_TEMPLATE))
    start = next(i for i, ln in enumerate(lines) if ln.strip() == "# exclusions:")
    block = ["exclusions:"]
    for ln in lines[start + 1:]:
        m = re.match(r"^  #   (\S.*)$", ln)
        if not m:
            break
        block.append("  " + m.group(1))
    return loads("\n".join(block) + "\n", origin="template exclusions example")["exclusions"]


def _codes(report) -> set[str]:
    return {f.code for f in report.findings}


class TestFieldNamesAreDocumented(unittest.TestCase):
    def test_template_documents_exclusions_keys(self):
        text = _read(_TEMPLATE)
        for name in ("exclusions", "rule", "action", "applied_before_split", "justification",
                     "DSX-VAL-080", "DSX-SPEC-083"):
            with self.subTest(name=name):
                self.assertIn(name, text)

    def test_skill_documents_ledger_and_score_fields(self):
        text = _read(_SKILL)
        for name in ("model.selection_ledger", "candidates_evaluated", "configurations_tried",
                     "selected_on", "results.model_score_source", "results.fold_scores"):
            with self.subTest(name=name):
                self.assertIn(name, text)

    def test_skill_inputs_block_is_unchanged_in_keys(self):
        text = _read(_SKILL)
        m = re.search(r"<inputs>(.*?)</inputs>", text, re.DOTALL)
        self.assertIsNotNone(m)
        for forbidden in ("selection_ledger", "model_score_source", "fold_scores"):
            self.assertNotIn(forbidden, m.group(1))

    def test_skill_accepted_values_match_ml_py(self):
        text = _read(_SKILL)
        for value in ("cv_mean", "holdout", "nested_cv"):
            self.assertIn(value, ml.SCORE_SOURCES)
            self.assertIn(f"`{value}`", text)
        for value in sorted(ml.SELECTION_BASES):
            self.assertIn(f"`{value}`", text)

    def test_auditor_compares_code_with_declared_fields(self):
        flat = " ".join(_read(_AUDITOR).split())
        for name in ("model.selection_ledger", "results.model_score_source", "results.fold_scores"):
            with self.subTest(name=name):
                self.assertIn(name, flat)
        self.assertIn("compare the code", flat.lower())


class TestDocumentedExclusionsExample(unittest.TestCase):
    def _spec_with(self, exclusions) -> dict:
        spec = load(_GOOD)
        spec.setdefault("validity_frame", {})["exclusions"] = exclusions
        return spec

    def test_example_parses_with_the_four_documented_keys(self):
        example = _documented_exclusions_example()
        self.assertEqual(
            set(example), {"rule", "action", "applied_before_split", "justification"}
        )

    def test_example_produces_no_spec_083_and_no_val_080(self):
        spec = self._spec_with(_documented_exclusions_example())
        self.assertNotIn("DSX-SPEC-083", _codes(spec_mod.validate_structure(spec)))
        self.assertNotIn("DSX-VAL-080", _codes(val.check(spec)))

    def test_blank_justification_fires_val_080_only_then(self):
        example = dict(_documented_exclusions_example())
        example["justification"] = ""
        spec = self._spec_with(example)
        self.assertIn("DSX-VAL-080", _codes(val.check(spec)))
        self.assertNotIn("DSX-SPEC-083", _codes(spec_mod.validate_structure(spec)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
