# Forecasting *AI Prompts *

4 Financial Analyst prompts in Forecasting. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 3 single prompts · 1 chain. 

## AI prompts in Forecasting 
4 prompts Advanced Chain 01 
### Full Financial Planning Chain 

Step 1: Business driver identification - identify the 5-8 key drivers that determine financial outcomes for this business. For each driver: current value, historical trend, and... 
Prompt text Step 1: Business driver identification - identify the 5-8 key drivers that determine financial outcomes for this business. For each driver: current value, historical trend, and forecast assumption with rationale.
Step 2: Revenue model - build a bottom-up revenue model from the key drivers. Disaggregate revenue into its components (new business, existing customer growth, churn). Build three scenarios: base, bull, and bear.
Step 3: Cost model - forecast each major cost category as either a fixed cost, a variable cost tied to a revenue driver, or a headcount-driven cost. Identify operating leverage: at what revenue level does EBITDA turn positive or reach the target margin?
Step 4: Cash flow model - build the FCF model from EBITDA to free cash flow. Include working capital movements, capex, interest, and taxes. Compute cash runway under each scenario.
Step 5: Balance sheet build - project the balance sheet for each period. Verify it balances. Identify any periods where the company needs additional financing.
Step 6: Sensitivity and scenario analysis - build a tornado chart of the top inputs by impact. Create a 5x5 sensitivity table for the two most impactful inputs. Present the three scenarios with narrative.
Step 7: Management presentation - produce a one-page financial summary: revenue, EBITDA, and FCF for each period with actuals and forecast. Include key assumptions, risks, and the single most important financial question the team needs to answer in the next 90 days. Copy prompt Open prompt details Intermediate Single prompt 02 
### Rolling Forecast Design 

Design and build a rolling forecast process to replace or supplement the annual budget. Company context: {{company_context}} Forecast horizon: {{horizon}} quarters ahead (always... 
Prompt text Design and build a rolling forecast process to replace or supplement the annual budget.

Company context: {{company_context}}
Forecast horizon: {{horizon}} quarters ahead (always maintained)
Update frequency: {{frequency}} (monthly or quarterly)

1. Rolling forecast architecture:
 - Horizon: always maintain {{horizon}} quarters forward regardless of fiscal year
 - Lock periods: actuals replace forecast as months close
 - Driver-based: forecast built from business drivers, not top-down targets
 Revenue = {{driver_1}} x {{driver_2}} (not 'last year + 10%')

2. Key drivers to forecast:
 Identify the 5-8 leading indicators that drive financial results:
 - Revenue drivers: new customer count, pipeline conversion rate, average deal size, renewal rate
 - Cost drivers: headcount plan, average cost per hire, usage-based costs, inflation
 - Working capital drivers: DSO, DPO, inventory turns
 For each driver: who owns the forecast input? What is the data source?

3. Forecast submission workflow:
 - Week 1: close actuals and update models
 - Week 2: business unit managers submit driver updates
 - Week 3: FP&A consolidates and runs scenarios
 - Week 4: review with senior leadership, finalize

4. Rolling forecast vs budget comparison:
 Rather than budget vs actual, track:
 - Forecast vs actual (how accurate was the rolling forecast?)
 - Forecast revision history: is the forecast converging or diverging as we approach the period?
 - Bias analysis: is the team consistently optimistic or pessimistic?

5. Accuracy tracking:
 - MAPE (Mean Absolute Percentage Error) per forecast vintage and per line item
 - Target: < 5% MAPE for 1-quarter-ahead forecast
 - Which business units have the least accurate forecasts? (Requires coaching or process improvement)

Return: rolling forecast architecture, driver identification worksheet, submission workflow calendar, accuracy tracking framework, and comparison to annual budget approach. Copy prompt Open prompt details Intermediate Single prompt 03 
### Scenario Planning Framework 

Build a scenario planning framework for this business. Company: {{company}} Key uncertainties: {{key_uncertainties}} Planning horizon: {{horizon}} 1. Identify the key uncertaint... 
Prompt text Build a scenario planning framework for this business.

Company: {{company}}
Key uncertainties: {{key_uncertainties}}
Planning horizon: {{horizon}}

1. Identify the key uncertainties:
 From the provided list, select 2 dimensions with:
 - High impact on business outcomes
 - High uncertainty (we do not know which way they will go)
 - Independence from each other (orthogonal axes)

 Example axes: (Market growth: fast vs slow) x (Competitive intensity: high vs low)

2. Build four scenarios on a 2x2 matrix:
 Each quadrant = a different future world
 - Scenario 1 (best case): favorable on both axes
 - Scenario 2 (growth challenge): favorable market, unfavorable competitive position
 - Scenario 3 (volume challenge): unfavorable market, favorable competitive position
 - Scenario 4 (stress case): unfavorable on both axes

3. Financial model per scenario:
 For each scenario:
 - Revenue assumption (growth rate and trajectory)
 - Margin assumption (impact on gross and EBITDA margin)
 - Cash flow and liquidity position at end of horizon
 - Key financial metrics: revenue, EBITDA, FCF, net debt/EBITDA

4. Trigger indicators:
 For each scenario: what early data would signal we are moving into that scenario?
 - Revenue indicators: order intake, pipeline coverage, churn rate
 - Market indicators: competitor pricing, industry PMI, macro data
 - Operational indicators: hiring plan, supply chain lead times

5. Strategic responses:
 For each scenario: what actions would management take?
 - Scenario 1: accelerate investment, hire aggressively
 - Scenario 4: cost containment, preserve cash, renegotiate debt
 Pre-committing to responses removes decision delay when a scenario materializes.

Return: 2x2 scenario matrix, financial model per scenario, trigger indicator dashboard, and pre-committed strategic responses. Copy prompt Open prompt details Advanced Single prompt 04 
### Time Series Revenue Forecasting 

Build a statistical time series forecast for this revenue or financial metric. Metric: {{metric}} Historical data: {{data}} (at least 24 periods) Forecast horizon: {{horizon}} p... 
Prompt text Build a statistical time series forecast for this revenue or financial metric.

Metric: {{metric}}
Historical data: {{data}} (at least 24 periods)
Forecast horizon: {{horizon}} periods
Seasonality: {{seasonality}} (yes/no, and period: weekly/monthly/quarterly)

1. Exploratory analysis:
 - Plot the series: trend, seasonality, and irregular components visible?
 - Decompose using STL or classical decomposition: trend + seasonal + residual
 - Autocorrelation function (ACF) and Partial ACF (PACF): identify autoregressive and moving average structure
 - ADF test: is the series stationary? If not, difference and retest.

2. Model candidates:

 Holt-Winters (ETS):
 - Triple exponential smoothing: handles trend and seasonality
 - Parameters: alpha (level), beta (trend), gamma (seasonality)
 - Best for: smooth trends with regular seasonality, limited data (< 5 years)

 SARIMA:
 - Seasonal ARIMA (p,d,q)(P,D,Q)[m]
 - Select parameters using auto.arima (AIC/BIC minimization)
 - Best for: data with complex autocorrelation structure

 Prophet (Facebook/Meta):
 - Handles multiple seasonalities, holiday effects, and trend changepoints
 - Best for: monthly or daily data with irregular events and holidays

3. Model evaluation:
 - Split data: train on first 80%, test on last 20%
 - Metrics: MAPE, MAE, RMSE on the test set
 - Select the model with lowest MAPE on holdout

4. Forecast output:
 - Point forecast for each future period
 - 80% and 95% prediction intervals
 - Is the interval width reasonable given the metric's historical variance?

5. Forecast decomposition:
 - How much of the forecast is trend vs seasonal vs baseline?
 - What is the year-over-year growth implied by the forecast?

Return: model comparison table, selected model diagnostics, forecast with prediction intervals, and decomposition of forecast components. Copy prompt Open prompt details 
## Recommended Forecasting workflow 
1 
### Full Financial Planning Chain 

Start with a focused prompt in Forecasting so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Rolling Forecast Design 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Scenario Planning Framework 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Time Series Revenue Forecasting 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
