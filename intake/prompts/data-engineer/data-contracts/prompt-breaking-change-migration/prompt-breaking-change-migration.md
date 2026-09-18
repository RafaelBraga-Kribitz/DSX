# Breaking Change Migration *AI Prompt *

This prompt plans a safe migration path for breaking changes so producers can evolve schemas without abruptly disrupting consumers. It is especially useful when many reports, tables, or applications depend on the affected field or table grain. The response should focus on impact analysis, phased rollout, communication, and rollback options. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a safe migration process for this breaking schema change.

Breaking change: {{change_description}} (e.g. renaming column customer_id to account_id, or changing the grain from order to order_line)
Affected table: {{table_name}}
Known consumers: {{consumer_list}}

1. Impact assessment:
 - Query the data lineage graph to find ALL consumers of the affected table and column
 - For each consumer: team, table/report name, how the breaking column is used, migration effort (Low/Medium/High)
 - Identify any external consumers (APIs, applications) that cannot be migrated centrally

2. Migration strategy: Expand and Contract (strangler fig pattern):
 Phase 1 — Expand (add, don't remove):
 - Add the new column/structure alongside the existing one
 - Populate both: old column = old value, new column = new value
 - Publish schema with both old and new columns
 - Notify all consumers: 'New column available, please migrate. Old column will be removed on {{sunset_date}}'

 Phase 2 — Migrate:
 - Support consumer teams in migrating their pipelines/reports to the new column
 - Track migration progress per consumer team
 - Provide a migration deadline: {{deadline}}

 Phase 3 — Contract (remove the old):
 - Verify all consumers have migrated (query lineage + direct confirmation)
 - Remove the old column
 - Publish final schema version

3. Rollback plan:
 - At each phase: what is the rollback procedure if a critical consumer cannot migrate in time?
 - Rollback requires reverting only Phase 1 changes — no data is lost

4. Communication plan:
 - Initial announcement: {{notice_period}} before Phase 1
 - Weekly migration status updates to all consumers
 - Final warning: 1 week before Phase 3

Return: impact assessment table, phase-by-phase implementation plan, consumer communication templates, and rollback procedure. 
```

## When to use this prompt 
Use case 01 
When renaming columns or changing table semantics. 
Use case 02 
When a breaking schema change affects many downstream teams. 
Use case 03 
When expand-and-contract migration is the safest rollout method. 
Use case 04 
When communication and migration tracking are as important as technical changes. 

## What the AI should return 

Return an impact assessment of affected consumers, a phase-by-phase migration plan, communication templates, and rollback procedures. Include how migration progress is tracked and what gates must be met before removing the old structure. The output should support both technical execution and stakeholder coordination. 

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

Once you have the first result, continue deeper with related prompts in Data Contracts.
