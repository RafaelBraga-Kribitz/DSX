# Model Incident Response *AI Prompt *

This prompt creates a production model incident response playbook with severity levels, alerting chains, triage steps, rollback criteria, and post-mortem structure. It is designed to help teams respond quickly and consistently when a deployed model misbehaves. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write a model incident response playbook for production ML systems.

1. Incident classification:
 - P0 (Critical): model returning errors for >5% of requests, or predictions are completely wrong (e.g. all same class)
 - P1 (High): model latency > 2× SLA, silent accuracy degradation detected, feature drift alarm
 - P2 (Medium): single-segment performance degradation, prediction distribution shift detected
 - P3 (Low): data freshness lag, minor accuracy regression within acceptable bounds

2. Detection and alerting:
 - Define the monitoring signals that trigger each severity level
 - Alerting chain: PagerDuty → on-call ML engineer → ML team lead → CTO (for P0 only)
 - Initial acknowledgment SLA: P0=5 min, P1=15 min, P2=1 hour, P3=next business day

3. Immediate triage checklist (first 15 minutes for P0/P1):
 - Is this a model issue or an infrastructure issue? (Check serving logs, Kubernetes pod status)
 - Did a deployment happen recently? (Check deployment log)
 - Is the input data correct? (Check feature store freshness, pipeline health)
 - Is the error rate growing or stable?

4. Rollback procedure:
 - Trigger: error rate > 5% AND confirmed model issue
 - Steps: promote previous Production model version in registry → trigger rolling restart → verify error rate drops
 - Target: rollback complete within 10 minutes of decision to rollback

5. Post-incident review:
 - Timeline of events
 - Root cause analysis
 - Customer or business impact
 - What monitoring would have detected this earlier?
 - Action items with owners and deadlines

Return: complete incident response playbook with classification matrix, triage checklist, rollback procedure, and post-mortem template. 
```

## When to use this prompt 
Use case 01 
when production ML systems need a formal incident response procedure 
Use case 02 
when model failures must be classified by severity and response SLA 
Use case 03 
when on-call engineers need a concrete triage and rollback checklist 
Use case 04 
when post-incident reviews should lead to better monitoring and prevention 

## What the AI should return 

A complete model incident response playbook with severity matrix, detection rules, triage checklist, rollback steps, and post-mortem template. 

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

Once you have the first result, continue deeper with related prompts in MLOps and CI/CD.
