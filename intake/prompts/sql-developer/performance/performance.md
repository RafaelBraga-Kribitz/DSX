# Performance *AI Prompts *

2 SQL Developer prompts in Performance. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 2 single prompts. 

## AI prompts in Performance 
2 prompts Advanced Single prompt 01 
### SQL Anti-Patterns Reference 

Identify and fix SQL anti-patterns in this query or codebase. Query or codebase: {{query}} Database: {{database}} 1. Implicit conversion (prevents index use): -- Bad: string lit... 
Prompt text Identify and fix SQL anti-patterns in this query or codebase.

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

Return: identified anti-patterns in the query, refactored versions, and explanation of why each pattern is harmful. Copy prompt Open prompt details Intermediate Single prompt 02 
### SQL Query Optimization Techniques 

Optimize this slow SQL query. Query: {{query}} Database: {{database}} Table sizes: {{table_sizes}} Current runtime: {{runtime}} 1. Diagnosis first: Run EXPLAIN ANALYZE to unders... 
Prompt text Optimize this slow SQL query.

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

Return: optimized query with explanation for each change, expected improvement, and index recommendations. Copy prompt Open prompt details 
## Recommended Performance workflow 
1 
### SQL Anti-Patterns Reference 

Start with a focused prompt in Performance so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### SQL Query Optimization Techniques 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt
