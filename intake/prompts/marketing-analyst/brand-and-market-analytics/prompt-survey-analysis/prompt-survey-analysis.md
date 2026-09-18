# Survey Analysis for Marketing Insights *AI Prompt *

Analyze this marketing survey and extract actionable insights. Survey data: {{survey_data}} Survey type: {{survey_type}} (NPS, CSAT, brand awareness, customer effort, market res... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Analyze this marketing survey and extract actionable insights.

Survey data: {{survey_data}}
Survey type: {{survey_type}} (NPS, CSAT, brand awareness, customer effort, market research)
Respondents: {{n_respondents}}

1. Response quality check:
 - Response rate and completion rate
 - Speeders: respondents who completed the survey in < 30% of median time (unreliable data)
 - Straightliners: respondents who gave the same answer to every scale question
 - Recommend excluding speeders and straightliners from analysis

2. Quantitative analysis:
 - For each closed-ended question: frequency distribution (count and % per response option)
 - For scale questions (1-10 NPS, 1-5 satisfaction): mean, median, standard deviation
 - Cross-tabulation: how do responses differ by key demographic or segment?

3. NPS analysis (if applicable):
 - Promoters (9-10), Passives (7-8), Detractors (0-6): count and %
 - NPS = % Promoters - % Detractors
 - NPS by segment: which customer group has the highest / lowest NPS?
 - NPS trend vs prior survey wave

4. Open-text analysis:
 - Theme extraction: top 10 themes from open-ended responses
 - Sentiment per theme: positive, neutral, negative
 - Volume and sentiment for: Promoters vs Detractors vs Passives
 - Most actionable verbatims: select 5 representative quotes per theme

5. Correlation with behavior:
 - Match survey respondents to CRM/behavioral data
 - Do high-NPS customers actually have higher retention rates?
 - Do customers who cite price as a concern have higher churn rates?

6. Marketing implications:
 - Promoter themes to amplify in marketing messaging
 - Detractor themes that are reputation risks to address
 - Awareness and perception gaps revealed by the survey

Return: response quality check, quantitative summary, NPS calculation, theme analysis, behavioral correlation, and marketing implications. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin brand and market analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Brand and Market Analytics or the wider Marketing Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Response quality check:, Response rate and completion rate, Speeders: respondents who completed the survey in < 30% of median time (unreliable data). The final answer should stay clear, actionable, and easy to review inside a brand and market analytics workflow for marketing analyst work. 

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

Once you have the first result, continue deeper with related prompts in Brand and Market Analytics.
