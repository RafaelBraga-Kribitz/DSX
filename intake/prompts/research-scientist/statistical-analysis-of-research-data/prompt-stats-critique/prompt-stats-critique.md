# Peer Review Statistics Critique *AI Prompt *

Critically evaluate the statistical methods and reporting in this paper I am reviewing. Paper abstract/methods/results: {{paper_content}} Systematically check for the following... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Critically evaluate the statistical methods and reporting in this paper I am reviewing.

Paper abstract/methods/results: {{paper_content}}

Systematically check for the following statistical issues:

1. Study design and causal inference:
 - Does the study design support the causal claims made in the discussion?
 - Are observational data used to support causal conclusions without adequate justification?
 - Is confounding adequately addressed?

2. Sample size and power:
 - Was a power analysis reported? Does the achieved sample size match the power analysis?
 - Is the study adequately powered for the primary outcome? (Effect size and sample size allow calculation)
 - Is the study appropriately cautious about null results given potential underpowering?

3. Multiple comparisons:
 - How many outcomes were tested? Were corrections for multiple comparisons applied?
 - Are results from exploratory analyses clearly labeled as such?
 - Is there evidence of outcome switching (primary outcome appears to have been changed post-hoc)?

4. Effect sizes and practical significance:
 - Are effect sizes reported for all main findings?
 - Are confidence intervals reported?
 - Is the distinction between statistical significance and practical significance made?

5. Specific red flags:
 - p-hacking indicators: p-values clustered just below 0.05, unusual number of 'marginally significant' results (p = .06, .07, .08)
 - HARKing (Hypothesizing After Results are Known): post-hoc hypotheses presented as a priori
 - Selective reporting: were all pre-specified outcomes reported? Are non-significant results reported?
 - Base rate neglect: does the probability of a true finding justify the strength of the conclusion?
 - Overfitting: in predictive models, is there a held-out test set? Is in-sample fit used to claim out-of-sample performance?

6. For each issue identified:
 - Severity: does this issue invalidate the conclusions, weaken them, or require clarification?
 - Recommended author action: specific request for analysis, reporting, or language change
 - Reviewer language: suggest wording appropriate for a peer review

Return: structured peer review critique organized by issue, severity ratings, and specific revision requests. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin statistical analysis of research data work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Statistical Analysis of Research Data or the wider Research Scientist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Study design and causal inference:, Does the study design support the causal claims made in the discussion?, Are observational data used to support causal conclusions without adequate justification?. The final answer should stay clear, actionable, and easy to review inside a statistical analysis of research data workflow for research scientist work. 

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

Once you have the first result, continue deeper with related prompts in Statistical Analysis of Research Data.
