# CTEs and Subquery Patterns *AI Prompt *

Rewrite this query or problem using CTEs for clarity and identify when to use subqueries vs CTEs. Query or problem: {{query_or_problem}} Database: {{database}} 1. CTE syntax and... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Rewrite this query or problem using CTEs for clarity and identify when to use subqueries vs CTEs.

Query or problem: {{query_or_problem}}
Database: {{database}}

1. CTE syntax and benefits:
 WITH cte_name AS (
 SELECT ...
 ),
 second_cte AS (
 SELECT ... FROM cte_name
 )
 SELECT * FROM second_cte;

 Benefits: readability (name complex subqueries), reusability within the query, easier debugging (comment out sections)

2. Recursive CTEs (for hierarchical data):
 WITH RECURSIVE org_hierarchy AS (
 -- Anchor: start from the top of the tree
 SELECT employee_id, name, manager_id, 1 AS level
 FROM employees
 WHERE manager_id IS NULL

 UNION ALL

 -- Recursive: join back to the CTE to traverse down
 SELECT e.employee_id, e.name, e.manager_id, h.level + 1
 FROM employees e
 JOIN org_hierarchy h ON e.manager_id = h.employee_id
 )
 SELECT * FROM org_hierarchy ORDER BY level;

 Use for: org charts, category trees, bill of materials, path finding

3. When to use CTE vs subquery:
 CTE: when the logic is complex and needs a name; when used more than once in the query; when you want to debug step by step
 Subquery: for simple one-off filters; when the optimizer may push down predicates better

 PostgreSQL optimization note: CTEs are optimization fences in PostgreSQL < 12 (materializes the result). Use CTE with MATERIALIZED / NOT MATERIALIZED hint in PostgreSQL 12+.

4. Lateral joins as an alternative:
 SELECT c.customer_id, recent.order_id, recent.amount
 FROM customers c
 CROSS JOIN LATERAL (
 SELECT order_id, amount FROM orders
 WHERE customer_id = c.customer_id
 ORDER BY created_at DESC LIMIT 1
 ) AS recent;
 -- LATERAL can reference outer query columns; equivalent to a correlated subquery but more flexible

5. CTE materialization and performance:
 NOT MATERIALIZED: allow the optimizer to inline the CTE
 MATERIALIZED: force the CTE to be executed once and cached
 WITH customer_metrics AS NOT MATERIALIZED (
 SELECT customer_id, COUNT(*) AS order_count FROM orders GROUP BY 1
 )

Return: rewritten query using CTEs, recursive CTE if hierarchical data is involved, and performance considerations. 
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

The AI should return a structured result that covers the main requested outputs, such as CTE syntax and benefits:, Recursive CTEs (for hierarchical data):, When to use CTE vs subquery:. The final answer should stay clear, actionable, and easy to review inside a query fundamentals workflow for sql developer work. 

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
