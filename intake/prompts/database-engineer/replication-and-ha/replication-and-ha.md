# Replication and HA *AI Prompts *

2 Database Engineer prompts in Replication and HA. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 2 single prompts. 

## AI prompts in Replication and HA 
2 prompts Advanced Single prompt 01 
### Backup and Recovery Strategy 

Design a backup and recovery strategy for this production database. Database size: {{size}} RPO: {{rpo}} RTO: {{rto}} Retention requirement: {{retention}} (30 days, 7 years for... 
Prompt text Design a backup and recovery strategy for this production database.

Database size: {{size}}
RPO: {{rpo}}
RTO: {{rto}}
Retention requirement: {{retention}} (30 days, 7 years for compliance, etc.)
Database: {{database}}

1. Backup types:

 Full backup:
 - Complete copy of the database
 - Slow to create and restore; self-contained
 - Frequency: weekly or daily depending on RPO

 Incremental backup:
 - Only changes since the last full or incremental backup
 - Fast to create; requires chaining backups for restore
 - pgBackRest and Barman support incremental PostgreSQL backups

 WAL archiving (point-in-time recovery):
 - Archive every WAL segment to S3/GCS/Azure Blob
 - Enables recovery to any point in time within the archive window
 - Combined with a base backup: recover to any second
 - archive_mode = on; archive_command = 'pgbackrest --stanza=main archive-push %p'

2. pgBackRest configuration:
 stanza: production
 repo1-path: /var/lib/pgbackrest
 repo1-retention-full: 4 # keep 4 full backups
 repo1-s3-bucket: company-db-backups

 Schedule:
 - Full backup: weekly (Sunday 02:00)
 - Differential backup: daily (02:00 Mon-Sat)
 - WAL archiving: continuous

3. Recovery time estimate:
 - Full restore: depends on backup size and network bandwidth
 - PITR: restore the base backup + replay WAL up to the target time
 - Test restore time regularly: log the time taken in the DR runbook

4. Backup validation (critical — most organizations skip this):
 - Monthly automated restore test: restore to a staging instance, run integrity checks
 - pg_restore --list: verify backup catalog is intact
 - SELECT COUNT(*) on key tables after restore
 - Log validation results; alert if restore fails

5. Offsite and immutable backups:
 - Store backups in a separate cloud region from the primary database
 - Enable S3 Object Lock (WORM) for compliance retention requirements
 - Encrypt backups at rest and in transit

Return: backup schedule, pgBackRest configuration, PITR setup, restore time estimate, and validation automation plan. Copy prompt Open prompt details Intermediate Single prompt 02 
### Replication Setup 

Design a replication and high-availability setup for this PostgreSQL database. RPO requirement: {{rpo}} (maximum acceptable data loss) RTO requirement: {{rto}} (maximum acceptab... 
Prompt text Design a replication and high-availability setup for this PostgreSQL database.

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

Return: replication architecture for the given RPO/RTO, synchronous vs async decision, Patroni configuration, and lag monitoring. Copy prompt Open prompt details 
## Recommended Replication and HA workflow 
1 
### Backup and Recovery Strategy 

Start with a focused prompt in Replication and HA so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Replication Setup 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt
