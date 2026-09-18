# CDC Pipeline Design *AI Prompt *

Design a Change Data Capture (CDC) pipeline to replicate database changes to a cloud data platform. Source database: {{source_db}} (PostgreSQL, MySQL, SQL Server, Oracle) Target... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a Change Data Capture (CDC) pipeline to replicate database changes to a cloud data platform.

Source database: {{source_db}} (PostgreSQL, MySQL, SQL Server, Oracle)
Target: {{target}} (Snowflake, BigQuery, Redshift, S3 Delta Lake)
Volume: {{volume}} changes per second
Latency requirement: {{latency}}

1. CDC methods:

 Log-based CDC (recommended):
 - Reads the database transaction log (WAL for Postgres, binlog for MySQL)
 - Zero impact on the source database (no queries)
 - Captures all changes: INSERT, UPDATE, DELETE
 - Tools: Debezium (open-source), AWS DMS, Airbyte, Fivetran

 Query-based CDC:
 - Periodically queries the source for rows changed since the last poll
 - Requires updated_at column; cannot detect deletes
 - Higher load on the source; simpler to set up

 Trigger-based CDC:
 - Database triggers write changes to a shadow table
 - Captures deletes; impacts source performance
 - Legacy approach; avoid for new designs

2. Debezium pipeline (log-based, Kafka):
 Source DB → Debezium Connector → Kafka → Sink Connector → Target

 PostgreSQL setup:
 wal_level = logical
 CREATE PUBLICATION debezium_pub FOR ALL TABLES;

 Debezium connector config:
 {
 "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
 "database.hostname": "...",
 "database.port": "5432",
 "slot.name": "debezium_slot",
 "publication.name": "debezium_pub",
 "transforms": "unwrap",
 "transforms.unwrap.type": "io.debezium.transforms.ExtractNewRecordState"
 }

3. CDC event format:
 Each event contains: before (old row state), after (new row state), op (c/u/d/r for create/update/delete/snapshot)
 Use the after record for upserts into the target

4. Target landing pattern:
 - Stage all CDC events in S3/GCS as Parquet/Avro
 - Apply MERGE into the target table hourly: upsert based on primary key
 - Or: use Flink/Spark Structured Streaming to apply changes in near-real-time

5. Backfill / initial snapshot:
 - Debezium performs an initial snapshot of the full table before starting log-based CDC
 - For large tables: take a manual full dump, load it, then start CDC from the current LSN
 - Verify: row counts match between source and target after initial load

Return: CDC method selection, Debezium configuration, Kafka topic design, target landing pattern, and initial snapshot strategy. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin streaming work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Streaming or the wider Cloud Data Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as CDC methods:, Reads the database transaction log (WAL for Postgres, binlog for MySQL), Zero impact on the source database (no queries). The final answer should stay clear, actionable, and easy to review inside a streaming workflow for cloud data engineer work. 

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

Once you have the first result, continue deeper with related prompts in Streaming.
