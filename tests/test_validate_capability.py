"""scripts/validate-capability.py: the checks beyond the manifest reference.

Covers the M5 audit gaps: frontmatter is read only up to its closing ``---``,
fragments nothing references are reported, and each gate command's
``dsx gate <point>`` and flags are cross-checked against dsx.cli.
"""

from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "validate-capability.py"
CAP_DIR = ROOT / "capabilities" / "dsx"
PREFIX = 'DSX="$(command -v dsx 2>/dev/null || echo "$HOME/.gsd/capabilities/dsx/bin/dsx")"; "$DSX" '


def load_module():
    spec = importlib.util.spec_from_file_location("validate_capability_mod", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


VC = load_module()


def real_manifest() -> dict:
    return json.loads((CAP_DIR / "capability.json").read_text(encoding="utf-8"))


class TestShippedManifest(unittest.TestCase):
    def test_shipped_manifest_is_conformant_without_warnings(self):
        proc = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("is conformant", proc.stdout)
        self.assertNotIn("warn:", proc.stdout)


class TestFrontmatter(unittest.TestCase):
    def _agent(self, tmp: str, text: str) -> Path:
        path = Path(tmp) / "dsx-probe.md"
        path.write_text(text, encoding="utf-8")
        return path

    def test_name_in_body_does_not_satisfy_frontmatter(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self._agent(tmp, "---\nname: something-else\ndescription: d\ntools: Read\n---\n"
                                    "name: dsx-probe\n")
            errors, _ = VC.check_agent_frontmatter(path, "dsx-probe")
        self.assertTrue(any("does not match" in e for e in errors), errors)

    def test_unclosed_frontmatter_is_an_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self._agent(tmp, "---\nname: dsx-probe\ndescription: d\n")
            errors, _ = VC.check_agent_frontmatter(path, "dsx-probe")
        self.assertTrue(any("no frontmatter" in e for e in errors), errors)

    def test_missing_description_errors_and_missing_tools_warns(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self._agent(tmp, "---\nname: dsx-probe\n---\nbody\n")
            errors, warnings = VC.check_agent_frontmatter(path, "dsx-probe")
        self.assertTrue(any("description" in e for e in errors), errors)
        self.assertTrue(any("tools" in w for w in warnings), warnings)

    def test_well_formed_frontmatter_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = self._agent(tmp, "---\nname: dsx-probe\ndescription: d\ntools: Read, Bash\n---\n")
            self.assertEqual(VC.check_agent_frontmatter(path, "dsx-probe"), ([], []))


class TestOrphanFragments(unittest.TestCase):
    def test_shipped_fragments_are_all_referenced(self):
        self.assertEqual(VC.orphan_fragments(real_manifest(), CAP_DIR), [])

    def test_unreferenced_fragment_warns(self):
        with tempfile.TemporaryDirectory() as tmp:
            cap = Path(tmp) / "dsx"
            (cap / "fragments").mkdir(parents=True)
            (cap / "fragments" / "used.md").write_text("x", encoding="utf-8")
            (cap / "fragments" / "stray.md").write_text("x", encoding="utf-8")
            manifest = {"steps": [{"fragment": {"path": "fragments/used.md"}}], "contributions": []}
            warnings = VC.orphan_fragments(manifest, cap)
        self.assertEqual(len(warnings), 1, warnings)
        self.assertIn("stray.md", warnings[0])


class TestGateCommands(unittest.TestCase):
    def test_shipped_gate_commands_pass(self):
        for gate in real_manifest()["gates"]:
            command = gate["check"]["predicate"]["command"]
            self.assertEqual(VC.check_gate_command(command), [], command)

    def test_unknown_point_is_rejected(self):
        problems = VC.check_gate_command(PREFIX + 'gate deploy --phase-dir "${PHASE_DIR}"')
        self.assertTrue(any("not a gate profile" in p for p in problems), problems)

    def test_unknown_flag_is_rejected(self):
        problems = VC.check_gate_command(PREFIX + 'gate plan --phase-dir "${PHASE_DIR}" --allow-missng')
        self.assertTrue(any("--allow-missng" in p for p in problems), problems)

    def test_flag_missing_its_value_is_rejected(self):
        problems = VC.check_gate_command(PREFIX + "gate verify --report")
        self.assertTrue(problems, "a --report with no path must not pass")

    def test_non_dsx_command_is_not_judged(self):
        self.assertEqual(VC.check_gate_command("test -f README.md"), [])

    def test_bad_gate_fails_whole_validation(self):
        manifest = copy.deepcopy(real_manifest())
        manifest["gates"][0]["check"]["predicate"]["command"] = PREFIX + "gate plan --no-such-flag"
        errors, _ = VC.validate(manifest, ROOT, CAP_DIR)
        self.assertTrue(any("gates[0]" in e and "--no-such-flag" in e for e in errors), errors)


if __name__ == "__main__":
    unittest.main()
