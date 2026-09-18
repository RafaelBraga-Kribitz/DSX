# SQL *AI Prompts *

7 Data Analyst prompts in SQL. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 1 single prompt · 6 templates. 

## AI prompts in SQL 
7 prompts Intermediate Template 01 
### Cohort Retention Analysis 

Cohort Retention Analysis is a intermediate template for sql. This prompt is meant to generate production-usable SQL for analytical tasks. It gives the AI enough direction to build a query that is not only correct, but also readable, structured, and adapted to the database engine or business question. Use it when you want a query you can review, run, and modify with minimal rework. It is structured as a reusable template, so placeholders can be filled in for a specific table, metric, or business context. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Write a SQL cohort retention analysis using the table {{table_name}} in {{database_type}}.

Definitions:
- Cohort: the month of a user's first {{cohort_event}} recorded in {{date_column}}
- Retention: whether the user performed {{retention_event}} in each subsequent month

The query should:
1. Define cohorts using a CTE that finds each user's first event month
2. Join back to activity data to find which months each user was active
3. Calculate cohort size and retention count per month offset (0, 1, 2, ... N)
4. Return a cohort × month offset matrix with retention percentages

Include comments on each CTE. Database: {{database_type}}. Copy prompt Open prompt details Advanced Template 02 
### Customer Lifetime Value Query 

Customer Lifetime Value Query is a advanced template for sql. This prompt is meant to generate production-usable SQL for analytical tasks. It gives the AI enough direction to build a query that is not only correct, but also readable, structured, and adapted to the database engine or business question. Use it when you want a query you can review, run, and modify with minimal rework. It is structured as a reusable template, so placeholders can be filled in for a specific table, metric, or business context. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. 
Prompt text Write a SQL query to calculate customer lifetime value (LTV) from the transactions table {{table_name}} in {{database_type}}.

The query should compute per customer:
- First purchase date and most recent purchase date
- Total number of orders
- Total revenue
- Average order value
- Purchase frequency (orders per month since first purchase)
- Predicted LTV using the formula: avg_order_value × purchase_frequency × customer_lifespan_months

Also segment customers into LTV tiers: Top 10%, Mid 40%, Bottom 50%.
Return one row per customer with all metrics and the LTV tier label.
Database: {{database_type}}. Copy prompt Open prompt details Beginner Template 03 
### Date Range and Gap Analysis 

Date Range and Gap Analysis is a beginner template for sql. This prompt is meant to generate production-usable SQL for analytical tasks. It gives the AI enough direction to build a query that is not only correct, but also readable, structured, and adapted to the database engine or business question. Use it when you want a query you can review, run, and modify with minimal rework. It is structured as a reusable template, so placeholders can be filled in for a specific table, metric, or business context. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Write a SQL query to analyze the date coverage of the table {{table_name}} using the date column {{date_column}} in {{database_type}}.

The query should:
1. Return min date, max date, and total days spanned
2. Count distinct dates present vs expected dates in the range
3. Identify any missing dates (gaps in the sequence)
4. Show the top 5 largest gaps with start date, end date, and gap length in days
5. Count records per month to show data volume over time

Add a comment explaining how to interpret each section. Copy prompt Open prompt details Intermediate Single prompt 04 
### Funnel Analysis Query 

Funnel Analysis Query is a intermediate prompt for sql. This prompt is meant to generate production-usable SQL for analytical tasks. It gives the AI enough direction to build a query that is not only correct, but also readable, structured, and adapted to the database engine or business question. Use it when you want a query you can review, run, and modify with minimal rework. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Write a SQL funnel analysis for a multi-step user journey in this dataset.

1. Identify the funnel steps from the event data (look for event_name or action columns)
2. For each step, count: users who reached it, users who converted to the next step, and the conversion rate
3. Calculate time between steps for users who completed each transition (median and p90)
4. Identify where the biggest drop-off occurs
5. Segment the funnel by at least one dimension (e.g., device type, acquisition channel, country) if the column exists

Return the full funnel table and a plain-English summary of the biggest opportunity for improvement. Copy prompt Open prompt details Intermediate Template 05 
### Running Metrics with Window Functions 

Running Metrics with Window Functions is a intermediate template for sql. This prompt is meant to generate production-usable SQL for analytical tasks. It gives the AI enough direction to build a query that is not only correct, but also readable, structured, and adapted to the database engine or business question. Use it when you want a query you can review, run, and modify with minimal rework. It is structured as a reusable template, so placeholders can be filled in for a specific table, metric, or business context. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Write a SQL query for the table {{table_name}} using window functions to compute:

1. Running total of {{metric}} ordered by {{date_column}}
2. 7-day and 30-day moving average of {{metric}}
3. Rank of each {{entity_column}} by {{metric}} within each {{partition_column}}
4. Each row's {{metric}} as a percentage of its {{partition_column}} total
5. Period-over-period change: vs prior row and vs same period last year

Database: {{database_type}}. Add a comment explaining each window function used. Copy prompt Open prompt details Advanced Template 06 
### Slowly Changing Dimension Query 

Slowly Changing Dimension Query is a advanced template for sql. This prompt is meant to generate production-usable SQL for analytical tasks. It gives the AI enough direction to build a query that is not only correct, but also readable, structured, and adapted to the database engine or business question. Use it when you want a query you can review, run, and modify with minimal rework. It is structured as a reusable template, so placeholders can be filled in for a specific table, metric, or business context. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. 
Prompt text Write a SQL Type 2 Slowly Changing Dimension (SCD) implementation for the dimension table {{dim_table}} in {{database_type}}.

The table structure uses:
- Natural key: {{natural_key}}
- Tracked attributes that trigger a new version: {{tracked_columns}}
- SCD columns to manage: surrogate_key, valid_from, valid_to, is_current

Write:
1. The CREATE TABLE statement with all required columns
2. The MERGE / UPSERT logic to handle: new records, changed records (expire old, insert new), unchanged records
3. A query to retrieve the current version of each record
4. A query to retrieve the historical version valid at a specific point in time: {{as_of_date}}

Add comments explaining the SCD logic at each step. Copy prompt Open prompt details Beginner Template 07 
### Table Profiling Query 

Table Profiling Query is a beginner template for sql. This prompt is meant to generate production-usable SQL for analytical tasks. It gives the AI enough direction to build a query that is not only correct, but also readable, structured, and adapted to the database engine or business question. Use it when you want a query you can review, run, and modify with minimal rework. It is structured as a reusable template, so placeholders can be filled in for a specific table, metric, or business context. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Write a SQL query to profile the table {{table_name}} in {{database_type}}.

The query should return:
- Total row count
- Distinct value count per column
- NULL count and NULL percentage per column
- Min, max, and average for numeric columns
- Top 5 most frequent values for categorical columns

Structure the output so each column appears as a separate row with all metrics in one result set.
Add comments explaining each section. Copy prompt Open prompt details 
## Recommended SQL workflow 
1 
### Cohort Retention Analysis 

Start with a focused prompt in SQL so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Customer Lifetime Value Query 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Date Range and Gap Analysis 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Funnel Analysis Query 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
