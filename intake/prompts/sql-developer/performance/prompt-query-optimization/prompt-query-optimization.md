# SQL Query Optimization Techniques *AI Prompt *

Optimize this slow SQL query. Query: {{query}} Database: {{database}} Table sizes: {{table_sizes}} Current runtime: {{runtime}} 1. Diagnosis first: Run EXPLAIN ANALYZE to unders... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Optimize this slow SQL query.

Query: {{query}}
Database: {{database}}
Table sizes: {{table_sizes}}
Current runtime: {{runtime}}

1. Diagnosis first:
 Run EXPLAIN ANALYZE to understand the query plan before making changes.
 Identify: Seq Scans on large tables, high estimated vs actual row counts, sort operations.

2. Optimization techniques:

 Filter early (predicate pushdown):
 -- Bad: filter after join
 SELECT * FROM orders o JOIN customers c ON o.customer_id = c.id
 WHERE o.created_at > '2024-01-01';
 -- Good: same query but the optimizer should handle this; verify in EXPLAIN

 Avoid functions on indexed columns in WHERE:
 WHERE YEAR(created_at) = 2024 -- prevents index use
 WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31' -- uses index

 Use EXISTS instead of IN for subqueries:
 -- Slow for large subqueries:
 WHERE customer_id IN (SELECT id FROM customers WHERE tier = 'premium')
 -- Often faster:
 WHERE EXISTS (SELECT 1 FROM customers c WHERE c.id = orders.customer_id AND c.tier = 'premium')

 Avoid SELECT *:
 - Retrieves unnecessary columns, increases I/O and memory
 - Select only the columns you need

 Pagination: use keyset instead of OFFSET:
 -- Slow: OFFSET scans and discards N rows
 SELECT * FROM orders ORDER BY id LIMIT 20 OFFSET 10000;
 -- Fast: continue from last seen id
 SELECT * FROM orders WHERE id > 12345 ORDER BY id LIMIT 20;

3. Aggregate optimization:
 - Move aggregation before joins where possible
 - Pre-aggregate in a CTE, then join to the aggregated result

4. Rewriting correlated subqueries:
 -- Correlated: executes once per row (slow)
 SELECT c.*, (SELECT COUNT(*) FROM orders WHERE customer_id = c.id) AS order_count
 FROM customers c;
 -- Better: pre-aggregate and join
 SELECT c.*, COALESCE(o.order_count, 0) AS order_count
 FROM customers c
 LEFT JOIN (SELECT customer_id, COUNT(*) AS order_count FROM orders GROUP BY 1) o
 ON c.id = o.customer_id;

Return: optimized query with explanation for each change, expected improvement, and index recommendations. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin performance work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Performance or the wider SQL Developer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Diagnosis first:, Optimization techniques:, Retrieves unnecessary columns, increases I/O and memory. The final answer should stay clear, actionable, and easy to review inside a performance workflow for sql developer work. 

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

Once you have the first result, continue deeper with related prompts in Performance.
