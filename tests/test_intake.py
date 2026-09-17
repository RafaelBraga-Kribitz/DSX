"""Tests for scripts/intake.py against a synthetic project root."""

from __future__ import annotations

import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import intake  # noqa: E402


def quiet_main(argv):
    """Run intake.main without letting its report leak into the test output."""
    with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
        return intake.main(argv)

GOOD_SKILL = """---
name: {name}
description: "{desc}"
allowed-tools:
  - Read
---

<objective>
Body.
</objective>
"""

GOOD_AGENT = """---
name: {name}
description: {desc}
tools: Read
---

<role>Break the claim.</role>
"""

MANIFEST = """{
  "id": "dsx",
  "version": "2.0.0",
  "skills": [
    "dsx-scope-analysis",
    "dsx-explore-data"
  ],
  "agents": [
    "dsx-statistician"
  ]
}
"""


def make_root(tmp: str) -> Path:
    root = Path(tmp)
    (root / "skills" / "dsx-scope-analysis").mkdir(parents=True)
    (root / "skills" / "dsx-scope-analysis" / "SKILL.md").write_text(GOOD_SKILL.format(
        name="dsx-scope-analysis",
        desc="Turn a business question into a checkable ANALYSIS-SPEC before touching data."))
    (root / "skills" / "dsx-explore-data").mkdir()
    (root / "skills" / "dsx-explore-data" / "SKILL.md").write_text(GOOD_SKILL.format(
        name="dsx-explore-data", desc="Programmatic exploratory data analysis with a fixed protocol."))
    (root / "agents").mkdir()
    (root / "agents" / "dsx-statistician.md").write_text(GOOD_AGENT.format(
        name="dsx-statistician", desc="Adversarial review of the statistical content of a completed analysis."))
    (root / "capabilities" / "dsx").mkdir(parents=True)
    (root / "capabilities" / "dsx" / "capability.json").write_text(MANIFEST)
    (root / "intake" / "skills").mkdir(parents=True)
    (root / "intake" / "agents").mkdir()
    return root


class TestScan(unittest.TestCase):
    def test_empty_intake(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(intake.scan(make_root(tmp)), [])

    def test_statuses(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            (root / "intake" / "skills" / "cohort-retention").mkdir()
            (root / "intake" / "skills" / "cohort-retention" / "SKILL.md").write_text(GOOD_SKILL.format(
                name="cohort-retention", desc="Build a retention cohort table with a fixed denominator."))
            (root / "intake" / "skills" / "dsx-explore-data").mkdir()
            (root / "intake" / "skills" / "dsx-explore-data" / "SKILL.md").write_text(GOOD_SKILL.format(
                name="dsx-explore-data", desc="Another exploratory data analysis skill."))
            (root / "intake" / "skills" / "Bad Name").mkdir()
            (root / "intake" / "skills" / "Bad Name" / "SKILL.md").write_text(GOOD_SKILL.format(
                name="Bad Name", desc="x"))
            (root / "intake" / "agents" / "nofront.md").write_text("# no frontmatter\n")
            (root / "intake" / "agents" / "reviewer.md").write_text(GOOD_AGENT.format(
                name="mismatch", desc="Name does not match the file."))
            by_name = {i.name: i for i in intake.scan(root)}
        self.assertEqual(by_name["cohort-retention"].status, "ok")
        self.assertEqual(by_name["dsx-explore-data"].status, "collision")
        self.assertTrue(any("capability.json" in n or "skills/" in n for n in by_name["dsx-explore-data"].notes))
        self.assertEqual(by_name["Bad Name"].status, "invalid")
        self.assertEqual(by_name["nofront"].status, "invalid")
        self.assertEqual(by_name["reviewer"].status, "invalid")
        self.assertTrue(any("does not match" in n for n in by_name["reviewer"].notes))

    def test_overlap_hint(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            (root / "intake" / "skills" / "spec-first").mkdir()
            (root / "intake" / "skills" / "spec-first" / "SKILL.md").write_text(GOOD_SKILL.format(
                name="spec-first",
                desc="Turn a business question into a checkable ANALYSIS-SPEC before touching data."))
            [item] = intake.scan(root)
        self.assertEqual(item.status, "ok")
        self.assertTrue(any("possible overlap with dsx-scope-analysis" in n for n in item.notes), item.notes)


class TestPromote(unittest.TestCase):
    def test_promote_skill_moves_and_declares(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            (root / "intake" / "skills" / "cohort-retention").mkdir()
            (root / "intake" / "skills" / "cohort-retention" / "SKILL.md").write_text(GOOD_SKILL.format(
                name="cohort-retention", desc="Build a retention cohort table."))
            code = quiet_main(["--root", str(root), "--promote", "cohort-retention"])
            self.assertEqual(code, 0)
            self.assertTrue((root / "skills" / "cohort-retention" / "SKILL.md").exists())
            self.assertFalse((root / "intake" / "skills" / "cohort-retention").exists())
            manifest = json.loads((root / "capabilities" / "dsx" / "capability.json").read_text())
            self.assertIn("cohort-retention", manifest["skills"])
            self.assertEqual(manifest["skills"][:2], ["dsx-scope-analysis", "dsx-explore-data"])
            self.assertEqual(manifest["agents"], ["dsx-statistician"])

    def test_promote_agent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            (root / "intake" / "agents" / "dsx-de-reviewer.md").write_text(GOOD_AGENT.format(
                name="dsx-de-reviewer", desc="Review a data pipeline for idempotency and late data."))
            code = quiet_main(["--root", str(root), "--promote", "dsx-de-reviewer"])
            self.assertEqual(code, 0)
            self.assertTrue((root / "agents" / "dsx-de-reviewer.md").exists())
            manifest = json.loads((root / "capabilities" / "dsx" / "capability.json").read_text())
            self.assertEqual(manifest["agents"], ["dsx-statistician", "dsx-de-reviewer"])

    def test_promote_refuses_collision_and_unknown(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            (root / "intake" / "skills" / "dsx-explore-data").mkdir()
            (root / "intake" / "skills" / "dsx-explore-data" / "SKILL.md").write_text(GOOD_SKILL.format(
                name="dsx-explore-data", desc="dup"))
            self.assertEqual(quiet_main(["--root", str(root), "--promote", "dsx-explore-data"]), 1)
            self.assertEqual(quiet_main(["--root", str(root), "--promote", "nothing-here"]), 1)
            self.assertTrue((root / "intake" / "skills" / "dsx-explore-data").exists())


if __name__ == "__main__":
    unittest.main()
