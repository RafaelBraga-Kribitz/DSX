# Cloud Cost Management *AI Prompt *

Implement cost monitoring and optimization for this cloud data platform. Provider: {{provider}} Current monthly spend: {{spend}} Main cost drivers: {{cost_drivers}} (compute, st... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement cost monitoring and optimization for this cloud data platform.

Provider: {{provider}}
Current monthly spend: {{spend}}
Main cost drivers: {{cost_drivers}} (compute, storage, data transfer, queries)
Budget: {{budget}}

1. Cost visibility:

 AWS:
 - AWS Cost Explorer: visualize spend by service, tag, and time
 - Enable cost allocation tags: tag every resource with team, environment, project
 - AWS Budgets: set budget alerts at 50%, 80%, 100% of monthly budget
 - AWS Cost and Usage Report (CUR): detailed hourly billing data in S3 for analysis

 GCP:
 - BigQuery Billing export: export billing data to BigQuery for analysis
 - Labels on every resource (equivalent to AWS tags)
 - Budget alerts via Cloud Billing API

 Snowflake:
 - QUERY_HISTORY: identify expensive queries (total_elapsed_time, credits_used_cloud_services)
 - WAREHOUSE_METERING_HISTORY: credits consumed per warehouse
 - Resource monitors: cap spend per warehouse per day/week/month

2. Compute optimization:
 - Use spot/preemptible instances for fault-tolerant batch jobs (70-90% discount)
 - Right-size warehouse clusters: if avg cluster utilization < 30%, downsize
 - Auto-suspend warehouses when idle: 60-second suspension for transient workloads
 - Reserved instances / committed use discounts for stable baseline compute

3. Storage optimization:
 - S3 Intelligent-Tiering: auto-moves objects to cheaper tiers based on access patterns
 - Enforce lifecycle policies: delete temp/staging files after 7 days
 - Columnar formats: Parquet is 5-10x smaller than CSV → less storage and scan cost
 - Compression: snappy or zstd for Parquet (default in most tools)

4. Query cost optimization (BigQuery/Athena/Snowflake):
 - Partition pruning: WHERE clauses on the partition key
 - Column pruning: avoid SELECT *; project only needed columns
 - Result caching: identical queries hit the cache (free in Snowflake/BigQuery)
 - Materialized views: pre-compute expensive aggregations

5. FinOps process:
 - Monthly cost review: top 10 expensive resources, trends, anomalies
 - Showback / chargeback: allocate costs to teams using tags
 - Cost anomaly alerts: alert when spend > 150% of the 7-day rolling average

Return: cost monitoring setup, tagging strategy, compute and storage optimizations, query cost reduction, and FinOps process. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin security and governance work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Security and Governance or the wider Cloud Data Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Cost visibility:, AWS Cost Explorer: visualize spend by service, tag, and time, Enable cost allocation tags: tag every resource with team, environment, project. The final answer should stay clear, actionable, and easy to review inside a security and governance workflow for cloud data engineer work. 

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

Once you have the first result, continue deeper with related prompts in Security and Governance.
