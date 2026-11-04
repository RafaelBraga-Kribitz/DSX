"""Tests for scripts/lint-scope.py and the promoted-material policy in check.sh.

The policy: material promoted out of intake/ keeps the style its author gave it,
and still fails the gate when it is actually broken. Both halves are asserted
here, the second by running ruff with the selection parsed out of check.sh -- so
a future edit that quietly drops the second pass, or widens it back to the full
rule set, fails a test rather than surprising someone months later.
"""

from __future__ import annotations

import importlib.util
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECK_SH = ROOT / "scripts" / "check.sh"

_spec = importlib.util.spec_from_file_location(
    "lint_scope", ROOT / "scripts" / "lint-scope.py"
)
lint_scope = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lint_scope)


def build_tree(root: Path, skills=(), agents=(), prompts=()) -> None:
    for name in skills:
        (root / "skills" / name).mkdir(parents=True, exist_ok=True)
        (root / "skills" / name / "SKILL.md").write_text("# s\n")
    for folder, names in (("agents", agents), ("prompts", prompts)):
        if names:
            (root / folder).mkdir(parents=True, exist_ok=True)
        for name in names:
            (root / folder / name).write_text("# a\n")


class TestClassification(unittest.TestCase):
    def test_our_own_names_are_authored_here(self):
        for name in ("dsx-scope-analysis", "dsx-statistician", "using-dsx", "README"):
            self.assertTrue(lint_scope.is_authored_here(name), name)

    def test_a_promoted_name_is_not(self):
        # Real names from the first drop: an author names a skill after its
        # subject, not after the project that adopted it.
        for name in ("forecasting", "postgres", "mlflow", "academic-paper"):
            self.assertFalse(lint_scope.is_authored_here(name), name)

    def test_the_prefix_must_be_the_whole_first_segment(self):
        # `dsxfoo` is not ours; the convention is `dsx-`.
        self.assertFalse(lint_scope.is_authored_here("dsxfoo"))

    def test_classify_splits_a_mixed_tree(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            build_tree(
                root,
                skills=("dsx-funnel", "using-dsx", "postgres"),
                agents=("dsx-statistician.md", "code-reviewer.md"),
                prompts=("README.md", "weekly-brief.md"),
            )
            authored, promoted = lint_scope.classify(root)
            self.assertEqual(
                authored,
                [
                    "agents/dsx-statistician.md",
                    "prompts/README.md",
                    "skills/dsx-funnel",
                    "skills/using-dsx",
                ],
            )
            self.assertEqual(
                promoted,
                ["agents/code-reviewer.md", "prompts/weekly-brief.md", "skills/postgres"],
            )

    def test_every_path_lands_in_exactly_one_list(self):
        """No third bucket: anything under the three folders is ours or theirs."""
        authored, promoted = lint_scope.classify(ROOT)
        overlap = set(authored) & set(promoted)
        self.assertEqual(overlap, set())
        on_disk = set()
        for folder in ("skills", "agents", "prompts"):
            base = ROOT / folder
            for entry in base.iterdir():
                if folder == "skills":
                    if entry.is_dir():
                        on_disk.add(f"{folder}/{entry.name}")
                elif entry.is_file() and entry.suffix == ".md":
                    on_disk.add(f"{folder}/{entry.name}")
        self.assertEqual(set(authored) | set(promoted), on_disk)

    def test_a_skills_own_payload_is_not_classified(self):
        """Only the top level is an item. A skill's scripts/ is part of the skill."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            build_tree(root, skills=("postgres",))
            (root / "skills" / "postgres" / "references").mkdir()
            (root / "skills" / "postgres" / "references" / "notes.md").write_text("# n\n")
            _, promoted = lint_scope.classify(root)
            self.assertEqual(promoted, ["skills/postgres"])

    def test_this_repository_ships_no_unlinted_work_of_its_own(self):
        """Everything named `dsx-*` or `using-dsx` faces the full rule set."""
        _, promoted = lint_scope.classify(ROOT)
        ours = [p for p in promoted
                if Path(p).stem.startswith("dsx-") or Path(p).stem == "using-dsx"]
        self.assertEqual(ours, [], f"named like our own work but exempt from style: {ours}")


class TestOutputShapes(unittest.TestCase):
    def test_ruff_gets_directories_only(self):
        """ruff reads no markdown; handing it an agent file would be noise."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            build_tree(root, skills=("postgres",), agents=("code-reviewer.md",))
            _, promoted = lint_scope.classify(root)
            dirs = [p for p in promoted if not p.endswith(".md")]
            self.assertEqual(dirs, ["skills/postgres"])

    def test_markdown_globs_cover_a_directory_but_name_a_file(self):
        self.assertEqual(lint_scope.as_glob("skills/postgres"), "skills/postgres/**")
        self.assertEqual(lint_scope.as_glob("agents/code-reviewer.md"), "agents/code-reviewer.md")

    def test_the_cli_modes_agree_with_classify(self):
        out = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "lint-scope.py"), "--authored"],
            capture_output=True, text=True, check=True,
        ).stdout.split()
        authored, _ = lint_scope.classify(ROOT)
        self.assertEqual(out, authored)


class TestCheckShWiring(unittest.TestCase):
    """The policy is only real where the gate applies it."""

    def setUp(self):
        self.text = CHECK_SH.read_text()

    def test_both_linters_are_told_what_is_promoted(self):
        self.assertIn("lint-scope.py --ruff", self.text)
        self.assertIn("lint-scope.py --markdown", self.text)
        self.assertIn("--extend-exclude=$p", self.text)
        self.assertIn('set -- "$@" "!$g"', self.text)

    def test_the_exclusion_is_paired_with_a_second_pass(self):
        """Excluding promoted material from style may not exclude it from the gate."""
        self.assertIn("ruff check --select", self.text)

    def test_the_second_pass_keeps_the_rules_that_catch_a_broken_file(self):
        select = self.selection()
        for rule in ("E9", "F"):
            self.assertIn(rule, select["select"])
        # Tidiness rules may be dropped; rules that mean "this cannot work" may not.
        for rule in ("F821", "F811", "F632"):
            self.assertNotIn(rule, select["ignore"])

    def selection(self) -> dict:
        match = re.search(
            r"ruff check --select (\S+) --ignore (\S+)", self.text
        )
        self.assertIsNotNone(match, "check.sh no longer runs a promoted-material pass")
        return {"select": match.group(1).split(","), "ignore": match.group(2).split(",")}


@unittest.skipIf(shutil.which("ruff") is None, "ruff is not installed")
class TestPolicyBehaviour(unittest.TestCase):
    """What the two passes actually do, run against ruff itself."""

    def selection(self) -> list[str]:
        match = re.search(r"ruff check --select (\S+) --ignore (\S+)", CHECK_SH.read_text())
        return ["--select", match.group(1), "--ignore", match.group(2)]

    def run_promoted_pass(self, body: str) -> int:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "skills" / "postgres"
            target.mkdir(parents=True)
            (target / "helper.py").write_text(body)
            return subprocess.run(
                ["ruff", "check", "--isolated", *self.selection(), str(target)],
                capture_output=True, text=True, check=False,
            ).returncode

    def test_house_style_alone_does_not_fail_the_gate(self):
        # Spacing, quoting and an f-string with nothing in it: their house, not ours.
        self.assertEqual(self.run_promoted_pass("x=1\nprint(f'done')\n"), 0)

    def test_an_undefined_name_still_fails_the_gate(self):
        self.assertNotEqual(self.run_promoted_pass("def f():\n    return nope\n"), 0)

    def test_a_file_that_cannot_be_parsed_still_fails_the_gate(self):
        self.assertNotEqual(self.run_promoted_pass("def f(:\n"), 0)



@unittest.skipIf(shutil.which("sh") is None, "no POSIX shell")
class TestGlobsReachTheLinter(unittest.TestCase):
    """`skills/<name>/**` is a pattern for markdownlint, not one for the shell.

    The words are built from an unquoted expansion, which the shell also subjects
    to pathname expansion -- so without `set -f` the pattern is replaced by the
    files it happens to match in this checkout, and a file added to a promoted
    skill later is linted after all. Measured before the fix: one promoted skill
    became six `!` arguments naming its own subfolders.
    """

    def markdown_block(self) -> str:
        lines = CHECK_SH.read_text().splitlines()
        start = next(i for i, line in enumerate(lines)
                     if line.startswith('echo "==> markdown lint'))
        end = next(i for i in range(start, len(lines)) if lines[i] == "fi")
        return "\n".join(lines[start:end + 1])

    def test_the_pattern_is_passed_through_unexpanded(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "skills" / "postgres" / "references").mkdir(parents=True)
            (root / "skills" / "postgres" / "SKILL.md").write_text("# s\n")
            (root / "skills" / "postgres" / "references" / "notes.md").write_text("# n\n")
            stub_dir = root / "stub"
            stub_dir.mkdir()
            stub = stub_dir / "markdownlint-cli2"
            stub.write_text('#!/bin/sh\nfor a in "$@"; do echo "$a"; done\n')
            stub.chmod(0o755)

            script = f'set -eu\nmd_promoted="skills/postgres/**"\n{self.markdown_block()}\n'
            result = subprocess.run(
                ["sh", "-c", script], cwd=tmp, capture_output=True, text=True,
                env={"PATH": f"{stub_dir}:/usr/bin:/bin", "HOME": tmp}, check=True,
            )
            args = result.stdout.split("\n")
            self.assertIn("!skills/postgres/**", args)
            self.assertNotIn("!skills/postgres/SKILL.md", args)
            self.assertNotIn("!skills/postgres/references", args)
            self.assertIn("**/*.md", args)


if __name__ == "__main__":
    unittest.main()
