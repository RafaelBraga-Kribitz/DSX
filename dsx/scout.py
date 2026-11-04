"""Multi-table schema scout — grain, join keys and fan-out across local extracts.

``dsx profile`` describes one table. Most wrong totals come from what happens
*between* tables: a join declared one-to-one that fans out, a key that matches
half the rows, two columns with one name and two meanings, one amount in cents
and another in dollars. ``dsx scout`` reads two or more CSV extracts and writes
``SCHEMA-SCOUT.yaml`` with:

- **grain** per table: the smallest column set (one or two columns) that is
  unique and never null, or ``null`` when none is found;
- **joins**: every column pair across two tables whose values overlap, with
  the cardinality (``one_to_one`` … ``many_to_many``), both left-join fan-outs,
  the match rate and the null-key rate — the fan-out matrix
  ``skills/dsx-explore-data/SKILL.md`` step 1b asks for, computed rather than
  typed;
- **warnings**: fan-out, many-to-many keys, low match rates, a shared column
  name whose values never overlap, and a shared numeric column whose medians
  differ by a power of ten (a likely unit mismatch).

``--expect LEFT.col=RIGHT.col`` turns the join learning
(``docs/dsx/learnings/2026-08-28-join-fanout-inflates-additive-metrics.md``)
into a check: the command exits 1 when an expected one-to-one join fans out in
either direction, or when a named column is missing.

Gates never call this; it is analyst-invoked, like ``dsx profile``. Stdlib only.
It only reads files — it never runs a query or the analyst's code.
"""

from __future__ import annotations

import csv
import math
import re
import statistics
from collections import Counter
from itertools import combinations
from pathlib import Path
from typing import Any

from .findings import CheckError
from .profiler import _FLOAT_RE, _INT_RE, _infer_dtype, _is_null, file_sha256

SCOUT_VERSION = 1
COMPUTED_BY = "dsx-scout"

# A column pair is a join candidate when this share of the smaller side's
# distinct values also appears on the other side.
MIN_CONTAINMENT = 0.5
# Below this share of left rows finding a match, a join is flagged.
LOW_MATCH_RATE = 0.9
# Two-column grain search is bounded so a wide table cannot blow up.
MAX_GRAIN_PAIR_COLUMNS = 30
# A numeric column with fewer distinct values than this is a flag or a code,
# not a key, and is never proposed as a join key on value overlap alone.
MIN_KEY_DISTINCT = 3
_KEY_DTYPES = {"integer", "string", "mixed", "date"}
_ID_NAME_RE = re.compile(r"(^id$|_id$|^id_|_key$|^key$|_code$|uuid)", re.IGNORECASE)


class _Table:
    """One CSV extract, read once, kept in memory as column value counts."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.name = path.stem
        self.rows: list[tuple[str, ...]] = []
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            sample = handle.read(8192)
            handle.seek(0)
            try:
                dialect = csv.Sniffer().sniff(sample, delimiters=",\t|;")
            except csv.Error:
                dialect = csv.excel
            reader = csv.reader(handle, dialect=dialect)
            try:
                header = next(reader)
            except StopIteration:
                raise CheckError(f"{path}: CSV has no header row") from None
            if not header:
                raise CheckError(f"{path}: CSV has no header row")
            self.columns = [c.strip() for c in header]
            if len(set(self.columns)) != len(self.columns):
                dupes = sorted({c for c in self.columns if self.columns.count(c) > 1})
                raise CheckError(f"{path}: duplicate column name(s): {', '.join(dupes)}")
            width = len(self.columns)
            for raw in reader:
                if not raw:
                    continue
                cells = [c.strip() for c in raw[:width]]
                cells += [""] * (width - len(cells))
                self.rows.append(tuple("" if _is_null(c) else c for c in cells))
        self.row_count = len(self.rows)
        self.counts: dict[str, Counter[str]] = {}
        self.nulls: dict[str, int] = {}
        self.dtype: dict[str, str] = {}
        for i, col in enumerate(self.columns):
            counter: Counter[str] = Counter()
            nulls = 0
            for row in self.rows:
                value = row[i]
                if value == "":
                    nulls += 1
                else:
                    counter[value] += 1
            self.counts[col] = counter
            self.nulls[col] = nulls
            self.dtype[col] = _infer_dtype(sorted(counter)[:200])

    def median(self, col: str) -> float | None:
        values: list[float] = []
        for value, n in self.counts[col].items():
            if _INT_RE.match(value) or _FLOAT_RE.match(value):
                values.extend([float(value)] * n)
        if not values:
            return None
        return float(statistics.median(values))


def _grain(table: _Table) -> dict[str, Any]:
    """Smallest unique, never-null key: every qualifying single column, else
    the first qualifying pair in header order."""
    n = table.row_count
    full_dupes = n - len(set(table.rows))
    # Identifier-looking names first, so ``order_id`` outranks an ``amount``
    # that happens to be unique in a small extract.
    ordered = sorted(table.columns, key=lambda c: (not _ID_NAME_RE.search(c), table.columns.index(c)))
    singles = [
        [c] for c in ordered
        if n and table.nulls[c] == 0 and len(table.counts[c]) == n
        and table.dtype[c] != "float"
    ]
    keys = singles
    if not keys and n:
        cols = [
            c for c in ordered if table.nulls[c] == 0 and table.dtype[c] != "float"
        ][:MAX_GRAIN_PAIR_COLUMNS]
        index = {c: table.columns.index(c) for c in cols}
        for a, b in combinations(cols, 2):
            ia, ib = index[a], index[b]
            if len({(r[ia], r[ib]) for r in table.rows}) == n:
                keys = [[a, b]]
                break
    if singles:
        verdict = "unique_key"
    elif keys:
        verdict = "composite_key"
    elif full_dupes:
        verdict = "duplicate_rows"
    else:
        verdict = "no_key_found"
    return {"candidate_keys": ["+".join(k) for k in keys], "verdict": verdict, "duplicate_full_rows": full_dupes}


def _cardinality(left_max: int, right_max: int) -> str:
    if left_max <= 1 and right_max <= 1:
        return "one_to_one"
    if left_max <= 1:
        return "one_to_many"
    if right_max <= 1:
        return "many_to_one"
    return "many_to_many"


def _left_join(left: _Table, lcol: str, right: _Table, rcol: str) -> dict[str, Any]:
    """Row arithmetic of ``left LEFT JOIN right ON lcol = rcol``. A null key
    never matches (SQL semantics) and keeps its one left row."""
    rows_before = left.row_count
    rcounts = right.counts[rcol]
    rows_after = left.nulls[lcol]
    matched = 0
    for value, n in left.counts[lcol].items():
        hit = rcounts.get(value, 0)
        if hit:
            matched += n
        rows_after += n * max(hit, 1)
    return {
        "rows_before": rows_before,
        "rows_after": rows_after,
        "fanout": (rows_after / rows_before) if rows_before else None,
        "match_rate": (matched / rows_before) if rows_before else None,
        "null_key_rate": (left.nulls[lcol] / rows_before) if rows_before else None,
    }


def _join_record(a: _Table, acol: str, b: _Table, bcol: str, containment: float) -> dict[str, Any]:
    a_max = max(a.counts[acol].values(), default=0)
    b_max = max(b.counts[bcol].values(), default=0)
    return {
        "left": f"{a.name}.{acol}",
        "right": f"{b.name}.{bcol}",
        "same_name": acol.lower() == bcol.lower(),
        "containment": containment,
        "cardinality": _cardinality(a_max, b_max),
        "left_join": _left_join(a, acol, b, bcol),
        "right_join": _left_join(b, bcol, a, acol),
    }


def _containment(a: Counter[str], b: Counter[str]) -> float:
    small, large = (a, b) if len(a) <= len(b) else (b, a)
    if not small:
        return 0.0
    return sum(1 for v in small if v in large) / len(small)


def _is_key_like(table: _Table, col: str) -> bool:
    if table.dtype[col] not in _KEY_DTYPES:
        return False
    return len(table.counts[col]) >= MIN_KEY_DISTINCT


def _join_warnings(join: dict[str, Any]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    pair = f"{join['left']} = {join['right']}"
    for side, block, other in (
        ("left", join["left_join"], join["right"]),
        ("right", join["right_join"], join["left"]),
    ):
        base = join[side].split(".", 1)[0]
        other_table = other.split(".", 1)[0]
        fan = block["fanout"]
        if fan is not None and fan > 1.0:
            out.append({
                "kind": "fanout",
                "join": pair,
                "detail": (
                    f"joining {other_table} onto {base} turns {block['rows_before']} rows "
                    f"into {block['rows_after']} (fanout {_fmt(fan)}); every additive "
                    f"metric of {base} summed after this join is inflated"
                ),
            })
        rate = block["match_rate"]
        if rate is not None and rate < LOW_MATCH_RATE:
            out.append({
                "kind": "low_match_rate",
                "join": pair,
                "detail": (
                    f"only {_fmt(rate)} of {base} rows find a match in {other_table}; "
                    "an inner join drops the rest silently"
                ),
            })
    if join["cardinality"] == "many_to_many":
        out.append({
            "kind": "many_to_many",
            "join": pair,
            "detail": "both sides repeat the key; neither table is at the key's grain",
        })
    return out


def _fmt(x: float) -> str:
    return f"{x:.4f}".rstrip("0").rstrip(".")


def scout(
    paths: list[str | Path], *, min_containment: float = MIN_CONTAINMENT
) -> dict[str, Any]:
    """Compute the SCHEMA-SCOUT mapping for two or more CSV extracts."""
    if len(paths) < 2:
        raise CheckError("dsx scout needs at least two CSV files")
    tables: list[_Table] = []
    seen_names: set[str] = set()
    for raw in paths:
        path = Path(raw)
        if not path.exists():
            raise CheckError(f"CSV not found: {path}")
        if path.suffix.lower() not in {".csv", ".tsv", ".txt"}:
            raise CheckError(f"dsx scout reads CSV only (got {path.suffix!r}): {path}")
        table = _Table(path)
        if table.name in seen_names:
            raise CheckError(f"two inputs share the table name {table.name!r}; rename one")
        seen_names.add(table.name)
        tables.append(table)

    table_blocks: dict[str, Any] = {}
    for t in tables:
        cols: dict[str, Any] = {}
        for c in t.columns:
            cols[c] = {
                "dtype": t.dtype[c],
                "null_rate": (t.nulls[c] / t.row_count) if t.row_count else 0.0,
                "n_unique": len(t.counts[c]),
            }
        table_blocks[t.name] = {
            "source_path": str(t.path).replace("\\", "/"),
            "source_hash": file_sha256(t.path),
            "row_count": t.row_count,
            "grain": _grain(t),
            "columns": cols,
        }

    joins: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    for a, b in combinations(tables, 2):
        for acol in a.columns:
            for bcol in b.columns:
                same = acol.lower() == bcol.lower()
                share = _containment(a.counts[acol], b.counts[bcol])
                key_like = _is_key_like(a, acol) and _is_key_like(b, bcol)
                unit = _unit_warning(a, acol, b, bcol) if same else None
                if unit:
                    warnings.append(unit)
                if key_like and share >= min_containment:
                    joins.append(_join_record(a, acol, b, bcol, share))
                elif same and not unit and share == 0.0 and key_like:
                    warnings.append({
                        "kind": "name_collision",
                        "join": f"{a.name}.{acol} = {b.name}.{bcol}",
                        "detail": "same column name, no shared values; the name means "
                                  "different things in the two tables",
                    })

    # Strongest candidates first: same name, then containment, then name order.
    joins.sort(key=lambda j: (not j["same_name"], -j["containment"], j["left"], j["right"]))
    for j in joins:
        warnings.extend(_join_warnings(j))
    warnings.sort(key=lambda w: (w["kind"], w["join"], w["detail"]))

    return {
        "scout_version": SCOUT_VERSION,
        "computed_by": COMPUTED_BY,
        "tables": table_blocks,
        "joins": joins,
        "warnings": warnings,
    }


def _unit_warning(a: _Table, acol: str, b: _Table, bcol: str) -> dict[str, Any] | None:
    """Same-named numeric columns whose medians differ by roughly a factor of
    10**k (k ≥ 2): cents vs dollars, milliseconds vs seconds, grams vs kg."""
    if a.dtype[acol] not in ("integer", "float") or b.dtype[bcol] not in ("integer", "float"):
        return None
    ma, mb = a.median(acol), b.median(bcol)
    if not ma or not mb or (ma < 0) != (mb < 0):
        return None
    ratio = max(abs(ma), abs(mb)) / min(abs(ma), abs(mb))
    if ratio < 50:
        return None
    exponent = round(math.log10(ratio))
    if exponent < 2 or abs(math.log10(ratio) - exponent) > 0.15:
        return None
    return {
        "kind": "possible_unit_mismatch",
        "join": f"{a.name}.{acol} = {b.name}.{bcol}",
        "detail": (
            f"medians {_fmt(ma)} and {_fmt(mb)} differ by about 10^{exponent}; "
            "check the unit before comparing or summing"
        ),
    }


def check_expectations(result: dict[str, Any], expects: list[str]) -> list[str]:
    """Each ``LEFT.col=RIGHT.col`` is asserted one-to-one. Returns one failure
    message per broken expectation (empty when all hold)."""
    failures: list[str] = []
    by_pair = {(j["left"], j["right"]): j for j in result["joins"]}
    tables = result["tables"]
    for raw in expects:
        if "=" not in raw:
            raise CheckError(f"--expect {raw!r}: write it as LEFT.col=RIGHT.col")
        left, right = (s.strip() for s in raw.split("=", 1))
        missing = [
            ref for ref in (left, right)
            if "." not in ref
            or ref.split(".", 1)[0] not in tables
            or ref.split(".", 1)[1] not in tables[ref.split(".", 1)[0]]["columns"]
        ]
        if missing:
            failures.append(f"{raw}: no such table column {', '.join(missing)}")
            continue
        join = by_pair.get((left, right))
        flipped = False
        if join is None and (right, left) in by_pair:
            join, flipped = by_pair[(right, left)], True
        if join is None:
            failures.append(
                f"{raw}: the two columns share too few values to be a join key"
            )
            continue
        lj, rj = join["left_join"], join["right_join"]
        if flipped:
            lj, rj = rj, lj
        for label, block in ((left, lj), (right, rj)):
            if block["fanout"] is not None and block["fanout"] != 1.0:
                base = label.split(".", 1)[0]
                failures.append(
                    f"{raw}: expected one-to-one, but the join turns the "
                    f"{block['rows_before']} rows of {base} into {block['rows_after']} "
                    f"(fanout {_fmt(block['fanout'])})"
                )
    return failures
