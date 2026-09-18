# Statistical Methods Section Writer *AI Prompt *

Write the statistical methods section of a research paper or technical report for this analysis. Study design: {{study_design}} Data: {{data_description}} Primary analysis: {{pr... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write the statistical methods section of a research paper or technical report for this analysis.

Study design: {{study_design}}
Data: {{data_description}}
Primary analysis: {{primary_analysis}}
Secondary analyses: {{secondary_analyses}}
Software: {{software}}
Journal / reporting standard: {{reporting_standard}} (CONSORT, STROBE, ARRIVE, APA, etc.)

1. Participants and data:
 - Sample description: how were participants/observations selected?
 - Inclusion and exclusion criteria
 - Sample size and statistical rationale (brief reference to power analysis)

2. Statistical methods:
 - Primary outcome: describe the variable and its measurement level
 - Descriptive statistics: state how continuous variables are summarized (mean ± SD, or median [IQR] if non-normal); categorical variables as count (%)
 - Primary analysis: name the test, state the null hypothesis, and specify the significance threshold
 - Secondary analyses: list any planned comparisons or subgroup analyses
 - Multiple testing: if multiple tests, specify the correction method
 - Handling of missing data: complete case, multiple imputation (state the model), or other

3. Model assumptions:
 - State which assumptions were checked and how
 - State what action was taken if assumptions were violated

4. Software and packages:
 - 'All analyses were conducted in R version {{version}} (R Core Team, {{year}}) using the packages {{list}}'
 - or 'Python version X.X using statsmodels X.X, scipy X.X'

5. Reporting standards to reference:
 - CONSORT (for RCTs): report CONSORT flow diagram
 - STROBE (for observational studies): 22-item checklist
 - PRISMA (for systematic reviews): 27-item checklist
 - ARRIVE 2.0 (for animal research): 21 items

6. Preregistration:
 - If applicable: 'The primary outcome, hypotheses, and analysis plan were pre-registered at {{registry}} (registration number: {{number}})'

Return: complete statistical methods section text suitable for inclusion in a research paper, formatted according to the specified reporting standard. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin statistical communication work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Statistical Communication or the wider Statistician library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Participants and data:, Sample description: how were participants/observations selected?, Inclusion and exclusion criteria. The final answer should stay clear, actionable, and easy to review inside a statistical communication workflow for statistician work. 

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

Once you have the first result, continue deeper with related prompts in Statistical Communication.
