# Business Rules Extraction *AI Prompt *

This prompt helps business analysts turn messy project inputs into structured discovery outputs. It is designed for the early phase of an initiative when the team still needs clarity on needs, scope, stakeholders, constraints, and direction. Use it to move from conversations and assumptions to something documented, reviewable, and ready for decision-making or backlog creation. It surfaces the rules, policies, and constraints hidden in documents, datasets, or existing processes. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Extract and catalog all business rules from this dataset, document, or process description: {{source}}

A business rule is a specific, actionable constraint, condition, or policy that governs business behavior.

1. Identify and classify each rule by type:
 - Constraint rules: 'A customer must have an active account to place an order'
 - Derivation rules: 'Loyalty tier is Gold if annual spend > $5,000'
 - Inference rules: 'If a customer has 3 late payments, flag account for review'
 - Timing rules: 'Invoices must be paid within 30 days of issue'

2. For each rule write:
 - Rule ID (BR-001)
 - Rule statement in plain English
 - Rule type
 - Source (policy document, legal requirement, historical practice)
 - Current enforcement method (manual check, system validation, not enforced)
 - Business impact if rule is violated
 - Exceptions to the rule

3. Flag rules that are ambiguous, conflicting, or out of date
4. Identify rules that should be automated but are currently manual

Return: business rules catalog and a list of automation candidates. 
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
