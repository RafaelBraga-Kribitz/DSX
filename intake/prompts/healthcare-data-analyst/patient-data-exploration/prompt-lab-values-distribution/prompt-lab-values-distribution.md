# Lab Values Distribution *AI Prompt *

This prompt is intended for detailed review of laboratory result columns from both a statistical and clinical perspective. It combines descriptive distribution analysis with reference-range interpretation, critical value screening, and plausibility checks so the analyst can distinguish normal variation from dangerous values or likely data-entry errors. It is especially helpful when lab data will be used for cohort definitions, severity adjustment, or predictive modeling. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze the distribution of laboratory values in this dataset.

For each lab test column:
1. Compute: mean, median, std, min, max, and key percentiles (5th, 25th, 75th, 95th)
2. Show the reference range for each lab (normal range) and calculate:
 - % of values below normal range
 - % of values within normal range
 - % of values above normal range
3. Flag clinically critical values (panic values) — values so extreme they require immediate clinical attention:
 - e.g. potassium < 2.5 or > 6.5 mEq/L, glucose < 40 or > 500 mg/dL, sodium < 120 or > 160 mEq/L
4. Check for implausible values that are likely data entry errors (e.g. hemoglobin of 0 or 500)
5. Show missingness rate per lab — high missingness may indicate the test is only ordered for specific patient types

Return a lab profile table and flag any lab with more than 30% critical or implausible values. 
```

## When to use this prompt 
Use case 01 
when your dataset contains multiple lab result columns or repeated lab observations 
Use case 02 
when you need to distinguish clinically abnormal results from data-entry errors 
Use case 03 
when lab distributions will inform cohort rules, severity logic, or model features 
Use case 04 
when you want to screen for missingness patterns in ordered versus rarely ordered tests 

## What the AI should return 

A lab summary table by test showing descriptive statistics, normal-range proportions, critical and implausible value flags, missingness, and a prioritized list of labs that need investigation. 

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
