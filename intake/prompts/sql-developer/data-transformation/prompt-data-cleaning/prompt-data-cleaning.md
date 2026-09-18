# Data Cleaning in SQL *AI Prompt *

Write SQL to clean and standardize this dirty dataset. Issues identified: {{issues}} (nulls, duplicates, format inconsistencies, outliers, invalid values) Table: {{table}} Datab... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write SQL to clean and standardize this dirty dataset.

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

Return: SQL cleaning queries for each identified issue, data profiling queries for quality assessment, and update statements to persist the cleaned values. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin data transformation work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Data Transformation or the wider SQL Developer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as NULL handling:, String standardization:, Date standardization:. The final answer should stay clear, actionable, and easy to review inside a data transformation workflow for sql developer work. 

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

Once you have the first result, continue deeper with related prompts in Data Transformation.
