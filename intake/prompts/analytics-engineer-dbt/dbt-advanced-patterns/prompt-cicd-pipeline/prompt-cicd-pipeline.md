# dbt CI/CD Pipeline *AI Prompt *

Design a CI/CD pipeline for this dbt project. Repository: {{repo}} (GitHub, GitLab, Bitbucket) Warehouse: {{warehouse}} Platform: {{platform}} (dbt Cloud, dbt Core + Airflow, Pr... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a CI/CD pipeline for this dbt project.

Repository: {{repo}} (GitHub, GitLab, Bitbucket)
Warehouse: {{warehouse}}
Platform: {{platform}} (dbt Cloud, dbt Core + Airflow, Prefect, etc.)
Team size: {{team_size}}

1. Branch strategy:
 - main / production: deploys to production schema
 - dev branches: each engineer works in a personal dev schema (schema: dbt_{{ env_var('DBT_USER') }})
 - PR → staging → main merge

2. CI checks on every PR:

 Step 1: dbt compile
 - Verifies all SQL is syntactically valid and all ref() / source() targets exist
 - Catches: typos, broken references, missing macros

 Step 2: dbt build --select state:modified+
 - Runs only modified models and their downstream dependents
 - Compares against the last production manifest (state artifacts)
 - Much faster than running the full project

 Step 3: dbt test --select state:modified+
 - Runs all tests on the affected models
 - Fail CI if any test with severity: error fails

 Step 4: dbt source freshness
 - Verify all source tables are fresh before running

3. GitHub Actions workflow:
 name: dbt CI
 on: [pull_request]
 jobs:
 dbt-ci:
 runs-on: ubuntu-latest
 steps:
 - uses: actions/checkout@v4
 - name: Install dbt
 run: pip install dbt-snowflake
 - name: dbt compile
 run: dbt compile --profiles-dir .
 - name: dbt build (modified)
 run: dbt build --select state:modified+ --defer --state ./prod-artifacts

4. Production deployment:
 - Trigger: merge to main
 - Run: dbt build (full project or slim CI against state)
 - On failure: alert Slack, block further deployments until resolved
 - Artifact storage: upload manifest.json to S3 or dbt Cloud after each successful run

5. dbt Cloud setup:
 - Dev environment: each user gets their own target schema
 - CI job: triggered on PR, runs slim CI
 - Production job: scheduled daily, full run with freshness checks
 - Notifications: Slack on job failure

Return: branch strategy, CI workflow YAML, production deployment steps, and dbt Cloud job configuration. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin dbt advanced patterns work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in dbt Advanced Patterns or the wider Analytics Engineer (dbt) library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Branch strategy:, main / production: deploys to production schema, dev branches: each engineer works in a personal dev schema (schema: dbt_{{ env_var('DBT_USER') }}). The final answer should stay clear, actionable, and easy to review inside a dbt advanced patterns workflow for analytics engineer (dbt) work. 

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

Once you have the first result, continue deeper with related prompts in dbt Advanced Patterns.
