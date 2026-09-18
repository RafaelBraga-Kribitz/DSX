# Delta Lake / Apache Iceberg *AI Prompt *

Implement an open table format (Delta Lake or Apache Iceberg) for ACID transactions on a data lake. Format choice: {{format}} (Delta Lake or Iceberg) Compute engine: {{engine}}... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement an open table format (Delta Lake or Apache Iceberg) for ACID transactions on a data lake.

Format choice: {{format}} (Delta Lake or Iceberg)
Compute engine: {{engine}} (Spark, Trino, Flink, Databricks, BigQuery)
Primary use case: {{use_case}} (upserts, time travel, schema evolution, multi-engine access)

1. Delta Lake vs Iceberg comparison:

 Delta Lake:
 - Best for: Databricks environments, Python/Spark workflows, simpler setup
 - ACID transactions via a JSON transaction log in _delta_log/
 - Strong Spark integration; growing support for other engines
 - Optimize and Z-Order commands for layout optimization

 Apache Iceberg:
 - Best for: multi-engine environments (Spark + Trino + Flink + BigQuery)
 - ACID via metadata tree (manifest files + snapshot files)
 - Better multi-engine support (no engine lock-in)
 - Hidden partitioning: partition scheme can change without rewriting data

2. Core capabilities:

 ACID upserts (MERGE):
 MERGE INTO target USING source ON target.id = source.id
 WHEN MATCHED THEN UPDATE SET *
 WHEN NOT MATCHED THEN INSERT *;

 Time travel:
 -- Read data as of a point in time:
 SELECT * FROM orders TIMESTAMP AS OF '2024-01-15 10:00:00';
 SELECT * FROM orders VERSION AS OF 42; -- specific snapshot ID

 Schema evolution:
 ALTER TABLE orders ADD COLUMN is_flagged BOOLEAN;
 ALTER TABLE orders RENAME COLUMN old_name TO new_name;
 -- Historical data is not rewritten; schema is evolved in the metadata

3. Optimize and compaction (Delta Lake):
 OPTIMIZE orders ZORDER BY (customer_id, order_date);
 -- Reorganizes file layout so related data is co-located for faster queries
 -- Run after bulk writes or on a daily schedule

4. Vacuum (removing old files):
 VACUUM orders RETAIN 168 HOURS; -- delete files older than 7 days
 -- Required to reclaim storage from deleted/updated rows
 -- Note: vacuuming too aggressively removes time travel history

5. Table maintenance schedule:
 - OPTIMIZE: daily, after the main load
 - VACUUM: weekly (retain at least 7 days for time travel)
 - Schema evolution: via PR with impact assessment

Return: format selection rationale, MERGE pattern for upserts, schema evolution DDL, OPTIMIZE configuration, and maintenance schedule. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin cloud storage work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Cloud Storage or the wider Cloud Data Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Delta Lake vs Iceberg comparison:, Best for: Databricks environments, Python/Spark workflows, simpler setup, ACID transactions via a JSON transaction log in _delta_log/. The final answer should stay clear, actionable, and easy to review inside a cloud storage workflow for cloud data engineer work. 

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

Once you have the first result, continue deeper with related prompts in Cloud Storage.
