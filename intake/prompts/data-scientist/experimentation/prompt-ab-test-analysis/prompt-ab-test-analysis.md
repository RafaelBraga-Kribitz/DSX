# A/B Test Analysis *AI Prompt *

This prompt analyzes a standard A/B test with both statistical and business interpretation. It is useful when you need a clean answer to whether the experiment worked and whether the result is large enough to matter. The workflow includes SRM, significance, confidence intervals, and recommendation logic. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze the results of this A/B test.

1. Describe the experiment: what was tested, what is the primary metric, how many users in each group?
2. Check for sample ratio mismatch (SRM): is the split between control and treatment what was intended? Use a chi-squared test.
3. Run the primary hypothesis test:
 - For conversion rates: two-proportion z-test or chi-squared test
 - For continuous metrics: two-sample t-test or Mann-Whitney U test
4. Report: p-value, observed difference, 95% confidence interval for the difference, and statistical power
5. Calculate practical significance: is the observed effect large enough to matter for the business? Compare to the minimum detectable effect.
6. State the recommendation clearly: ship, do not ship, or run a follow-up experiment — and why. 
```

## When to use this prompt 
Use case 01 
You have completed an A/B test and need a decision-ready readout. 
Use case 02 
You want both statistical significance and practical significance. 
Use case 03 
You need to validate the experiment setup before trusting the result. 
Use case 04 
A clear ship / no-ship / follow-up recommendation is required. 

## What the AI should return 

An experiment summary, SRM check, primary statistical test results, p-value and confidence interval, power and practical significance assessment, and a final recommendation with rationale. 

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

Once you have the first result, continue deeper with related prompts in Experimentation.
