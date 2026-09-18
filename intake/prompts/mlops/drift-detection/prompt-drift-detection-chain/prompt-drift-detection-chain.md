# Drift Detection Setup Chain *AI Prompt *

This chain prompt lays out a full drift detection program, from feature ranking and baselines to univariate and multivariate monitors, concept drift tracking, alert routing, and runbooks. It is useful when building a comprehensive drift detection stack from scratch. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Feature importance ranking — use SHAP values from the production model to rank all features by their average impact on predictions. These are the features where drift matters most.
Step 2: Reference distribution computation — compute reference statistics (mean, std, histogram, PSI bins) for the top 20 features and the prediction output on the training validation set. Store in a metadata table.
Step 3: Univariate drift monitors — implement daily PSI checks for all top-20 features and the prediction distribution. Set alert thresholds: PSI > 0.1 warning, PSI > 0.2 alert. Test with synthetic drift to validate sensitivity.
Step 4: Multivariate drift monitor — implement classifier-based multivariate drift detection running weekly. Validate that it detects joint distribution shifts that the univariate monitors miss.
Step 5: Concept drift monitor — implement rolling performance tracking using the ground truth feedback loop. Set retraining trigger: performance drops below {{threshold}} for {{n}} consecutive days.
Step 6: Alerting and routing — configure alert routing: feature drift → Slack to ML team, prediction drift → Slack + email, performance drift → PagerDuty. Test all alert paths end-to-end.
Step 7: Runbook — document for each alert: what it means, first 3 investigation steps, escalation path, and how to silence a false alarm. Conduct a fire drill with the on-call team. 
```

## When to use this prompt 
Use case 01 
when setting up a complete drift monitoring capability 
Use case 02 
when both feature drift and concept drift need coverage 
Use case 03 
when alert routing and runbooks should be designed alongside detectors 
Use case 04 
when you want an ordered implementation plan rather than isolated checks 

## What the AI should return 

A full drift detection rollout plan covering baselines, detectors, performance monitoring, alerting, and operational documentation. 

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
