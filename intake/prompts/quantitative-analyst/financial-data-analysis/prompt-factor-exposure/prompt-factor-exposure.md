# Factor Exposure Analysis *AI Prompt *

Analyze the factor exposures of this portfolio or asset using standard risk factor models. Portfolio / asset: {{portfolio}} Factor model: {{factor_model}} (Fama-French 3, Fama-F... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze the factor exposures of this portfolio or asset using standard risk factor models.

Portfolio / asset: {{portfolio}}
Factor model: {{factor_model}} (Fama-French 3, Fama-French 5, Carhart 4, Barra, or custom factors)
Time period: {{period}}

1. Factor model regression:
 Run OLS regression of excess returns on factor returns:
 R_i - R_f = α + β₁F₁ + β₂F₂ + ... + βₙFₙ + ε

 For Fama-French 3-factor:
 R_i - R_f = α + β_MKT(R_M - R_f) + β_SMB(SMB) + β_HML(HML) + ε

 Report for each factor:
 - Beta (exposure): with 95% confidence interval
 - t-statistic and p-value
 - Economic significance: what does a 1-unit factor shock imply for portfolio return?

2. Alpha (Jensen's alpha):
 - Report α with standard error and t-statistic
 - Annualized alpha = daily_alpha × 252
 - Is alpha statistically significant (t > 2.0)? Is it economically meaningful?
 - Caveat: alpha depends heavily on which factors are included in the model

3. Model fit:
 - R² and Adjusted R²: what % of return variation is explained by the factors?
 - Information ratio: α / tracking_error (annualized)
 - Residual autocorrelation: Durbin-Watson test on residuals

4. Rolling factor exposures:
 - 252-day rolling betas for each factor
 - Plot over time: are exposures stable or do they drift significantly?
 - Significant beta drift may indicate strategy drift, market regime change, or reconstitution

5. Factor contribution to return:
 - Decompose total return into: factor contribution + alpha + unexplained
 - Factor contribution_i = β_i × Factor_return_i
 - Which factors contributed most positively and negatively over the period?

6. Residual analysis:
 - Is the idiosyncratic risk (residual std) large relative to systematic risk?
 - High idiosyncratic risk suggests security-specific risks not captured by the factor model

Return: factor exposure table with CIs, alpha analysis, R², rolling beta plots, return decomposition, and residual analysis. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin financial data analysis work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Financial Data Analysis or the wider Quantitative Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Factor model regression:, Beta (exposure): with 95% confidence interval, t-statistic and p-value. The final answer should stay clear, actionable, and easy to review inside a financial data analysis workflow for quantitative analyst work. 

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

Once you have the first result, continue deeper with related prompts in Financial Data Analysis.
