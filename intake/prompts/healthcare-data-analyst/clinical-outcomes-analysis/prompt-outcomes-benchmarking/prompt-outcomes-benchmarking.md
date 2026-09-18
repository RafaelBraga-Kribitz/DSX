# Outcomes Benchmarking Chain *AI Prompt *

This chain prompt provides a structured framework for benchmarking multiple core outcomes rather than examining one metric at a time. It introduces risk adjustment, observed-to-expected comparisons, and percentile-style benchmarking so the analyst can separate raw performance from patient mix effects. It is best used when an organization wants a broad outcomes scorecard with clear priorities for deeper follow-up. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Step 1: Calculate observed rates for the top 5 clinical outcome metrics: 30-day readmission, in-hospital mortality, LOS, HAC rate, and discharge to home rate.
Step 2: Risk-adjust each metric using available patient demographics and comorbidities (age, sex, Elixhauser or Charlson comorbidity index, admission type, payer). Calculate expected rates.
Step 3: Compute the observed-to-expected (O/E) ratio for each metric. O/E > 1 indicates worse than expected performance; O/E < 1 indicates better.
Step 4: Compare O/E ratios to CMS national benchmarks and rank the facility's performance percentile for each metric.
Step 5: Identify the 3 metrics with the worst O/E ratios. For each, drill down to the top 3 contributing patient segments or conditions.
Step 6: Write a performance summary report: overall standing, top achievements, priority improvement areas, and recommended next analytical steps. 
```

## When to use this prompt 
Use case 01 
when you need one integrated outcomes benchmarking report instead of separate metric reviews 
Use case 02 
when case mix differences make raw comparisons misleading 
Use case 03 
when leadership wants observed-to-expected performance by major clinical metrics 
Use case 04 
when you need to prioritize which outcome areas deserve deeper root-cause analysis 

## What the AI should return 

A multi-metric benchmarking summary with observed and expected rates, O/E ratios, percentile-style standing versus benchmarks, top problem areas, and recommended next steps. 

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
