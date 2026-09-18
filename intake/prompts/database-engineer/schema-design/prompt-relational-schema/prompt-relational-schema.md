# Relational Schema Design *AI Prompt *

Design a normalized relational schema for this domain. Domain: {{domain}} Entities described: {{entities}} Key relationships: {{relationships}} Database: {{database}} (PostgreSQ... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a normalized relational schema for this domain.

Domain: {{domain}}
Entities described: {{entities}}
Key relationships: {{relationships}}
Database: {{database}} (PostgreSQL, MySQL, SQL Server, Oracle)

1. Normalization levels:

 1NF (First Normal Form):
 - Atomic values: no repeating groups, no arrays in columns
 - Each column holds a single value
 - Example violation: storing 'tag1,tag2,tag3' in a tags column

 2NF (Second Normal Form):
 - Must be in 1NF
 - No partial dependencies: every non-key column depends on the WHOLE primary key
 - Applies to tables with composite primary keys

 3NF (Third Normal Form):
 - Must be in 2NF
 - No transitive dependencies: non-key columns should not depend on other non-key columns
 - Example violation: storing both zip_code and city in the same table (city depends on zip)

 BCNF (Boyce-Codd Normal Form):
 - Stricter version of 3NF; every determinant must be a candidate key
 - Required for mission-critical schemas

2. Primary key strategy:
 - Surrogate key: auto-incrementing integer or UUID — decouples business logic from identity
 - Natural key: use when the business key is stable and unique (e.g. ISO country code)
 - Composite key: for junction tables (order_id + product_id as PK in order_items)
 - UUID vs SERIAL: UUID is globally unique (good for distributed systems); SERIAL is faster for single-DB

3. Foreign key design:
 - Always create FK constraints: enforces referential integrity at the database level
 - ON DELETE behavior: RESTRICT (default, safest), CASCADE (auto-delete children), SET NULL
 - Index all FK columns: queries joining on FK columns need indexes

4. Column data types:
 - Prefer: TIMESTAMP WITH TIME ZONE (not WITHOUT), NUMERIC for money (not FLOAT), TEXT over VARCHAR(n) in Postgres
 - Avoid: storing dates as VARCHAR, using FLOAT for currency

5. Schema documentation:
 - Add comments to every table and column: COMMENT ON TABLE orders IS '...';
 - Maintain an ERD (Entity Relationship Diagram) in draw.io or dbdiagram.io

Return: normalized schema DDL, primary and foreign key definitions, index recommendations, and ERD description. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin schema design work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Schema Design or the wider Database Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Normalization levels:, Atomic values: no repeating groups, no arrays in columns, Each column holds a single value. The final answer should stay clear, actionable, and easy to review inside a schema design workflow for database engineer work. 

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

Once you have the first result, continue deeper with related prompts in Schema Design.
