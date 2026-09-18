# Medallion Architecture Design *AI Prompt *

This prompt defines Bronze, Silver, and Gold layers in a way that clarifies what belongs in each layer and what quality expectations apply. It is useful when building a lakehouse or modern warehouse platform that needs both raw replayability and curated business-ready outputs. The response should emphasize responsibilities, retention, access, and lineage across layers. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a medallion (Bronze / Silver / Gold) architecture for this data platform.

Data sources: {{source_systems}}
Consumers: {{downstream_consumers}}
Platform: {{platform}}

1. Bronze layer (raw ingest):
 - Store data exactly as received from the source — no transformation, no business logic
 - Schema: source columns + metadata columns (ingested_at, source_file, pipeline_run_id)
 - File format: Parquet or Delta (preserve original data types)
 - Partitioning: by ingestion date (not event date — you want to find what was loaded when)
 - Retention: keep all data indefinitely — Bronze is your audit trail and replay source
 - Access: restricted to data engineers only

2. Silver layer (cleansed, conformed):
 - Clean and standardize: fix types, normalize casing, handle nulls, apply business rules
 - Deduplicate: one row per natural key per valid state
 - Conform: common naming conventions, standard date formats, unified entity IDs across sources
 - Add: valid_from / valid_to for SCD2 entities, data quality score per row
 - Partitioning: by event date (not ingestion date) for time-series data
 - Access: data engineers and data scientists

3. Gold layer (business-ready):
 - Aggregated, joined, and modeled for specific use cases: star schemas, wide flat tables, aggregated metrics
 - Optimized for query performance: partitioned, clustered, materialized
 - Documented: every table and column has a business description
 - Access: analysts, BI tools, applications

4. Cross-layer governance:
 - Lineage: track which Gold tables derive from which Silver, which derives from which Bronze
 - SLA: Bronze = 30 min from source, Silver = 1 hour, Gold = 2 hours
 - Testing: Bronze (schema only), Silver (schema + row counts + nulls), Gold (schema + business rules + reconciliation)

Return: layer definitions, DDL templates for each layer, lineage tracking approach, and SLA commitments. 
```

## When to use this prompt 
Use case 01 
When designing a medallion or lakehouse architecture. 
Use case 02 
When formalizing layer boundaries for a platform team. 
Use case 03 
When you need clear data contracts between raw, cleaned, and curated layers. 
Use case 04 
When onboarding teams to a shared architecture standard. 

## What the AI should return 

Return layer definitions, example DDL templates, partitioning and retention guidance, access expectations, and cross-layer lineage and SLA rules. Explain what transformations belong in Bronze, Silver, and Gold and how testing differs by layer. The result should read like a platform design standard. 

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

Once you have the first result, continue deeper with related prompts in Data Warehouse Patterns.
