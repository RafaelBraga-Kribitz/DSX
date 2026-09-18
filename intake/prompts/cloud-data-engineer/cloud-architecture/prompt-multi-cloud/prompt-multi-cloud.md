# Multi-Cloud Data Strategy *AI Prompt *

Design a multi-cloud data strategy that avoids vendor lock-in and leverages the strengths of multiple providers. Primary provider: {{primary}} Secondary provider: {{secondary}}... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: multi-cloud architecture recommendation, lock-in avoidance strategy, data transfer cost analysis, and governance approach. 
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

The AI should return a structured result that covers the main requested outputs, such as Multi-cloud patterns:, All data lives in the primary cloud, Burst compute to secondary cloud for overflow workloads. The final answer should stay clear, actionable, and easy to review inside a cloud architecture workflow for cloud data engineer work. 

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
