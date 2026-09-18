# Prediction Logging Setup *AI Prompt *

This prompt defines a production prediction logging system for online inference, covering schema design, async delivery, sink selection, retention, and privacy controls. It is useful when a serving stack needs traceable prediction records without adding latency to the request path. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design and implement a production prediction logging system for this ML model.

Model: {{model_name}}
Serving framework: {{serving_framework}}
Expected throughput: {{requests_per_second}} requests/sec

1. What to log per prediction:
 - request_id: unique identifier for traceability
 - model_name and model_version: which exact artifact served this request
 - timestamp: ISO 8601, UTC
 - input_features: the feature vector sent to the model (after preprocessing)
 - raw_input: the original unprocessed input (for debugging preprocessing bugs)
 - prediction: the model's output (class label, score, or generated value)
 - prediction_probability or confidence: confidence score where applicable
 - latency_ms: total inference time
 - serving_node: which pod/instance served the request (for debugging node-specific issues)

2. Async logging (never block the serving path):
 - Write to an in-memory queue in the request handler
 - Background thread drains the queue and writes to the log sink in batches
 - If the log sink is unavailable: drop logs gracefully, do not fail the prediction

3. Log sink options by throughput:
 - < 1k RPS: write directly to a structured log file, ship with Fluentd/Logstash
 - 1k–100k RPS: write to Kafka topic, consume to object storage and OLAP table
 - > 100k RPS: write to a high-throughput sink (Kinesis Data Firehose, Pub/Sub) with batching

4. Storage and retention:
 - Raw logs: object storage (S3/GCS), partitioned by model_name/date, retained for 90 days
 - Queryable table: OLAP warehouse (BigQuery/Snowflake), retained for 1 year
 - PII handling: mask or hash any PII fields in the feature log before storage

5. Log schema versioning:
 - Version the log schema alongside the model version
 - Never remove fields from the log schema — add new fields with NULL backfill for old records

Return: prediction log schema (JSON), async logging implementation, sink configuration for the given throughput, and PII masking approach. 
```

## When to use this prompt 
Use case 01 
when you need to log every production prediction with traceability metadata 
Use case 02 
when the serving path must remain non-blocking while logs are shipped asynchronously 
Use case 03 
when choosing the right log sink based on serving throughput 
Use case 04 
when retention, schema evolution, and PII masking need to be designed together 

## What the AI should return 

A production prediction logging design including JSON schema, async logging implementation, sink recommendation, storage plan, and PII masking strategy. 

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

Once you have the first result, continue deeper with related prompts in Model Monitoring.
