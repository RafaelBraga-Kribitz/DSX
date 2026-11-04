"""The finding-code extractors key on the FIRST positional argument of
``report.add(...)`` only (audit L22).

``dsx/checks/ml.py`` writes other codes into free text ("DSX-ML-023 fired",
"DSX-ML-090 fired: missing ...") inside decision-record choices and could do
the same in a finding's title, detail or remedy. Neither the catalogue
generator (``scripts/gen-finding-catalogue.py::extract``) nor the suppression
vocabulary (``dsx/suppressions.py::known_codes``) may mint or mis-attribute a
code from such text.

Run:  python3 -m unittest tests.test_catalogue_extractor -v
"""

from __future__ import annotations

import importlib.util
import re
import tempfile
import unittest
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
_SCRIPT = _ROOT / "scripts" / "gen-finding-catalogue.py"
_CODE = re.compile(r"DSX-[A-Z]+-\d{3}")


def _load_script():
    spec = importlib.util.spec_from_file_location("gen_finding_catalogue_l22", _SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


g = _load_script()

_SOURCE = '''
def check(report, leaky, record_decision, DecisionRecord):
    report.add(
        "DSX-ZZ-001",
        "HIGH",
        f"DSX-ZZ-900 fired ({len(leaky)} step(s)); see DSX-ZZ-901",
        detail="Related: DSX-ZZ-902.",
        remedy="Fix DSX-ZZ-903 first.",
        where="spec.x",
    )
    report.add("DSX-ZZ-002", "LOW", "plain title mentioning DSX-ZZ-904")
    report.add(f"prefix DSX-ZZ-905", "LOW", "code arg is not a DSX- literal")
    report.add("not a code DSX-ZZ-906", "LOW", "first arg does not start with DSX-")
    record_decision(report, DecisionRecord(choice="DSX-ZZ-907 fired: missing a, b"))
    report.ok("DSX-ZZ-908 cleared")
'''


class TestExtractorIgnoresCodesInMessageText(unittest.TestCase):
    def test_only_first_positional_arg_codes_are_extracted(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "fake_check.py"
            path.write_text(_SOURCE, encoding="utf-8")
            rows = g.extract(path)
        self.assertEqual(["DSX-ZZ-001", "DSX-ZZ-002"], [code for code, _s, _t in rows])
        # The message text is kept verbatim as the title, never parsed for codes.
        self.assertEqual("DSX-ZZ-900 fired (<…> step(s)); see DSX-ZZ-901", rows[0][2])

    def test_real_tree_codes_equal_first_arg_literals(self):
        """Every catalogued code is some report.add call's first argument, and
        no code that appears only inside message or decision text (e.g. the
        ml.py "DSX-ML-023 fired" choice strings) gains a row of its own."""
        ml = _ROOT / "dsx" / "checks" / "ml.py"
        first_args = {code for code, _s, _t in g.extract(ml)}
        mentioned = set(_CODE.findall(ml.read_text(encoding="utf-8")))
        self.assertIn("DSX-ML-023", first_args)
        self.assertIn("DSX-ML-090", first_args)
        # Mentions are a superset; extraction never adds a code not emitted.
        self.assertLessEqual(first_args, mentioned)
        catalogue_codes = {row[0] for row in g.collect()}
        self.assertTrue(first_args <= catalogue_codes)

    def test_known_codes_uses_first_arg_only(self):
        from dsx.suppressions import known_codes

        known = known_codes()
        catalogue_codes = {row[0] for row in g.collect()}
        # The suppression vocabulary and the catalogue agree code for code, so
        # neither picked up a code from free text the other ignored.
        self.assertEqual(catalogue_codes, known)


if __name__ == "__main__":
    unittest.main()
