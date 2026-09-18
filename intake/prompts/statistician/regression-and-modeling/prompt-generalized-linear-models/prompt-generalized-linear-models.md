# Generalized Linear Models *AI Prompt *

Specify and interpret the appropriate Generalized Linear Model (GLM) for this outcome. Outcome variable: {{outcome}} and its distribution: {{distribution}} Predictors: {{predict... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Specify and interpret the appropriate Generalized Linear Model (GLM) for this outcome.

Outcome variable: {{outcome}} and its distribution: {{distribution}}
Predictors: {{predictors}}
Data structure: {{data_structure}} (cross-sectional, panel, clustered)

1. GLM family and link function selection:

 Gaussian family, identity link:
 - Outcome: continuous, approximately normal
 - Equivalent to OLS linear regression

 Binomial family, logit link (logistic regression):
 - Outcome: binary (0/1) or proportion
 - Coefficient interpretation: log-odds. exp(beta) = odds ratio
 - Alternative links: probit (normal CDF), complementary log-log (for rare events)

 Poisson family, log link:
 - Outcome: count data (non-negative integers)
 - Assumption: mean = variance (equidispersion)
 - exp(beta) = incidence rate ratio
 - Add offset term (log of exposure) for rate models: log(mu) = offset + X'beta

 Negative binomial family, log link:
 - Outcome: overdispersed count data (variance > mean)
 - Adds a dispersion parameter: variance = mu + mu^2/theta
 - Check: if Poisson residual deviance >> df, use negative binomial

 Gamma family, log or inverse link:
 - Outcome: positive continuous, right-skewed (cost, duration, concentration)
 - Log link preferred for interpretability

 Inverse Gaussian family, log link:
 - Outcome: positive continuous, strongly right-skewed

2. Model fitting and interpretation:
 - Fit the GLM using maximum likelihood
 - Coefficients are on the scale of the link function
 - Back-transform for interpretation: exponentiate log-link coefficients for multiplicative effects
 - Confidence intervals: profile likelihood CI preferred over Wald CI for small samples

3. Overdispersion check (for count models):
 - Residual deviance / df: should be close to 1.0 for Poisson
 - If >> 1: overdispersion → switch to negative binomial or quasi-Poisson
 - If << 1: underdispersion (rare) → investigate data generation process

4. Zero inflation:
 - If there are more zeros than the Poisson/NB distribution predicts: zero-inflated model
 - ZIP (Zero-inflated Poisson): mixture of a point mass at zero and a Poisson distribution
 - ZINB: Zero-inflated negative binomial
 - Test: Vuong test comparing Poisson to ZIP

5. Goodness of fit:
 - Pearson chi-square statistic / df
 - Deviance / df
 - Rootogram (for count data): visual comparison of observed vs fitted count distributions

Return: GLM family and link function selection with rationale, coefficient interpretation, overdispersion check, zero-inflation assessment, and goodness-of-fit evaluation. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin regression and modeling work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Regression and Modeling or the wider Statistician library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as GLM family and link function selection:, Outcome: continuous, approximately normal, Equivalent to OLS linear regression. The final answer should stay clear, actionable, and easy to review inside a regression and modeling workflow for statistician work. 

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

Once you have the first result, continue deeper with related prompts in Regression and Modeling.
