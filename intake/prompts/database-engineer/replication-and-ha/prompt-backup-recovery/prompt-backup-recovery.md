# Backup and Recovery Strategy *AI Prompt *

Design a backup and recovery strategy for this production database. Database size: {{size}} RPO: {{rpo}} RTO: {{rto}} Retention requirement: {{retention}} (30 days, 7 years for... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a backup and recovery strategy for this production database.

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

Return: backup schedule, pgBackRest configuration, PITR setup, restore time estimate, and validation automation plan. 
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

The AI should return a structured result that covers the main requested outputs, such as Backup types:, Complete copy of the database, Slow to create and restore; self-contained. The final answer should stay clear, actionable, and easy to review inside a replication and ha workflow for database engineer work. 

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
