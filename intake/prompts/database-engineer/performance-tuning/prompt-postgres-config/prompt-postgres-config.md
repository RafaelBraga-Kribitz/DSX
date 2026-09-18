# PostgreSQL Configuration Tuning *AI Prompt *

Tune PostgreSQL configuration parameters for this server and workload. Server specs: {{specs}} (RAM, CPU cores, disk type) Workload type: {{workload}} (OLTP, OLAP, mixed, write-... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Tune PostgreSQL configuration parameters for this server and workload.

Server specs: {{specs}} (RAM, CPU cores, disk type)
Workload type: {{workload}} (OLTP, OLAP, mixed, write-heavy)
PostgreSQL version: {{version}}

1. Memory configuration:

 shared_buffers:
 - PostgreSQL's main cache for data pages
 - Set to: 25% of total RAM
 - 32GB RAM → shared_buffers = 8GB

 effective_cache_size:
 - Estimate of total memory available for caching (OS + shared_buffers)
 - Set to: 75% of total RAM (helps the planner make better decisions)
 - Does NOT allocate memory; it's a planning hint

 work_mem:
 - Memory per sort / hash operation (not per connection!)
 - Formula: (Total RAM - shared_buffers) / (max_connections * average_parallel_queries * 2)
 - OLTP: 4-16MB; OLAP: 64-256MB
 - Too high with many connections = OOM; too low = spills to disk

 maintenance_work_mem:
 - Memory for VACUUM, CREATE INDEX, ALTER TABLE
 - Set to: 256MB - 1GB (operations run one at a time)

2. WAL and checkpoints:

 wal_buffers: 64MB (or auto-tuned by default)

 checkpoint_completion_target: 0.9
 - Spread checkpoint I/O over 90% of the checkpoint interval (reduces I/O spikes)

 max_wal_size: 4GB (default 1GB)
 - Allow larger WAL between checkpoints for write-heavy workloads

 wal_level: replica (minimum for streaming replication)

3. Connection management:
 max_connections: 100-200 (not more; use PgBouncer for connection pooling)
 PgBouncer pool_size = 10-20 × CPU cores

4. Query planner:
 random_page_cost: 1.1 for SSD (default 4.0 is for spinning disk)
 effective_io_concurrency: 200 for SSD (default 1)

5. Autovacuum tuning for high-write tables:
 ALTER TABLE orders SET (
 autovacuum_vacuum_scale_factor = 0.01,
 autovacuum_analyze_scale_factor = 0.005
 );
 - Default 20% threshold is too high for large tables; trigger more frequently

Return: postgresql.conf settings for the given server spec and workload, PgBouncer configuration, and autovacuum tuning. 
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

The AI should return a structured result that covers the main requested outputs, such as Memory configuration:, PostgreSQL's main cache for data pages, Set to: 25% of total RAM. The final answer should stay clear, actionable, and easy to review inside a performance tuning workflow for database engineer work. 

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
