# Concept Drift Localization *AI Prompt *

This prompt localizes concept drift by estimating when it started, which features changed, and which user segments are most affected. It is designed for post-detection investigation and root cause analysis rather than first-pass monitoring. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
When concept drift is detected, implement methods to localize where and when the drift occurred.

Concept drift has been confirmed (performance degradation with available labels). Now identify the specifics.

1. Temporal localization — when did the drift start?:
 - Use CUSUM (Cumulative Sum) change point detection on the rolling performance metric
 - Alternatively: Page-Hinkley test for online change point detection
 - Binary search approach: is performance worse in the last week vs the week before? If yes, recurse into the worse half.
 - Report the estimated change point date with a confidence interval

2. Feature-space localization — what changed?:
 - If labels are available: train a model to predict where errors occur
 - Features that predict model errors are candidates for concept drift
 - Compare SHAP values from the original model on recent data vs reference data
 - Features with the largest SHAP distribution shift are likely driving the concept drift

3. Segment localization — which user segments are most affected?:
 - Compute performance metrics separately for each dimension (region, device, user_type, price_tier)
 - Rank segments by performance degradation: which segment shows the largest drop?
 - Check if the worst-performing segment has grown in volume (could amplify overall degradation)

4. Root cause hypothesis:
 Based on localization results, form hypotheses:
 - Temporal drift on specific date → check for: product change, external event, data pipeline issue
 - Feature-driven drift → check for: upstream data source change, feature engineering bug, new user behavior
 - Segment-driven drift → check for: new customer segment entered the product, regional regulation change

5. Remediation options:
 - Retrain on recent data (weights recent data more heavily)
 - Targeted retraining: only retrain on the drifted segment
 - Feature replacement: if a feature is no longer predictive, replace it
 - Model architecture change: if the relationship structure has fundamentally changed

Return: CUSUM change point detection, feature importance drift analysis, segment performance comparison, and root cause hypothesis framework. 
```

## When to use this prompt 
Use case 01 
when concept drift has already been detected and needs deeper investigation 
Use case 02 
when you need change-point analysis on model performance 
Use case 03 
when segment-level degradation may explain overall performance decline 
Use case 04 
when remediation depends on understanding where drift is concentrated 

## What the AI should return 

A concept drift investigation package with temporal localization, feature-space analysis, segment comparison, and a root-cause hypothesis framework. 

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
