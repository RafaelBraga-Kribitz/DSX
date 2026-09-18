# BigQuery Optimization *AI Prompt *

Optimize BigQuery performance and cost for this workload. Workload: {{workload}} Current monthly cost: {{current_cost}} Query patterns: {{query_patterns}} Data volume: {{volume}... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Optimize BigQuery performance and cost for this workload.

Workload: {{workload}}
Current monthly cost: {{current_cost}}
Query patterns: {{query_patterns}}
Data volume: {{volume}}

1. BigQuery cost model:
 - On-demand: $5 per TB of data scanned (minimize bytes read)
 - Flat-rate / capacity pricing: reserved slot commitments for predictable workloads
 - Storage: $0.02/GB for active, $0.01/GB for long-term (not modified for 90 days)

2. Reducing bytes scanned:
 - Partition tables by date:
 PARTITION BY DATE(event_timestamp)
 Queries with WHERE event_date BETWEEN ... AND ... only scan relevant partitions

 - Cluster by frequently filtered columns:
 CLUSTER BY user_id, product_category
 Improves scan efficiency for queries filtering on these columns

 - Use INFORMATION_SCHEMA to find expensive queries:
 SELECT total_bytes_billed/POW(1024,3) AS gb_billed, query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 ORDER BY total_bytes_billed DESC LIMIT 20;

3. Schema design for BigQuery:
 - Prefer denormalized (nested and repeated) schemas over normalized schemas
 - Use STRUCT and ARRAY columns to store related data in one row
 - Avoids expensive cross-shard joins on normalized data
 - Nested repeated fields are stored in columnar format → efficient for column scans

4. Materialized views:
 CREATE MATERIALIZED VIEW daily_revenue AS
 SELECT DATE(order_date) AS d, SUM(amount) AS revenue
 FROM orders GROUP BY 1;
 - BigQuery automatically refreshes within 5 minutes of base table changes
 - Queries on the base table can transparently use the materialized view

5. Slot utilization:
 - Monitor: INFORMATION_SCHEMA.JOBS_TIMELINE for slot hours
 - Identify: queries with high slot_ms = compute-intensive (add partitioning)
 - BI Engine: in-memory acceleration for Looker and Looker Studio

Return: partitioning and clustering DDL, cost investigation queries, materialized view setup, and schema design recommendation. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin cloud warehouse work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Cloud Warehouse or the wider Cloud Data Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as BigQuery cost model:, On-demand: $5 per TB of data scanned (minimize bytes read), Flat-rate / capacity pricing: reserved slot commitments for predictable workloads. The final answer should stay clear, actionable, and easy to review inside a cloud warehouse workflow for cloud data engineer work. 

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

Once you have the first result, continue deeper with related prompts in Cloud Warehouse.
