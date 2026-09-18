---
name: ds-skill--data-quality-audit
description: >
  Structured data quality assessment before any analysis. Checks completeness,
  consistency, validity, timeliness, and uniqueness. Outputs a quality scorecard
  and go/no-go fitness verdict with caveats.
tags: [skill, data-quality, eda, profiling, validation]
---

# Data Quality Audit

## When to Use
- First time using a new data source
- After a data pipeline change
- When EDA reveals unexpected patterns
- Before any high-stakes analysis or model training

## 5-Dimension Framework (DAMA-based)

### 1. Completeness
> Are all expected records and fields present?

```
Checks:
□ Row count vs expected (from source system or prior pulls)
□ % null per column (flag >5%)
□ Required fields (PK, date, metric) — must be 100% populated
□ Expected date range fully covered (no gaps)

Score: (non-null critical fields / expected) × 100
```

### 2. Consistency
> Do values agree across sources and within the dataset?

```
Checks:
□ Cross-source reconciliation: does sum(revenue) in DWH = source system?
□ Internal consistency: does revenue = price × qty × (1 - discount)?
□ Referential integrity: do FK values exist in reference tables?
□ No duplicate primary keys

Score: (consistent records / total records) × 100
```

### 3. Validity
> Do values conform to business rules and expected domains?

```
Checks:
□ Revenue, quantity ≥ 0
□ Dates in valid range (not future, not before business start date)
□ Categorical values in expected set (no unknown status codes)
□ Numeric values in plausible range (no 999999 placeholder)
□ Email, phone format valid if applicable

Score: (valid records / total records) × 100
```

### 4. Timeliness
> Is the data fresh enough for the use case?

```
Checks:
□ Most recent record timestamp vs expected refresh cadence
□ Max lag acceptable: daily analysis → <24h, real-time → <1h
□ Is the pipeline latency documented?

Score: pass / fail / degraded
```

### 5. Uniqueness
> Are records deduplicated as expected?

```
Checks:
□ Primary key uniqueness: COUNT(*) = COUNT(DISTINCT pk)
□ Expected grain matches actual grain (e.g., 1 row per user per day)
□ Dedup logic documented if applied

Score: (unique PK records / total records) × 100
```

## Quality Scorecard Output

```markdown
## Data Quality Report: [Table/Dataset] — [Date]

### Overall Fitness: [READY | READY WITH CAVEATS | NOT READY]

| Dimension | Score | Issues Found | Decision |
|-----------|-------|-------------|---------|
| Completeness | X% | [issue or none] | proceed / flag / block |
| Consistency | X% | [issue or none] | proceed / fix / block |
| Validity | X% | [issue or none] | proceed / exclude / block |
| Timeliness | pass/fail | [issue or none] | proceed / delay |
| Uniqueness | X% | [issue or none] | proceed / dedup / block |

### Critical Issues (must fix before analysis)
1. [Issue]: affects X% of rows — [recommended action]

### Non-Critical Issues (document as caveats)
1. [Issue]: affects X% of rows — [caveat wording for output]

### Recommended Analysis Caveats
- "Results exclude X records due to [data quality issue]"
- "Revenue figures may be understated by ~X% due to [issue]"
```

## Decision Rules
| Score | Action |
|-------|--------|
| All dimensions >95% | Ready — proceed |
| Critical dimension 80-95% | Ready with caveats — document |
| Any critical dimension <80% | Not ready — fix or rescope |
| Consistency <90% | Block — reconcile before analysis |
