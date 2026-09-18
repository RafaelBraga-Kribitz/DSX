# Complex JOIN Patterns *AI Prompt *

Write SQL queries using the correct JOIN type for this analysis. Tables: {{tables}} Relationships: {{relationships}} Question: {{question}} Database: {{database}} 1. JOIN type s... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write SQL queries using the correct JOIN type for this analysis.

Tables: {{tables}}
Relationships: {{relationships}}
Question: {{question}}
Database: {{database}}

1. JOIN type selection:

 INNER JOIN: only rows with matches in BOTH tables
 - Use when: you only want records that have a corresponding record in the other table
 - SELECT o.order_id, c.customer_name FROM orders o INNER JOIN customers c ON o.customer_id = c.id

 LEFT JOIN: ALL rows from the left table, NULLs where no right-table match
 - Use when: you want all records from the left table, with or without a match
 - 'Find all customers and their orders, including customers with no orders'
 - SELECT c.customer_name, COUNT(o.order_id) AS order_count FROM customers c LEFT JOIN orders o ON c.id = o.customer_id GROUP BY c.id

 RIGHT JOIN: ALL rows from the right table (equivalent to LEFT JOIN with tables swapped)
 - Rarely needed; prefer rewriting as a LEFT JOIN for readability

 FULL OUTER JOIN: ALL rows from both tables, NULLs where no match on either side
 - Use when: you need all records from both tables and want to identify unmatched rows on either side
 - 'Find all products and all orders, including products never ordered and orders for deleted products'

 CROSS JOIN: every combination of rows (Cartesian product)
 - Use when: you intentionally want all combinations (date × product for a sales matrix)
 - Warning: 1000 rows × 1000 rows = 1,000,000 rows; always filter the result

 SELF JOIN: a table joined to itself
 - Use when: a table has a self-referential relationship (employee and manager in the same table)
 - SELECT e.name AS employee, m.name AS manager FROM employees e LEFT JOIN employees m ON e.manager_id = m.id

2. Anti-join (find records with NO match):
 SELECT c.customer_id FROM customers c
 LEFT JOIN orders o ON c.id = o.customer_id
 WHERE o.order_id IS NULL;
 -- or equivalently: NOT EXISTS / NOT IN

3. Semi-join (filter by existence without duplicate rows):
 SELECT DISTINCT c.customer_id FROM customers c
 WHERE EXISTS (
 SELECT 1 FROM orders o WHERE o.customer_id = c.id AND o.amount > 100
 );

Return: SQL query using the appropriate JOIN type, explanation of why this JOIN was chosen, and alternative approaches. 
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

The AI should return a structured result that covers the main requested outputs, such as JOIN type selection:, Use when: you only want records that have a corresponding record in the other table, SELECT o.order_id, c.customer_name FROM orders o INNER JOIN customers c ON o.customer_id = c.id. The final answer should stay clear, actionable, and easy to review inside a query fundamentals workflow for sql developer work. 

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
