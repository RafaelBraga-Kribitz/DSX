# Streaming *AI Prompts *

3 Cloud Data Engineer prompts in Streaming. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 3 single prompts. 

## AI prompts in Streaming 
3 prompts Advanced Single prompt 01 
### CDC Pipeline Design 

Design a Change Data Capture (CDC) pipeline to replicate database changes to a cloud data platform. Source database: {{source_db}} (PostgreSQL, MySQL, SQL Server, Oracle) Target... 
Prompt text Design a Change Data Capture (CDC) pipeline to replicate database changes to a cloud data platform.

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

Return: CDC method selection, Debezium configuration, Kafka topic design, target landing pattern, and initial snapshot strategy. Copy prompt Open prompt details Advanced Single prompt 02 
### Real-Time Analytics Architecture 

Design a real-time analytics system that can answer queries over streaming data. Use case: {{use_case}} (live dashboard, fraud detection, real-time recommendation, monitoring) Q... 
Prompt text Design a real-time analytics system that can answer queries over streaming data.

Use case: {{use_case}} (live dashboard, fraud detection, real-time recommendation, monitoring)
Query latency requirement: {{latency}} (sub-second / seconds / minutes)
Throughput: {{throughput}} events per second
Cloud provider: {{provider}}

1. Architecture options by latency tier:

 Sub-second (operational analytics):
 - Pre-aggregate into a fast OLAP store (Apache Druid, ClickHouse, Apache Pinot)
 - These systems ingest from Kafka directly and support sub-second SQL
 - Trade-off: limited join support; pre-aggregation required at ingestion

 Seconds (near-real-time):
 - Streaming aggregation in Flink/Spark Streaming → Redis or DynamoDB for serving
 - Query latency: < 100ms from the serving layer
 - Useful for: live counters, session activity feeds, fraud scores

 Minutes (micro-batch):
 - Spark Structured Streaming or Flink with checkpointing every 1-5 minutes
 - Land in Delta Lake or Iceberg; query via Athena or BigQuery
 - Simpler operations than sub-second; good for most near-real-time dashboards

2. ClickHouse for real-time OLAP:
 - Ingests from Kafka natively (Kafka Engine table)
 - Columnar storage; billion-row aggregations in < 1 second
 - Materialized views update automatically as new data arrives
 - Self-managed or managed via ClickHouse Cloud / Altinity

3. Apache Pinot for real-time serving:
 - Designed for Uber/LinkedIn-scale user-facing analytics
 - Upserts supported; indexes optimized for filtering and aggregation
 - Real-time segment from Kafka + offline segment from S3 merged seamlessly

4. Lambda + materialized serving layer (simpler):
 - Batch layer: nightly aggregates materialized in the warehouse
 - Speed layer: streaming aggregates in Redis (last 15 minutes)
 - Serving layer: query combines batch + speed for a complete picture

5. Managed options:
 - BigQuery: Streaming inserts for near-real-time; Bigtable for < 10ms lookups
 - Snowflake: Dynamic Tables (incremental refresh) for near-real-time

Return: architecture for the latency tier, technology choices, ingestion and serving design, and operational considerations. Copy prompt Open prompt details Intermediate Single prompt 03 
### Streaming Data Pipeline Design 

Design a cloud streaming data pipeline for this use case. Cloud provider: {{provider}} Source: {{source}} (application events, CDC from database, IoT sensors, clickstream) Sink:... 
Prompt text Design a cloud streaming data pipeline for this use case.

Cloud provider: {{provider}}
Source: {{source}} (application events, CDC from database, IoT sensors, clickstream)
Sink: {{sink}} (data warehouse, data lake, real-time dashboard, downstream service)
Latency SLA: {{latency}} (sub-second, seconds, minutes)
Throughput: {{throughput}} messages per second

1. Message queue selection:

 AWS Kinesis Data Streams:
 - Managed, serverless, integrates with Lambda, Firehose, Flink
 - Shard-based scaling: 1 shard = 1MB/s ingest, 2MB/s read
 - Retention: 24h default, up to 7 days
 - Cost: per shard-hour + per PUT payload

 Google Pub/Sub:
 - Fully serverless (no shards to manage)
 - Auto-scales; guaranteed at-least-once delivery
 - Integrates tightly with Dataflow, BigQuery subscriptions

 Azure Event Hubs:
 - Kafka-compatible protocol (no code changes for Kafka producers)
 - Partition-based like Kinesis
 - Event Hubs Capture: auto-writes to ADLS Gen2

 Self-managed Kafka (on Confluent Cloud or MSK):
 - Maximum flexibility and ecosystem integration
 - Best for: existing Kafka investment, complex routing, exactly-once semantics

2. Stream processing:
 - Apache Flink: stateful, exactly-once, low latency (< 1 second) — best for complex CEP
 - Apache Spark Structured Streaming: micro-batch, easy to use, integrates with Delta Lake
 - Kinesis Data Analytics / Managed Flink: fully managed Flink on AWS
 - Google Dataflow (Apache Beam): unified batch + streaming, serverless on GCP

3. Lambda vs Kappa architecture:
 Lambda: separate batch and streaming paths that merge in a serving layer
 - Pro: batch path can reprocess historical data; streaming path handles recent data
 - Con: two codebases, complexity in merging

 Kappa: one streaming pipeline handles everything (batch = bounded stream)
 - Pro: single codebase, simpler operations
 - Recommended for most modern architectures with replayable message queues

4. Exactly-once semantics:
 - At-least-once: messages may be reprocessed on failure → idempotent sinks required
 - Exactly-once: Kafka Transactions + idempotent producers + transactional sinks
 - For most use cases: design for at-least-once with idempotent writes

Return: message queue recommendation, processing engine, Lambda vs Kappa decision, and exactly-once handling strategy. Copy prompt Open prompt details 
## Recommended Streaming workflow 
1 
### CDC Pipeline Design 

Start with a focused prompt in Streaming so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Real-Time Analytics Architecture 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Streaming Data Pipeline Design 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
