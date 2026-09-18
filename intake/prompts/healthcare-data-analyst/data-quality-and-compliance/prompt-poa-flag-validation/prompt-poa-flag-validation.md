# POA Flag Validation *AI Prompt *

This prompt is designed to validate present-on-admission coding, which is essential for distinguishing pre-existing conditions from complications that occurred during the hospitalization. It helps analysts detect documentation gaps, coding inconsistencies, and HAC-related payment exposure. It is particularly valuable in inpatient quality, coding compliance, and CMS-focused reimbursement reviews. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Validate the Present on Admission (POA) flags in this dataset.

POA flags indicate whether a diagnosis existed before the hospital admission. Correct POA coding is critical for quality reporting and HAC identification.

1. Check completeness: what % of secondary diagnoses have a POA flag? CMS requires POA for all diagnoses on inpatient claims.
2. Check value distribution: what % are Y (yes), N (no), U (unknown), W (clinically undetermined), 1 (exempt)?
 - Flag if >10% are U or W — this indicates documentation gaps
3. Validate HAC-relevant codes: for conditions that are CMS Hospital-Acquired Conditions (e.g. CAUTI, CLABSI, pressure injuries, DVT), verify that POA = N or W is correctly assigned
4. Check for impossible POA assignments:
 - Chronic diseases like diabetes, COPD, hypertension should almost never have POA = N
 - Flag any case where a common chronic condition has POA = N (likely a coding error)
5. Calculate the financial impact: how many cases have HAC conditions with POA = N, triggering potential CMS payment reductions?

Return a POA validation report with error rates per condition category and estimated payment impact. 
```

## When to use this prompt 
Use case 01 
when inpatient diagnosis coding includes POA indicators 
Use case 02 
when HAC identification or CMS payment risk is being reviewed 
Use case 03 
when documentation teams want to reduce unknown or clinically undetermined POA usage 
Use case 04 
when you suspect chronic conditions are being incorrectly marked as not present on admission 

## What the AI should return 

A POA validation report with completeness and value-distribution tables, HAC-specific error checks, chronic-condition anomaly flags, and an estimate of payment impact exposure. 

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
