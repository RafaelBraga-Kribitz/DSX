# Monitoring and Observability *AI Prompts *

4 DataOps Engineer prompts in Monitoring and Observability. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 3 single prompts · 1 chain. 

## AI prompts in Monitoring and Observability 
4 prompts Advanced Single prompt 01 
### Cost Optimization for Data Pipelines 

Optimize the cost of running these data pipelines. Pipelines: {{pipeline_list}} Current monthly cost: {{cost}} Primary cost drivers: {{drivers}} (compute, query scanning, storag... 
Prompt text Optimize the cost of running these data pipelines.

Pipelines: {{pipeline_list}}
Current monthly cost: {{cost}}
Primary cost drivers: {{drivers}} (compute, query scanning, storage, data transfer)

1. Identify cost drivers:
 - Compute: warehouse/cluster runtime (cloud DW idle time, Spark cluster cost)
 - Query scanning: BigQuery/Athena per-byte pricing
 - Storage: raw data accumulation, no lifecycle policies
 - Data transfer: cross-region or cross-cloud movements

2. Compute optimization:
 - Right-size clusters: monitor CPU and memory utilization; if < 40%, downsize
 - Auto-terminate idle clusters: Databricks clusters auto-terminate after 10 minutes of inactivity
 - Spot/preemptible instances: 70-90% cheaper for fault-tolerant batch jobs
 - Consolidate pipelines: running 10 pipelines per hour is more expensive than 1 pipeline that processes 10 jobs per run

3. Query scanning optimization:
 - Partition pruning: ensure queries include the partition key in WHERE clauses
 - Column pruning: avoid SELECT *; query only required columns
 - Cache: use result caching for repeated identical queries
 - Materialized views: pre-compute expensive aggregations that are queried frequently

4. Storage optimization:
 - Enforce lifecycle policies: delete staging and temp files after 7 days
 - Compress and convert: convert CSV raw files to Parquet (5-10x smaller)
 - Deduplicate: remove exact duplicate files in the landing zone
 - Tiered storage: move cold data to cheaper storage tiers after 90 days

5. Pipeline scheduling optimization:
 - Batch small jobs together: instead of running 20 single-table pipelines, run one multi-table job
 - Shift heavy jobs to off-peak hours (lower spot prices; avoids peak warehouse pricing)
 - Skip runs when source data has not changed (source freshness check before running)

Return: cost breakdown analysis, compute optimization plan, query scanning reduction, storage lifecycle configuration, and scheduling optimization. Copy prompt Open prompt details Intermediate Single prompt 02 
### Data Pipeline Monitoring 

Set up comprehensive monitoring and alerting for this data pipeline. Pipeline: {{pipeline}} Orchestrator: {{orchestrator}} Stakeholder SLA: {{sla}} Alert channel: {{channel}} (S... 
Prompt text Set up comprehensive monitoring and alerting for this data pipeline.

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

Return: metrics definition, freshness monitoring queries, quality monitoring setup, alerting rules, and runbook templates. Copy prompt Open prompt details Advanced Chain 03 
### Full DataOps Chain 

Step 1: Maturity assessment - score the current team on: version control, automated testing, CI/CD, monitoring, documentation, and incident management. Identify the two lowest-s... 
Prompt text Step 1: Maturity assessment - score the current team on: version control, automated testing, CI/CD, monitoring, documentation, and incident management. Identify the two lowest-scoring dimensions and set 90-day improvement targets.
Step 2: Pipeline testing strategy - design the test pyramid for the stack. Implement unit tests for transformation logic. Configure dbt or Great Expectations for data quality tests. Create synthetic test data for integration tests.
Step 3: CI/CD pipeline - configure CI with linting, unit tests, smoke tests, and schema validation. Configure CD with environment promotion gates, staging integration tests, and automated production deployment with rollback capability.
Step 4: Monitoring and alerting - set up pipeline health metrics (success rate, duration trend, retry rate). Configure freshness monitoring per critical table. Implement row count anomaly detection with seasonality adjustment.
Step 5: Incident management - write a runbook for the top 5 most common failure modes. Set up Slack/PagerDuty alerting with escalation policies. Run the first blameless post-mortem simulation to build the muscle.
Step 6: Data quality framework - implement schema validation at ingestion, completeness/validity/consistency checks at each pipeline stage, and a DQ score dashboard by tier.
Step 7: Documentation and governance - register all production pipelines in the data catalog with owner, SLA, and lineage. Set up schema version control with Flyway or Liquibase. Establish the data contract registration process for all new data products. Copy prompt Open prompt details Advanced Single prompt 04 
### Root Cause Analysis for Data Incidents 

Build a root cause analysis process for data incidents in this pipeline. Incident: {{incident_description}} Affected pipelines: {{affected}} Business impact: {{impact}} 1. Incid... 
Prompt text Build a root cause analysis process for data incidents in this pipeline.

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

Return: incident response runbook, post-mortem template, five whys analysis, and action item tracking process. Copy prompt Open prompt details 
## Recommended Monitoring and Observability workflow 
1 
### Cost Optimization for Data Pipelines 

Start with a focused prompt in Monitoring and Observability so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Data Pipeline Monitoring 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Full DataOps Chain 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Root Cause Analysis for Data Incidents 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
