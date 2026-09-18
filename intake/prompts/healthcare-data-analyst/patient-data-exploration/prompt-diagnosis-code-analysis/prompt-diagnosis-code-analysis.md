# Diagnosis Code Analysis *AI Prompt *

This prompt helps analysts understand how diagnosis coding is being used across encounters and whether the diagnosis data is analytically reliable. It surfaces coding frequency, major disease categories, specificity problems, invalid codes, and common comorbidity combinations that shape both quality reporting and risk stratification. It is useful for both clinical analytics and revenue-cycle oriented reviews of diagnosis documentation quality. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze the diagnosis codes (ICD-10-CM) in this dataset.

1. Count the total number of unique ICD-10 codes present
2. Show the top 20 most frequent primary diagnoses with code, description, count, and % of encounters
3. Group diagnoses by ICD-10 chapter (first 3 characters) — what are the top 5 disease categories?
4. Check coding quality:
 - What % of diagnoses use unspecified codes (codes ending in '9' or containing 'unspecified')? High rates suggest poor coding specificity.
 - Are there any invalid or non-existent ICD-10 codes?
 - Is there a mix of ICD-9 and ICD-10 codes?
5. Identify the top 10 comorbidity pairs — which two diagnoses most frequently appear together for the same patient?
6. Flag any patients with an unusually high number of diagnosis codes per encounter (>15 codes may indicate upcoding) 
```

## When to use this prompt 
Use case 01 
when diagnosis codes are central to cohort building, risk adjustment, or reporting 
Use case 02 
when you need to assess ICD coding specificity and validity 
Use case 03 
when you suspect a mix of coding systems or heavy use of unspecified diagnoses 
Use case 04 
when you want to understand the most common conditions and comorbidity patterns 

## What the AI should return 

A diagnosis coding report with code counts, top primary diagnoses, chapter-level groupings, coding quality checks, comorbidity pairs, and flags for invalid codes, unspecified coding, or unusually dense encounters. 

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

Once you have the first result, continue deeper with related prompts in Patient Data Exploration.
