# Clinical Data Quality Audit *AI Prompt *

This prompt is a broad clinical data quality audit tailored to common healthcare data failure modes rather than generic spreadsheet issues. It checks missingness, coding validity, temporal logic, and cross-field consistency in ways that directly affect quality measurement, claims logic, and clinical interpretation. It is most useful before reporting, modeling, or submitting data for operational decision-making. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Audit the quality of this clinical dataset and return a structured quality report.

Check each of the following dimensions:

1. Completeness: which required clinical fields are missing?
 - Critical fields (flag if >5% missing): patient_id, admission_date, discharge_date, primary_diagnosis, discharge_disposition
 - Important fields (flag if >15% missing): attending_physician, procedure_codes, payer, age, sex

2. Validity: are clinical values within plausible ranges?
 - Negative LOS (discharge before admission)
 - Age > 120 or < 0
 - Invalid ICD-10 codes (not in official code list)
 - Discharge disposition codes that don't exist in standard NUBC taxonomy

3. Consistency: are related fields logically consistent?
 - Death as discharge disposition but no mortality flag
 - Pediatric patients with adult diagnoses (and vice versa)
 - Procedure dates outside the admission window

4. Timeliness: when was the data last updated? Are there records with suspiciously old last-modified dates?

Return: quality scorecard with pass/fail per dimension, top 10 specific issues, and estimated % of records affected by each issue. 
```

## When to use this prompt 
Use case 01 
when a clinical dataset will be used for reporting, modeling, or executive decisions 
Use case 02 
when you need a healthcare-specific audit of completeness, validity, and logic 
Use case 03 
when stakeholders suspect temporal or coding inconsistencies in the source data 
Use case 04 
when you want a prioritized defect list before downstream use 

## What the AI should return 

A clinical data quality scorecard by dimension, a ranked issue log with affected-record estimates, and a concise summary of the most important defects to fix first. 

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

Once you have the first result, continue deeper with related prompts in Data Quality and Compliance.
