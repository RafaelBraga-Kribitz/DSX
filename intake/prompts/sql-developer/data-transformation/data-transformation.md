# Data Transformation *AI Prompts *

3 SQL Developer prompts in Data Transformation. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 3 single prompts. 

## AI prompts in Data Transformation 
3 prompts Intermediate Single prompt 01 
### Data Cleaning in SQL 

Write SQL to clean and standardize this dirty dataset. Issues identified: {{issues}} (nulls, duplicates, format inconsistencies, outliers, invalid values) Table: {{table}} Datab... 
Prompt text Write SQL to clean and standardize this dirty dataset.

Issues identified: {{issues}} (nulls, duplicates, format inconsistencies, outliers, invalid values)
Table: {{table}}
Database: {{database}}

1. NULL handling:
 COALESCE(column, default_value): return first non-null value
 NULLIF(column, 0): convert 0 (or empty string) to NULL
 IS NULL / IS NOT NULL: never use = NULL

 Replace NULL with 'Unknown':
 COALESCE(status, 'Unknown') AS status

 NULL-safe comparison:
 WHERE status IS DISTINCT FROM 'cancelled'
 -- equivalent to: WHERE status != 'cancelled' OR status IS NULL

2. String standardization:
 Remove extra whitespace: REGEXP_REPLACE(name, '\s+', ' ', 'g')
 Normalize email: TRIM(LOWER(email))
 Extract only digits: REGEXP_REPLACE(phone, '[^0-9]', '', 'g')
 Standardize state codes: UPPER(TRIM(state))

3. Date standardization:
 -- Handle multiple date formats in one column (PostgreSQL):
 CASE
 WHEN raw_date ~ '^\d{4}-\d{2}-\d{2}$' THEN raw_date::date
 WHEN raw_date ~ '^\d{2}/\d{2}/\d{4}$' THEN TO_DATE(raw_date, 'MM/DD/YYYY')
 ELSE NULL
 END AS clean_date

4. Outlier detection and flagging:
 -- Flag values more than 3 standard deviations from the mean
 SELECT *,
 ABS(amount - AVG(amount) OVER ()) / NULLIF(STDDEV(amount) OVER (), 0) AS z_score
 FROM transactions
 WHERE ABS(amount - AVG(amount) OVER ()) / NULLIF(STDDEV(amount) OVER (), 0) > 3;

5. Invalid value replacement:
 CASE
 WHEN age < 0 OR age > 120 THEN NULL
 ELSE age
 END AS cleaned_age

6. Data profiling queries:
 -- Column completeness
 SELECT
 COUNT(*) AS total_rows,
 COUNT(email) AS non_null_email,
 COUNT(DISTINCT email) AS unique_emails,
 SUM(CASE WHEN email ~ '^[^@]+@[^@]+\.[^@]+$' THEN 0 ELSE 1 END) AS invalid_emails
 FROM users;

Return: SQL cleaning queries for each identified issue, data profiling queries for quality assessment, and update statements to persist the cleaned values. Copy prompt Open prompt details Advanced Single prompt 02 
### Pivoting and Unpivoting Data 

Write SQL to pivot rows to columns and unpivot columns to rows. Source data: {{data_description}} Desired output: {{desired_output}} Database: {{database}} 1. Manual pivot with... 
Prompt text Write SQL to pivot rows to columns and unpivot columns to rows.

Source data: {{data_description}}
Desired output: {{desired_output}}
Database: {{database}}

1. Manual pivot with CASE WHEN (works in all databases):
 -- Pivot: rows of (product, month, revenue) → one column per month
 SELECT
 product,
 SUM(CASE WHEN month = 'Jan' THEN revenue ELSE 0 END) AS jan_revenue,
 SUM(CASE WHEN month = 'Feb' THEN revenue ELSE 0 END) AS feb_revenue,
 SUM(CASE WHEN month = 'Mar' THEN revenue ELSE 0 END) AS mar_revenue
 FROM monthly_sales
 GROUP BY product;

2. CROSSTAB (PostgreSQL tablefunc extension):
 CREATE EXTENSION IF NOT EXISTS tablefunc;

 SELECT * FROM CROSSTAB(
 'SELECT product, month, revenue
 FROM monthly_sales
 ORDER BY 1, 2',
 'VALUES (''Jan''),(''Feb''),(''Mar'')'
 ) AS ct(product TEXT, jan NUMERIC, feb NUMERIC, mar NUMERIC);

3. Unpivot: columns to rows (PostgreSQL UNNEST approach):
 -- Transform: one row with jan_rev, feb_rev, mar_rev → 3 rows
 SELECT
 product,
 month_name,
 revenue
 FROM monthly_wide_table,
 LATERAL (
 VALUES
 ('Jan', jan_revenue),
 ('Feb', feb_revenue),
 ('Mar', mar_revenue)
 ) AS t(month_name, revenue);

4. Dynamic pivot (when column values are unknown at query time):
 In SQL this requires dynamic SQL or a two-step approach:
 Step 1: SELECT DISTINCT month FROM monthly_sales → get the list of columns
 Step 2: Build and execute dynamic SQL with EXECUTE in a PL/pgSQL function

5. BigQuery / Snowflake PIVOT syntax:
 -- BigQuery:
 SELECT * FROM monthly_sales
 PIVOT (SUM(revenue) FOR month IN ('Jan', 'Feb', 'Mar'));

 -- Snowflake:
 SELECT * FROM monthly_sales
 PIVOT (SUM(revenue) FOR month IN ('Jan', 'Feb', 'Mar'))
 AS p (product, jan, feb, mar);

Return: pivot SQL for the specific data, unpivot SQL if needed, and dynamic pivot approach if the column values are dynamic. Copy prompt Open prompt details Intermediate Single prompt 03 
### String and Date Manipulation 

Write SQL for these string parsing and date calculation tasks. Tasks: {{tasks}} Database: {{database}} 1. String functions: CONCAT / ||: concatenate strings SUBSTRING(text, star... 
Prompt text Write SQL for these string parsing and date calculation tasks.

Tasks: {{tasks}}
Database: {{database}}

1. String functions:
 CONCAT / ||: concatenate strings
 SUBSTRING(text, start, length): extract substring
 REGEXP_REPLACE(text, pattern, replacement): replace with regex
 SPLIT_PART(text, delimiter, part): split and extract nth part
 TRIM / LTRIM / RTRIM: remove whitespace or characters
 LOWER / UPPER: normalize case
 REGEXP_MATCHES: extract all regex captures

 Email domain extraction:
 SPLIT_PART(email, '@', 2) AS email_domain

 Normalize phone number:
 REGEXP_REPLACE(phone, '[^0-9]', '', 'g') AS clean_phone

2. Date functions:
 DATE_TRUNC('month', timestamp): truncate to month start
 DATE_PART('year', timestamp): extract year
 EXTRACT(DOW FROM timestamp): day of week (0=Sunday)
 CURRENT_DATE, NOW()

 Days between two dates:
 (end_date::date - start_date::date) AS days_elapsed

 First day of next month:
 DATE_TRUNC('month', CURRENT_DATE) + INTERVAL '1 month'

 Age in complete years:
 DATE_PART('year', AGE(birth_date)) AS age_years

3. Interval arithmetic:
 created_at + INTERVAL '30 days' AS trial_end
 WHERE event_date BETWEEN CURRENT_DATE - INTERVAL '7 days' AND CURRENT_DATE

4. Time zone handling:
 event_timestamp AT TIME ZONE 'UTC' AT TIME ZONE 'America/New_York' AS local_time
 -- Always store timestamps in UTC; convert on display only

5. JSON extraction (PostgreSQL):
 properties->>'user_id' AS user_id -- text extraction
 (properties->>'amount')::NUMERIC AS amount -- cast to numeric
 properties @> '{"plan": "premium"}' -- containment check
 JSONB_ARRAY_ELEMENTS(properties->'items') -- expand array

Return: SQL for each transformation task with inline comments explaining the function used. Copy prompt Open prompt details 
## Recommended Data Transformation workflow 
1 
### Data Cleaning in SQL 

Start with a focused prompt in Data Transformation so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Pivoting and Unpivoting Data 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### String and Date Manipulation 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
