# Data Contracts *AI Prompts *

5 Data Engineer prompts in Data Contracts. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 5 single prompts. 

## AI prompts in Data Contracts 
5 prompts Advanced Single prompt 01 
### Breaking Change Migration 

This prompt plans a safe migration path for breaking changes so producers can evolve schemas without abruptly disrupting consumers. It is especially useful when many reports, tables, or applications depend on the affected field or table grain. The response should focus on impact analysis, phased rollout, communication, and rollback options. 
Prompt text Design a safe migration process for this breaking schema change.

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

Return: impact assessment table, phase-by-phase implementation plan, consumer communication templates, and rollback procedure. Copy prompt Open prompt details Intermediate Single prompt 02 
### Contract Validation Pipeline 

This prompt builds a gate that validates data against its contract before consumers can access it. It is useful for enforcing trust boundaries where producers must prove that schema, semantics, and freshness commitments were met on each run. The output should describe both validation behavior and promotion mechanics. 
Prompt text Build an automated contract validation pipeline that verifies produced data meets all contract commitments before it is made available to consumers.

Data contract: {{contract_name}}

1. Validation gate architecture:
 - Produce data to a staging location (not the production table)
 - Run all contract validations against the staging data
 - Only promote to production if ALL blocking validations pass
 - If any blocking validation fails: halt, alert producer, do not expose data to consumers

2. Schema validation:
 - All required columns are present
 - All column data types match the contract definition
 - No unexpected new columns (flag as warning — possible unplanned schema evolution)

3. Semantic validation:
 - Primary key is unique and non-null
 - All NOT NULL columns have no nulls
 - All categorical columns contain only contract-defined values
 - Business rule assertions: {{business_rules}}

4. Freshness validation:
 - MAX(event_timestamp) is within the contract-defined freshness window
 - Row count is within ±{{tolerance}}% of the expected count for this time period

5. Promotion to production:
 - Atomic swap: rename staging table to production (or INSERT OVERWRITE the partition)
 - Log promotion: contract_name, run_id, validation_results, promotion_timestamp
 - Notify downstream consumers that fresh data is available (via event or polling endpoint)

6. Consumer-facing freshness endpoint:
 - GET /contracts/{{contract_name}}/freshness → returns: last_updated, row_count, validation_status
 - Consumers can poll this endpoint to know when new data is ready

Return: validation pipeline code, promotion logic, freshness endpoint spec, and consumer notification design. Copy prompt Open prompt details Beginner Single prompt 03 
### Data Contract Definition 

This prompt creates a formal data contract that defines what a dataset is, what it means, how fresh and accurate it will be, and how changes are managed. It is useful when producer and consumer teams need explicit expectations instead of informal assumptions. The contract should be precise enough to support governance and automation. 
Prompt text Write a data contract for the dataset: {{dataset_name}} produced by the {{producer_team}} team and consumed by {{consumer_teams}}.

A data contract is a formal agreement between data producers and consumers specifying what data will be delivered, in what format, with what quality guarantees, and on what schedule.

1. Dataset identity:
 - Dataset name and version
 - Producer: team, contact, and escalation path
 - Consumers: teams currently depending on this dataset

2. Schema definition:
 - Table or topic name
 - For each column/field: name, data type, nullable (Y/N), description, example value, PII classification (Y/N)
 - Primary key or unique identifier
 - Partitioning columns

3. Semantics and business rules:
 - Grain: what does one row represent?
 - Business rules: constraints and derived logic (e.g. 'order_total is always the sum of line items')
 - Key relationships to other datasets

4. Quality commitments:
 - Completeness: which columns are guaranteed non-null?
 - Uniqueness: which column combinations are guaranteed unique?
 - Freshness: data will be available by {{sla_time}} on each {{frequency}}
 - Accuracy: key measures are reconciled to source within {{tolerance}}

5. Change management:
 - Breaking change definition: removed column, type change, semantic change
 - Notice period: {{notice_period}} days notice required before a breaking change
 - Deprecation process: how will consumers be notified and given time to migrate?

6. SLA and support:
 - Incident response time: {{response_time}}
 - Scheduled maintenance window: {{maintenance_window}}
 - Where to report issues: {{issue_channel}}

Return: complete data contract document in YAML format. Copy prompt Open prompt details Advanced Single prompt 04 
### Data Mesh Contract Governance 

This prompt designs governance for data contracts in a data mesh where many domain teams publish their own data products. It helps define ownership, standards, enforcement, discoverability, and dispute handling without creating a central bottleneck. The answer should balance autonomy with enough consistency to keep the ecosystem reliable. 
Prompt text Design a data contract governance model for a data mesh architecture with {{num_domains}} domain teams.

In a data mesh, domain teams own and publish their own data products. Contracts are the mechanism that makes data products reliable and trustworthy.

1. Contract ownership model:
 - Producer team: responsible for defining the contract, meeting the commitments, and handling breaking changes
 - Consumer teams: responsible for registering as consumers and migrating when notified
 - Data platform team: responsible for tooling, enforcement, and governance process
 - No central team should approve every contract — this creates bottlenecks

2. Contract registry:
 - Centralized catalog of all published contracts (not a bottleneck — just a registry)
 - Each contract: schema, SLA, consumers, version history, compliance status
 - Automatic registration when a producer publishes a new dataset

3. Automated enforcement:
 - CI/CD check: new data publication must include a valid contract
 - Automated compatibility check: new schema version must be compatible with current contract
 - Consumer registration: consumers must register in the contract registry to receive change notifications
 - SLA monitoring: automated checks run against every published contract

4. Cross-domain standards (things that must be consistent across all domains):
 - Common entity IDs (customer_id must mean the same thing everywhere)
 - Standard date/time formats and timezone
 - PII classification and handling
 - Minimum required fields in every contract

5. Dispute resolution:
 - Process for when a producer cannot meet a consumer's requirements
 - Escalation path for unresolved contract disputes
 - SLA breach accountability and remediation

6. Discoverability:
 - Data product catalog: searchable, showing all published contracts, quality scores, and consumer counts
 - Quality score per data product: based on SLA compliance, test pass rate, consumer satisfaction

Return: governance model document, contract registry schema, enforcement automation design, and cross-domain standards. Copy prompt Open prompt details Intermediate Single prompt 05 
### Schema Evolution Strategy 

This prompt defines how schemas can evolve safely over time without breaking downstream consumers unexpectedly. It helps classify changes by compatibility, define registry rules, enforce additive-first practices, and handle unavoidable breaking changes with versioning. The response should feel like a policy plus an implementation pattern. 
Prompt text Design a schema evolution strategy that allows the {{producer_team}} to evolve data schemas without breaking downstream consumers.

1. Compatible change classification:
 BACKWARD COMPATIBLE (consumers with old schema can read new data):
 - Adding a new optional column with a default value
 - Widening a type (INT → BIGINT, VARCHAR(50) → VARCHAR(255))
 - Adding a new enum value to a categorical column

 FORWARD COMPATIBLE (consumers with new schema can read old data):
 - Removing a column (old data will have the column, new data won't)
 - Narrowing a type (consumers must handle both)

 BREAKING (requires coordinated migration):
 - Removing a required column
 - Renaming a column
 - Changing a type in a non-widening way (VARCHAR → INT)
 - Changing the meaning of an existing column
 - Changing the grain of the table

2. Schema registry:
 - Register every schema version with its compatibility mode in Confluent Schema Registry or AWS Glue
 - Default compatibility mode: BACKWARD (new schema must be able to read old data)
 - Enforce compatibility checks on every schema change before deployment

3. Additive-first approach:
 - Prefer adding new columns over renaming or replacing existing ones
 - Deprecate columns by marking them in the schema comment before removing
 - Retain deprecated columns for {{deprecation_period}} before removing

4. Versioned tables:
 - For breaking changes that cannot be avoided: publish a new versioned table (orders_v2)
 - Run v1 and v2 in parallel for {{parallel_period}} to allow consumers to migrate
 - Provide a migration guide and migration deadline

5. Consumer notification workflow:
 - Automated notification to all registered consumers when schema changes are registered
 - For breaking changes: personal outreach to each consumer team, migration support offered

Return: change classification guide, schema registry setup, deprecation process, and versioned table migration procedure. Copy prompt Open prompt details 
## Recommended Data Contracts workflow 
1 
### Breaking Change Migration 

Start with a focused prompt in Data Contracts so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Contract Validation Pipeline 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Data Contract Definition 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Data Mesh Contract Governance 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
