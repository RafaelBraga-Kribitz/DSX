# dbt for Machine Learning Features *AI Prompt *

Use dbt to build and manage ML feature tables for training and serving. ML use case: {{use_case}} (e.g. churn prediction, recommendation, fraud detection) Features needed: {{fea... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Use dbt to build and manage ML feature tables for training and serving.

ML use case: {{use_case}} (e.g. churn prediction, recommendation, fraud detection)
Features needed: {{features}}
Downstream ML platform: {{platform}} (SageMaker, Vertex AI, Feature Store, custom)

1. Why dbt for ML features:
 - Features computed in the warehouse are reproducible, testable, and versioned
 - dbt tests catch feature drift before it reaches the model
 - Same feature definitions for training AND serving (no training-serving skew)
 - Feature history available via incremental models or snapshots

2. Feature table design:
 Each feature table has:
 - entity_id: the prediction target (customer_id, user_id, etc.)
 - feature_date: the date the feature was computed (for point-in-time correctness)
 - One column per feature

 Example: fct_customer_features_daily
 customer_id | feature_date | days_since_last_purchase | order_count_30d | avg_order_value_90d

3. Point-in-time correct features:
 For training: join features to labels using the feature_date <= label_date condition
 SELECT
 l.customer_id,
 l.churned_flag,
 f.days_since_last_purchase,
 f.order_count_30d
 FROM {{ ref('training_labels') }} l
 LEFT JOIN {{ ref('fct_customer_features_daily') }} f
 ON l.customer_id = f.customer_id
 AND f.feature_date = l.label_date

4. Feature tests for ML:
 - No future leakage: verify feature_date is always <= the observation date
 - No nulls in required features: all input features must be non-null
 - Reasonable ranges: order_count_30d between 0 and 1000
 - Stability: feature distribution should not shift dramatically week-over-week

5. Export to ML platform:
 Option A: Export from warehouse to S3/GCS as Parquet for batch training
 Option B: Connect dbt-generated tables directly to a feature store (Feast, Tecton)
 Option C: Use dbt Cloud job to trigger a downstream Python training pipeline on completion

Return: feature table schema, point-in-time join pattern, ML-specific tests, and export strategy. 
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

The AI should return a structured result that covers the main requested outputs, such as Why dbt for ML features:, Features computed in the warehouse are reproducible, testable, and versioned, dbt tests catch feature drift before it reaches the model. The final answer should stay clear, actionable, and easy to review inside a dbt advanced patterns workflow for analytics engineer (dbt) work. 

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
