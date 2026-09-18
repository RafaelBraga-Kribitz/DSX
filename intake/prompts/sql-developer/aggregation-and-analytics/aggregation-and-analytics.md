# Aggregation and Analytics *AI Prompts *

3 SQL Developer prompts in Aggregation and Analytics. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 3 single prompts. 

## AI prompts in Aggregation and Analytics 
3 prompts Advanced Single prompt 01 
### Cohort and Funnel Analysis in SQL 

Write SQL to perform cohort retention analysis and funnel analysis. Event table: {{event_table}} User table: {{user_table}} Cohort definition: {{cohort}} (acquisition month, fir... 
Prompt text Write SQL to perform cohort retention analysis and funnel analysis.

Event table: {{event_table}}
User table: {{user_table}}
Cohort definition: {{cohort}} (acquisition month, first purchase date, etc.)
Database: {{database}}

1. Cohort retention matrix:

 WITH user_cohorts AS (
 -- Assign each user to a cohort based on their first activity
 SELECT user_id,
 DATE_TRUNC('month', MIN(event_date)) AS cohort_month
 FROM events
 GROUP BY user_id
 ),
 user_activity AS (
 -- Find each user's activity by month
 SELECT e.user_id,
 DATE_TRUNC('month', e.event_date) AS activity_month,
 c.cohort_month,
 EXTRACT(EPOCH FROM DATE_TRUNC('month', e.event_date) - c.cohort_month)
 / (30 * 24 * 3600) AS month_number
 FROM events e
 JOIN user_cohorts c USING (user_id)
 )
 SELECT
 cohort_month,
 month_number,
 COUNT(DISTINCT user_id) AS retained_users,
 COUNT(DISTINCT user_id) / FIRST_VALUE(COUNT(DISTINCT user_id))
 OVER (PARTITION BY cohort_month ORDER BY month_number) AS retention_rate
 FROM user_activity
 GROUP BY cohort_month, month_number
 ORDER BY cohort_month, month_number;

2. Funnel analysis (ordered step completion):

 WITH funnel_steps AS (
 SELECT user_id,
 MIN(CASE WHEN event_name = 'signup' THEN event_time END) AS step1_time,
 MIN(CASE WHEN event_name = 'onboarding_complete' THEN event_time END) AS step2_time,
 MIN(CASE WHEN event_name = 'first_purchase' THEN event_time END) AS step3_time
 FROM events
 GROUP BY user_id
 )
 SELECT
 COUNT(*) AS entered_funnel,
 COUNT(step2_time) AS completed_step2,
 COUNT(step3_time) AS completed_step3,
 ROUND(COUNT(step2_time)::NUMERIC / COUNT(*) * 100, 1) AS step1_to_step2_pct,
 ROUND(COUNT(step3_time)::NUMERIC / NULLIF(COUNT(step2_time),0) * 100, 1) AS step2_to_step3_pct
 FROM funnel_steps
 WHERE step1_time IS NOT NULL;

3. Ordered funnel (steps must occur in sequence):
 Add: AND step2_time > step1_time AND step3_time > step2_time
 to enforce that steps happened in the correct order.

Return: cohort retention matrix SQL, funnel analysis SQL, ordered funnel variant, and a description of how to pivot the cohort matrix for a heatmap. Copy prompt Open prompt details Intermediate Single prompt 02 
### Grouping and Aggregation Patterns 

Write SQL aggregation queries to answer these analytical questions. Questions: {{questions}} Tables: {{tables}} Database: {{database}} 1. Standard aggregations: SELECT category,... 
Prompt text Write SQL aggregation queries to answer these analytical questions.

Questions: {{questions}}
Tables: {{tables}}
Database: {{database}}

1. Standard aggregations:
 SELECT
 category,
 COUNT(*) AS row_count,
 COUNT(DISTINCT customer_id) AS unique_customers,
 SUM(amount) AS total_amount,
 AVG(amount) AS avg_amount,
 MIN(created_at) AS first_event,
 MAX(created_at) AS last_event,
 PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY amount) AS median_amount
 FROM orders
 GROUP BY category;

2. HAVING vs WHERE:
 WHERE filters rows BEFORE aggregation
 HAVING filters groups AFTER aggregation
 SELECT customer_id, SUM(amount) AS total
 FROM orders
 WHERE created_at >= '2024-01-01' -- filter rows before grouping
 GROUP BY customer_id
 HAVING SUM(amount) > 1000; -- filter groups after aggregation

3. GROUPING SETS for multi-level summaries:
 SELECT region, product, SUM(revenue)
 FROM sales
 GROUP BY GROUPING SETS (
 (region, product), -- subtotal per region+product
 (region), -- subtotal per region
 (product), -- subtotal per product
 () -- grand total
 );

 ROLLUP: hierarchical subtotals (region → product → grand total)
 GROUP BY ROLLUP (region, product)

 CUBE: all possible combinations of groupings
 GROUP BY CUBE (region, product, channel)

4. Conditional aggregation:
 SELECT
 customer_id,
 SUM(CASE WHEN status = 'completed' THEN amount ELSE 0 END) AS completed_revenue,
 SUM(CASE WHEN status = 'refunded' THEN amount ELSE 0 END) AS refunded_revenue,
 COUNT(CASE WHEN status = 'pending' THEN 1 END) AS pending_count
 FROM orders
 GROUP BY customer_id;

5. Filter clause (cleaner than CASE WHEN for filtered aggregations):
 COUNT(*) FILTER (WHERE status = 'completed') AS completed_count,
 SUM(amount) FILTER (WHERE created_at >= CURRENT_DATE - INTERVAL '30 days') AS last_30d_revenue

Return: SQL queries for each analytical question, explanation of GROUPING SETS when multi-level summaries are needed, and conditional aggregation patterns. Copy prompt Open prompt details Advanced Single prompt 03 
### Statistical Aggregations in SQL 

Write SQL to compute statistical measures and distributions. Analysis: {{analysis}} Data: {{data_description}} Database: {{database}} 1. Descriptive statistics: SELECT COUNT(*)... 
Prompt text Write SQL to compute statistical measures and distributions.

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

Return: complete statistical analysis SQL, histogram bucketing, correlation, and regression queries. Copy prompt Open prompt details 
## Recommended Aggregation and Analytics workflow 
1 
### Cohort and Funnel Analysis in SQL 

Start with a focused prompt in Aggregation and Analytics so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Grouping and Aggregation Patterns 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Statistical Aggregations in SQL 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
