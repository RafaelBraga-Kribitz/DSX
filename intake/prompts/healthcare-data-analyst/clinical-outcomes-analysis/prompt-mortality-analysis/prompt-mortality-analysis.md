# Mortality Analysis *AI Prompt *

This prompt analyzes inpatient mortality in a way that supports both internal performance review and benchmarking. It highlights crude and stratified mortality patterns, time-to-death distributions, and high-risk diagnosis groups that may require deeper case review. It is especially useful when leadership needs to understand whether mortality differences reflect case mix, care processes, or potential quality concerns. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze inpatient mortality in this dataset.

1. Calculate crude in-hospital mortality rate: deaths / total admissions
2. Break down mortality rate by:
 - Primary diagnosis category
 - Age group (especially 65+, 75+, 85+)
 - ICU vs non-ICU admission
 - Elective vs emergency admission
 - Day of week of admission (weekend effect on mortality is well-documented)
3. Compute case mix index (CMI) adjusted mortality if DRG data is available
4. Compare condition-specific mortality rates to national benchmarks:
 - Sepsis: national mortality ~15–20%
 - AMI: national in-hospital mortality ~5–6%
 - Stroke: national in-hospital mortality ~5–8%
5. Analyze time to death distribution: what % of deaths occur within 24 hours, 48 hours, 7 days, and 30 days of admission?
6. Identify the top 5 conditions with mortality rates significantly above benchmark

Return a mortality summary table with benchmark comparisons and flag any rate that exceeds 1.5× the national benchmark. 
```

## When to use this prompt 
Use case 01 
when mortality trends are a priority quality indicator for leadership 
Use case 02 
when you need to benchmark mortality for specific diagnoses or units 
Use case 03 
when you want to see whether mortality differs by age, ICU status, or admission type 
Use case 04 
when suspiciously high mortality groups need escalation for case review 

## What the AI should return 

A mortality report with crude and stratified rates, benchmark comparisons, time-to-death distributions, and a shortlist of conditions or segments with elevated mortality that merit review. 

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
