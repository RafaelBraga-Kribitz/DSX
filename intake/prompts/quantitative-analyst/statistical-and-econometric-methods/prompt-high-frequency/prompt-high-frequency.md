# High-Frequency Data Analysis *AI Prompt *

Analyze this high-frequency (intraday) financial data and estimate microstructure-aware statistics. Data: {{hf_data}} (tick or bar data with timestamps, prices, volumes) Frequen... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze this high-frequency (intraday) financial data and estimate microstructure-aware statistics.

Data: {{hf_data}} (tick or bar data with timestamps, prices, volumes)
Frequency: {{frequency}} (tick, 1-second, 1-minute)

1. Data cleaning for HF data:
 - Remove pre-market and post-market trades if analyzing regular session
 - Remove trades outside the bid-ask spread (erroneous prints)
 - Remove trades flagged with conditions (correction, cancel, out-of-sequence)
 - Handle auction prices: opening and closing auctions have different microstructure
 - Timestamps: ensure microsecond timestamps are in the same timezone

2. Realized volatility estimation:
 - Realized variance: RV_t = Σ r²_{t,i} (sum of squared high-frequency returns)
 - Optimal sampling frequency: avoid microstructure noise (bid-ask bounce) at very high frequency
 - Signature plot: plot RV as a function of sampling frequency → select the frequency where RV stabilizes
 - Bias-Variance tradeoff: higher frequency → more observations but more noise
 - Two-Scale Realized Variance (TSRV): subsampling estimator robust to microstructure noise
 - Realized kernel estimator (Barndorff-Nielsen): state-of-the-art for noisy tick data

3. Bid-ask spread estimation:
 If only trade prices are available (no quote data):
 - Roll's implied spread: 2 × sqrt(-cov(ΔP_t, ΔP_{t-1}))
 Under the model: trades alternate between bid and ask, creating negative autocovariance
 - Corwin-Schultz estimator: uses daily high-low prices

4. Market impact and order flow:
 - Order imbalance: (buy volume - sell volume) / total volume
 - Order flow toxicity (VPIN): volume-synchronized probability of informed trading
 - Amihud illiquidity ratio at intraday frequency: |return| / dollar_volume_per_bar

5. Intraday seasonality:
 - Plot average volume by time of day: U-shaped pattern typical for equities (high at open and close)
 - Plot average volatility by time of day: similar U-shape
 - Normalize statistics for seasonality before strategy analysis

6. Jump detection:
 - Barndorff-Nielsen & Shephard (BNS) test: separates continuous volatility from jumps
 - Bipower variation: BV_t = (π/2) Σ |r_{t,i}| × |r_{t,i+1}| (robust to jumps)
 - Jump statistic: (RV - BV) / RV → fraction of total variance due to jumps
 - Detect individual jumps: flag returns exceeding 3σ_BV (jump threshold)

Return: data quality report, realized volatility estimates with signature plot, bid-ask spread estimates, intraday seasonality plots, and jump detection results. 
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

The AI should return a structured result that covers the main requested outputs, such as Data cleaning for HF data:, Remove pre-market and post-market trades if analyzing regular session, Remove trades outside the bid-ask spread (erroneous prints). The final answer should stay clear, actionable, and easy to review inside a statistical and econometric methods workflow for quantitative analyst work. 

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
