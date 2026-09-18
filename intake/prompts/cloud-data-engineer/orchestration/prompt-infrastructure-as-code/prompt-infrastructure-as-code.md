# Infrastructure as Code for Data *AI Prompt *

Implement Infrastructure as Code (IaC) for this cloud data platform. Cloud provider: {{provider}} IaC tool: {{iac_tool}} (Terraform, Pulumi, CDK, Bicep) Components to provision:... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: Terraform module structure, resource examples, state management configuration, and CI/CD pipeline for IaC. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin orchestration work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Orchestration or the wider Cloud Data Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Why IaC for data infrastructure:, Reproducible: dev, staging, and prod environments are identical, Version-controlled: infrastructure changes are reviewed like code. The final answer should stay clear, actionable, and easy to review inside a orchestration workflow for cloud data engineer work. 

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

Once you have the first result, continue deeper with related prompts in Orchestration.
