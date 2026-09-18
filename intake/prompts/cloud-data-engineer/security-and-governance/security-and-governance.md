# Security and Governance *AI Prompts *

2 Cloud Data Engineer prompts in Security and Governance. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate levels and 2 single prompts. 

## AI prompts in Security and Governance 
2 prompts Intermediate Single prompt 01 
### Cloud Cost Management 

Implement cost monitoring and optimization for this cloud data platform. Provider: {{provider}} Current monthly spend: {{spend}} Main cost drivers: {{cost_drivers}} (compute, st... 
Prompt text Implement cost monitoring and optimization for this cloud data platform.

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

Return: cost monitoring setup, tagging strategy, compute and storage optimizations, query cost reduction, and FinOps process. Copy prompt Open prompt details Intermediate Single prompt 02 
### Cloud Data Security 

Implement security controls for this cloud data platform. Provider: {{provider}} Sensitive data types: {{sensitive_data}} (PII, PCI, PHI, financial) Compliance: {{compliance}} (... 
Prompt text Implement security controls for this cloud data platform.

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

Return: IAM role design, encryption configuration, network security setup, data masking policy, and audit logging configuration. Copy prompt Open prompt details 
## Recommended Security and Governance workflow 
1 
### Cloud Cost Management 

Start with a focused prompt in Security and Governance so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Cloud Data Security 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt
