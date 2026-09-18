# Readmission Rate Analysis *AI Prompt *

This prompt is designed to quantify short-term readmissions and identify where readmission risk is concentrated across diagnoses, demographics, and discharge patterns. It supports quality improvement, utilization management, and external benchmarking by comparing internal rates with national references where relevant. It is particularly useful for identifying conditions or care pathways that may benefit from transitional care interventions. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze 30-day hospital readmission rates in this dataset.

1. Define readmission: any inpatient admission within 30 days of a prior discharge for the same patient
2. Calculate:
 - Overall 30-day readmission rate
 - 7-day and 90-day readmission rates for comparison
3. Break down readmission rates by:
 - Primary diagnosis category (top 10 conditions)
 - Service line or department
 - Payer type
 - Age group (10-year bands)
 - Day of week of original discharge (are Friday/weekend discharges more likely to readmit?)
4. Identify the top 10 diagnosis pairs: original admission diagnosis vs readmission diagnosis
5. Compare your readmission rate to CMS national benchmarks for the top conditions (AMI, heart failure, pneumonia, COPD, hip/knee replacement, CABG)

Flag any condition or patient segment with a readmission rate more than 2× the overall average. 
```

## When to use this prompt 
Use case 01 
when a hospital wants to monitor or reduce avoidable readmissions 
Use case 02 
when you need to compare internal readmission rates with national benchmarks 
Use case 03 
when you want to identify diagnoses, payers, or age groups driving readmission burden 
Use case 04 
when discharge timing or service line variation may affect post-acute outcomes 

## What the AI should return 

A readmission analysis table with overall and stratified rates, benchmark comparisons, common index-to-readmission diagnosis pairs, and clear flags for segments performing far worse than average. 

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
