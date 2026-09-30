---
id: SEED-005
status: dormant
planted: 2026-09-30
planted_during: project audit 2026-09-30 (item L75) — a Phase 13 deferral found carried with no entry condition, contrary to D-13
trigger_when: a known-bad corpus case whose target defect is a narrative that omits its "So What" (the action the pre-declared rule implies) or its "Now What" (what would change the verdict) is measured a LIVE MISS at all four gate points — every existing DSX-NAR, DSX-CLM and DSX-COH check clearing on it — AND a milestone opens that is allowed to mint a code
scope: small once triggered — one check in `dsx/checks/narrative.py`, one D-05 citation, one fixture; a D-13 evidence phase first, never a mint on the strength of the template alone
---

# SEED-005: A narrative-shape gate (a `DSX-NAR` section check)

## What is true today (verified 2026-09-30 against the code)

- `skills/dsx-narrate/SKILL.md` (`:55-68`) prescribes a five-part narrative carrying an
  explicit **What / So What / Now What** shape, and says plainly that the shape "mints no new
  narrative code and adds no heading-scanner gate".
- `dsx/checks/narrative.py` emits `DSX-NAR-001`/`-010` (narrative path), `DSX-NAR-020`
  (declared claim text present in the narrative), `DSX-NAR-030` (forbidden wording),
  `DSX-NAR-040` (relative % without a base) and `DSX-NAR-050` (dashboard path). None of them
  reads the narrative's sections, so a narrative with no "So What" or "Now What" passes.
- Parts of the "Now What" half are already gated through the spec, not the prose:
  `decision.revisit_when` (`DSX-COH-040`) and a non-empty `limitations[]` (`DSX-CLM-080`).
  The gap is that the narrative itself is never checked for saying them.
- Origin: Phase 13 decision D-04 made the shape template-only, and the deferred-ideas list
  (`.planning/milestones/v2.2-phases/13-task-playbooks-that-fill-the-spec/13-CONTEXT.md:301`)
  parked the gate "to a future milestone that opens the catalogue, if ever wanted" — with no
  entry condition, which D-13 (`.planning/PROJECT.md`) does not allow.

## Why this is a seed and not a fix now

No corpus case has shown the shape's absence letting a bad readout through: every known-bad
fixture is caught or missed for reasons unrelated to section order. A heading scanner built
without such a case would be a style rule with a CRITICAL/HIGH severity attached, and would
also be the first `DSX-*` check that judges prose structure rather than a declared fact or a
literal string. D-13 says build the case and measure it first.

## Entry condition (D-13)

Both, in this order:

1. **The case.** Build a known-bad fixture whose narrative states the number (What) but
   omits the implied action or the evidence that would flip it, with the spec otherwise clean
   (`decision.revisit_when` and `limitations[]` declared, so `DSX-COH-040` and `DSX-CLM-080`
   clear). Measure it at `plan`, `execute`, `verify` and `ship` from a fresh temp directory
   and record a `VERDICT:` line, as Phases 27–29 did. If any existing code already fires on
   the target defect, close this seed with that code named and mint nothing.
2. **The source.** An admissible D-05 source that states the omitted-implication or
   omitted-reversal-condition failure as a reporting defect, read first-hand at its locator.
   A style guide or a vendor blog does not qualify.

## Sibling deferral recorded here (Phase 14)

Phase 14 deferred "a gate check for DATA-DICTIONARY / learnings / the disclosure block" on
the same "would mint a code … if ever wanted" wording
(`.planning/milestones/v2.2-phases/14-compounding-and-data-onboarding/14-CONTEXT.md:352`).
It takes the same entry condition: a known-bad case whose target defect is a missing
research-domain AI-assistance disclosure (or an absent data dictionary the spec relies on),
measured a LIVE MISS at all four gate points, plus a first-hand D-05 source. Until then it
stays template-only, like the narrative shape.

## Breadcrumbs

- `skills/dsx-narrate/SKILL.md:55-68` — the shape, and the "no heading-scanner gate" sentence
- `dsx/checks/narrative.py` — the existing `DSX-NAR-*` checks
- `.planning/milestones/v2.2-phases/13-task-playbooks-that-fill-the-spec/13-CONTEXT.md:127, 301`
  — D-04 and the deferral
- `.planning/milestones/v2.2-phases/14-compounding-and-data-onboarding/14-CONTEXT.md:352`
  — the Phase 14 sibling
