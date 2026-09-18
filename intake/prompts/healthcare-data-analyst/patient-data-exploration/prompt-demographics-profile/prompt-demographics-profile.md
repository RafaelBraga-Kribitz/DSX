# Demographics Profile *AI Prompt *

This prompt is built to characterize who is represented in the dataset and whether the patient population reflects the intended care setting or study use case. It goes beyond simple counts by surfacing payer mix, geography, and social risk indicators that often shape utilization, outcomes, and equity analyses. It also helps identify whether the data may underrepresent certain demographic groups, which matters for benchmarking and generalizability. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Create a comprehensive demographic profile of the patient population in this dataset.

1. Age distribution: histogram with 10-year age bands, mean, median, and IQR
2. Sex/gender breakdown: count and percentage
3. Race and ethnicity breakdown if available: count, percentage, and flag if >10% are recorded as 'Unknown' or 'Other'
4. Insurance/payer mix: breakdown by payer type (Medicare, Medicaid, Commercial, Self-pay, Other)
5. Geographic distribution: by zip code, county, or state if available — identify top 10 areas by patient volume
6. Socioeconomic indicators if present: area deprivation index, social determinants of health flags

Compare this population to national or regional benchmarks where possible.
Flag any demographic group that is underrepresented and may affect generalizability of findings. 
```

## When to use this prompt 
Use case 01 
when you need to describe the population served by a hospital, clinic, or program 
Use case 02 
when you are checking representativeness before outcomes or model analysis 
Use case 03 
when leadership asks who is in the dataset by age, payer, geography, or equity factors 
Use case 04 
when you need a demographic baseline for benchmarking or subgroup comparisons 

## What the AI should return 

A demographic profile with tables and charts for age, sex, race/ethnicity, payer mix, geography, and social risk indicators, plus benchmark commentary and notes on underrepresented groups. 

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
