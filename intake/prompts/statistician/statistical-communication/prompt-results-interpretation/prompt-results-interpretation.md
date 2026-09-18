# Statistical Results Interpretation *AI Prompt *

Interpret and communicate these statistical results for a non-technical audience. Statistical results: {{results}} Audience: {{audience}} (business stakeholders, clinical team,... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Interpret and communicate these statistical results for a non-technical audience.

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

Return: plain-language interpretation of each result, effect size with CI, practical significance assessment, and caveats. 
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

The AI should return a structured result that covers the main requested outputs, such as Lead with the scientific conclusion, not the statistic:, Start with what it means for people and decisions, not the p-value, Wrong: 'The t-test yielded t(48) = 2.3, p = 0.026'. The final answer should stay clear, actionable, and easy to review inside a statistical communication workflow for statistician work. 

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
