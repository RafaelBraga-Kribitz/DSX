"""Decision-record schema, append-only crash-safe emitter, tolerant reader.

Top-level peer to ``dsx/findings.py`` — the second output contract this package
writes, not just reads. Stdlib only (D-01): a decision trail is worthless if the
gate that would emit it can't run because a dependency is missing.

The append contract (D-19), normative for any future writer of this file:

- **File:** ``DECISIONS.jsonl``, written beside the resolved spec (see
  ``decisions_path()``) — the same root ``dsx gate``/``dsx check`` already
  resolve for evidence and profile paths.
- **Format:** one JSON object per line (JSON Lines). Each line is
  ``json.dumps(record.to_dict(), sort_keys=True)`` followed by a single ``\\n``.
  No trailing commas, no enclosing array — the file is never parsed as a whole
  JSON document, always line by line.
- **Required fields:** every record carries a ``record_type`` of either
  ``"invocation"`` or ``"decision"`` (see ``RECORD_TYPES``). An invocation
  header (``InvocationHeader``) carries ``invocation_id``, ``gate_point``,
  ``dsx_version`` and ``frame_digest`` — the grouping anchor for one gate run's
  trail. A decision record (``DecisionRecord``) carries ``id``,
  ``invocation_id``, ``layer``, ``choice``, ``inputs``, ``rule``, ``citation``,
  ``counterfactual``, ``alternatives_rejected``, ``confidence`` and
  ``escalate`` — the ten brief-5.5 fields plus the ``invocation_id`` that ties
  it back to its header.
- **Layers:** ``layer`` is one of two values (``DECISION_LAYERS``):
  ``"deterministic"`` (a dsx check's own rule-based judgment) or
  ``"stochastic"`` (an agent's judgment call, with a confidence and a
  counterfactual). The gate emits ``layer: "deterministic"`` records only.
  A dsx agent may begin appending ``layer: "stochastic"`` entries to the same
  file with no further code change here — the schema already carries
  ``confidence`` and ``escalate`` for that case.
- **Durability:** ``append()`` writes, ``flush()``es and ``os.fsync()``s the
  file descriptor per record, so a line that finished writing survives a
  crashed run. ``read_all()`` is the other half of that guarantee: it
  tolerates an unparseable line (the half-written tail of a crash) and an
  undecodable byte (a hand-edit, filesystem-level corruption of an
  already-committed byte, or any future non-ASCII write), so one crash or one
  corrupted byte never invalidates every record written before it. A missing
  file is an empty trail. A path that exists but cannot be read (a directory,
  a device node, a revoked permission) is *not* an empty trail — treating it
  as one would restart ``next_invocation_id()`` at ``INV-0001`` and write a
  duplicate id — so it raises ``CheckError`` naming the path; the callers
  that promise never to block (``_write_decision_trail``, ``dsx explain``,
  ``dsx stats``) already guard over ``Exception`` and report it.
- **Concurrency (WR-02, SEED-004 CL-01):** ``next_invocation_id()`` and the
  header ``append()`` are a read-then-write, so a writer holds
  ``trail_lock(path)`` across both (``dsx/cli.py::_write_decision_trail``
  holds it across the whole invocation's records). The lock is an exclusive
  OS advisory lock (``fcntl.flock`` on POSIX, ``msvcrt.locking`` on Windows)
  on the sibling file ``DECISIONS.jsonl.lock``. The kernel drops it when the
  holding process exits, however it exits, so the lock file's existence never
  means "held" and a crashed writer can never wedge the next run. A writer
  that cannot take the lock within its timeout raises ``TrailLockTimeout``
  and writes nothing — the trail is a side channel, so the gate still exits
  on its findings. Readers take no lock: ``append()`` writes one whole line
  per call and ``read_all()`` tolerates a torn tail.
"""

from __future__ import annotations

import contextlib
import hashlib
import json
import os
import time
from collections.abc import Iterator
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from .findings import CheckError

DECISION_LAYERS = frozenset({"deterministic", "stochastic"})
RECORD_TYPES = {"invocation", "decision", "amendment"}


@dataclass(frozen=True)
class DecisionRecord:
    """One decision-trail entry — brief section 5.5's schema.

    ``counterfactual`` is the field that teaches: what would have made this
    choice go the other way. Mirrors ``dsx.findings.Finding``'s frozen-dataclass
    idiom.
    """

    id: str
    invocation_id: str
    layer: str
    choice: str
    inputs: list[str] = field(default_factory=list)
    rule: str = ""
    citation: str = ""
    counterfactual: str = ""
    alternatives_rejected: list[str] = field(default_factory=list)
    confidence: str | None = None
    escalate: bool = False

    def __post_init__(self) -> None:
        # The one place a decision record is built, whether by a check
        # (``record_decision``) or by the trail writer from a frame module's
        # plain dict — so an unknown layer cannot reach the file.
        if self.layer not in DECISION_LAYERS:
            raise ValueError(
                f"decision record {self.id or '?'} has layer {self.layer!r}; "
                f"expected one of {sorted(DECISION_LAYERS)}"
            )

    def to_dict(self) -> dict[str, Any]:
        out = asdict(self)
        out["record_type"] = "decision"
        return out


@dataclass(frozen=True)
class InvocationHeader:
    """The per-invocation grouping anchor (D-16) for one gate run's trail.

    The frame digest lives here, once per invocation — not on every decision
    record — because it is a property of the invocation (which spec, at which
    content), not of any individual choice made during it.

    ``spec_id`` (REQ-P11.2-05, D-08) is a defaulted field, appended AFTER
    ``frame_digest`` — never inserted earlier — because this is a
    ``frozen=True`` dataclass with four required fields and no defaults, and
    9 existing construction sites (``dsx/cli.py::_write_decision_trail``,
    ``tests/_trail_seed.py::seed_plan_header``, and 7 more across
    ``tests/test_frame_prereg.py``/``test_dsx.py``/``test_decisions.py``)
    pass no ``spec_id`` today. Python requires every non-default dataclass
    field to precede every defaulted one, so a no-default ``spec_id`` or one
    inserted before ``frame_digest`` would break the class definition itself
    or every one of those 9 call sites at construction time. It is the
    operator's declared top-level spec identity — never placed inside
    ``validity_frame:``/``inference:``, so it never enters ``frame_digest``'s
    inputs (D-08) — used by ``dsx/frame/prereg.py``'s ``DSX-PRE-040``/
    ``DSX-PRE-041`` to group invocation headers by the spec they belong to
    and count how many distinct frame digests were recorded under one
    identity.
    """

    invocation_id: str
    gate_point: str
    dsx_version: str
    frame_digest: str
    spec_id: str | None = None

    def to_dict(self) -> dict[str, Any]:
        out = asdict(self)
        out["record_type"] = "invocation"
        return out


@dataclass(frozen=True)
class AmendmentRecord:
    """A ``record_type: "amendment"`` decision-trail entry (REQ-P11.2-05, D-10).

    The clearing half of the ``DSX-PRE-041`` amendment counter
    (``dsx/frame/prereg.py::_check_amendment_ledger``): an operator-authored
    record naming *when* (``invocation_id``, ``gate_point``, ``dsx_version``),
    *which* spec (``spec_id``), *what* changed (``prev_frame_digest`` ->
    ``new_frame_digest``) and *why* (``reason``) a locked plan was amended
    after results existed. Mirrors ``DecisionRecord``'s exact
    ``@dataclass(frozen=True)`` + ``to_dict()`` idiom: ``to_dict()`` hardcodes
    the literal ``"amendment"`` rather than consulting ``RECORD_TYPES``,
    because ``RECORD_TYPES`` is decorative documentation only, never
    enforced — the same reason ``DecisionRecord.to_dict()`` hardcodes
    ``"decision"`` instead of reading it back out of the module constant.

    This is a committed-trail honesty signal, not a tamper-proof control
    (D-12): the trail is a plain, unsigned, tolerant-read local file, and
    ``reason`` is checkable for form (not a placeholder or refusal, via
    ``dsx.spec.is_placeholder_or_refusal``) but never for truth.

    **Nothing in dsx writes this record, by design.** The gate cannot know
    *why* a locked frame changed — only the operator can — so the gate writes
    invocation headers and decision records only, and ``prereg`` reads
    amendment records back. This class is the schema for that consumer side:
    the shape an operator (or an operator's own tooling, via ``append()`` under
    ``trail_lock()``) writes when amending a locked plan, and the shape the
    tests construct. It is not dead code awaiting a writer.
    """

    spec_id: str
    invocation_id: str
    gate_point: str
    dsx_version: str
    prev_frame_digest: str
    new_frame_digest: str
    reason: str

    def to_dict(self) -> dict[str, Any]:
        out = asdict(self)
        out["record_type"] = "amendment"
        return out


class TrailLockTimeout(CheckError):
    """The decision-trail lock could not be taken within the timeout."""


_LOCK_POLL_SECONDS = 0.05
# How long a writer waits for another writer before giving up on the trail.
LOCK_TIMEOUT_SECONDS = 10.0


def _try_lock(fh: Any) -> bool:
    """One non-blocking attempt at an exclusive lock on ``fh``; ``True`` if held."""
    if os.name == "nt":  # pragma: no cover - exercised on Windows only
        import msvcrt

        fh.seek(0)
        try:
            msvcrt.locking(fh.fileno(), msvcrt.LK_NBLCK, 1)
        except OSError:
            return False
        return True
    import fcntl

    try:
        fcntl.flock(fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        return False
    return True


def _unlock(fh: Any) -> None:
    if os.name == "nt":  # pragma: no cover - exercised on Windows only
        import msvcrt

        fh.seek(0)
        msvcrt.locking(fh.fileno(), msvcrt.LK_UNLCK, 1)
        return
    import fcntl

    fcntl.flock(fh.fileno(), fcntl.LOCK_UN)


def lock_path(path: str | Path) -> Path:
    """The advisory lock file for the trail at ``path``: ``<trail>.lock``."""
    trail = Path(path)
    return trail.with_name(trail.name + ".lock")


@contextlib.contextmanager
def trail_lock(path: str | Path, timeout: float | None = None) -> Iterator[None]:
    """Hold an exclusive advisory lock for the trail at ``path`` (SEED-004 CL-01).

    Serialises ``next_invocation_id()`` + ``append()`` across processes, so two
    concurrent ``dsx gate`` runs against one root get distinct invocation ids.
    Polls a non-blocking lock until ``timeout`` seconds (default
    ``LOCK_TIMEOUT_SECONDS``, read at call time) pass, then raises
    ``TrailLockTimeout`` (a ``CheckError``) — never waits forever. The lock
    file is created if absent and never deleted: unlinking a lock file while
    another process waits on it would let two writers hold "the" lock at once.
    The OS releases the lock when the holder exits, even when it is killed.
    """
    if timeout is None:
        timeout = LOCK_TIMEOUT_SECONDS
    target = lock_path(path)
    # "a+b" creates the file without truncating it, and gives a descriptor
    # both flock (POSIX) and msvcrt.locking (Windows, needs write access) accept.
    with target.open("a+b") as fh:
        deadline = time.monotonic() + max(timeout, 0.0)
        while not _try_lock(fh):
            if time.monotonic() >= deadline:
                raise TrailLockTimeout(
                    f"could not lock {target} within {timeout:g}s — another dsx "
                    "gate is writing this decision trail"
                )
            time.sleep(_LOCK_POLL_SECONDS)
        try:
            yield
        finally:
            _unlock(fh)


def append(
    path: str | Path, record: DecisionRecord | InvocationHeader | AmendmentRecord
) -> None:
    """Append one record. flush()+fsync() so a completed line survives a crash;
    the reader (read_all) skips an unparseable tail line rather than failing
    the file."""
    line = json.dumps(record.to_dict(), sort_keys=True)
    # newline="\n" pins the D-19 byte contract (one JSON object per line ending
    # in a single \n). Default text mode translates \n -> \r\n on Windows, and
    # Phase 10 made DECISIONS.jsonl a content-locked gate input (byte
    # comparison), so trail fidelity now has to hold byte-for-byte across
    # platforms — read_all()'s splitlines() tolerated \r\n on the read side, but
    # the write must still honour the documented single-\n contract.
    with Path(path).open("a", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")
        fh.flush()
        os.fsync(fh.fileno())


def read_all(path: str | Path) -> list[dict]:
    """Return every parseable record; tolerant of damaged content, not of an
    unreadable file:

    - **Missing path** -> ``[]`` (no trail yet is an empty trail).
    - **Unreadable path** (a directory rather than a file, a device node, a
      revoked permission) -> raises ``CheckError`` naming the path. An
      unreadable trail is not an empty one: returning ``[]`` would restart
      ``next_invocation_id()`` at ``INV-0001`` and let the next append write a
      duplicate invocation id, and would let ``prereg`` report "no plan-time
      header" for a header that exists. Callers that must never block
      (``_write_decision_trail``, ``cmd_explain``, ``cmd_stats``) guard over
      ``Exception`` and report the error.
    - **Undecodable bytes** in the file (not valid UTF-8) -> ``errors="replace"``
      on the decode, so the read itself cannot raise; a line degraded by
      replacement characters then either still parses as JSON or falls into
      the existing unparseable-line skip below.
    - **An unparseable line** (JSON-level truncation, e.g. the half-written
      tail of a crash, or arbitrary non-JSON content), and a line that is valid
      JSON but not an object (``[1, 2]``, ``42``, ``null``), is skipped, not fatal —
      the tolerant-reader design this docstring's module-level durability
      paragraph describes.
    """
    p = Path(path)
    if not p.exists():
        return []
    try:
        text = p.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return []  # removed between the exists() test and the read
    except OSError as exc:
        raise CheckError(f"decision trail {p} exists but cannot be read: {exc}") from exc
    records: list[dict] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue  # tolerant reader — a half-written crash-tail line is skipped, not fatal
        if isinstance(record, dict):
            records.append(record)
        # else: valid JSON that is not a record object (``[1, 2]``, ``42``,
        # ``null``) is skipped like a torn line, so every caller may call
        # ``.get()`` on what it gets back.
    return records


def next_invocation_id(path: str | Path) -> str:
    """Deterministic, file-derived invocation identifier — never uuid, never a
    clock read, so identical input produces identical output. Named
    ``invocation_id``, not ``run_id`` (D-15): ``run_id`` is
    ``visuals[].run_id``, checked by ``DSX-SMELL-013``.

    **Concurrency (WR-02):** the identifier is derived by counting existing
    invocation records and the caller appends the new header separately, so a
    writer must call this and append the header while holding
    ``trail_lock(path)`` — as ``dsx/cli.py::_write_decision_trail`` does.
    Without the lock, two ``dsx gate`` processes racing against one
    ``DECISIONS.jsonl`` can both derive the same identifier and ``dsx
    explain``, which groups purely on invocation-id equality, would interleave
    their records under one header. This function takes no lock itself: the
    lock has to span the append that follows it.
    """
    records = read_all(path)
    n = sum(1 for r in records if r.get("record_type") == "invocation") + 1
    return f"INV-{n:04d}"


def frame_digest(spec: dict[str, Any]) -> str:
    """Stable digest over the ``validity_frame:``/``inference:`` blocks only.
    Key-order invariant (``sort_keys=True``); unchanged by edits elsewhere in
    the spec. Change-detection, not a security control."""
    payload = json.dumps(
        {"validity_frame": spec.get("validity_frame"), "inference": spec.get("inference")},
        sort_keys=True,
        default=str,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def decisions_path(root: str | Path) -> Path:
    """``DECISIONS.jsonl`` beside the resolved spec (D-14). Does not
    re-implement ``find_spec()``'s search: the caller already has the resolved
    root (``args.phase_dir or str(path.parent)``)."""
    return Path(root) / "DECISIONS.jsonl"


def record_decision(report: Any, decision_record: DecisionRecord) -> None:
    """Append one decision record onto ``report.context["decisions"]``.

    Phase 11.1 (REQ-P11.1-01): the shared write path for ``dsx/checks/*.py``
    modules. ``tests/test_dsx.py::test_no_check_module_appends_to_a_decisions_list``
    forbids any file under ``dsx/checks/`` from containing the literal
    ``context.setdefault("decisions", ...)``/``context["decisions"]`` idiom
    inline — that test predates this function and still passes unmodified,
    because a check module calling this helper never spells that idiom itself.
    This is not a relaxation of the boundary the test enforces; it is the one
    sanctioned indirection through it, so a check module can still participate
    in the milestone's standing per-phase decision-record deliverable (D-04)
    without duplicating ``dsx/frame/*.py``'s inline-append pattern in a
    package that test explicitly keeps free of it.

    ``dsx/frame/*.py`` modules are unaffected and keep writing inline
    (Phase 6-10 precedent) — this helper exists for callers outside that
    package; nothing here changes how ``collect_from_report`` reads the
    result back, since both paths leave the same shape under
    ``report.context[<check-name>]["decisions"]``.
    """
    report.context.setdefault("decisions", []).append(decision_record.to_dict())


def collect_from_report(report: Any) -> list[dict]:
    """Flatten every sub-report's ``decisions`` list out of a merged
    ``Report.context`` (``merge()`` nests each sub-report's context under its
    own check name), in iteration order. Producers append plain dicts onto
    ``report.context.setdefault("decisions", [])`` before merge; this keeps
    checks pure and puts the only file write at the CLI layer."""
    out: list[dict] = []
    for value in report.context.values():
        if isinstance(value, dict):
            decisions = value.get("decisions")
            if isinstance(decisions, list):
                out.extend(decisions)
    return out
