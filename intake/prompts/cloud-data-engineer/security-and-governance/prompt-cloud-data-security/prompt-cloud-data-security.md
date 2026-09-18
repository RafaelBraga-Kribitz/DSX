# Cloud Data Security *AI Prompt *

Implement security controls for this cloud data platform. Provider: {{provider}} Sensitive data types: {{sensitive_data}} (PII, PCI, PHI, financial) Compliance: {{compliance}} (... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: IAM role design, encryption configuration, network security setup, data masking policy, and audit logging configuration. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin security and governance work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Security and Governance or the wider Cloud Data Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Identity and access management:, Use cloud IAM roles (not static credentials): EC2 instance profiles, GCP service accounts, Azure managed identities, Principle of least privilege: grant only the minimum permissions required for each service. The final answer should stay clear, actionable, and easy to review inside a security and governance workflow for cloud data engineer work. 

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

Once you have the first result, continue deeper with related prompts in Security and Governance.
