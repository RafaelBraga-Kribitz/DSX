# Duplicate Detection at Scale *AI Prompt *

This prompt tackles duplicate detection in large tables where simple manual inspection is not enough. It combines exact duplicate checks, near-duplicate strategies, canonical record selection, and upstream prevention. It is particularly useful for high-volume datasets with compound keys and recurring deduplication problems. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Implement scalable duplicate detection for a large table ({{table_size}} rows) with a compound natural key.

Natural key: {{natural_key_columns}}
Table: {{table_name}}

1. Exact duplicate detection (fast):
 ```sql
 SELECT {{natural_key_columns}}, COUNT(*) AS cnt
 FROM {{table_name}}
 GROUP BY {{natural_key_columns}}
 HAVING COUNT(*) > 1
 ORDER BY cnt DESC
 LIMIT 100
 ```
 - Run this query and report: total duplicate groups, total excess rows, and sample examples

2. Near-duplicate detection for string keys:
 - Phonetic matching: Soundex or Metaphone for name fields
 - MinHash LSH for large-scale fuzzy deduplication (scales to billions of rows)
 - Blocking: reduce comparison space by only comparing within the same first-letter group or zip code

3. Deduplication strategy:
 - Deterministic: define a priority rule for which record to keep (most recent, most complete, specific source)
 - Write a SELECT DISTINCT-equivalent using ROW_NUMBER() to select the canonical record:
 ```sql
 WITH ranked AS (
 SELECT *,
 ROW_NUMBER() OVER (
 PARTITION BY {{natural_key_columns}}
 ORDER BY {{priority_column}} DESC
 ) AS rn
 FROM {{table_name}}
 )
 SELECT * FROM ranked WHERE rn = 1
 ```

4. Prevention (upstream fix):
 - Add a UNIQUE constraint if the warehouse supports it
 - Add a pre-load duplicate check that blocks the load if duplicates are detected in the incoming batch
 - Instrument the source system write path to prevent duplicates at origin

5. Monitoring:
 - Add a daily duplicate count metric to the DQ dashboard
 - Alert if duplicate count increases day-over-day

Return: exact duplicate query, ROW_NUMBER deduplication query, near-duplicate detection approach, and prevention implementation. 
```

## When to use this prompt 
Use case 01 
When duplicate records appear in very large warehouse tables. 
Use case 02 
When the natural key spans multiple columns. 
Use case 03 
When near-duplicate matching is needed for messy string fields. 
Use case 04 
When you need both cleanup logic and prevention controls. 

## What the AI should return 

Return exact duplicate queries, canonical-record selection logic using window functions, an approach for near-duplicate detection at scale, and prevention recommendations. Include monitoring ideas and how to quantify duplicate groups and excess rows. The result should balance warehouse-side cleanup with upstream controls. 

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

Once you have the first result, continue deeper with related prompts in Data Quality.
