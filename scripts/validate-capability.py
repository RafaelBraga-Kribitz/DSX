#!/usr/bin/env python3
"""Validate capability.json against the GSD capability contract before shipping.

GSD validates the manifest at install time; failing there means a broken install
for the user. This re-implements the conformance rules from the ADR-894 /
ADR-1016 manifest reference so the failure happens here instead.

    python3 scripts/validate-capability.py

Beyond the manifest reference it also cross-checks the manifest against this
repository: agent frontmatter (parsed up to its closing ``---``), fragments on
disk that nothing references, and every gate command's ``dsx gate <point>``
and flags against the real argparse parser in dsx.cli, so a renamed flag or
profile breaks here instead of in every user's loop.
"""

from __future__ import annotations

import contextlib
import io
import json
import re
import shlex
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "capabilities" / "dsx" / "capability.json"

# The closed vocabulary of loop extension points (12, additive-only).
POINTS = {
    "discuss:pre", "discuss:post",
    "plan:pre", "plan:post",
    "execute:pre", "execute:wave:pre", "execute:wave:post", "execute:post",
    "verify:pre", "verify:post",
    "ship:pre", "ship:post",
}

# Agent roles published by each step, from gsd-core/bin/lib/loop-host-contract.cjs.
ROLES_BY_POINT = {
    "discuss:pre": {"orchestrator"}, "discuss:post": {"orchestrator"},
    "plan:pre": {"researcher", "planner", "checker"},
    "plan:post": {"researcher", "planner", "checker"},
    "execute:pre": {"executor", "verifier"}, "execute:wave:pre": {"executor", "verifier"},
    "execute:wave:post": {"executor", "verifier"}, "execute:post": {"executor", "verifier"},
    "verify:pre": {"orchestrator"}, "verify:post": {"orchestrator"},
    "ship:pre": {"orchestrator"}, "ship:post": {"orchestrator"},
}

RESERVED_PREFIXES = ("gsd-", "gsd-core-", "anthropic-")
TIERS = {"core", "standard", "full"}
ON_ERROR = {"skip", "halt"}
CONFIG_TYPES = {"boolean", "string", "number", "enum"}
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SEMVER = re.compile(r"^\d+\.\d+\.\d+")
COMMAND_MAX_LENGTH = 4096


def main() -> int:
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: cannot read {MANIFEST}: {exc}", file=sys.stderr)
        return 1

    errors, warnings = validate(manifest, ROOT, MANIFEST.parent)

    # ── report ───────────────────────────────────────────────────────────────
    for warning in warnings:
        print(f"warn: {warning}")
    if errors:
        print(f"\nFAIL: {len(errors)} conformance error(s)", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print(
        f"capability '{manifest.get('id', '')}' v{manifest['version']} is conformant: "
        f"{len(manifest.get('steps') or [])} steps, "
        f"{len(manifest.get('contributions') or [])} contributions, "
        f"{len(manifest.get('gates') or [])} gates, "
        f"{len(manifest.get('skills') or [])} skills, {len(manifest.get('agents') or [])} agents, "
        f"{len(manifest.get('config') or {})} config keys"
    )
    return 0


def validate(manifest: dict, root: Path, cap_dir: Path) -> tuple[list[str], list[str]]:
    """Return (errors, warnings) for ``manifest`` read from ``cap_dir`` under ``root``."""
    errors: list[str] = []
    warnings: list[str] = []

    cap_id = manifest.get("id", "")

    # ── envelope ─────────────────────────────────────────────────────────────
    if not KEBAB.match(cap_id):
        errors.append(f"id {cap_id!r} must be kebab-case")
    if cap_id != cap_dir.name:
        errors.append(f"id {cap_id!r} must equal the folder name {cap_dir.name!r}")
    if cap_id.startswith(RESERVED_PREFIXES):
        errors.append(f"id {cap_id!r} uses a reserved prefix ({', '.join(RESERVED_PREFIXES)})")
    if manifest.get("role") != "feature":
        errors.append("role must be 'feature'")
    if not SEMVER.match(str(manifest.get("version", ""))):
        errors.append("version must be semver")
    for field in ("title", "description"):
        if not str(manifest.get(field, "")).strip():
            errors.append(f"{field} must be a non-empty string")
    if manifest.get("tier") not in TIERS:
        errors.append(f"tier must be one of {sorted(TIERS)}")
    if not isinstance(manifest.get("requires"), list):
        errors.append("requires must be present as an array")

    compat = manifest.get("runtimeCompat")
    if not isinstance(compat, dict):
        errors.append("runtimeCompat is required for a feature capability")
    else:
        supported = compat.get("supported")
        if not isinstance(supported, list) or not supported:
            errors.append("runtimeCompat.supported must be a non-empty array")
        elif "*" in supported and len(supported) > 1:
            errors.append("runtimeCompat.supported may not mix '*' with concrete ids")
        if "*" in (compat.get("unsupported") or []):
            errors.append("runtimeCompat.unsupported may not contain '*'")

    # ── owned artefacts ──────────────────────────────────────────────────────
    skills = manifest.get("skills") or []
    agents = manifest.get("agents") or []
    for name in skills + agents:
        if name.startswith(RESERVED_PREFIXES):
            errors.append(f"{name!r} uses a reserved prefix")
        if not KEBAB.match(name):
            errors.append(f"{name!r} must be kebab-case")
    if len(set(skills)) != len(skills):
        errors.append("duplicate skill stem")
    if len(set(agents)) != len(agents):
        errors.append("duplicate agent stem")

    for name in skills:
        if not (root / "skills" / name / "SKILL.md").exists():
            errors.append(f"declared skill {name!r} has no skills/{name}/SKILL.md")
    for name in agents:
        path = root / "agents" / f"{name}.md"
        if not path.exists():
            errors.append(f"declared agent {name!r} has no agents/{name}.md")
        else:
            agent_errors, agent_warnings = check_agent_frontmatter(path, name)
            errors.extend(agent_errors)
            warnings.extend(agent_warnings)

    # Every file on disk should be declared, or it will not install.
    for path in sorted((root / "agents").glob("*.md")):
        if path.stem not in agents:
            warnings.append(f"agents/{path.name} exists but is not declared in the manifest")
    for path in sorted(p for p in (root / "skills").iterdir() if p.is_dir()):
        if path.name not in skills:
            warnings.append(f"skills/{path.name}/ exists but is not declared in the manifest")

    # ── config ───────────────────────────────────────────────────────────────
    for key, schema in (manifest.get("config") or {}).items():
        if not key.startswith(f"{cap_id}."):
            warnings.append(
                f"config key {key!r} is outside the '{cap_id}.' namespace — collision risk "
                "with core or another capability"
            )
        if schema.get("type") not in CONFIG_TYPES:
            errors.append(f"config {key!r}: type must be one of {sorted(CONFIG_TYPES)}")
        if "default" not in schema:
            errors.append(f"config {key!r}: default is required")
        if not str(schema.get("description", "")).strip():
            errors.append(f"config {key!r}: description is required")
        if schema.get("type") == "enum":
            values = schema.get("values")
            if not isinstance(values, list) or not values:
                errors.append(f"config {key!r}: enum requires a non-empty values array")
            elif schema.get("default") not in values:
                errors.append(f"config {key!r}: default is not in values")
        elif schema.get("type") == "boolean" and not isinstance(schema.get("default"), bool):
            errors.append(f"config {key!r}: default must be a boolean")

    config_keys = set(manifest.get("config") or {})

    def check_when(when: str | None, where: str) -> None:
        if when and when not in config_keys:
            errors.append(f"{where}: when={when!r} is not a config key this capability owns")

    # ── steps ────────────────────────────────────────────────────────────────
    produced_per_point: dict[str, set[str]] = {}
    for index, step in enumerate(manifest.get("steps") or []):
        where = f"steps[{index}]"
        point = step.get("point")
        if point not in POINTS:
            errors.append(f"{where}: point {point!r} is not one of the 12 loop extension points")
        ref = step.get("ref")
        if not isinstance(ref, dict) or len(ref) != 1:
            errors.append(f"{where}: ref must be exactly one of skill | agent | command")
        else:
            kind, name = next(iter(ref.items()))
            if kind == "skill" and name not in skills:
                errors.append(f"{where}: ref.skill {name!r} is not declared in skills")
            if kind == "agent" and name not in agents:
                errors.append(f"{where}: ref.agent {name!r} is not declared in agents")
            if kind not in ("skill", "agent", "command"):
                errors.append(f"{where}: ref kind {kind!r} is invalid")
        for field in ("produces", "consumes"):
            if not isinstance(step.get(field), list):
                errors.append(f"{where}: {field} must be present as an array")
        if step.get("onError") not in ON_ERROR:
            errors.append(f"{where}: onError must be 'skip' or 'halt'")
        check_when(step.get("when"), where)
        _check_fragment(step.get("fragment"), where, errors, cap_dir)

        bucket = produced_per_point.setdefault(point or "?", set())
        for artefact in step.get("produces") or []:
            if artefact in bucket:
                errors.append(f"{where}: {artefact!r} is produced twice at {point}")
            bucket.add(artefact)

    # ── contributions ────────────────────────────────────────────────────────
    for index, contribution in enumerate(manifest.get("contributions") or []):
        where = f"contributions[{index}]"
        point = contribution.get("point")
        if point not in POINTS:
            errors.append(f"{where}: point {point!r} is invalid")
        else:
            role = contribution.get("into")
            allowed = ROLES_BY_POINT[point]
            if role not in allowed:
                errors.append(
                    f"{where}: into={role!r} is not published at {point} (allowed: {sorted(allowed)})"
                )
        for field in ("produces", "consumes"):
            if not isinstance(contribution.get(field), list):
                errors.append(f"{where}: {field} must be present as an array")
        if not isinstance(contribution.get("fragment"), dict):
            errors.append(f"{where}: fragment is required")
        _check_fragment(contribution.get("fragment"), where, errors, cap_dir)
        check_when(contribution.get("when"), where)
        if contribution.get("onError") not in ON_ERROR | {None}:
            errors.append(f"{where}: onError must be 'skip' or 'halt'")

    # ── gates ────────────────────────────────────────────────────────────────
    for index, gate in enumerate(manifest.get("gates") or []):
        where = f"gates[{index}]"
        if gate.get("point") not in POINTS:
            errors.append(f"{where}: point {gate.get('point')!r} is invalid")
        check = gate.get("check")
        if not isinstance(check, dict):
            errors.append(f"{where}: check must be an object")
        else:
            shapes = [k for k in ("query", "predicate", "agentVerdict") if k in check]
            if len(shapes) != 1:
                errors.append(f"{where}: check must carry exactly one of query|predicate|agentVerdict")
            elif shapes[0] == "predicate":
                predicate = check["predicate"]
                if predicate.get("kind") != "command-exit-zero":
                    errors.append(f"{where}: unknown predicate kind {predicate.get('kind')!r}")
                command = predicate.get("command", "")
                if not isinstance(command, str) or not command.strip():
                    errors.append(f"{where}: predicate.command must be a non-empty string")
                elif len(command) > COMMAND_MAX_LENGTH:
                    errors.append(f"{where}: predicate.command exceeds {COMMAND_MAX_LENGTH} chars")
                else:
                    for placeholder in re.findall(r"\$\{([A-Z_]+)\}", command):
                        if placeholder not in ("PHASE_NUMBER", "PHASE_DIR", "PHASE_REQ_IDS"):
                            warnings.append(
                                f"{where}: ${{{placeholder}}} is not a GSD gate placeholder — "
                                "it will be left for sh to expand"
                            )
                    errors.extend(f"{where}: {problem}" for problem in check_gate_command(command))
                timeout = predicate.get("timeout")
                if timeout is not None and (
                    not isinstance(timeout, (int, float)) or timeout <= 0
                ):
                    errors.append(f"{where}: predicate.timeout must be a positive number")
            elif shapes[0] == "agentVerdict" and gate.get("blocking"):
                errors.append(f"{where}: agentVerdict gates may not be blocking")
        if not isinstance(gate.get("blocking"), bool):
            errors.append(f"{where}: blocking must be present and boolean")
        if gate.get("onError") not in ON_ERROR:
            errors.append(f"{where}: onError must be 'skip' or 'halt'")
        check_when(gate.get("when"), where)

    # ── fragments nobody references ──────────────────────────────────────────
    warnings.extend(orphan_fragments(manifest, cap_dir))

    return errors, warnings


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Top-level ``key: value`` pairs between the opening and closing ``---``.

    Returns None when the file does not open with ``---`` or never closes it.
    Only the frontmatter block is read: a ``name: x`` line in the body must not
    satisfy a check about the frontmatter.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        match = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip().strip("\"'")
    return None


def check_agent_frontmatter(path: Path, name: str) -> tuple[list[str], list[str]]:
    """Errors and warnings for one agent file's frontmatter."""
    errors: list[str] = []
    warnings: list[str] = []
    rel = f"agents/{path.name}"
    fields = parse_frontmatter(path.read_text(encoding="utf-8"))
    if fields is None:
        errors.append(f"{rel} has no frontmatter (or it is never closed with ---)")
        return errors, warnings
    if fields.get("name") != name:
        errors.append(f"{rel} frontmatter name {fields.get('name')!r} does not match {name!r}")
    if not fields.get("description"):
        errors.append(f"{rel} frontmatter has no description")
    if "tools" not in fields:
        warnings.append(f"{rel} frontmatter has no tools line — the agent inherits every tool")
    return errors, warnings


def orphan_fragments(manifest: dict, cap_dir: Path) -> list[str]:
    """Warnings for fragments/*.md that no step or contribution points at."""
    referenced = set()
    for item in (manifest.get("steps") or []) + (manifest.get("contributions") or []):
        fragment = item.get("fragment")
        if isinstance(fragment, dict) and isinstance(fragment.get("path"), str):
            referenced.add(Path(fragment["path"]).as_posix())
    return [
        f"fragments/{path.name} exists but no step or contribution references it"
        for path in sorted((cap_dir / "fragments").glob("*.md"))
        if f"fragments/{path.name}" not in referenced
    ]


_SHELL_SEPARATORS = {";", "&&", "||", "|", "&"}


def check_gate_command(command: str) -> list[str]:
    """Problems with the ``dsx gate <point> ...`` call inside a gate command.

    The point must be a key of dsx.cli.GATE_PROFILES and every flag must be one
    the real ``dsx gate`` argparse parser accepts. Placeholders such as
    ``${PHASE_DIR}`` are kept as literal argument values, which argparse takes
    as-is. A command that does not invoke ``dsx gate`` is not dsx's to judge.
    """
    try:
        lexer = shlex.shlex(command, posix=True, punctuation_chars=True)
        lexer.whitespace_split = True
        tokens = list(lexer)
    except ValueError as exc:
        return [f"predicate.command does not parse as shell words: {exc}"]

    calls = []
    for i, token in enumerate(tokens[:-1]):
        if tokens[i + 1] == "gate" and (token in ("$DSX", "${DSX}") or token.rsplit("/", 1)[-1] == "dsx"):
            args = []
            for arg in tokens[i + 2:]:
                if arg in _SHELL_SEPARATORS:
                    break
                args.append(arg)
            calls.append(args)
    if not calls:
        return []

    try:
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))
        from dsx.cli import GATE_PROFILES, build_parser
    except Exception as exc:  # noqa: BLE001 - report any import failure as a finding
        return [f"cannot import dsx.cli to cross-check the gate command: {exc}"]

    problems = []
    for args in calls:
        if not args:
            problems.append("`dsx gate` is called without a point")
            continue
        point = args[0]
        if point not in GATE_PROFILES:
            problems.append(
                f"`dsx gate {point}` is not a gate profile (dsx.cli.GATE_PROFILES: {sorted(GATE_PROFILES)})"
            )
            continue
        err = io.StringIO()
        try:
            with contextlib.redirect_stderr(err):
                _namespace, unknown = build_parser().parse_known_args(["gate", *args])
        except SystemExit:
            message = err.getvalue().strip().splitlines()
            problems.append(f"`dsx gate {' '.join(args)}` is rejected by dsx.cli: "
                            f"{message[-1] if message else 'argparse error'}")
            continue
        if unknown:
            problems.append(f"`dsx gate {point}` does not accept {' '.join(unknown)}")
    return problems


def _check_fragment(fragment, where: str, errors: list[str], cap_dir: Path) -> None:
    if fragment is None:
        return
    if not isinstance(fragment, dict) or len(fragment) != 1:
        errors.append(f"{where}: fragment must be exactly one of path | inline")
        return
    if "path" in fragment:
        rel = fragment["path"]
        if ".." in Path(rel).parts:
            errors.append(f"{where}: fragment path {rel!r} escapes the capability directory")
        elif not (cap_dir / rel).exists():
            errors.append(f"{where}: fragment path {rel!r} does not exist")
    elif "inline" not in fragment:
        errors.append(f"{where}: fragment must carry path or inline")


if __name__ == "__main__":
    sys.exit(main())
