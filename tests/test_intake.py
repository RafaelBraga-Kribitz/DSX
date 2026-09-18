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

import intake


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

PROMPT_NO_FRONTMATTER = """# {heading}

{body}
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
    (root / "intake" / "prompts").mkdir()
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


class TestPrompts(unittest.TestCase):
    """A prompt is a third kind: frontmatter optional, never declared in the manifest."""

    def test_prompt_without_frontmatter_is_ok_and_uses_its_heading(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            (root / "intake" / "prompts" / "one-shot-eda.md").write_text(
                PROMPT_NO_FRONTMATTER.format(
                    heading="One-shot exploratory pass",
                    body="Profile the extract, then report what would invalidate an analysis.",
                ))
            [item] = intake.scan(root)
        self.assertEqual((item.kind, item.status), ("prompt", "ok"))
        self.assertEqual(item.description, "One-shot exploratory pass")
        self.assertTrue(any("first heading" in n for n in item.notes), item.notes)

    def test_prompt_with_frontmatter_keeps_its_description_and_gets_overlap_hints(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            (root / "intake" / "prompts" / "spec-first-opener.md").write_text(GOOD_SKILL.format(
                name="spec-first-opener",
                desc="Turn a business question into a checkable ANALYSIS-SPEC before touching data."))
            [item] = intake.scan(root)
        self.assertEqual((item.kind, item.status), ("prompt", "ok"))
        self.assertTrue(
            any("possible overlap with dsx-scope-analysis" in n for n in item.notes),
            item.notes,
        )

    def test_promote_prompt_lands_in_prompts_and_is_not_declared(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            (root / "intake" / "prompts" / "one-shot-eda.md").write_text(
                PROMPT_NO_FRONTMATTER.format(heading="One-shot pass", body="Do the thing."))
            self.assertEqual(quiet_main(["--root", str(root), "--promote", "one-shot-eda"]), 0)
            self.assertTrue((root / "prompts" / "one-shot-eda.md").exists())
            self.assertFalse((root / "intake" / "prompts" / "one-shot-eda.md").exists())
            manifest = json.loads((root / "capabilities" / "dsx" / "capability.json").read_text())
        # A prompt is reference material; declaring it would make the manifest lie.
        self.assertNotIn("one-shot-eda", manifest["skills"])
        self.assertNotIn("one-shot-eda", manifest["agents"])

    def test_a_promoted_prompt_then_collides_by_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            (root / "prompts").mkdir()
            (root / "prompts" / "taken.md").write_text("# Already here\n")
            (root / "intake" / "prompts" / "taken.md").write_text("# Duplicate\n")
            [item] = intake.scan(root)
        self.assertEqual(item.status, "collision")
        self.assertTrue(any("prompts/taken.md" in n for n in item.notes), item.notes)

    def test_prompts_readme_is_not_read_as_a_prompt(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            (root / "intake" / "prompts" / "README.md").write_text("# How to use this folder\n")
            self.assertEqual(intake.scan(root), [])

    def test_skills_index_is_unrecognised_not_promotable(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            (root / "intake" / "prompts" / "SKILLs.md").write_text(
                "# AI Prompts for Data Professionals\n\nBrowse by role.\n")
            [item] = intake.scan(root)
            self.assertEqual((item.kind, item.status), ("prompt", "unrecognised"))
            self.assertTrue(any("library index" in n for n in item.notes), item.notes)
            self.assertEqual(quiet_main(["--root", str(root), "--promote", "SKILLs"]), 1)
            self.assertTrue((root / "intake" / "prompts" / "SKILLs.md").exists())


class TestUnrecognised(unittest.TestCase):
    """Nothing under intake/ is skipped in silence."""

    def test_unknown_folder_is_reported_with_its_file_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            (root / "intake" / "notebooks" / "deep").mkdir(parents=True)
            (root / "intake" / "notebooks" / "scratch.md").write_text("notes\n")
            (root / "intake" / "notebooks" / "deep" / "nested.md").write_text("more\n")
            [item] = intake.scan(root)
        self.assertEqual((item.kind, item.status), ("unknown", "unrecognised"))
        self.assertEqual(item.name, "notebooks")
        self.assertTrue(any("2 file(s)" in n for n in item.notes), item.notes)

    def test_loose_file_directly_under_intake_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            (root / "intake" / "TODO.md").write_text("route me\n")
            [item] = intake.scan(root)
        self.assertEqual(item.status, "unrecognised")
        self.assertEqual(item.name, "TODO.md")

    def test_intake_readme_and_dotfiles_are_not_unrecognised(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            (root / "intake" / "README.md").write_text("# Intake\n")
            (root / "intake" / ".gitkeep").write_text("")
            (root / "intake" / "skills" / ".gitkeep").write_text("")
            self.assertEqual(intake.scan(root), [])

    def test_skill_folder_without_skill_md_is_invalid_not_invisible(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            (root / "intake" / "skills" / "half-written").mkdir()
            (root / "intake" / "skills" / "half-written" / "notes.md").write_text("wip\n")
            [item] = intake.scan(root)
        self.assertEqual((item.kind, item.status), ("skill", "invalid"))
        self.assertTrue(any("no SKILL.md" in n for n in item.notes), item.notes)

    def test_non_markdown_file_in_a_flat_kind_folder_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            (root / "intake" / "prompts" / "notes.txt").write_text("x\n")
            [item] = intake.scan(root)
        self.assertEqual((item.kind, item.status), ("prompt", "unrecognised"))
        self.assertTrue(any("not a .md file" in n for n in item.notes), item.notes)

    def test_nested_folder_in_a_flat_kind_folder_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            (root / "intake" / "prompts" / "data-analyst" / "eda").mkdir(parents=True)
            (root / "intake" / "prompts" / "data-analyst" / "eda" / "a.md").write_text("# A\n")
            (root / "intake" / "agents" / "global").mkdir()
            (root / "intake" / "agents" / "global" / "data-scientist.md").write_text(
                GOOD_AGENT.format(name="data-scientist", desc="A generalist."))
            items = {i.name: i for i in intake.scan(root)}
        self.assertEqual(items["data-analyst"].status, "unrecognised")
        self.assertEqual(items["data-analyst"].kind, "prompt")
        self.assertTrue(any("nested folder" in n for n in items["data-analyst"].notes),
                        items["data-analyst"].notes)
        self.assertEqual(items["global"].status, "unrecognised")
        self.assertEqual(items["global"].kind, "agent")

    def test_unrecognised_is_never_promotable(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            (root / "intake" / "notebooks").mkdir()
            (root / "intake" / "notebooks" / "a.md").write_text("a\n")
            self.assertEqual(quiet_main(["--root", str(root), "--promote", "notebooks"]), 1)
            self.assertTrue((root / "intake" / "notebooks" / "a.md").exists())


class TestBatchPromote(unittest.TestCase):
    def test_several_names_in_one_call(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            (root / "intake" / "skills" / "cohort-retention").mkdir()
            (root / "intake" / "skills" / "cohort-retention" / "SKILL.md").write_text(
                GOOD_SKILL.format(name="cohort-retention", desc="Retention cohort table."))
            (root / "intake" / "agents" / "dsx-de-reviewer.md").write_text(GOOD_AGENT.format(
                name="dsx-de-reviewer", desc="Review a pipeline for idempotency and late data."))
            (root / "intake" / "prompts" / "opener.md").write_text("# Opener\n")
            code = quiet_main(["--root", str(root), "--promote",
                               "cohort-retention", "dsx-de-reviewer", "opener"])
            self.assertEqual(code, 0)
            self.assertTrue((root / "skills" / "cohort-retention" / "SKILL.md").exists())
            self.assertTrue((root / "agents" / "dsx-de-reviewer.md").exists())
            self.assertTrue((root / "prompts" / "opener.md").exists())
            manifest = json.loads((root / "capabilities" / "dsx" / "capability.json").read_text())
        self.assertEqual(manifest["skills"][-1], "cohort-retention")
        self.assertEqual(manifest["agents"][-1], "dsx-de-reviewer")

    def test_one_bad_name_does_not_stop_the_batch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_root(tmp)
            (root / "intake" / "prompts" / "good.md").write_text("# Good\n")
            code = quiet_main(["--root", str(root), "--promote", "nope", "good"])
            # Non-zero because one name failed, but the valid one still moved.
            self.assertEqual(code, 1)
            self.assertTrue((root / "prompts" / "good.md").exists())


if __name__ == "__main__":
    unittest.main()
