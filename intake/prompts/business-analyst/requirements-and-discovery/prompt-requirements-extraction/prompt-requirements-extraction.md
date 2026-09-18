# Requirements Extraction *AI Prompt *

This prompt helps business analysts turn messy project inputs into structured discovery outputs. It is designed for the early phase of an initiative when the team still needs clarity on needs, scope, stakeholders, constraints, and direction. Use it to move from conversations and assumptions to something documented, reviewable, and ready for decision-making or backlog creation. It is especially useful for turning raw notes into traceable requirements with priorities, sources, and open questions. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Extract and structure the business requirements from the following input: {{input}} (meeting notes, email thread, or stakeholder interview transcript).

1. Identify and separate:
 - Business requirements: what the business needs to achieve (outcomes)
 - Functional requirements: what the system or process must do
 - Non-functional requirements: performance, security, compliance constraints
 - Out of scope: what was explicitly excluded

2. For each requirement write:
 - Unique ID (BR-001, FR-001, etc.)
 - Clear one-sentence statement in the format: 'The system/process shall [action] so that [business outcome]'
 - Priority: Must Have / Should Have / Nice to Have (MoSCoW)
 - Source: who requested it
 - Open questions that need clarification before this requirement can be finalized

3. Flag any conflicting requirements between stakeholders

Return a structured requirements table and a list of open questions to resolve in the next session. 
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
