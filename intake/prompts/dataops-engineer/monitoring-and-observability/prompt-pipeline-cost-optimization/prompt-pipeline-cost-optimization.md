# Cost Optimization for Data Pipelines *AI Prompt *

Optimize the cost of running these data pipelines. Pipelines: {{pipeline_list}} Current monthly cost: {{cost}} Primary cost drivers: {{drivers}} (compute, query scanning, storag... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Optimize the cost of running these data pipelines.

Pipelines: {{pipeline_list}}
Current monthly cost: {{cost}}
Primary cost drivers: {{drivers}} (compute, query scanning, storage, data transfer)

1. Identify cost drivers:
 - Compute: warehouse/cluster runtime (cloud DW idle time, Spark cluster cost)
 - Query scanning: BigQuery/Athena per-byte pricing
 - Storage: raw data accumulation, no lifecycle policies
 - Data transfer: cross-region or cross-cloud movements

2. Compute optimization:
 - Right-size clusters: monitor CPU and memory utilization; if < 40%, downsize
 - Auto-terminate idle clusters: Databricks clusters auto-terminate after 10 minutes of inactivity
 - Spot/preemptible instances: 70-90% cheaper for fault-tolerant batch jobs
 - Consolidate pipelines: running 10 pipelines per hour is more expensive than 1 pipeline that processes 10 jobs per run

3. Query scanning optimization:
 - Partition pruning: ensure queries include the partition key in WHERE clauses
 - Column pruning: avoid SELECT *; query only required columns
 - Cache: use result caching for repeated identical queries
 - Materialized views: pre-compute expensive aggregations that are queried frequently

4. Storage optimization:
 - Enforce lifecycle policies: delete staging and temp files after 7 days
 - Compress and convert: convert CSV raw files to Parquet (5-10x smaller)
 - Deduplicate: remove exact duplicate files in the landing zone
 - Tiered storage: move cold data to cheaper storage tiers after 90 days

5. Pipeline scheduling optimization:
 - Batch small jobs together: instead of running 20 single-table pipelines, run one multi-table job
 - Shift heavy jobs to off-peak hours (lower spot prices; avoids peak warehouse pricing)
 - Skip runs when source data has not changed (source freshness check before running)

Return: cost breakdown analysis, compute optimization plan, query scanning reduction, storage lifecycle configuration, and scheduling optimization. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin monitoring and observability work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Monitoring and Observability or the wider DataOps Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Identify cost drivers:, Compute: warehouse/cluster runtime (cloud DW idle time, Spark cluster cost), Query scanning: BigQuery/Athena per-byte pricing. The final answer should stay clear, actionable, and easy to review inside a monitoring and observability workflow for dataops engineer work. 

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

Once you have the first result, continue deeper with related prompts in Monitoring and Observability.
