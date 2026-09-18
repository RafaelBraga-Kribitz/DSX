# Database Version Upgrade *AI Prompt *

Plan a major PostgreSQL version upgrade for this production system. Current version: {{current_version}} Target version: {{target_version}} Database size: {{size}} RPO: {{rpo}}... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Plan a major PostgreSQL version upgrade for this production system.

Current version: {{current_version}}
Target version: {{target_version}}
Database size: {{size}}
RPO: {{rpo}}
Upgrade method: {{method}} (pg_upgrade, logical replication, dump/restore)

1. Upgrade methods comparison:

 pg_upgrade (in-place, fast):
 - Upgrades the data directory in-place (or with hard links for near-instant speed)
 - Downtime: 5-30 minutes for most databases
 - Process: pg_upgrade --old-datadir --new-datadir --old-bindir --new-bindir --link
 - Requires: stop the old cluster, upgrade, start the new cluster
 - Rollback: keep the old data directory until validated (can revert in minutes)

 Logical replication (minimal downtime):
 - Set up logical replication from old version to new version instance
 - Wait for replicas to catch up, then switch over
 - Cutover window: 30-60 seconds (stop app, wait for lag to drain, update connection string)
 - Limitation: logical replication does not replicate DDL or sequences automatically

 Dump and restore (safest, most downtime):
 - pg_dump → transfer → pg_restore on new version
 - Downtime: proportional to database size (hours for large databases)
 - Best for: small databases or when a long maintenance window is acceptable

2. Pre-upgrade checklist:
 ☐ Test on a clone: run the upgrade on a copy of production first
 ☐ Review extension compatibility: all extensions must have versions for the target PostgreSQL version
 ☐ Check pg_upgrade --check: dry run without actually upgrading
 ☐ Verify application compatibility: any deprecated functions or behaviors in the new version?
 ☐ Update statistics: run ANALYZE on the new cluster after pg_upgrade before opening to traffic
 ☐ Rebuild indexes: pg_upgrade preserves indexes but recommend REINDEX for safety

3. Cutover plan:
 T-2h: disable application writes (maintenance mode)
 T-1h: final sync check if using logical replication
 T-0: run pg_upgrade; start new cluster; verify; update connection strings
 T+15m: re-enable application writes; monitor for errors
 T+24h: if stable, remove old cluster and backup files

4. Rollback plan:
 - Keep old cluster stopped but intact for 24 hours post-upgrade
 - Rollback: stop new cluster, restart old cluster, update connection strings

Return: upgrade method recommendation, step-by-step plan, pre-upgrade checklist, cutover procedure, and rollback plan. 
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

The AI should return a structured result that covers the main requested outputs, such as Upgrade methods comparison:, Upgrades the data directory in-place (or with hard links for near-instant speed), Downtime: 5-30 minutes for most databases. The final answer should stay clear, actionable, and easy to review inside a migration and upgrades workflow for database engineer work. 

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
