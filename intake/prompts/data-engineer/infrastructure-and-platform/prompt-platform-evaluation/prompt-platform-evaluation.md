# Platform Evaluation Chain *AI Prompt *

This prompt structures a full platform selection process from requirements through proof of concept, TCO, risk, and final recommendation. It is designed for decisions that are expensive to reverse and need evidence across technology, cost, operations, and team fit. The output should resemble a platform evaluation dossier rather than a quick opinion. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Requirements gathering — document the platform requirements: data volume (current and 3-year projection), workload types (batch ETL, streaming, ad-hoc SQL, ML), latency SLAs, team size and SQL vs code preference, compliance requirements (data residency, SOC2, HIPAA), and budget range.
Step 2: Candidate selection — identify 3 candidate platforms based on the requirements. Typical candidates: Snowflake vs Databricks vs BigQuery, or Airflow vs Prefect vs Dagster. Eliminate options that fail hard requirements immediately.
Step 3: Evaluation criteria scoring — score each candidate on: performance (benchmark on representative workloads), total cost of ownership (compute + storage + egress + seats), developer experience (ease of use for the team), ecosystem (integrations with existing tools), operational burden (managed vs self-hosted), and vendor risk.
Step 4: Proof of concept — run a 2-week PoC for the top 2 candidates. Use a representative subset of actual workloads. Measure: query performance, pipeline development speed, operational effort, and cost.
Step 5: TCO modeling — build a 3-year TCO model for each finalist: compute, storage, licensing, personnel, migration, and training costs. Include the cost of not choosing this platform (opportunity cost).
Step 6: Risk assessment — for each finalist: vendor lock-in risk, migration complexity, scaling limits, support quality, and financial stability of the vendor.
Step 7: Write the platform recommendation document: requirements summary, evaluation matrix, PoC results, TCO comparison, risk assessment, final recommendation with rationale, migration plan, and success metrics. 
```

## When to use this prompt 
Use case 01 
When choosing between major data platforms or orchestration tools. 
Use case 02 
When a formal evaluation and PoC are needed before purchase or migration. 
Use case 03 
When long-term cost, lock-in, and team fit matter as much as raw performance. 
Use case 04 
When leadership expects a documented recommendation with risks and migration considerations. 

## What the AI should return 

Return a staged platform evaluation covering requirements, shortlisted candidates, scoring criteria, PoC design, 3-year TCO, risks, and final recommendation. Include a comparison matrix, rationale for eliminations, and a high-level migration plan. The output should support executive and technical decision-making. 

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

Once you have the first result, continue deeper with related prompts in Infrastructure and Platform.
