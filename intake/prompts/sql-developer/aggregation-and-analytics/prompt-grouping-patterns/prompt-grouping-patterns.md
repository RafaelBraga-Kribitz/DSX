# Grouping and Aggregation Patterns *AI Prompt *

Write SQL aggregation queries to answer these analytical questions. Questions: {{questions}} Tables: {{tables}} Database: {{database}} 1. Standard aggregations: SELECT category,... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write SQL aggregation queries to answer these analytical questions.

Questions: {{questions}}
Tables: {{tables}}
Database: {{database}}

1. Standard aggregations:
 SELECT
 category,
 COUNT(*) AS row_count,
 COUNT(DISTINCT customer_id) AS unique_customers,
 SUM(amount) AS total_amount,
 AVG(amount) AS avg_amount,
 MIN(created_at) AS first_event,
 MAX(created_at) AS last_event,
 PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY amount) AS median_amount
 FROM orders
 GROUP BY category;

2. HAVING vs WHERE:
 WHERE filters rows BEFORE aggregation
 HAVING filters groups AFTER aggregation
 SELECT customer_id, SUM(amount) AS total
 FROM orders
 WHERE created_at >= '2024-01-01' -- filter rows before grouping
 GROUP BY customer_id
 HAVING SUM(amount) > 1000; -- filter groups after aggregation

3. GROUPING SETS for multi-level summaries:
 SELECT region, product, SUM(revenue)
 FROM sales
 GROUP BY GROUPING SETS (
 (region, product), -- subtotal per region+product
 (region), -- subtotal per region
 (product), -- subtotal per product
 () -- grand total
 );

 ROLLUP: hierarchical subtotals (region → product → grand total)
 GROUP BY ROLLUP (region, product)

 CUBE: all possible combinations of groupings
 GROUP BY CUBE (region, product, channel)

4. Conditional aggregation:
 SELECT
 customer_id,
 SUM(CASE WHEN status = 'completed' THEN amount ELSE 0 END) AS completed_revenue,
 SUM(CASE WHEN status = 'refunded' THEN amount ELSE 0 END) AS refunded_revenue,
 COUNT(CASE WHEN status = 'pending' THEN 1 END) AS pending_count
 FROM orders
 GROUP BY customer_id;

5. Filter clause (cleaner than CASE WHEN for filtered aggregations):
 COUNT(*) FILTER (WHERE status = 'completed') AS completed_count,
 SUM(amount) FILTER (WHERE created_at >= CURRENT_DATE - INTERVAL '30 days') AS last_30d_revenue

Return: SQL queries for each analytical question, explanation of GROUPING SETS when multi-level summaries are needed, and conditional aggregation patterns. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin aggregation and analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Aggregation and Analytics or the wider SQL Developer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Standard aggregations:, HAVING vs WHERE:, GROUPING SETS for multi-level summaries:. The final answer should stay clear, actionable, and easy to review inside a aggregation and analytics workflow for sql developer work. 

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

Once you have the first result, continue deeper with related prompts in Aggregation and Analytics.
