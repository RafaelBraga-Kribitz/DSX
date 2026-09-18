# Data Lake File Format Selection *AI Prompt *

This prompt helps select the right file and table formats for a lake or lakehouse based on workloads, engines, and update requirements. It is especially valuable when teams need to choose between plain file formats and ACID table formats for different layers. The response should clearly separate storage format from table-management capabilities. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Select the right file format and table format for each layer of this data lake.

Workloads: {{workloads}} (batch analytics, streaming, ML feature engineering, etc.)
Platform: {{compute_engines}} (Spark, Trino, Dremio, BigQuery, etc.)

1. File format comparison:

 Parquet:
 - Columnar, splittable, highly compressed
 - Best for: analytical reads, column-selective queries, broad engine support
 - Limitations: no ACID transactions, no efficient row-level updates, schema evolution is limited
 - Choose when: read-heavy analytics, stable schemas, no need for row-level changes

 ORC:
 - Similar to Parquet, marginally better for Hive workloads
 - Choose when: primary engine is Hive or Hive-compatible

 Avro:
 - Row-based, schema embedded in file, excellent schema evolution support
 - Best for: streaming ingestion, schema-registry integration, write-heavy workloads
 - Choose when: Kafka → data lake ingestion, schema evolution is frequent

 Delta Lake / Apache Iceberg / Apache Hudi (table formats):
 - ACID transactions, time travel, schema evolution, row-level deletes
 - Delta: tightest Spark integration, best for Databricks
 - Iceberg: broadest engine support (Spark, Trino, Flink, Dremio, BigQuery), best for multi-engine lakes
 - Hudi: streaming-optimized, best for CDC and near-real-time use cases

2. Recommendation by layer:
 - Bronze (raw ingest): Parquet or Avro depending on source
 - Silver (cleansed): Delta or Iceberg (need row-level updates for SCD)
 - Gold (marts): Delta or Iceberg (need ACID for concurrent writes)

3. Compression codec recommendation:
 - Snappy: fast compression/decompression, moderate compression ratio (default)
 - Zstd: better compression ratio than Snappy at similar speed (preferred for cold storage)
 - Gzip: maximum compression, slow decompression (use only for archival)

Return: format selection matrix, recommendation per layer, and compression codec guide. 
```

## When to use this prompt 
Use case 01 
When designing a data lake or lakehouse storage standard. 
Use case 02 
When supporting multiple compute engines over the same data. 
Use case 03 
When deciding between Parquet, Avro, Delta, Iceberg, or Hudi. 
Use case 04 
When compression choices affect performance and storage cost. 

## What the AI should return 

Return a format-selection matrix, layer-by-layer recommendation, and codec guide. Explain trade-offs for analytics, streaming, schema evolution, and row-level updates. The output should tell the reader what to use in Bronze, Silver, and Gold, and why. 

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

Once you have the first result, continue deeper with related prompts in Infrastructure and Platform.
