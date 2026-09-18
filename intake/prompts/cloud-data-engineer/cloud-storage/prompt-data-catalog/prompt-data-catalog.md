# Cloud Data Catalog and Metadata Management *AI Prompt *

Implement a data catalog and metadata management strategy for this cloud data platform. Cloud provider: {{provider}} Data assets: {{data_assets}} (tables, dashboards, ML models,... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: catalog tool recommendation, metadata schema, PII classification automation, and governance process. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin cloud storage work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Cloud Storage or the wider Cloud Data Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Why a data catalog:, Discoverability: users can find the data they need without asking Slack, Trust: users know who owns the data, when it was last updated, and its quality. The final answer should stay clear, actionable, and easy to review inside a cloud storage workflow for cloud data engineer work. 

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

Once you have the first result, continue deeper with related prompts in Cloud Storage.
