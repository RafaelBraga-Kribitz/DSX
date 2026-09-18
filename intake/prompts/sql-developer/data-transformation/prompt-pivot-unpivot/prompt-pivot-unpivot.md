# Pivoting and Unpivoting Data *AI Prompt *

Write SQL to pivot rows to columns and unpivot columns to rows. Source data: {{data_description}} Desired output: {{desired_output}} Database: {{database}} 1. Manual pivot with... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write SQL to pivot rows to columns and unpivot columns to rows.

Source data: {{data_description}}
Desired output: {{desired_output}}
Database: {{database}}

1. Manual pivot with CASE WHEN (works in all databases):
 -- Pivot: rows of (product, month, revenue) → one column per month
 SELECT
 product,
 SUM(CASE WHEN month = 'Jan' THEN revenue ELSE 0 END) AS jan_revenue,
 SUM(CASE WHEN month = 'Feb' THEN revenue ELSE 0 END) AS feb_revenue,
 SUM(CASE WHEN month = 'Mar' THEN revenue ELSE 0 END) AS mar_revenue
 FROM monthly_sales
 GROUP BY product;

2. CROSSTAB (PostgreSQL tablefunc extension):
 CREATE EXTENSION IF NOT EXISTS tablefunc;

 SELECT * FROM CROSSTAB(
 'SELECT product, month, revenue
 FROM monthly_sales
 ORDER BY 1, 2',
 'VALUES (''Jan''),(''Feb''),(''Mar'')'
 ) AS ct(product TEXT, jan NUMERIC, feb NUMERIC, mar NUMERIC);

3. Unpivot: columns to rows (PostgreSQL UNNEST approach):
 -- Transform: one row with jan_rev, feb_rev, mar_rev → 3 rows
 SELECT
 product,
 month_name,
 revenue
 FROM monthly_wide_table,
 LATERAL (
 VALUES
 ('Jan', jan_revenue),
 ('Feb', feb_revenue),
 ('Mar', mar_revenue)
 ) AS t(month_name, revenue);

4. Dynamic pivot (when column values are unknown at query time):
 In SQL this requires dynamic SQL or a two-step approach:
 Step 1: SELECT DISTINCT month FROM monthly_sales → get the list of columns
 Step 2: Build and execute dynamic SQL with EXECUTE in a PL/pgSQL function

5. BigQuery / Snowflake PIVOT syntax:
 -- BigQuery:
 SELECT * FROM monthly_sales
 PIVOT (SUM(revenue) FOR month IN ('Jan', 'Feb', 'Mar'));

 -- Snowflake:
 SELECT * FROM monthly_sales
 PIVOT (SUM(revenue) FOR month IN ('Jan', 'Feb', 'Mar'))
 AS p (product, jan, feb, mar);

Return: pivot SQL for the specific data, unpivot SQL if needed, and dynamic pivot approach if the column values are dynamic. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin data transformation work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Data Transformation or the wider SQL Developer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Manual pivot with CASE WHEN (works in all databases):, CROSSTAB (PostgreSQL tablefunc extension):, Unpivot: columns to rows (PostgreSQL UNNEST approach):. The final answer should stay clear, actionable, and easy to review inside a data transformation workflow for sql developer work. 

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

Once you have the first result, continue deeper with related prompts in Data Transformation.
