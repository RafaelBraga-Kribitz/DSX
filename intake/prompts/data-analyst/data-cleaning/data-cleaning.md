# Data Cleaning *AI Prompts *

15 Data Analyst prompts in Data Cleaning. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 13 single prompts · 2 chains. 

## AI prompts in Data Cleaning 
15 prompts Advanced Single prompt 01 
### Automated Cleaning Code Generator 

Automated Cleaning Code Generator is a advanced prompt for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is best suited for direct execution against a real dataset. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. 
Prompt text Analyze this dataset and generate a complete, production-ready Python cleaning script.

The script must:
1. Load the data
2. Fix all data type issues (with explicit dtype mapping)
3. Handle all missing values with the appropriate strategy per column
4. Remove or flag duplicate rows
5. Apply all string standardizations needed
6. Fix date columns to ISO 8601 format
7. Clip or remove outliers where appropriate
8. Assert data quality at the end: row count within expected range, no nulls in key columns, all dates in valid range

Code style requirements:
- Use pandas
- Add a comment above every transformation explaining why it is needed
- Include a final print() summary: rows before, rows after, columns changed
- Make the script idempotent — safe to run multiple times Copy prompt Open prompt details Beginner Single prompt 02 
### Column Renaming Plan 

Column Renaming Plan is a beginner prompt for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Review all column names in this dataset and produce a renaming plan:

1. Identify columns that violate snake_case convention (spaces, camelCase, PascalCase, hyphens, special characters)
2. Identify columns with unclear or ambiguous abbreviations (e.g. 'qty', 'amt', 'dt', 'flg')
3. Identify columns where the name doesn't match the apparent content based on sample values
4. Propose a clear, descriptive snake_case name for each column that needs renaming

Return a table: original_name | issue | proposed_name | reason
Also return a Python code snippet using df.rename() to apply all changes at once. Copy prompt Open prompt details Advanced Chain 03 
### Data Quality Score Chain 

Data Quality Score Chain is a advanced chain for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is structured as a multi-step chain so the AI can reason through the problem in a deliberate order and produce a more complete result. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. 
Prompt text Step 1: Assess completeness — calculate the percentage of non-null values across all columns and rows. Score: (non-null cells / total cells) × 100.
Step 2: Assess consistency — count type mismatches, formatting inconsistencies, and constraint violations. Score: 100 minus one point per violation type found.
Step 3: Assess uniqueness — count exact duplicate rows and near-duplicate rows. Score: (unique rows / total rows) × 100.
Step 4: Assess validity — count values that fail domain rules (impossible numbers, invalid dates, unexpected categoricals). Score: (valid rows / total rows) × 100.
Step 5: Compute an overall Data Quality Score as a weighted average: completeness 30%, consistency 25%, uniqueness 20%, validity 25%.
Step 6: Return a one-page Data Quality Report: score per dimension, overall score, top 5 issues to fix, and estimated effort to resolve each. Copy prompt Open prompt details Beginner Single prompt 04 
### Data Type Fixer 

Data Type Fixer is a beginner prompt for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Audit and fix the data types in this dataset:
- Identify all columns where the stored type does not match the semantic type (e.g. dates stored as strings, IDs stored as floats, booleans stored as integers)
- For each mismatch: show current type, correct type, and a code snippet to convert it
- Check numeric columns for values that contain currency symbols, commas, or percent signs that prevent proper numeric parsing
- Identify any column that should be treated as an ordered categorical rather than a plain string

Return corrected pandas dtype assignments for the full dataset. Copy prompt Open prompt details Intermediate Single prompt 05 
### Date and Time Standardization 

Date and Time Standardization is a intermediate prompt for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Standardize all date and time columns in this dataset:

1. Identify every column that contains dates or times, including those stored as strings
2. Detect all date format variations in use (e.g. 'MM/DD/YYYY', 'DD-Mon-YYYY', 'YYYY-MM-DD', Unix timestamps)
3. Convert all date columns to a single standard format: ISO 8601 (YYYY-MM-DD for dates, YYYY-MM-DDTHH:MM:SS for datetimes)
4. Handle timezone information: identify columns with mixed timezones and convert all to UTC
5. Extract useful components as new columns where relevant: year, month, day_of_week, hour, is_weekend
6. Flag any ambiguous dates where format is unclear (e.g. 01/02/03 could be Jan 2, 2003 or Feb 1, 2003)

Return the conversion code and a before/after sample for each date column. Copy prompt Open prompt details Intermediate Single prompt 06 
### Duplicate Detection and Deduplication 

Duplicate Detection and Deduplication is a intermediate prompt for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Find and handle all duplicate records in this dataset:

1. Exact duplicates — rows identical across all columns. Count them and show 3 examples.
2. Key duplicates — rows with the same primary key or identifier column but different values elsewhere. Which columns differ?
3. Fuzzy duplicates — near-identical records in string columns (name, email, address). Use fuzzy matching with a similarity threshold of 0.85.

For each type, recommend a deduplication strategy (keep first, keep last, merge, manual review).
Apply the strategy and report how many rows were removed. Copy prompt Open prompt details Intermediate Chain 07 
### Full Cleaning Pipeline 

Full Cleaning Pipeline is a intermediate chain for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is structured as a multi-step chain so the AI can reason through the problem in a deliberate order and produce a more complete result. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Step 1: Audit the dataset — list all data quality issues: missing values, duplicates, type mismatches, impossible values, encoding problems, inconsistent formatting.
Step 2: Propose a prioritized cleaning plan. Order tasks from highest to lowest impact. Justify each decision.
Step 3: Execute every cleaning step. Show before and after statistics for each transformation.
Step 4: Validate the cleaned dataset — confirm row count retained, zero remaining missing values (or document intentional exceptions), type consistency.
Step 5: Generate a cleaning report: one row per transformation, with column name, issue type, action taken, and rows affected. Copy prompt Open prompt details Beginner Single prompt 08 
### Impossible Value Detector 

Impossible Value Detector is a beginner prompt for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Scan this dataset for values that are logically impossible or highly implausible:

1. Numeric impossibilities: negative ages, negative prices, quantities above a plausible maximum, percentages above 100 or below 0
2. Date impossibilities: future dates in historical columns, dates before the business existed, end dates before start dates
3. Cross-column contradictions: e.g. refund amount greater than original order amount, child account older than parent account
4. Statistical implausibility: values more than 6 standard deviations from the mean (not just outliers — true anomalies)

For each impossible value found: column, row index, value, why it is impossible, and recommended fix. Copy prompt Open prompt details Beginner Single prompt 09 
### Missing Value Strategy 

Missing Value Strategy is a beginner prompt for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Analyze all missing values in this dataset and recommend a handling strategy for each column.

For numeric columns, choose between: drop, mean imputation, median imputation, forward fill, or model-based imputation.
For categorical columns, choose between: drop, mode imputation, 'Unknown' category, or indicator variable.
For any column with more than 50% missing values, recommend dropping it.

Also scan for hidden nulls: empty strings, 'N/A', 'null', 'None', 'nan', '-', whitespace-only values.

Return a table: column | missing % | recommended strategy | rationale. Copy prompt Open prompt details Intermediate Single prompt 10 
### Numeric Precision and Rounding Audit 

Numeric Precision and Rounding Audit is a intermediate prompt for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Audit the numeric precision in this dataset:

1. For each numeric column, check the number of decimal places used — is it consistent?
2. Identify columns where values are suspiciously round (e.g. all multiples of 100 or 1000) — this may indicate estimation or truncation
3. Check for floating point precision issues (e.g. 0.1 + 0.2 ≠ 0.3 artifacts stored as data)
4. Identify columns that should be integers but are stored as floats (e.g. counts, quantities, IDs)
5. Flag any columns where precision varies significantly across rows (some with 0 decimals, some with 8)

Return recommendations for the correct data type and precision for each numeric column, plus code to apply the corrections. Copy prompt Open prompt details Intermediate Single prompt 11 
### Outlier Treatment 

Outlier Treatment is a intermediate prompt for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Identify and treat outliers in all numeric columns:

1. Detect outliers using IQR (flag values beyond Q1 - 1.5×IQR and Q3 + 1.5×IQR)
2. For each outlier cluster, determine: data entry error, legitimate extreme, or distribution tail?
3. Apply appropriate treatment per column:
 - Cap at percentile boundary (Winsorization) if legitimate extremes
 - Replace with null then impute if likely data error
 - Keep as-is if confirmed legitimate
4. Show before/after statistics for each treated column
5. Document every decision made Copy prompt Open prompt details Intermediate Single prompt 12 
### Referential Integrity Check 

Referential Integrity Check is a intermediate prompt for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Check referential integrity across the tables or joined datasets provided:

1. Identify all foreign key – primary key relationships between tables
2. For each relationship, count:
 - Orphaned records: foreign key values with no matching primary key
 - Unmatched primary keys: records in the parent table with no children
3. Calculate the match rate for each join: what percentage of records join successfully?
4. Show examples of orphaned records and identify the most common missing foreign key values
5. Assess the impact: if orphaned records are dropped, what percentage of rows would be lost from each table?

Return an integrity report table and recommend whether to: drop orphans, impute, or flag for manual review. Copy prompt Open prompt details Advanced Single prompt 13 
### Schema and Constraint Validation 

Schema and Constraint Validation is a advanced prompt for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is best suited for direct execution against a real dataset. The requested output should be comprehensive, methodical, and suitable for expert review or production-style work. 
Prompt text Validate this dataset against data engineering best practices:

Naming: Are column names in snake_case? Any spaces, special characters, or ambiguous abbreviations?
Types: Do types match the semantic meaning? (e.g., IDs stored as float, dates stored as string, booleans stored as int)
Ranges: Are there numeric values outside a plausible range? (negative ages, prices, quantities; future dates in a historical column)
Cardinality: Do categorical columns contain unexpected values or obvious typos?
Referential integrity: If multiple tables are provided, do foreign keys match primary keys?

Return a validation report with columns: field | issue type | severity (error / warning / info) | description | suggested fix. Copy prompt Open prompt details Intermediate Single prompt 14 
### String Standardization 

String Standardization is a intermediate prompt for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is best suited for direct execution against a real dataset. The requested output can include more technical detail, prioritization, and interpretation while still staying practical. 
Prompt text Standardize all text and string columns in this dataset:

1. Trim leading and trailing whitespace from all string fields
2. Detect and normalize inconsistent casing (e.g. 'new york', 'New York', 'NEW YORK' → 'New York')
3. Find and consolidate equivalent values using different spellings or abbreviations (e.g. 'US', 'USA', 'United States', 'U.S.A.')
4. Detect and fix common OCR or data entry errors (e.g. '0' vs 'O', '1' vs 'l')
5. Standardize phone numbers, postcodes, and email addresses to consistent formats where present

Return the full set of replacements applied and the number of rows affected by each. Copy prompt Open prompt details Beginner Single prompt 15 
### Whitespace and Encoding Audit 

Whitespace and Encoding Audit is a beginner prompt for data cleaning. This prompt focuses on identifying and resolving data quality problems that can distort analysis or break downstream workflows. It guides the AI to inspect the dataset systematically, explain the issues clearly, and recommend or apply practical fixes. It is useful when the data is messy, inconsistent, or not yet ready for reliable reporting or modeling. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. 
Prompt text Audit this dataset for whitespace, encoding, and character set issues:

1. Find all string columns that contain leading or trailing whitespace
2. Detect non-printable characters, null bytes, or control characters embedded in string fields
3. Identify any columns with mixed encodings (UTF-8 vs Latin-1 artifacts like Ã© instead of é)
4. Find columns with inconsistent use of quotes, apostrophes, or escaped characters
5. Detect columns where numeric values are stored with thousands separators (1,234 vs 1234) or currency symbols ($1,234)
6. Check for Windows-style line endings (\r\n) in text fields

Return a list of affected columns, the issue type, an example, and the cleaning code to fix it. Copy prompt Open prompt details 
## Recommended Data Cleaning workflow 
1 
### Automated Cleaning Code Generator 

Start with a focused prompt in Data Cleaning so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Column Renaming Plan 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Data Quality Score Chain 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Data Type Fixer 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
