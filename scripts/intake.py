#!/usr/bin/env python3
"""Intake for skills and agents brought in from elsewhere.

Drop folders into intake/skills/<name>/SKILL.md and files into
intake/agents/<name>.md, then:

    python3 scripts/intake.py                    # report
    python3 scripts/intake.py --json             # report, machine-readable
    python3 scripts/intake.py --promote <name>   # move into skills/ or agents/
                                                 # and declare it in the manifest

Stdlib only, like everything else here.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9-]*$")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
STOPWORDS = {
    "a", "an", "and", "any", "are", "as", "at", "be", "before", "by", "for",
    "from", "in", "into", "is", "it", "its", "of", "on", "or", "that", "the",
    "this", "to", "use", "when", "with", "without", "you", "your", "whenever",
    "after", "one", "someone", "else", "own", "made", "full",
}
OVERLAP_MIN_SHARED = 4


@dataclass
class Item:
    name: str
    kind: str            # "skill" | "agent"
    path: str
    status: str          # "ok" | "collision" | "invalid"
    words: int = 0
    description: str = ""
    notes: list[str] = field(default_factory=list)


# ── frontmatter ──────────────────────────────────────────────────────────────


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Return the top-level scalar keys of a YAML frontmatter block, or None.

    This reads only ``key: value`` lines at column zero. Nested keys and lists
    are ignored — the intake checker needs ``name`` and ``description``, and
    both are scalars in every skill and agent format this project knows.
    """
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line or line[0] in " \t#":
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        result[key.strip()] = value
    return result


def content_words(text: str) -> set[str]:
    return {
        w for w in re.findall(r"[a-z][a-z0-9-]{2,}", text.lower())
        if w not in STOPWORDS
    }


# ── discovery ────────────────────────────────────────────────────────────────


def existing_names(root: Path) -> dict[str, list[str]]:
    """Every name already taken, and where it lives."""
    taken: dict[str, list[str]] = {}

    def add(name: str, where: str) -> None:
        taken.setdefault(name, []).append(where)

    skills_dir = root / "skills"
    if skills_dir.is_dir():
        for path in sorted(skills_dir.iterdir()):
            if path.is_dir() and (path / "SKILL.md").exists():
                add(path.name, f"skills/{path.name}/")
    agents_dir = root / "agents"
    if agents_dir.is_dir():
        for path in sorted(agents_dir.glob("*.md")):
            add(path.stem, f"agents/{path.name}")
    manifest = root / "capabilities" / "dsx" / "capability.json"
    if manifest.exists():
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            data = {}
        for name in data.get("skills") or []:
            add(name, "capability.json skills[]")
        for name in data.get("agents") or []:
            add(name, "capability.json agents[]")
    return taken


def existing_descriptions(root: Path) -> list[tuple[str, set[str]]]:
    """(name, content words) for every shipped skill and agent, for overlap hints."""
    out: list[tuple[str, set[str]]] = []
    for path in sorted((root / "skills").glob("*/SKILL.md")):
        fm = parse_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
        if fm and fm.get("description"):
            out.append((path.parent.name, content_words(fm["description"])))
    for path in sorted((root / "agents").glob("*.md")):
        fm = parse_frontmatter(path.read_text(encoding="utf-8", errors="replace"))
        if fm and fm.get("description"):
            out.append((path.stem, content_words(fm["description"])))
    return out


def scan(root: Path) -> list[Item]:
    intake = root / "intake"
    taken = existing_names(root)
    shipped = existing_descriptions(root)
    items: list[Item] = []

    candidates: list[tuple[str, str, Path]] = []
    for path in sorted((intake / "skills").glob("*/SKILL.md")):
        candidates.append((path.parent.name, "skill", path))
    for path in sorted((intake / "agents").glob("*.md")):
        candidates.append((path.stem, "agent", path))

    for expected_name, kind, path in candidates:
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = str(path.relative_to(root))
        item = Item(name=expected_name, kind=kind, path=rel, status="ok",
                    words=len(text.split()))
        fm = parse_frontmatter(text)
        if fm is None:
            item.status = "invalid"
            item.notes.append("no YAML frontmatter block")
        else:
            name = fm.get("name", "")
            desc = fm.get("description", "")
            item.description = desc
            if not name:
                item.status = "invalid"
                item.notes.append("frontmatter has no name")
            elif not NAME_RE.match(name):
                item.status = "invalid"
                item.notes.append(f"name {name!r} must be letters, digits and hyphens")
            elif name != expected_name:
                item.status = "invalid"
                item.notes.append(f"frontmatter name {name!r} does not match path")
            if not desc:
                item.status = "invalid"
                item.notes.append("frontmatter has no description")
        if item.status == "ok" and expected_name in taken:
            item.status = "collision"
            item.notes.append("name already used by " + ", ".join(taken[expected_name]))
        if item.description:
            mine = content_words(item.description)
            for other, theirs in shipped:
                shared = mine & theirs
                if len(shared) >= OVERLAP_MIN_SHARED:
                    item.notes.append(
                        f"possible overlap with {other} ({', '.join(sorted(shared)[:5])})"
                    )
        items.append(item)
    return items


# ── promote ──────────────────────────────────────────────────────────────────


def declare_in_manifest(manifest_path: Path, key: str, name: str) -> None:
    """Append ``name`` to the manifest's ``key`` array in place.

    Edits the text rather than re-serialising, so the hand-formatted file
    keeps its layout. Validates the result parses before writing.
    """
    text = manifest_path.read_text(encoding="utf-8")
    pattern = re.compile(rf'("{re.escape(key)}"\s*:\s*\[)(.*?)(\s*\])', re.DOTALL)
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"intake: cannot find \"{key}\": [...] in {manifest_path}")
    head, body, tail = match.group(1), match.group(2), match.group(3)
    if re.search(rf'"{re.escape(name)}"', body):
        return
    stripped = body.rstrip()
    if stripped.strip():
        indent = re.match(r"\s*", body.split("\n", 1)[-1] if "\n" in body else "").group(0) or "    "
        new_body = f"{stripped},\n{indent}\"{name}\""
    else:
        new_body = f"\n    \"{name}\""
    new_text = text[:match.start()] + head + new_body + tail + text[match.end():]
    json.loads(new_text)  # must still parse
    manifest_path.write_text(new_text, encoding="utf-8")


def promote(root: Path, name: str) -> int:
    items = {i.name: i for i in scan(root)}
    item = items.get(name)
    if item is None:
        print(f"intake: no item named {name!r} under intake/", file=sys.stderr)
        return 1
    if item.status != "ok":
        print(f"intake: {name} is {item.status}: {'; '.join(item.notes)}", file=sys.stderr)
        return 1
    src = root / item.path
    if item.kind == "skill":
        dst = root / "skills" / name
        shutil.move(str(src.parent), str(dst))
        key = "skills"
    else:
        dst = root / "agents" / f"{name}.md"
        shutil.move(str(src), str(dst))
        key = "agents"
    manifest = root / "capabilities" / "dsx" / "capability.json"
    if manifest.exists():
        declare_in_manifest(manifest, key, name)
        declared = f" and declared in {manifest.relative_to(root)}"
    else:
        declared = ""
    print(f"promoted {item.kind} {name} -> {dst.relative_to(root)}{declared}")
    print("next: python3 scripts/validate-capability.py && ./scripts/check.sh")
    if item.kind == "skill":
        print("      add a row to skills/using-dsx/SKILL.md if it should be routed to by name")
    return 0


# ── report ───────────────────────────────────────────────────────────────────


def report(items: list[Item], as_json: bool) -> int:
    if as_json:
        print(json.dumps([asdict(i) for i in items], indent=2))
        return 0
    if not items:
        print("intake/ is empty. Drop skills into intake/skills/<name>/SKILL.md "
              "and agents into intake/agents/<name>.md.")
        return 0
    width = max(len(i.name) for i in items)
    print(f"{'name':<{width}}  kind   status     words  notes")
    for i in items:
        notes = "; ".join(i.notes) if i.notes else "-"
        print(f"{i.name:<{width}}  {i.kind:<6} {i.status:<10} {i.words:>5}  {notes}")
    ok = sum(1 for i in items if i.status == "ok")
    print(f"\n{ok}/{len(items)} promotable. "
          "python3 scripts/intake.py --promote <name>")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--root", default=None,
                        help="project root (default: parent of scripts/)")
    parser.add_argument("--json", action="store_true", help="machine-readable report")
    parser.add_argument("--promote", metavar="NAME", help="move NAME out of intake/")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent
    if args.promote:
        return promote(root, args.promote)
    return report(scan(root), args.json)


if __name__ == "__main__":
    sys.exit(main())
