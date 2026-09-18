# Statistical Communication *AI Prompts *

2 Statistician prompts in Statistical Communication. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → intermediate levels and 2 single prompts. 

## AI prompts in Statistical Communication 
2 prompts Intermediate Single prompt 01 
### Statistical Methods Section Writer 

Write the statistical methods section of a research paper or technical report for this analysis. Study design: {{study_design}} Data: {{data_description}} Primary analysis: {{pr... 
Prompt text Write the statistical methods section of a research paper or technical report for this analysis.

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

Return: complete statistical methods section text suitable for inclusion in a research paper, formatted according to the specified reporting standard. Copy prompt Open prompt details Beginner Single prompt 02 
### Statistical Results Interpretation 

Interpret and communicate these statistical results for a non-technical audience. Statistical results: {{results}} Audience: {{audience}} (business stakeholders, clinical team,... 
Prompt text Interpret and communicate these statistical results for a non-technical audience.

Statistical results: {{results}}
Audience: {{audience}} (business stakeholders, clinical team, policymakers, general public)
Context: {{context}}

1. Lead with the scientific conclusion, not the statistic:
 - Start with what it means for people and decisions, not the p-value
 - Wrong: 'The t-test yielded t(48) = 2.3, p = 0.026'
 - Right: 'Patients receiving the new treatment recovered an average of 3 days faster than controls'

2. Effect size before statistical significance:
 - Report the magnitude of the effect, not just whether it is statistically significant
 - 'The intervention increased sales by 12% (95% CI: 7% to 17%)'
 - A large sample can produce a statistically significant but practically meaningless effect
 - A small sample can fail to detect a large and important effect

3. Confidence intervals over p-values:
 - Report 95% CIs alongside point estimates
 - CI communicates uncertainty: a wide interval means we are less sure about the true effect
 - 'We are 95% confident the true effect is between 7% and 17%'
 - Never say 'the probability that the true value is in this interval is 95%' (frequentist CI does not have this interpretation)

4. Practical significance:
 - Is the effect large enough to matter for the decision at hand?
 - Provide a concrete translation: 'An 8% reduction in churn would save approximately $2M annually'
 - Benchmark against a meaningful threshold, not just 'statistically significant'

5. What statistical significance does and does NOT mean:
 - It means: if the null hypothesis were true, we would rarely see results this extreme by chance
 - It does NOT mean: the effect is large, important, replicable, or clinically meaningful
 - p > 0.05 does NOT mean the null hypothesis is true

6. Uncertainty and limitations:
 - What assumptions could be violated?
 - What alternative explanations cannot be ruled out?
 - How would the interpretation change if the sample were different?

Return: plain-language interpretation of each result, effect size with CI, practical significance assessment, and caveats. Copy prompt Open prompt details 
## Recommended Statistical Communication workflow 
1 
### Statistical Methods Section Writer 

Start with a focused prompt in Statistical Communication so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Statistical Results Interpretation 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt
