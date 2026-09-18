# Data Pipeline CI/CD *AI Prompt *

Design a CI/CD pipeline for this data pipeline project. Stack: {{stack}} (dbt, Airflow, Spark, Python) Repository: {{repo}} Environments: {{environments}} (dev, staging, prod) D... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a CI/CD pipeline for this data pipeline project.

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

Return: CI workflow YAML, staging and production deployment steps, rollback procedure, and credential management pattern. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin ci/cd for data work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in CI/CD for Data or the wider DataOps Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as CI pipeline (every pull request):, Lint: flake8, black, sqlfluff (SQL style checker), Unit tests: pytest → fail if any test fails. The final answer should stay clear, actionable, and easy to review inside a ci/cd for data workflow for dataops engineer work. 

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

Once you have the first result, continue deeper with related prompts in CI/CD for Data.
