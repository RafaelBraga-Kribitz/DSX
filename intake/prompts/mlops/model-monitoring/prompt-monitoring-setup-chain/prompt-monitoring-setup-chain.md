# Monitoring Setup Chain *AI Prompt *

This chain prompt walks through end-to-end monitoring setup for a production model, from requirements and logging to baselines, drift checks, ground truth tracking, and runbook handoff. It is ideal when standing up a complete monitoring program rather than a single isolated component. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Define monitoring requirements — for this model, specify: what constitutes a healthy prediction distribution, the acceptable performance floor, the label availability timeline, and the business cost of undetected degradation vs false alarms.
Step 2: Instrument prediction logging — add async prediction logging to the serving layer. Log: request_id, model_version, features, prediction, confidence, latency. Verify logs are flowing to the storage layer.
Step 3: Establish baselines — compute reference distributions for all features and model outputs using the first 2 weeks of production data (or the validation set if launching new). Store baseline statistics.
Step 4: Deploy serving metrics — instrument Prometheus metrics (RPS, latency, error rate). Set up Grafana dashboard. Configure AlertManager rules for SLA violations.
Step 5: Deploy drift monitors — implement daily PSI checks for top features and prediction distribution. Set thresholds and alert routing. Run a backtest to validate alert sensitivity.
Step 6: Deploy performance tracking — implement ground truth join pipeline. Set up rolling performance metric computation. Define retraining trigger condition.
Step 7: Document and hand off — write the monitoring runbook: what each alert means, initial triage steps, escalation path, and how to silence a false alarm. Get sign-off from the on-call team before go-live. 
```

## When to use this prompt 
Use case 01 
when launching monitoring for a newly deployed model 
Use case 02 
when you want a step-by-step rollout from logging to retraining triggers 
Use case 03 
when multiple monitoring layers need to be sequenced in a practical order 
Use case 04 
when an on-call handoff and runbook are part of the deliverable 

## What the AI should return 

A staged monitoring implementation plan covering requirements, logging, serving metrics, drift monitoring, performance tracking, alerting, and operational handoff. 

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
