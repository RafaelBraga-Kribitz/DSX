# Cloud Storage *AI Prompts *

3 Cloud Data Engineer prompts in Cloud Storage. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 3 single prompts. 

## AI prompts in Cloud Storage 
3 prompts Advanced Single prompt 01 
### Cloud Data Catalog and Metadata Management 

Implement a data catalog and metadata management strategy for this cloud data platform. Cloud provider: {{provider}} Data assets: {{data_assets}} (tables, dashboards, ML models,... 
Prompt text Implement a data catalog and metadata management strategy for this cloud data platform.

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

Return: catalog tool recommendation, metadata schema, PII classification automation, and governance process. Copy prompt Open prompt details Intermediate Single prompt 02 
### Data Lake Design on Cloud Object Storage 

Design a well-organized, cost-effective data lake on cloud object storage. Provider: {{provider}} (S3, GCS, ADLS Gen2) Data types: {{data_types}} (raw events, processed tables,... 
Prompt text Design a well-organized, cost-effective data lake on cloud object storage.

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

Return: folder structure, file format recommendations, partitioning strategy, compaction schedule, and lifecycle policy configuration. Copy prompt Open prompt details Intermediate Single prompt 03 
### Delta Lake / Apache Iceberg 

Implement an open table format (Delta Lake or Apache Iceberg) for ACID transactions on a data lake. Format choice: {{format}} (Delta Lake or Iceberg) Compute engine: {{engine}}... 
Prompt text Implement an open table format (Delta Lake or Apache Iceberg) for ACID transactions on a data lake.

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

Return: format selection rationale, MERGE pattern for upserts, schema evolution DDL, OPTIMIZE configuration, and maintenance schedule. Copy prompt Open prompt details 
## Recommended Cloud Storage workflow 
1 
### Cloud Data Catalog and Metadata Management 

Start with a focused prompt in Cloud Storage so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Data Lake Design on Cloud Object Storage 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Delta Lake / Apache Iceberg 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
