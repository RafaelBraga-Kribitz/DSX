# SLA Monitoring for Pipelines *AI Prompt *

This prompt builds an SLA monitoring system around pipeline delivery commitments such as table availability and freshness deadlines. It is useful when business users depend on data arriving by specific times and late delivery must be detected early. The output should include both real-time checks and recurring compliance reporting. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build an SLA monitoring system for data pipeline delivery commitments.

Pipelines to monitor: {{pipeline_list}}
SLA targets: {{sla_targets}} (e.g. 'orders table available by 06:00 UTC daily')

1. SLA definition table:
 ```sql
 CREATE TABLE pipeline_slas (
 pipeline_name VARCHAR,
 table_name VARCHAR,
 sla_type VARCHAR, -- 'availability' or 'freshness'
 sla_deadline TIME, -- time by which data must be available
 sla_timezone VARCHAR,
 warn_minutes_before INT, -- warn this many minutes before breach
 owner_team VARCHAR,
 slack_channel VARCHAR
 )
 ```

2. SLA tracking (run every 5 minutes):
 - For availability SLAs: has the pipeline completed successfully since the last scheduled run?
 - For freshness SLAs: is MAX(updated_at) in the target table within the SLA window?
 - Record each check: pipeline_name, check_time, status (ON_TIME / AT_RISK / BREACHED)

3. Early warning system:
 - AT_RISK: pipeline is running but has not completed with {{warn_minutes}} minutes remaining before SLA
 - Estimate: based on current progress, will it complete in time?
 - Alert the pipeline owner with estimated completion time

4. SLA breach handling:
 - BREACHED: SLA deadline has passed and data is not available
 - Page the on-call data engineer
 - Notify downstream consumers automatically
 - Log breach duration for SLA reporting

5. SLA reporting (weekly):
 - SLA compliance rate per pipeline (target: ≥ 99.5%)
 - Average delay for late pipelines
 - Top 3 pipelines by breach frequency
 - MTTD and MTTR per pipeline

Return: SLA definition table DDL, monitoring query, early warning logic, breach alert template, and weekly SLA report query. 
```

## When to use this prompt 
Use case 01 
When data products have committed delivery deadlines. 
Use case 02 
When pipeline lateness impacts dashboards, reports, or downstream jobs. 
Use case 03 
When early-warning alerts are needed before an SLA breach occurs. 
Use case 04 
When compliance rates, MTTD, and MTTR must be reported over time. 

## What the AI should return 

Return SLA definition DDL, monitoring queries, early-warning rules, breach-handling logic, alert templates, and weekly reporting queries. Explain how availability and freshness SLAs differ and how each is checked. The output should also define statuses such as ON_TIME, AT_RISK, and BREACHED. 

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

Once you have the first result, continue deeper with related prompts in Data Quality.
