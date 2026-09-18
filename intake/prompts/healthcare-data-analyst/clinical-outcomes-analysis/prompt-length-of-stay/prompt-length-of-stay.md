# Length of Stay Analysis *AI Prompt *

This prompt evaluates inpatient length of stay using methods appropriate for heavily right-skewed hospital utilization data. It emphasizes median and geometric mean comparisons, highlights outlier stays, and quantifies excess bed-day consumption beyond expected norms. It is useful for throughput improvement, case management reviews, and benchmarking against national LOS expectations. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze inpatient length of stay (LOS) in this dataset.

1. Calculate overall LOS statistics: mean, median, std, 25th, 75th, 90th, 95th percentiles
2. Use median rather than mean as the primary metric — LOS is right-skewed and mean is sensitive to outliers
3. Break down median LOS by:
 - Primary diagnosis (top 15 conditions)
 - Service line or unit
 - Discharge disposition (home, SNF, rehab, AMA, death)
 - Payer type
 - ICU vs non-ICU stay
4. Identify geometric mean LOS per DRG and compare to CMS national geometric mean LOS benchmarks
5. Flag outlier stays: admissions with LOS > 3× the condition-specific median
6. Analyze LOS trends over time: is average LOS increasing or decreasing by quarter?
7. Estimate excess days: for outlier stays, how many total bed-days were consumed beyond the expected LOS?

Return a LOS breakdown table and a trend chart by month or quarter. 
```

## When to use this prompt 
Use case 01 
when bed capacity, throughput, or case management efficiency is under review 
Use case 02 
when you need a diagnosis- or unit-level breakdown of length of stay 
Use case 03 
when leadership asks how many excess bed-days are being consumed 
Use case 04 
when you want to compare internal LOS performance with DRG benchmarks 

## What the AI should return 

A length-of-stay report with overall statistics, subgroup medians, benchmark comparisons, outlier-stay analysis, excess bed-day estimates, and a time trend visualization. 

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
