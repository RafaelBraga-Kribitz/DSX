# Chronic Disease Cohort *AI Prompt *

This prompt is designed to define a chronic disease cohort in a defensible, repeatable way before downstream analysis begins. It includes longitudinal inclusion logic, exclusion of weak rule-out signals, and a comparison between cohort and non-cohort patients so the disease population can be understood in clinical and utilization terms. It is useful for registry creation, quality programs, and disease management reporting. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build and profile a chronic disease patient cohort from this dataset.

Target disease: {{disease}} (e.g. Type 2 Diabetes, Heart Failure, COPD, CKD)

1. Identify cohort inclusion criteria using ICD-10 codes for {{disease}} — list the specific codes used
2. Apply inclusion and exclusion criteria:
 - Include: patients with ≥2 diagnoses of {{disease}} at least 30 days apart (to confirm chronic status)
 - Exclude: patients with only a rule-out or screening code
3. Profile the cohort:
 - Size: how many patients qualify?
 - Demographics: age, sex, payer mix
 - Top comorbidities and their prevalence rates
 - Average number of hospitalizations, ED visits, and outpatient encounters per year
4. Compute disease severity distribution if a severity classification exists (e.g. HbA1c ranges for diabetes, NYHA class for heart failure)
5. Compare cohort demographics and utilization to the non-{{disease}} patient population

Return a cohort definition table and a summary profile comparing cohort vs non-cohort patients. 
```

## When to use this prompt 
Use case 01 
when building a disease registry or service-line cohort definition 
Use case 02 
when a chronic disease program needs a defensible inclusion logic 
Use case 03 
when you want to compare disease patients with the general population 
Use case 04 
when utilization and comorbidity patterns are needed for program design 

## What the AI should return 

A cohort definition section listing inclusion and exclusion logic, followed by a cohort profile comparing disease and non-disease populations on demographics, comorbidities, severity, and utilization. 

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

Once you have the first result, continue deeper with related prompts in Cohort Analysis.
