# Drift Detection *AI Prompt *

This prompt detects whether the data or predictions seen in production have drifted away from the training environment. It is useful for model monitoring and retraining decisions after deployment. The analysis prioritizes drift in features that the model actually depends on most. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Detect whether this model's input data or predictions have drifted from the training distribution.

1. Feature drift (data drift): for each feature, compare the training distribution to the current serving distribution using:
 - Kolmogorov-Smirnov test for continuous features
 - Chi-squared test for categorical features
 - Population Stability Index (PSI) for all features
2. Flag features with PSI > 0.2 (significant drift) or PSI 0.1–0.2 (moderate drift)
3. Prediction drift: compare the distribution of model outputs in training vs serving. Has the prediction distribution shifted?
4. Concept drift (if labels are available): compare model performance in recent data vs training data. Has accuracy degraded?
5. Prioritize: which drifting features are most important to the model (high SHAP importance)? These pose the greatest risk.

Return: drift report table per feature, PSI heatmap, and a retraining recommendation: retrain now / monitor / no action needed. 
```

## When to use this prompt 
Use case 01 
A model is in production or being monitored post-training. 
Use case 02 
You suspect feature distribution or prediction behavior has shifted. 
Use case 03 
You want statistical drift tests plus PSI-based thresholds. 
Use case 04 
You need a practical retraining recommendation, not just raw diagnostics. 

## What the AI should return 

A per-feature drift report with tests and PSI values, prediction-drift summary, optional concept-drift check if labels exist, prioritized risk assessment based on feature importance, and a retrain/monitor/no-action recommendation. 

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

Once you have the first result, continue deeper with related prompts in Model Evaluation.
