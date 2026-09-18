# Bayesian A/B Analysis *AI Prompt *

This prompt analyzes experiment results through a Bayesian lens, focusing on posterior uncertainty and decision-making under risk. It is useful when teams prefer probabilities of winning and expected loss over binary p-value decisions. It also lets you compare Bayesian and frequentist conclusions directly. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze this A/B test using a Bayesian framework instead of frequentist hypothesis testing.

1. Model the conversion rate for control and treatment as Beta distributions:
 - Prior: Beta(1, 1) — uninformative
 - Posterior: Beta(1 + conversions, 1 + non-conversions) for each variant
2. Plot the posterior distributions for control and treatment on the same chart
3. Compute:
 - Probability that treatment beats control: P(θ_treatment > θ_control) using Monte Carlo sampling (100k samples)
 - Expected lift: mean of (θ_treatment - θ_control) / θ_control
 - 95% credible interval for the lift
 - Expected loss from choosing the wrong variant
4. Apply a decision rule: ship treatment if P(treatment > control) > 0.95 AND expected lift > MDE of {{mde}}
5. Compare the Bayesian conclusion to a frequentist t-test conclusion — do they agree?

Return: posterior plots, probability table, decision recommendation, and a plain-English interpretation. 
```

## When to use this prompt 
Use case 01 
You want a Bayesian interpretation of an A/B test instead of only a p-value. 
Use case 02 
Decision-makers prefer probabilities, credible intervals, and expected loss. 
Use case 03 
You need a ship rule based on posterior evidence and minimum lift. 
Use case 04 
You want to compare Bayesian and frequentist conclusions side by side. 

## What the AI should return 

Posterior distribution plots, probability and lift summary table, expected-loss analysis, Bayesian decision recommendation, and a plain-English explanation of what the posterior says about the treatment. 

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
