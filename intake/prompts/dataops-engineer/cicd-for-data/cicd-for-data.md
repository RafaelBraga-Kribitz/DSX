# CI/CD for Data *AI Prompts *

4 DataOps Engineer prompts in CI/CD for Data. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 4 single prompts. 

## AI prompts in CI/CD for Data 
4 prompts Intermediate Single prompt 01 
### Data Pipeline CI/CD 

Design a CI/CD pipeline for this data pipeline project. Stack: {{stack}} (dbt, Airflow, Spark, Python) Repository: {{repo}} Environments: {{environments}} (dev, staging, prod) D... 
Prompt text Design a CI/CD pipeline for this data pipeline project.

Stack: {{stack}} (dbt, Airflow, Spark, Python)
Repository: {{repo}}
Environments: {{environments}} (dev, staging, prod)
Deployment frequency target: {{target}}

1. CI pipeline (every pull request):
 - Lint: flake8, black, sqlfluff (SQL style checker)
 - Unit tests: pytest → fail if any test fails
 - Schema validation: verify SQL models compile and the output schema is as expected
 - Data quality checks: run against a small synthetic dataset
 - Security scan: detect hardcoded credentials, sensitive data in code (Trufflehog, detect-secrets)
 - Documentation check: ensure every changed model has a description

2. Staging deployment (merge to main):
 - Deploy pipeline changes to the staging environment
 - Run integration tests against staging data (representative subset of production)
 - Comparison tests: compare output of new version vs current production version
 - Notify: Slack message to #data-deployments channel

3. Production deployment (manual approval or automatic):
 - High-criticality pipelines: require manual approval from a senior engineer
 - Low-criticality pipelines: auto-deploy after staging tests pass
 - Canary: route 5% of data through new pipeline version first (if architecture supports it)
 - Zero-downtime deployment: for Airflow, version DAG filenames; old version finishes, new version starts

4. Rollback strategy:
 - Tag every production deployment with a git tag
 - Rollback: deploy the previous tagged version
 - Data rollback: if the pipeline has already written bad data, run a compensation job to restore from the last known good state
 - Time to rollback SLA: < 15 minutes for Tier 1 pipelines

5. Environment configuration management:
 - Use environment variables or secrets managers (AWS Secrets Manager, GCP Secret Manager) for credentials
 - Never commit credentials to git
 - Configuration file per environment: config/dev.yml, config/prod.yml

Return: CI workflow YAML, staging and production deployment steps, rollback procedure, and credential management pattern. Copy prompt Open prompt details Advanced Single prompt 02 
### DataOps Maturity Assessment 

Conduct a DataOps maturity assessment for this data team and create an improvement roadmap. Team: {{team_description}} Current practices: {{current_practices}} Pain points: {{pa... 
Prompt text Conduct a DataOps maturity assessment for this data team and create an improvement roadmap.

Team: {{team_description}}
Current practices: {{current_practices}}
Pain points: {{pain_points}}
Goals: {{goals}}

1. Maturity dimensions to assess (score 1-5 each):

 Version control:
 1: No version control; SQL in spreadsheets / ad-hoc scripts
 3: All code in git; PRs required for changes
 5: All code, config, and DDL in git; automated linting and formatting

 Automated testing:
 1: No automated tests; manual QA before deployment
 3: Unit tests for transformations; basic schema tests
 5: Full test pyramid; contract tests; automated regression testing

 CI/CD:
 1: Manual deployments; no CI
 3: CI runs on PR; deployment is semi-automated with a manual step
 5: Fully automated CI/CD; canary deployments; automated rollback

 Monitoring and alerting:
 1: Consumers notice data issues before the data team
 3: Pipeline success/failure alerts; basic freshness monitoring
 5: Comprehensive quality monitoring; anomaly detection; SLA tracking per table

 Documentation:
 1: No documentation; knowledge in people's heads
 3: Key models documented in the catalog; ownership assigned
 5: All assets documented; auto-updated catalog; data contracts for all public data products

 Incident management:
 1: Ad-hoc response; no runbooks
 3: Runbooks for common failures; post-mortems for major incidents
 5: Automated incident detection; auto-remediation for known failure patterns; blameless post-mortems

2. Current state scoring:
 Score each dimension for the current team.
 Identify: the two lowest-scoring dimensions (highest improvement opportunity).

3. 90-day improvement roadmap:
 Based on the lowest scores, propose 3 high-impact initiatives for the next 90 days.
 Each initiative: title, current state, target state, actions, owner, success metric.

4. Quick wins (< 2 weeks each):
 Identify 3 changes that can be made immediately with high visibility impact.

Return: maturity scorecard for each dimension, gap analysis, 90-day roadmap, and quick wins. Copy prompt Open prompt details Advanced Single prompt 03 
### Environment Parity and Promotion 

Design a data environment strategy that ensures dev/staging/prod parity and safe change promotion. Stack: {{stack}} Environments needed: {{environments}} Data sensitivity: {{sen... 
Prompt text Design a data environment strategy that ensures dev/staging/prod parity and safe change promotion.

Stack: {{stack}}
Environments needed: {{environments}}
Data sensitivity: {{sensitivity}}

1. Environment definitions:

 Development (dev):
 - Each engineer has their own isolated dev environment
 - Small subset of data (last 7 days, or synthetic)
 - Cheap: use small warehouse sizes, turn off when not in use
 - Schema prefix: dbt_{{user}}_ (e.g., dbt_john_orders)

 Staging / QA:
 - Shared environment for integration testing before production
 - A representative subset of production data (30-day snapshot, anonymized)
 - Must have the same schema as production — never drift
 - Updated weekly from a production snapshot

 Production:
 - Full data, full warehouse size
 - Changes only via the automated CD pipeline; no manual changes

2. Data anonymization for non-prod environments:
 - PII replacement: replace names with Faker-generated names, emails with test@example.com format
 - Consistent anonymization: use deterministic hashing so foreign key relationships are preserved
 - Automated: run an anonymization pipeline on the production snapshot before loading to staging

3. Promotion gates:
 Dev → Staging: PR approved, CI passes, documentation added
 Staging → Production: integration tests pass, regression comparison approved, no open critical incidents

4. Schema drift detection:
 - Run a schema comparison job daily: staging schema vs production schema
 - Alert if staging has columns or tables not in production (or vice versa)
 - Prevents surprises where staging tests pass but production breaks due to schema differences

5. Feature flags for data:
 - Allow a new pipeline feature to be deployed to production but not activated
 - Activation: update the feature flag (a database table or config) without redeploying code
 - Useful for: gradual rollouts, A/B testing pipeline versions

Return: environment configuration, anonymization pipeline, promotion gate checklist, drift detection, and feature flag implementation. Copy prompt Open prompt details Intermediate Single prompt 04 
### Schema Version Control 

Implement schema version control and migration management for this database. Database: {{database}} Migration tool: {{tool}} (Flyway, Liquibase, Alembic, sqitch, dbt contracts)... 
Prompt text Implement schema version control and migration management for this database.

Database: {{database}}
Migration tool: {{tool}} (Flyway, Liquibase, Alembic, sqitch, dbt contracts)
Change types: {{change_types}} (additive, destructive, data migrations)

1. Schema migration principles:
 - Every schema change is versioned and applied consistently across all environments
 - Changes are irreversible once applied to production; never modify a migration after it runs
 - All changes applied by an automated migration tool, never manually
 - Every migration has a corresponding rollback (or a documented reason why rollback is not possible)

2. Migration file structure (Flyway/Liquibase):
 V001__create_orders_table.sql
 V002__add_status_column.sql
 V003__add_customer_index.sql
 V004__backfill_status_values.sql

 Naming convention: V{version}__{description}.sql
 Version: timestamp or sequential integer

3. Safe migration patterns:
 Additive changes (safe, no downtime):
 - Add a new column (nullable or with a default)
 - Add an index CONCURRENTLY
 - Add a new table

 Destructive changes (require careful handling):
 - Remove a column: use the expand-contract pattern (2 deployments)
 - Rename a column: add new, migrate data, remove old (3 deployments)
 - Change a column type: depends on the type change; most require a rewrite

4. Data migration within schema migrations:
 - Keep DDL migrations separate from data migrations
 - Data migrations can be slow on large tables and may need to be run as separate batch jobs
 - Idempotent data migrations: check if the migration has already been applied before running

5. CI/CD integration:
 - Run migrations in CI against a test database: verify the migration applies cleanly
 - Staging: migrations run automatically on merge
 - Production: migrations run as part of the deployment pipeline; applied before new code is deployed

Return: migration file structure, naming conventions, safe vs destructive migration patterns, and CI/CD integration steps. Copy prompt Open prompt details 
## Recommended CI/CD for Data workflow 
1 
### Data Pipeline CI/CD 

Start with a focused prompt in CI/CD for Data so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### DataOps Maturity Assessment 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Environment Parity and Promotion 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Schema Version Control 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
