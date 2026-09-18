# Lookalike Audience Analysis *AI Prompt *

Build a lookalike audience strategy based on best-customer characteristics. Seed audience: {{seed_audience}} (your best customers by LTV or conversion) Available platforms: {{pl... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a lookalike audience strategy based on best-customer characteristics.

Seed audience: {{seed_audience}} (your best customers by LTV or conversion)
Available platforms: {{platforms}} (Meta, Google, LinkedIn, programmatic DSP)
Campaign goal: {{goal}}

1. Seed audience definition and quality:
 - Define 'best customers': top 10% by LTV, or converted within 30 days, or completed {{action}}
 - Minimum seed size: 1,000 users for reliable lookalike modeling (500 minimum, 5,000+ recommended)
 - Seed quality check: are seed customers actually your most profitable? (Not just most active)

2. First-party data preparation:
 - Match rate optimization: use email, phone, MAIDS for highest match rates
 - Hashed PII: never pass unhashed emails to platforms
 - Audience freshness: use customers acquired in the last 6 months for best results
 - Exclude: existing customers from prospecting lookalike campaigns

3. Platform-specific lookalike construction:

 Meta Lookalike Audiences:
 - Similarity range: 1% (most similar) to 10% (broader reach, less similar)
 - Recommendation: 1-2% for highest intent, 3-5% for broader prospecting
 - Layer with interest targeting for higher precision

 Google Similar Audiences / Customer Match:
 - Smart Bidding automatically adjusts bids for similar audiences
 - Customer Match can be used for similar segments via automatically created lists

 LinkedIn Lookalikes:
 - Most valuable for B2B: match on company, industry, job title characteristics
 - Seed with MQL or customer list from CRM

4. Testing framework:
 - A/B test: lookalike 1% vs lookalike 3% vs interest targeting vs no audience filter
 - Measure: CPA and conversion rate per audience type
 - Duration: minimum 2 weeks, 50+ conversions per variant for statistical reliability

5. Performance benchmarks:
 - Lookalike audiences should outperform broad targeting by 20-40% on CPA
 - If lookalike is not outperforming: seed audience may not be differentiated enough

Return: seed audience definition, data preparation checklist, platform construction guide, testing framework, and performance benchmarks. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin audience segmentation work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Audience Segmentation or the wider Marketing Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Seed audience definition and quality:, Define 'best customers': top 10% by LTV, or converted within 30 days, or completed {{action}}, Minimum seed size: 1,000 users for reliable lookalike modeling (500 minimum, 5,000+ recommended). The final answer should stay clear, actionable, and easy to review inside a audience segmentation workflow for marketing analyst work. 

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

Once you have the first result, continue deeper with related prompts in Audience Segmentation.
