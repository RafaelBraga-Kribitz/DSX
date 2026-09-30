"""dsx command-line interface — the surface GSD gates call.

Every subcommand obeys one contract:

    exit 0  the spec satisfies the check at the configured blocking severity
    exit 1  at least one finding at or above that severity
    exit 2  the check could not run (bad path, unparseable spec, internal error)

GSD's ``command-exit-zero`` gate predicate maps 1 to "block" and 2 to the gate's
``onError`` route, which is exactly the distinction we want: a spec we judged bad
stops the loop; a spec we could not read is an operational error, not a verdict.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import traceback
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from . import __version__
from .checks import (
    chart_review,
    claims,
    code,
    coherence,
    decision,
    design,
    dq,
    figures,
    metrics,
    ml,
    narrative,
    repro,
    smells,
    stats,
    viz,
)
from .decisions import (
    DecisionRecord,
    InvocationHeader,
    collect_from_report,
    decisions_path,
    frame_digest,
    next_invocation_id,
    read_all,
)
from .decisions import (
    append as append_decision,
)
from .findings import EXIT_ERROR, CheckError, Report, Severity, emit, merge
from .frame import admissibility, interference, paradigm, prereg, val
from .loader import SpecParseError, load
from .spec import describe_vocabulary, validate_structure
from .suppressions import apply_suppressions

DEFAULT_SPEC_NAMES = (
    "ANALYSIS-SPEC.yaml",
    "ANALYSIS-SPEC.yml",
    "ANALYSIS-SPEC.json",
    "analysis-spec.yaml",
    "analysis-spec.yml",
    "analysis-spec.json",
)


@dataclass(frozen=True)
class CheckContext:
    """The per-run keyword set ``run_checks`` computes once and hands to every
    registered check. Each ``CheckEntry.run`` picks the fields its module's
    real ``check()`` signature takes.

    ``phase_dir`` is the GSD phase directory as given (repro's entrypoint
    existence checks); ``root`` is where relative evidence paths resolve
    (``resolve_root`` or ``phase_dir``); ``strict`` is true at verify/ship;
    ``reconcile_trail`` is true only for a real ``dsx gate`` at verify/ship.
    """

    phase_dir: str | None
    root: str | None
    strict: bool
    gate_point: str | None
    reconcile_trail: bool


@dataclass(frozen=True)
class CheckEntry:
    """One ``CHECKS`` registry entry. ``check`` is the module's own function,
    whose signature differs by family (see ``dsx/checks/__init__.py``);
    ``run(check, spec, ctx)`` adapts the common ``CheckContext`` onto it."""

    check: Callable[..., Report]
    run: Callable[[Callable[..., Report], dict, CheckContext], Report]


def _spec_only(check: Callable[..., Report], spec: dict, ctx: CheckContext) -> Report:
    return check(spec)


def _admissibility(check: Callable[..., Report], spec: dict, ctx: CheckContext) -> Report:
    # The frequentist-only scoping decision this check needs is forbidden to
    # the adjudicator itself: dsx/frame/admissibility.py is scanned by the
    # D-11 boundary test and must never read inference.paradigm.
    # dsx/frame/paradigm.py is the one module that scanner exempts, so the
    # boolean is computed here, in cli.py where both may be seen, and handed in
    # as a plain parameter — the same shape `strict` and `reconcile_trail`
    # already take. Computed inside this adapter rather than once per run in
    # CheckContext, so the call is paid only when the check actually runs and
    # its helper and consumer stay on adjacent lines for a reader.
    return check(spec, applies_to_frame=paradigm.applies_to_frequentist_admissibility(spec))


# Registry of individual checks — the single source of truth for which check
# names exist and how each is called. `dsx audit` (and a bare `dsx check`)
# runs all of them, in this order.
CHECKS: dict[str, CheckEntry] = {
    "spec": CheckEntry(validate_structure, _spec_only),
    "design": CheckEntry(design.check, lambda f, spec, ctx: f(spec, strict=ctx.strict)),
    "stats": CheckEntry(stats.check, _spec_only),
    "ml": CheckEntry(ml.check, _spec_only),
    "metrics": CheckEntry(metrics.check, _spec_only),
    "claims": CheckEntry(
        claims.check, lambda f, spec, ctx: f(spec, ctx.root, strict=ctx.strict)
    ),
    "viz": CheckEntry(viz.check, _spec_only),
    "coherence": CheckEntry(coherence.check, lambda f, spec, ctx: f(spec, strict=ctx.strict)),
    "dq": CheckEntry(dq.check, lambda f, spec, ctx: f(spec, ctx.root)),
    "smells": CheckEntry(smells.check, _spec_only),
    "figures": CheckEntry(
        figures.check, lambda f, spec, ctx: f(spec, ctx.root, strict=ctx.strict)
    ),
    "narrative": CheckEntry(
        narrative.check, lambda f, spec, ctx: f(spec, ctx.root, gate_point=ctx.gate_point)
    ),
    "code": CheckEntry(code.check, lambda f, spec, ctx: f(spec, ctx.root)),
    "decision": CheckEntry(decision.check, lambda f, spec, ctx: f(spec, gate_point=ctx.gate_point)),
    "paradigm": CheckEntry(paradigm.check, _spec_only),
    "val": CheckEntry(val.check, _spec_only),
    "interference": CheckEntry(interference.check, _spec_only),
    "prereg": CheckEntry(
        prereg.check,
        lambda f, spec, ctx: f(spec, ctx.root, reconcile_trail=ctx.reconcile_trail),
    ),
    "admissibility": CheckEntry(admissibility.check, _admissibility),
    "chart_review": CheckEntry(
        chart_review.check, lambda f, spec, ctx: f(spec, ctx.root, strict=ctx.strict)
    ),
    # repro resolves entrypoints against the phase directory as given, not
    # the evidence root, so it reads ctx.phase_dir rather than ctx.root.
    "repro": CheckEntry(
        repro.check, lambda f, spec, ctx: f(spec, ctx.phase_dir, strict=ctx.strict)
    ),
}

# Which checks each GSD loop point cares about. Keeping this here rather than in
# the capability manifest means the gate command stays short and the policy stays
# versioned with the code that implements it.
#
# "paradigm" (DSX-PAR-001, informational, REQ-P6-09) is registered at all four
# points, not just verify/ship: it must be visible wherever a gate runs, and
# INFO severity means it structurally cannot flip any gate's exit code.
#
# "prereg" is the first family whose gate points differ from the rest of the
# table: it is registered at verify and ship only, and absent from plan and
# execute. There is no executed procedure to reconcile the declared branch
# against until the run has happened, so plan and execute have nothing for
# this family to check — registration is the knob that keeps it off those two
# points. Severity (CRITICAL, dsx/frame/prereg.py) is a separate knob from
# registration: registration decides *where* the family runs at all, severity
# decides whether a fired finding blocks once it does.
#
# "admissibility" (DSX-ADM-*, dsx/frame/admissibility.py) is registered at
# plan, verify and ship, and absent from execute. It is registered at plan
# because an underdetermined frame — a blank estimand type or dependence
# structure, or a declared procedure the ontology cannot resolve — is a
# planning-time defect an analyst can fix before touching data; it is absent
# from execute for the same reason "prereg" is: there is nothing about a run
# in progress for it to adjudicate. Whether the family applies at all to a
# given spec is a third, separate knob from registration and severity: it is
# computed by dsx/frame/paradigm.py::applies_to_frequentist_admissibility and
# passed in by the "admissibility" CHECKS adapter (_admissibility) above, never
# decided inside the adjudicator itself (D-22).
GATE_PROFILES: dict[str, tuple[str, ...]] = {
    "plan": (
        "spec", "design", "metrics", "coherence", "paradigm", "val",
        "interference", "admissibility",
    ),
    "execute": ("spec", "ml", "repro", "dq", "code", "paradigm"),
    "verify": (
        "spec", "design", "stats", "ml", "metrics", "claims", "viz", "repro",
        "dq", "coherence", "smells", "figures", "narrative", "code", "decision",
        "paradigm", "val", "interference", "prereg", "admissibility", "chart_review",
    ),
    "ship": (
        "spec", "design", "stats", "ml", "metrics", "claims", "viz", "repro",
        "dq", "coherence", "smells", "figures", "narrative", "code", "decision",
        "paradigm", "val", "interference", "prereg", "admissibility", "chart_review",
    ),
}

# Environment variable that makes main() print the traceback behind an
# "invalid input" error (see the --help epilog).
DEBUG_ENV = "DSX_DEBUG"

# Default blocking severity per gate. Planning blocks on structural defects;
# shipping blocks on anything material.
GATE_THRESHOLDS: dict[str, str] = {
    "plan": "CRITICAL",
    "execute": "CRITICAL",
    "verify": "HIGH",
    "ship": "HIGH",
}


def find_spec(explicit: str | None, phase_dir: str | None) -> Path:
    if explicit:
        path = Path(explicit)
        if not path.exists():
            raise CheckError(f"spec not found: {path}")
        return path

    roots = [Path(phase_dir)] if phase_dir else []
    roots.extend([Path.cwd(), Path.cwd() / ".planning"])
    for root in roots:
        for name in DEFAULT_SPEC_NAMES:
            candidate = root / name
            if candidate.exists():
                return candidate
    searched = ", ".join(str(r) for r in roots)
    raise CheckError(
        "no ANALYSIS-SPEC found. Looked for "
        + ", ".join(DEFAULT_SPEC_NAMES)
        + f" in: {searched}. Run `dsx init` to scaffold one."
    )


def run_checks(
    spec: dict,
    names: tuple[str, ...],
    phase_dir: str | None,
    *,
    gate_point: str | None = None,
    resolve_root: str | None = None,
    gate_invocation: bool = False,
) -> Report:
    """Run named checks.

    ``phase_dir`` is the GSD phase directory (entrypoint existence checks).
    ``resolve_root`` is where relative evidence/profile paths resolve — defaults
    to ``phase_dir``, then cwd. Callers typically pass the spec's parent so
    ``--spec examples/good-….yaml`` finds sibling artifacts. ``gate_invocation``
    is ``True`` only for a real ``dsx gate`` run — it is what tells a check the
    decision trail is a live gate input, rather than a file the read-only
    inspection commands (``validate``/``check``/``audit``) happen to have
    access to.
    """
    ctx = CheckContext(
        phase_dir=phase_dir,
        root=resolve_root or phase_dir,
        strict=gate_point in {"verify", "ship"},
        gate_point=gate_point,
        reconcile_trail=gate_invocation and gate_point in {"verify", "ship"},
    )
    reports: list[Report] = []
    for name in names:
        entry = CHECKS.get(name)
        if entry is None:
            raise CheckError(
                f"unknown check {name!r}; known: " + ", ".join(sorted(CHECKS))
            )
        reports.append(entry.run(entry.check, spec, ctx))
    merged = merge("+".join(names), reports)
    return apply_suppressions(spec, merged)


# ── Subcommands ──────────────────────────────────────────────────────────────


def cmd_validate(args: argparse.Namespace) -> int:
    path = find_spec(args.spec, args.phase_dir)
    spec = load(path)
    report = run_checks(
        spec,
        ("spec",),
        args.phase_dir,
        resolve_root=args.phase_dir or str(path.parent),
    )
    report.context["spec_path"] = str(path)
    return emit(report, Severity.parse(args.block_on), args.json, args.verbose)


def cmd_check(args: argparse.Namespace) -> int:
    path = find_spec(args.spec, args.phase_dir)
    spec = load(path)
    names = tuple(args.checks) if args.checks else tuple(CHECKS)
    report = run_checks(
        spec,
        names,
        args.phase_dir,
        resolve_root=args.phase_dir or str(path.parent),
    )
    report.context["spec_path"] = str(path)
    return emit(report, Severity.parse(args.block_on), args.json, args.verbose)


def cmd_audit(args: argparse.Namespace) -> int:
    path = find_spec(args.spec, args.phase_dir)
    spec = load(path)
    report = run_checks(
        spec,
        tuple(CHECKS),
        args.phase_dir,
        gate_point="ship",
        resolve_root=args.phase_dir or str(path.parent),
    )
    report.context["spec_path"] = str(path)
    code = emit(report, Severity.parse(args.block_on), args.json, args.verbose)
    if args.report:
        Path(args.report).write_text(
            _markdown_report(report, Severity.parse(args.block_on), str(path)),
            encoding="utf-8",
        )
    return code


def cmd_gate(args: argparse.Namespace) -> int:
    """Run the profile for a GSD loop point. This is what capability.json calls."""
    point = args.point
    # argparse's `choices` already rejects an unknown point on the CLI; this
    # guard is for programmatic callers that build the Namespace themselves
    # (tests/test_cli_charts_init.py pins it).
    if point not in GATE_PROFILES:
        raise CheckError(
            f"unknown gate point {point!r}; expected one of {', '.join(GATE_PROFILES)}"
        )
    threshold = Severity.parse(args.block_on or GATE_THRESHOLDS[point])

    try:
        path = find_spec(args.spec, args.phase_dir)
    except CheckError:
        if args.allow_missing:
            print(
                f"dsx: no ANALYSIS-SPEC found for gate '{point}' — skipping "
                "(dsx.require_spec is disabled)",
                file=sys.stdout,
            )
            return 0
        raise

    spec = load(path)
    root = args.phase_dir or str(path.parent)
    report = run_checks(
        spec,
        GATE_PROFILES[point],
        args.phase_dir,
        gate_point=point,
        resolve_root=root,
        gate_invocation=True,
    )
    report.check = f"gate:{point}"
    report.context["spec_path"] = str(path)
    _write_decision_trail(report, spec, root, point, args.verbose)
    if args.report:
        Path(args.report).write_text(
            _markdown_report(report, threshold, str(path)), encoding="utf-8"
        )
    return emit(report, threshold, args.json, args.verbose)


def _write_decision_trail(
    report: Report, spec: dict, root: str, point: str, verbose: bool
) -> None:
    """Append this gate run's invocation header and decision records to
    ``DECISIONS.jsonl`` (D-14, D-16). Only ``dsx gate`` calls this —
    ``validate``/``check``/``audit`` are read-only inspection commands, not
    the plan-through-ship trail D-04 wants rendered.

    Wrapped in ``try/except Exception`` and swallowed on failure: this is the
    mirror of D-04, ``dsx explain``'s side of the same rule. A trail that
    cannot be written is a missing trail, not a failed gate — the *write*
    path this function implements is a side channel, never part of the block
    contract, so it can never itself change ``point``'s exit code. Surfaced
    only under ``--verbose``.

    From Phase 10 this invariant is scoped to the write path only, not to the
    file as a whole: once a plan-time header has been written here, it
    becomes a *read* input for ``prereg`` (``dsx/frame/prereg.py::
    _check_content_lock``) at verify and ship, where a missing header stops
    the run at exit 2 rather than passing it. The two statements are
    compatible because they describe opposite directions of the same file —
    writing here stays unconditional and inert; reading it, at the gate
    points that opt in via ``gate_invocation``, is conditional and can block.
    Leaving this docstring saying only the old, unqualified half after the
    read side went live would produce a comment that contradicts the code's
    own behaviour, which is exactly the class of drift this project's
    honesty controls exist to catch.

    The guard is deliberately ``Exception``, not ``OSError``: the invariant
    this function documents is unconditional, so naming one exception class
    makes the invariant conditional on the exception taxonomy of everything
    this function calls transitively — ``next_invocation_id``, ``read_all``,
    ``frame_digest``, ``collect_from_report``, ``append`` and the
    ``DecisionRecord`` constructor. The constructor in particular raises
    ``TypeError`` on any future shape drift in the producer-side decision
    dicts, which an ``OSError``-only guard would not catch. The guard stops
    at ``Exception`` — control-flow signals like ``KeyboardInterrupt`` and
    ``SystemExit`` are deliberately left to propagate.

    Concurrency (SEED-004 CL-01): the id derivation and every append run
    under ``trail_lock(target)``, an exclusive OS advisory lock, so two gate
    runs against one root get distinct invocation ids and each run's records
    stay contiguous. Every record is built before the first line is written,
    so a record that fails validation leaves no orphan header. A lock that
    cannot be taken raises ``TrailLockTimeout`` into the same guard: the trail
    is skipped and the gate still exits on its findings.
    """
    from .decisions import trail_lock

    try:
        target = decisions_path(root)
        with trail_lock(target):
            inv = next_invocation_id(target)
            records: list[InvocationHeader | DecisionRecord] = [
                InvocationHeader(
                    invocation_id=inv,
                    gate_point=point,
                    dsx_version=__version__,
                    frame_digest=frame_digest(spec),
                    spec_id=spec.get("spec_id"),
                )
            ]
            for n, raw in enumerate(collect_from_report(report), start=1):
                fields = {k: v for k, v in raw.items() if k != "record_type"}
                fields["id"] = f"DEC-{n:03d}"
                fields["invocation_id"] = inv
                records.append(DecisionRecord(**fields))
            for record in records:
                append_decision(target, record)
    except Exception as exc:  # noqa: BLE001 -- D-04: the trail is a side channel; never fail the gate over it
        if verbose:
            print(f"dsx: could not write decision trail — {exc}", file=sys.stderr)


def cmd_profile(args: argparse.Namespace) -> int:
    from .profiler import profile_csv, write_profile

    pk = [p.strip() for p in (args.pk or "").split(",") if p.strip()] or None
    # Sentinels pass through as the raw strings the user typed: they are the
    # keys `sentinels_found` reports, and the profiler does its own numeric
    # comparison (so `--sentinel -1` still matches a `-1.0` cell).
    sentinels = list(args.sentinel or [])

    profile = profile_csv(
        args.csv,
        primary_key=pk,
        time_column=args.time,
        sentinels=sentinels or None,
        unit=args.unit,
        target=args.target,
    )
    out = Path(args.out or "DATA-PROFILE.yaml")
    write_profile(profile, out)
    summary = {
        "wrote": str(out).replace("\\", "/"),
        "row_count": profile["row_count"],
        "source_hash": profile["source_hash"],
        "primary_key_unique": profile["primary_key_unique"],
        "sentinels_found": profile["sentinels_found"],
    }
    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(
            f"wrote {out} — {profile['row_count']} rows, "
            f"hash={profile['source_hash'][:19]}…"
        )
    return 0


def cmd_recommend(args: argparse.Namespace) -> int:
    from .checks.stats import recommend_test
    from .frame.admissibility import admissible_families
    from .frame.paradigm import applies_to_frequentist_admissibility

    recommendation = recommend_test(
        args.outcome_type,
        args.groups,
        paired=args.paired,
        normal=_tri(args.normal),
        equal_variance=_tri(args.equal_variance),
        n_per_group=args.n_per_group,
        overdispersed=_tri(args.overdispersed),
    )
    # Copy into a new dict so the four existing keys keep their insertion
    # order — recommend_test()'s own return value is never mutated in place.
    out = dict(recommendation)

    # Composition is opt-in only: find_spec(None, None) would search the
    # working directory, making this command's output depend on where the
    # operator happens to be standing, which is exactly what the byte-
    # identity requirement (REQ-P11-05) forbids. 11-RESEARCH.md's auto-
    # discovery variant was considered and rejected for that reason — a
    # spec is composed in only when the operator names one explicitly.
    if args.spec is not None or args.phase_dir is not None:
        path = find_spec(args.spec, args.phase_dir)
        spec = load(path)
        # Same frequentist-only scoping decision run_checks's "admissibility"
        # branch applies (D-22/REQ-P11-05) — admissible_families() has no
        # scoping of its own and always evaluates against the frequentist-only
        # ontology, so a declared non-frequentist paradigm (e.g. bayesian)
        # must never reach it here either, or this command would refuse a
        # procedure the analyst never claimed was frequentist in the first
        # place. Omit the key rather than emit a not-applicable marker,
        # matching admissibility.check()'s own widen-never-penalise shape.
        if applies_to_frequentist_admissibility(spec):
            out["admissibility"] = admissible_families(spec)

    print(json.dumps(out, indent=2))
    return 0


def cmd_power(args: argparse.Namespace) -> int:
    from .mathx import mde_two_proportions, power_two_proportions, sample_size_two_proportions

    out: dict[str, object] = {"alpha": args.alpha, "power": args.power, "baseline": args.baseline}
    if args.mde is not None:
        out["mde"] = args.mde
        out["required_n_per_arm"] = sample_size_two_proportions(
            args.baseline, args.mde, args.alpha, args.power
        )
        if args.n_per_arm:
            out["achieved_power_at_n"] = round(
                power_two_proportions(args.baseline, args.mde, args.n_per_arm, args.alpha), 4
            )
    if args.n_per_arm:
        out["n_per_arm"] = args.n_per_arm
        out["detectable_mde"] = round(
            mde_two_proportions(args.baseline, args.n_per_arm, args.alpha, args.power), 6
        )
    print(json.dumps(out, indent=2))
    return 0


def cmd_vocab(args: argparse.Namespace) -> int:
    print(json.dumps(describe_vocabulary(), indent=2))
    return 0


def cmd_charts(args: argparse.Namespace) -> int:
    """Permitted chart types for a data shape. The lookup that replaces asking.

    Deterministic: same shape and relationship in, same marks out. A missing
    or unknown shape is a usage error, so it exits 2 (``EXIT_ERROR``) like
    every other could-not-run path — exit 1 stays reserved for a blocking
    finding, so a typo in a chart id is never mistaken for a blocked gate.
    """
    from .input_types import UnknownShape, input_types, permitted

    if args.list:
        rows = [
            {
                "id": item["id"],
                "name": item["name"],
                "signature": item["signature"],
                "columns": item["columns"],
                "family": item["family"],
                "admissible": item["admissible"],
            }
            for item in input_types()
        ]
        if args.json:
            print(json.dumps(rows, indent=2))
        else:
            for row in rows:
                print(f"{row['id']}  {row['name']}")
                print(f"        signature: {row['signature']}  ({row['columns']} cols)")
                print(f"        permitted: {', '.join(row['admissible'])}")
        return 0

    if not args.shape:
        print("dsx charts: give a shape (e.g. IT007 or composition) or --list", file=sys.stderr)
        return EXIT_ERROR

    try:
        marks = permitted(args.shape, args.relationship)
    except UnknownShape:
        print(
            f"dsx charts: unknown data shape {args.shape!r}. "
            "Use an inventory id IT001-IT040 or a family name from `dsx vocab`.",
            file=sys.stderr,
        )
        return EXIT_ERROR

    if args.json:
        print(
            json.dumps(
                {
                    "shape": args.shape,
                    "relationship": args.relationship,
                    "permitted": marks,
                },
                indent=2,
            )
        )
    else:
        print(", ".join(marks))
    return 0


def cmd_explain(args: argparse.Namespace) -> int:
    """Render the decision trail (D-04, REQ-P6-08). A pure reader over
    ``DECISIONS.jsonl``: never imports the block-contract primitives (the
    severity ladder, the per-gate threshold table, the report emitter) or
    ``Report`` itself, never blocks, always returns 0 by construction rather
    than by enumeration — modelled on ``cmd_vocab``'s bare ``return 0``, not
    on ``cmd_validate``'s pattern of returning the emitted report's exit code.

    Root resolution is defensive by necessity, not by style: ``find_spec``
    raises ``CheckError`` on a missing explicit ``--spec`` path, and ``main()``
    maps that to exit 2 for every other subcommand. A missing spec is a
    missing trail here, not an error, so the exception is caught and root
    falls back to ``--phase-dir`` (or cwd). That ``CheckError`` guard is about
    root resolution and is separately load-bearing; it is kept exactly as
    written.

    Everything from the trail read through the final print is additionally
    wrapped in a guard over ``Exception`` — control-flow signals like
    ``KeyboardInterrupt``/``SystemExit`` are deliberately left to propagate —
    so no failure mode reachable from ``read_all`` or the render step can
    escape this function. ``read_all`` returns ``[]`` for a missing trail but
    can raise for one that exists and cannot be read, and this guard is what
    makes the "always returns 0" contract a structural property of
    ``cmd_explain`` rather than an enumeration of the failure modes someone
    happened to test.

    A caught failure is never silent: the underlying exception is always
    printed to stderr, and under ``--json`` the output is an object with
    ``"status": "unreadable"`` and the error text, so a broken trail cannot be
    mistaken for an empty one (an empty or absent trail is the JSON array
    ``[]``). Exit 0 either way (D-04).
    """
    path: Path | None = None
    try:
        path = find_spec(args.spec, args.phase_dir)
        root = args.phase_dir or str(path.parent)
    except CheckError:
        root = args.phase_dir or "."

    try:
        records = read_all(decisions_path(root))
        not_found_message = None

        # The self-reported (taken-on-trust) section (D-13) is fed from this
        # same spec load, guarded exactly like `root` above: a spec that
        # cannot be found or parsed yields `spec_data = None`, and
        # `_render_decision_trail` renders no self-reported section rather
        # than raising — the returns-0-by-construction contract is
        # unaffected by whether the spec is readable.
        spec_data: dict | None = None
        if path is not None:
            try:
                spec_data = load(path)
            except Exception:  # noqa: BLE001 -- explain always renders; an unloadable spec renders without it
                spec_data = None

        if args.invocation:
            selected = [r for r in records if r.get("invocation_id") == args.invocation]
            if not selected:
                not_found_message = (
                    f"no decision trail found for invocation {args.invocation!r}"
                )
        else:
            last_id = None
            for record in records:
                if record.get("record_type") == "invocation":
                    last_id = record.get("invocation_id")
            selected = (
                [r for r in records if r.get("invocation_id") == last_id] if last_id else []
            )

        if args.json:
            print(json.dumps(selected, indent=2, sort_keys=True))
        elif not_found_message:
            print(not_found_message)
        else:
            print(_render_decision_trail(selected, spec_data))
    except Exception as exc:  # noqa: BLE001 -- explain always exits 0 (D-04); the failure is reported, not raised
        if args.json:
            print(
                json.dumps(
                    {"status": "unreadable", "error": _describe(exc), "records": []},
                    indent=2,
                    sort_keys=True,
                )
            )
        else:
            print("dsx: no readable decision trail was found", file=sys.stdout)
        print(f"dsx: could not read the decision trail — {_describe(exc)}", file=sys.stderr)
    return 0


def _describe(exc: BaseException) -> str:
    """``TypeName: message`` — the exception text alone is often empty or
    ambiguous (a bare ``KeyError`` prints only the key)."""
    return f"{type(exc).__name__}: {exc}"


def _discover_operator_trails(root: str | Path) -> list[Path]:
    """Every ``DECISIONS.jsonl`` under ``root`` that counts as *operator*
    history (D-13). Hard-**excludes** any trail whose path passes through an
    ``examples/`` tree or a ``templates/`` tree — matched by path COMPONENT,
    not a single hardcoded string literal, so ``examples/DECISIONS.jsonl``,
    ``examples/known-bad/DECISIONS.jsonl`` and ``templates/DECISIONS.jsonl``
    are all dropped.

    The exclusion is the negative-source boundary the whole readout turns on:
    ``examples/known-bad/DECISIONS.jsonl`` is a polluted test floor (~1,151
    invocation records but only ~15 distinct ``frame_digest``, ~45.8%
    raw-Bayesian) that, counted, would inflate the §6.5 item-4 "Bayesian >
    15%" gate roughly four-fold on fixture re-runs. This has no analog in
    ``cmd_explain`` (a single-root reader with no exclusion list at all).

    D-13 is an ABSOLUTE boundary: the fixture floor must NEVER enter the split,
    regardless of where ``--root`` is anchored. The excluded component is
    therefore matched against the trail's RESOLVED path, not its root-relative
    parts (CR-01, 12-REVIEW.md: computing parts as ``relative_to(root)`` stripped
    the very ``examples``/``templates`` component the guard filters on whenever
    ``--root`` pointed *at* or *inside* the fixture tree — e.g.
    ``--root examples/known-bad`` counted the floor at 20% Bayesian). ``resolve()``
    also collapses symlink aliasing, and the compare is case-folded for
    case-insensitive filesystems (Windows: ``Examples`` == ``examples``). The one
    residual — a repository checked out under an ancestor directory literally
    named ``examples``/``templates`` — fails SAFE (the readout goes empty, never a
    false promotion), an accepted known-limit of an absolute-boundary fix.
    """
    root_path = Path(root)
    trails: list[Path] = []
    excluded = {"examples", "templates"}
    for trail in root_path.rglob("DECISIONS.jsonl"):
        if excluded & {part.lower() for part in trail.resolve().parts}:
            continue
        trails.append(trail)
    return trails


def cmd_stats(args: argparse.Namespace) -> int:
    """Operator readouts over the decision trails (REQ-P12-04, D-12). A pure
    reader modelled on ``cmd_explain``'s structural safety: it never imports
    the block-contract primitives (``Severity``/``GATE_THRESHOLDS``/
    ``Report``), carries no ``--block-on``, is not registered in ``CHECKS`` or
    ``GATE_PROFILES``, and ``return 0`` at the end by construction rather than
    by enumeration — it is a readout, never a gate (D-18).

    Dispatch is by report selector flag through ``_STATS_REPORTS``. The
    paradigm split is the only report today and the default when no selector
    is given, so ``dsx stats`` and ``dsx stats --paradigm`` are identical by
    design (IN-01, 12-REVIEW.md). A second report adds its flag in
    ``build_parser`` and one entry in ``_STATS_REPORTS``.
    """
    selected = [name for name in _STATS_REPORTS if getattr(args, name, False)]
    for name in selected or [_STATS_DEFAULT_REPORT]:
        _STATS_REPORTS[name](args)
    return 0


def _stats_paradigm(args: argparse.Namespace) -> None:
    """The ``--paradigm`` report: the frequentist/bayesian/undeclared split.

    Root resolution has a defensive fallback (an unusable ``--root`` degrades
    to ``.planning``), and everything from trail discovery through the final
    print is wrapped in a guard over ``Exception`` — control-flow signals like
    ``KeyboardInterrupt``/``SystemExit`` are deliberately left to propagate —
    so no failure reachable from ``rglob``/``read_all``/the aggregation can
    escape ``cmd_stats``'s "always returns 0" contract, exactly as
    ``cmd_explain`` does. A caught failure is still reported: the exception
    goes to stderr unconditionally and the JSON carries ``"status":
    "unreadable"`` plus ``"error"``, where a readable-but-empty history says
    ``"status": "no_history"`` and a populated one ``"status": "ok"``.
    """
    root = getattr(args, "root", None) or ".planning"

    result: dict[str, Any] = {"root": str(root)}
    try:
        # Dedup by distinct frame_digest (D-14): re-running the same spec
        # collapses to one frame, so raw invocation volume cannot move the
        # split. The frame_digest lives on the invocation header; the paradigm
        # lives in a choice="paradigm=…" decision record tied back by
        # invocation_id — so map invocation_id -> frame_digest per file (ids are
        # only unique within one trail, WR-02) and read one paradigm per
        # distinct frame. This multi-file aggregation is the deliberate
        # divergence from cmd_explain's single-root read (RESEARCH landmine 3):
        # reuse read_all() and the existing digest key, do not reparse trails.
        digest_paradigm: dict[str, str] = {}
        digests_seen: set[str] = set()
        trails = 0
        raw_invocations = 0
        for trail in _discover_operator_trails(root):
            trails += 1
            records = read_all(trail)
            local_inv: dict[str, str] = {}
            for rec in records:
                if rec.get("record_type") == "invocation":
                    raw_invocations += 1
                    digest = rec.get("frame_digest")
                    if digest is None:
                        continue
                    digests_seen.add(digest)
                    inv_id = rec.get("invocation_id")
                    if inv_id is not None:
                        local_inv[inv_id] = digest
            for rec in records:
                if rec.get("record_type") != "decision":
                    continue
                choice = rec.get("choice", "")
                if not (isinstance(choice, str) and choice.startswith("paradigm=")):
                    continue
                digest = local_inv.get(rec.get("invocation_id"))
                if digest is None:
                    continue
                value = choice.split("=", 1)[1]
                if value not in ("frequentist", "bayesian"):
                    value = "undeclared"
                digest_paradigm[digest] = value

        buckets = {"frequentist": 0, "bayesian": 0, "undeclared": 0}
        for digest in digests_seen:
            buckets[digest_paradigm.get(digest, "undeclared")] += 1
        distinct = len(digests_seen)

        result["trails_read"] = trails
        result["distinct_frames"] = distinct
        result["paradigm_split"] = buckets
        # Secondary diagnostic only — the split's one unambiguous denominator
        # is distinct_frames, never this raw count (D-14).
        result["raw_invocation_count"] = raw_invocations
        if distinct == 0:
            result["status"] = "no_history"
            result["message"] = "no operator history yet"
        else:
            result["status"] = "ok"
            result["shares"] = {k: v / distinct for k, v in buckets.items()}
        _print_stats(args, result, distinct)
    except Exception as exc:  # noqa: BLE001 -- stats always exits 0, like explain; the failure is reported, not raised
        result.setdefault("paradigm_split", {"frequentist": 0, "bayesian": 0, "undeclared": 0})
        result.setdefault("distinct_frames", 0)
        result.setdefault("raw_invocation_count", 0)
        result.pop("shares", None)
        result["status"] = "unreadable"
        result["error"] = _describe(exc)
        result["message"] = "operator decision trails could not be read"
        _print_stats(args, result, 0)
        print(f"dsx: could not read operator decision trails — {_describe(exc)}", file=sys.stderr)


# `dsx stats` report selectors: flag name (the argparse dest) -> renderer.
_STATS_REPORTS: dict[str, Callable[[argparse.Namespace], None]] = {
    "paradigm": _stats_paradigm,
}
_STATS_DEFAULT_REPORT = "paradigm"


def _print_stats(args: argparse.Namespace, result: dict[str, Any], denom: int) -> None:
    """Render the paradigm split. ``--json`` is deterministic
    (``sort_keys=True``); the text form labels the raw invocation count as a
    secondary diagnostic so the 15% predicate has one unambiguous
    denominator."""
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
        return
    if result.get("status") == "unreadable":
        print(
            f"dsx: the operator decision trails under {result['root']!r} could not "
            "be read — no split reported (the error is on stderr)."
        )
        return
    if denom == 0:
        print(
            "dsx: no operator history yet — no operator decision trails found "
            f"under {result['root']!r} (examples/ and templates/ excluded)."
        )
        return
    split = result["paradigm_split"]
    shares = result["shares"]
    print(f"paradigm split over {denom} distinct operator frame(s):")
    for name in ("frequentist", "bayesian", "undeclared"):
        print(f"  {name:<12} {split[name]:>4}  ({shares[name] * 100:.1f}%)")
    print(
        "raw invocation count (secondary diagnostic): "
        f"{result.get('raw_invocation_count', 0)}"
    )


def _self_reported_fields(spec: dict) -> list[tuple[str, Any]]:
    """The compared-but-never-computed field set (D-13, T-11.2-11): every
    declared spec value the gate compares against but never itself computes
    -- ``validity_frame.*`` and ``inference.*`` in full (including
    ``inference.declared_at``), plus ``analysis.test`` alone. The rest of the
    ``analysis:`` block (``outcome_type``, ``n_per_group``, etc.) is derived
    from the data by the analyst's own tooling, not a declared trust input,
    so it is deliberately excluded.

    ``frame_digest`` is COMPUTED (lives on the invocation header, not the
    spec) and is never a candidate here by construction -- there is no path
    by which this function could emit it."""
    fields: list[tuple[str, Any]] = []

    def _flatten(prefix: str, value: Any) -> None:
        if isinstance(value, dict):
            for key, sub in value.items():
                _flatten(f"{prefix}.{key}", sub)
        elif isinstance(value, list):
            fields.append((prefix, ", ".join(str(v) for v in value) if value else "[]"))
        else:
            fields.append((prefix, value))

    for top in ("validity_frame", "inference"):
        block = spec.get(top)
        if isinstance(block, dict):
            _flatten(top, block)

    analysis = spec.get("analysis")
    if isinstance(analysis, dict) and "test" in analysis:
        fields.append(("analysis.test", analysis["test"]))

    return fields


def _render_decision_trail(records: list[dict], spec: dict | None = None) -> str:
    """Human-readable text: the invocation header line, then one block per
    decision record, then (D-13) a separately-labelled self-reported section
    listing every declared value the gate compared but never computed.
    ``counterfactual`` is rendered prominently, not as a footnote — 'what
    would have to be different for me to choose otherwise' is the rule the
    record teaches, not just the instance it recorded.

    ``frame_digest`` stays only in the computed header line above — it is
    never passed into ``_self_reported_fields`` and never appears in the
    self-reported block. Labelling a computed value "taken on trust" would be
    the exact honesty inversion this project exists to prevent (T-11.2-11)."""
    if not records:
        return "no decision trail was found."

    lines: list[str] = []
    header = next((r for r in records if r.get("record_type") == "invocation"), None)
    if header:
        lines.append(
            f"invocation {header.get('invocation_id')} "
            f"(gate={header.get('gate_point')}, dsx={header.get('dsx_version')}, "
            f"frame_digest={header.get('frame_digest')})"
        )

    for record in records:
        if record.get("record_type") != "decision":
            continue
        lines.append("")
        lines.append(f"{record.get('id')} [{record.get('layer')}] {record.get('choice')}")
        if record.get("rule"):
            lines.append(f"  rule:           {record['rule']}")
        if record.get("citation"):
            lines.append(f"  citation:       {record['citation']}")
        if record.get("counterfactual"):
            lines.append(f"  counterfactual: {record['counterfactual']}")

    if spec:
        trust_fields = _self_reported_fields(spec)
        if trust_fields:
            lines.append("")
            lines.append("self-reported (taken on trust, not verified by dsx):")
            for field_path, value in trust_fields:
                lines.append(f"  {field_path}: {value}")

    return "\n".join(lines) if lines else "no decision trail was found."


def cmd_init(args: argparse.Namespace) -> int:
    template = Path(__file__).resolve().parent.parent / "templates" / "ANALYSIS-SPEC.yaml"
    if not template.exists():
        raise CheckError(f"template not found at {template}")
    target = Path(args.output or "ANALYSIS-SPEC.yaml")
    if target.exists() and not args.force:
        raise CheckError(f"{target} already exists; pass --force to overwrite")
    target.write_text(template.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"wrote {target}")
    return 0


def cmd_seal(args: argparse.Namespace) -> int:
    # The JSON key is `svg_sha256` for every format (SVG, PNG, HTML): it names
    # the spec field the digest is pasted into (visuals[].svg_sha256, the only
    # seal field dsx/checks/figures.py reads), not the file type.
    from .checks.figures import file_sha256

    path = Path(args.path)
    if not path.exists():
        raise CheckError(f"file not found: {path}")
    digest = file_sha256(path)
    if args.json:
        print(json.dumps({"path": str(path).replace("\\", "/"), "svg_sha256": digest}, indent=2))
    else:
        print(digest)
    return 0


def _tri(value: str | None) -> bool | None:
    if value is None:
        return None
    lowered = value.strip().lower()
    if lowered in ("true", "yes", "1"):
        return True
    if lowered in ("false", "no", "0"):
        return False
    return None


def _markdown_report(report: Report, threshold: Severity, spec_path: str) -> str:
    counts = report.counts()
    verdict = "BLOCKED" if report.blocks(threshold) else "PASSED"
    lines = [
        f"# dsx report — {report.check}",
        "",
        f"- **Verdict:** {verdict} (blocking at {threshold.label})",
        f"- **Spec:** `{spec_path}`",
        "- **Findings:** "
        + ", ".join(f"{k} {v}" for k, v in counts.items() if v),
        "",
    ]
    if report.findings:
        lines += ["## Findings", ""]
        for finding in sorted(report.findings, key=lambda f: (-f.severity, f.code)):
            lines += [
                f"### {finding.code} — {finding.title}",
                "",
                f"**Severity:** {finding.severity.label}  ",
                f"**Where:** `{finding.where or 'n/a'}`",
                "",
            ]
            if finding.detail:
                lines += [finding.detail, ""]
            if finding.remedy:
                lines += [f"**Fix:** {finding.remedy}", ""]
    applied = report.context.get("suppressions_applied") or []
    if applied:
        lines += ["## Suppressions applied", ""]
        for row in applied:
            chart = f" (chart_id={row['chart_id']})" if row.get("chart_id") else ""
            lines += [
                f"- `{row['code']}`{chart}: {row['reason']} — authority: {row['authority']}",
            ]
        lines.append("")
    if report.passed_checks:
        lines += ["## Passed", ""]
        lines += [f"- {item}" for item in sorted(set(report.passed_checks))]
        lines.append("")
    return "\n".join(lines)


# ── Parser ───────────────────────────────────────────────────────────────────


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dsx",
        description="Deterministic guardrails for data-science, analytics and BI work.",
        epilog=(
            "Exit codes: 0 pass, 1 block, 2 could not run. "
            f"Set {DEBUG_ENV}=1 (or pass --verbose) to print a traceback on "
            "stderr when a command fails with an invalid-input error, so an "
            "internal bug is not mistaken for bad input."
        ),
    )
    parser.add_argument("--version", action="version", version=f"dsx {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    def add_common(
        p: argparse.ArgumentParser,
        default_block: str = "HIGH",
        *,
        include_block_on: bool = True,
    ) -> None:
        p.add_argument("--spec", help="path to ANALYSIS-SPEC (auto-discovered when omitted)")
        p.add_argument("--phase-dir", help="GSD phase directory to search and resolve paths against")
        if include_block_on:
            p.add_argument("--block-on", default=default_block,
                           help="minimum severity that fails the command (default: %(default)s)")
        p.add_argument("--json", action="store_true", help="emit machine-readable JSON")
        p.add_argument("--verbose", action="store_true", help="list checks that passed")

    p_validate = sub.add_parser("validate", help="structural validation of the spec only")
    add_common(p_validate, "CRITICAL")
    p_validate.set_defaults(func=cmd_validate)

    p_check = sub.add_parser("check", help="run selected checks")
    p_check.add_argument("checks", nargs="*", help="subset to run: " + ", ".join(sorted(CHECKS)))
    add_common(p_check)
    p_check.set_defaults(func=cmd_check)

    p_audit = sub.add_parser("audit", help="run every check")
    add_common(p_audit)
    p_audit.add_argument("--report", help="also write a markdown report to this path")
    p_audit.set_defaults(func=cmd_audit)

    p_gate = sub.add_parser("gate", help="run the profile for a GSD loop point")
    p_gate.add_argument("point", choices=sorted(GATE_PROFILES))
    add_common(p_gate, "")
    p_gate.add_argument("--report", help="also write a markdown report to this path")
    p_gate.add_argument("--allow-missing", action="store_true",
                        help="exit 0 when no spec exists instead of erroring")
    p_gate.set_defaults(func=cmd_gate)

    p_explain = sub.add_parser(
        "explain",
        help="render the decision trail from DECISIONS.jsonl — read-only, never blocks",
    )
    add_common(p_explain, include_block_on=False)
    p_explain.add_argument("--invocation", help="render only this invocation id's records")
    p_explain.set_defaults(func=cmd_explain)

    p_stats = sub.add_parser(
        "stats",
        help="report the operator's own paradigm split — read-only, never blocks",
    )
    # Deliberately NOT add_common(...): that helper also adds --block-on, and
    # this command always passes (D-12) — a blocking-severity flag on a reader
    # that returns 0 by construction would be a lie in the help text, the same
    # reasoning already recorded for `explain`/`recommend-test`. It is NOT
    # registered in CHECKS or GATE_PROFILES; it is a readout, not a gate (D-18).
    # Each report selector flag's dest is a key of _STATS_REPORTS, which
    # cmd_stats dispatches on. --paradigm is the only report today and the
    # default when no selector is given (IN-01, 12-REVIEW.md), so a bare
    # `dsx stats` reporting the same split is by design, not a false contract.
    p_stats.add_argument("--paradigm", action="store_true",
                         help="report the frequentist/bayesian/undeclared frame split "
                              "(the default report when no selector is given)")
    p_stats.add_argument("--root", default=".planning",
                         help="operator trail search root (default: %(default)s; D-13)")
    p_stats.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    p_stats.add_argument("--verbose", action="store_true",
                         help="accepted for symmetry; read errors always go to stderr")
    p_stats.set_defaults(func=cmd_stats)

    p_rec = sub.add_parser("recommend-test", help="derive the correct test from the data's shape")
    p_rec.add_argument("outcome_type", help="proportion | continuous | count | ordinal | time_to_event")
    p_rec.add_argument("--groups", type=int, default=2)
    p_rec.add_argument("--paired", action="store_true")
    p_rec.add_argument("--normal", choices=["true", "false"])
    p_rec.add_argument("--equal-variance", choices=["true", "false"])
    p_rec.add_argument("--overdispersed", choices=["true", "false"])
    p_rec.add_argument("--n-per-group", type=int)
    # Deliberately not add_common(...): that helper also adds --block-on,
    # and this command never blocks — a blocking-severity flag on a command
    # that always exits 0 (once its spec resolves) would be a lie in the
    # help text, the same reasoning already recorded for `explain` (D-04).
    # Only the two spec-resolution flags are added, additively (D-04a).
    p_rec.add_argument("--spec", help="path to ANALYSIS-SPEC (adds an admissibility section)")
    p_rec.add_argument("--phase-dir", help="GSD phase directory to resolve --spec against")
    p_rec.set_defaults(func=cmd_recommend)

    p_power = sub.add_parser("power", help="sample size, achieved power and detectable effect")
    p_power.add_argument("--baseline", type=float, required=True, help="baseline proportion")
    p_power.add_argument("--mde", type=float, help="absolute minimum detectable effect")
    p_power.add_argument("--n-per-arm", type=int)
    p_power.add_argument("--alpha", type=float, default=0.05)
    p_power.add_argument("--power", type=float, default=0.80)
    p_power.set_defaults(func=cmd_power)

    p_vocab = sub.add_parser("vocab", help="dump every closed vocabulary as JSON")
    p_vocab.set_defaults(func=cmd_vocab)

    p_charts = sub.add_parser(
        "charts", help="permitted chart types for a data shape (IT001-IT040 or family)"
    )
    p_charts.add_argument("shape", nargs="?", help="inventory id (IT007) or family (composition)")
    p_charts.add_argument(
        "--relationship", help="narrow by relationship (comparison, trend, …)"
    )
    p_charts.add_argument("--list", action="store_true", help="print the whole catalogue")
    p_charts.add_argument("--json", action="store_true", help="machine-readable output")
    p_charts.set_defaults(func=cmd_charts)

    p_init = sub.add_parser("init", help="scaffold an ANALYSIS-SPEC from the template")
    p_init.add_argument("--output", "-o")
    p_init.add_argument("--force", action="store_true")
    p_init.set_defaults(func=cmd_init)

    p_profile = sub.add_parser(
        "profile",
        help="compute a DATA-PROFILE.yaml from a local CSV (stdlib)",
    )
    p_profile.add_argument("csv", help="path to a CSV extract")
    p_profile.add_argument("--out", "-o", default="DATA-PROFILE.yaml")
    p_profile.add_argument("--pk", help="comma-separated primary key columns")
    p_profile.add_argument("--time", help="time column for gap detection")
    p_profile.add_argument("--unit", help="unit column for rows-per-unit stats")
    p_profile.add_argument(
        "--target",
        help="binary {0,1} target column for the weekly base rate (requires --time)",
    )
    p_profile.add_argument(
        "--sentinel",
        action="append",
        help="banned sentinel value to scan for (repeatable)",
    )
    p_profile.add_argument("--json", action="store_true")
    p_profile.set_defaults(func=cmd_profile)

    p_seal = sub.add_parser(
        "seal",
        help="compute sha256:… for a figure file to paste into visuals[].svg_sha256",
        description=(
            "Compute the sha256:… seal of a figure file. The seal goes in the spec's "
            "visuals[].svg_sha256 field whatever the format — SVG, PNG or HTML — so "
            "the --json output names the key svg_sha256 for every format too."
        ),
    )
    p_seal.add_argument("path", help="path to an SVG/PNG/HTML figure")
    p_seal.add_argument(
        "--json", action="store_true",
        help="emit {path, svg_sha256}; the key is svg_sha256 for every format",
    )
    p_seal.set_defaults(func=cmd_seal)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return int(args.func(args))
    except (CheckError, SpecParseError) as exc:
        print(f"dsx: {exc}", file=sys.stderr)
        return EXIT_ERROR
    except ValueError as exc:
        # Most ValueErrors are genuine bad input (a severity name, a number
        # out of range), but a check bug surfaces the same way. The message
        # and exit 2 stay; the traceback is one env var away.
        print(f"dsx: invalid input — {exc}", file=sys.stderr)
        debug = os.environ.get(DEBUG_ENV, "").strip() not in ("", "0")
        if debug or getattr(args, "verbose", False):
            traceback.print_exc(file=sys.stderr)
        else:
            print(f"dsx: set {DEBUG_ENV}=1 or pass --verbose for the traceback", file=sys.stderr)
        return EXIT_ERROR
    except KeyboardInterrupt:  # pragma: no cover
        return 130


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
