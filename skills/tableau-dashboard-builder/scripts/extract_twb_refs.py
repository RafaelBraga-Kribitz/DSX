#!/usr/bin/env python3
"""Extract TWB files from TWBX archives and optionally scan for Tableau XML patterns."""

from __future__ import annotations

import argparse
import glob
import sys
import zipfile
from pathlib import Path

DEFAULT_PATTERNS = [
    "reference-line",
    "[:Measure Names]",
    "[Multiple Values]",
    "tsc:tsl-filter",
    "boxplot",
    "GanttBar",
    "customized-label",
    "layout-flow",
    "formula='constant'",
    "random()",
]


def extract_twbx(twbx_path: Path, out_dir: Path) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    with zipfile.ZipFile(twbx_path) as zf:
        for name in zf.namelist():
            if not name.lower().endswith(".twb"):
                continue
            data = zf.read(name)
            dest = out_dir / Path(name).name
            dest.write_bytes(data)
            written.append(dest)
    return written


def scan_file(twb_path: Path, patterns: list[str]) -> dict[str, int]:
    content = twb_path.read_text(encoding="utf-8", errors="replace")
    return {p: content.count(p) for p in patterns}


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract TWB from TWBX and scan patterns")
    parser.add_argument(
        "--scan",
        required=True,
        help="Glob pattern for .twbx files (e.g. 'exports/tableau_public/*.twbx')",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("_twb_refs"),
        help="Output directory for extracted .twb files",
    )
    parser.add_argument(
        "--patterns",
        nargs="*",
        default=DEFAULT_PATTERNS,
        help="Substring patterns to count in each extracted TWB",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Max TWBX files to process (0 = all)",
    )
    args = parser.parse_args()

    twbx_files = sorted(glob.glob(args.scan))
    if not twbx_files:
        print(f"No files matched: {args.scan}", file=sys.stderr)
        sys.exit(1)

    if args.limit:
        twbx_files = twbx_files[: args.limit]

    total_twbs = 0
    for twbx in twbx_files:
        path = Path(twbx)
        print(f"\n=== {path.name} ===")
        try:
            extracted = extract_twbx(path, args.out)
        except zipfile.BadZipFile:
            print(f"  [SKIP] Not a valid zip: {path}")
            continue
        if not extracted:
            print("  [SKIP] No .twb inside archive")
            continue
        for twb in extracted:
            total_twbs += 1
            print(f"  Wrote {twb}")
            counts = scan_file(twb, args.patterns)
            hits = {k: v for k, v in counts.items() if v > 0}
            if hits:
                for k, v in sorted(hits.items(), key=lambda x: -x[1]):
                    print(f"    {k}: {v}")

    print(f"\nExtracted {total_twbs} TWB file(s) to {args.out.resolve()}")


if __name__ == "__main__":
    main()
