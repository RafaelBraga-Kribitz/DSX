# Data Lineage Tracking *AI Prompt *

This prompt designs lineage tracking so teams can understand how data moves from source columns through transformations into analytical outputs. It supports impact analysis, root-cause investigation, and compliance questions, especially in platforms with dbt, Spark, and orchestration tools. The answer should treat lineage as an operational capability, not just documentation. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement column-level data lineage tracking for this data platform.

1. Lineage metadata model:
 - Node types: source_system, table, column, transformation, pipeline_run
 - Edge types: table_derives_from, column_derives_from, transformation_reads, transformation_writes
 - Lineage table DDL:
 ```sql
 CREATE TABLE column_lineage (
 target_table VARCHAR,
 target_column VARCHAR,
 source_table VARCHAR,
 source_column VARCHAR,
 transformation_description VARCHAR,
 pipeline_name VARCHAR,
 recorded_at TIMESTAMP
 )
 ```

2. Automated lineage extraction:
 - For dbt: parse dbt's manifest.json — it contains full column-level lineage from ref() and source() calls
 - For Spark SQL: parse the SQL AST to extract table and column references
 - For Airflow DAGs: extract lineage from task input/output datasets (OpenLineage / Marquez)

3. Lineage use cases:
 - Impact analysis: 'if I change this source column, which downstream tables and reports are affected?'
 - Root cause analysis: 'this report column has wrong values — trace back to the source'
 - Compliance: 'which tables contain data derived from PII column X?'

4. Lineage UI (if building custom):
 - Graph visualization: nodes are tables/columns, edges are derivation relationships
 - Search: find all downstream consumers of a given column
 - Highlight path from a source column to a final report metric

5. OpenLineage integration:
 - Emit OpenLineage events from Airflow and Spark jobs
 - Store in Marquez or forward to data catalog (DataHub, Atlan, Alation)

Return: lineage metadata DDL, automated extraction script for dbt, impact analysis query, and PII propagation query. 
```

## When to use this prompt 
Use case 01 
When you need column-level traceability across a data platform. 
Use case 02 
When impact analysis is required before schema changes. 
Use case 03 
When debugging incorrect metrics back to their source. 
Use case 04 
When PII propagation or compliance lineage must be demonstrable. 

## What the AI should return 

Return lineage metadata DDL, extraction approach for the stated tools, and example queries for impact analysis and PII tracing. Include a description of node and edge types and how lineage events are recorded over time. The output should be specific enough to guide a first implementation. 

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

Once you have the first result, continue deeper with related prompts in Data Quality.
