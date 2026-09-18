# SQL Generation Prompt *AI Prompt *

Design a prompt that reliably generates correct SQL from natural language questions about a specific database schema. Database schema: {{schema_definition}} SQL dialect: {{diale... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a prompt that reliably generates correct SQL from natural language questions about a specific database schema.

Database schema: {{schema_definition}}
SQL dialect: {{dialect}} (PostgreSQL / BigQuery / Snowflake / DuckDB)
Target user: {{user_type}} (data analyst / business user / developer)

1. Schema context injection:
 - Include the full DDL for all relevant tables in the prompt
 - Add a brief description above each table: what it represents and its grain
 - Add a brief description of each column that is not self-explanatory
 - Include sample data (3 rows per table) to help the model understand value formats
 - Specify relationships: 'orders.customer_id is a foreign key to customers.id'

2. Dialect-specific instructions:
 - List the dialect-specific functions to use: 'Use DATE_TRUNC for date truncation, not TRUNC'
 - Specify quoting conventions: 'Quote identifiers with double quotes'
 - Specify NULL handling conventions relevant to this dialect

3. SQL style guidelines (for readable, consistent output):
 - SELECT clause: one column per line, aligned
 - Use CTEs (WITH clauses) for multi-step logic, not nested subqueries
 - Always use explicit JOIN syntax, never implicit comma joins
 - Always qualify column names with table aliases when joining multiple tables
 - Add a comment above each CTE explaining what it computes

4. Ambiguity resolution rules:
 - 'When the question is ambiguous about date range, default to the last 30 days'
 - 'When the question asks for top N without specifying N, use 10'
 - 'When a metric could be calculated multiple ways, choose the simplest correct interpretation and add a SQL comment noting the assumption'

5. Error prevention instructions:
 - 'Never use SELECT * in the final output'
 - 'Always add a LIMIT clause when the question does not specify a row count'
 - 'For aggregations, always include GROUP BY for all non-aggregated columns'

6. Output format:
 - Return only the SQL query
 - No explanation unless explicitly asked
 - Add inline SQL comments for any non-obvious logic

Return: the complete SQL generation prompt, 5 test questions ranging from simple to complex, the correct SQL for each, and a rubric for evaluating SQL correctness. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin prompt design for data tasks work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Prompt Design for Data Tasks or the wider Prompts Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Schema context injection:, Include the full DDL for all relevant tables in the prompt, Add a brief description above each table: what it represents and its grain. The final answer should stay clear, actionable, and easy to review inside a prompt design for data tasks workflow for prompts engineer work. 

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

Once you have the first result, continue deeper with related prompts in Prompt Design for Data Tasks.
