# Streaming Data Pipeline Design *AI Prompt *

Design a cloud streaming data pipeline for this use case. Cloud provider: {{provider}} Source: {{source}} (application events, CDC from database, IoT sensors, clickstream) Sink:... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a cloud streaming data pipeline for this use case.

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

Return: message queue recommendation, processing engine, Lambda vs Kappa decision, and exactly-once handling strategy. 
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

The AI should return a structured result that covers the main requested outputs, such as Message queue selection:, Managed, serverless, integrates with Lambda, Firehose, Flink, Shard-based scaling: 1 shard = 1MB/s ingest, 2MB/s read. The final answer should stay clear, actionable, and easy to review inside a streaming workflow for cloud data engineer work. 

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
