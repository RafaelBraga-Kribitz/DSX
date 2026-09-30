"""templates/dsx_plotstyle.py::use_style — named style selection (audit M37/L81).

Repo-integrity test, off the gate path: ``use_style(name)`` must resolve
``styles/<name>.mplstyle`` relative to the helper module (not the working
directory), apply it, and refuse an unknown name with a ``ValueError`` that lists
the styles that exist. ``available_styles()`` must name exactly the vendored
``styles/dsx-*.mplstyle`` files.

Guarded with ``@unittest.skipIf`` when matplotlib is absent (analyst-side only),
and loaded by file path because ``templates/`` is not a package — the same
pattern as ``tests/test_dsx_plotstyle_api.py``.

Run:  python -m unittest tests.test_dsx_plotstyle_use_style -v
"""

from __future__ import annotations

import importlib.util
import os
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HELPER_PATH = ROOT / "templates" / "dsx_plotstyle.py"
STYLE_DIR = ROOT / "styles"

try:
    import matplotlib  # noqa: F401

    _MPL_AVAILABLE = True
except ImportError:
    _MPL_AVAILABLE = False


def _load_helper():
    spec = importlib.util.spec_from_file_location("dsx_plotstyle", HELPER_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@unittest.skipIf(not _MPL_AVAILABLE, "matplotlib not installed — analyst-side only")
class TestUseStyle(unittest.TestCase):
    def setUp(self):
        import matplotlib as mpl

        self.mpl = mpl
        self.mod = _load_helper()
        self._saved = mpl.rcParams.copy()

    def tearDown(self):
        self.mpl.rcParams.update(self._saved)

    def test_available_styles_match_the_vendored_files(self):
        expected = sorted(p.stem for p in STYLE_DIR.glob("dsx-*.mplstyle"))
        self.assertTrue(expected, "no styles/dsx-*.mplstyle files found (non-vacuity)")
        self.assertEqual(self.mod.available_styles(), expected)
        for name in ("dsx-urban", "dsx-538", "dsx-bbc", "dsx-econ"):
            self.assertIn(name, expected)

    def test_every_style_applies_and_returns_its_path(self):
        for name in self.mod.available_styles():
            with self.subTest(style=name):
                path = self.mod.use_style(name)
                self.assertEqual(path, (STYLE_DIR / f"{name}.mplstyle").resolve())
                self.assertEqual(self.mpl.rcParams["font.sans-serif"][0], "Lato")

    def test_resolution_does_not_depend_on_working_directory(self):
        before = os.getcwd()
        with tempfile.TemporaryDirectory() as tmp:
            try:
                os.chdir(tmp)
                path = self.mod.use_style("dsx-urban")
            finally:
                os.chdir(before)
        self.assertTrue(path.is_file())

    def test_unknown_name_raises_value_error_listing_known_styles(self):
        for bad in ("dsx-nope", "urban", "../styles/dsx-urban", ""):
            with self.subTest(name=bad):
                with self.assertRaises(ValueError) as ctx:
                    self.mod.use_style(bad)
                message = str(ctx.exception)
                self.assertIn("dsx-urban", message)
                self.assertIn("dsx-538", message)

    def test_both_lato_faces_are_registered(self):
        from matplotlib import font_manager

        names = {Path(f.fname).name for f in font_manager.fontManager.ttflist}
        self.assertIn("Lato-Regular.ttf", names)
        self.assertIn("Lato-Bold.ttf", names)


if __name__ == "__main__":
    unittest.main()
