# Orchestration *AI Prompts *

4 Cloud Data Engineer prompts in Orchestration. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 4 single prompts. 

## AI prompts in Orchestration 
4 prompts Intermediate Single prompt 01 
### Cloud Orchestration with Airflow 

Design and implement an Airflow orchestration pattern for this data pipeline. Provider: {{provider}} (AWS MWAA, GCP Cloud Composer, Astronomer, self-hosted) Pipeline: {{pipeline... 
Prompt text Design and implement an Airflow orchestration pattern for this data pipeline.

Provider: {{provider}} (AWS MWAA, GCP Cloud Composer, Astronomer, self-hosted)
Pipeline: {{pipeline_description}}
Dependencies: {{dependencies}}
SLA: {{sla}}

1. DAG design principles:
 - One DAG = one business process (not one per table)
 - Idempotent tasks: re-running any task produces the same result
 - No business logic in the DAG file; DAG file only defines the workflow
 - Use template variables for dates: {{ ds }}, {{ execution_date }}, {{ next_ds }}

2. Task types:
 BashOperator: shell commands
 PythonOperator: Python functions (keep functions small and focused)
 BigQueryInsertJobOperator: BigQuery SQL execution
 RedshiftSQLOperator: Redshift queries
 S3ToRedshiftOperator: load S3 files to Redshift
 DbtOperator / DbtCloudRunJobOperator: trigger dbt runs
 HttpSensor: wait for an API endpoint to be available
 ExternalTaskSensor: wait for a task in another DAG

3. Retry and SLA configuration:
 default_args = {
 'retries': 3,
 'retry_delay': timedelta(minutes=5),
 'retry_exponential_backoff': True,
 'email_on_failure': True,
 'sla': timedelta(hours=4),
 }

4. Dynamic DAGs (for many similar pipelines):
 # Generate a DAG per source table from a config file
 for table in config['tables']:
 with DAG(f'sync_{table["name"]}', ...) as dag:
 globals()[f'dag_{table["name"]}'] = dag

5. Data-aware scheduling (Airflow 2.4+):
 # Trigger a downstream DAG when an upstream dataset is updated
 @dag(schedule=[Dataset('s3://bucket/processed/orders')])
 def downstream_dag():
 ...
 # Declarative dependency management without sensors

6. Testing Airflow DAGs:
 - DAG integrity test: ensure all DAGs parse without errors (dag.test_cycle())
 - Task unit tests: test the Python function independently
 - Integration test: airflow dags test <dag_id> <execution_date> in a local environment

Return: DAG template with retry configuration, dynamic DAG generation pattern, data-aware scheduling, and testing approach. Copy prompt Open prompt details Advanced Single prompt 02 
### Data Contracts and SLA Management 

Implement data contracts and SLA management for data products in this cloud platform. Data producers: {{producers}} Data consumers: {{consumers}} Current issues: {{issues}} (sch... 
Prompt text Implement data contracts and SLA management for data products in this cloud platform.

Data producers: {{producers}}
Data consumers: {{consumers}}
Current issues: {{issues}} (schema breaking changes, missed SLAs, undocumented changes)

1. What is a data contract:
 A data contract is a formal agreement between a data producer (team that writes the data) and data consumers (teams that read it). It specifies:
 - Schema: column names, types, and semantic meaning
 - Quality: expected null rates, value distributions, referential integrity
 - SLA: freshness (max hours since last update), availability (uptime %)
 - Versioning: how schema changes are communicated and backward compatibility

2. Data contract specification (YAML):
 apiVersion: v1
 kind: DataContract
 id: orders.v1
 producer: payments-team
 owner: payments-data@company.com
 schema:
 - name: order_id
 type: bigint
 nullable: false
 unique: true
 - name: amount_usd
 type: numeric(10,2)
 nullable: false
 minimum: 0
 sla:
 freshness_hours: 2
 availability_percent: 99.5
 versioning:
 current: 1.2.0
 breaking_change_policy: 30-day notice required

3. Tooling:
 - Data Contract CLI (open-source): validate data against contracts, publish to catalog
 - Soda Core: run quality checks defined in contracts
 - dbt + Elementary: enforce schema contracts via model contracts; test quality via tests

4. SLA monitoring:
 - Freshness check: query MAX(updated_at) per table; alert if > SLA threshold
 - Availability: monitor pipeline success rate; alert on consecutive failures
 - Quality score: % of tests passing per data product; publish in the catalog
 - SLA breach report: weekly report of SLA breaches per team, with trend

5. Governance process:
 - Contract registration: new data products must register a contract before GA
 - Breaking change process: 30-day notice + migration guide for all consumers
 - Deprecation: deprecated products sunset after 90 days with active consumer notification

Return: data contract YAML schema, tooling recommendation, SLA monitoring implementation, and governance process. Copy prompt Open prompt details Intermediate Single prompt 03 
### Infrastructure as Code for Data 

Implement Infrastructure as Code (IaC) for this cloud data platform. Cloud provider: {{provider}} IaC tool: {{iac_tool}} (Terraform, Pulumi, CDK, Bicep) Components to provision:... 
Prompt text Implement Infrastructure as Code (IaC) for this cloud data platform.

Cloud provider: {{provider}}
IaC tool: {{iac_tool}} (Terraform, Pulumi, CDK, Bicep)
Components to provision: {{components}}
Team: {{team}}

1. Why IaC for data infrastructure:
 - Reproducible: dev, staging, and prod environments are identical
 - Version-controlled: infrastructure changes are reviewed like code
 - Self-documenting: the Terraform / Pulumi code IS the documentation
 - Auditable: every change is in git history with the author

2. Terraform for cloud data resources:

 S3 bucket with lifecycle and logging:
 resource "aws_s3_bucket" "data_lake" {
 bucket = "${var.env}-data-lake-${var.account_id}"
 tags = { Environment = var.env, Team = "data-engineering" }
 }

 Snowflake warehouse:
 resource "snowflake_warehouse" "analytics" {
 name = "ANALYTICS_WH"
 warehouse_size = "SMALL"
 auto_suspend = 60
 auto_resume = true
 }

3. Module structure:
 modules/
 data_lake/ # S3 bucket + lifecycle + IAM
 snowflake_env/ # databases, warehouses, roles
 airflow_mwaa/ # MWAA environment + networking
 monitoring/ # CloudWatch dashboards + alarms

 environments/
 dev/main.tf # calls modules with dev variables
 prod/main.tf # calls modules with prod variables

4. State management:
 - Remote state: store in S3 + DynamoDB (AWS) or GCS (GCP) with locking
 - State locking: prevents concurrent runs from corrupting state
 - Separate state per environment: dev and prod should never share state

5. CI/CD for IaC:
 PR: terraform plan → post plan output as PR comment
 Merge to main: terraform apply (with approval gate for prod)
 Tool: Atlantis (open-source) or Terraform Cloud for automated plan/apply

Return: Terraform module structure, resource examples, state management configuration, and CI/CD pipeline for IaC. Copy prompt Open prompt details Advanced Single prompt 04 
### Pipeline Observability and Monitoring 

Design an observability framework for this cloud data pipeline. Cloud provider: {{provider}} Orchestrator: {{orchestrator}} (Airflow, Prefect, Dagster, dbt Cloud) Pipeline count... 
Prompt text Design an observability framework for this cloud data pipeline.

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

Return: monitoring metric definitions, alerting configuration, lineage tooling recommendation, and runbook templates. Copy prompt Open prompt details 
## Recommended Orchestration workflow 
1 
### Cloud Orchestration with Airflow 

Start with a focused prompt in Orchestration so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Data Contracts and SLA Management 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Infrastructure as Code for Data 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Pipeline Observability and Monitoring 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
