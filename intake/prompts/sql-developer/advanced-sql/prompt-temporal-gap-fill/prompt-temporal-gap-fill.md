# Temporal and Gap-Fill Patterns *AI Prompt *

Write SQL for these time series and gap-filling analytical challenges. Problem: {{problem}} Date table or generate_series available: {{date_generation}} Database: {{database}} 1... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write SQL for these time series and gap-filling analytical challenges.

Problem: {{problem}}
Date table or generate_series available: {{date_generation}}
Database: {{database}}

1. Generate a date spine:
 -- PostgreSQL:
 SELECT generate_series('2024-01-01'::date, '2024-12-31'::date, '1 day'::interval)::date AS d;

 -- Snowflake / BigQuery: use a date dimension table or UNNEST(GENERATE_ARRAY(...))

2. Gap-fill (show zero for days with no data):
 WITH date_spine AS (
 SELECT generate_series('2024-01-01'::date, CURRENT_DATE, '1 day')::date AS d
 )
 SELECT
 ds.d AS date,
 COALESCE(SUM(o.amount), 0) AS daily_revenue
 FROM date_spine ds
 LEFT JOIN orders o ON o.created_at::date = ds.d
 GROUP BY ds.d
 ORDER BY ds.d;

3. Running totals and moving averages:
 SELECT
 date,
 daily_revenue,
 SUM(daily_revenue) OVER (ORDER BY date) AS cumulative_revenue,
 AVG(daily_revenue) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS ma_7d
 FROM daily_revenue_series;

4. Find gaps in a sequence (missing IDs or dates):
 SELECT id + 1 AS gap_start,
 next_id - 1 AS gap_end
 FROM (
 SELECT id,
 LEAD(id) OVER (ORDER BY id) AS next_id
 FROM transactions
 ) t
 WHERE next_id > id + 1;

5. Islands problem (consecutive sequences):
 -- Find runs of consecutive active days per user
 WITH numbered AS (
 SELECT user_id, active_date,
 active_date - ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY active_date) * INTERVAL '1 day' AS grp
 FROM user_activity
 )
 SELECT user_id, MIN(active_date) AS streak_start, MAX(active_date) AS streak_end,
 COUNT(*) AS streak_length
 FROM numbered
 GROUP BY user_id, grp
 ORDER BY user_id, streak_start;

Return: SQL for each temporal challenge, gap-fill pattern, running aggregations, and island/gap detection queries. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin advanced sql work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Advanced SQL or the wider SQL Developer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Generate a date spine:, Gap-fill (show zero for days with no data):, Running totals and moving averages:. The final answer should stay clear, actionable, and easy to review inside a advanced sql workflow for sql developer work. 

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

Once you have the first result, continue deeper with related prompts in Advanced SQL.
