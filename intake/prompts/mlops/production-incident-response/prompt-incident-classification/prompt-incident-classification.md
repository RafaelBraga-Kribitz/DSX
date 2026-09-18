# Incident Classification Matrix *AI Prompt *

This prompt defines severity levels, SLAs, declaration rules, and communication templates for ML production incidents. It is helpful when teams need a shared language for incident response before building detailed runbooks. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Define an ML model incident classification matrix and response procedures for each severity level.

1. Severity levels and definitions:

 P0 — Critical (page immediately, all hands):
 - Model is returning errors for > 5% of requests (hard failures)
 - Model is completely unresponsive (serving down)
 - Model predictions are obviously wrong across the board (e.g. classifier predicting all-one-class)
 - Downstream system failure caused by model output
 Response SLA: acknowledge in 5 minutes, update in 15 minutes, resolve or mitigate in 60 minutes

 P1 — High (page on-call engineer):
 - Model latency p99 > 2× SLA for > 10 minutes
 - Error rate > 1% and rising
 - Significant prediction distribution shift detected (PSI > 0.5)
 - Silent accuracy degradation confirmed (performance drop > 10% vs baseline)
 Response SLA: acknowledge in 15 minutes, resolve or mitigate in 4 hours

 P2 — Medium (notify ML team via Slack):
 - Model latency p99 between 1× and 2× SLA
 - Moderate drift detected (PSI 0.2–0.5)
 - Performance drop 5–10% vs baseline
 - Label rate dropped below expected (feedback loop issue)
 Response SLA: acknowledge in 1 hour, resolve in 24 hours

 P3 — Low (create ticket, handle next business day):
 - Minor drift (PSI 0.1–0.2)
 - Performance drop < 5%
 - Monitoring data quality issues (missing logs, delayed metrics)
 Response SLA: acknowledge in 4 hours, resolve in 1 week

2. Incident declaration criteria:
 - Any automated alert at P0 or P1 automatically creates an incident
 - P2 and P3: engineer uses judgment based on business context

3. Incident communication template:
 - Status page update: 'Investigating reports of [issue] affecting [model]. Engineers are engaged.'
 - Internal Slack: 'P[X] incident declared for [model_name]. Owner: [name]. Bridge: [link]'

Return: classification matrix table, SLA definitions, alert-to-incident mapping, and communication templates. 
```

## When to use this prompt 
Use case 01 
when an ML team needs a formal incident severity matrix 
Use case 02 
when alerts must map consistently to incident declarations 
Use case 03 
when response SLAs should be explicit for model-related failures 
Use case 04 
when standard communication templates are needed for incidents 

## What the AI should return 

An ML incident classification matrix with severity definitions, SLAs, declaration logic, and communication templates. 

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
