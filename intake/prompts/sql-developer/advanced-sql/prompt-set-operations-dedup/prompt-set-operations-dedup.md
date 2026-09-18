# Set Operations and Deduplication *AI Prompt *

Write SQL for set operations (UNION, INTERSECT, EXCEPT) and deduplication tasks. Problem: {{problem}} Tables: {{tables}} Database: {{database}} 1. Set operations: UNION: all row... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write SQL for set operations (UNION, INTERSECT, EXCEPT) and deduplication tasks.

Problem: {{problem}}
Tables: {{tables}}
Database: {{database}}

1. Set operations:
 UNION: all rows from both queries, removing duplicates
 UNION ALL: all rows including duplicates (faster than UNION when duplicates are acceptable)
 INTERSECT: rows present in BOTH queries
 EXCEPT / MINUS: rows in the first query but NOT in the second

 Find customers who ordered last year but not this year:
 SELECT customer_id FROM orders WHERE EXTRACT(YEAR FROM order_date) = 2023
 EXCEPT
 SELECT customer_id FROM orders WHERE EXTRACT(YEAR FROM order_date) = 2024;

2. Deduplication with ROW_NUMBER:
 -- Keep the most recent version of each customer record
 WITH ranked AS (
 SELECT *,
 ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY updated_at DESC) AS rn
 FROM customers
 )
 SELECT * FROM ranked WHERE rn = 1;

3. DISTINCT ON (PostgreSQL):
 -- Efficient alternative to ROW_NUMBER deduplication
 SELECT DISTINCT ON (customer_id)
 customer_id, name, email, updated_at
 FROM customers
 ORDER BY customer_id, updated_at DESC;

4. Fuzzy deduplication:
 -- Find potential duplicate customers by similarity
 SELECT a.customer_id, b.customer_id,
 SIMILARITY(a.email, b.email) AS email_sim
 FROM customers a
 JOIN customers b ON a.customer_id < b.customer_id
 WHERE SIMILARITY(a.name, b.name) > 0.7
 AND a.zip_code = b.zip_code;
 -- Requires: CREATE EXTENSION pg_trgm;

5. Merge deduplication (upsert):
 INSERT INTO customers (customer_id, name, email, updated_at)
 VALUES (...)
 ON CONFLICT (customer_id)
 DO UPDATE SET
 name = EXCLUDED.name,
 email = EXCLUDED.email,
 updated_at = EXCLUDED.updated_at
 WHERE EXCLUDED.updated_at > customers.updated_at;

Return: SQL for each set operation or deduplication task, DISTINCT ON pattern for PostgreSQL, and upsert pattern. 
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

The AI should return a structured result that covers the main requested outputs, such as Set operations:, Deduplication with ROW_NUMBER:, DISTINCT ON (PostgreSQL):. The final answer should stay clear, actionable, and easy to review inside a advanced sql workflow for sql developer work. 

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
