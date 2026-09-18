# Advanced SQL *AI Prompts *

4 SQL Developer prompts in Advanced SQL. Copy ready-to-use templates and run them in your AI workflow. Covers advanced levels and 3 single prompts · 1 chain. 

## AI prompts in Advanced SQL 
4 prompts Advanced Chain 01 
### Full SQL Development Chain 

Step 1: Requirements analysis - translate the analytical requirement into precise SQL semantics. Define the grain of the output, identify the tables needed, and map each column... 
Prompt text Step 1: Requirements analysis - translate the analytical requirement into precise SQL semantics. Define the grain of the output, identify the tables needed, and map each column in the output to its source column and any required transformations.
Step 2: Query architecture - decide whether to use a single query, CTEs, or multiple queries. Identify window functions, aggregations, or recursive CTEs needed. Sketch the logical flow before writing SQL.
Step 3: Write the query - implement the query using CTEs for each logical step. Add clear comments on each CTE's purpose. Use explicit JOINs (no implicit joins). Handle NULLs explicitly with COALESCE where appropriate.
Step 4: Correctness validation - test with known inputs and expected outputs. Verify: row count matches expectation, aggregations handle NULLs correctly, deduplication is correct, date range logic is inclusive/exclusive as intended.
Step 5: Performance review - run EXPLAIN ANALYZE. Check for Seq Scans on large tables. Identify missing indexes. Rewrite any correlated subqueries as JOINs. Check for implicit type conversions.
Step 6: Documentation - add a header comment with: purpose, inputs, outputs, business rules applied, known limitations, and author. Add inline comments for complex logic. Document any assumptions about data quality.
Step 7: Optimization and handoff - propose indexes needed for production performance. If the query is recurrent, recommend materializing as a view or a scheduled table. Provide a test dataset for regression testing. Copy prompt Open prompt details Advanced Single prompt 02 
### Recursive Hierarchies and Graph SQL 

Write SQL to query hierarchical and graph structures. Structure: {{structure}} (org chart, product categories, bill of materials, network graph) Table: {{table}} Database: {{dat... 
Prompt text Write SQL to query hierarchical and graph structures.

Structure: {{structure}} (org chart, product categories, bill of materials, network graph)
Table: {{table}}
Database: {{database}}

1. Org chart traversal (recursive CTE):
 WITH RECURSIVE hierarchy AS (
 -- Anchor: the root node(s)
 SELECT id, name, manager_id, 0 AS depth,
 ARRAY[id] AS path,
 name::TEXT AS path_string
 FROM employees
 WHERE manager_id IS NULL

 UNION ALL

 -- Recursive member
 SELECT e.id, e.name, e.manager_id, h.depth + 1,
 h.path || e.id,
 h.path_string || ' > ' || e.name
 FROM employees e
 JOIN hierarchy h ON e.manager_id = h.id
 WHERE NOT e.id = ANY(h.path) -- cycle detection
 )
 SELECT * FROM hierarchy ORDER BY path;

2. Finding all descendants of a node:
 WHERE ARRAY[root_node_id] && path -- path contains the root node

3. Closure table pattern (alternative for frequent reads):
 Create a closure_table with columns: ancestor_id, descendant_id, depth
 Pre-compute all ancestor-descendant pairs
 Query: O(1) for finding all descendants — much faster than recursive CTEs on large hierarchies

4. Bill of Materials (multi-level explosion):
 WITH RECURSIVE bom AS (
 SELECT component_id, product_id, quantity, 1 AS level
 FROM bom_raw WHERE product_id = :top_product

 UNION ALL

 SELECT r.component_id, r.product_id, r.quantity * b.quantity, b.level + 1
 FROM bom_raw r
 JOIN bom b ON r.product_id = b.component_id
 )
 SELECT component_id, SUM(quantity) AS total_needed FROM bom GROUP BY 1;

5. Cycle detection:
 -- Track the path as an array; stop if the next node is already in the path
 WHERE NOT next_node_id = ANY(path_array)

6. Path existence query:
 -- Does a path exist from A to B?
 SELECT EXISTS (
 SELECT 1 FROM hierarchy
 WHERE root_id = :start AND id = :end
 );

Return: recursive CTE for the specific hierarchy, cycle detection, closure table DDL for performance-critical use cases, and BOM explosion pattern. Copy prompt Open prompt details Advanced Single prompt 03 
### Set Operations and Deduplication 

Write SQL for set operations (UNION, INTERSECT, EXCEPT) and deduplication tasks. Problem: {{problem}} Tables: {{tables}} Database: {{database}} 1. Set operations: UNION: all row... 
Prompt text Write SQL for set operations (UNION, INTERSECT, EXCEPT) and deduplication tasks.

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

Return: SQL for each set operation or deduplication task, DISTINCT ON pattern for PostgreSQL, and upsert pattern. Copy prompt Open prompt details Advanced Single prompt 04 
### Temporal and Gap-Fill Patterns 

Write SQL for these time series and gap-filling analytical challenges. Problem: {{problem}} Date table or generate_series available: {{date_generation}} Database: {{database}} 1... 
Prompt text Write SQL for these time series and gap-filling analytical challenges.

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

Return: SQL for each temporal challenge, gap-fill pattern, running aggregations, and island/gap detection queries. Copy prompt Open prompt details 
## Recommended Advanced SQL workflow 
1 
### Full SQL Development Chain 

Start with a focused prompt in Advanced SQL so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Recursive Hierarchies and Graph SQL 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Set Operations and Deduplication 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Temporal and Gap-Fill Patterns 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
