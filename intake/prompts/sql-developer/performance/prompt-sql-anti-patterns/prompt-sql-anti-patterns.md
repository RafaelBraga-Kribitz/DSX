# SQL Anti-Patterns Reference *AI Prompt *

Identify and fix SQL anti-patterns in this query or codebase. Query or codebase: {{query}} Database: {{database}} 1. Implicit conversion (prevents index use): -- Bad: string lit... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: identified anti-patterns in the query, refactored versions, and explanation of why each pattern is harmful. 
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

The AI should return a structured result that covers the main requested outputs, such as Implicit conversion (prevents index use):, Leading wildcard (prevents index use):, COUNT(DISTINCT) on large tables:. The final answer should stay clear, actionable, and easy to review inside a performance workflow for sql developer work. 

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
