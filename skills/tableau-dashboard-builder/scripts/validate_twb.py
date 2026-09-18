#!/usr/bin/env python3
"""Validate Tableau TWB/TWBX for common anti-patterns and packaging invariants."""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

FAIL = "[FAIL]"
PASS = "[PASS]"
WARN = "[WARN]"


def check_xml_parse(twb_path: Path) -> tuple[bool, str]:
    try:
        ET.parse(twb_path)
        return True, f"{PASS} TWB XML parses cleanly"
    except ET.ParseError as exc:
        return False, f"{FAIL} TWB XML parse error: {exc}"


def check_measure_values(content: str) -> tuple[bool, str]:
    if "[:Measure Values]" in content:
        return False, f"{FAIL} Found deprecated [:Measure Values] (use [Multiple Values])"
    return True, f"{PASS} No [:Measure Values] references"


def check_multiple_values(content: str) -> tuple[bool, str]:
    count = content.count("[Multiple Values]")
    if count == 0:
        return True, f"{WARN} No [Multiple Values] references (ok if no pivot sheets)"
    return True, f"{PASS} Found {count} [Multiple Values] reference(s)"


def check_raw_measure_names_members(content: str) -> tuple[bool, str]:
    """Raw members look like member='&quot;[field]&quot;' without datasource prefix."""
    pattern = re.compile(
        r"level='\[:Measure Names\]' member='&quot;\[[^\]]+\]&quot;'"
    )
    raw = pattern.findall(content)
    if raw:
        return False, f"{FAIL} Found {len(raw)} raw Measure Names member(s) (need [ds].[sum:field:qk])"
    return True, f"{PASS} No raw Measure Names members"


def check_scoped_measure_names(content: str) -> tuple[bool, str]:
    pattern = re.compile(r"level='\[:Measure Names\]' member='")
    members = pattern.findall(content)
    if not members:
        return True, f"{PASS} No Measure Names filters (ok)"
    scoped = len(re.findall(r"\]\.\[(sum|avg|usr|none|pcto):", content))
    if scoped == 0 and members:
        return False, f"{FAIL} Measure Names filters present but no scoped column instances in members"
    return True, f"{PASS} Measure Names members appear datasource-scoped"


def check_extract_relations(content: str) -> tuple[bool, str]:
    extracts = content.count("<extract ")
    relations = content.count("relation name='Extract'")
    if extracts == 0:
        return True, f"{WARN} No <extract> blocks (Desktop-only CSV workbook?)"
    if relations < extracts:
        return False, f"{FAIL} {extracts} extract(s) but only {relations} Extract relation(s)"
    return True, f"{PASS} All {extracts} extract block(s) have Extract relation"


def check_extract_connection_attrs(content: str) -> tuple[bool, str]:
    if "<extract " not in content:
        return True, f"{PASS} Skipped extract attribute check (no extracts)"
    required = ["authentication='auth-none'", "default-settings='hyper'", "schema='Extract'"]
    missing = [a for a in required if a not in content]
    if missing:
        return False, f"{FAIL} Extract connection missing: {', '.join(missing)}"
    return True, f"{PASS} Extract connections have required attributes"


def check_twbx(twbx_path: Path, twb_name: str | None) -> list[tuple[bool, str]]:
    results: list[tuple[bool, str]] = []
    if not twbx_path.exists():
        results.append((False, f"{FAIL} TWBX not found: {twbx_path}"))
        return results
    try:
        with zipfile.ZipFile(twbx_path) as zf:
            names = zf.namelist()
            twb_files = [n for n in names if n.endswith(".twb")]
            hyper_files = [n for n in names if n.endswith(".hyper")]
            if not twb_files:
                results.append((False, f"{FAIL} TWBX contains no .twb"))
            else:
                results.append((True, f"{PASS} TWBX contains {len(twb_files)} .twb file(s)"))
            if twb_name and twb_name not in names and not any(twb_name in n for n in names):
                results.append((WARN, f"{WARN} Expected TWB '{twb_name}' not in archive"))
            if hyper_files:
                results.append((True, f"{PASS} TWBX contains {len(hyper_files)} .hyper file(s)"))
            else:
                results.append((WARN, f"{WARN} TWBX contains no .hyper files"))
    except zipfile.BadZipFile as exc:
        results.append((False, f"{FAIL} Invalid TWBX zip: {exc}"))
    return results


def validate(twb_path: Path, twbx_path: Path | None) -> int:
    if not twb_path.exists():
        print(f"{FAIL} TWB not found: {twb_path}")
        return 1

    content = twb_path.read_text(encoding="utf-8")
    checks: list[tuple[bool, str]] = []

    checks.append(check_xml_parse(twb_path))
    checks.append(check_measure_values(content))
    checks.append(check_multiple_values(content))
    checks.append(check_raw_measure_names_members(content))
    checks.append(check_scoped_measure_names(content))
    checks.append(check_extract_relations(content))
    checks.append(check_extract_connection_attrs(content))

    if twbx_path:
        checks.extend(check_twbx(twbx_path, twb_path.name))

    failed = False
    for ok, msg in checks:
        print(msg)
        if not ok:
            failed = True

    if failed:
        print(f"\n{FAIL} Validation failed")
        return 1
    print(f"\n{PASS} Validation passed")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate Tableau TWB/TWBX files")
    parser.add_argument("twb", type=Path, help="Path to .twb file")
    parser.add_argument("twbx", type=Path, nargs="?", help="Optional path to .twbx package")
    args = parser.parse_args()
    sys.exit(validate(args.twb, args.twbx))


if __name__ == "__main__":
    main()
