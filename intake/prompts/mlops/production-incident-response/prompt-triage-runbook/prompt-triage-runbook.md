# Triage Runbook *AI Prompt *

This prompt writes a practical triage runbook that any on-call engineer can execute quickly, even without deep model context. It is useful for turning incident response from tribal knowledge into a repeatable first-response procedure. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write a model incident triage runbook for on-call engineers who may not be deeply familiar with the specific model.

Model: {{model_name}}
Serving infrastructure: {{infrastructure}}

The runbook must be executable by any on-call engineer within 15 minutes of being paged.

1. Initial triage (first 5 minutes):
 - Is this a model issue or an infrastructure issue?
 Check 1: Are the Kubernetes pods healthy? (kubectl get pods -n {{namespace}})
 Check 2: Is the serving endpoint returning any responses? (curl -X POST {{health_endpoint}})
 Check 3: Are the upstream feature pipelines healthy? (link to pipeline dashboard)
 Check 4: Was there a recent deployment? (check deployment log at {{deploy_log_link}})

2. Model-specific diagnostics (minutes 5–10):
 - Check serving dashboard: error rate, latency, prediction distribution (link: {{dashboard_link}})
 - Check feature drift dashboard: any features showing high PSI? (link: {{drift_dashboard_link}})
 - Check model version currently serving: what model version is in production? Expected: {{expected_version}}
 - Sample 10 recent predictions: do the inputs and outputs look sane? (query: {{sample_query}})

3. Common failure modes and immediate actions:
 - High error rate → Check logs for error type. If OOM: restart pods. If model file missing: check object storage.
 - High latency → Check GPU utilization. If GPU saturated: scale up pods. If CPU-bound: check for preprocessing bottleneck.
 - Wrong predictions → Check model version. If unexpected version: trigger rollback. Check feature pipeline for data quality issues.
 - All predictions same class → Model likely receiving all-null or all-default features. Check feature pipeline.

4. Rollback procedure:
 - Command: {{rollback_command}}
 - Expected output: {{expected_rollback_output}}
 - Verification: wait 2 minutes, then confirm error rate has returned to baseline

5. Escalation:
 - If unresolved in 30 minutes: page {{escalation_contact}}
 - If data pipeline issue: page {{data_team_contact}}
 - If model quality issue: page {{ml_team_contact}}

Return: complete triage runbook formatted as a step-by-step guide. 
```

## When to use this prompt 
Use case 01 
when on-call engineers need a step-by-step diagnostic guide 
Use case 02 
when model, infrastructure, and data-pipeline failures must be separated quickly 
Use case 03 
when rollback instructions and escalation paths need to be explicit 
Use case 04 
when first-response actions should fit into a 15-minute triage window 

## What the AI should return 

A step-by-step incident triage runbook with checks, diagnostics, immediate actions, rollback steps, and escalation guidance. 

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

Once you have the first result, continue deeper with related prompts in Production Incident Response.
