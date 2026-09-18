# Advanced Filtering Patterns *AI Prompt *

Write advanced SQL filtering conditions for these complex requirements. Requirements: {{requirements}} Tables: {{tables}} Database: {{database}} 1. ANY / ALL operators: -- Custo... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write advanced SQL filtering conditions for these complex requirements.

Requirements: {{requirements}}
Tables: {{tables}}
Database: {{database}}

1. ANY / ALL operators:
 -- Customers who ordered every product in a list:
 SELECT customer_id FROM orders
 GROUP BY customer_id
 HAVING array_agg(product_id ORDER BY product_id)
 @> ARRAY[1,2,3]::int[]; -- contains all required products

 -- Value greater than all values in a subquery:
 WHERE amount > ALL(SELECT amount FROM orders WHERE year = 2023)

2. Relational division (find entities meeting ALL criteria):
 -- Find customers who purchased ALL products in a category
 SELECT customer_id
 FROM orders o
 JOIN products p ON o.product_id = p.id
 WHERE p.category = 'Electronics'
 GROUP BY customer_id
 HAVING COUNT(DISTINCT o.product_id) = (
 SELECT COUNT(*) FROM products WHERE category = 'Electronics'
 );

3. Latest record per group (common requirement):
 -- Method 1: ROW_NUMBER
 SELECT * FROM (
 SELECT *, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY updated_at DESC) AS rn
 FROM customer_states
 ) WHERE rn = 1;

 -- Method 2: DISTINCT ON (PostgreSQL)
 SELECT DISTINCT ON (customer_id) *
 FROM customer_states
 ORDER BY customer_id, updated_at DESC;

4. NOT EXISTS vs NOT IN (important difference with NULLs):
 -- NOT IN fails silently if the subquery returns any NULLs
 WHERE id NOT IN (SELECT customer_id FROM blacklist) -- wrong if blacklist has NULLs
 -- NOT EXISTS handles NULLs correctly:
 WHERE NOT EXISTS (SELECT 1 FROM blacklist b WHERE b.customer_id = c.id)

5. Overlapping intervals:
 -- Find all events that overlap with a given time window
 WHERE start_time < :window_end AND end_time > :window_start
 -- Allen's interval overlap condition: two intervals overlap if neither ends before the other starts

Return: SQL for each complex filtering requirement with explanations of edge cases and NULL handling. 
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

The AI should return a structured result that covers the main requested outputs, such as ANY / ALL operators:, Relational division (find entities meeting ALL criteria):, Latest record per group (common requirement):. The final answer should stay clear, actionable, and easy to review inside a query fundamentals workflow for sql developer work. 

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
