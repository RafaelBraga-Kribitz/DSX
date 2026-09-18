# Linear Regression Diagnostics *AI Prompt *

Diagnose and validate a fitted linear regression model. Model: {{model_description}} (outcome, predictors, n) Fitted model output: {{model_output}} 1. The four core OLS assumpti... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Diagnose and validate a fitted linear regression model.

Model: {{model_description}} (outcome, predictors, n)
Fitted model output: {{model_output}}

1. The four core OLS assumptions (LINE):

 L — Linearity:
 - Residuals vs fitted values plot: should show random scatter around zero
 - Pattern in residuals = non-linearity → add polynomial terms, interaction terms, or transform predictors
 - Partial regression plots (added variable plots): check linearity of each predictor separately

 I — Independence of errors:
 - By design: is this a cross-sectional dataset (no natural ordering)?
 - For time series or clustered data: Durbin-Watson test for serial autocorrelation (target: DW near 2)
 - If observations are clustered: use clustered standard errors or mixed effects model

 N — Normality of residuals:
 - Q-Q plot of standardized residuals: points should fall on the diagonal
 - Shapiro-Wilk test for normality (reliable for n < 2000)
 - Note: normality of residuals is the LEAST critical assumption for large samples (CLT)
 - Skewed residuals suggest: log-transform the outcome, or consider a GLM with appropriate family

 E — Equal variance (homoscedasticity):
 - Scale-location plot (sqrt(|standardized residuals|) vs fitted): should be flat
 - Breusch-Pagan test: p < 0.05 indicates heteroscedasticity
 - Fix: use heteroscedasticity-consistent (HC) standard errors (HC3 is robust in small samples)
 - Or: weighted least squares if variance structure is known

2. Influential observations:
 - Leverage (h_ii): measures how far an observation's predictor values are from the mean
 High leverage: h_ii > 2(k+1)/n
 - Cook's Distance: measures overall influence of each observation on all fitted values
 Influential if D_i > 4/n (rule of thumb)
 - DFFITS and DFBETAS: influence on fitted values and specific coefficients
 - Action: investigate (not automatically remove) flagged observations

3. Multicollinearity:
 - Variance Inflation Factor (VIF) per predictor
 - VIF > 5: concerning, VIF > 10: severe multicollinearity
 - Fix: remove redundant predictors, combine correlated predictors via PCA, or use ridge regression

4. Model fit assessment:
 - R-squared: proportion of variance explained (note: always increases with more predictors)
 - Adjusted R-squared: penalizes for adding unhelpful predictors
 - AIC/BIC: for model comparison (lower is better)
 - RMSE on a holdout set: most honest measure of predictive accuracy

Return: assumption check results per criterion, influential observation list, multicollinearity report, and model fit summary. 
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

The AI should return a structured result that covers the main requested outputs, such as The four core OLS assumptions (LINE):, Residuals vs fitted values plot: should show random scatter around zero, Pattern in residuals = non-linearity → add polynomial terms, interaction terms, or transform predictors. The final answer should stay clear, actionable, and easy to review inside a regression and modeling workflow for statistician work. 

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
