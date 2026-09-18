# Feature Drift Detection *AI Prompt *

This prompt implements feature drift monitoring with reference statistics, daily statistical tests, prioritized alerts, and visualizations. It is a practical choice when an ML team wants interpretable drift checks on the most important input features. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement feature drift detection to identify when the distribution of input features shifts from the training distribution.

Model: {{model_name}}
Top features to monitor: {{top_features}} (recommend top 10–20 by model importance)

1. Reference distribution (computed once from training or first 2 weeks of production):
 - Numeric features: mean, std, min, max, and histogram with 20 fixed bins
 - Categorical features: value frequency distribution
 - Store reference statistics in a metadata table

2. Statistical tests for drift detection (run daily on last 24h of production data):

 For numeric features:
 - Kolmogorov-Smirnov (KS) test: sensitive to distribution shape changes
 - Population Stability Index (PSI): standard industry metric, interpretable thresholds
 - Wasserstein distance (Earth Mover's Distance): good for detecting small but systematic shifts

 For categorical features:
 - Chi-squared test: tests if observed frequencies match expected frequencies
 - PSI on each category's frequency
 - Jensen-Shannon divergence: symmetric, bounded [0,1], good for comparing distributions

3. PSI interpretation and thresholds:
 - PSI < 0.1: no significant drift → continue
 - PSI 0.1–0.2: moderate drift → log warning, increase monitoring frequency
 - PSI > 0.2: significant drift → alert ML team, evaluate for retraining
 - PSI > 0.5: severe drift → escalate, consider emergency rollback investigation

4. Prioritized alerting:
 - Weight drift severity by feature importance: drift in a top-5 feature is more critical than drift in a low-importance feature
 - Composite drift score: weighted average of PSI scores across all monitored features

5. Visualization:
 - Side-by-side histogram: reference vs current distribution for each drifting feature
 - Drift heatmap: features × time with PSI color coding (green/yellow/red)

Return: reference statistics computation, daily drift detection script, PSI calculation, composite score, and visualization code. 
```

## When to use this prompt 
Use case 01 
when you need daily monitoring of feature distribution changes 
Use case 02 
when top model features should drive drift severity and alerting 
Use case 03 
when PSI, KS, and related tests are needed for production monitoring 
Use case 04 
when you want both scripts and visual drift diagnostics 

## What the AI should return 

A feature drift monitoring solution with reference statistics, daily detection jobs, PSI and other tests, composite drift scoring, and visualization code. 

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
