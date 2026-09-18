# Real-Time Analytics Architecture *AI Prompt *

Design a real-time analytics system that can answer queries over streaming data. Use case: {{use_case}} (live dashboard, fraud detection, real-time recommendation, monitoring) Q... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a real-time analytics system that can answer queries over streaming data.

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

Return: architecture for the latency tier, technology choices, ingestion and serving design, and operational considerations. 
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

The AI should return a structured result that covers the main requested outputs, such as Architecture options by latency tier:, Pre-aggregate into a fast OLAP store (Apache Druid, ClickHouse, Apache Pinot), These systems ingest from Kafka directly and support sub-second SQL. The final answer should stay clear, actionable, and easy to review inside a streaming workflow for cloud data engineer work. 

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
