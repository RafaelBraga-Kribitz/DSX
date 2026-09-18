# Ingestion Pattern Selector *AI Prompt *

This prompt helps choose the right ingestion pattern for a source based on latency, volume, change behavior, and source-system constraints. It avoids the common mistake of defaulting to full loads or CDC without checking whether the source and business requirements justify that choice. The result should balance simplicity, correctness, source impact, and future scalability. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Recommend the right data ingestion pattern for this source system.

Source system: {{source_system}}
Data characteristics: {{data_characteristics}}
Latency requirement: {{latency_requirement}}
Volume: {{volume}}

Evaluate and recommend from these patterns:

1. Full load:
 - Re-ingest the entire source table on every run
 - When to use: small tables (<1M rows), no reliable change tracking, sources that cannot support incremental queries
 - Drawbacks: expensive, slow, high source system load

2. Incremental load (timestamp-based):
 - Query rows where updated_at > last_watermark
 - When to use: source has a reliable updated_at column, append-and-update workloads
 - Drawbacks: misses hard deletes, requires reliable timestamp column

3. Change Data Capture (CDC):
 - Read from database transaction log (Debezium, AWS DMS, Fivetran)
 - When to use: need to capture deletes, near-real-time latency, high-volume OLTP source
 - Drawbacks: requires log access, more complex infrastructure

4. Event streaming:
 - Source publishes events to Kafka/Kinesis, pipeline consumes
 - When to use: event-driven architecture already exists, sub-minute latency needed
 - Drawbacks: requires event producer instrumentation

5. API polling:
 - Call REST/GraphQL API on schedule
 - When to use: no database access, SaaS sources (Salesforce, HubSpot)
 - Drawbacks: rate limits, pagination, no deletes

Return: recommended pattern with rationale, drawbacks to be aware of, and implementation checklist. 
```

## When to use this prompt 
Use case 01 
When onboarding a new source system into a data platform. 
Use case 02 
When deciding between batch, CDC, streaming, or API-based ingestion. 
Use case 03 
When a current ingestion method is too slow, too expensive, or missing deletes. 
Use case 04 
When you need to justify the chosen pattern to engineers or stakeholders. 

## What the AI should return 

Return the recommended ingestion pattern first, followed by a comparison of the main alternatives considered. Include rationale tied to source characteristics, latency needs, and operational complexity. Add drawbacks, prerequisites, and a practical implementation checklist with key design decisions and risks. 

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
