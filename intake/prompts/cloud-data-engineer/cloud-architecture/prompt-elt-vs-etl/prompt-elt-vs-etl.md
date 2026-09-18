# ELT vs ETL on Cloud *AI Prompt *

Design the data transformation strategy for this cloud data platform. Cloud warehouse: {{warehouse}} Data volume: {{volume}} Transformation complexity: {{complexity}} Team skill... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design the data transformation strategy for this cloud data platform.

Cloud warehouse: {{warehouse}}
Data volume: {{volume}}
Transformation complexity: {{complexity}}
Team skills: {{team_skills}}

1. ETL (Extract, Transform, Load):
 - Transform data BEFORE loading into the warehouse
 - Transformation happens in an external processing engine (Spark, Python)
 - Use when: data must be transformed before it reaches the warehouse (privacy, compliance), large-scale transformations that the warehouse handles poorly, non-SQL transformations

2. ELT (Extract, Load, Transform):
 - Load raw data INTO the warehouse first, then transform using SQL
 - Leverage the warehouse's MPP engine for transformations
 - Default choice for modern cloud warehouses (BigQuery, Snowflake, Redshift)
 - Enables: instant access to raw data, auditability, re-transformation without re-extraction

3. ELT stack (recommended for most teams):
 - Extraction: Fivetran / Airbyte / Stitch (managed connectors)
 - Loading: load raw to the warehouse (Snowflake COPY INTO, BigQuery load jobs, Redshift COPY)
 - Transformation: dbt (SQL transformations, testing, documentation)

4. When to use a processing engine (Spark / Dataflow) alongside ELT:
 - Complex unstructured data: log parsing, NLP, image metadata extraction
 - Large-scale deduplication across billions of rows
 - ML feature computation that requires Python libraries
 - Data that must NOT enter the warehouse (PII that must be tokenized first)

5. Reverse ETL:
 - Push transformed data FROM the warehouse TO operational systems (CRM, ad platforms, email tools)
 - Tools: Census, Hightouch, Grouparoo
 - Use case: sync customer segments from the warehouse to Salesforce or Facebook Ads

Return: ELT vs ETL recommendation, tool stack, processing engine use cases, and reverse ETL pattern. 
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

The AI should return a structured result that covers the main requested outputs, such as ETL (Extract, Transform, Load):, Transform data BEFORE loading into the warehouse, Transformation happens in an external processing engine (Spark, Python). The final answer should stay clear, actionable, and easy to review inside a cloud architecture workflow for cloud data engineer work. 

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
