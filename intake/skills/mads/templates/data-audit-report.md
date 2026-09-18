# Data Audit Report (DAR)

> Document owner: Diego
> Status: DRAFT | COMPLETE | FEASIBLE | FEASIBLE WITH CAVEATS | NOT FEASIBLE
> Version: 1.0
> Date:
> References MAB version:

---

## 1. Data Source Inventory

| Source name | Type | Owner | Refresh cadence | Access confirmed |
|-------------|------|-------|----------------|-----------------|
| | Events log | | Daily | Yes / No / Pending |
| | CRM export | | Weekly | Yes / No / Pending |
| | | | | |

**Access issues to resolve before proceeding:**

---

## 2. Schema Profiles

*One section per data source.*

### Source: {source_name}

| Column | Dtype | Nullable | Null % | Cardinality | Notes |
|--------|-------|----------|--------|-------------|-------|
| user_id | STRING | No | 0.0% | High | Primary key |
| event_date | DATE | No | 0.0% | Medium | |
| | | | | | |

**Row count:** {N}
**Date range:** {start} to {end}
**Duplicate rate on primary key:** {pct}%

**Anomalies found:**

---

## 3. Quality Dimensions Assessment

| Dimension | Check | Finding | Flag |
|-----------|-------|---------|------|
| Completeness | Null rate per key column | | ✅ / ⚠️ / ❌ |
| Uniqueness | Duplicate rate on PK | | ✅ / ⚠️ / ❌ |
| Validity | Values within expected range | | ✅ / ⚠️ / ❌ |
| Consistency | Cross-table referential integrity | | ✅ / ⚠️ / ❌ |
| Timeliness | Data freshness vs. MAB requirement | | ✅ / ⚠️ / ❌ |
| Representativeness | Coverage of target population | | ✅ / ⚠️ / ❌ |

**Key quality issues:**

---

## 4. Target Variable Analysis

**Target variable:** {label_name}

**Distribution:**

| Statistic | Value |
|-----------|-------|
| N (total rows) | |
| N positive (if binary) | |
| Positive rate | {pct}% |
| Mean (if continuous) | |
| Std (if continuous) | |
| Min / Max | |

**Temporal stability:** Is the target rate stable over time, or drifting?

**Relationship to suspected predictors:** (key correlations or cross-tabs)

---

## 5. Temporal Integrity Check

- [ ] Clear event timestamp column confirmed
- [ ] Data is orderable by time
- [ ] No future-dated records (event_date > today)
- [ ] `created_at` vs. `event_at` vs. `label_at` disambiguated
- [ ] No temporal leakage in any candidate feature (label happens after feature cutoff)

**Temporal integrity status:**

---

## 6. Leakage Risk Assessment

| Feature | Leakage type | Risk level | Mitigation |
|---------|-------------|-----------|-----------|
| | None | Low | |
| | Temporal | HIGH | Enforce cutoff date |
| | Label proxy | HIGH | Exclude |

**Leakage verdict:** CLEAN / ISSUES FOUND (resolve before Marco starts)

---

## 7. Sample Size Feasibility

**Minimum required per Eva's power analysis (if experiment):**

**Available sample size:** {N}

**After applying exclusion criteria:** {N}

**After applying quality filters:** {N}

**Feasibility verdict on sample size:** SUFFICIENT / BORDERLINE / INSUFFICIENT

---

## 8. Feasibility Verdict

**Overall verdict:**

- [ ] FEASIBLE — proceed to Phase 3
- [ ] FEASIBLE WITH CAVEATS — proceed with stated limitations (listed below)
- [ ] NOT FEASIBLE — redirect to Carla to revise MAB

**If feasible with caveats, list each caveat:**

1.
2.

**If not feasible, root cause:**

---

## Diego's Quality Gate

- [ ] All data sources inventoried; access confirmed for each
- [ ] Schema profiled for every key table
- [ ] Null rates, duplicates, and cardinality documented
- [ ] Target variable distribution analyzed
- [ ] Temporal integrity confirmed
- [ ] Leakage risk assessment complete
- [ ] Feasibility verdict stated clearly
- [ ] If caveats exist, stakeholder notified before proceeding
