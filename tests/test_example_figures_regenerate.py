"""The committed exemplar figures are what examples/analysis/charts.py draws
(project audit 2026-09-30, L31).

``examples/figures/*.svg`` are sealed by ``dsx seal`` (their sha256 is recorded in
``examples/good-ANALYSIS-SPEC.yaml``), so they are frozen artefacts and are never
rewritten by this test. This test re-runs the three generators into a temporary
directory and compares the output with the committed files, so a change to
charts.py, the house style or the plot helper that is not re-rendered and
re-sealed shows up here.

The comparison is not raw bytes, for two measured reasons: the committed files
were rendered on Windows (CRLF line endings; ``.gitattributes`` stores them
binary so the seals survive), and the SVG metadata names the exact matplotlib
version. Line endings and that one ``<dc:title>`` line are normalised; every
other byte must match. Output geometry can move between matplotlib minor
releases, so the test is skipped when the running matplotlib's major.minor
differs from the one recorded in the committed files, and when matplotlib is
not installed (the gate path is stdlib-only and CI need not have it).

Writes only into a ``tempfile.TemporaryDirectory``.

Run:  python3 -m unittest tests.test_example_figures_regenerate -v
"""

from __future__ import annotations

import importlib.util
import re
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHARTS_PATH = ROOT / "examples" / "analysis" / "charts.py"
FIG_DIR = ROOT / "examples" / "figures"
_VERSION_RE = re.compile(rb"Matplotlib v(\d+)\.(\d+)\.\d+")

try:
    import matplotlib

    _MPL_VERSION = tuple(int(p) for p in matplotlib.__version__.split(".")[:2])
except ImportError:  # pragma: no cover - depends on the environment
    matplotlib = None
    _MPL_VERSION = None


def _normalise(data: bytes) -> bytes:
    data = data.replace(b"\r\n", b"\n")
    return _VERSION_RE.sub(b"Matplotlib vX", data)


def _recorded_version() -> tuple[int, int] | None:
    match = _VERSION_RE.search((FIG_DIR / "activation_uplift.svg").read_bytes())
    return (int(match.group(1)), int(match.group(2))) if match else None


@unittest.skipIf(matplotlib is None, "matplotlib not installed; figures are frozen artefacts")
class TestExampleFiguresRegenerate(unittest.TestCase):
    def test_charts_py_redraws_the_committed_figures(self):
        recorded = _recorded_version()
        if recorded != _MPL_VERSION:
            self.skipTest(
                f"committed figures were rendered with matplotlib {recorded}, running "
                f"{_MPL_VERSION}; geometry is not comparable across minor releases"
            )
        spec = importlib.util.spec_from_file_location("_dsx_example_charts", CHARTS_PATH)
        charts = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(charts)
        import matplotlib.pyplot as plt

        with tempfile.TemporaryDirectory() as tmp, matplotlib.rc_context():
            charts.FIG_DIR = Path(tmp)
            plt.style.use(str(charts.STYLE))
            written = [
                charts.render_activation_uplift(),
                charts.render_daily_trend(),
                charts.render_uplift_ci(),
            ]
            self.assertEqual(
                sorted(p.name for p in written),
                sorted(p.name for p in FIG_DIR.glob("*.svg")),
                "charts.py and examples/figures/ disagree on which figures exist",
            )
            for path in written:
                with self.subTest(figure=path.name):
                    self.assertEqual(
                        _normalise(path.read_bytes()),
                        _normalise((FIG_DIR / path.name).read_bytes()),
                        f"{path.name} re-rendered differently from the committed file: "
                        "re-run examples/analysis/charts.py and re-seal with dsx seal",
                    )


if __name__ == "__main__":
    unittest.main()
