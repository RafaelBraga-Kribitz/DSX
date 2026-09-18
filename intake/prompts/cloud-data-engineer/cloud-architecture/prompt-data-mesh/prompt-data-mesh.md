# Data Mesh on Cloud *AI Prompt *

Design a data mesh architecture on this cloud platform. Organization size: {{org_size}} Domains identified: {{domains}} (finance, product, marketing, operations, etc.) Cloud pro... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: domain architecture, AWS/GCP/Azure implementation approach, governance layer design, and data product contract schema. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin cloud architecture work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Cloud Architecture or the wider Cloud Data Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Data mesh principles:, Domain ownership: each business domain owns and publishes its own data products, Data as a product: data is treated with product-quality standards (SLA, documentation, quality). The final answer should stay clear, actionable, and easy to review inside a cloud architecture workflow for cloud data engineer work. 

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

Once you have the first result, continue deeper with related prompts in Cloud Architecture.
