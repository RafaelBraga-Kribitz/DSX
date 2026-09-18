# Regression and Modeling *AI Prompts *

3 Statistician prompts in Regression and Modeling. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 3 single prompts. 

## AI prompts in Regression and Modeling 
3 prompts Advanced Single prompt 01 
### Generalized Linear Models 

Specify and interpret the appropriate Generalized Linear Model (GLM) for this outcome. Outcome variable: {{outcome}} and its distribution: {{distribution}} Predictors: {{predict... 
Prompt text Specify and interpret the appropriate Generalized Linear Model (GLM) for this outcome.

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

Return: GLM family and link function selection with rationale, coefficient interpretation, overdispersion check, zero-inflation assessment, and goodness-of-fit evaluation. Copy prompt Open prompt details Intermediate Single prompt 02 
### Linear Regression Diagnostics 

Diagnose and validate a fitted linear regression model. Model: {{model_description}} (outcome, predictors, n) Fitted model output: {{model_output}} 1. The four core OLS assumpti... 
Prompt text Diagnose and validate a fitted linear regression model.

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

Return: assumption check results per criterion, influential observation list, multicollinearity report, and model fit summary. Copy prompt Open prompt details Intermediate Single prompt 03 
### Model Selection and Comparison 

Compare candidate statistical models and select the most appropriate one. Outcome variable: {{outcome}} Candidate models: {{models}} (list of model specifications) Data: {{data_... 
Prompt text Compare candidate statistical models and select the most appropriate one.

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

Return: AIC/BIC comparison table, LRT results (if applicable), cross-validation scores, and model selection recommendation with rationale. Copy prompt Open prompt details 
## Recommended Regression and Modeling workflow 
1 
### Generalized Linear Models 

Start with a focused prompt in Regression and Modeling so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Linear Regression Diagnostics 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Model Selection and Comparison 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
