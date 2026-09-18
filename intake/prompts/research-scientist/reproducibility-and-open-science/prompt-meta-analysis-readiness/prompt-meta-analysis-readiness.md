# Meta-Analysis Readiness *AI Prompt *

Prepare my study to maximize its contribution to future meta-analyses of this research area. Study details: {{study_details}} Field: {{field}} Meta-analyses synthesize evidence... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Prepare my study to maximize its contribution to future meta-analyses of this research area.

Study details: {{study_details}}
Field: {{field}}

Meta-analyses synthesize evidence across studies, but are only as good as the data provided by individual studies. Most studies are meta-analysis-unfriendly due to incomplete reporting.

1. Effect size reporting requirements:
 Report ALL of the following for every primary and secondary outcome:
 - Sample size per group (or total N for correlational studies)
 - Means and standard deviations per group (for continuous outcomes)
 - The correlation between time points (for pre-post designs without a control group)
 - Cell frequencies (for categorical outcomes)
 - The exact test statistic (t, F, z, χ²) and degrees of freedom
 - Exact p-value
 - Effect size (d, r, OR, RR) with 95% CI
 These allow meta-analysts to compute any effect size metric from your data.

2. Complete reporting for non-significant results:
 - Non-significant results are as important to meta-analysis as significant ones
 - Report exact statistics even for null results — 'p = .42' is far more informative than 'ns'
 - Null results suppressed by publication bias cause meta-analyses to overestimate effects

3. Moderator variables:
 Report participant characteristics that are common moderators in {{field}}:
 - Demographic variables: age (mean, SD, range), sex/gender (proportions), relevant clinical characteristics
 - Study characteristics: setting, assessor training, duration, intensity
 - These allow meta-analysts to test heterogeneity and identify moderators

4. PRISMA / CONSORT reporting:
 - Clinical trials: follow CONSORT checklist for complete reporting
 - Observational studies: follow STROBE checklist
 - Systematic reviews: follow PRISMA checklist
 - These checklists ensure all information needed for meta-analysis is reported

5. Data and code sharing for meta-analytic use:
 - Provide participant-level data when possible (allows individual-patient-data meta-analysis)
 - At minimum: provide a summary statistics table with all the values in point 1 above
 - Share in a format compatible with meta-analysis software (metafor in R, Comprehensive Meta-Analysis, RevMan)

6. Registered in a trials registry:
 - Clinical trials: PROSPERO, ClinicalTrials.gov
 - Psychological studies: OSF, AsPredicted
 - Registry number must appear in the paper for inclusion in high-quality meta-analyses

Return: meta-analysis reporting checklist, summary statistics table template, CONSORT/STROBE/PRISMA compliance check, and data sharing format recommendation. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin reproducibility and open science work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Reproducibility and Open Science or the wider Research Scientist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Effect size reporting requirements:, Sample size per group (or total N for correlational studies), Means and standard deviations per group (for continuous outcomes). The final answer should stay clear, actionable, and easy to review inside a reproducibility and open science workflow for research scientist work. 

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

Once you have the first result, continue deeper with related prompts in Reproducibility and Open Science.
