# Comorbidity Burden Analysis *AI Prompt *

This prompt measures comorbidity burden using recognized clinical scoring systems and ties those scores to outcomes such as length of stay, readmissions, and mortality. It is useful for understanding how illness burden is distributed across the population and how strongly it relates to resource use and risk. It also supports risk adjustment and segmentation for quality or population health analyses. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Calculate and analyze the comorbidity burden of patients in this dataset.

1. Calculate the Charlson Comorbidity Index (CCI) for each patient using their ICD-10 diagnosis codes:
 - Map each ICD-10 code to its CCI weight
 - Sum weights per patient
 - Classify: CCI 0 (no comorbidity), 1–2 (low), 3–4 (moderate), ≥5 (severe)
2. Calculate the Elixhauser Comorbidity Score as an alternative measure
3. Show distribution of CCI scores across the patient population
4. Analyze relationship between CCI and outcomes:
 - Mean LOS by CCI category
 - 30-day readmission rate by CCI category
 - In-hospital mortality rate by CCI category
5. Identify the 10 most common comorbidity combinations (top comorbidity pairs and triples)
6. Map comorbidity burden by age group — show how CCI increases with age

Return a comorbidity burden table, CCI distribution chart, and outcomes by CCI category. 
```

## When to use this prompt 
Use case 01 
when you need a standardized measure of illness burden across patients 
Use case 02 
when comorbidity scores will be used for stratification or risk adjustment 
Use case 03 
when you want to quantify how comorbidity burden relates to outcomes 
Use case 04 
when clinical leaders need a simple view of low, moderate, and severe burden segments 

## What the AI should return 

A comorbidity burden output with Charlson and optionally Elixhauser results, score distribution summaries, age-pattern analysis, and outcome rates by burden category. 

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
