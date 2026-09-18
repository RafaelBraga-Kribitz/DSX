# Pipeline Observability and Monitoring *AI Prompt *

Design an observability framework for this cloud data pipeline. Cloud provider: {{provider}} Orchestrator: {{orchestrator}} (Airflow, Prefect, Dagster, dbt Cloud) Pipeline count... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design an observability framework for this cloud data pipeline.

Cloud provider: {{provider}}
Orchestrator: {{orchestrator}} (Airflow, Prefect, Dagster, dbt Cloud)
Pipeline count: {{pipeline_count}}
SLA requirements: {{sla}}

1. What to monitor:

 Pipeline health:
 - Success/failure rate per DAG/job over time
 - Duration trend: is a job getting slower? (may indicate data volume growth or a query regression)
 - Retry rate: high retries indicate flaky upstream dependencies

 Data freshness:
 - Time since last successful run per table
 - SLA breach: alert if a critical table has not been updated within {{sla}} hours

 Data quality:
 - Test failure rate per dbt model
 - Row count anomalies: significant drop or spike vs rolling average

 Infrastructure:
 - Cloud service quotas: Airflow task concurrency, Snowflake credit consumption
 - Storage growth: S3/GCS bucket size trends

2. Observability stack:
 - Airflow: built-in metrics via StatsD → Prometheus → Grafana
 - dbt: elementary package → data observability dashboard
 - Cloud-native: AWS CloudWatch / GCP Cloud Monitoring / Azure Monitor for infrastructure
 - Data catalog: Dataplex / Purview / Atlan for data lineage and freshness

3. Alerting design:
 - Alert on pipeline failure: Slack + PagerDuty (for SLA-critical pipelines)
 - Alert on SLA breach (job did not complete on time): escalate based on tier
 - Alert on data quality failure: Slack with affected model, failure reason, and link to dbt docs
 - Avoid alert fatigue: start with few high-signal alerts; add gradually

4. Lineage tracking:
 - Column-level lineage: which source columns feed each output column
 - Tools: dbt + Elementary (column-level lineage), DataHub, Atlan, OpenLineage
 - OpenLineage standard: emit lineage events from Airflow/Spark/dbt → centralize in Marquez or DataHub

5. Runbook for common failures:
 - Source freshness failure: check source system → check connector logs → retry
 - dbt test failure: run `dbt test --select <model>` in dev → investigate SQL → fix upstream
 - Airflow DAG stuck: check Airflow scheduler logs → check DB connections → manually clear task

Return: monitoring metric definitions, alerting configuration, lineage tooling recommendation, and runbook templates. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin orchestration work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Orchestration or the wider Cloud Data Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as What to monitor:, Success/failure rate per DAG/job over time, Duration trend: is a job getting slower? (may indicate data volume growth or a query regression). The final answer should stay clear, actionable, and easy to review inside a orchestration workflow for cloud data engineer work. 

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

Once you have the first result, continue deeper with related prompts in Orchestration.
