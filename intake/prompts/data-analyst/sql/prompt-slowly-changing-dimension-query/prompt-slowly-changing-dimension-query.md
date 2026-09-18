# Slowly Changing Dimension Query *AI Prompt *

Slowly Changing Dimension Query is a advanced template for sql. This prompt is meant to generate production-usable SQL for analytical tasks. It gives the AI enough direction to build a query that is not only correct, but also readable, structured, and adapted to the database engine or business question. Use it when you want a query you can review, run, and modify with minimal rework. It is structured as a reusable template, so placeholders can be filled in for a specific table, metric, or business context. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write a SQL Type 2 Slowly Changing Dimension (SCD) implementation for the dimension table {{dim_table}} in {{database_type}}.

The table structure uses:
- Natural key: {{natural_key}}
- Tracked attributes that trigger a new version: {{tracked_columns}}
- SCD columns to manage: surrogate_key, valid_from, valid_to, is_current

Write:
1. The CREATE TABLE statement with all required columns
2. The MERGE / UPSERT logic to handle: new records, changed records (expire old, insert new), unchanged records
3. A query to retrieve the current version of each record
4. A query to retrieve the historical version valid at a specific point in time: {{as_of_date}}

Add comments explaining the SCD logic at each step. 
```

## When to use this prompt 
Use case 01 
When you want a query drafted faster than writing it from scratch. 
Use case 02 
When you need SQL that follows a clear analytical structure with comments. 
Use case 03 
When you are working across different databases and need engine-specific wording. 
Use case 04 
When you want a reusable query pattern for profiling, retention, funnels, or forecasting inputs. 

## What the AI should return 

The AI should return a complete SQL query or query set that is ready to review and adapt. It should use comments, readable CTE names, and clear formatting so the logic is easy to follow. If assumptions are required, they should be stated briefly before or after the query. The result should be practical enough that an analyst can copy it into their SQL editor with minimal cleanup. 

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

Once you have the first result, continue deeper with related prompts in SQL.
