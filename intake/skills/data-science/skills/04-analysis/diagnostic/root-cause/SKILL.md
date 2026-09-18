---
name: ds-skill--root-cause-analysis
description: >
  Structured root cause investigation for metric drops or spikes.
  Run when a business metric changed and the cause is unknown.
  Uses decomposition + segment attribution. Outputs ranked hypotheses.
tags: [skill, diagnostic, root-cause, attribution]
---

# Root Cause Analysis

## When to Use
- A metric dropped or spiked unexpectedly
- You need to explain *why* a KPI changed, not just *that* it changed
- Before recommending a fix

## Protocol (4-step)

### Step 1: Characterize the Change
```
- What metric? What period? What magnitude?
- When exactly did it start? (pinpoint the inflection point)
- Is it sustained or a spike?
- Is it in one geography/segment or broad?
```

### Step 2: Decompose the Metric
Break the metric into its component parts.

**Example: Revenue drop**
```
Revenue = Users × Conversion Rate × Average Order Value
→ Which component changed?
→ Decompose each component one level deeper
```

**Example: DAU drop**
```
DAU = New users + Retained users
    = (New installs × D0 activation rate) + (D1/D7/D30 retention × prior DAU)
→ Which flow changed?
```

### Step 3: Segment Attribution
For the component that changed, break by:
- **Internal segments:** platform (iOS/Android/web), geography, user tier,
  acquisition channel, product feature, plan type
- **External factors:** day-of-week, seasonality, holiday, competitor event,
  marketing campaign start/stop

**Attribution rule:** The segment(s) that drove the change must sum to the
total change. Use waterfall decomposition.

### Step 4: Rank Hypotheses
```
For each candidate cause:
  - Evidence for: <what data supports this>
  - Evidence against: <what data contradicts this>
  - Estimated share of change: <X%>
  - Testability: <how would we confirm this>

Rank by: evidence strength × magnitude of contribution
```

## Output Template
```markdown
## Root Cause Analysis: [Metric] [Direction] on [Date]

**Change:** [Metric] declined by X% from [baseline] to [current]
**Period:** [Start] to [End]

### Decomposition
| Component | Before | After | Change | % of Total Change |
|-----------|--------|-------|--------|------------------|
| [Component A] | | | | |
| [Component B] | | | | |

### Primary Cause (most likely)
**[Hypothesis 1]** — accounts for ~X% of the change
Evidence: [supporting data]
Confidence: high / medium / low

### Secondary Causes
**[Hypothesis 2]** — accounts for ~Y%
**[Hypothesis 3]** — accounts for ~Z%

### Ruled Out
- [Hypothesis X]: data shows [contradicting evidence]

### Recommended Next Step
[Specific action to confirm primary hypothesis or remediate]
```

## Caveats to Always Include
- "This is observational — we are identifying correlation, not proven causation"
- Confounders checked: [list]
- Confidence: [high/medium/low] based on evidence quality
