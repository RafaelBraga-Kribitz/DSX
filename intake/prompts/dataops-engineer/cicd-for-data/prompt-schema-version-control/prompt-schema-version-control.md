# Schema Version Control *AI Prompt *

Implement schema version control and migration management for this database. Database: {{database}} Migration tool: {{tool}} (Flyway, Liquibase, Alembic, sqitch, dbt contracts)... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement schema version control and migration management for this database.

Database: {{database}}
Migration tool: {{tool}} (Flyway, Liquibase, Alembic, sqitch, dbt contracts)
Change types: {{change_types}} (additive, destructive, data migrations)

1. Schema migration principles:
 - Every schema change is versioned and applied consistently across all environments
 - Changes are irreversible once applied to production; never modify a migration after it runs
 - All changes applied by an automated migration tool, never manually
 - Every migration has a corresponding rollback (or a documented reason why rollback is not possible)

2. Migration file structure (Flyway/Liquibase):
 V001__create_orders_table.sql
 V002__add_status_column.sql
 V003__add_customer_index.sql
 V004__backfill_status_values.sql

 Naming convention: V{version}__{description}.sql
 Version: timestamp or sequential integer

3. Safe migration patterns:
 Additive changes (safe, no downtime):
 - Add a new column (nullable or with a default)
 - Add an index CONCURRENTLY
 - Add a new table

 Destructive changes (require careful handling):
 - Remove a column: use the expand-contract pattern (2 deployments)
 - Rename a column: add new, migrate data, remove old (3 deployments)
 - Change a column type: depends on the type change; most require a rewrite

4. Data migration within schema migrations:
 - Keep DDL migrations separate from data migrations
 - Data migrations can be slow on large tables and may need to be run as separate batch jobs
 - Idempotent data migrations: check if the migration has already been applied before running

5. CI/CD integration:
 - Run migrations in CI against a test database: verify the migration applies cleanly
 - Staging: migrations run automatically on merge
 - Production: migrations run as part of the deployment pipeline; applied before new code is deployed

Return: migration file structure, naming conventions, safe vs destructive migration patterns, and CI/CD integration steps. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin ci/cd for data work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in CI/CD for Data or the wider DataOps Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Schema migration principles:, Every schema change is versioned and applied consistently across all environments, Changes are irreversible once applied to production; never modify a migration after it runs. The final answer should stay clear, actionable, and easy to review inside a ci/cd for data workflow for dataops engineer work. 

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

Once you have the first result, continue deeper with related prompts in CI/CD for Data.
