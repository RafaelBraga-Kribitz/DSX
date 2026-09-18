# Data Lake Design on Cloud Object Storage *AI Prompt *

Design a well-organized, cost-effective data lake on cloud object storage. Provider: {{provider}} (S3, GCS, ADLS Gen2) Data types: {{data_types}} (raw events, processed tables,... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a well-organized, cost-effective data lake on cloud object storage.

Provider: {{provider}} (S3, GCS, ADLS Gen2)
Data types: {{data_types}} (raw events, processed tables, ML features, archived logs)
Access patterns: {{access_patterns}}
Retention: {{retention}}

1. Folder structure (medallion architecture):
 s3://company-data-lake/
 ├── bronze/ # raw data, immutable, exactly as received
 │ ├── source_system=stripe/
 │ ├── source_system=postgres/
 │ └── source_system=salesforce/
 ├── silver/ # cleaned, validated, enriched
 │ ├── domain=finance/
 │ ├── domain=product/
 │ └── domain=marketing/
 ├── gold/ # business-ready aggregates, mart tables
 │ ├── reporting/
 │ └── ml-features/
 └── sandbox/ # exploratory work, not production

2. File format selection:
 - Parquet: columnar, compressed, best for analytical queries — use for all structured data
 - ORC: similar to Parquet, preferred in Hive/Hadoop ecosystems
 - Avro: row-oriented, schema evolution support — use for streaming and Kafka
 - JSON/CSV: only for bronze landing zone (raw source format)
 - Delta / Iceberg: Parquet + transaction log — use when ACID and schema evolution needed

3. Partitioning strategy:
 - Partition by ingestion date for time-series data: year=2024/month=01/day=15/
 - Partition by business key for lookup data: tenant_id=abc/
 - Avoid over-partitioning: < 10MB per partition file is too small (many small files problem)
 - Target: 100MB–1GB per partition file for Spark/Athena efficiency

4. Compaction (small file problem):
 - Streaming writes create many small files → poor query performance
 - Run a compaction job periodically: read partition, write as one large file
 - Delta Lake: OPTIMIZE command with Z-ORDER for layout optimization
 - AWS S3: S3 Intelligent-Tiering for cost optimization across file sizes

5. Lifecycle policies:
 - Bronze: retain forever (immutable raw data)
 - Silver: retain 3 years, move to Glacier after 1 year
 - Gold: retain 1 year, recreatable from silver
 - Sandbox: delete after 90 days

Return: folder structure, file format recommendations, partitioning strategy, compaction schedule, and lifecycle policy configuration. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin cloud storage work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Cloud Storage or the wider Cloud Data Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Folder structure (medallion architecture):, File format selection:, Parquet: columnar, compressed, best for analytical queries — use for all structured data. The final answer should stay clear, actionable, and easy to review inside a cloud storage workflow for cloud data engineer work. 

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

Once you have the first result, continue deeper with related prompts in Cloud Storage.
