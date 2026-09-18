# LifeOS Fractal System — Opus Builder Prompt

**Paste this entire file as your opening message to Claude Opus.**  
**Mode: BUILDER — produce all implementation artifacts.**

---

## Your Mission

You are a senior system architect. Build the full implementation of a deterministic personal operating system called **LifeOS** for Rafael, a Brazilian professional (born 1981, Styria/Vienna, Austria) transitioning from senior digital marketing into Data Analysis/BI and Data Science.

Rafael operates across: Obsidian (knowledge vault), GitHub (execution ledger), Google Calendar (capacity ledger), and Claude (primary orchestrator agent — you).

Produce all implementation artifacts listed in the Deliverables section below. Every artifact must be implementation-ready, not advisory.

---

## Non-Negotiable Constraints

1. **No hard delete** anywhere in the system. Terminal action: export + exclude-from-queries + archive.
2. **Single facet owner per object dimension.** No system claims dual canonical ownership over the same facet.
3. **Confidence-gated autonomy.** No autonomous mutation without evidence triple: `schema_validation_pass`, `source_coverage_count`, `conflict_check_pass`. Missing field forces blocked/gated.
4. **Fractal Simplicity Law.** Top layers short and stable; complexity increases only downward. No tool playbooks at Principles/GovernanceRules level.
5. **Method precedence must be explicit.** No "it depends" without attached decision criteria.
6. **All workflows** must include: trigger, inputs, process, outputs, owner, completion criteria, failure path.

---

## Architecture Summary

### Dual System

**Action Hierarchy** (GitHub + GCal):
- Methods: GTD, PARA, Cascading Goals, Johnny Decimal, COG
- State machine: `inbox → clarified → next → scheduled → inprogress → done → voided → archived`
- Execution state canonical: GitHub. Time/capacity canonical: GCal.

**Knowledge Network** (Obsidian):
- Methods: Zettelkasten, IDI, Two-layer Second Brain, Claudesidian
- Note types: `fleeting | atom | molecule | project-note | evergreen`
- Knowledge state canonical: Obsidian.

**Bidirectional interface:** atoms/molecules surface ACE tasks; closed GitHub issues generate IDI knowledge updates; project-notes reference GitHub project_ids; deep work sessions trigger COG scheduling.

### Three Core Workflows

**IDI** (Knowledge): `unprocessed fleeting note → digest (extract claim, find links) → integrate (atom + min 2 links)`. Owner: Claude if confidence ≥ 90.

**ACE** (Execution): `action item → GitHub issue (verb title + Obsidian link + DoD + estimate)`. Owner: Claude if confidence ≥ 90.

**COG** (Scheduling): `issue with estimate in Next state → staged GCal block proposal`. Owner: Claude generates proposal; human always confirms. Never auto-confirm.

### Confidence Bands

```
confidence >= 90   → auto-execute (audit on real state change)
75 <= confidence < 90 → approval-gated (stage for human)
confidence < 75    → blocked (DLQ entry; human triage)
Missing evidence field → force confidence < 75
```

Registry defaults: `AUTO_EXECUTE_MIN=90`, `APPROVAL_MIN=75`, `MAX_ACTIVE_PROJECTS=12`, `MIN_LINKS_PER_ATOM=2`, `CAPACITY_ALERT_PCT=20`, `MAX_FOLDER_DEPTH=3`.

### Facet Source of Truth

| Facet | Canonical | Mirror |
|---|---|---|
| Execution state | GitHub | Obsidian (read-only) |
| Time/capacity | Google Calendar | Obsidian daily note |
| Narrative/context | Obsidian | GitHub (link + snippet) |
| Note graph | Obsidian | — |
| Policy registry | Versioned repo doc | — |

**Conflict order:** capacity (GCal) → execution state (GitHub) → containment (Obsidian + PARA) → knowledge synthesis → convenience.

### Method Integration

| Method | Role | Notes |
|---|---|---|
| GTD | Capture/clarify/weekly review backbone | GitHub is canonical for state |
| PARA | Container taxonomy | Applies to both Obsidian vault and GitHub labels |
| Zettelkasten | Atomic note format | note_id immutable; min 2 links per atom |
| Johnny Decimal | Address scheme for Obsidian paths | Global grammar root; PARA adds scoped suffixes only |
| ACE | GitHub issue shape: Action + Context + Execution | Required format; deviations flagged |
| IDI | Inbox → Digest → Integrate | Trigger: unprocessed fleeting note |
| COG | Categorize → Organize → Generate calendar | GCal blocks always staged; never auto-confirmed |
| Cascading Goals | Annual → quarterly → project → task decomposition | Stored in Obsidian; GitHub milestones mirror project goals |

### Deployment Profiles

| Profile | Capabilities | Gate |
|---|---|---|
| A (Advisory) | Read + plan only; no autonomous writes | Zero harmful incidents; human signs checklist |
| B (Bounded) | Auto IDI + auto ACE + staged COG; external writes gated | DLQ SLA met; reconciliation drill; kill-switch drill |
| C (Full Policy) | All confidence-gated ops; kill-switch + DLQ live | Continuous; regress to B on kill-switch trigger |

### Naming Convention

Global grammar: `<scope>-<topic>--<qualifier>` — lowercase, hyphens only, max 64 chars.  
Examples: `doc-2025-annual-review`, `area-health--sleep-protocol`, `proj-ds-journey--milestone-1`.

---

## Deliverables

Build all of the following. Save each as a file in `~/lifeOS/lifeos-fractal-architect/implementation/`.

### 1. Obsidian Vault Structure (`vault-structure.md`)
Complete folder hierarchy using PARA + Johnny Decimal. Include:
- Top-level PARA folders with JD addresses for each of Rafael's life areas (professional, health/fitness, learning/DS-journey, relationships, finance, personal-projects)
- Subfolder rules and depth limits (max 3)
- Note type folder conventions (fleeting inbox, atoms, molecules, evergreens, project-notes)
- Archive folder conventions
- Template file list (one template per note type)

### 2. Obsidian Note Templates (`templates/`)
Produce actual template file content for:
- `template-fleeting.md` — raw capture with YAML front matter
- `template-atom.md` — single permanent idea with required link fields
- `template-molecule.md` — synthesis note
- `template-project-note.md` — project context linked to GitHub
- `template-evergreen.md` — mature stable knowledge
- `template-daily-note.md` — daily anchor with GCal mirror, focus list, carry-forward

Each template must include complete YAML front matter fields matching the data model.

### 3. GitHub Project Structure (`github-structure.md`)
Define:
- Project board columns (matching the lifecycle state machine)
- Issue label taxonomy (risk_class, PARA area, note type, state flags)
- ACE issue template (complete `.github/ISSUE_TEMPLATE/ace-task.yml`)
- Milestone naming convention (cascading goals alignment)
- GitHub Actions or automation hooks for state sync (what triggers what)

### 4. CLAUDE.md Files (`claude-mds/`)
Produce content for:
- `root-CLAUDE.md` — universal heuristics + routing table (≤ 400 words)
- `professional-CLAUDE.md` — rules for professional/DS-journey area (≤ 800 words)
- `health-CLAUDE.md` — rules for health/fitness area (≤ 800 words)
- `lifeos-project-CLAUDE.md` — rules for the lifeos build project itself (≤ 1200 words)

Each file must follow the fractal harness stack: no duplication across layers; link downward.

### 5. Google Calendar Setup (`gcal-setup.md`)
Define:
- Calendar names and color conventions (one per PARA Area + one meta/admin)
- Event naming convention (aligned to global grammar)
- Staged event convention (how staged vs confirmed events are differentiated)
- Block types: deep work, review anchor, COG-scheduled execution, personal commitment
- Capacity rules: `CAPACITY_ALERT_PCT=20` buffer per week; how to compute it

### 6. Review Checklists (`review-checklists/`)
Produce step-by-step executable checklists for:
- `daily-review-checklist.md` — 10–20 min; each step has a specific action and artifact output
- `weekly-review-checklist.md` — 45–90 min; same format
- `monthly-review-checklist.md` — 60–120 min; includes registry tuning and profile gate check

Each checklist step: `[ ] Action → artifact produced → canonical system updated`.

### 7. Autonomy Policy Matrix (`autonomy-matrix.md`)
Full matrix of every operation Claude might perform, with:
- Operation name
- Risk class
- Minimum deployment profile
- Confidence band
- Rollback/compensation mechanism
- Specific evidence fields required

Include at minimum 25 operation rows covering IDI, ACE, COG, review, archive, and naming operations.

### 8. Data Model Schemas (`data-model.md`)
Complete YAML schemas for all six entities: Task, Project, Note, Event, Deliverable, Area.
For each entity: all fields, types, minting system, required vs optional, and validation rules.
Plus: UUID minting rules, lifecycle state machine diagram (Mermaid), conflict resolution order.

### 9. Anti-Patterns Catalog (`anti-patterns.md`)
Minimum 12 named anti-patterns, each with:
- Name
- Description
- Diagnostic signal
- Root cause
- Corrective action
- Regression check to add

Plus: 8 active automated guardrails table.

### 10. Bootstrap Runbook (`bootstrap-runbook.md`)
Step-by-step instructions for Rafael to go from zero to deployed Profile B. Includes:
- Phase 0 (Baseline): exact commands to set up vault structure, GitHub project, and Calendar
- Phase 1 (Knowledge hygiene): IDI backlog processing procedure
- Phase 2 (Action execution): ACE activation and first weekly review
- Phase 3 (Profile B): gate checklist and activation procedure
- Estimated time per phase
- Definition of "done" for each phase gate

---

## Quality Gates

Before delivering any artifact:
- [ ] Every workflow has trigger, inputs, outputs, owner, completion criteria, failure path.
- [ ] No "it depends" without attached decision criteria.
- [ ] No hard delete anywhere.
- [ ] No duplicate MUST/NEVER across layers.
- [ ] Every entity schema has a named canonical system.
- [ ] Language is imperative and testable.
- [ ] All KPIs have owner, source, and breach playbook.

---

## Rafael's Context (apply throughout)

- Transitioning from 20 years in data-driven digital marketing into Data Analysis/BI → Data Science/AI
- Lives in Seiersberg-Pirka, Styria, Austria; often in Vienna for study
- Languages: PT-BR (native), EN-US (fluent), DE-AT (beginner)
- Current learning focus: Python, R, SQL, Jupyter, Docker, Git/GitHub, Linux/Bash
- Style: direct, professional, no sugarcoating; prefers step-by-step with examples
- Naming preference: English for all system constructs

The system must support Rafael's DS journey as a first-class life area, with project tracking for courses, notebooks, and portfolio work integrated into the PARA structure.
