# Cross-Sectional Regression *AI Prompt *

Run and interpret a cross-sectional regression of asset returns on characteristics for factor research. Universe: {{universe}} (N assets) Dependent variable: {{horizon}}-day for... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Run and interpret a cross-sectional regression of asset returns on characteristics for factor research.

Universe: {{universe}} (N assets)
Dependent variable: {{horizon}}-day forward returns
Characteristics: {{characteristics}} (value, momentum, quality, size, etc.)
Period: {{period}}

1. Fama-MacBeth two-step procedure:
 This is the standard approach for cross-sectional factor research:

 Step 1 — Cross-sectional regressions (each period t):
 R_{i,t+h} = α_t + γ_{1,t} X_{1,i,t} + γ_{2,t} X_{2,i,t} + ... + ε_{i,t}
 Run this regression for each time period t → get a time series of γ_{k,t} for each characteristic k

 Step 2 — Time series inference:
 - Mean γ_k: average return premium for characteristic k
 - Std of γ_k: variation in premium over time
 - t-statistic: γ̄_k / (std_k / sqrt(T)) — adjust for autocorrelation with Newey-West
 - Reject H₀ (no premium) if |t| > 2.0; prefer t > 3.0 (Harvey et al. 2016) given multiple testing

2. Data preparation for cross-sectional regression:
 - Winsorize characteristics at 1st and 99th percentile: prevents extreme values from dominating
 - Rank-normalize characteristics: rank each characteristic within each cross-section, then scale to [-1, 1] or [0, 1]
 - Industry/sector neutralization: demean within each industry to remove sector bias
 - Standardize (z-score within each cross-section): ensures γ is interpretable as return per unit of normalized characteristic

3. Multi-characteristic regression:
 - Joint regression: controls for the correlation between characteristics
 - Standalone vs joint premium: a characteristic with a strong standalone premium may become insignificant after controlling for other characteristics (it was proxying for something else)
 - Check VIF: multicollinearity is common between related characteristics (value measures, for example)

4. Economic interpretation:
 - γ_k × 252 / h: annualized return premium for a 1-unit characteristic tilt
 - Economic significance: if γ_k is statistically significant but implies only 0.2% annualized premium, is it worth implementing?

5. Stability analysis:
 - Plot γ_{k,t} over time: is the premium stable or cyclical?
 - Pre-publication vs post-publication premium: has the premium decayed?
 - Bull vs bear market performance: does the premium hold in all market conditions?

Return: Fama-MacBeth regression table, Newey-West t-statistics, standalone vs joint premium comparison, premium stability plots. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin statistical and econometric methods work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Statistical and Econometric Methods or the wider Quantitative Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Fama-MacBeth two-step procedure:, Mean γ_k: average return premium for characteristic k, Std of γ_k: variation in premium over time. The final answer should stay clear, actionable, and easy to review inside a statistical and econometric methods workflow for quantitative analyst work. 

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

Once you have the first result, continue deeper with related prompts in Statistical and Econometric Methods.
