# Incrementality Testing Design *AI Prompt *

Design an incrementality test to measure the true causal impact of a marketing channel. Channel to test: {{channel}} (e.g. Facebook Ads, email retargeting, TV) Primary metric: {... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design an incrementality test to measure the true causal impact of a marketing channel.

Channel to test: {{channel}} (e.g. Facebook Ads, email retargeting, TV)
Primary metric: {{metric}} (conversions, revenue)
Business context: {{context}}

Incrementality testing answers: what revenue would we have generated WITHOUT this channel?
This is the only way to determine true incremental value beyond what would have happened anyway.

1. Test design options:

 Geo holdout test:
 - Split geography into test regions (channel active) and holdout regions (channel paused)
 - Match regions by: historical performance, demographics, market size
 - Duration: minimum 4 weeks (longer for lower-frequency purchase categories)
 - Measure: conversion rate in test regions vs holdout regions

 User holdout (ghost bidding):
 - Randomly assign users: treatment (see ads) vs control (ad slot left empty)
 - Platform-native holdout if available (Facebook Brand Lift, Google Conversion Lift)
 - Best for: digital channels with user-level targeting

 Time-based holdout:
 - Turn off the channel for a period and compare to matched prior period
 - Weakness: seasonal and macro factors can confound results
 - Requires: careful selection of the comparison period

2. Sample size and duration:
 - Required sample: power calculation based on baseline conversion rate and expected lift
 - Minimum detectable effect: if the channel drives < {{mde}}% lift, you need more data
 - Duration: long enough to capture a full purchase cycle

3. Measurement:
 - Lift = (Conversion Rate_test - Conversion Rate_holdout) / Conversion Rate_holdout
 - Incremental conversions = Lift x Holdout user volume
 - True CPA = Channel Spend / Incremental Conversions
 - Compare to attributed CPA: the gap shows how much attribution was overstating the channel

4. Common pitfalls:
 - Spillover: people in the holdout region still see the ads via other means
 - Holdout contamination: test and control groups interact (e.g. via social sharing)
 - Too short a test: brand campaigns need months to show full effect

Return: test design recommendation, sample size calculation, measurement plan, and common pitfall mitigations. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin attribution work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Attribution or the wider Marketing Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Test design options:, Split geography into test regions (channel active) and holdout regions (channel paused), Match regions by: historical performance, demographics, market size. The final answer should stay clear, actionable, and easy to review inside a attribution workflow for marketing analyst work. 

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

Once you have the first result, continue deeper with related prompts in Attribution.
