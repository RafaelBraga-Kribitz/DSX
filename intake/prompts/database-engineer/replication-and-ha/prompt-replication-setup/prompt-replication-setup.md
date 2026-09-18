# Replication Setup *AI Prompt *

Design a replication and high-availability setup for this PostgreSQL database. RPO requirement: {{rpo}} (maximum acceptable data loss) RTO requirement: {{rto}} (maximum acceptab... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a replication and high-availability setup for this PostgreSQL database.

RPO requirement: {{rpo}} (maximum acceptable data loss)
RTO requirement: {{rto}} (maximum acceptable downtime)
Read scaling needed: {{read_scaling}} (yes/no)
Cloud provider: {{cloud}}

1. Replication types:

 Physical (streaming) replication:
 - Copies WAL (Write-Ahead Log) byte-for-byte from primary to standby
 - Standby is an exact replica at the byte level
 - Synchronous mode: primary waits for standby to confirm WAL receipt before committing (RPO = 0)
 - Asynchronous mode: primary does not wait (small data loss risk; better performance)

 Logical replication:
 - Replicates logical changes (INSERT/UPDATE/DELETE) via the publication/subscription model
 - Can replicate specific tables or schemas
 - Allows different PostgreSQL versions between publisher and subscriber
 - Use for: selective replication, zero-downtime migrations, cross-version upgrades

2. Synchronous vs asynchronous:
 synchronous_standby_names = 'ANY 1 (standby1, standby2)'
 - Synchronous: guarantees RPO=0 but adds latency to every write
 - Asynchronous: no write latency penalty; potential for a small amount of data loss
 - Choice: financial / healthcare data → synchronous; acceptable small RPO → asynchronous

3. Automatic failover with Patroni:
 - Patroni: open-source HA solution using etcd/Consul/ZooKeeper for leader election
 - Automatically promotes the most up-to-date standby when the primary fails
 - Provides: REST API for cluster status, automatic primary registration with load balancer
 - Managed alternatives: AWS RDS Multi-AZ, GCP Cloud SQL HA, Azure Flexible Server

4. Read replica routing:
 - Direct read-heavy queries (reporting, analytics) to standby replicas
 - Use PgBouncer or application-level routing to send reads to replicas
 - Caution: replica lag means reads may see slightly stale data

5. Monitoring replication lag:
 SELECT
 client_addr,
 state,
 sent_lsn,
 replay_lsn,
 (sent_lsn - replay_lsn) AS lag_bytes
 FROM pg_stat_replication;
 Alert if lag_bytes > threshold.

Return: replication architecture for the given RPO/RTO, synchronous vs async decision, Patroni configuration, and lag monitoring. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin replication and ha work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Replication and HA or the wider Database Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Replication types:, Copies WAL (Write-Ahead Log) byte-for-byte from primary to standby, Standby is an exact replica at the byte level. The final answer should stay clear, actionable, and easy to review inside a replication and ha workflow for database engineer work. 

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

Once you have the first result, continue deeper with related prompts in Replication and HA.
