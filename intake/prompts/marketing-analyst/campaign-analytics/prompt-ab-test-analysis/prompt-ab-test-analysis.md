# A/B Test Analysis for Campaigns *AI Prompt *

Analyze this marketing A/B test and produce a decision-ready report. Test description: {{test_description}} Variants: Control: {{control}} | Treatment: {{treatment}} Primary met... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze this marketing A/B test and produce a decision-ready report.

Test description: {{test_description}}
Variants: Control: {{control}} | Treatment: {{treatment}}
Primary metric: {{primary_metric}}
Test data: {{results_data}}

1. Statistical analysis:
 - Control and treatment values for the primary metric
 - Absolute and relative difference
 - Two-proportion z-test (for conversion rates) or t-test (for continuous metrics)
 - p-value and 95% confidence interval
 - Is the result statistically significant at alpha = 0.05?
 - Statistical power: given the observed sample size and effect, what was the test's power?

2. Practical significance:
 - Effect size: Cohen's h (for proportions) or Cohen's d (for means)
 - Business impact: if this effect persists at scale, what is the annual revenue or cost impact?
 - Minimum detectable effect vs observed effect: did we detect what we expected to detect?

3. Secondary metric analysis:
 - Repeat for all secondary metrics
 - Did any guardrail metrics degrade significantly?

4. Segment analysis:
 - Break results by: device, geography, new vs returning, customer tier
 - Is the effect consistent across segments or driven by one?
 - Heterogeneous treatment effects: does the winner differ by segment?

5. Decision:
 - Implement / Do not implement / Run follow-up test
 - If implementing: rollout plan
 - If running follow-up: what specific question does the next test answer?

6. Learnings for future campaigns:
 - What does this test teach us about our audience or message?
 - Should this insight change any other running campaigns?

Return: statistical analysis, effect size calculation, segment breakdown, decision, and learnings. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin campaign analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Campaign Analytics or the wider Marketing Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Statistical analysis:, Control and treatment values for the primary metric, Absolute and relative difference. The final answer should stay clear, actionable, and easy to review inside a campaign analytics workflow for marketing analyst work. 

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

Once you have the first result, continue deeper with related prompts in Campaign Analytics.
