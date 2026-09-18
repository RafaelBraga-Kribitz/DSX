# Data Literacy Translation *AI Prompt *

This prompt helps translate analysis into communication that stakeholders can understand and act on. It is useful when the quality of the message matters as much as the quality of the analysis, especially with senior leaders or non-technical teams. The focus is on clarity, relevance, objection handling, and moving the conversation toward a decision. It rewrites technical analysis into language that a non-technical business audience can understand and repeat. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Translate this technical analysis into plain business language for {{audience}} who has no data or statistical background.

Technical analysis: {{technical_content}}

1. Remove or replace every technical term:
 - Replace statistical terms with business language
 - Example: 'statistically significant at p < 0.05' → 'we are 95% confident this is a real change, not random noise'
 - Example: 'regression coefficient of 0.42' → 'for every $1 increase in marketing spend, revenue increases by 42 cents'

2. Replace abstract numbers with concrete comparisons:
 - Instead of '15% increase', say 'that's like adding the equivalent of our entire Q3 sales team's output'
 - Use the audience's own business context for analogies

3. Connect every finding to a decision:
 - For each insight, state what it means for a decision the audience controls

4. Summarize in 3 bullet points a non-technical executive could repeat to their peers accurately

5. Identify any nuance or caveat that was lost in the translation that the audience must still know

Return: translated version, 3-bullet summary, and a list of caveats that survived translation. 
```

## When to use this prompt 
Use case 01 
Use when analysis must be translated for a non-technical or skeptical audience. 
Use case 02 
Use before a presentation, leadership meeting, or difficult performance conversation. 
Use case 03 
Use when the same insight needs to be framed differently for different stakeholders. 
Use case 04 
Use when you need a message that leads to action rather than passive awareness. 

## What the AI should return 

The AI should return stakeholder-ready communication in plain language, tailored to the audience and purpose. It should lead with the key message, support it with a few specific facts, and end with a concrete action, ask, or discussion point. The response should sound natural enough to use directly in a slide, email, meeting, or Slack post. 

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

Once you have the first result, continue deeper with related prompts in Stakeholder Communication.
