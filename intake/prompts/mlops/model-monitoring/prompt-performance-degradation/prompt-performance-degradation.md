# Model Performance Degradation Alert *AI Prompt *

This prompt designs an early warning system for model degradation using proxy signals such as confidence shifts, entropy, anomaly rate, and business metrics. It is intended for situations where labels arrive too late to rely on direct performance monitoring alone. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build an early warning system for model performance degradation before ground truth labels arrive.

Since labels often arrive days or weeks after predictions, rely on proxy signals that correlate with model quality.

1. Proxy signal monitoring (no labels required):

 a. Confidence score degradation:
 - Track the distribution of model confidence scores daily
 - A well-calibrated model should have a stable confidence distribution
 - Alert if mean confidence drops > {{confidence_drop_threshold}} or if the distribution becomes more uniform (model is less certain)

 b. Prediction entropy (for classifiers):
 - Entropy = -Σ p_i × log(p_i) across classes
 - Higher entropy = less confident predictions
 - Alert if rolling 7-day mean entropy increases > 1σ above the baseline mean entropy

 c. Feature anomaly rate:
 - Track the % of incoming requests where at least one feature falls outside the training distribution
 - A rising anomaly rate predicts performance degradation before it appears in labels

 d. Business metric correlation (if available):
 - Track downstream business metrics that the model influences (conversion rate, fraud rate)
 - Unexplained movements in business metrics may indicate model degradation

2. Composite degradation score:
 - Combine multiple proxy signals into a single degradation score (0–100)
 - Weight by historical correlation with actual performance drops
 - Thresholds: score > 60 → Slack alert, score > 80 → PagerDuty

3. Alert content:
 - Current degradation score and contributing signals
 - Trend: is degradation accelerating or stable?
 - Recommended action: monitor / investigate / retrain
 - Link to monitoring dashboard and recent prediction sample for manual inspection

4. Validation:
 - Backtest the proxy signals on historical data: did they predict known past degradation events?
 - Report: lead time before degradation became visible in labels, false positive rate

Return: proxy signal monitoring code, composite score calculation, alerting logic, and backtest methodology. 
```

## When to use this prompt 
Use case 01 
when you need degradation alerts before ground truth is available 
Use case 02 
when proxy signals may reveal model quality issues earlier than labels 
Use case 03 
when you want a composite risk score from multiple monitoring signals 
Use case 04 
when you need backtesting to validate early-warning indicators 

## What the AI should return 

An early warning design with proxy signal monitors, composite degradation scoring, alert logic, and a methodology for historical validation. 

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

Once you have the first result, continue deeper with related prompts in Model Monitoring.
