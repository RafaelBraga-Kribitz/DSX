# Query Fundamentals *AI Prompts *

4 SQL Developer prompts in Query Fundamentals. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 4 single prompts. 

## AI prompts in Query Fundamentals 
4 prompts Advanced Single prompt 01 
### Advanced Filtering Patterns 

Write advanced SQL filtering conditions for these complex requirements. Requirements: {{requirements}} Tables: {{tables}} Database: {{database}} 1. ANY / ALL operators: -- Custo... 
Prompt text Write advanced SQL filtering conditions for these complex requirements.

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

Return: SQL for each complex filtering requirement with explanations of edge cases and NULL handling. Copy prompt Open prompt details Beginner Single prompt 02 
### Complex JOIN Patterns 

Write SQL queries using the correct JOIN type for this analysis. Tables: {{tables}} Relationships: {{relationships}} Question: {{question}} Database: {{database}} 1. JOIN type s... 
Prompt text Write SQL queries using the correct JOIN type for this analysis.

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

Return: SQL query using the appropriate JOIN type, explanation of why this JOIN was chosen, and alternative approaches. Copy prompt Open prompt details Intermediate Single prompt 03 
### CTEs and Subquery Patterns 

Rewrite this query or problem using CTEs for clarity and identify when to use subqueries vs CTEs. Query or problem: {{query_or_problem}} Database: {{database}} 1. CTE syntax and... 
Prompt text Rewrite this query or problem using CTEs for clarity and identify when to use subqueries vs CTEs.

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

Return: rewritten query using CTEs, recursive CTE if hierarchical data is involved, and performance considerations. Copy prompt Open prompt details Intermediate Single prompt 04 
### Window Functions 

Write SQL using window functions to solve this analytical problem. Problem: {{problem}} Table: {{table}} Database: {{database}} 1. Window function syntax: function_name() OVER (... 
Prompt text Write SQL using window functions to solve this analytical problem.

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

Return: SQL query using the appropriate window function, window frame explanation, and alternative approaches. Copy prompt Open prompt details 
## Recommended Query Fundamentals workflow 
1 
### Advanced Filtering Patterns 

Start with a focused prompt in Query Fundamentals so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Complex JOIN Patterns 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### CTEs and Subquery Patterns 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Window Functions 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
