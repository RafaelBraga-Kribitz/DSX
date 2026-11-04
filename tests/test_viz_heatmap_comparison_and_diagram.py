"""Two vocabulary gaps in ``dsx check viz`` (DSX-VIZ-012, DSX-VIZ-010/064/061).

1. ``heatmap`` is admitted under the ``comparison`` relationship for
   ``grouped-categorical`` input (a group x category table of values), and for no
   other input type. The relationship list and the input-type matrix agree.
2. ``visual_kind: diagram`` declares a figure with no data. It is exempt from
   DSX-VIZ-010, DSX-VIZ-064 and DSX-VIZ-061 and from nothing else, and a figure
   that carries data fields cannot use it to skip those checks.

Run: python -m unittest tests.test_viz_heatmap_comparison_and_diagram -v
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from dsx.checks import figures as figures_check
from dsx.checks import viz
from dsx.input_types import permitted
from dsx.spec import VISUAL_KINDS, describe_vocabulary

_SHARES = {
    "name": "Skill share by role family",
    "relationship": "comparison",
    "type": "heatmap",
    "data_input_type": "grouped-categorical",
    "units": "% of postings of each role family",
    "takeaway": "BI names visualisation most (86%), data science AI wording (82%).",
    "source": "T05, 2026-11-04",
}

_FLOW = {
    "name": "Module flow",
    "visual_kind": "diagram",
    "takeaway": "Modules run in order and each ends in its own check.",
    "source": "project structure",
}


def _codes(visual: dict) -> list[str]:
    return [f.code for f in viz.check({"visuals": [visual]}).findings]


def _with(base: dict, **changes) -> dict:
    out = dict(base)
    out.update(changes)
    return out


class TestHeatmapUnderComparison(unittest.TestCase):
    def test_grouped_categorical_comparison_heatmap_passes(self):
        self.assertEqual(_codes(_SHARES), [])

    def test_inventory_id_of_the_grouped_categorical_family_passes(self):
        # IT006 is a grouped-categorical shape in the input-type inventory.
        self.assertEqual(_codes(_with(_SHARES, data_input_type="IT006")), [])

    def test_comparison_heatmap_on_another_input_type_still_fails(self):
        # trivariate admits heatmap in the matrix, but not as a comparison.
        codes = _codes(_with(_SHARES, data_input_type="trivariate"))
        self.assertEqual(codes, ["DSX-VIZ-012"])

    def test_comparison_heatmap_without_input_type_fails(self):
        codes = _codes({k: v for k, v in _SHARES.items() if k != "data_input_type"})
        self.assertIn("DSX-VIZ-012", codes)

    def test_heatmap_under_a_relationship_that_does_not_allow_it_still_fails(self):
        for relationship in ("trend", "ranking", "part_to_whole", "distribution"):
            with self.subTest(relationship=relationship):
                codes = _codes(_with(_SHARES, relationship=relationship))
                self.assertIn("DSX-VIZ-012", codes)

    def test_correlation_heatmap_is_unchanged(self):
        visual = _with(_SHARES, relationship="correlation", data_input_type="matrix")
        self.assertEqual(_codes(visual), [])

    def test_other_comparison_marks_are_unchanged(self):
        self.assertIn("DSX-VIZ-012", _codes(_with(_SHARES, type="line", data_input_type="time-series")))

    def test_charts_lookup_agrees_with_the_gate(self):
        self.assertIn("heatmap", permitted("grouped-categorical", "comparison"))
        self.assertIn("heatmap", permitted("IT006", "comparison"))
        # No narrowing for other shapes: the comparison list gives them no mark but
        # heatmap, and the gate removes it, so the lookup falls back to the shape's
        # own set (its documented empty-intersection behaviour), not a heatmap pick.
        self.assertEqual(permitted("trivariate", "comparison"), permitted("trivariate"))
        self.assertEqual(permitted("matrix", "comparison"), permitted("matrix"))
        self.assertEqual(
            permitted("grouped-categorical", "comparison"),
            ["bar", "dot_plot", "heatmap", "horizontal_bar"],
        )
        # The correlation reading keeps its marks.
        self.assertIn("heatmap", permitted("trivariate", "correlation"))


class TestDiagramDeclaration(unittest.TestCase):
    def test_diagram_passes_viz_010_064_and_061(self):
        # No relationship, no units, and a takeaway with no digit or comparison word.
        codes = _codes(_FLOW)
        for code in ("DSX-VIZ-010", "DSX-VIZ-064", "DSX-VIZ-061"):
            self.assertNotIn(code, codes)
        self.assertEqual(codes, [])

    def test_same_figure_without_the_declaration_gets_all_three(self):
        visual = {k: v for k, v in _FLOW.items() if k != "visual_kind"}
        codes = _codes(visual)
        for code in ("DSX-VIZ-010", "DSX-VIZ-064", "DSX-VIZ-061"):
            self.assertIn(code, codes)

    def test_normal_figure_without_relationship_still_gets_viz_010(self):
        visual = {k: v for k, v in _SHARES.items() if k != "relationship"}
        self.assertIn("DSX-VIZ-010", _codes(visual))

    def test_visual_kind_data_is_the_default_and_exempts_nothing(self):
        visual = {k: v for k, v in _FLOW.items() if k != "visual_kind"}
        codes = _codes(_with(visual, visual_kind="data"))
        self.assertEqual(codes, _codes(visual))
        self.assertIn("DSX-VIZ-010", codes)

    def test_data_figure_cannot_use_the_exemption(self):
        data_fields = {
            "relationship": "comparison",
            "data_input_type": "categorical-value",
            "y_axis": "share",
            "y_axis_min": 10,
            "y_axis_starts_at_zero": True,
            "dual_axis": True,
            "shows_estimates": True,
            "shows_uncertainty": True,
            "uncertainty_mark": "error_bars",
            "category_count": 5,
        }
        for field, value in data_fields.items():
            with self.subTest(field=field):
                # A bare name and a takeaway with no digit: every exempt check
                # would fire on a data figure.
                visual = _with(_FLOW, **{field: value})
                findings = viz.check({"visuals": [visual]}).findings
                guard = [f for f in findings if f.code == "DSX-VIZ-015"]
                self.assertEqual(len(guard), 1)
                self.assertEqual(guard[0].severity.name, "HIGH")
                self.assertIn(field, guard[0].detail)
                # The exemption is void: the three exempt checks fire as for any figure.
                codes = {f.code for f in findings}
                self.assertIn("DSX-VIZ-064", codes)
                self.assertIn("DSX-VIZ-061", codes)

    def test_false_flags_are_not_data(self):
        visual = _with(_FLOW, dual_axis=False, shows_estimates=False, shows_uncertainty=False)
        self.assertEqual(_codes(visual), [])

    def test_unrecognised_visual_kind_fails_and_exempts_nothing(self):
        findings = viz.check({"visuals": [_with(_FLOW, visual_kind="picture")]}).findings
        codes = {f.code for f in findings}
        self.assertIn("DSX-VIZ-015", codes)
        self.assertIn("DSX-VIZ-010", codes)
        self.assertIn("DSX-VIZ-064", codes)

    def test_diagram_still_needs_a_takeaway(self):
        codes = _codes({k: v for k, v in _FLOW.items() if k != "takeaway"})
        self.assertIn("DSX-VIZ-060", codes)
        self.assertIn("DSX-VIZ-063", codes)

    def test_diagram_takeaway_equal_to_name_still_fails(self):
        codes = _codes(_with(_FLOW, takeaway=_FLOW["name"]))
        self.assertIn("DSX-VIZ-063", codes)

    def test_diagram_still_gets_the_banned_type_check(self):
        self.assertIn("DSX-VIZ-001", _codes(_with(_FLOW, type="radar")))

    def test_diagram_still_gets_source_note_check(self):
        codes = _codes({k: v for k, v in _FLOW.items() if k != "source"})
        self.assertIn("DSX-VIZ-062", codes)

    def test_diagram_still_needs_its_seal(self):
        # The exemption lives in viz.py; the figures check never reads visual_kind.
        with tempfile.TemporaryDirectory() as tmp:
            svg = Path(tmp) / "flow.svg"
            svg.write_text("<svg/>", encoding="utf-8")
            wrong = _with(
                _FLOW, artifact_path=str(svg), svg_sha256="sha256:" + "0" * 64, renderer="other"
            )
            report = figures_check.check({"visuals": [wrong]}, phase_dir=tmp)
            self.assertIn("DSX-FIG-010", [f.code for f in report.findings])
            unsealed = _with(_FLOW, artifact_path=str(svg), renderer="other")
            report = figures_check.check({"visuals": [unsealed]}, phase_dir=tmp, strict=True)
            self.assertIn("DSX-FIG-011", [f.code for f in report.findings])
        glyph = _with(_FLOW, renderer="glyph")
        report = figures_check.check({"visuals": [glyph]})
        self.assertIn("DSX-FIG-020", [f.code for f in report.findings])

    def test_visual_kind_is_a_published_closed_vocabulary(self):
        self.assertEqual(set(VISUAL_KINDS), {"data", "diagram"})
        self.assertIn("visual_kinds", describe_vocabulary())


if __name__ == "__main__":
    unittest.main()
