# Root Cause Analysis for Data Incidents *AI Prompt *

Build a root cause analysis process for data incidents in this pipeline. Incident: {{incident_description}} Affected pipelines: {{affected}} Business impact: {{impact}} 1. Incid... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a root cause analysis process for data incidents in this pipeline.

Incident: {{incident_description}}
Affected pipelines: {{affected}}
Business impact: {{impact}}

1. Incident response phases:

 Detection (0-5 minutes):
 - Automated alert fires → on-call engineer acknowledges
 - Declare incident in #data-incidents: title, affected systems, business impact
 - Start an incident timeline document

 Triage (5-30 minutes):
 - Is this affecting consumers right now? If yes: communicate status to stakeholders
 - What is the blast radius? List affected tables, dashboards, and downstream pipelines
 - Can we roll back to a known good state? If yes: initiate rollback while investigating

 Investigation (30 minutes - 2 hours):
 - Walk the pipeline backwards from the symptom to the root cause
 - Check: upstream data freshness, row counts at each stage, error logs at each step
 - Questions to answer:
 When did it start? (check pipeline history)
 What changed recently? (git log, deployment history)
 Is the source data valid? (check at the raw/bronze layer)

 Resolution:
 - Fix the root cause OR apply a workaround (data patch, pipeline re-run)
 - Verify: affected tables are fresh and quality checks pass
 - Close the incident; communicate resolution to stakeholders

2. Blameless post-mortem template:
 Incident summary:
 Timeline: (bullet points with timestamps)
 Root cause: (technical and process causes)
 Impact: (duration, affected users, business cost)
 What went well:
 What went poorly:
 Action items: (specific, assigned, time-bound)

3. Five whys for data incidents:
 Why were the dashboards stale? → The pipeline failed
 Why did the pipeline fail? → A source table had no new rows
 Why was the source table empty? → The upstream ETL job failed silently
 Why was the failure silent? → No alert was configured for that ETL job
 Why was no alert configured? → The pipeline was added without following the onboarding checklist
 Root cause: missing monitoring onboarding checklist item

4. Action item types:
 Detection: add monitoring to catch this class of failure earlier
 Prevention: add a test or validation that would have prevented this
 Response: update the runbook with the steps that resolved this incident

Return: incident response runbook, post-mortem template, five whys analysis, and action item tracking process. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin monitoring and observability work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Monitoring and Observability or the wider DataOps Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Incident response phases:, Automated alert fires → on-call engineer acknowledges, Declare incident in #data-incidents: title, affected systems, business impact. The final answer should stay clear, actionable, and easy to review inside a monitoring and observability workflow for dataops engineer work. 

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

Once you have the first result, continue deeper with related prompts in Monitoring and Observability.
