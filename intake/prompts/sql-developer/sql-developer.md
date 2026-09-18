# SQL Developer *AI Prompts *

SQL Developer AI prompt library with 16 prompts in 5 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 5 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse SQL Developer prompt categories 
5 categories 
### Advanced SQL 

AI prompts for advanced SQL techniques including window functions, CTE patterns, recursive queries, and robust analytical query design. 
4 prompts Full SQL Development Chain Recursive Hierarchies and Graph SQL → 
### Query Fundamentals 

AI prompts for SQL query fundamentals including filtering, joins, grouping, and clean query structure for reliable analytical outcomes. 
4 prompts Advanced Filtering Patterns Complex JOIN Patterns → 
### Aggregation and Analytics 

AI prompts for aggregation and analytics workflows, including grouped metrics, cohort aggregations, and business KPI computation patterns. 
3 prompts Cohort and Funnel Analysis in SQL Grouping and Aggregation Patterns → 
### Data Transformation 

AI prompts for data transformation workflows including normalization, enrichment, business logic implementation, and reproducible transformations. 
3 prompts Data Cleaning in SQL Pivoting and Unpivoting Data → 
### Performance 

AI prompts for performance optimization, including bottleneck detection, throughput improvement, latency reduction, and resource efficiency tuning. 
2 prompts SQL Anti-Patterns Reference SQL Query Optimization Techniques → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 16 Advanced SQL 4 Query Fundamentals 4 Aggregation and Analytics 3 Data Transformation 3 Performance 2 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **16 **of 16 prompts 
## Advanced SQL 
4 prompt s Advanced SQL Advanced Chain 01 
### Full SQL Development Chain 
Step 1: Requirements analysis - translate the analytical requirement into precise SQL semantics. Define the grain of the output, identify the tables needed, and map each column in the output to its source column and any required transformations.
Step 2: Query architecture - decide whether to use a single query, CTEs, or multiple queries. Identify window functions, aggregations, or recursive CTEs needed. Sketch the logical flow before writing SQL.
Step 3: Write the query - implement the query using CTEs for each logical step. Add clear comments on each CTE's purpose. Use explicit JOINs (no implicit joins). Handle NULLs explicitly with COALESCE where appropriate.
Step 4: Correctness validation - test with known inputs and expected outputs. Verify: row count matches expectation, aggregations handle NULLs correctly, deduplication is correct, date range logic is inclusive/exclusive as intended.
Step 5: Performance review - run EXPLAIN ANALYZE. Check for Seq Scans on large tables. Identify missing indexes. Rewrite any correlated subqueries as JOINs. Check for implicit type conversions.
Step 6: Documentation - add a header comment with: purpose, inputs, outputs, business rules applied, known limitations, and author. Add inline comments for complex logic. Document any assumptions about data quality.
Step 7: Optimization and handoff - propose indexes needed for production performance. If the query is recurrent, recommend materializing as a view or a scheduled table. Provide a test dataset for regression testing. Copy prompt View page Show more ↓ Advanced SQL Advanced Prompt 02 
### Recursive Hierarchies and Graph SQL 
Write SQL to query hierarchical and graph structures.

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

Return: recursive CTE for the specific hierarchy, cycle detection, closure table DDL for performance-critical use cases, and BOM explosion pattern. Copy prompt View page Show more ↓ Advanced SQL Advanced Prompt 03 
### Set Operations and Deduplication 
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

Return: SQL for each set operation or deduplication task, DISTINCT ON pattern for PostgreSQL, and upsert pattern. Copy prompt View page Show more ↓ Advanced SQL Advanced Prompt 04 
### Temporal and Gap-Fill Patterns 
Write SQL for these time series and gap-filling analytical challenges.

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

Return: SQL for each temporal challenge, gap-fill pattern, running aggregations, and island/gap detection queries. Copy prompt View page Show more ↓ 
## Query Fundamentals 
4 prompt s Query Fundamentals Advanced Prompt 01 
### Advanced Filtering Patterns 
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

Return: SQL for each complex filtering requirement with explanations of edge cases and NULL handling. Copy prompt View page Show more ↓ Query Fundamentals Beginner Prompt 02 
### Complex JOIN Patterns 
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

Return: SQL query using the appropriate JOIN type, explanation of why this JOIN was chosen, and alternative approaches. Copy prompt View page Show more ↓ Query Fundamentals Intermediate Prompt 03 
### CTEs and Subquery Patterns 
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

Return: rewritten query using CTEs, recursive CTE if hierarchical data is involved, and performance considerations. Copy prompt View page Show more ↓ Query Fundamentals Intermediate Prompt 04 
### Window Functions 
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

Return: SQL query using the appropriate window function, window frame explanation, and alternative approaches. Copy prompt View page Show more ↓ 
## Aggregation and Analytics 
3 prompt s Aggregation and Analytics Advanced Prompt 01 
### Cohort and Funnel Analysis in SQL 
Write SQL to perform cohort retention analysis and funnel analysis.

Event table: {{event_table}}
User table: {{user_table}}
Cohort definition: {{cohort}} (acquisition month, first purchase date, etc.)
Database: {{database}}

1. Cohort retention matrix:

 WITH user_cohorts AS (
 -- Assign each user to a cohort based on their first activity
 SELECT user_id,
 DATE_TRUNC('month', MIN(event_date)) AS cohort_month
 FROM events
 GROUP BY user_id
 ),
 user_activity AS (
 -- Find each user's activity by month
 SELECT e.user_id,
 DATE_TRUNC('month', e.event_date) AS activity_month,
 c.cohort_month,
 EXTRACT(EPOCH FROM DATE_TRUNC('month', e.event_date) - c.cohort_month)
 / (30 * 24 * 3600) AS month_number
 FROM events e
 JOIN user_cohorts c USING (user_id)
 )
 SELECT
 cohort_month,
 month_number,
 COUNT(DISTINCT user_id) AS retained_users,
 COUNT(DISTINCT user_id) / FIRST_VALUE(COUNT(DISTINCT user_id))
 OVER (PARTITION BY cohort_month ORDER BY month_number) AS retention_rate
 FROM user_activity
 GROUP BY cohort_month, month_number
 ORDER BY cohort_month, month_number;

2. Funnel analysis (ordered step completion):

 WITH funnel_steps AS (
 SELECT user_id,
 MIN(CASE WHEN event_name = 'signup' THEN event_time END) AS step1_time,
 MIN(CASE WHEN event_name = 'onboarding_complete' THEN event_time END) AS step2_time,
 MIN(CASE WHEN event_name = 'first_purchase' THEN event_time END) AS step3_time
 FROM events
 GROUP BY user_id
 )
 SELECT
 COUNT(*) AS entered_funnel,
 COUNT(step2_time) AS completed_step2,
 COUNT(step3_time) AS completed_step3,
 ROUND(COUNT(step2_time)::NUMERIC / COUNT(*) * 100, 1) AS step1_to_step2_pct,
 ROUND(COUNT(step3_time)::NUMERIC / NULLIF(COUNT(step2_time),0) * 100, 1) AS step2_to_step3_pct
 FROM funnel_steps
 WHERE step1_time IS NOT NULL;

3. Ordered funnel (steps must occur in sequence):
 Add: AND step2_time > step1_time AND step3_time > step2_time
 to enforce that steps happened in the correct order.

Return: cohort retention matrix SQL, funnel analysis SQL, ordered funnel variant, and a description of how to pivot the cohort matrix for a heatmap. Copy prompt View page Show more ↓ Aggregation and Analytics Intermediate Prompt 02 
### Grouping and Aggregation Patterns 
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

Return: SQL queries for each analytical question, explanation of GROUPING SETS when multi-level summaries are needed, and conditional aggregation patterns. Copy prompt View page Show more ↓ Aggregation and Analytics Advanced Prompt 03 
### Statistical Aggregations in SQL 
Write SQL to compute statistical measures and distributions.

Analysis: {{analysis}}
Data: {{data_description}}
Database: {{database}}

1. Descriptive statistics:
 SELECT
 COUNT(*) AS n,
 AVG(amount) AS mean,
 STDDEV(amount) AS std_dev,
 VARIANCE(amount) AS variance,
 MIN(amount) AS min_val,
 MAX(amount) AS max_val,
 PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY amount) AS p25,
 PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY amount) AS median,
 PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY amount) AS p75,
 PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY amount) AS p95,
 PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY amount) AS p99
 FROM orders;

2. Correlation:
 SELECT CORR(x_column, y_column) AS pearson_r FROM metrics;
 -- Values: -1 (perfect negative), 0 (no correlation), 1 (perfect positive)

3. Histogram buckets:
 SELECT
 FLOOR(amount / 100) * 100 AS bucket_start,
 COUNT(*) AS count
 FROM orders
 GROUP BY 1
 ORDER BY 1;
 -- Groups amounts into buckets of 100: 0-100, 100-200, etc.

 WIDTH_BUCKET function:
 SELECT
 WIDTH_BUCKET(amount, 0, 5000, 10) AS bucket, -- 10 equal-width buckets from 0 to 5000
 COUNT(*)
 FROM orders
 GROUP BY bucket;

4. Regression (simple linear):
 SELECT
 REGR_SLOPE(y, x) AS slope,
 REGR_INTERCEPT(y, x) AS intercept,
 REGR_R2(y, x) AS r_squared
 FROM data_points;

5. Mode (most frequent value):
 SELECT MODE() WITHIN GROUP (ORDER BY product_category) AS most_common_category
 FROM orders;

6. Distribution comparison (KS test proxy):
 -- Compare two distributions by percentile
 SELECT percentile, group_a_value, group_b_value,
 ABS(group_a_value - group_b_value) AS diff
 FROM (
 SELECT unnest(array[0.1,0.25,0.5,0.75,0.9]) AS percentile,
 PERCENTILE_CONT(p) WITHIN GROUP (ORDER BY amount) AS val_a,
 PERCENTILE_CONT(p) WITHIN GROUP (ORDER BY amount) AS val_b
 -- ... group by condition
 );

Return: complete statistical analysis SQL, histogram bucketing, correlation, and regression queries. Copy prompt View page Show more ↓ 
## Data Transformation 
3 prompt s Data Transformation Intermediate Prompt 01 
### Data Cleaning in SQL 
Write SQL to clean and standardize this dirty dataset.

Issues identified: {{issues}} (nulls, duplicates, format inconsistencies, outliers, invalid values)
Table: {{table}}
Database: {{database}}

1. NULL handling:
 COALESCE(column, default_value): return first non-null value
 NULLIF(column, 0): convert 0 (or empty string) to NULL
 IS NULL / IS NOT NULL: never use = NULL

 Replace NULL with 'Unknown':
 COALESCE(status, 'Unknown') AS status

 NULL-safe comparison:
 WHERE status IS DISTINCT FROM 'cancelled'
 -- equivalent to: WHERE status != 'cancelled' OR status IS NULL

2. String standardization:
 Remove extra whitespace: REGEXP_REPLACE(name, '\s+', ' ', 'g')
 Normalize email: TRIM(LOWER(email))
 Extract only digits: REGEXP_REPLACE(phone, '[^0-9]', '', 'g')
 Standardize state codes: UPPER(TRIM(state))

3. Date standardization:
 -- Handle multiple date formats in one column (PostgreSQL):
 CASE
 WHEN raw_date ~ '^\d{4}-\d{2}-\d{2}$' THEN raw_date::date
 WHEN raw_date ~ '^\d{2}/\d{2}/\d{4}$' THEN TO_DATE(raw_date, 'MM/DD/YYYY')
 ELSE NULL
 END AS clean_date

4. Outlier detection and flagging:
 -- Flag values more than 3 standard deviations from the mean
 SELECT *,
 ABS(amount - AVG(amount) OVER ()) / NULLIF(STDDEV(amount) OVER (), 0) AS z_score
 FROM transactions
 WHERE ABS(amount - AVG(amount) OVER ()) / NULLIF(STDDEV(amount) OVER (), 0) > 3;

5. Invalid value replacement:
 CASE
 WHEN age < 0 OR age > 120 THEN NULL
 ELSE age
 END AS cleaned_age

6. Data profiling queries:
 -- Column completeness
 SELECT
 COUNT(*) AS total_rows,
 COUNT(email) AS non_null_email,
 COUNT(DISTINCT email) AS unique_emails,
 SUM(CASE WHEN email ~ '^[^@]+@[^@]+\.[^@]+$' THEN 0 ELSE 1 END) AS invalid_emails
 FROM users;

Return: SQL cleaning queries for each identified issue, data profiling queries for quality assessment, and update statements to persist the cleaned values. Copy prompt View page Show more ↓ Data Transformation Advanced Prompt 02 
### Pivoting and Unpivoting Data 
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

Return: pivot SQL for the specific data, unpivot SQL if needed, and dynamic pivot approach if the column values are dynamic. Copy prompt View page Show more ↓ Data Transformation Intermediate Prompt 03 
### String and Date Manipulation 
Write SQL for these string parsing and date calculation tasks.

Tasks: {{tasks}}
Database: {{database}}

1. String functions:
 CONCAT / ||: concatenate strings
 SUBSTRING(text, start, length): extract substring
 REGEXP_REPLACE(text, pattern, replacement): replace with regex
 SPLIT_PART(text, delimiter, part): split and extract nth part
 TRIM / LTRIM / RTRIM: remove whitespace or characters
 LOWER / UPPER: normalize case
 REGEXP_MATCHES: extract all regex captures

 Email domain extraction:
 SPLIT_PART(email, '@', 2) AS email_domain

 Normalize phone number:
 REGEXP_REPLACE(phone, '[^0-9]', '', 'g') AS clean_phone

2. Date functions:
 DATE_TRUNC('month', timestamp): truncate to month start
 DATE_PART('year', timestamp): extract year
 EXTRACT(DOW FROM timestamp): day of week (0=Sunday)
 CURRENT_DATE, NOW()

 Days between two dates:
 (end_date::date - start_date::date) AS days_elapsed

 First day of next month:
 DATE_TRUNC('month', CURRENT_DATE) + INTERVAL '1 month'

 Age in complete years:
 DATE_PART('year', AGE(birth_date)) AS age_years

3. Interval arithmetic:
 created_at + INTERVAL '30 days' AS trial_end
 WHERE event_date BETWEEN CURRENT_DATE - INTERVAL '7 days' AND CURRENT_DATE

4. Time zone handling:
 event_timestamp AT TIME ZONE 'UTC' AT TIME ZONE 'America/New_York' AS local_time
 -- Always store timestamps in UTC; convert on display only

5. JSON extraction (PostgreSQL):
 properties->>'user_id' AS user_id -- text extraction
 (properties->>'amount')::NUMERIC AS amount -- cast to numeric
 properties @> '{"plan": "premium"}' -- containment check
 JSONB_ARRAY_ELEMENTS(properties->'items') -- expand array

Return: SQL for each transformation task with inline comments explaining the function used. Copy prompt View page Show more ↓ 
## Performance 
2 prompt s Performance Advanced Prompt 01 
### SQL Anti-Patterns Reference 
Identify and fix SQL anti-patterns in this query or codebase.

Query or codebase: {{query}}
Database: {{database}}

1. Implicit conversion (prevents index use):
 -- Bad: string literal with integer column
 WHERE user_id = '12345'
 -- Fix: match types
 WHERE user_id = 12345

2. Leading wildcard (prevents index use):
 WHERE name LIKE '%smith%' -- full table scan
 -- Fix: use full-text search or trigram index
 WHERE name ILIKE 'smith%' -- trailing wildcard can use index
 -- Or: CREATE INDEX ON users USING GIN (name gin_trgm_ops);

3. COUNT(DISTINCT) on large tables:
 -- Exact distinct count is expensive; consider HyperLogLog approximation:
 SELECT hll_cardinality(hll_add_agg(hll_hash_integer(user_id))) FROM events;
 -- Requires: hll extension; ~2% error, 100x faster

4. OR conditions that prevent index use:
 WHERE country = 'US' OR country = 'UK' -- may or may not use index
 -- Fix: rewrite as IN:
 WHERE country IN ('US', 'UK')

5. DISTINCT as a performance crutch:
 SELECT DISTINCT customer_id FROM orders -- signals a bad query (probably a bad JOIN)
 -- Fix: investigate why duplicates appear; fix the join instead

6. Non-sargable predicates:
 WHERE YEAR(created_at) = 2024 -- function on column = no index use
 WHERE created_at >= '2024-01-01' AND created_at < '2025-01-01' -- sargable

7. Storing comma-separated lists:
 WHERE tags LIKE '%finance%' -- impossible to index; violates 1NF
 -- Fix: normalize to a separate tags table

8. Using OFFSET for deep pagination:
 SELECT * FROM orders LIMIT 20 OFFSET 100000 -- scans and discards 100,000 rows
 -- Fix: keyset pagination
 SELECT * FROM orders WHERE id > :last_seen_id ORDER BY id LIMIT 20

Return: identified anti-patterns in the query, refactored versions, and explanation of why each pattern is harmful. Copy prompt View page Show more ↓ Performance Intermediate Prompt 02 
### SQL Query Optimization Techniques 
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

Return: optimized query with explanation for each change, expected improvement, and index recommendations. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
- Terms of Service 
- Privacy Policy 
- AI Policy 
- Licenses 
### AI Data Analysis Examples 

- LLM Benchmark on AI Data Analysis 
- Air Passengers Forecast 
- Iris Classification 
- Customer Churn Prediction 
- Energy Consumption Forecast 
### Resources 

- Example Python notebooks 
- Fix ModuleNotFoundError 
- Glossary 
- Brand 
- Answers 
- ML Algorithm Comparison 
- Research 
- Solutions 
### Products 

- MLJAR Studio 
- MLJAR AutoML 
- AI Data Analyst 
- AutoLab Experiments 
- Mercury 
### Tutorials 

- AutoML in Python: Beginner Tutorial with House Prices 
### Open Source 

- MLJAR AutoML 
- Mercury 
- More ... 
### AI Prompts 

- Prompts for Data Professionals 
- Data Analyst prompts 
- Business Analyst prompts 
- Data Scientist prompts 
- ML Engineer prompts 
- Data Engineer prompts 
- MLOps prompts 
### Compare 

- MLJAR Studio vs Julius 
- MLJAR Studio vs H2O 
- MLJAR Studio vs DataRobot 
- MLJAR Studio vs Jupyter 
- MLJAR Studio vs ChatGPT 
- MLJAR Studio vs Cursor 
### Company 

- Contact us 
- Services 
- About us 
- Blog Made by MLJAR. All rights reserved. Created in 🇵🇱 We ❤ you! 
We collect traffic information to improve the site. 

Data is collected in a privacy-friendly way (IP anonymization, no ads, no cross-site tracking). 
Analytics are only enabled if you accept. 
Read Privacy Policy Reject Accept
