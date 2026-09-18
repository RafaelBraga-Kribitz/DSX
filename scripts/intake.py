#!/usr/bin/env python3
"""Intake for skills, agents and prompts brought in from elsewhere.

Drop them under intake/, one kind per folder:

    intake/skills/<name>/SKILL.md     -> skills/<name>/       (declared in the manifest)
    intake/agents/<name>.md           -> agents/<name>.md     (declared in the manifest)
    intake/prompts/<name>.md          -> prompts/<name>.md    (reference material)

Then:

    python3 scripts/intake.py                       # report
    python3 scripts/intake.py --json                # report, machine-readable
    python3 scripts/intake.py --promote <name>...   # move one or more out of intake/

Anything under intake/ that is not one of the three folders above is reported
as `unrecognised`, never skipped in silence: a folder this script cannot place
is the operator's to route, and a checker that ignores what it does not
understand is the same defect class as a gate that passes what it cannot read.

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

# The SAME pattern scripts/validate-capability.py enforces on every declared
# name (its KEBAB, line 45). It must not be looser: a promoted skill or agent is
# written into capabilities/dsx/capability.json, so a name intake admits but the
# manifest gate rejects turns ./scripts/check.sh red on the operator's next run.
# Measured before this was tied together: intake admitted "Good9" and
# "global--code-reviewer"; the manifest gate rejects both.
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
STOPWORDS = {
    "a", "an", "and", "any", "are", "as", "at", "be", "before", "by", "for",
    "from", "in", "into", "is", "it", "its", "of", "on", "or", "that", "the",
    "this", "to", "use", "when", "with", "without", "you", "your", "whenever",
    "after", "one", "someone", "else", "own", "made", "full",
}
OVERLAP_MIN_SHARED = 4

# One row per kind. `manifest_key` is None for a kind the capability manifest
# does not declare; `frontmatter` is False for a kind whose files are often
# written without any, which is normal for a prompt.
KINDS: dict[str, dict] = {
    "skill": {
        "intake_dir": "skills",
        "destination": "skills",
        "manifest_key": "skills",
        "frontmatter": True,
        "layout": "<name>/SKILL.md",
    },
    "agent": {
        "intake_dir": "agents",
        "destination": "agents",
        "manifest_key": "agents",
        "frontmatter": True,
        "layout": "<name>.md",
    },
    "prompt": {
        "intake_dir": "prompts",
        "destination": "prompts",
        "manifest_key": None,
        "frontmatter": False,
        "layout": "<name>.md",
    },
}
INTAKE_FILES_OK = {"README.md"}


@dataclass
class Item:
    name: str
    kind: str            # "skill" | "agent" | "prompt" | "unknown"
    path: str
    status: str          # "ok" | "collision" | "invalid" | "unrecognised"
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


def first_heading(text: str) -> str:
    """The first markdown heading, used as a stand-in description.

    A prompt usually carries no frontmatter, so its heading is the only
    self-description available for the report and the overlap hint.
    """
    match = HEADING_RE.search(text)
    return match.group(1).strip() if match else ""


def kebab(name: str) -> str:
    """The nearest name that satisfies NAME_RE, for the report's fix hint."""
    out = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return out or "unnamed"


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
    prompts_dir = root / "prompts"
    if prompts_dir.is_dir():
        for path in sorted(prompts_dir.glob("*.md")):
            if path.name not in INTAKE_FILES_OK:
                add(path.stem, f"prompts/{path.name}")
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


def _candidates(intake: Path) -> list[tuple[str, str, Path]]:
    """(name, kind, path) for every file a known kind claims."""
    out: list[tuple[str, str, Path]] = []
    for kind, spec in KINDS.items():
        base = intake / spec["intake_dir"]
        if not base.is_dir():
            continue
        if kind == "skill":
            for path in sorted(base.glob("*/SKILL.md")):
                out.append((path.parent.name, kind, path))
        else:
            for path in sorted(base.glob("*.md")):
                if path.name in INTAKE_FILES_OK:
                    continue
                out.append((path.stem, kind, path))
    return out


def _unrecognised(intake: Path, root: Path) -> list[Item]:
    """Everything under intake/ that no kind claims.

    Reported rather than skipped: a folder this script cannot place needs a
    decision, and silence would hide it.
    """
    out: list[Item] = []
    if not intake.is_dir():
        return out
    known_dirs = {spec["intake_dir"] for spec in KINDS.values()}

    for path in sorted(intake.iterdir()):
        if path.name.startswith("."):
            continue
        if path.is_dir():
            if path.name in known_dirs:
                continue
            files = [p for p in sorted(path.rglob("*")) if p.is_file()
                     and not p.name.startswith(".")]
            out.append(Item(
                name=path.name, kind="unknown", path=str(path.relative_to(root)) + "/",
                status="unrecognised", words=0,
                notes=[
                    f"{len(files)} file(s) in a folder no kind claims — intake reads only "
                    + ", ".join(sorted(f"intake/{d}/" for d in known_dirs)),
                    "move each file into one of those, or route it by hand",
                ],
            ))
        elif path.name not in INTAKE_FILES_OK:
            out.append(Item(
                name=path.name, kind="unknown", path=str(path.relative_to(root)),
                status="unrecognised", words=len(
                    path.read_text(encoding="utf-8", errors="replace").split()),
                notes=["a loose file directly under intake/; move it into a kind folder"],
            ))

    # A folder under intake/skills/ with no SKILL.md is claimed by no candidate
    # and would otherwise vanish from the report entirely.
    skills = intake / "skills"
    if skills.is_dir():
        for path in sorted(p for p in skills.iterdir() if p.is_dir()):
            if not (path / "SKILL.md").exists():
                out.append(Item(
                    name=path.name, kind="skill", path=str(path.relative_to(root)) + "/",
                    status="invalid", notes=["no SKILL.md in the folder"],
                ))

    # A non-markdown file sitting in a flat-file kind folder.
    for kind, spec in KINDS.items():
        if kind == "skill":
            continue
        base = intake / spec["intake_dir"]
        if not base.is_dir():
            continue
        for path in sorted(p for p in base.iterdir() if p.is_file()):
            if path.suffix.lower() != ".md" and not path.name.startswith("."):
                out.append(Item(
                    name=path.name, kind=kind, path=str(path.relative_to(root)),
                    status="unrecognised",
                    notes=[(f"not a .md file; {kind}s are read as "
                            f"intake/{spec['intake_dir']}/{spec['layout']}")],
                ))
    return out


def scan(root: Path) -> list[Item]:
    intake = root / "intake"
    taken = existing_names(root)
    shipped = existing_descriptions(root)
    items: list[Item] = []

    for expected_name, kind, path in _candidates(intake):
        spec = KINDS[kind]
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = str(path.relative_to(root))
        item = Item(name=expected_name, kind=kind, path=rel, status="ok",
                    words=len(text.split()))
        fm = parse_frontmatter(text)

        if fm is None:
            if spec["frontmatter"]:
                item.status = "invalid"
                item.notes.append("no YAML frontmatter block")
            else:
                item.description = first_heading(text)
                item.notes.append("no frontmatter — described by its first heading")
        else:
            name = fm.get("name", "")
            desc = fm.get("description", "")
            item.description = desc or first_heading(text)
            if name and not NAME_RE.match(name):
                item.status = "invalid"
                item.notes.append(
                    f"name {name!r} is not lower-case kebab, which the manifest gate "
                    f"requires — use {kebab(name)!r}"
                )
            elif name and name != expected_name:
                item.status = "invalid"
                item.notes.append(f"frontmatter name {name!r} does not match path")
            elif not name and spec["frontmatter"]:
                item.status = "invalid"
                item.notes.append("frontmatter has no name")
            if not desc and spec["frontmatter"]:
                item.status = "invalid"
                item.notes.append("frontmatter has no description")

        if not NAME_RE.match(expected_name):
            item.status = "invalid"
            item.notes.append(
                f"path name {expected_name!r} is not lower-case kebab, which the "
                f"manifest gate requires — rename it to {kebab(expected_name)!r}"
            )

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

    items.extend(_unrecognised(intake, root))

    # Names must be unique ACROSS intake, not just against what is already
    # shipped. promote() looks an item up by name; two items sharing one name
    # meant the lookup silently kept whichever sorted last, moved it, and left
    # the other behind reporting `ok` — measured, with exit 0 and no warning.
    by_name: dict[str, list[Item]] = {}
    for item in items:
        by_name.setdefault(item.name, []).append(item)
    for name, group in by_name.items():
        if len(group) < 2:
            continue
        for item in group:
            others = [o.path for o in group if o is not item]
            if item.status == "ok":
                item.status = "collision"
            item.notes.append(
                f"name {name!r} is claimed by {len(group)} items under intake/: "
                + ", ".join(sorted(others))
            )

    items.sort(key=lambda i: (i.kind, i.name))
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


def promote_one(root: Path, name: str, items: dict[str, list[Item]]) -> int:
    group = items.get(name) or []
    if len(group) > 1:
        print(f"intake: {name!r} is ambiguous — {len(group)} items claim it: "
              + ", ".join(sorted(i.path for i in group))
              + ". Rename one before promoting.", file=sys.stderr)
        return 1
    item = group[0] if group else None
    if item is None:
        print(f"intake: no item named {name!r} under intake/", file=sys.stderr)
        return 1
    if item.status != "ok":
        print(f"intake: {name} is {item.status}: {'; '.join(item.notes)}", file=sys.stderr)
        return 1

    spec = KINDS[item.kind]
    src = root / item.path
    dst_dir = root / spec["destination"]
    dst_dir.mkdir(parents=True, exist_ok=True)

    if item.kind == "skill":
        dst = dst_dir / name
        shutil.move(str(src.parent), str(dst))
    else:
        dst = dst_dir / f"{name}.md"
        shutil.move(str(src), str(dst))

    declared = ""
    key = spec["manifest_key"]
    if key:
        manifest = root / "capabilities" / "dsx" / "capability.json"
        if manifest.exists():
            declare_in_manifest(manifest, key, name)
            declared = f" and declared in {manifest.relative_to(root)}"

    print(f"promoted {item.kind} {name} -> {dst.relative_to(root)}{declared}")
    if item.kind == "skill":
        print("      add a row to skills/using-dsx/SKILL.md if it should be routed to by name")
    elif item.kind == "prompt":
        print("      prompts are reference material: nothing loads them automatically.")
        print("      A prompt that encodes a repeatable workflow belongs in skills/ instead.")
    return 0


def promote(root: Path, names: list[str]) -> int:
    # One scan for the whole batch, re-scanning between moves so a later name
    # still resolves after an earlier promotion changed the tree.
    def index(root: Path) -> dict[str, list[Item]]:
        out: dict[str, list[Item]] = {}
        for i in scan(root):
            out.setdefault(i.name, []).append(i)
        return out

    failures = 0
    for name in names:
        failures += promote_one(root, name, index(root))
    print("next: python3 scripts/validate-capability.py && ./scripts/check.sh")
    return 1 if failures else 0


# ── report ───────────────────────────────────────────────────────────────────


def report(items: list[Item], as_json: bool) -> int:
    if as_json:
        print(json.dumps([asdict(i) for i in items], indent=2))
        return 0
    if not items:
        layouts = "  ".join(
            f"intake/{spec['intake_dir']}/{spec['layout']}" for spec in KINDS.values()
        )
        print(f"intake/ is empty. Drop files in:\n  {layouts}")
        return 0
    width = max(*(len(i.name) for i in items), len("name"))
    print(f"{'name':<{width}}  kind    status        words  notes")
    for i in items:
        notes = "; ".join(i.notes) if i.notes else "-"
        print(f"{i.name:<{width}}  {i.kind:<7} {i.status:<13} {i.words:>5}  {notes}")

    ok = [i for i in items if i.status == "ok"]
    unrecognised = [i for i in items if i.status == "unrecognised"]
    print(f"\n{len(ok)}/{len(items)} promotable.")
    if ok:
        print("  python3 scripts/intake.py --promote " + " ".join(i.name for i in ok))
    if unrecognised:
        print(f"  {len(unrecognised)} unrecognised — route by hand, nothing was skipped silently.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--root", default=None,
                        help="project root (default: parent of scripts/)")
    parser.add_argument("--json", action="store_true", help="machine-readable report")
    parser.add_argument("--promote", metavar="NAME", nargs="+",
                        help="move one or more items out of intake/")
    args = parser.parse_args(argv)
    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent
    if args.promote:
        return promote(root, args.promote)
    return report(scan(root), args.json)


if __name__ == "__main__":
    sys.exit(main())
