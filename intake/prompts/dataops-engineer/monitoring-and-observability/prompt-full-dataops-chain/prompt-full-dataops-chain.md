# Full DataOps Chain *AI Prompt *

Step 1: Maturity assessment - score the current team on: version control, automated testing, CI/CD, monitoring, documentation, and incident management. Identify the two lowest-s... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Maturity assessment - score the current team on: version control, automated testing, CI/CD, monitoring, documentation, and incident management. Identify the two lowest-scoring dimensions and set 90-day improvement targets.
Step 2: Pipeline testing strategy - design the test pyramid for the stack. Implement unit tests for transformation logic. Configure dbt or Great Expectations for data quality tests. Create synthetic test data for integration tests.
Step 3: CI/CD pipeline - configure CI with linting, unit tests, smoke tests, and schema validation. Configure CD with environment promotion gates, staging integration tests, and automated production deployment with rollback capability.
Step 4: Monitoring and alerting - set up pipeline health metrics (success rate, duration trend, retry rate). Configure freshness monitoring per critical table. Implement row count anomaly detection with seasonality adjustment.
Step 5: Incident management - write a runbook for the top 5 most common failure modes. Set up Slack/PagerDuty alerting with escalation policies. Run the first blameless post-mortem simulation to build the muscle.
Step 6: Data quality framework - implement schema validation at ingestion, completeness/validity/consistency checks at each pipeline stage, and a DQ score dashboard by tier.
Step 7: Documentation and governance - register all production pipelines in the data catalog with owner, SLA, and lineage. Set up schema version control with Flyway or Liquibase. Establish the data contract registration process for all new data products. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin monitoring and observability work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Monitoring and Observability or the wider DataOps Engineer library. 

## What the AI should return 

The AI should return a structured result that is directly usable in a monitoring and observability workflow, with explicit outputs, readable formatting, and enough clarity to support the next step in dataops engineer work. 

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

Once you have the first result, continue deeper with related prompts in Monitoring and Observability.
