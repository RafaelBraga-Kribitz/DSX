# Full Cloud Data Engineering Chain *AI Prompt *

Step 1: Architecture design - choose the cloud data platform components (ingestion, storage, processing, serving, orchestration, catalog) for the given provider and requirements... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Architecture design - choose the cloud data platform components (ingestion, storage, processing, serving, orchestration, catalog) for the given provider and requirements. Define the medallion zones and table format (Delta Lake or Iceberg).
Step 2: Ingestion design - design the batch ingestion pipeline (ELT with managed connectors) and the streaming pipeline (CDC or event streaming). Define the landing zone schema and file format.
Step 3: Transformation layer - set up dbt on the cloud warehouse. Design the staging, intermediate, and mart layers. Configure incremental models for large tables. Set up dbt tests and source freshness checks.
Step 4: Orchestration - configure Airflow or the managed orchestrator. Define DAG structure, retry policies, and SLA alerts. Implement data-aware scheduling between upstream and downstream pipelines.
Step 5: Security and governance - configure IAM roles, network security (private endpoints), data encryption, and audit logging. Tag PII columns. Set up the data catalog and ownership assignments.
Step 6: Observability - implement pipeline monitoring (success rates, duration trends, SLA breaches), data quality monitoring (dbt test failures, row count anomalies), and cost monitoring (tagged resource spend).
Step 7: IaC and CI/CD - provision all infrastructure via Terraform. Set up CI for dbt (slim builds on PR). Set up CD for pipeline deployment. Define the runbook for common failure scenarios. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin cloud architecture work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Cloud Architecture or the wider Cloud Data Engineer library. 

## What the AI should return 

The AI should return a structured result that is directly usable in a cloud architecture workflow, with explicit outputs, readable formatting, and enough clarity to support the next step in cloud data engineer work. 

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

Once you have the first result, continue deeper with related prompts in Cloud Architecture.
