# Date Range and Gap Analysis *AI Prompt *

Date Range and Gap Analysis is a beginner template for sql. This prompt is meant to generate production-usable SQL for analytical tasks. It gives the AI enough direction to build a query that is not only correct, but also readable, structured, and adapted to the database engine or business question. Use it when you want a query you can review, run, and modify with minimal rework. It is structured as a reusable template, so placeholders can be filled in for a specific table, metric, or business context. The requested output should remain approachable and easy to review, even for someone with limited analytical background. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write a SQL query to analyze the date coverage of the table {{table_name}} using the date column {{date_column}} in {{database_type}}.

The query should:
1. Return min date, max date, and total days spanned
2. Count distinct dates present vs expected dates in the range
3. Identify any missing dates (gaps in the sequence)
4. Show the top 5 largest gaps with start date, end date, and gap length in days
5. Count records per month to show data volume over time

Add a comment explaining how to interpret each section. 
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
