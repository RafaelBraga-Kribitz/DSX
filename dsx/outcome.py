"""Outcome experiment scorer — does running under DSX make answers right more often?

Every other number DSX reports is about DSX itself: how many seeded flaws it
catches, how many clean analyses it leaves alone. This module measures the
thing those numbers stand in for. Run the same agent on the same benchmark
tasks twice — a **control** arm without DSX and a **treatment** arm with the
DSX gates in the loop — and score both arms against the answer key.

Inputs are JSON Lines, one object per line:

- the **key**: ``{"task_id": ..., "answer": ..., "category": ...}``
  (``category`` optional, used for the per-category breakdown);
- each **arm**: ``{"task_id": ..., "answer": ..., "status": ...}`` where
  ``status`` is ``answered`` (default), ``blocked`` (the gate refused to let
  the answer ship) or ``error``. A task missing from an arm counts as
  unanswered. An unanswered task is wrong in the primary metric: a gate that
  blocks everything must not look accurate.

An ``answer`` is a scalar, a list of rows, or ``{"columns": [...], "rows":
[[...], ...]}``. Matching is order-insensitive over rows and, for the
``columns`` form, over columns; numbers compare after rounding to
``sig_digits`` significant digits; strings compare case- and
whitespace-insensitively.

The primary statistic is the paired difference in accuracy (treatment minus
control) with the exact McNemar test, because both arms answer the same tasks.
Stdlib only; deterministic.
"""

from __future__ import annotations

import json
import math
from collections import Counter
from pathlib import Path
from typing import Any

from .findings import CheckError
from .mathx import mcnemar_exact, paired_diff_ci, wilson_interval

STATUSES = ("answered", "blocked", "error")
DEFAULT_SIG_DIGITS = 4


def read_jsonl(path: str | Path, *, what: str) -> dict[str, dict[str, Any]]:
    p = Path(path)
    if not p.exists():
        raise CheckError(f"{what} file not found: {p}")
    out: dict[str, dict[str, Any]] = {}
    for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError as exc:
            raise CheckError(f"{p}:{n}: not valid JSON ({exc.msg})") from None
        if not isinstance(rec, dict) or "task_id" not in rec:
            raise CheckError(f"{p}:{n}: each line needs an object with a task_id")
        tid = str(rec["task_id"])
        if tid in out:
            raise CheckError(f"{p}:{n}: task_id {tid!r} appears twice")
        status = rec.get("status", "answered")
        if status not in STATUSES:
            raise CheckError(f"{p}:{n}: status {status!r} is not one of {', '.join(STATUSES)}")
        out[tid] = rec
    return out


def _norm_cell(value: Any, sig_digits: int) -> Any:
    if isinstance(value, bool):
        return ("b", value)
    if isinstance(value, (int, float)):
        x = float(value)
    elif isinstance(value, str):
        if not _looks_numeric(value):
            return ("s", " ".join(value.lower().split()))
        x = float(value.strip().replace(",", "").rstrip("%"))
    elif value is None:
        return ("n", None)
    else:
        return ("s", json.dumps(value, sort_keys=True))
    if math.isnan(x) or math.isinf(x):
        return ("s", str(x))
    if x == 0:
        return ("f", 0.0)
    digits = sig_digits - 1 - math.floor(math.log10(abs(x)))
    return ("f", round(x, digits))


def _looks_numeric(text: str) -> bool:
    t = text.strip().replace(",", "").rstrip("%")
    if not t:
        return False
    try:
        float(t)
    except ValueError:
        return False
    return True


def normalise(answer: Any, sig_digits: int = DEFAULT_SIG_DIGITS) -> Any:
    """Canonical, hashable, order-insensitive form of an answer."""
    if isinstance(answer, dict) and "rows" in answer:
        columns = [str(c).strip().lower() for c in answer.get("columns") or []]
        order = sorted(range(len(columns)), key=lambda i: columns[i]) if columns else None
        rows = []
        for row in answer["rows"]:
            cells = list(row) if isinstance(row, (list, tuple)) else [row]
            if order is not None and len(cells) == len(order):
                cells = [cells[i] for i in order]
            rows.append(tuple(_norm_cell(c, sig_digits) for c in cells))
        return ("table", tuple(sorted(columns)), tuple(sorted(rows, key=repr)))
    if isinstance(answer, (list, tuple)):
        rows = []
        for row in answer:
            cells = list(row) if isinstance(row, (list, tuple)) else [row]
            rows.append(tuple(_norm_cell(c, sig_digits) for c in cells))
        return ("table", (), tuple(sorted(rows, key=repr)))
    return ("table", (), ((_norm_cell(answer, sig_digits),),))


def is_correct(gold: Any, answer: Any, sig_digits: int = DEFAULT_SIG_DIGITS) -> bool:
    g = normalise(gold, sig_digits)
    a = normalise(answer, sig_digits)
    if g == a:
        return True
    # A keyed gold table matched by an un-keyed answer (or vice versa): compare rows only.
    return g[2] == a[2] and (not g[1] or not a[1])


def _arm_outcomes(
    key: dict[str, dict[str, Any]], arm: dict[str, dict[str, Any]], sig_digits: int
) -> tuple[dict[str, bool], Counter[str]]:
    right: dict[str, bool] = {}
    statuses: Counter[str] = Counter()
    for tid, gold in key.items():
        rec = arm.get(tid)
        if rec is None:
            statuses["missing"] += 1
            right[tid] = False
            continue
        status = rec.get("status", "answered")
        statuses[status] += 1
        right[tid] = status == "answered" and is_correct(gold.get("answer"), rec.get("answer"), sig_digits)
    return right, statuses


def _accuracy(right: dict[str, bool], tids: list[str], alpha: float) -> dict[str, Any]:
    n = len(tids)
    k = sum(1 for t in tids if right[t])
    lo, hi = wilson_interval(k, n, alpha) if n else (None, None)
    return {"correct": k, "n": n, "accuracy": k / n if n else None, "ci": [lo, hi]}


def score(
    key: dict[str, dict[str, Any]],
    control: dict[str, dict[str, Any]],
    treatment: dict[str, dict[str, Any]],
    *,
    sig_digits: int = DEFAULT_SIG_DIGITS,
    alpha: float = 0.05,
) -> dict[str, Any]:
    if not key:
        raise CheckError("the answer key is empty")
    stray = sorted((set(control) | set(treatment)) - set(key))
    c_right, c_status = _arm_outcomes(key, control, sig_digits)
    t_right, t_status = _arm_outcomes(key, treatment, sig_digits)
    tids = sorted(key)

    b = sum(1 for t in tids if c_right[t] and not t_right[t])
    c = sum(1 for t in tids if t_right[t] and not c_right[t])
    n = len(tids)
    lo, hi = paired_diff_ci(b, c, n, alpha)

    def _selective(right: dict[str, bool], arm: dict[str, dict[str, Any]]) -> dict[str, Any]:
        answered = [t for t in tids if t in arm and arm[t].get("status", "answered") == "answered"]
        return _accuracy(right, answered, alpha)

    # The tasks the gate blocked in treatment, and how control did on them: if
    # control got most of them right, the gate blocked good work.
    blocked = [t for t in tids if treatment.get(t, {}).get("status") == "blocked"]
    blocked_block = {
        "n": len(blocked),
        "control_correct_on_them": sum(1 for t in blocked if c_right[t]),
    }

    categories: dict[str, Any] = {}
    cats = sorted({str(key[t].get("category")) for t in tids if key[t].get("category") is not None})
    for cat in cats:
        sub = [t for t in tids if str(key[t].get("category")) == cat]
        cb = sum(1 for t in sub if c_right[t] and not t_right[t])
        cc = sum(1 for t in sub if t_right[t] and not c_right[t])
        categories[cat] = {
            "n": len(sub),
            "control_accuracy": sum(c_right[t] for t in sub) / len(sub),
            "treatment_accuracy": sum(t_right[t] for t in sub) / len(sub),
            "discordant": {"control_only": cb, "treatment_only": cc},
            "mcnemar_p": mcnemar_exact(cb, cc),
        }

    return {
        "n_tasks": n,
        "sig_digits": sig_digits,
        "alpha": alpha,
        "control": {
            "accuracy": _accuracy(c_right, tids, alpha),
            "selective_accuracy": _selective(c_right, control),
            "statuses": dict(sorted(c_status.items())),
        },
        "treatment": {
            "accuracy": _accuracy(t_right, tids, alpha),
            "selective_accuracy": _selective(t_right, treatment),
            "statuses": dict(sorted(t_status.items())),
        },
        "paired": {
            "difference": (c - b) / n,
            "ci": [lo, hi],
            "discordant": {"control_only": b, "treatment_only": c},
            "mcnemar_p": mcnemar_exact(b, c),
        },
        "treatment_blocked": blocked_block,
        "categories": categories,
        "stray_task_ids": stray,
    }


def render_text(result: dict[str, Any]) -> str:
    def pct(x: float | None) -> str:
        return "n/a" if x is None else f"{x * 100:.1f}%"

    lines = [f"outcome experiment over {result['n_tasks']} task(s):"]
    for arm in ("control", "treatment"):
        acc = result[arm]["accuracy"]
        sel = result[arm]["selective_accuracy"]
        lines.append(
            f"  {arm:<10} accuracy {pct(acc['accuracy'])} "
            f"[{pct(acc['ci'][0])}, {pct(acc['ci'][1])}]  "
            f"answered-only {pct(sel['accuracy'])} of {sel['n']}  "
            f"statuses {result[arm]['statuses']}"
        )
    pr = result["paired"]
    lines.append(
        f"  paired difference (treatment - control) {pr['difference'] * 100:+.1f} points "
        f"[{pr['ci'][0] * 100:+.1f}, {pr['ci'][1] * 100:+.1f}], "
        f"exact McNemar p = {pr['mcnemar_p']:.4g} "
        f"(discordant: control-only {pr['discordant']['control_only']}, "
        f"treatment-only {pr['discordant']['treatment_only']})"
    )
    tb = result["treatment_blocked"]
    if tb["n"]:
        lines.append(
            f"  the gate blocked {tb['n']} task(s); control answered "
            f"{tb['control_correct_on_them']} of those correctly"
        )
    for cat, block in result["categories"].items():
        lines.append(
            f"  [{cat}] n={block['n']} control {pct(block['control_accuracy'])} "
            f"treatment {pct(block['treatment_accuracy'])} p={block['mcnemar_p']:.4g}"
        )
    if result["stray_task_ids"]:
        lines.append(f"  ignored {len(result['stray_task_ids'])} task id(s) not in the key")
    return "\n".join(lines)
