# Data Drift vs Concept Drift *AI Prompt *

This prompt explains the major kinds of drift and connects each one to detection and response strategies. It is useful when a team needs both conceptual clarity and implementation guidance for diagnosing why model quality is changing. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Explain and implement detection methods for the different types of drift this model may experience.

1. Definitions with examples:

 Data drift (covariate shift): P(X) changes, P(Y|X) stays the same
 - Input feature distributions change, but the relationship between features and target is unchanged
 - Example: your fraud model was trained on 2023 data. In 2024, transaction amounts increased due to inflation. The fraud patterns are the same, but the feature distributions shifted.
 - Detection: monitor feature distributions (PSI, KS test)
 - Impact: model may make more errors on out-of-distribution inputs

 Concept drift: P(Y|X) changes, P(X) may stay the same
 - The underlying relationship between features and target changes
 - Example: consumer behavior changed post-COVID. Features that predicted churn in 2019 no longer predict churn in 2023.
 - Detection: requires ground truth labels — monitor model performance over time
 - Impact: model becomes fundamentally wrong, not just uncertain

 Label drift: P(Y) changes
 - The prevalence of the target class changes
 - Example: fraud rate drops from 2% to 0.5% due to a new prevention system
 - Detection: monitor positive prediction rate and, when available, actual label rate
 - Impact: model calibration becomes off, decision threshold may need adjustment

 Prior probability shift: combination of covariate and label drift

2. Detection implementation for each type:
 - Data drift: daily PSI on all features
 - Concept drift: rolling model performance on labeled data (AUC, precision, recall)
 - Label drift: daily positive rate monitoring with statistical significance test

3. Diagnosis flowchart:
 - Performance degrading + feature drift detected → likely data drift
 - Performance degrading + no feature drift → likely concept drift
 - Calibration off + positive rate changed → likely label drift
 - All metrics stable + business impact → investigate downstream factors

4. Response strategy per drift type:
 - Data drift: retrain on recent data, update preprocessing normalization parameters
 - Concept drift: retrain with new data, potentially redesign features
 - Label drift: recalibrate the model, adjust decision threshold

Return: drift type detection implementation, diagnosis flowchart, and response playbook per type. 
```

## When to use this prompt 
Use case 01 
when you need to distinguish data drift from concept drift and label drift 
Use case 02 
when designing a drift diagnosis workflow for production models 
Use case 03 
when response actions should vary by the type of drift detected 
Use case 04 
when you want code guidance plus a practical decision flow 

## What the AI should return 

A drift diagnosis package covering definitions, detection methods, a diagnosis flowchart, and response playbooks for each drift type. 

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
