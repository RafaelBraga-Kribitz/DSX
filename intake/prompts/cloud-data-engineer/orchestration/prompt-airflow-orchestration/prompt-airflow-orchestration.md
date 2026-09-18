# Cloud Orchestration with Airflow *AI Prompt *

Design and implement an Airflow orchestration pattern for this data pipeline. Provider: {{provider}} (AWS MWAA, GCP Cloud Composer, Astronomer, self-hosted) Pipeline: {{pipeline... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design and implement an Airflow orchestration pattern for this data pipeline.

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

Return: DAG template with retry configuration, dynamic DAG generation pattern, data-aware scheduling, and testing approach. 
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

The AI should return a structured result that covers the main requested outputs, such as DAG design principles:, One DAG = one business process (not one per table), Idempotent tasks: re-running any task produces the same result. The final answer should stay clear, actionable, and easy to review inside a orchestration workflow for cloud data engineer work. 

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
