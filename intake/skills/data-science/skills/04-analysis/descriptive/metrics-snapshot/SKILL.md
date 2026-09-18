---
name: ds-skill--metrics-snapshot
description: >
  Rapid metrics summary for any business question. Answers "how are we doing?"
  with primary KPI + 3-5 supporting metrics, comparison baseline, and
  a 1-sentence business verdict. Completes in <30 min.
tags: [skill, descriptive, metrics, kpi, snapshot]
---

# Metrics Snapshot

## When to Use
- Weekly/monthly business review
- Quick status check on a KPI
- Before a stakeholder meeting
- First step in any descriptive analysis

## Protocol

### Step 1: Identify Metrics
For the given business context, select:

| Layer | What | Example |
|-------|------|---------|
| North Star | Company-level health | MAU, GMV, NPS |
| Primary KPI | Question-specific | Conversion rate, Churn rate |
| Supporting (2-3) | Explain the KPI | Visits, ATC rate, AOV |
| Guardrail (1-2) | Can't get worse | Error rate, LTV |

### Step 2: Choose Comparison Baseline
Pick the most meaningful comparison (not all of them):

| Context | Best comparison |
|---------|----------------|
| Cyclical business | Same period last year (YoY) |
| Fast-moving product | Last week (WoW) |
| Target-driven team | vs Plan/Budget |
| Competitive market | vs Benchmark |
| Long tail | vs 90th percentile |

### Step 3: Compute with Context
```
Format each metric as:
  [Metric name]: [Value] ([+/-X%] vs [baseline], [direction emoji])
  
Example:
  Conversion Rate: 3.2% (+0.4pp vs last week 🟢)
  Revenue: €142K (-8% vs last month 🔴)
  AOV: €89 (+3% vs last month 🟢)
```

### Step 4: Write the Verdict
One sentence. Business language. No jargon.
```
Format: "[Period] was [above/below/on track] — [metric] [direction] 
         driven by [top 1 factor], partially offset by [top 2 factor]."
         
Example: "October was below plan — revenue fell 8% driven by conversion 
          rate decline in mobile, partially offset by higher AOV."
```

## Output Template
```markdown
## Metrics Snapshot: [Entity] — [Period]

**Verdict:** [1-sentence business summary]

| Metric | Value | vs [Baseline] | Status |
|--------|-------|---------------|--------|
| [KPI 1] | [value] | [+/-X%] | 🟢🟡🔴 |
| [KPI 2] | [value] | [+/-X%] | 🟢🟡🔴 |
| [KPI 3] | [value] | [+/-X%] | 🟢🟡🔴 |

**Key driver:** [1 sentence on what moved the number]
**Watch:** [1 metric that needs attention]

*Period: [dates] | Source: [data source] | As of: [data freshness]*
```

## Status Thresholds (default, adjust to business)
- 🟢 Within ±5% of target or better
- 🟡 5-15% below target
- 🔴 >15% below target or guardrail violated
