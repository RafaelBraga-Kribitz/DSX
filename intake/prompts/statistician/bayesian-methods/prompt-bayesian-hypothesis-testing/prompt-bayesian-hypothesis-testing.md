# Bayesian Hypothesis Testing *AI Prompt *

Perform a Bayesian analysis as an alternative or complement to frequentist hypothesis testing. Hypothesis: {{hypothesis}} Data: {{data}} Prior information: {{prior_info}} (liter... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Perform a Bayesian analysis as an alternative or complement to frequentist hypothesis testing.

Hypothesis: {{hypothesis}}
Data: {{data}}
Prior information: {{prior_info}} (literature values, expert knowledge, or 'weakly informative')

1. The Bayesian framework:
 - Prior: P(theta) — your belief about the parameter before seeing the data
 - Likelihood: P(data | theta) — how probable is the data at each value of theta?
 - Posterior: P(theta | data) ∝ P(data | theta) x P(theta)
 - The posterior combines prior belief with the evidence from the data

2. Prior specification:

 Informative prior:
 - Based on previous studies or expert knowledge
 - Example: beta(8, 4) for a success probability believed to be around 0.67
 - Must be documented and justified

 Weakly informative prior:
 - Provides mild regularization without dominating the data
 - Example: Normal(0, 2.5) on logistic regression coefficients (Gelman's recommendation)
 - Prevents extreme estimates while allowing the data to speak

 Non-informative / reference prior:
 - Jeffreys prior: invariant under reparameterization
 - Flat prior: uniform over all values (often improper and not recommended)

3. Bayes factor:
 BF = P(data | H1) / P(data | H0)
 - BF > 10: strong evidence for H1
 - BF 3-10: moderate evidence
 - BF 1-3: weak evidence
 - BF < 1: evidence favors H0
 - BF 1/10 to 1/3: moderate evidence for H0
 - Interpretation: the Bayes factor is how much more probable the data is under H1 vs H0

4. Posterior credible interval:
 - The 95% credible interval contains the true parameter with 95% posterior probability
 - Contrast with frequentist CI: the frequentist CI does NOT have a probability interpretation for the parameter
 - Highest Density Interval (HDI): the shortest interval containing 95% of the posterior mass

5. Decision making under uncertainty:
 - Region of Practical Equivalence (ROPE): define a range of effect sizes that are practically negligible
 - If the posterior is entirely within the ROPE: accept H0 as practically equivalent
 - If the posterior is entirely outside the ROPE: reject H0
 - If the posterior overlaps the ROPE: suspend judgment

Return: posterior distribution, Bayes factor, 95% credible interval, and ROPE-based decision. 
```

## When to use this prompt 

Use case 01: Use it when you want to begin bayesian methods work without writing the first draft from scratch. 
Use case 02: Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03: Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04: Use it when you want a clear next step into adjacent prompts in Bayesian Methods or the wider Statistician library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as The Bayesian framework:, Prior: P(theta) — your belief about the parameter before seeing the data, Likelihood: P(data | theta) — how probable is the data at each value of theta?. The final answer should stay clear, actionable, and easy to review inside a bayesian methods workflow for statistician work. 

## How to use this prompt 

1. ### Open your data context 
Load your dataset, notebook, or working environment so the AI can operate on the actual project context. 

2. ### Copy the prompt text 
Use the copy button above and paste the prompt into the AI assistant or prompt input area. 

3. ### Review the output critically 
Check whether the result matches your data, assumptions, and desired format before moving on. 

4. ### Chain into the next prompt 
Once you have the first result, continue deeper with related prompts in Bayesian Methods.
