# Data Pipeline Testing Strategy *AI Prompt *

Design a comprehensive testing strategy for this data pipeline. Pipeline: {{pipeline_description}} Technology stack: {{stack}} Data volume: {{volume}} 1. Test pyramid for data p... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a comprehensive testing strategy for this data pipeline.

Pipeline: {{pipeline_description}}
Technology stack: {{stack}}
Data volume: {{volume}}

1. Test pyramid for data pipelines:

 Unit tests (many, fast):
 - Test individual transformation functions, SQL logic, and business rules
 - Use: pytest for Python, dbt tests for SQL models
 - Sample data: create small, synthetic datasets covering edge cases
 - Run in: local development and CI (< 2 minutes)

 Integration tests (some, medium speed):
 - Test the full pipeline end-to-end on a representative data sample
 - Verify: input → transform → output produces expected results
 - Use: a dedicated test environment with a small copy of production data
 - Run in: CI on PR (< 10 minutes)

 Data quality tests (automated, production):
 - Run continuously on production data
 - Test: row counts, null rates, uniqueness, referential integrity, distribution ranges
 - Alert on failure; do not block deployment but create an incident

2. Test data management:
 - Golden dataset: a curated set of inputs with verified expected outputs
 - Synthetic data generation: use Faker or Mimesis to generate realistic test data
 - Production data snapshot: an anonymized subset of production data for integration tests
 - Data versioning: version the test datasets alongside the pipeline code

3. Regression testing:
 - After any change: compare output of new version vs old version on the same input
 - Row count comparison: new_count / old_count should be between 0.95 and 1.05
 - Key metric comparison: sum of revenue, count of distinct customers should match ± 1%
 - Schema comparison: no columns added, removed, or type-changed without a version bump

4. Contract testing:
 - Verify: the pipeline's output matches the consumer's expected schema and quality requirements
 - Run at deployment time: if the contract is violated, block the deployment

Return: test pyramid implementation for the stack, synthetic data strategy, regression testing approach, and contract test configuration. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin pipeline reliability work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Pipeline Reliability or the wider DataOps Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Test pyramid for data pipelines:, Test individual transformation functions, SQL logic, and business rules, Use: pytest for Python, dbt tests for SQL models. The final answer should stay clear, actionable, and easy to review inside a pipeline reliability workflow for dataops engineer work. 

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

Once you have the first result, continue deeper with related prompts in Pipeline Reliability.
