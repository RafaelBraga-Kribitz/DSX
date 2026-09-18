# Partitioning Strategy *AI Prompt *

This prompt helps choose partitioning and clustering based on real query behavior and platform-specific capabilities. It is aimed at improving scan efficiency, cost, and maintainability rather than blindly partitioning by date. The answer should connect the physical design to workload patterns and platform constraints. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design the optimal partitioning and clustering strategy for this data warehouse table.

Table: {{table_name}}
Approximate size: {{table_size}}
Query patterns: {{query_patterns}}
Warehouse platform: {{platform}} (BigQuery / Snowflake / Redshift / Databricks / Trino)

1. Partitioning:
 - Partition by the column most frequently used in WHERE filters
 - For time-series data: partition by date (daily partitions for tables < 1TB, monthly for larger)
 - For non-time data: partition by a low-cardinality column (region, status, product_category)
 - Avoid over-partitioning: partitions should be > 100MB each to avoid small-file problems
 - Avoid under-partitioning: each partition should be a meaningful data subset to skip files effectively

2. Clustering / sort keys:
 - After partitioning, cluster by the next most common filter column (e.g. customer_id, product_id)
 - Cluster by columns used in JOIN conditions to collocate related rows
 - For Snowflake: choose cluster keys with high cardinality and low correlation with insert order
 - For BigQuery: cluster up to 4 columns in order of filter frequency
 - For Redshift: SORTKEY on the main time column, DISTKEY on the most common join key

3. Partition pruning validation:
 - Write a test query using EXPLAIN to confirm partition pruning is occurring
 - Alert if a query scans > {{max_scan_ratio}}% of partitions (indicates missing partition filter)

4. Maintenance:
 - For Delta/Iceberg: OPTIMIZE (compaction) and VACUUM (remove deleted files) on a schedule
 - For Redshift: VACUUM and ANALYZE after large loads
 - Monitor partition statistics: flag partitions with unusually high or low row counts

Return: partitioning and clustering DDL, partition pruning test query, and maintenance schedule. 
```

## When to use this prompt 
Use case 01 
When creating or redesigning large warehouse tables. 
Use case 02 
When query costs are high because too much data is scanned. 
Use case 03 
When moving a model to BigQuery, Snowflake, Redshift, or lakehouse tables. 
Use case 04 
When you need both DDL guidance and validation steps. 

## What the AI should return 

Return a recommended partitioning and clustering strategy with platform-aware rationale. Include DDL or pseudo-DDL, a pruning validation query, and a maintenance schedule for compaction or statistics refresh. Explain why the chosen columns fit the stated query patterns and table size. 

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
