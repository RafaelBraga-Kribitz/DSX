# Model Selection and Comparison *AI Prompt *

Compare candidate statistical models and select the most appropriate one. Outcome variable: {{outcome}} Candidate models: {{models}} (list of model specifications) Data: {{data_... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Compare candidate statistical models and select the most appropriate one.

Outcome variable: {{outcome}}
Candidate models: {{models}} (list of model specifications)
Data: {{data_description}}
Goal: {{goal}} (inference / prediction / both)

1. Information criteria:
 AIC = 2k - 2 ln(L)
 BIC = k ln(n) - 2 ln(L)
 where k = number of parameters, L = maximized likelihood, n = sample size

 - Lower AIC/BIC = better model
 - AIC minimizes prediction error; BIC penalizes complexity more (prefers parsimonious models)
 - Delta AIC: difference from the best model
 Delta < 2: substantial support for this model
 Delta 4-7: considerably less support
 Delta > 10: essentially no support
 - For purely predictive goals: use AIC or cross-validation
 - For inference with parsimony: use BIC

2. Likelihood ratio test (LRT) for nested models:
 LRT statistic = -2(ln L_restricted - ln L_full)
 Follows chi-square distribution with df = difference in number of parameters
 Reject the restricted model if p < 0.05
 Use LRT when: comparing a simpler model to a more complex one that contains it as a special case

3. Cross-validation:
 For predictive model selection, k-fold cross-validation gives the most honest estimate:
 - Split data into k folds (k=10 is standard)
 - Train on k-1 folds, test on held-out fold
 - Average test metric (RMSE for continuous, AUC for binary) across folds
 - Select model with best mean CV metric, accounting for standard error
 - One-standard-error rule: prefer the simpler model within 1 SE of the best

4. Goodness-of-fit tests:
 - For linear regression: overall F-test (are any predictors useful?)
 - For logistic regression: Hosmer-Lemeshow test (is the calibration good?)
 - For count models: overdispersion test (is Poisson appropriate, or do we need negative binomial?)

5. Parsimony principle:
 - Between models with similar fit: prefer the simpler one
 - A model that is too complex will overfit: good in-sample fit, poor out-of-sample prediction
 - Report confidence/credible intervals for all selected model parameters

Return: AIC/BIC comparison table, LRT results (if applicable), cross-validation scores, and model selection recommendation with rationale. 
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

The AI should return a structured result that covers the main requested outputs, such as Information criteria:, Lower AIC/BIC = better model, AIC minimizes prediction error; BIC penalizes complexity more (prefers parsimonious models). The final answer should stay clear, actionable, and easy to review inside a regression and modeling workflow for statistician work. 

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
