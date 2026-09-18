# Recursive Hierarchies and Graph SQL *AI Prompt *

Write SQL to query hierarchical and graph structures. Structure: {{structure}} (org chart, product categories, bill of materials, network graph) Table: {{table}} Database: {{dat... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: recursive CTE for the specific hierarchy, cycle detection, closure table DDL for performance-critical use cases, and BOM explosion pattern. 
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

The AI should return a structured result that covers the main requested outputs, such as Org chart traversal (recursive CTE):, Finding all descendants of a node:, Closure table pattern (alternative for frequent reads):. The final answer should stay clear, actionable, and easy to review inside a advanced sql workflow for sql developer work. 

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
