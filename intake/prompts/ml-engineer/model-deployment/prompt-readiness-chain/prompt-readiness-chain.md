# Deployment Readiness Chain *AI Prompt *

This chain assesses whether a model service is truly ready for production by verifying model outputs, API behavior, load performance, rollback readiness, monitoring, runbooks, and sign-off gates. It is meant to reduce surprises during launch. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Model validation — run the model on a fixed golden dataset and assert outputs match expected values to ±1e-5. Confirm model size, latency on target hardware (p50/p95/p99), and memory footprint meet requirements.
Step 2: API contract verification — test all endpoints with valid inputs, invalid inputs, edge cases (empty batch, max size batch), and concurrent requests. Verify error codes and messages match the API spec.
Step 3: Load testing — run a 5-minute load test at 2× expected peak traffic using Locust or k6. Confirm p99 latency stays within SLA, error rate < 0.1%, and no memory leaks (memory usage stable).
Step 4: Rollback plan — document the exact steps to roll back to the previous model version within 5 minutes. Verify the rollback procedure works in staging before deploying to production.
Step 5: Monitoring setup — confirm all dashboards are in place: request rate, error rate, p50/p95/p99 latency, prediction distribution, feature drift, and GPU/CPU utilization. Verify alerts are firing correctly.
Step 6: Runbook — write a deployment runbook covering: deployment steps, expected log messages, how to verify success, known issues and their fixes, and escalation path if something goes wrong.
Step 7: Go / no-go checklist — create a final checklist with sign-off required from: ML engineer (model quality), SRE (infrastructure), and product (business metrics). Block deployment until all sign off. 
```

## When to use this prompt 
Use case 01 
when preparing a model or API for production release 
Use case 02 
when load testing, rollback validation, and monitoring checks are mandatory 
Use case 03 
when teams need a deployment runbook and formal go or no-go criteria 
Use case 04 
when multiple stakeholders must sign off before launch 

## What the AI should return 

A deployment readiness checklist and action plan covering validation, API contract testing, load testing, rollback, monitoring, runbooks, and final sign-off. 

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

Once you have the first result, continue deeper with related prompts in Model Deployment.
