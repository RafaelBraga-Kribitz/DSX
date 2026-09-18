# Connection Pooling with PgBouncer *AI Prompt *

Configure PgBouncer connection pooling for this PostgreSQL deployment. Max connections PostgreSQL can handle: {{max_connections}} Application connection demand: {{app_connection... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Configure PgBouncer connection pooling for this PostgreSQL deployment.

Max connections PostgreSQL can handle: {{max_connections}}
Application connection demand: {{app_connections}} (peak concurrent connections from app servers)
Workload: {{workload}} (short OLTP transactions vs long-running analytics queries)

1. Why connection pooling:
 - Each PostgreSQL connection consumes ~5-10MB RAM and a process
 - With 500 app server threads each holding an open connection → 500 Postgres processes → OOM
 - PgBouncer maintains a small pool of actual database connections; app connections are multiplexed

2. Pooling modes:

 Session pooling:
 - App connection holds a server connection for its entire lifetime
 - No statement restriction; full PostgreSQL feature support
 - Limited benefit: only helps when connections are idle for long periods

 Transaction pooling (recommended for most OLTP apps):
 - App connection holds a server connection only during a transaction
 - Server connection returned to pool after COMMIT/ROLLBACK
 - 100x reduction in required server connections for typical apps
 - Restriction: prepared statements and advisory locks do not work in transaction mode
 Fix: use named prepared statements via protocol-level support (pgBouncer >= 1.21)

 Statement pooling:
 - Server connection returned after every single statement
 - Most aggressive pooling; does not support multi-statement transactions
 - Use only for read-only single-statement workloads

3. pgbouncer.ini configuration:
 [databases]
 production = host=localhost port=5432 dbname=production

 [pgbouncer]
 pool_mode = transaction
 max_client_conn = 2000
 default_pool_size = 25 # = max_connections / number_of_databases
 min_pool_size = 5
 reserve_pool_size = 5
 server_idle_timeout = 600
 client_idle_timeout = 0

4. Monitoring PgBouncer:
 Connect to the PgBouncer admin: psql -p 6432 pgbouncer
 SHOW POOLS; -- active/waiting clients, server connections
 SHOW STATS; -- requests per second, average query time
 Alert on: cl_waiting > 0 for more than 5 seconds (connection queue building up)

5. PgBouncer in Kubernetes:
 - Deploy as a sidecar or as a shared deployment per database cluster
 - Use environment variable injection for credentials (never hardcode passwords)

Return: pgbouncer.ini configuration, pool size calculation, mode recommendation, and monitoring setup. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin performance tuning work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Performance Tuning or the wider Database Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Why connection pooling:, Each PostgreSQL connection consumes ~5-10MB RAM and a process, With 500 app server threads each holding an open connection → 500 Postgres processes → OOM. The final answer should stay clear, actionable, and easy to review inside a performance tuning workflow for database engineer work. 

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

Once you have the first result, continue deeper with related prompts in Performance Tuning.
