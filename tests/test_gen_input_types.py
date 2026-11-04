"""scripts/gen-input-types.py --check: a drift gate that never writes.

Mirrors tests/test_gen_finding_catalogue.py for the sibling generator. The
module is loaded by path (its file name has a hyphen) and TARGET is pointed at
a scratch copy, so the checked-in dsx/data/input_types.json is never touched.
"""

from __future__ import annotations

import contextlib
import importlib.util
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "gen-input-types.py"
TARGET = ROOT / "dsx" / "data" / "input_types.json"


def load_module():
    spec = importlib.util.spec_from_file_location("gen_input_types_check_mod", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestGenInputTypesCheck(unittest.TestCase):
    def test_checked_in_json_is_current(self):
        proc = subprocess.run([sys.executable, str(SCRIPT), "--check"],
                              capture_output=True, text=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("current", proc.stdout)

    def _run_main(self, module, argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = module.main(argv)
        return code, out.getvalue(), err.getvalue()

    def test_stale_json_fails_and_is_not_rewritten(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            scratch = Path(tmp) / "input_types.json"
            stale = TARGET.read_text(encoding="utf-8").replace('"IT001"', '"IT001-stale"', 1)
            scratch.write_text(stale, encoding="utf-8")
            module.TARGET = scratch
            code, _out, err = self._run_main(module, ["--check"])
            self.assertEqual(code, 1)
            self.assertIn("stale", err)
            self.assertEqual(scratch.read_text(encoding="utf-8"), stale, "--check must never write")

    def test_missing_json_fails_under_check_without_creating_it(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            scratch = Path(tmp) / "input_types.json"
            module.TARGET = scratch
            code, _out, _err = self._run_main(module, ["--check"])
            self.assertEqual(code, 1)
            self.assertFalse(scratch.exists())

    def test_write_regenerates_the_checked_in_bytes(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp:
            scratch = Path(tmp) / "input_types.json"
            module.TARGET = scratch
            code, _out, _err = self._run_main(module, ["--write"])
            self.assertEqual(code, 0)
            self.assertEqual(scratch.read_text(encoding="utf-8"), TARGET.read_text(encoding="utf-8"))
            module.TARGET = scratch
            code, _out, _err = self._run_main(module, ["--check"])
            self.assertEqual(code, 0)


if __name__ == "__main__":
    unittest.main()
