# Streaming Pipeline Design *AI Prompt *

This prompt is for designing a streaming pipeline that can meet strict throughput and latency requirements while remaining replayable and observable. It covers broker setup, consumer behavior, stateful processing, exactly-once considerations, DLQ handling, and monitoring. It is useful when the team needs an end-to-end real-time design, not just code snippets. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a streaming data pipeline for processing {{event_type}} events from {{source}} to {{destination}}.

Throughput requirement: {{throughput}} events/sec
Latency requirement: end-to-end < {{latency_target}}

1. Message broker configuration (Kafka / Kinesis):
 - Topic partitioning: number of partitions = max_throughput / throughput_per_partition
 - Partition key: choose a key that distributes load evenly AND ensures ordering where required
 - Retention: set to at least 7 days to allow replay from any point in the last week
 - Replication factor: 3 for production (tolerates 2 broker failures)

2. Consumer design:
 - Consumer group: one per logical pipeline to enable independent replay
 - Offset commit strategy: commit after successful write to destination (at-least-once delivery)
 - Idempotent consumer: handle duplicate messages at the destination with deduplication on event_id
 - Backpressure: limit consumer fetch size and processing batch to control memory usage

3. Stream processing (Flink / Spark Structured Streaming / Kafka Streams):
 - Windowing: tumbling window of {{window_size}} for aggregations
 - Watermark: allow late events up to {{late_arrival_tolerance}} before closing window
 - State management: use checkpointing every 60 seconds for fault tolerance

4. Exactly-once semantics:
 - Kafka transactions + idempotent producers for source-to-broker
 - Transactional writes to destination (or idempotent upserts)
 - Checkpoint-based recovery to avoid reprocessing

5. Dead letter queue:
 - Route unparseable or schema-invalid messages to a DLQ topic
 - Alert on DLQ growth rate > {{dlq_threshold}} messages/min

6. Monitoring:
 - Consumer lag per partition (alert if lag > {{lag_threshold}})
 - Processing latency (time from event timestamp to destination write)
 - Throughput (events/sec in and out)

Return: architecture diagram (text), configuration recommendations, processing code skeleton, and monitoring setup. 
```

## When to use this prompt 
Use case 01 
When designing a Kafka, Kinesis, Flink, or streaming Spark pipeline. 
Use case 02 
When moving from batch to near-real-time processing. 
Use case 03 
When you need to reason about late events, lag, and replayability. 
Use case 04 
When planning production monitoring and DLQ handling for event pipelines. 

## What the AI should return 

Return a text architecture diagram, recommended broker and consumer configuration, processing design, and monitoring plan. Include key assumptions, trade-offs around delivery semantics, and a code skeleton for the stream processing layer. The output should also specify what to alert on and how to handle poison messages. 

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

Once you have the first result, continue deeper with related prompts in Pipeline Design.
