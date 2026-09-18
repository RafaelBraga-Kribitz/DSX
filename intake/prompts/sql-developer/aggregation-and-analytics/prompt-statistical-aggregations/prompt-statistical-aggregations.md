# Statistical Aggregations in SQL *AI Prompt *

Write SQL to compute statistical measures and distributions. Analysis: {{analysis}} Data: {{data_description}} Database: {{database}} 1. Descriptive statistics: SELECT COUNT(*)... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write SQL to compute statistical measures and distributions.

Analysis: {{analysis}}
Data: {{data_description}}
Database: {{database}}

1. Descriptive statistics:
 SELECT
 COUNT(*) AS n,
 AVG(amount) AS mean,
 STDDEV(amount) AS std_dev,
 VARIANCE(amount) AS variance,
 MIN(amount) AS min_val,
 MAX(amount) AS max_val,
 PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY amount) AS p25,
 PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY amount) AS median,
 PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY amount) AS p75,
 PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY amount) AS p95,
 PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY amount) AS p99
 FROM orders;

2. Correlation:
 SELECT CORR(x_column, y_column) AS pearson_r FROM metrics;
 -- Values: -1 (perfect negative), 0 (no correlation), 1 (perfect positive)

3. Histogram buckets:
 SELECT
 FLOOR(amount / 100) * 100 AS bucket_start,
 COUNT(*) AS count
 FROM orders
 GROUP BY 1
 ORDER BY 1;
 -- Groups amounts into buckets of 100: 0-100, 100-200, etc.

 WIDTH_BUCKET function:
 SELECT
 WIDTH_BUCKET(amount, 0, 5000, 10) AS bucket, -- 10 equal-width buckets from 0 to 5000
 COUNT(*)
 FROM orders
 GROUP BY bucket;

4. Regression (simple linear):
 SELECT
 REGR_SLOPE(y, x) AS slope,
 REGR_INTERCEPT(y, x) AS intercept,
 REGR_R2(y, x) AS r_squared
 FROM data_points;

5. Mode (most frequent value):
 SELECT MODE() WITHIN GROUP (ORDER BY product_category) AS most_common_category
 FROM orders;

6. Distribution comparison (KS test proxy):
 -- Compare two distributions by percentile
 SELECT percentile, group_a_value, group_b_value,
 ABS(group_a_value - group_b_value) AS diff
 FROM (
 SELECT unnest(array[0.1,0.25,0.5,0.75,0.9]) AS percentile,
 PERCENTILE_CONT(p) WITHIN GROUP (ORDER BY amount) AS val_a,
 PERCENTILE_CONT(p) WITHIN GROUP (ORDER BY amount) AS val_b
 -- ... group by condition
 );

Return: complete statistical analysis SQL, histogram bucketing, correlation, and regression queries. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin aggregation and analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Aggregation and Analytics or the wider SQL Developer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Descriptive statistics:, Correlation:, Histogram buckets:. The final answer should stay clear, actionable, and easy to review inside a aggregation and analytics workflow for sql developer work. 

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

Once you have the first result, continue deeper with related prompts in Aggregation and Analytics.
