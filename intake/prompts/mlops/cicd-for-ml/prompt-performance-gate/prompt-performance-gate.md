# Model Performance Gate *AI Prompt *

This prompt designs a deterministic model performance gate that decides whether a challenger can move forward based on holdout metrics, guardrails, fairness, and calibration. It is useful for reducing subjective promotion decisions in CI/CD workflows. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement a model performance gate that automatically approves or blocks model promotion based on predefined quality criteria.

1. Gate design principles:
 - Evaluate the challenger model against a fixed, versioned holdout dataset — never the training or validation set
 - The holdout dataset must represent the real-world distribution (not just historical data)
 - Gate must be deterministic: same model + same dataset must always produce the same pass/fail decision

2. Gate criteria — the challenger must pass ALL of these to be promoted:

 a. Absolute performance floor:
 - Primary metric (e.g. AUC) > {{min_auc}} — if below this, the model is too weak to ship regardless of improvement

 b. Relative improvement vs champion:
 - Primary metric improvement > {{min_improvement_pct}}% vs current production model
 - This prevents promoting a model that is technically better but not meaningfully so

 c. Guardrail metrics — must not degrade:
 - Secondary metrics (precision, recall, F1) must not degrade by more than {{max_guardrail_degradation}}%
 - Inference latency p99 must not increase by more than {{max_latency_increase_pct}}%

 d. Fairness check (if applicable):
 - Performance disparity across demographic groups must be within {{max_disparity_pct}}%

 e. Calibration check:
 - Expected Calibration Error (ECE) < {{max_ece}}

3. Gate output:
 - PASS: all criteria met → auto-promote to staging
 - CONDITIONAL PASS: improvement is positive but small → require human approval
 - FAIL: one or more criteria not met → block promotion, notify team with specific reason
 - Gate report: a structured JSON with all metric values, thresholds, and pass/fail per criterion

4. Gate versioning:
 - Version the gate criteria alongside the model — different model families may have different gates
 - Audit log: record every gate evaluation with model version, criteria version, and outcome

Return: gate evaluation code, gate criteria configuration (YAML), pass/fail report generator, and CI/CD integration. 
```

## When to use this prompt 
Use case 01 
when model promotion should be blocked automatically on quality failures 
Use case 02 
when challenger and champion models need deterministic comparison 
Use case 03 
when guardrail metrics, fairness, and calibration must be part of approval 
Use case 04 
when you need a reportable pass, conditional pass, or fail decision 

## What the AI should return 

A model gating system with evaluation code, YAML criteria, structured pass-fail reporting, and CI/CD integration. 

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

Once you have the first result, continue deeper with related prompts in CI/CD for ML.
