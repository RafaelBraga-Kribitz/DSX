# Warehouse Design Chain *AI Prompt *

This prompt walks through complete warehouse design, from business questions and source profiling to physical design, loading, testing, and documentation. It is meant for end-to-end modeling efforts where tables, pipelines, and consumers must align. The output should feel like a warehouse design blueprint rather than a disconnected set of notes. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Requirements — identify the business processes to model, the grain of each fact table, the key business questions to answer, and the consumers (BI tools, DS teams, apps).
Step 2: Source analysis — profile each source table: row counts, key columns, update patterns, data quality issues, and join relationships. Identify integration challenges (different customer IDs across systems).
Step 3: Dimensional model design — design the star schema(s): fact tables with grain and measures, dimension tables with attributes and SCD type per column. Draw the ER diagram.
Step 4: Physical design — choose partitioning, clustering, file format, and materialization strategy for each table. Estimate storage size and query cost at expected query volume.
Step 5: Loading design — design the loading pattern for each table: full load vs incremental vs SCD2 merge. Write the key SQL statements.
Step 6: Testing plan — define data quality tests for each table: row count checks, uniqueness, not-null, referential integrity, and business rule validation.
Step 7: Document the warehouse design: data model diagram, table catalog (name, description, grain, owner), loading schedule, SLA, and known limitations. 
```

## When to use this prompt 
Use case 01 
When starting a new warehouse domain or subject area. 
Use case 02 
When translating source systems into curated analytical models. 
Use case 03 
When a design document is needed for implementation planning. 
Use case 04 
When you want one structured response covering model, loads, tests, and documentation. 

## What the AI should return 

Return a staged warehouse design covering requirements, sources, dimensional model, physical design, loading patterns, tests, and documentation. Include fact grains, dimension definitions, file or table layout choices, SQL patterns, and known limitations. The result should support both implementation and review. 

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
