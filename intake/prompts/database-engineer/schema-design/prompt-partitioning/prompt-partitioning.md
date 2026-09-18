# Partitioning Strategy *AI Prompt *

Design a table partitioning strategy for this large table. Table: {{table}} with estimated {{row_count}} rows, growing at {{growth_rate}} Query patterns: {{query_patterns}} (alw... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a table partitioning strategy for this large table.

Table: {{table}} with estimated {{row_count}} rows, growing at {{growth_rate}}
Query patterns: {{query_patterns}} (always filter by date? by region? by tenant?)
Database: {{database}}

1. Partitioning methods:

 Range partitioning (most common for time-series data):
 - Partition by date range: one partition per month or per year
 - Queries filtering by date only scan relevant partitions (partition pruning)
 - CREATE TABLE orders_2024_q1 PARTITION OF orders
 FOR VALUES FROM ('2024-01-01') TO ('2024-04-01');

 List partitioning:
 - Partition by discrete values: country, region, status, tenant_id
 - FOR VALUES IN ('US', 'CA')
 - Use when: queries always filter on a low-cardinality categorical column

 Hash partitioning:
 - Distribute rows evenly across N partitions based on a hash of a key
 - FOR VALUES WITH (MODULUS 8, REMAINDER 0)
 - Use when: no natural range or list key but want to distribute I/O load

2. PostgreSQL declarative partitioning:
 CREATE TABLE orders (
 order_id BIGINT,
 order_date DATE NOT NULL,
 ...
 ) PARTITION BY RANGE (order_date);

 Automating partition creation:
 - pg_partman: automatically creates and maintains time-based partitions
 - Configure: retention period, pre-creation interval, maintenance job

3. Partition pruning:
 - The planner must be able to eliminate partitions from the query plan
 - Partition pruning requires: the filter condition uses the partition key column directly
 - Verify: EXPLAIN shows 'Partitions: 1 (of N)' rather than scanning all partitions

4. Global indexes on partitioned tables:
 - PostgreSQL: no global indexes across all partitions; each partition has its own indexes
 - Unique constraints must include the partition key
 - Workaround for cross-partition uniqueness: application-level enforcement or a separate lookup table

5. Partition maintenance:
 - Detach old partitions for archival: ALTER TABLE orders DETACH PARTITION orders_2020;
 - Archive to cold storage, then DROP TABLE orders_2020;
 - Automate with pg_partman or a scheduled maintenance procedure

Return: partitioning DDL, partition pruning verification, pg_partman configuration, and maintenance/archival plan. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin schema design work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Schema Design or the wider Database Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Partitioning methods:, Partition by date range: one partition per month or per year, Queries filtering by date only scan relevant partitions (partition pruning). The final answer should stay clear, actionable, and easy to review inside a schema design workflow for database engineer work. 

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

Once you have the first result, continue deeper with related prompts in Schema Design.
