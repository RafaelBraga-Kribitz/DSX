# Data Pipeline Monitoring *AI Prompt *

Set up comprehensive monitoring and alerting for this data pipeline. Pipeline: {{pipeline}} Orchestrator: {{orchestrator}} Stakeholder SLA: {{sla}} Alert channel: {{channel}} (S... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Set up comprehensive monitoring and alerting for this data pipeline.

Pipeline: {{pipeline}}
Orchestrator: {{orchestrator}}
Stakeholder SLA: {{sla}}
Alert channel: {{channel}} (Slack, PagerDuty, email)

1. Pipeline health metrics:
 - Success rate: % of pipeline runs that completed without errors (target > 99% for Tier 1)
 - Duration trend: track p50/p95 runtime per pipeline; alert on significant increase (>30% WoW)
 - Retry rate: high retries indicate a flaky upstream dependency
 - Queue wait time: for orchestrators with queuing, time before a task starts executing

2. Data freshness monitoring:
 - For each critical output table: monitor MAX(updated_at)
 - Alert: if MAX(updated_at) has not moved within 1.5× the expected refresh interval
 - Freshness check query:
 SELECT table_name,
 MAX(updated_at) AS last_update,
 CURRENT_TIMESTAMP - MAX(updated_at) AS lag
 FROM critical_tables
 GROUP BY 1
 HAVING lag > INTERVAL '4 hours';

3. Data quality monitoring:
 - Row count trend: compare today's row count to the 7-day rolling average
 Flag: > 20% deviation
 - Null rate: track % null per critical column over time
 Flag: null rate increases by > 5 percentage points
 - Duplicate rate: unique count / total count per primary key column
 Flag: duplicate rate > 0.01%

4. Alerting runbook per alert type:
 Pipeline failure alert:
 1. Check Airflow/orchestrator logs for the error
 2. Check upstream data source for freshness
 3. Retry the pipeline; if it fails again, escalate
 4. If blocked for > 30 minutes, post in #data-incidents and tag the on-call engineer

5. Alert suppression during maintenance:
 - Suppress alerts during planned maintenance windows
 - Declare maintenance in a shared runbook before starting
 - Auto-suppress: if the pipeline is manually paused, suppress freshness alerts

Return: metrics definition, freshness monitoring queries, quality monitoring setup, alerting rules, and runbook templates. 
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

The AI should return a structured result that covers the main requested outputs, such as Pipeline health metrics:, Success rate: % of pipeline runs that completed without errors (target > 99% for Tier 1), Duration trend: track p50/p95 runtime per pipeline; alert on significant increase (>30% WoW). The final answer should stay clear, actionable, and easy to review inside a monitoring and observability workflow for dataops engineer work. 

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
