# Environment Parity and Promotion *AI Prompt *

Design a data environment strategy that ensures dev/staging/prod parity and safe change promotion. Stack: {{stack}} Environments needed: {{environments}} Data sensitivity: {{sen... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a data environment strategy that ensures dev/staging/prod parity and safe change promotion.

Stack: {{stack}}
Environments needed: {{environments}}
Data sensitivity: {{sensitivity}}

1. Environment definitions:

 Development (dev):
 - Each engineer has their own isolated dev environment
 - Small subset of data (last 7 days, or synthetic)
 - Cheap: use small warehouse sizes, turn off when not in use
 - Schema prefix: dbt_{{user}}_ (e.g., dbt_john_orders)

 Staging / QA:
 - Shared environment for integration testing before production
 - A representative subset of production data (30-day snapshot, anonymized)
 - Must have the same schema as production — never drift
 - Updated weekly from a production snapshot

 Production:
 - Full data, full warehouse size
 - Changes only via the automated CD pipeline; no manual changes

2. Data anonymization for non-prod environments:
 - PII replacement: replace names with Faker-generated names, emails with test@example.com format
 - Consistent anonymization: use deterministic hashing so foreign key relationships are preserved
 - Automated: run an anonymization pipeline on the production snapshot before loading to staging

3. Promotion gates:
 Dev → Staging: PR approved, CI passes, documentation added
 Staging → Production: integration tests pass, regression comparison approved, no open critical incidents

4. Schema drift detection:
 - Run a schema comparison job daily: staging schema vs production schema
 - Alert if staging has columns or tables not in production (or vice versa)
 - Prevents surprises where staging tests pass but production breaks due to schema differences

5. Feature flags for data:
 - Allow a new pipeline feature to be deployed to production but not activated
 - Activation: update the feature flag (a database table or config) without redeploying code
 - Useful for: gradual rollouts, A/B testing pipeline versions

Return: environment configuration, anonymization pipeline, promotion gate checklist, drift detection, and feature flag implementation. 
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

The AI should return a structured result that covers the main requested outputs, such as Environment definitions:, Each engineer has their own isolated dev environment, Small subset of data (last 7 days, or synthetic). The final answer should stay clear, actionable, and easy to review inside a ci/cd for data workflow for dataops engineer work. 

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
