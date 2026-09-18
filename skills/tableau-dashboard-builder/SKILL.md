---
name: tableau-dashboard-builder
description: Build Tableau TWB/TWBX dashboards from CSV or Hyper data using validated XML patterns, Hyper extract packaging, and headless validation. Use when creating or fixing Tableau workbooks, generating TWB from scripts, packaging TWBX for Tableau Public, extracting patterns from reference TWBX files, or diagnosing Tableau Desktop load errors (Measure Names, Measure Values, extract connection, DF4A1293).
---

# Tableau Dashboard Builder

Generate reproducible Tableau workbooks programmatically. Prefer reference TWB patterns over invented XML.

## Quick start

1. Profile input data (CSV columns, types, row counts).
2. Extract patterns from working reference `.twbx` files if available.
3. Generate Hyper extracts (Tableau Public) and TWB via Python generator.
4. Package TWBX (`.twb` + `Data/Extracts/*.hyper`).
5. Run headless validation before claiming success.
6. Require manual Tableau Desktop QA for visual correctness.

```bash
python3 scripts/validate_twb.py path/to/workbook.twb path/to/workbook.twbx
python3 scripts/extract_twb_refs.py --scan reference.twbx --out _twb_refs/
```

## Workflow

Follow [workflow.md](workflow.md) for the full intake → generate → validate → QA loop.

## Reference docs

| File | When to read |
|------|--------------|
| [twb-patterns.md](twb-patterns.md) | Emitting or fixing TWB XML (fields, extracts, worksheets, dashboards) |
| [anti-patterns.md](anti-patterns.md) | Tableau load errors, missing fields, internal errors |
| [known-unknowns.md](known-unknowns.md) | Limits of headless validation; unresolved issues |
| [examples.md](examples.md) | warehouse_humanoid_tco reference implementation |

## Core rules (always apply)

- Field references MUST be datasource-scoped: `[federated.x].[sum:field:qk]`.
- Measure Values shelf/encoding: `[ds].[Multiple Values]` — NEVER `[ds].[:Measure Values]`.
- Measure Names filter members and palette buckets: fully qualified column instances, not raw `[field]`.
- Hyper extract connection MUST include inner `<relation name='Extract' table='[Extract].[Extract]' type='table' />`.
- TWBX MUST contain the TWB and every `.hyper` under `Data/Extracts/`.
- XML validation passing does NOT mean the dashboard renders correctly in Tableau Desktop.

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/validate_twb.py` | Parse TWB/TWBX, detect anti-patterns, report [PASS]/[FAIL] |
| `scripts/extract_twb_refs.py` | Extract TWB from TWBX references, optional pattern scan |

## When to escalate

- Tableau Desktop shows field-removal warnings → read [anti-patterns.md](anti-patterns.md), compare filter members to reference TWBs.
- Internal error DF4A1293 / A1232EF3 → often malformed pseudo-fields or incomplete extract metadata.
- Workbook loads but a sheet is empty (e.g. payback KPI) → see [known-unknowns.md](known-unknowns.md); do not close without Desktop verification.
