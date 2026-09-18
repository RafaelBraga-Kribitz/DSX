# Cloud Data Engineer *AI Prompts *

Cloud Data Engineer AI prompt library with 20 prompts in 6 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 6 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse Cloud Data Engineer prompt categories 
6 categories 
### Cloud Architecture 

AI prompts for cloud data architecture covering service selection, scalability, cost tradeoffs, reliability design, and platform governance. 
5 prompts Cloud Data Platform Architecture Data Mesh on Cloud → 
### Orchestration 

AI prompts for orchestration workflows including DAG design, scheduling strategy, dependency management, and resilient pipeline execution. 
4 prompts Cloud Orchestration with Airflow Data Contracts and SLA Management → 
### Cloud Storage 

AI prompts for cloud storage design, partitioning strategy, lifecycle management, format selection, and cost-performance optimization. 
3 prompts Cloud Data Catalog and Metadata Management Data Lake Design on Cloud Object Storage → 
### Cloud Warehouse 

AI prompts for cloud data warehouse modeling and operations, including performance patterns, workload management, and analytics-ready schemas. 
3 prompts BigQuery Optimization Redshift Architecture and Tuning → 
### Streaming 

AI prompts for streaming data systems including event design, lag management, windowing logic, and reliable real-time analytics pipelines. 
3 prompts CDC Pipeline Design Real-Time Analytics Architecture → 
### Security and Governance 

AI prompts for security and governance including policy controls, data access standards, auditability, and compliance-aligned architecture. 
2 prompts Cloud Cost Management Cloud Data Security → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 20 Cloud Architecture 5 Orchestration 4 Cloud Storage 3 Cloud Warehouse 3 Streaming 3 Security and Governance 2 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **20 **of 20 prompts 
## Cloud Architecture 
5 prompt s Cloud Architecture Beginner Prompt 01 
### Cloud Data Platform Architecture 
Design a cloud-native data platform architecture for this organization.

Cloud provider: {{provider}} (AWS, GCP, Azure)
Data sources: {{sources}}
Users: {{users}} (analysts, data scientists, engineers)
Scale: {{scale}}

1. AWS reference architecture:
 - Ingestion: Kinesis Data Streams (streaming) / AWS Glue (batch ETL)
 - Storage: S3 (data lake) + Redshift (warehouse) + RDS (operational)
 - Processing: AWS Glue / EMR (Spark) / Lambda (serverless)
 - Serving: Redshift / Athena (S3 queries) / DynamoDB (low-latency lookups)
 - Orchestration: Apache Airflow on MWAA / AWS Step Functions
 - Catalog: AWS Glue Data Catalog
 - BI: QuickSight / Tableau / Looker

2. GCP reference architecture:
 - Ingestion: Pub/Sub (streaming) / Cloud Dataflow / Cloud Composer (Airflow)
 - Storage: Cloud Storage (data lake) + BigQuery (warehouse)
 - Processing: Dataflow (Apache Beam) / Dataproc (Spark)
 - Serving: BigQuery / Bigtable (low-latency) / Cloud Spanner (transactional)
 - Catalog: Dataplex / Data Catalog
 - BI: Looker / Looker Studio / Tableau

3. Azure reference architecture:
 - Ingestion: Event Hubs (streaming) / Azure Data Factory (ETL/ELT)
 - Storage: ADLS Gen2 (data lake) + Synapse Analytics (warehouse)
 - Processing: Databricks / Azure Synapse Spark / Azure Stream Analytics
 - Serving: Synapse / Cosmos DB / Azure SQL
 - Catalog: Microsoft Purview
 - BI: Power BI

4. Lake House pattern (recommended default):
 - Single storage layer (cloud object storage) holds all data in open formats (Parquet, Delta, Iceberg)
 - Multiple compute engines query the same data (Spark, Athena, BigQuery Omni, Trino)
 - Delta Lake / Apache Iceberg: ACID transactions on the data lake
 - Eliminates data duplication between a separate data lake and warehouse

5. Cost optimization:
 - Separate storage and compute: scale them independently
 - Use spot/preemptible instances for batch processing
 - Implement data tiering: hot (SSD), warm (HDD/standard), cold (archival)

Return: reference architecture diagram (text), component selection rationale, lake house vs traditional warehouse decision, and cost optimization approach. Copy prompt View page Show more ↓ Cloud Architecture Advanced Prompt 02 
### Data Mesh on Cloud 
Design a data mesh architecture on this cloud platform.

Organization size: {{org_size}}
Domains identified: {{domains}} (finance, product, marketing, operations, etc.)
Cloud provider: {{provider}}
Current state: {{current_state}} (centralized data warehouse, fragmented silos, etc.)

1. Data mesh principles:
 - Domain ownership: each business domain owns and publishes its own data products
 - Data as a product: data is treated with product-quality standards (SLA, documentation, quality)
 - Self-serve data platform: a platform team provides the infrastructure; domain teams use it
 - Federated computational governance: global policies enforced automatically; local flexibility

2. Domain data product structure:
 Each domain publishes:
 - Input data: raw data from its systems
 - Transformed data: cleansed, enriched, domain-specific tables
 - Output data products: interfaces for other domains (S3 path, Snowflake share, BigQuery authorized dataset)
 - SLA: freshness, availability, schema stability guarantees
 - Documentation: data catalog entry with owner, description, quality metrics

3. Technical implementation on AWS:
 - Account per domain: separate AWS accounts for finance, product, marketing data
 - Cross-domain access: AWS Lake Formation data sharing; S3 bucket policies for cross-account access
 - Central catalog: AWS Glue Data Catalog federated with domain-level catalogs
 - Self-serve platform: reusable Terraform modules for each domain to provision standard infrastructure

4. Governance layer:
 - Global policies (applied everywhere): PII tagging, retention rules, access logging
 - Domain policies (domain-specific): schema standards, SLA definitions, quality thresholds
 - Policy engine: AWS SCP (service control policies), OPA (Open Policy Agent), Apache Ranger

5. Data product contract:
 interface_type: s3_parquet
 location: s3://finance-data-products/revenue/v1/
 schema: {order_id: bigint, amount_usd: numeric, date: date}
 sla_freshness: 4 hours
 owner: finance-analytics@company.com
 version: 1.2.0

Return: domain architecture, AWS/GCP/Azure implementation approach, governance layer design, and data product contract schema. Copy prompt View page Show more ↓ Cloud Architecture Intermediate Prompt 03 
### ELT vs ETL on Cloud 
Design the data transformation strategy for this cloud data platform.

Cloud warehouse: {{warehouse}}
Data volume: {{volume}}
Transformation complexity: {{complexity}}
Team skills: {{team_skills}}

1. ETL (Extract, Transform, Load):
 - Transform data BEFORE loading into the warehouse
 - Transformation happens in an external processing engine (Spark, Python)
 - Use when: data must be transformed before it reaches the warehouse (privacy, compliance), large-scale transformations that the warehouse handles poorly, non-SQL transformations

2. ELT (Extract, Load, Transform):
 - Load raw data INTO the warehouse first, then transform using SQL
 - Leverage the warehouse's MPP engine for transformations
 - Default choice for modern cloud warehouses (BigQuery, Snowflake, Redshift)
 - Enables: instant access to raw data, auditability, re-transformation without re-extraction

3. ELT stack (recommended for most teams):
 - Extraction: Fivetran / Airbyte / Stitch (managed connectors)
 - Loading: load raw to the warehouse (Snowflake COPY INTO, BigQuery load jobs, Redshift COPY)
 - Transformation: dbt (SQL transformations, testing, documentation)

4. When to use a processing engine (Spark / Dataflow) alongside ELT:
 - Complex unstructured data: log parsing, NLP, image metadata extraction
 - Large-scale deduplication across billions of rows
 - ML feature computation that requires Python libraries
 - Data that must NOT enter the warehouse (PII that must be tokenized first)

5. Reverse ETL:
 - Push transformed data FROM the warehouse TO operational systems (CRM, ad platforms, email tools)
 - Tools: Census, Hightouch, Grouparoo
 - Use case: sync customer segments from the warehouse to Salesforce or Facebook Ads

Return: ELT vs ETL recommendation, tool stack, processing engine use cases, and reverse ETL pattern. Copy prompt View page Show more ↓ Cloud Architecture Advanced Chain 04 
### Full Cloud Data Engineering Chain 
Step 1: Architecture design - choose the cloud data platform components (ingestion, storage, processing, serving, orchestration, catalog) for the given provider and requirements. Define the medallion zones and table format (Delta Lake or Iceberg).
Step 2: Ingestion design - design the batch ingestion pipeline (ELT with managed connectors) and the streaming pipeline (CDC or event streaming). Define the landing zone schema and file format.
Step 3: Transformation layer - set up dbt on the cloud warehouse. Design the staging, intermediate, and mart layers. Configure incremental models for large tables. Set up dbt tests and source freshness checks.
Step 4: Orchestration - configure Airflow or the managed orchestrator. Define DAG structure, retry policies, and SLA alerts. Implement data-aware scheduling between upstream and downstream pipelines.
Step 5: Security and governance - configure IAM roles, network security (private endpoints), data encryption, and audit logging. Tag PII columns. Set up the data catalog and ownership assignments.
Step 6: Observability - implement pipeline monitoring (success rates, duration trends, SLA breaches), data quality monitoring (dbt test failures, row count anomalies), and cost monitoring (tagged resource spend).
Step 7: IaC and CI/CD - provision all infrastructure via Terraform. Set up CI for dbt (slim builds on PR). Set up CD for pipeline deployment. Define the runbook for common failure scenarios. Copy prompt View page Show more ↓ Cloud Architecture Advanced Prompt 05 
### Multi-Cloud Data Strategy 
Design a multi-cloud data strategy that avoids vendor lock-in and leverages the strengths of multiple providers.

Primary provider: {{primary}}
Secondary provider: {{secondary}}
Reason for multi-cloud: {{reason}} (regulatory, best-of-breed, M&A, risk)
Data sharing requirements: {{sharing}}

1. Multi-cloud patterns:

 Primary + Burst:
 - All data lives in the primary cloud
 - Burst compute to secondary cloud for overflow workloads
 - Risk: data transfer costs between clouds

 Federated (query across clouds):
 - Data stays in each cloud; queries federate across them
 - BigQuery Omni: query S3/ADLS data from BigQuery
 - Snowflake: available on AWS, GCP, and Azure; same interface across clouds
 - Trino / Presto: open-source federated query across any data source

 Replicated (synchronized copy):
 - Mirror critical datasets between clouds for disaster recovery or locality
 - High cost and complexity; justified for active-active multi-region

2. Avoiding lock-in:
 - Open formats: Parquet, Delta Lake, Apache Iceberg — readable by any engine
 - Open protocols: S3-compatible APIs (all clouds support S3 API now)
 - Open orchestration: Apache Airflow (portable across all clouds)
 - Containerize processing: Docker + Kubernetes (runs on any cloud)

3. Data transfer cost management:
 - Data egress is expensive (AWS: $0.09/GB outbound)
 - Minimize cross-cloud data movement: process in the cloud where the data lives
 - Use direct connectivity: AWS Direct Connect ↔ Azure ExpressRoute peering
 - Snowflake / Databricks: same vendor platform across all clouds (no egress for SQL queries)

4. Governance across clouds:
 - Unified catalog: DataHub or Microsoft Purview can catalog assets across clouds
 - Unified IAM: OIDC federation between cloud providers
 - Unified monitoring: Datadog or Splunk for cross-cloud observability

Return: multi-cloud architecture recommendation, lock-in avoidance strategy, data transfer cost analysis, and governance approach. Copy prompt View page Show more ↓ 
## Orchestration 
4 prompt s Orchestration Intermediate Prompt 01 
### Cloud Orchestration with Airflow 
Design and implement an Airflow orchestration pattern for this data pipeline.

Provider: {{provider}} (AWS MWAA, GCP Cloud Composer, Astronomer, self-hosted)
Pipeline: {{pipeline_description}}
Dependencies: {{dependencies}}
SLA: {{sla}}

1. DAG design principles:
 - One DAG = one business process (not one per table)
 - Idempotent tasks: re-running any task produces the same result
 - No business logic in the DAG file; DAG file only defines the workflow
 - Use template variables for dates: {{ ds }}, {{ execution_date }}, {{ next_ds }}

2. Task types:
 BashOperator: shell commands
 PythonOperator: Python functions (keep functions small and focused)
 BigQueryInsertJobOperator: BigQuery SQL execution
 RedshiftSQLOperator: Redshift queries
 S3ToRedshiftOperator: load S3 files to Redshift
 DbtOperator / DbtCloudRunJobOperator: trigger dbt runs
 HttpSensor: wait for an API endpoint to be available
 ExternalTaskSensor: wait for a task in another DAG

3. Retry and SLA configuration:
 default_args = {
 'retries': 3,
 'retry_delay': timedelta(minutes=5),
 'retry_exponential_backoff': True,
 'email_on_failure': True,
 'sla': timedelta(hours=4),
 }

4. Dynamic DAGs (for many similar pipelines):
 # Generate a DAG per source table from a config file
 for table in config['tables']:
 with DAG(f'sync_{table["name"]}', ...) as dag:
 globals()[f'dag_{table["name"]}'] = dag

5. Data-aware scheduling (Airflow 2.4+):
 # Trigger a downstream DAG when an upstream dataset is updated
 @dag(schedule=[Dataset('s3://bucket/processed/orders')])
 def downstream_dag():
 ...
 # Declarative dependency management without sensors

6. Testing Airflow DAGs:
 - DAG integrity test: ensure all DAGs parse without errors (dag.test_cycle())
 - Task unit tests: test the Python function independently
 - Integration test: airflow dags test <dag_id> <execution_date> in a local environment

Return: DAG template with retry configuration, dynamic DAG generation pattern, data-aware scheduling, and testing approach. Copy prompt View page Show more ↓ Orchestration Advanced Prompt 02 
### Data Contracts and SLA Management 
Implement data contracts and SLA management for data products in this cloud platform.

Data producers: {{producers}}
Data consumers: {{consumers}}
Current issues: {{issues}} (schema breaking changes, missed SLAs, undocumented changes)

1. What is a data contract:
 A data contract is a formal agreement between a data producer (team that writes the data) and data consumers (teams that read it). It specifies:
 - Schema: column names, types, and semantic meaning
 - Quality: expected null rates, value distributions, referential integrity
 - SLA: freshness (max hours since last update), availability (uptime %)
 - Versioning: how schema changes are communicated and backward compatibility

2. Data contract specification (YAML):
 apiVersion: v1
 kind: DataContract
 id: orders.v1
 producer: payments-team
 owner: payments-data@company.com
 schema:
 - name: order_id
 type: bigint
 nullable: false
 unique: true
 - name: amount_usd
 type: numeric(10,2)
 nullable: false
 minimum: 0
 sla:
 freshness_hours: 2
 availability_percent: 99.5
 versioning:
 current: 1.2.0
 breaking_change_policy: 30-day notice required

3. Tooling:
 - Data Contract CLI (open-source): validate data against contracts, publish to catalog
 - Soda Core: run quality checks defined in contracts
 - dbt + Elementary: enforce schema contracts via model contracts; test quality via tests

4. SLA monitoring:
 - Freshness check: query MAX(updated_at) per table; alert if > SLA threshold
 - Availability: monitor pipeline success rate; alert on consecutive failures
 - Quality score: % of tests passing per data product; publish in the catalog
 - SLA breach report: weekly report of SLA breaches per team, with trend

5. Governance process:
 - Contract registration: new data products must register a contract before GA
 - Breaking change process: 30-day notice + migration guide for all consumers
 - Deprecation: deprecated products sunset after 90 days with active consumer notification

Return: data contract YAML schema, tooling recommendation, SLA monitoring implementation, and governance process. Copy prompt View page Show more ↓ Orchestration Intermediate Prompt 03 
### Infrastructure as Code for Data 
Implement Infrastructure as Code (IaC) for this cloud data platform.

Cloud provider: {{provider}}
IaC tool: {{iac_tool}} (Terraform, Pulumi, CDK, Bicep)
Components to provision: {{components}}
Team: {{team}}

1. Why IaC for data infrastructure:
 - Reproducible: dev, staging, and prod environments are identical
 - Version-controlled: infrastructure changes are reviewed like code
 - Self-documenting: the Terraform / Pulumi code IS the documentation
 - Auditable: every change is in git history with the author

2. Terraform for cloud data resources:

 S3 bucket with lifecycle and logging:
 resource "aws_s3_bucket" "data_lake" {
 bucket = "${var.env}-data-lake-${var.account_id}"
 tags = { Environment = var.env, Team = "data-engineering" }
 }

 Snowflake warehouse:
 resource "snowflake_warehouse" "analytics" {
 name = "ANALYTICS_WH"
 warehouse_size = "SMALL"
 auto_suspend = 60
 auto_resume = true
 }

3. Module structure:
 modules/
 data_lake/ # S3 bucket + lifecycle + IAM
 snowflake_env/ # databases, warehouses, roles
 airflow_mwaa/ # MWAA environment + networking
 monitoring/ # CloudWatch dashboards + alarms

 environments/
 dev/main.tf # calls modules with dev variables
 prod/main.tf # calls modules with prod variables

4. State management:
 - Remote state: store in S3 + DynamoDB (AWS) or GCS (GCP) with locking
 - State locking: prevents concurrent runs from corrupting state
 - Separate state per environment: dev and prod should never share state

5. CI/CD for IaC:
 PR: terraform plan → post plan output as PR comment
 Merge to main: terraform apply (with approval gate for prod)
 Tool: Atlantis (open-source) or Terraform Cloud for automated plan/apply

Return: Terraform module structure, resource examples, state management configuration, and CI/CD pipeline for IaC. Copy prompt View page Show more ↓ Orchestration Advanced Prompt 04 
### Pipeline Observability and Monitoring 
Design an observability framework for this cloud data pipeline.

Cloud provider: {{provider}}
Orchestrator: {{orchestrator}} (Airflow, Prefect, Dagster, dbt Cloud)
Pipeline count: {{pipeline_count}}
SLA requirements: {{sla}}

1. What to monitor:

 Pipeline health:
 - Success/failure rate per DAG/job over time
 - Duration trend: is a job getting slower? (may indicate data volume growth or a query regression)
 - Retry rate: high retries indicate flaky upstream dependencies

 Data freshness:
 - Time since last successful run per table
 - SLA breach: alert if a critical table has not been updated within {{sla}} hours

 Data quality:
 - Test failure rate per dbt model
 - Row count anomalies: significant drop or spike vs rolling average

 Infrastructure:
 - Cloud service quotas: Airflow task concurrency, Snowflake credit consumption
 - Storage growth: S3/GCS bucket size trends

2. Observability stack:
 - Airflow: built-in metrics via StatsD → Prometheus → Grafana
 - dbt: elementary package → data observability dashboard
 - Cloud-native: AWS CloudWatch / GCP Cloud Monitoring / Azure Monitor for infrastructure
 - Data catalog: Dataplex / Purview / Atlan for data lineage and freshness

3. Alerting design:
 - Alert on pipeline failure: Slack + PagerDuty (for SLA-critical pipelines)
 - Alert on SLA breach (job did not complete on time): escalate based on tier
 - Alert on data quality failure: Slack with affected model, failure reason, and link to dbt docs
 - Avoid alert fatigue: start with few high-signal alerts; add gradually

4. Lineage tracking:
 - Column-level lineage: which source columns feed each output column
 - Tools: dbt + Elementary (column-level lineage), DataHub, Atlan, OpenLineage
 - OpenLineage standard: emit lineage events from Airflow/Spark/dbt → centralize in Marquez or DataHub

5. Runbook for common failures:
 - Source freshness failure: check source system → check connector logs → retry
 - dbt test failure: run `dbt test --select <model>` in dev → investigate SQL → fix upstream
 - Airflow DAG stuck: check Airflow scheduler logs → check DB connections → manually clear task

Return: monitoring metric definitions, alerting configuration, lineage tooling recommendation, and runbook templates. Copy prompt View page Show more ↓ 
## Cloud Storage 
3 prompt s Cloud Storage Advanced Prompt 01 
### Cloud Data Catalog and Metadata Management 
Implement a data catalog and metadata management strategy for this cloud data platform.

Cloud provider: {{provider}}
Data assets: {{data_assets}} (tables, dashboards, ML models, data products)
Users: {{users}} (data engineers, analysts, data scientists)
Compliance: {{compliance}}

1. Why a data catalog:
 - Discoverability: users can find the data they need without asking Slack
 - Trust: users know who owns the data, when it was last updated, and its quality
 - Compliance: understand what PII data exists and where it lives
 - Lineage: understand the impact of changes before making them

2. Catalog tool selection:
 - AWS Glue Data Catalog: native AWS integration; good for Athena + Glue workflows; limited UI
 - Google Dataplex: unified GCP data governance + catalog
 - Microsoft Purview: enterprise governance for Azure + multi-cloud
 - DataHub (open-source): rich lineage, push-pull metadata; connects to any stack
 - Atlan / Alation (commercial): best-in-class UX; strong search and collaboration
 - dbt docs: good starting point; limited to dbt assets only

3. Metadata to capture per asset:
 - Technical: schema, data types, row count, size, freshness
 - Business: description, owner, domain, use cases, related assets
 - Operational: SLA, lineage (upstream sources, downstream consumers), quality scores
 - Governance: PII classification, retention policy, access controls, audit log

4. PII classification automation:
 - Tag PII columns automatically using regex patterns or NLP classifiers
 - AWS Macie: scans S3 for PII automatically
 - GCP DLP API: classifies data in BigQuery and Cloud Storage
 - Apply tags: pii_type=email, pii_type=ssn, pii_type=phone_number
 - Trigger: alert when untagged PII is detected in a new dataset

5. Catalog governance process:
 - Owner assignment: every table must have an owner before it goes to production
 - Description SLA: new tables must be documented within 5 business days
 - Freshness monitoring: catalog must show last update time for all production tables
 - Quarterly audit: review stale or orphaned assets and archive or document them

Return: catalog tool recommendation, metadata schema, PII classification automation, and governance process. Copy prompt View page Show more ↓ Cloud Storage Intermediate Prompt 02 
### Data Lake Design on Cloud Object Storage 
Design a well-organized, cost-effective data lake on cloud object storage.

Provider: {{provider}} (S3, GCS, ADLS Gen2)
Data types: {{data_types}} (raw events, processed tables, ML features, archived logs)
Access patterns: {{access_patterns}}
Retention: {{retention}}

1. Folder structure (medallion architecture):
 s3://company-data-lake/
 ├── bronze/ # raw data, immutable, exactly as received
 │ ├── source_system=stripe/
 │ ├── source_system=postgres/
 │ └── source_system=salesforce/
 ├── silver/ # cleaned, validated, enriched
 │ ├── domain=finance/
 │ ├── domain=product/
 │ └── domain=marketing/
 ├── gold/ # business-ready aggregates, mart tables
 │ ├── reporting/
 │ └── ml-features/
 └── sandbox/ # exploratory work, not production

2. File format selection:
 - Parquet: columnar, compressed, best for analytical queries — use for all structured data
 - ORC: similar to Parquet, preferred in Hive/Hadoop ecosystems
 - Avro: row-oriented, schema evolution support — use for streaming and Kafka
 - JSON/CSV: only for bronze landing zone (raw source format)
 - Delta / Iceberg: Parquet + transaction log — use when ACID and schema evolution needed

3. Partitioning strategy:
 - Partition by ingestion date for time-series data: year=2024/month=01/day=15/
 - Partition by business key for lookup data: tenant_id=abc/
 - Avoid over-partitioning: < 10MB per partition file is too small (many small files problem)
 - Target: 100MB–1GB per partition file for Spark/Athena efficiency

4. Compaction (small file problem):
 - Streaming writes create many small files → poor query performance
 - Run a compaction job periodically: read partition, write as one large file
 - Delta Lake: OPTIMIZE command with Z-ORDER for layout optimization
 - AWS S3: S3 Intelligent-Tiering for cost optimization across file sizes

5. Lifecycle policies:
 - Bronze: retain forever (immutable raw data)
 - Silver: retain 3 years, move to Glacier after 1 year
 - Gold: retain 1 year, recreatable from silver
 - Sandbox: delete after 90 days

Return: folder structure, file format recommendations, partitioning strategy, compaction schedule, and lifecycle policy configuration. Copy prompt View page Show more ↓ Cloud Storage Intermediate Prompt 03 
### Delta Lake / Apache Iceberg 
Implement an open table format (Delta Lake or Apache Iceberg) for ACID transactions on a data lake.

Format choice: {{format}} (Delta Lake or Iceberg)
Compute engine: {{engine}} (Spark, Trino, Flink, Databricks, BigQuery)
Primary use case: {{use_case}} (upserts, time travel, schema evolution, multi-engine access)

1. Delta Lake vs Iceberg comparison:

 Delta Lake:
 - Best for: Databricks environments, Python/Spark workflows, simpler setup
 - ACID transactions via a JSON transaction log in _delta_log/
 - Strong Spark integration; growing support for other engines
 - Optimize and Z-Order commands for layout optimization

 Apache Iceberg:
 - Best for: multi-engine environments (Spark + Trino + Flink + BigQuery)
 - ACID via metadata tree (manifest files + snapshot files)
 - Better multi-engine support (no engine lock-in)
 - Hidden partitioning: partition scheme can change without rewriting data

2. Core capabilities:

 ACID upserts (MERGE):
 MERGE INTO target USING source ON target.id = source.id
 WHEN MATCHED THEN UPDATE SET *
 WHEN NOT MATCHED THEN INSERT *;

 Time travel:
 -- Read data as of a point in time:
 SELECT * FROM orders TIMESTAMP AS OF '2024-01-15 10:00:00';
 SELECT * FROM orders VERSION AS OF 42; -- specific snapshot ID

 Schema evolution:
 ALTER TABLE orders ADD COLUMN is_flagged BOOLEAN;
 ALTER TABLE orders RENAME COLUMN old_name TO new_name;
 -- Historical data is not rewritten; schema is evolved in the metadata

3. Optimize and compaction (Delta Lake):
 OPTIMIZE orders ZORDER BY (customer_id, order_date);
 -- Reorganizes file layout so related data is co-located for faster queries
 -- Run after bulk writes or on a daily schedule

4. Vacuum (removing old files):
 VACUUM orders RETAIN 168 HOURS; -- delete files older than 7 days
 -- Required to reclaim storage from deleted/updated rows
 -- Note: vacuuming too aggressively removes time travel history

5. Table maintenance schedule:
 - OPTIMIZE: daily, after the main load
 - VACUUM: weekly (retain at least 7 days for time travel)
 - Schema evolution: via PR with impact assessment

Return: format selection rationale, MERGE pattern for upserts, schema evolution DDL, OPTIMIZE configuration, and maintenance schedule. Copy prompt View page Show more ↓ 
## Cloud Warehouse 
3 prompt s Cloud Warehouse Intermediate Prompt 01 
### BigQuery Optimization 
Optimize BigQuery performance and cost for this workload.

Workload: {{workload}}
Current monthly cost: {{current_cost}}
Query patterns: {{query_patterns}}
Data volume: {{volume}}

1. BigQuery cost model:
 - On-demand: $5 per TB of data scanned (minimize bytes read)
 - Flat-rate / capacity pricing: reserved slot commitments for predictable workloads
 - Storage: $0.02/GB for active, $0.01/GB for long-term (not modified for 90 days)

2. Reducing bytes scanned:
 - Partition tables by date:
 PARTITION BY DATE(event_timestamp)
 Queries with WHERE event_date BETWEEN ... AND ... only scan relevant partitions

 - Cluster by frequently filtered columns:
 CLUSTER BY user_id, product_category
 Improves scan efficiency for queries filtering on these columns

 - Use INFORMATION_SCHEMA to find expensive queries:
 SELECT total_bytes_billed/POW(1024,3) AS gb_billed, query
 FROM `region-us`.INFORMATION_SCHEMA.JOBS_BY_PROJECT
 ORDER BY total_bytes_billed DESC LIMIT 20;

3. Schema design for BigQuery:
 - Prefer denormalized (nested and repeated) schemas over normalized schemas
 - Use STRUCT and ARRAY columns to store related data in one row
 - Avoids expensive cross-shard joins on normalized data
 - Nested repeated fields are stored in columnar format → efficient for column scans

4. Materialized views:
 CREATE MATERIALIZED VIEW daily_revenue AS
 SELECT DATE(order_date) AS d, SUM(amount) AS revenue
 FROM orders GROUP BY 1;
 - BigQuery automatically refreshes within 5 minutes of base table changes
 - Queries on the base table can transparently use the materialized view

5. Slot utilization:
 - Monitor: INFORMATION_SCHEMA.JOBS_TIMELINE for slot hours
 - Identify: queries with high slot_ms = compute-intensive (add partitioning)
 - BI Engine: in-memory acceleration for Looker and Looker Studio

Return: partitioning and clustering DDL, cost investigation queries, materialized view setup, and schema design recommendation. Copy prompt View page Show more ↓ Cloud Warehouse Advanced Prompt 02 
### Redshift Architecture and Tuning 
Design and optimize a Redshift deployment for this workload.

Workload: {{workload}}
Data volume: {{volume}}
Query patterns: {{query_patterns}}
Cluster type: {{cluster_type}} (provisioned vs Serverless)

1. Redshift Serverless vs Provisioned:
 Serverless: auto-scales, pay per compute-second, no cluster management
 - Use for: unpredictable workloads, intermittent usage, cost optimization
 Provisioned: fixed cluster, predictable performance and cost
 - Use for: consistent heavy workloads, >$500/month sustained use

2. Table design:
 Distribution styles:
 - DISTSTYLE KEY (column): rows with the same key on the same slice — use for large JOIN tables
 - DISTSTYLE EVEN: round-robin — use for large tables with no clear join key
 - DISTSTYLE ALL: copy to every slice — use for small dimension tables (< 1M rows)

 Sort keys:
 - COMPOUND SORTKEY (col1, col2): range scan optimization on ordered columns (date)
 - INTERLEAVED SORTKEY: equal weight to all sort key columns — use for multiple filter patterns

3. COPY command for loading:
 COPY orders FROM 's3://bucket/data/orders/'
 IAM_ROLE 'arn:aws:iam::123456789:role/RedshiftRole'
 FORMAT AS PARQUET;
 - Use PARQUET (fastest) or CSV with GZIP compression
 - Parallel loading: split files into 1× number of slices for maximum parallelism

4. Vacuuming:
 VACUUM orders TO 100 PERCENT BOOST;
 -- Reclaims space from deleted rows and re-sorts unsorted rows
 -- Schedule weekly; automatic vacuum may not keep up with high-write tables

5. WLM (Workload Management):
 - Define query queues by user group or query group
 - Short query acceleration (SQA): auto-routes short queries to a fast lane
 - Concurrency scaling: auto-adds read capacity during peak periods

Return: distribution and sort key design, COPY command, vacuum schedule, and WLM configuration. Copy prompt View page Show more ↓ Cloud Warehouse Intermediate Prompt 03 
### Snowflake Architecture and Best Practices 
Design and optimize a Snowflake deployment for this organization.

Workload: {{workload}} (ELT, mixed, analytics, ML feature store)
Team: {{team}} (data engineers, analysts, data scientists)
Data volume: {{volume}}
Cost target: {{cost_target}}

1. Snowflake architecture concepts:
 - Separation of storage and compute: storage billed per TB, compute per second
 - Virtual warehouses: compute clusters that scale independently
 - Databases → Schemas → Tables: same as traditional databases
 - Zero-copy cloning: instant clone of any table/schema/database for testing or branching

2. Virtual warehouse strategy:
 - One warehouse per workload type (not per team):
 LOADING_WH (X-Large): bulk data loading, ELT
 ANALYTICS_WH (Small-Medium): analyst queries
 TRANSFORM_WH (Medium): dbt runs
 ML_WH (Large): data science ad-hoc
 - Auto-suspend: 60 seconds (analysts), 300 seconds (loading)
 - Auto-resume: always enabled
 - Multi-cluster warehouses: for concurrent analyst workloads

3. Cost optimization:
 - Monitor: QUERY_HISTORY view for expensive queries
 - Use result cache: same query within 24h returns the cached result (free)
 - Use CLUSTERING KEYS on large tables filtered by a column:
 ALTER TABLE orders CLUSTER BY (TO_DATE(order_date));
 - Use SEARCH OPTIMIZATION for high-cardinality point lookups
 - Tag warehouses with resource monitors to cap monthly spend

4. Snowflake roles hierarchy:
 ACCOUNTADMIN → SYSADMIN → custom roles
 - SYSADMIN: creates databases, warehouses
 - Custom roles: ANALYST_ROLE (SELECT), ENGINEER_ROLE (DML + DDL on own schema), LOADER_ROLE (COPY INTO)
 - Follow least-privilege; never use ACCOUNTADMIN for day-to-day operations

5. Data sharing:
 - Share data with other Snowflake accounts without copying (live read access)
 - CREATE SHARE; GRANT SELECT ON TABLE TO SHARE; ADD ACCOUNT TO SHARE
 - Use for: sharing data products with customers, cross-department data sharing

Return: warehouse configuration, role hierarchy DDL, clustering key recommendations, cost monitoring queries, and data sharing setup. Copy prompt View page Show more ↓ 
## Streaming 
3 prompt s Streaming Advanced Prompt 01 
### CDC Pipeline Design 
Design a Change Data Capture (CDC) pipeline to replicate database changes to a cloud data platform.

Source database: {{source_db}} (PostgreSQL, MySQL, SQL Server, Oracle)
Target: {{target}} (Snowflake, BigQuery, Redshift, S3 Delta Lake)
Volume: {{volume}} changes per second
Latency requirement: {{latency}}

1. CDC methods:

 Log-based CDC (recommended):
 - Reads the database transaction log (WAL for Postgres, binlog for MySQL)
 - Zero impact on the source database (no queries)
 - Captures all changes: INSERT, UPDATE, DELETE
 - Tools: Debezium (open-source), AWS DMS, Airbyte, Fivetran

 Query-based CDC:
 - Periodically queries the source for rows changed since the last poll
 - Requires updated_at column; cannot detect deletes
 - Higher load on the source; simpler to set up

 Trigger-based CDC:
 - Database triggers write changes to a shadow table
 - Captures deletes; impacts source performance
 - Legacy approach; avoid for new designs

2. Debezium pipeline (log-based, Kafka):
 Source DB → Debezium Connector → Kafka → Sink Connector → Target

 PostgreSQL setup:
 wal_level = logical
 CREATE PUBLICATION debezium_pub FOR ALL TABLES;

 Debezium connector config:
 {
 "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
 "database.hostname": "...",
 "database.port": "5432",
 "slot.name": "debezium_slot",
 "publication.name": "debezium_pub",
 "transforms": "unwrap",
 "transforms.unwrap.type": "io.debezium.transforms.ExtractNewRecordState"
 }

3. CDC event format:
 Each event contains: before (old row state), after (new row state), op (c/u/d/r for create/update/delete/snapshot)
 Use the after record for upserts into the target

4. Target landing pattern:
 - Stage all CDC events in S3/GCS as Parquet/Avro
 - Apply MERGE into the target table hourly: upsert based on primary key
 - Or: use Flink/Spark Structured Streaming to apply changes in near-real-time

5. Backfill / initial snapshot:
 - Debezium performs an initial snapshot of the full table before starting log-based CDC
 - For large tables: take a manual full dump, load it, then start CDC from the current LSN
 - Verify: row counts match between source and target after initial load

Return: CDC method selection, Debezium configuration, Kafka topic design, target landing pattern, and initial snapshot strategy. Copy prompt View page Show more ↓ Streaming Advanced Prompt 02 
### Real-Time Analytics Architecture 
Design a real-time analytics system that can answer queries over streaming data.

Use case: {{use_case}} (live dashboard, fraud detection, real-time recommendation, monitoring)
Query latency requirement: {{latency}} (sub-second / seconds / minutes)
Throughput: {{throughput}} events per second
Cloud provider: {{provider}}

1. Architecture options by latency tier:

 Sub-second (operational analytics):
 - Pre-aggregate into a fast OLAP store (Apache Druid, ClickHouse, Apache Pinot)
 - These systems ingest from Kafka directly and support sub-second SQL
 - Trade-off: limited join support; pre-aggregation required at ingestion

 Seconds (near-real-time):
 - Streaming aggregation in Flink/Spark Streaming → Redis or DynamoDB for serving
 - Query latency: < 100ms from the serving layer
 - Useful for: live counters, session activity feeds, fraud scores

 Minutes (micro-batch):
 - Spark Structured Streaming or Flink with checkpointing every 1-5 minutes
 - Land in Delta Lake or Iceberg; query via Athena or BigQuery
 - Simpler operations than sub-second; good for most near-real-time dashboards

2. ClickHouse for real-time OLAP:
 - Ingests from Kafka natively (Kafka Engine table)
 - Columnar storage; billion-row aggregations in < 1 second
 - Materialized views update automatically as new data arrives
 - Self-managed or managed via ClickHouse Cloud / Altinity

3. Apache Pinot for real-time serving:
 - Designed for Uber/LinkedIn-scale user-facing analytics
 - Upserts supported; indexes optimized for filtering and aggregation
 - Real-time segment from Kafka + offline segment from S3 merged seamlessly

4. Lambda + materialized serving layer (simpler):
 - Batch layer: nightly aggregates materialized in the warehouse
 - Speed layer: streaming aggregates in Redis (last 15 minutes)
 - Serving layer: query combines batch + speed for a complete picture

5. Managed options:
 - BigQuery: Streaming inserts for near-real-time; Bigtable for < 10ms lookups
 - Snowflake: Dynamic Tables (incremental refresh) for near-real-time

Return: architecture for the latency tier, technology choices, ingestion and serving design, and operational considerations. Copy prompt View page Show more ↓ Streaming Intermediate Prompt 03 
### Streaming Data Pipeline Design 
Design a cloud streaming data pipeline for this use case.

Cloud provider: {{provider}}
Source: {{source}} (application events, CDC from database, IoT sensors, clickstream)
Sink: {{sink}} (data warehouse, data lake, real-time dashboard, downstream service)
Latency SLA: {{latency}} (sub-second, seconds, minutes)
Throughput: {{throughput}} messages per second

1. Message queue selection:

 AWS Kinesis Data Streams:
 - Managed, serverless, integrates with Lambda, Firehose, Flink
 - Shard-based scaling: 1 shard = 1MB/s ingest, 2MB/s read
 - Retention: 24h default, up to 7 days
 - Cost: per shard-hour + per PUT payload

 Google Pub/Sub:
 - Fully serverless (no shards to manage)
 - Auto-scales; guaranteed at-least-once delivery
 - Integrates tightly with Dataflow, BigQuery subscriptions

 Azure Event Hubs:
 - Kafka-compatible protocol (no code changes for Kafka producers)
 - Partition-based like Kinesis
 - Event Hubs Capture: auto-writes to ADLS Gen2

 Self-managed Kafka (on Confluent Cloud or MSK):
 - Maximum flexibility and ecosystem integration
 - Best for: existing Kafka investment, complex routing, exactly-once semantics

2. Stream processing:
 - Apache Flink: stateful, exactly-once, low latency (< 1 second) — best for complex CEP
 - Apache Spark Structured Streaming: micro-batch, easy to use, integrates with Delta Lake
 - Kinesis Data Analytics / Managed Flink: fully managed Flink on AWS
 - Google Dataflow (Apache Beam): unified batch + streaming, serverless on GCP

3. Lambda vs Kappa architecture:
 Lambda: separate batch and streaming paths that merge in a serving layer
 - Pro: batch path can reprocess historical data; streaming path handles recent data
 - Con: two codebases, complexity in merging

 Kappa: one streaming pipeline handles everything (batch = bounded stream)
 - Pro: single codebase, simpler operations
 - Recommended for most modern architectures with replayable message queues

4. Exactly-once semantics:
 - At-least-once: messages may be reprocessed on failure → idempotent sinks required
 - Exactly-once: Kafka Transactions + idempotent producers + transactional sinks
 - For most use cases: design for at-least-once with idempotent writes

Return: message queue recommendation, processing engine, Lambda vs Kappa decision, and exactly-once handling strategy. Copy prompt View page Show more ↓ 
## Security and Governance 
2 prompt s Security and Governance Intermediate Prompt 01 
### Cloud Cost Management 
Implement cost monitoring and optimization for this cloud data platform.

Provider: {{provider}}
Current monthly spend: {{spend}}
Main cost drivers: {{cost_drivers}} (compute, storage, data transfer, queries)
Budget: {{budget}}

1. Cost visibility:

 AWS:
 - AWS Cost Explorer: visualize spend by service, tag, and time
 - Enable cost allocation tags: tag every resource with team, environment, project
 - AWS Budgets: set budget alerts at 50%, 80%, 100% of monthly budget
 - AWS Cost and Usage Report (CUR): detailed hourly billing data in S3 for analysis

 GCP:
 - BigQuery Billing export: export billing data to BigQuery for analysis
 - Labels on every resource (equivalent to AWS tags)
 - Budget alerts via Cloud Billing API

 Snowflake:
 - QUERY_HISTORY: identify expensive queries (total_elapsed_time, credits_used_cloud_services)
 - WAREHOUSE_METERING_HISTORY: credits consumed per warehouse
 - Resource monitors: cap spend per warehouse per day/week/month

2. Compute optimization:
 - Use spot/preemptible instances for fault-tolerant batch jobs (70-90% discount)
 - Right-size warehouse clusters: if avg cluster utilization < 30%, downsize
 - Auto-suspend warehouses when idle: 60-second suspension for transient workloads
 - Reserved instances / committed use discounts for stable baseline compute

3. Storage optimization:
 - S3 Intelligent-Tiering: auto-moves objects to cheaper tiers based on access patterns
 - Enforce lifecycle policies: delete temp/staging files after 7 days
 - Columnar formats: Parquet is 5-10x smaller than CSV → less storage and scan cost
 - Compression: snappy or zstd for Parquet (default in most tools)

4. Query cost optimization (BigQuery/Athena/Snowflake):
 - Partition pruning: WHERE clauses on the partition key
 - Column pruning: avoid SELECT *; project only needed columns
 - Result caching: identical queries hit the cache (free in Snowflake/BigQuery)
 - Materialized views: pre-compute expensive aggregations

5. FinOps process:
 - Monthly cost review: top 10 expensive resources, trends, anomalies
 - Showback / chargeback: allocate costs to teams using tags
 - Cost anomaly alerts: alert when spend > 150% of the 7-day rolling average

Return: cost monitoring setup, tagging strategy, compute and storage optimizations, query cost reduction, and FinOps process. Copy prompt View page Show more ↓ Security and Governance Intermediate Prompt 02 
### Cloud Data Security 
Implement security controls for this cloud data platform.

Provider: {{provider}}
Sensitive data types: {{sensitive_data}} (PII, PCI, PHI, financial)
Compliance: {{compliance}} (SOC 2, HIPAA, GDPR, PCI-DSS)
Access patterns: {{access_patterns}}

1. Identity and access management:
 - Use cloud IAM roles (not static credentials): EC2 instance profiles, GCP service accounts, Azure managed identities
 - Principle of least privilege: grant only the minimum permissions required for each service
 - Separate roles: data loader role, data reader role, admin role
 - Rotate credentials: automate rotation via AWS Secrets Manager, GCP Secret Manager, Azure Key Vault

2. Data encryption:
 - At-rest: cloud provider default encryption (AES-256); use customer-managed keys (CMK) for compliance
 - In-transit: TLS enforced for all connections to managed services
 - Column-level encryption: for PII fields that must be encrypted at the application layer
 - BigQuery: AEAD encryption functions for column-level encryption

3. Network security:
 - Private endpoints: connect services within a VPC without traversing the public internet
 - AWS: PrivateLink for S3, Redshift, and Glue
 - GCP: Private Google Access for Cloud Storage and BigQuery
 - VPC Service Controls (GCP): create security perimeters around data services

4. Data masking and tokenization:
 - Dynamic data masking: show masked values to non-privileged users
 - Snowflake: column masking policies based on role
 - BigQuery: authorized views with masked columns for analysts
 - PII tokenization: replace sensitive values with non-reversible tokens at ingestion

5. Audit logging:
 - Enable cloud provider data access logging: AWS CloudTrail, GCP Cloud Audit Logs, Azure Monitor
 - Log every: data access, configuration change, permission escalation
 - Centralize logs in a SIEM: Amazon Security Lake, Chronicle (GCP), Sentinel (Azure)
 - Retention: minimum 1 year for compliance

Return: IAM role design, encryption configuration, network security setup, data masking policy, and audit logging configuration. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Compliance & Privacy Analyst 12 prompts Browse Compliance & Privacy Analyst prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
- Terms of Service 
- Privacy Policy 
- AI Policy 
- Licenses 
### AI Data Analysis Examples 

- LLM Benchmark on AI Data Analysis 
- Air Passengers Forecast 
- Iris Classification 
- Customer Churn Prediction 
- Energy Consumption Forecast 
### Resources 

- Example Python notebooks 
- Fix ModuleNotFoundError 
- Glossary 
- Brand 
- Answers 
- ML Algorithm Comparison 
- Research 
- Solutions 
### Products 

- MLJAR Studio 
- MLJAR AutoML 
- AI Data Analyst 
- AutoLab Experiments 
- Mercury 
### Tutorials 

- AutoML in Python: Beginner Tutorial with House Prices 
### Open Source 

- MLJAR AutoML 
- Mercury 
- More ... 
### AI Prompts 

- Prompts for Data Professionals 
- Data Analyst prompts 
- Business Analyst prompts 
- Data Scientist prompts 
- ML Engineer prompts 
- Data Engineer prompts 
- MLOps prompts 
### Compare 

- MLJAR Studio vs Julius 
- MLJAR Studio vs H2O 
- MLJAR Studio vs DataRobot 
- MLJAR Studio vs Jupyter 
- MLJAR Studio vs ChatGPT 
- MLJAR Studio vs Cursor 
### Company 

- Contact us 
- Services 
- About us 
- Blog Made by MLJAR. All rights reserved. Created in 🇵🇱 We ❤ you! 
We collect traffic information to improve the site. 

Data is collected in a privacy-friendly way (IP anonymization, no ads, no cross-site tracking). 
Analytics are only enabled if you accept. 
Read Privacy Policy Reject Accept
