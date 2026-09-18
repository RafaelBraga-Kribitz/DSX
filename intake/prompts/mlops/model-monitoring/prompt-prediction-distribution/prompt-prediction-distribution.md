# Prediction Distribution Monitor *AI Prompt *

This prompt monitors how prediction outputs change over time, using baseline statistics, daily comparisons, segment analysis, and alert thresholds. It is designed to catch output drift early, especially when the model's predictions may shift before labels reveal a quality problem. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a system to monitor the distribution of model predictions over time and detect output drift.

Model type: {{model_type}} (binary classifier / multiclass / regression / ranking)

1. Baseline distribution:
 - Compute the prediction distribution on a held-out reference dataset (or first 2 weeks of production logs)
 - For classifiers: positive rate, score distribution (histogram with 20 bins), confusion matrix on labeled data
 - For regression: mean, std, percentiles (5th, 25th, 50th, 75th, 95th), histogram
 - Store baseline statistics in a metadata table for comparison

2. Daily distribution comparison:
 - Compute the same statistics on the last 24 hours of predictions
 - Statistical tests:
 - Classifier scores: Kolmogorov-Smirnov test (KS test) vs baseline distribution
 - Classifier positive rate: two-proportion z-test vs baseline positive rate
 - Regression outputs: KS test + t-test for mean shift
 - Population Stability Index (PSI):
 - PSI < 0.1: no significant shift
 - PSI 0.1–0.2: moderate shift — investigate
 - PSI > 0.2: significant shift — alert

3. Temporal patterns:
 - Plot rolling 7-day mean prediction score over time
 - Plot rolling positive rate (for classifiers) over time
 - Flag: sudden jumps (step change) vs gradual drift (slow trend)
 - Annotate with model deployment dates to distinguish drift from deployment effects

4. Segment-level monitoring:
 - Compute prediction distribution separately for key segments (region, user type, device)
 - Flag any segment where distribution diverges significantly from the population

5. Alerting:
 - PSI > 0.2 on overall prediction distribution: Slack alert to ML team (P2)
 - Positive rate changes > 2× std from 30-day rolling average: Slack alert (P2)
 - Positive rate changes > 5× std: PagerDuty (P1) — likely a model or feature pipeline failure

Return: baseline computation script, daily comparison script, PSI calculation function, and alerting configuration. 
```

## When to use this prompt 
Use case 01 
when you need to track prediction drift in production 
Use case 02 
when comparing current model outputs to a reference distribution 
Use case 03 
when segment-level prediction behavior may hide issues in the aggregate 
Use case 04 
when you want scripts for baselining, daily comparison, PSI, and alerting 

## What the AI should return 

A prediction distribution monitoring setup with baseline creation, daily drift checks, PSI and statistical tests, temporal plots, and alert rules. 

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
