# Complication Rate Tracking *AI Prompt *

This prompt focuses on hospital-acquired complications and other adverse events that have both patient safety and reimbursement implications. It combines coding-based identification, rate calculation, benchmark comparison, and financial impact estimation to make the results useful for both quality and operational leaders. It is well suited for monitoring CMS-sensitive safety events and prioritizing prevention work by unit or service. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Identify and analyze hospital-acquired complications (HACs) and adverse events in this dataset.

1. Identify the following HAC categories using ICD-10 codes:
 - Hospital-acquired pressure injuries (POA flag = N for HAPI codes)
 - Catheter-associated urinary tract infections (CAUTI)
 - Central line-associated bloodstream infections (CLABSI)
 - Surgical site infections (SSI)
 - Falls with injury
 - Venous thromboembolism (DVT/PE) with POA = N
2. Calculate HAC rate per 1,000 patient days for each category
3. Compare to CMS national rates and flag any HAC above the 75th percentile nationally
4. Analyze HACs by:
 - Unit or department
 - Shift (if time data is available)
 - Patient risk factors (age, LOS, comorbidities)
5. Calculate the estimated financial impact: average CMS HAC payment reduction × number of HAC cases

Return a HAC dashboard table with rates, benchmarks, and estimated financial impact per category. 
```

## When to use this prompt 
Use case 01 
when patient safety teams are tracking hospital-acquired conditions 
Use case 02 
when coding and POA flags are needed to distinguish acquired complications 
Use case 03 
when finance wants to estimate reimbursement impact of HAC performance 
Use case 04 
when leaders need a unit-level view of preventable adverse event burden 

## What the AI should return 

A hospital-acquired complication dashboard showing rates per 1,000 patient days, benchmark comparisons, segment breakdowns, and estimated financial impact by complication category. 

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

Once you have the first result, continue deeper with related prompts in Clinical Outcomes Analysis.
