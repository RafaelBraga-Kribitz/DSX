#!/usr/bin/env python3
"""Which skills, agents and prompts this project's house style applies to.

`skills/`, `agents/` and `prompts/` hold two kinds of material. Some of it was
written here and reads like the rest of the repository. The rest arrived through
`intake/` from someone else's library, was promoted unchanged, and is loaded by
the harness exactly as it was written.

Holding the second kind to this project's line length, heading style and import
order would make `./scripts/check.sh` fail for a reason the operator cannot act
on -- their own skill is not wrong, it is just not ours. Measured on the first
real drop: 19 promoted skills carried 16 ruff findings and 2,631 markdownlint
findings, while the 15 written here carried none.

So style stops at the border, and correctness does not: `scripts/check.sh`
excludes the promoted material from the full rule set and then runs ruff's `F`
rules over it, which is the family that catches an undefined name or an unused
import -- a real error, in anyone's house style.

The border is the naming convention, not a list to keep up to date. Everything
written here is named `dsx-*`, plus the always-on `using-dsx` and the `README`
of each folder. A promoted item keeps the name its author gave it.

    python3 scripts/lint-scope.py              # promoted paths, one per line
    python3 scripts/lint-scope.py --ruff       # promoted skill directories
    python3 scripts/lint-scope.py --markdown   # promoted paths as globs
    python3 scripts/lint-scope.py --authored   # the paths written here
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# A skill is a directory; an agent and a prompt are single markdown files.
FOLDERS = {"skills": "dir", "agents": "file", "prompts": "file"}


def is_authored_here(name: str) -> bool:
    """True when `name` is this project's own work rather than promoted material.

    `name` is the skill's folder name, or the agent's or prompt's file stem.
    """
    return name == "using-dsx" or name == "README" or name.startswith("dsx-")


def classify(root: Path = ROOT) -> tuple[list[str], list[str]]:
    """Return (authored here, promoted), each a sorted list of relative paths."""
    authored: list[str] = []
    promoted: list[str] = []
    for folder, shape in sorted(FOLDERS.items()):
        base = root / folder
        if not base.is_dir():
            continue
        for entry in sorted(base.iterdir()):
            if shape == "dir":
                if not entry.is_dir():
                    continue
                name = entry.name
            else:
                if entry.is_dir() or entry.suffix != ".md":
                    continue
                name = entry.stem
            rel = f"{folder}/{entry.name}"
            (authored if is_authored_here(name) else promoted).append(rel)
    return authored, promoted


def as_glob(path: str) -> str:
    """A path a markdownlint negation argument can use."""
    return path if path.endswith(".md") else f"{path}/**"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--ruff", action="store_true",
                       help="only the promoted skill directories (ruff reads no markdown)")
    group.add_argument("--markdown", action="store_true",
                       help="promoted paths as globs, for markdownlint negation arguments")
    group.add_argument("--authored", action="store_true",
                       help="the paths written here, which the full rule set applies to")
    args = parser.parse_args(argv)

    authored, promoted = classify()
    if args.authored:
        lines = authored
    elif args.ruff:
        lines = [p for p in promoted if not p.endswith(".md")]
    elif args.markdown:
        lines = [as_glob(p) for p in promoted]
    else:
        lines = promoted
    for line in lines:
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
