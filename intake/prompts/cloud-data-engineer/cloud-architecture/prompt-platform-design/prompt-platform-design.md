# Cloud Data Platform Architecture *AI Prompt *

Design a cloud-native data platform architecture for this organization. Cloud provider: {{provider}} (AWS, GCP, Azure) Data sources: {{sources}} Users: {{users}} (analysts, data... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a cloud-native data platform architecture for this organization.

Cloud provider: {{provider}} (AWS, GCP, Azure)
Data sources: {{sources}}
Users: {{users}} (analysts, data scientists, engineers)
Scale: {{scale}}

1. AWS reference architecture:
 - Ingestion: Kinesis Data Streams (streaming) / AWS Glue (batch ETL)
 - Storage: S3 (data lake) + Redshift (warehouse) + RDS (operational)
 - Processing: AWS Glue / EMR (Spark) / Lambda (serverless)
 - Serving: Redshift / Athena (S3 queries) / DynamoDB (low-latency lookups)
 - Orchestration: Apache Airflow on MWAA / AWS Step Functions
 - Catalog: AWS Glue Data Catalog
 - BI: QuickSight / Tableau / Looker

2. GCP reference architecture:
 - Ingestion: Pub/Sub (streaming) / Cloud Dataflow / Cloud Composer (Airflow)
 - Storage: Cloud Storage (data lake) + BigQuery (warehouse)
 - Processing: Dataflow (Apache Beam) / Dataproc (Spark)
 - Serving: BigQuery / Bigtable (low-latency) / Cloud Spanner (transactional)
 - Catalog: Dataplex / Data Catalog
 - BI: Looker / Looker Studio / Tableau

3. Azure reference architecture:
 - Ingestion: Event Hubs (streaming) / Azure Data Factory (ETL/ELT)
 - Storage: ADLS Gen2 (data lake) + Synapse Analytics (warehouse)
 - Processing: Databricks / Azure Synapse Spark / Azure Stream Analytics
 - Serving: Synapse / Cosmos DB / Azure SQL
 - Catalog: Microsoft Purview
 - BI: Power BI

4. Lake House pattern (recommended default):
 - Single storage layer (cloud object storage) holds all data in open formats (Parquet, Delta, Iceberg)
 - Multiple compute engines query the same data (Spark, Athena, BigQuery Omni, Trino)
 - Delta Lake / Apache Iceberg: ACID transactions on the data lake
 - Eliminates data duplication between a separate data lake and warehouse

5. Cost optimization:
 - Separate storage and compute: scale them independently
 - Use spot/preemptible instances for batch processing
 - Implement data tiering: hot (SSD), warm (HDD/standard), cold (archival)

Return: reference architecture diagram (text), component selection rationale, lake house vs traditional warehouse decision, and cost optimization approach. 
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

The AI should return a structured result that covers the main requested outputs, such as AWS reference architecture:, Ingestion: Kinesis Data Streams (streaming) / AWS Glue (batch ETL), Storage: S3 (data lake) + Redshift (warehouse) + RDS (operational). The final answer should stay clear, actionable, and easy to review inside a cloud architecture workflow for cloud data engineer work. 

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
