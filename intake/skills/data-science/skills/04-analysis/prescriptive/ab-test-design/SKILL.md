---
name: ds-skill--ab-test-design
description: >
  Pre-launch A/B test design. Defines hypothesis, primary metric, guardrails,
  randomization unit, sample size via power analysis, and stop rules.
  Output is a test spec that must be approved before data collection starts.
tags: [skill, experiment, ab-test, power-analysis, design]
---

# A/B Test Design

## When to Use
- You want to measure the causal impact of a product/marketing change
- Before starting any experiment — design first, collect second

## Design Protocol

### 1. Hypothesis
```
H₀ (null):      [Treatment] has no effect on [primary metric]
H₁ (alternative): [Treatment] increases [primary metric] by at least [MDE]%
```
MDE = Minimum Detectable Effect — smallest change that's practically meaningful.

### 2. Metrics
**Primary metric** (one only — what the test is optimized for):
- Must be measurable at the randomization unit level
- Must be sensitive enough to change within the test window

**Guardrail metrics** (must NOT get worse):
- Latency / error rate (technical guardrails)
- Key downstream metrics (e.g., LTV, D7 retention if primary is CTR)
- Revenue (if primary is engagement)

### 3. Randomization Unit
| Unit | When to use | Risk |
|------|-------------|------|
| User (recommended) | Nearly always | Network effects if users interact |
| Session | Never for user-state features | Novelty effect, inconsistency |
| Page view | Never | Severe imbalance, user sees both |

### 4. Power Analysis
```
Required inputs:
  α = 0.05 (Type I error — false positive rate)
  β = 0.80 (Power — 1 - Type II error rate)
  baseline_rate = [current metric value]
  MDE = [minimum % lift that matters]

Output: minimum users per variant

Formula (proportion):
  n = 2 × (z_α/2 + z_β)² × p(1-p) / MDE²
  
Use scipy.stats or online calculator to compute.
```

### 5. Timeline
```
Test duration = required_n / (daily_traffic / num_variants)
Minimum duration: 1 full week (to capture weekly seasonality)
Maximum duration: 4 weeks (novelty effect dissipates after 2-4w)
```

### 6. Stop Rules
**Option A — Fixed horizon (recommended for most teams)**
- Run for exactly N days (from power analysis)
- Do NOT peek and stop early based on results
- If you must peek: use Bonferroni correction on alpha

**Option B — Sequential testing (advanced)**
- Use alpha spending function (O'Brien-Fleming boundary)
- Allows early stopping with controlled Type I error
- Use: scipy or statsmodels sequential tests

### 7. Assignment & Logging
- Confirm assignment is truly random (hash user_id modulo n)
- Log assignment event with timestamp
- Verify assignment balance before launch (expected ±5% of 50/50)

## Test Spec Output
```yaml
test_name: <descriptive name>
hypothesis:
  h0: "No effect on [metric]"
  h1: "[Treatment] increases [metric] by ≥ [MDE]%"
primary_metric: <metric name + calculation>
guardrail_metrics:
  - <metric 1: threshold>
  - <metric 2: threshold>
randomization_unit: user
variants:
  control: <description>
  treatment: <description>
power_analysis:
  alpha: 0.05
  power: 0.80
  baseline: <current metric value>
  mde: <minimum detectable effect %>
  required_n_per_variant: <n>
  estimated_duration_days: <d>
stop_rules: fixed_horizon | sequential
start_date: <planned>
end_date: <planned>
owner: <name>
decision_criteria: >
  Ship if: primary metric significant (p<0.05), guardrails OK, practical effect ≥ MDE
  Rollback if: any guardrail violated
  Iterate if: inconclusive or effect < MDE
```
