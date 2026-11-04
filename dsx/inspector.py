"""Trail inspector — sort the failures recorded in decision trails into categories.

The ``dsx stats --inspect`` report. NVIDIA's KDD Cup 2026 data-agent team kept
execution traces and had an inspector sort failures into categories, then fixed
the harness category by category. DSX's trail is ``DECISIONS.jsonl``: every gate
run appends an invocation header and the deterministic decisions its checks
made, including every ``DSX-…`` code that fired. This module reads those trails
and answers "which kinds of mistake keep happening?".

Counting follows ``dsx stats --paradigm`` (D-14): a code is counted once per
distinct ``frame_digest``, so re-running one spec twenty times cannot make its
failures look twenty times as common. The categorisation is a fixed prefix
table, not a model's judgement, so the same trails always give the same report.
What to *do* about a recurring category stays a human decision: the report
names candidates, it changes nothing.

Pure reader. Stdlib only.
"""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from .decisions import read_all

_CODE_RE = re.compile(r"\bDSX-([A-Z]+)-(\d+)\b")
# Words in a decision's ``choice`` that mean a code fired rather than cleared.
_FIRED_RE = re.compile(r"\b(fired|blocked|failed|breach(?:ed)?)\b", re.IGNORECASE)

# Finding-code prefix -> failure category. Ordered as the analysis is: the
# contract, the design, the data, the inference, the model, the claim, the
# figure, the code.
CATEGORIES: dict[str, str] = {
    "SPEC": "contract",
    "COH": "contract",
    "EXP": "design_and_identification",
    "VAL": "design_and_identification",
    "INT": "design_and_identification",
    "PAR": "design_and_identification",
    "PRE": "design_and_identification",
    "ADM": "design_and_identification",
    "CAU": "design_and_identification",
    "DQ": "data_joins_and_metrics",
    "MET": "data_joins_and_metrics",
    "SQL": "data_joins_and_metrics",
    "STA": "statistical_inference",
    "ML": "ml_and_leakage",
    "CLM": "claims_and_reporting",
    "NAR": "claims_and_reporting",
    "DEC": "claims_and_reporting",
    "VIZ": "figures",
    "FIG": "figures",
    "CRV": "figures",
    "CODE": "code_and_reproducibility",
    "SMELL": "code_and_reproducibility",
    "REP": "code_and_reproducibility",
}
CATEGORY_ORDER = (
    "contract",
    "design_and_identification",
    "data_joins_and_metrics",
    "statistical_inference",
    "ml_and_leakage",
    "claims_and_reporting",
    "figures",
    "code_and_reproducibility",
    "uncategorised",
)
# A code that fired in at least this many distinct frames is a recurring
# failure — the candidate for a harness-level fix rather than a one-off repair.
RECURRING_MIN_FRAMES = 2
TOP_CODES = 5


def category_of(code: str) -> str:
    match = _CODE_RE.search(code)
    if not match:
        return "uncategorised"
    return CATEGORIES.get(match.group(1), "uncategorised")


def fired_codes(record: dict[str, Any]) -> list[str]:
    """The finding codes a decision record says fired; empty when it cleared."""
    choice = record.get("choice")
    if not isinstance(choice, str):
        return []
    codes = sorted({m.group(0) for m in _CODE_RE.finditer(choice)})
    if not codes:
        return []
    if _FIRED_RE.search(choice) or record.get("escalate") is True:
        return codes
    return []


def inspect_trails(trails: Iterable[Path]) -> dict[str, Any]:
    """Aggregate fired codes across trails, deduplicated by frame digest."""
    trails_read = 0
    frames: set[str] = set()
    # (frame_digest, code) pairs, and which gate points saw each code fire.
    frame_codes: dict[str, set[str]] = defaultdict(set)
    code_points: dict[str, set[str]] = defaultdict(set)
    escalated: set[tuple[str, str]] = set()
    for trail in trails:
        trails_read += 1
        records = read_all(trail)
        local: dict[Any, tuple[str, str]] = {}
        for rec in records:
            if rec.get("record_type") != "invocation":
                continue
            digest = rec.get("frame_digest")
            if not isinstance(digest, str):
                continue
            frames.add(digest)
            local[rec.get("invocation_id")] = (digest, str(rec.get("gate_point") or "?"))
        for rec in records:
            if rec.get("record_type") != "decision":
                continue
            anchor = local.get(rec.get("invocation_id"))
            if anchor is None:
                continue
            digest, point = anchor
            for code in fired_codes(rec):
                frame_codes[digest].add(code)
                code_points[code].add(point)
                if rec.get("escalate") is True:
                    escalated.add((digest, code))

    code_frames: Counter[str] = Counter()
    for codes in frame_codes.values():
        code_frames.update(codes)

    by_category: dict[str, dict[str, Any]] = {}
    for cat in CATEGORY_ORDER:
        cat_codes = {c: n for c, n in code_frames.items() if category_of(c) == cat}
        if not cat_codes:
            continue
        cat_frames = sum(1 for codes in frame_codes.values() if any(category_of(c) == cat for c in codes))
        ranked = sorted(cat_codes.items(), key=lambda kv: (-kv[1], kv[0]))
        by_category[cat] = {
            "frames": cat_frames,
            "share_of_frames": cat_frames / len(frames) if frames else None,
            "distinct_codes": len(cat_codes),
            "escalations": sum(1 for _, c in escalated if category_of(c) == cat),
            "top_codes": [{"code": c, "frames": n} for c, n in ranked[:TOP_CODES]],
        }

    recurring = [
        {
            "code": code,
            "category": category_of(code),
            "frames": n,
            "gate_points": sorted(code_points[code]),
        }
        for code, n in sorted(code_frames.items(), key=lambda kv: (-kv[1], kv[0]))
        if n >= RECURRING_MIN_FRAMES
    ]

    result: dict[str, Any] = {
        "trails_read": trails_read,
        "distinct_frames": len(frames),
        "frames_with_a_fired_code": sum(1 for codes in frame_codes.values() if codes),
        "categories": by_category,
        "recurring": recurring,
    }
    if not frames:
        result["status"] = "no_history"
        result["message"] = "no operator history yet"
    else:
        result["status"] = "ok"
    return result


def render_text(result: dict[str, Any]) -> str:
    if result.get("status") == "no_history":
        return (
            "dsx: no operator history yet — no operator decision trails found "
            f"under {result.get('root')!r} (examples/ and templates/ excluded)."
        )
    lines = [
        (
            f"failure categories over {result['distinct_frames']} distinct operator frame(s) "
            f"({result['frames_with_a_fired_code']} with at least one fired code):"
        )
    ]
    for cat, block in result["categories"].items():
        share = block["share_of_frames"]
        pct = f"{share * 100:.1f}%" if share is not None else "n/a"
        top = ", ".join(f"{t['code']}×{t['frames']}" for t in block["top_codes"])
        lines.append(f"  {cat:<27} {block['frames']:>4} frame(s) ({pct})  {top}")
    if result["recurring"]:
        lines.append("")
        lines.append(
            f"recurring (fired in ≥{RECURRING_MIN_FRAMES} distinct frames) — candidates "
            "for a harness-level fix, each one a human decision:"
        )
        for r in result["recurring"]:
            lines.append(
                f"  {r['code']:<14} {r['frames']:>3} frames  [{r['category']}]  "
                f"gate points: {', '.join(r['gate_points'])}"
            )
    return "\n".join(lines)
