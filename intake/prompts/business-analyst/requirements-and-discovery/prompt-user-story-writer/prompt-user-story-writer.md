# User Story Writer *AI Prompt *

This prompt helps business analysts turn messy project inputs into structured discovery outputs. It is designed for the early phase of an initiative when the team still needs clarity on needs, scope, stakeholders, constraints, and direction. Use it to move from conversations and assumptions to something documented, reviewable, and ready for decision-making or backlog creation. It converts broad requirements into delivery-ready user stories with acceptance criteria, dependencies, and sizing. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Convert these business requirements into well-formed user stories with acceptance criteria.

Requirements input: {{requirements}}

For each user story:
1. Write in standard format: 'As a [user type], I want [action] so that [benefit]'
2. Add a clear, specific title (5 words max)
3. Write 3–5 acceptance criteria in Given-When-Then (GWT) format:
 - Given [context/precondition]
 - When [action is taken]
 - Then [expected outcome]
4. Assign a story point estimate using Fibonacci scale (1, 2, 3, 5, 8, 13) based on complexity
5. Flag any story that is too large to complete in one sprint (>8 points) and suggest how to split it
6. Identify dependencies between stories

Return: formatted user story cards, dependency map, and a prioritized backlog order based on business value and dependencies. 
```

## When to use this prompt 
Use case 01 
Use when you need to turn interviews, notes, or stakeholder inputs into structured analysis. 
Use case 02 
Use at the start of a project, discovery phase, or process improvement initiative. 
Use case 03 
Use when scope, stakeholder needs, or future-state direction is still unclear. 
Use case 04 
Use when you need an artifact that can be reviewed in a workshop or planning session. 

## What the AI should return 

The AI should return a structured analysis in business analyst language, with clear headings, tables, and a short list of assumptions or open questions. The response should separate facts from inferred items, highlight conflicts or ambiguities, and make the output easy to review with stakeholders. Where prioritization or categorization is requested, it should be explicit and consistent. 

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

Once you have the first result, continue deeper with related prompts in Requirements and Discovery.
