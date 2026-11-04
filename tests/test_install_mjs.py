"""install.mjs overlay contract. Stdlib unittest; skipped when node is absent.

Runs the real installer against a throwaway HOME, so nothing outside the
temporary directory is touched.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NODE = shutil.which("node")


def run_installer(home: str, *args: str) -> subprocess.CompletedProcess:
    env = {**os.environ, "HOME": home, "USERPROFILE": home}
    env.pop("DSX_PYTHON", None)
    return subprocess.run(
        [NODE, str(ROOT / "install.mjs"), *args],
        capture_output=True, text=True, env=env, cwd=home, check=False, timeout=300,
    )


@unittest.skipIf(NODE is None, "node not available")
class TestInstallOverlay(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory()
        cls.home = cls._tmp.name
        cls.install = run_installer(cls.home)
        cls.overlay = Path(cls.home) / ".gsd" / "capabilities" / "dsx"

    @classmethod
    def tearDownClass(cls):
        cls._tmp.cleanup()

    def test_install_succeeds(self):
        self.assertEqual(self.install.returncode, 0, self.install.stderr + self.install.stdout)

    def test_overlay_carries_styles_and_fonts(self):
        # M23: templates/dsx_plotstyle.py looks for <overlay>/styles/fonts.
        for rel in ("styles/fonts/Lato-Regular.ttf", "styles/fonts/Lato-Bold.ttf",
                    "styles/dsx-538.mplstyle", "templates/dsx_plotstyle.py"):
            self.assertTrue((self.overlay / rel).is_file(), rel)

    def test_check_passes_then_flags_missing_styles(self):
        proc = run_installer(self.home, "--check")
        self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)
        self.assertIn("payload:", proc.stdout)
        backup = Path(self.home) / "styles-backup"
        shutil.move(str(self.overlay / "styles"), str(backup))
        try:
            proc = run_installer(self.home, "--check")
            self.assertEqual(proc.returncode, 1, proc.stdout)
            self.assertIn("missing from overlay", proc.stderr)
            self.assertIn("styles", proc.stderr)
        finally:
            shutil.move(str(backup), str(self.overlay / "styles"))


@unittest.skipIf(NODE is None, "node not available")
class TestInstallArgs(unittest.TestCase):
    def test_force_is_undocumented_but_still_accepted(self):
        # L48: --force never did anything; help no longer advertises it, and
        # passing it must not break older scripts.
        with tempfile.TemporaryDirectory() as home:
            help_text = run_installer(home, "--help")
            self.assertEqual(help_text.returncode, 0, help_text.stderr)
            self.assertNotIn("--force", help_text.stdout)
            proc = run_installer(home, "--force", "--help")
            self.assertEqual(proc.returncode, 0, proc.stderr)

    def test_unknown_argument_fails(self):
        with tempfile.TemporaryDirectory() as home:
            proc = run_installer(home, "--no-such-flag")
            self.assertEqual(proc.returncode, 1)
            self.assertIn("unknown argument", proc.stderr)


if __name__ == "__main__":
    unittest.main()
