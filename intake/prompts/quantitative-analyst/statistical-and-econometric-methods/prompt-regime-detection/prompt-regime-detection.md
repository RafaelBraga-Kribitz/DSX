# Regime Detection and Switching *AI Prompt *

Detect and model market regime switches in this financial time series. Time series: {{time_series}} Regime definition goal: {{goal}} (vol regimes, trend/mean-reversion, risk-on/... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Detect and model market regime switches in this financial time series.

Time series: {{time_series}}
Regime definition goal: {{goal}} (vol regimes, trend/mean-reversion, risk-on/risk-off, etc.)

1. Hidden Markov Model (HMM) regime detection:

 Specification for 2-state HMM:
 - State S_t ∈ {1, 2} (hidden, not directly observable)
 - Emission distribution: R_t | S_t = k ~ N(μ_k, σ²_k)
 - Transition matrix: P = [[p_{11}, p_{12}], [p_{21}, p_{22}]]
 p_{11} = P(stay in state 1 | currently in state 1)

 Estimation via EM algorithm (Baum-Welch):
 - Report: μ_1, σ_1, μ_2, σ_2, transition matrix P
 - Viterbi algorithm: most likely state sequence
 - Smoothed probabilities: P(S_t = k | all data) — softer than Viterbi

 Model selection:
 - 2 vs 3 states: compare BIC or AIC
 - 2-state typically: bull (high μ, low σ) and bear (low/negative μ, high σ)
 - 3-state may add: transition (moderate μ, rising σ)

2. Markov-Switching Regression:
 R_t = μ_{S_t} + φ_{S_t} R_{t-1} + ε_{S_t}
 - Different AR(1) coefficient in each regime
 - Captures mean-reversion in some regimes and momentum in others
 - Hamilton (1989) filter for real-time regime probability

3. Threshold and SETAR models:
 SETAR (Self-Exciting Threshold AR):
 - Regime is determined by whether a variable exceeds a threshold
 - R_t = α_1 + φ_1 R_{t-1} + ε_t if R_{t-d} ≤ threshold (regime 1)
 - R_t = α_2 + φ_2 R_{t-1} + ε_t if R_{t-d} > threshold (regime 2)
 - Self-exciting: the lagged return itself determines the regime
 - Suptest (Andrews) for the threshold location

4. Practical regime classification:
 Simple rule-based approach for transparency:
 - Regime = function of: trailing volatility, VIX level, credit spreads, or trend indicator
 - Pros: interpretable, auditable, does not require re-estimation
 - Cons: less statistically rigorous than HMM

5. Using regimes for portfolio management:
 - Regime-conditional strategy performance: does the alpha strategy perform differently across regimes?
 - Regime-conditional asset allocation: what is the historically optimal allocation in each regime?
 - Real-time regime probabilities: current P(S_t = bear) — use as a risk aversion dial
 - Transition probability: P(bear next month | bull this month) — forward-looking risk indicator

Return: HMM parameter estimates, smoothed regime probabilities, regime-conditional statistics, regime-conditional strategy performance, and current regime assessment. 
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

The AI should return a structured result that covers the main requested outputs, such as Hidden Markov Model (HMM) regime detection:, State S_t ∈ {1, 2} (hidden, not directly observable), Emission distribution: R_t | S_t = k ~ N(μ_k, σ²_k). The final answer should stay clear, actionable, and easy to review inside a statistical and econometric methods workflow for quantitative analyst work. 

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
