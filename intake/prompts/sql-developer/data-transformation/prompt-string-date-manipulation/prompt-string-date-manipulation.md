# String and Date Manipulation *AI Prompt *

Write SQL for these string parsing and date calculation tasks. Tasks: {{tasks}} Database: {{database}} 1. String functions: CONCAT / ||: concatenate strings SUBSTRING(text, star... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write SQL for these string parsing and date calculation tasks.

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

Return: SQL for each transformation task with inline comments explaining the function used. 
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

The AI should return a structured result that covers the main requested outputs, such as String functions:, Date functions:, Interval arithmetic:. The final answer should stay clear, actionable, and easy to review inside a data transformation workflow for sql developer work. 

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
