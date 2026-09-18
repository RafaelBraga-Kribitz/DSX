# Lag and Rolling Features *AI Prompt *

This prompt builds historical lag and rolling statistics for panel or time series data without leaking future information. It is meant for forecasting, churn, risk, and behavioral models where recent history is often the strongest signal. The structure keeps everything grouped by entity and aligned to prediction time. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Create lag and rolling window features for this time-ordered dataset.

Assume the data is ordered by {{date_column}} with one row per {{entity_column}} per time period.

Create per entity:
- Lag features: value at t-1, t-2, t-3, t-7, t-14, t-28 periods back
- Rolling mean: 7-period, 14-period, 28-period window
- Rolling standard deviation: 7-period and 28-period window
- Rolling min and max: 7-period window
- Exponentially weighted moving average (alpha=0.3)
- Trend: slope of a linear regression fitted on the last 7 values

Critical: ensure no data leakage — all features must use only information available at prediction time (strictly historical).

Return the feature creation code and confirm the leakage-free construction. 
```

## When to use this prompt 
Use case 01 
Your rows are ordered by time and tied to entities such as users, stores, or products. 
Use case 02 
You want classic time-aware features like lags, rolling averages, and trends. 
Use case 03 
Leakage prevention is critical because future values must never influence past predictions. 
Use case 04 
You need reusable pandas code for a forecasting or panel-data pipeline. 

## What the AI should return 

Leakage-free feature engineering code for lags, rolling windows, EWMA, and trend features, along with a short explanation confirming that all features use strictly historical information only. 

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

Once you have the first result, continue deeper with related prompts in Feature Engineering.
