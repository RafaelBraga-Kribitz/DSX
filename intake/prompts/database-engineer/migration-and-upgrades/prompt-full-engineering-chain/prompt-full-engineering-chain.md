# Full Database Engineering Chain *AI Prompt *

Step 1: Schema design - design the normalized relational schema for the domain. Define primary keys, foreign keys, and data types. Create an ERD. Identify tables requiring parti... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Schema design - design the normalized relational schema for the domain. Define primary keys, foreign keys, and data types. Create an ERD. Identify tables requiring partitioning based on expected data volume.
Step 2: Indexing strategy - analyze the query workload. Design B-tree, partial, and covering indexes for the top 10 query patterns. Identify unused index candidates. Document the index maintenance plan.
Step 3: Security hardening - configure pg_hba.conf for certificate or SCRAM authentication. Define the role hierarchy. Enable RLS for multi-tenant tables. Configure pgaudit for compliance logging.
Step 4: Performance configuration - tune postgresql.conf for the server specs (shared_buffers, work_mem, random_page_cost). Configure PgBouncer for connection pooling. Set autovacuum parameters for high-write tables.
Step 5: Replication and HA - configure streaming replication. Set up Patroni for automatic failover. Configure WAL archiving for PITR. Define the backup schedule using pgBackRest.
Step 6: Monitoring - deploy pg_stat_statements for slow query identification. Set up pg_stat_replication lag monitoring. Configure autovacuum bloat alerts. Integrate with the organization's observability stack.
Step 7: Migration and change management - define the zero-downtime migration procedure for schema changes. Create a runbook for major version upgrades. Establish the PR review checklist for database changes. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin migration and upgrades work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Migration and Upgrades or the wider Database Engineer library. 

## What the AI should return 

The AI should return a structured result that is directly usable in a migration and upgrades workflow, with explicit outputs, readable formatting, and enough clarity to support the next step in database engineer work. 

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

Once you have the first result, continue deeper with related prompts in Migration and Upgrades.
