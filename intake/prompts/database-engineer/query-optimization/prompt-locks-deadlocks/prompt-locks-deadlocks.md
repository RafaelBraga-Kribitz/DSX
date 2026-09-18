# Deadlock and Lock Analysis *AI Prompt *

Diagnose and resolve lock contention and deadlocks in this database. Database: {{database}} Application pattern: {{pattern}} (OLTP, batch processing, mixed) Lock issue: {{issue_... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Diagnose and resolve lock contention and deadlocks in this database.

Database: {{database}}
Application pattern: {{pattern}} (OLTP, batch processing, mixed)
Lock issue: {{issue_description}}

1. How deadlocks occur:
 Transaction A: locks row 1, waits for row 2
 Transaction B: locks row 2, waits for row 1
 → Neither can proceed; the database detects and rolls back one transaction.

2. Diagnosing locks in PostgreSQL:

 Active locks:
 SELECT pid, locktype, relation::regclass, mode, granted, query
 FROM pg_locks
 JOIN pg_stat_activity USING (pid)
 WHERE NOT granted;

 Blocking queries:
 SELECT blocking.pid AS blocking_pid, blocked.pid AS blocked_pid,
 blocking.query AS blocking_query, blocked.query AS blocked_query
 FROM pg_stat_activity blocked
 JOIN pg_stat_activity blocking
 ON blocking.pid = ANY(pg_blocking_pids(blocked.pid))
 WHERE blocked.wait_event_type = 'Lock';

3. Deadlock prevention strategies:

 Consistent lock ordering:
 - Always acquire locks in the same order across all transactions
 - If Transaction A locks customer then order, Transaction B must also lock customer then order

 Minimize lock duration:
 - Do expensive computation BEFORE the transaction, not inside it
 - Hold locks for as short a time as possible

 Use SELECT FOR UPDATE SKIP LOCKED for queue patterns:
 SELECT * FROM job_queue
 WHERE status = 'pending'
 ORDER BY created_at
 LIMIT 1
 FOR UPDATE SKIP LOCKED;
 - Workers pick uncontested jobs without blocking each other

 Reduce transaction scope:
 - Do not perform external API calls inside a transaction
 - Commit early; reopen if needed

4. Lock timeout:
 SET lock_timeout = '5s';
 - Prevents long lock waits from cascading into system-wide slowdowns
 - Raises LockNotAvailable exception; handle in the application with retry logic

5. Advisory locks:
 - Application-level locks without database row locking
 - SELECT pg_advisory_xact_lock(hashtext('job_processing_' || job_id::text));
 - Useful for: distributed mutual exclusion, serializing concurrent background jobs

Return: lock diagnosis queries, deadlock root cause analysis, prevention strategies, and lock timeout configuration. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin query optimization work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Query Optimization or the wider Database Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as How deadlocks occur:, Diagnosing locks in PostgreSQL:, Deadlock prevention strategies:. The final answer should stay clear, actionable, and easy to review inside a query optimization workflow for database engineer work. 

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

Once you have the first result, continue deeper with related prompts in Query Optimization.
