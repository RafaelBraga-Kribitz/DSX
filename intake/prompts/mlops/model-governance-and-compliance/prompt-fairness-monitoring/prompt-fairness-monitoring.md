# Fairness Monitoring *AI Prompt *

This prompt implements production fairness monitoring with disparity metrics, trend tracking, significance testing, alerting, and regulatory context. It is useful when fairness must be treated as an ongoing operational responsibility rather than a one-time evaluation. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement ongoing fairness monitoring for this production model.

Model: {{model_name}}
Sensitive attributes to monitor: {{sensitive_attributes}} (e.g. age_group, gender, region)
Fairness metric: {{fairness_metric}}

1. Fairness metrics — implement all of the following:

 a. Demographic parity (statistical parity):
 - Positive prediction rate should be equal across groups
 - Disparity = |P(ŷ=1 | group=A) - P(ŷ=1 | group=B)|
 - Alert threshold: disparity > {{dp_threshold}} (e.g. 0.05 = 5 percentage points)

 b. Equal opportunity:
 - True positive rate (recall) should be equal across groups
 - Requires ground truth labels
 - Disparity = |TPR_A - TPR_B|

 c. Predictive parity:
 - Precision (positive predictive value) should be equal across groups
 - Disparity = |Precision_A - Precision_B|

 d. Calibration by group:
 - Among predictions with score ~0.7, 70% should actually be positive, in every group
 - Plot calibration curves separately for each group

2. Monitoring implementation:
 - Compute all fairness metrics weekly on the last 4 weeks of labeled predictions
 - Track trends: is any metric getting worse over time?
 - Statistical significance: use bootstrap confidence intervals to determine if disparities are significant

3. Alerting:
 - Demographic parity disparity > {{dp_alert_threshold}}: Slack alert to model owner and legal/compliance team
 - Equal opportunity disparity > {{eo_alert_threshold}}: same alert
 - Fairness degradation trend: if any metric worsens for 3 consecutive weeks: escalate

4. Fairness-performance tradeoff:
 - Document the explicit tradeoff between overall performance and fairness
 - If improving fairness requires accepting a performance hit: this is a product and legal decision, not just a technical one

5. Regulatory context:
 - Flag which regulations apply to this model (ECOA, FCRA, EU AI Act, GDPR)
 - Document compliance status per regulation

Return: fairness metrics implementation, monitoring pipeline, alerting configuration, and regulatory compliance checklist. 
```

## When to use this prompt 
Use case 01 
when fairness metrics should be monitored continuously in production 
Use case 02 
when performance differences across sensitive groups need alerts and trends 
Use case 03 
when fairness and overall model performance must be considered together 
Use case 04 
when regulatory compliance needs to be tied to monitoring outputs 

## What the AI should return 

A fairness monitoring system with disparity metrics, weekly evaluation pipeline, alert configuration, and compliance-oriented reporting. 

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

Once you have the first result, continue deeper with related prompts in Model Governance and Compliance.
