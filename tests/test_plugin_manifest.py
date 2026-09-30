""".claude-plugin/plugin.json component paths follow the Claude Code manifest rules.

Checked against https://code.claude.com/docs/en/plugins-reference (2026-09-30):
every component path starts with ``./`` and must exist inside the plugin;
``commands`` takes flat .md files or directories; ``agents`` takes .md files
only (a directory fails ``claude plugin validate``), and when omitted the
default ``agents/`` folder is scanned.
"""

from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))


def as_list(value) -> list:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


class TestPluginManifestPaths(unittest.TestCase):
    def _assert_inside_and_present(self, rel: str) -> Path:
        self.assertTrue(rel.startswith("./"), f"{rel!r} must start with ./")
        self.assertNotIn("..", Path(rel).parts, rel)
        path = ROOT / rel
        self.assertTrue(path.exists(), f"{rel} does not exist")
        return path

    def test_csv_first_commands_are_shipped(self):
        # M24: /dsx-eda and /dsx-scope reach plugin users, not just this checkout.
        commands = as_list(PLUGIN.get("commands"))
        for name in ("dsx-eda.md", "dsx-scope.md"):
            self.assertTrue(any(c.endswith(name) for c in commands), f"{name} not in plugin.json commands")
        for rel in commands:
            path = self._assert_inside_and_present(rel)
            self.assertTrue(path.is_dir() or path.suffix == ".md", rel)

    def test_agents_are_files_or_left_to_the_default_scan(self):
        for rel in as_list(PLUGIN.get("agents")):
            path = self._assert_inside_and_present(rel)
            self.assertEqual(path.suffix, ".md", f"agents entries must be .md files, not {rel}")
        if "agents" not in PLUGIN:
            self.assertTrue(list((ROOT / "agents").glob("*.md")), "default agents/ scan finds nothing")

    def test_skills_paths_exist(self):
        for rel in as_list(PLUGIN.get("skills")):
            self.assertTrue(self._assert_inside_and_present(rel).is_dir(), rel)


if __name__ == "__main__":
    unittest.main()
