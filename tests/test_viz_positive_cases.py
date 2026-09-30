"""Constructed positive and negative cases for every DSX-VIZ code (post-ship
audit escalation #2, .planning/POST-SHIP-AUDIT-2026-09.md).

The known-bad corpus (examples/known-bad/chart-*) already carries one gate-level
fixture per DSX-VIZ code. This module is the unit-level counterpart: for every
``DSX-VIZ-*`` code that ``dsx/checks/viz.py`` emits, it builds a minimal spec in
memory that makes the code fire (positive) and a near-miss spec that must NOT fire
it (negative), and calls ``viz.check`` directly. No gate, no filesystem.

The code list is read from viz.py's own source, so a code added to viz.py
without a case here fails ``test_every_emitted_code_has_a_case`` instead of
joining the never-constructed set the escalation was about.

Run:  python3 -m unittest tests.test_viz_positive_cases -v
"""

from __future__ import annotations

import copy
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from dsx.checks import viz  # noqa: E402

_VIZ_SOURCE = ROOT / "dsx" / "checks" / "viz.py"
_CODE_RE = re.compile(r'"(DSX-VIZ-\d{3})"')

# A visual that fires nothing: a sorted horizontal bar ranking with a zero
# baseline, a declared input type, a takeaway with a magnitude, units and source.
_CLEAN_VISUAL: dict = {
    "name": "Focused minutes per session by editor surface",
    "relationship": "ranking",
    "type": "horizontal_bar",
    "data_input_type": "categorical-value",
    "y_axis_starts_at_zero": True,
    "category_order": "by_value",
    "units": "minutes per session",
    "takeaway": "The document editor leads at 10.4 minutes; the spreadsheet trails at 4.1.",
    "source": "product_marts.fct_sessions, 2026-07-01..2026-07-14",
}

_DELETE = object()


def _visual(overrides: dict) -> dict:
    """The clean visual with ``overrides`` applied (``_DELETE`` removes a key)."""
    out = copy.deepcopy(_CLEAN_VISUAL)
    for key, value in overrides.items():
        if value is _DELETE:
            out.pop(key, None)
        else:
            out[key] = value
    return out


# code -> (expected severity, positive overrides, negative overrides). The
# negative is the closest near-miss that must stay silent for that code, so
# each pair tests the boundary, not only "defect vs perfect".
_CASES: dict[str, tuple[str, dict, dict]] = {
    "DSX-VIZ-001": ("HIGH", {"type": "radar", "relationship": "comparison"},
                    {"type": "bar", "relationship": "comparison"}),
    "DSX-VIZ-010": ("MEDIUM", {"relationship": _DELETE}, {"relationship": "ranking"}),
    "DSX-VIZ-011": ("MEDIUM", {"relationship": "vibes"}, {"relationship": "comparison"}),
    # A ranking relationship drawn as a line: declared, recognised, inadmissible.
    "DSX-VIZ-012": ("HIGH", {"type": "line", "data_input_type": "time-series",
                             "y_axis_starts_at_zero": _DELETE},
                    {"type": "dot_plot"}),
    # Both DSX-VIZ-013 branches: an unrecognised input type, and a recognised
    # one that does not admit the mark. The negative is an admitted pairing.
    "DSX-VIZ-013": ("HIGH", {"data_input_type": "not-a-type"},
                    {"data_input_type": "categorical-multi"}),
    "DSX-VIZ-014": ("MEDIUM", {"data_input_type": _DELETE},
                    {"data_input_type": "IT001"}),
    "DSX-VIZ-020": ("CRITICAL", {"y_axis_starts_at_zero": False, "y_axis_min": 40},
                    {"y_axis_starts_at_zero": True, "y_axis_min": 0}),
    "DSX-VIZ-021": ("LOW", {"y_axis_starts_at_zero": _DELETE},
                    {"type": "dot_plot", "y_axis_starts_at_zero": _DELETE}),
    "DSX-VIZ-030": ("HIGH", {"dual_axis": True}, {"dual_axis": False}),
    "DSX-VIZ-040": ("MEDIUM",
                    {"type": "pie", "relationship": "part_to_whole", "category_count": 9,
                     "category_order": _DELETE},
                    {"type": "pie", "relationship": "part_to_whole", "category_count": 5,
                     "category_order": _DELETE}),
    "DSX-VIZ-050": ("MEDIUM", {"color_count": 12}, {"color_count": 7}),
    "DSX-VIZ-051": ("HIGH", {"palette": "red_green"},
                    {"palette": "red_green", "redundant_encoding": True}),
    "DSX-VIZ-052": ("MEDIUM", {"scale_type": "rainbow"}, {"scale_type": "viridis"}),
    "DSX-VIZ-060": ("MEDIUM", {"takeaway": ""},
                    {"takeaway": "Editors lead by 6.3 minutes."}),
    "DSX-VIZ-061": ("HIGH", {"units": ""}, {"units": "minutes"}),
    "DSX-VIZ-062": ("LOW", {"source": _DELETE}, {"source": "warehouse, July 2026"}),
    "DSX-VIZ-063": ("HIGH", {"takeaway": _CLEAN_VISUAL["name"].upper()},
                    {"takeaway": "Document editor leads the ranking by 6.3 minutes"}),
    "DSX-VIZ-064": ("MEDIUM", {"takeaway": "The document editor is the one to watch"},
                    {"takeaway": "The document editor is ahead of the rest"}),
    "DSX-VIZ-070": ("HIGH", {"shows_estimates": True},
                    {"shows_estimates": True, "shows_uncertainty": True}),
    "DSX-VIZ-071": ("MEDIUM", {"uncertainty_mark": "spaghetti_band"},
                    {"uncertainty_mark": "half_eye"}),
    "DSX-VIZ-080": ("LOW", {"category_order": "alphabetical"},
                    {"category_order": "descending_value"}),
}


def _emitted_codes() -> set[str]:
    return set(_CODE_RE.findall(_VIZ_SOURCE.read_text(encoding="utf-8")))


def _findings(visual: dict) -> list:
    return viz.check({"visuals": [visual]}).findings


class TestVizPositiveCases(unittest.TestCase):
    def test_every_emitted_code_has_a_case(self):
        emitted = _emitted_codes()
        self.assertTrue(emitted, f"no DSX-VIZ codes found in {_VIZ_SOURCE}")
        self.assertEqual(
            emitted ^ set(_CASES), set(),
            "DSX-VIZ codes in dsx/checks/viz.py and the constructed cases here disagree: "
            f"{sorted(emitted ^ set(_CASES))} — add a positive/negative pair per code",
        )

    def test_clean_visual_fires_nothing(self):
        found = [(f.code, f.severity.label) for f in _findings(_CLEAN_VISUAL)]
        self.assertEqual(found, [], "the clean baseline visual must fire no finding")

    def test_each_code_fires_on_its_positive_case(self):
        for code, (severity, positive, _negative) in _CASES.items():
            with self.subTest(code=code):
                fired = {(f.code, f.severity.label) for f in _findings(_visual(positive))}
                self.assertIn(
                    (code, severity), fired,
                    f"{code} did not fire at {severity} on its constructed case; got "
                    f"{sorted(fired)}",
                )

    def test_each_code_stays_silent_on_its_negative_case(self):
        for code, (_severity, _positive, negative) in _CASES.items():
            with self.subTest(code=code):
                fired = {f.code for f in _findings(_visual(negative))}
                self.assertNotIn(
                    code, fired, f"{code} fired on its near-miss negative case: {sorted(fired)}"
                )

    def test_viz_013_fires_on_both_branches(self):
        # Unrecognised input type (above) and recognised-but-inadmissible here.
        fired = {f.code for f in _findings(_visual({"data_input_type": "single-value"}))}
        self.assertIn("DSX-VIZ-013", fired)

    def test_viz_063_blank_branch_also_emits_060(self):
        # A blank takeaway emits both codes from the one field (the corpus's
        # chart-takeaway-blank two-tier fixture pins the same pairing).
        fired = {f.code for f in _findings(_visual({"takeaway": "  "}))}
        self.assertLessEqual({"DSX-VIZ-060", "DSX-VIZ-063"}, fired)


if __name__ == "__main__":
    unittest.main()
