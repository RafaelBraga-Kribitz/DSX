# Readmission Risk Cohort Chain *AI Prompt *

This chain prompt creates a full readmission-risk workflow centered on the LACE score and actual readmission outcomes. It moves from cohort definition to risk scoring, validation, profiling of high-risk patients, and practical prioritization for outreach. It is particularly helpful for organizations building or evaluating transitional care and readmission prevention programs. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Define the index admission cohort — all inpatient discharges in the study period, excluding deaths, AMA discharges, and transfers to other acute facilities.
Step 2: Calculate the LACE score for each patient (Length of stay, Acuity of admission, Charlson Comorbidity Index, ED visits in past 6 months). Classify: low risk (0–4), moderate (5–9), high (≥10).
Step 3: Validate LACE score performance against actual 30-day readmissions in the dataset: compute AUC-ROC, sensitivity, and specificity at each risk threshold.
Step 4: Profile the high-risk cohort (LACE ≥10): size, top diagnoses, demographics, payer mix, and social risk factors.
Step 5: Identify which high-risk patients were not readmitted — what interventions or patient factors may have protected them?
Step 6: Prioritize the top 50 patients by readmission risk for care management outreach. Return a ranked list with LACE score, primary diagnosis, payer, and suggested intervention type. 
```

## When to use this prompt 
Use case 01 
when building a readmission prevention list for outreach teams 
Use case 02 
when you want to validate how well LACE works in your own data 
Use case 03 
when you need to understand what differentiates high-risk from protected patients 
Use case 04 
when population health teams need a ranked intervention list rather than just summary rates 

## What the AI should return 

A full readmission-risk workflow output including index cohort definition, LACE scoring results, validation metrics, high-risk cohort profile, and a ranked outreach list with intervention suggestions. 

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
