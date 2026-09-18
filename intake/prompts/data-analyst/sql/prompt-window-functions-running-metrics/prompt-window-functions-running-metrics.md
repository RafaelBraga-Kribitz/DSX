# Running Metrics with Window Functions *AI Prompt *

Running Metrics with Window Functions is a intermediate template for sql. This prompt is meant to generate production-usable SQL for analytical tasks. It gives the AI enough direction to build a query that is not only correct, but also readable, structured, and adapted to the database engine or business question. Use it when you want a query you can review, run, and modify with minimal rework. It is structured as a reusable template, so placeholders can be filled in for a specific table, metric, or business context. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write a SQL query for the table {{table_name}} using window functions to compute:

1. Running total of {{metric}} ordered by {{date_column}}
2. 7-day and 30-day moving average of {{metric}}
3. Rank of each {{entity_column}} by {{metric}} within each {{partition_column}}
4. Each row's {{metric}} as a percentage of its {{partition_column}} total
5. Period-over-period change: vs prior row and vs same period last year

Database: {{database_type}}. Add a comment explaining each window function used. 
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
