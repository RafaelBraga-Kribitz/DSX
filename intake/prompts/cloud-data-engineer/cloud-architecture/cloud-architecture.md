# Cloud Architecture *AI Prompts *

5 Cloud Data Engineer prompts in Cloud Architecture. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 4 single prompts · 1 chain. 

## AI prompts in Cloud Architecture 
5 prompts Beginner Single prompt 01 
### Cloud Data Platform Architecture 

Design a cloud-native data platform architecture for this organization. Cloud provider: {{provider}} (AWS, GCP, Azure) Data sources: {{sources}} Users: {{users}} (analysts, data... 
Prompt text Design a cloud-native data platform architecture for this organization.

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

Return: reference architecture diagram (text), component selection rationale, lake house vs traditional warehouse decision, and cost optimization approach. Copy prompt Open prompt details Advanced Single prompt 02 
### Data Mesh on Cloud 

Design a data mesh architecture on this cloud platform. Organization size: {{org_size}} Domains identified: {{domains}} (finance, product, marketing, operations, etc.) Cloud pro... 
Prompt text Design a data mesh architecture on this cloud platform.

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

Return: domain architecture, AWS/GCP/Azure implementation approach, governance layer design, and data product contract schema. Copy prompt Open prompt details Intermediate Single prompt 03 
### ELT vs ETL on Cloud 

Design the data transformation strategy for this cloud data platform. Cloud warehouse: {{warehouse}} Data volume: {{volume}} Transformation complexity: {{complexity}} Team skill... 
Prompt text Design the data transformation strategy for this cloud data platform.

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

Return: ELT vs ETL recommendation, tool stack, processing engine use cases, and reverse ETL pattern. Copy prompt Open prompt details Advanced Chain 04 
### Full Cloud Data Engineering Chain 

Step 1: Architecture design - choose the cloud data platform components (ingestion, storage, processing, serving, orchestration, catalog) for the given provider and requirements... 
Prompt text Step 1: Architecture design - choose the cloud data platform components (ingestion, storage, processing, serving, orchestration, catalog) for the given provider and requirements. Define the medallion zones and table format (Delta Lake or Iceberg).
Step 2: Ingestion design - design the batch ingestion pipeline (ELT with managed connectors) and the streaming pipeline (CDC or event streaming). Define the landing zone schema and file format.
Step 3: Transformation layer - set up dbt on the cloud warehouse. Design the staging, intermediate, and mart layers. Configure incremental models for large tables. Set up dbt tests and source freshness checks.
Step 4: Orchestration - configure Airflow or the managed orchestrator. Define DAG structure, retry policies, and SLA alerts. Implement data-aware scheduling between upstream and downstream pipelines.
Step 5: Security and governance - configure IAM roles, network security (private endpoints), data encryption, and audit logging. Tag PII columns. Set up the data catalog and ownership assignments.
Step 6: Observability - implement pipeline monitoring (success rates, duration trends, SLA breaches), data quality monitoring (dbt test failures, row count anomalies), and cost monitoring (tagged resource spend).
Step 7: IaC and CI/CD - provision all infrastructure via Terraform. Set up CI for dbt (slim builds on PR). Set up CD for pipeline deployment. Define the runbook for common failure scenarios. Copy prompt Open prompt details Advanced Single prompt 05 
### Multi-Cloud Data Strategy 

Design a multi-cloud data strategy that avoids vendor lock-in and leverages the strengths of multiple providers. Primary provider: {{primary}} Secondary provider: {{secondary}}... 
Prompt text Design a multi-cloud data strategy that avoids vendor lock-in and leverages the strengths of multiple providers.

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

Return: multi-cloud architecture recommendation, lock-in avoidance strategy, data transfer cost analysis, and governance approach. Copy prompt Open prompt details 
## Recommended Cloud Architecture workflow 
1 
### Cloud Data Platform Architecture 

Start with a focused prompt in Cloud Architecture so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Data Mesh on Cloud 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### ELT vs ETL on Cloud 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Full Cloud Data Engineering Chain 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
