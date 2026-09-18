# Drift Root Cause Report *AI Prompt *

This prompt produces a structured report after drift has been detected, combining severity, scope, onset, likely causes, business impact, and recommended actions. It is useful for communicating drift investigations to technical and non-technical stakeholders. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Generate a structured drift root cause report when drift has been detected in this model.

Drift detected: {{drift_description}}
Model: {{model_name}}
Detection date: {{detection_date}}

The report should contain:

1. Executive summary (3 sentences):
 - What was detected, when, and how severe?
 - What is the estimated business impact if unaddressed?
 - What is the recommended immediate action?

2. Drift characterization:
 - Type: data drift / concept drift / label drift / combined
 - Severity: PSI scores, AUC degradation, or performance metric change
 - Onset: estimated date when drift began (from change point detection)
 - Scope: which features are most affected? Which user segments?
 - Trajectory: is the drift stable, accelerating, or decelerating?

3. Root cause investigation:
 - Timeline of events: deployments, data pipeline changes, external events near the drift onset date
 - Feature analysis: top 5 drifting features with their PSI scores and distribution visualizations
 - Upstream data quality: any anomalies in the data pipeline feeding this model?
 - External context: market events, seasonality, product changes that could explain the drift?

4. Impact assessment:
 - Estimated accuracy degradation: current performance vs baseline
 - Affected prediction volume: how many predictions per day are impacted?
 - Downstream business impact: estimated revenue, risk, or operational impact

5. Recommended actions (prioritized):
 - Immediate (< 24 hours): quick mitigations to limit damage
 - Short-term (< 1 week): retraining, threshold adjustment, feature fixes
 - Long-term (< 1 month): systematic fixes to prevent recurrence

6. Monitoring update:
 - What new tests or tighter thresholds should be added to catch this pattern earlier next time?

Return: complete drift root cause report template with all sections filled based on available data. 
```

## When to use this prompt 
Use case 01 
when drift has been confirmed and needs formal documentation 
Use case 02 
when stakeholders need severity, business impact, and action priorities in one report 
Use case 03 
when a consistent root-cause report format is needed across incidents 
Use case 04 
when investigation findings must be translated into next steps 

## What the AI should return 

A completed drift root cause report with executive summary, characterization, investigation findings, impact assessment, and prioritized actions. 

## How to use this prompt 
1 
### Open your data context 

Load your dataset, notebook, or working environment so the AI can operate on the actual project context. 
2 
### Copy the prompt text 

Use the copy button above and paste the prompt into the AI assistant or prompt input area. 
3 
### Review the output critically 

Check whether the result matches your data, assumptions, and desired format before moving on. 
4 
### Chain into the next prompt 

Once you have the first result, continue deeper with related prompts in Drift Detection.
