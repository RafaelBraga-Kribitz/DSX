# Model Audit Chain *AI Prompt *

This prompt audits a model across multiple trust dimensions instead of reporting only aggregate accuracy. It is designed for higher-stakes reviews where robustness, subgroup behavior, fairness, and leakage all matter. The result should function as a structured technical risk assessment. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Performance audit — evaluate on test set using all relevant metrics. Compare to baseline. Does the model meet the business performance threshold?
Step 2: Robustness audit — test performance on subgroups (by region, time period, user segment, etc.). Does performance degrade significantly for any group?
Step 3: Fairness audit — if sensitive attributes exist (age, gender, geography), check for disparate impact: does the false positive rate or false negative rate differ significantly across groups?
Step 4: Stability audit — add small amounts of Gaussian noise to input features and measure performance degradation. Is the model brittle to small input changes?
Step 5: Leakage audit — inspect the top 10 most important features. Do any of them look like they might encode the target or use future information?
Step 6: Write a model audit report: pass/fail for each audit, severity of any failures, and recommended mitigations. 
```

## When to use this prompt 
Use case 01 
A model is nearing production or formal review. 
Use case 02 
You need subgroup, fairness, and stability checks in one process. 
Use case 03 
The model may affect sensitive populations or critical decisions. 
Use case 04 
You want a pass/fail audit framework with mitigation ideas. 

## What the AI should return 

A structured audit report covering performance, robustness, fairness, stability, and leakage, with pass/fail status, severity of issues found, and recommended mitigations. 

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
