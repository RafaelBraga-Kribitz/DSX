# Window Functions *AI Prompt *

Write SQL using window functions to solve this analytical problem. Problem: {{problem}} Table: {{table}} Database: {{database}} 1. Window function syntax: function_name() OVER (... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write SQL using window functions to solve this analytical problem.

Problem: {{problem}}
Table: {{table}}
Database: {{database}}

1. Window function syntax:
 function_name() OVER (
 PARTITION BY column1, column2 -- optional: defines groups
 ORDER BY column3 -- optional: defines order within the window
 ROWS/RANGE BETWEEN ... AND ... -- optional: defines the window frame
 )

2. Ranking functions:
 ROW_NUMBER(): unique sequential number; no ties
 RANK(): same rank for ties; gaps after ties (1,1,3)
 DENSE_RANK(): same rank for ties; no gaps (1,1,2)
 NTILE(n): divide rows into n equal buckets

 Find the top customer per region:
 SELECT * FROM (
 SELECT customer_id, region, total_spend,
 ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_spend DESC) AS rn
 FROM customers
 ) WHERE rn = 1;

3. Aggregate window functions:
 Running total:
 SUM(amount) OVER (PARTITION BY customer_id ORDER BY order_date)

 Running average:
 AVG(amount) OVER (ORDER BY order_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)
 -- 7-day rolling average

 Percentage of total:
 amount / SUM(amount) OVER (PARTITION BY category) AS pct_of_category

4. Lag and Lead (access previous/next rows):
 LAG(metric, 1) OVER (PARTITION BY entity_id ORDER BY date) AS prev_value
 LEAD(metric, 1) OVER (PARTITION BY entity_id ORDER BY date) AS next_value

 Period-over-period change:
 revenue - LAG(revenue, 1) OVER (PARTITION BY product_id ORDER BY month) AS mom_change

5. FIRST_VALUE / LAST_VALUE:
 FIRST_VALUE(status) OVER (PARTITION BY order_id ORDER BY updated_at) AS first_status
 LAST_VALUE(status) OVER (PARTITION BY order_id ORDER BY updated_at
 ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_status
 -- LAST_VALUE requires the frame clause to reach the last row

6. WINDOW clause (reuse window definition):
 SELECT
 order_id,
 SUM(amount) OVER w AS running_total,
 AVG(amount) OVER w AS running_avg
 FROM orders
 WINDOW w AS (PARTITION BY customer_id ORDER BY order_date);

Return: SQL query using the appropriate window function, window frame explanation, and alternative approaches. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin query fundamentals work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Query Fundamentals or the wider SQL Developer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Window function syntax:, Ranking functions:, Aggregate window functions:. The final answer should stay clear, actionable, and easy to review inside a query fundamentals workflow for sql developer work. 

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

Once you have the first result, continue deeper with related prompts in Query Fundamentals.
