"""DSX-REP-040 reads the declared notebook's execution counts (SEED-003 AC-01, audit H4).

A ``runs_clean_top_to_bottom: true`` declaration is contradicted by the
notebook's own ``execution_count`` values when a non-blank code cell was never
run or the counts do not strictly increase top to bottom. When the notebook
cannot be read or parsed, the check falls back to the declaration.

Run:  python3 -m unittest tests.test_repro_notebook -v
"""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from dsx.checks import repro


def _cell(count, source="x = 1\n", cell_type="code"):
    cell = {"cell_type": cell_type, "metadata": {}, "source": source}
    if cell_type == "code":
        cell["execution_count"] = count
        cell["outputs"] = []
    return cell


def _notebook(*cells) -> dict:
    return {"cells": list(cells), "metadata": {}, "nbformat": 4, "nbformat_minor": 5}


def _spec(declared: bool, entrypoint: str = "analysis.ipynb") -> dict:
    return {
        "reproducibility": {
            "entrypoint": entrypoint,
            "runs_clean_top_to_bottom": declared,
        }
    }


def _rep040(spec: dict, phase_dir: str) -> list:
    report = repro.check(spec, phase_dir)
    return [f for f in report.findings if f.code == "DSX-REP-040"]


class TestNotebookExecutionCounts(unittest.TestCase):
    def _write(self, tmp: str, content, name: str = "analysis.ipynb") -> None:
        text = content if isinstance(content, str) else json.dumps(content)
        (Path(tmp) / name).write_text(text, encoding="utf-8")

    def test_clean_run_with_declaration_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._write(tmp, _notebook(
                _cell(None, "# Heading\n", cell_type="markdown"),
                _cell(1), _cell(2), _cell(None, source=""), _cell(3, source=["y = 2\n"]),
            ))
            self.assertEqual([], _rep040(_spec(True), tmp))

    def test_out_of_order_counts_contradict_declaration(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._write(tmp, _notebook(_cell(1), _cell(5), _cell(3)))
            found = _rep040(_spec(True), tmp)
            self.assertEqual(1, len(found))
            self.assertIn("execution counts contradict the declaration", found[0].detail)
            self.assertIn("code cell 3", found[0].detail)
            self.assertEqual("HIGH", found[0].severity.name)
            self.assertEqual("spec.reproducibility.entrypoint", found[0].where)

    def test_repeated_count_is_not_strictly_increasing(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._write(tmp, _notebook(_cell(1), _cell(1)))
            self.assertEqual(1, len(_rep040(_spec(True), tmp)))

    def test_never_run_code_cell_contradicts_declaration(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._write(tmp, _notebook(_cell(1), _cell(None), _cell(2)))
            found = _rep040(_spec(True), tmp)
            self.assertEqual(1, len(found))
            self.assertIn("never run", found[0].detail)

    def test_undeclared_still_fires_once_on_the_boolean(self):
        with tempfile.TemporaryDirectory() as tmp:
            self._write(tmp, _notebook(_cell(2), _cell(1)))
            found = _rep040(_spec(False), tmp)
            self.assertEqual(1, len(found))
            self.assertEqual("spec.reproducibility.runs_clean_top_to_bottom", found[0].where)

    def test_notebook_resolved_relative_to_phase_dir_subfolder(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "nb").mkdir()
            self._write(tmp, _notebook(_cell(2), _cell(1)), name="nb/a.ipynb")
            self.assertEqual(1, len(_rep040(_spec(True, "nb/a.ipynb"), tmp)))


class TestUnreadableNotebookFallsBackToDeclaration(unittest.TestCase):
    def test_missing_notebook_trusts_declaration(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual([], _rep040(_spec(True, "absent.ipynb"), tmp))

    def test_unparseable_notebook_trusts_declaration(self):
        for content in ("{not json", "[1, 2, 3]", json.dumps({"worksheets": []}),
                        json.dumps(_notebook(_cell("1"), _cell(0)))):
            with self.subTest(content=content[:20]), tempfile.TemporaryDirectory() as tmp:
                (Path(tmp) / "analysis.ipynb").write_text(content, encoding="utf-8")
                self.assertEqual([], _rep040(_spec(True), tmp))

    def test_directory_named_like_notebook_trusts_declaration(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "analysis.ipynb").mkdir()
            self.assertEqual([], _rep040(_spec(True), tmp))

    def test_script_entrypoint_is_out_of_scope(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual([], _rep040(_spec(False, "analysis.py"), tmp))


if __name__ == "__main__":
    unittest.main()
