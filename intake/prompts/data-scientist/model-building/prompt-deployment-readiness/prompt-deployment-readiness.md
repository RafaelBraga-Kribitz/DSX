# Model Deployment Readiness *AI Prompt *

This prompt evaluates whether a trained model is operationally ready, not just statistically strong. It is useful right before deployment when latency, memory, robustness, reproducibility, and monitoring all matter. The result should support a go/no-go launch decision. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Assess whether this model is ready for production deployment.

Run the following checks and report pass / fail / needs review for each:

1. Performance: does the model meet the minimum performance threshold of {{performance_threshold}} on the test set?
2. Latency: can the model produce a single prediction in under {{latency_ms}}ms? Test with 1000 sequential predictions.
3. Memory: what is the model's memory footprint in MB? Is it within the deployment limit of {{memory_limit_mb}}MB?
4. Robustness: does performance degrade by more than 5% when tested on data from the last month vs the training period?
5. Edge cases: test with 10 adversarial inputs (nulls, extreme values, empty strings). Does the model throw errors or return sensible predictions?
6. Reproducibility: given the same inputs, does the model return identical outputs on repeated calls?
7. Monitoring plan: are feature drift and prediction drift monitors in place? Is there an alert for performance degradation?

Return: deployment readiness checklist and a go/no-go recommendation. 
```

## When to use this prompt 
Use case 01 
A model is nearing production deployment. 
Use case 02 
You need operational checks alongside predictive performance. 
Use case 03 
Latency, memory footprint, and edge-case handling matter in the serving environment. 
Use case 04 
You need a concise readiness checklist for stakeholders. 

## What the AI should return 

A deployment readiness checklist with pass/fail/needs-review status for each criterion, findings on performance and operational constraints, and a clear go/no-go recommendation. 

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

Once you have the first result, continue deeper with related prompts in Model Building.
