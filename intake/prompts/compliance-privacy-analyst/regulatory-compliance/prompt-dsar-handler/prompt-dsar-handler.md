# Data Subject Rights Request Handler *AI Prompt *

Design a workflow and response template for handling Data Subject Access Requests (DSARs) and other data subject rights requests. Regulation: {{regulation}} (GDPR, CCPA, PIPEDA,... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a workflow and response template for handling Data Subject Access Requests (DSARs) and other data subject rights requests.

Regulation: {{regulation}} (GDPR, CCPA, PIPEDA, etc.)
Organization type: {{org_type}}
Systems holding personal data: {{systems}}

Data subjects have enforceable rights over their personal data. Failure to respond correctly and within deadlines is a common basis for regulatory complaints and fines.

1. Rights covered and deadlines:

 GDPR rights:
 - Right of access (Art. 15): receive a copy of all personal data held, plus metadata
 Deadline: 1 month from receipt of request (extendable to 3 months for complex requests)
 - Right to rectification (Art. 16): correct inaccurate or incomplete data
 Deadline: 1 month
 - Right to erasure / right to be forgotten (Art. 17): delete personal data when certain conditions apply
 Deadline: 1 month
 - Right to restriction (Art. 18): restrict processing while accuracy is contested or objection is pending
 Deadline: 1 month
 - Right to data portability (Art. 20): receive data in machine-readable format (applies to consent/contract basis only)
 Deadline: 1 month
 - Right to object (Art. 21): object to processing based on legitimate interests or direct marketing
 Deadline: immediately for direct marketing; 1 month for other objections
 - Rights related to automated decision-making (Art. 22): not be subject to solely automated decisions with significant effects

 CCPA rights (California):
 - Right to know: what data is collected, used, disclosed, sold
 - Right to delete
 - Right to opt-out of sale of personal information
 - Right to non-discrimination for exercising rights
 Deadline: 45 days (extendable by 45 days with notice)

2. Request intake and verification:
 - Intake channel: dedicated email address, web form, or in-product request
 - Identity verification: must verify the requester is who they claim to be
 - For low-risk requests: email verification sufficient
 - For access requests returning sensitive data: stronger verification required (government ID)
 - Do NOT ask for more information than necessary to verify identity
 - Acknowledgment: send within 3 working days confirming receipt and expected response date
 - Clock starts: from receipt of the valid request (if identity verification is needed, clock starts when verification is complete)

3. Data search procedure:
 For an access request: search must be comprehensive
 - List all systems that may hold personal data for this individual
 - Search procedure per system (who runs it, how, how long it takes)
 - Format for compiling results
 - Review results before sending: remove data about third parties, apply legal professional privilege redactions if applicable

4. Response templates:

 Acknowledgment:
 'We have received your [request type] request dated [date]. We will respond by [deadline date]. If we need to verify your identity, we will contact you within [X] working days. Reference number: [REF].'

 Exemption response (when a right does not apply):
 'We have reviewed your request. We are unable to [action] because [specific exemption applies — e.g. the data is required to comply with a legal obligation / the data concerns third parties / processing is necessary for a legal claim]. You have the right to lodge a complaint with [supervisory authority].'

5. Refusal grounds (legitimate):
 - Request is manifestly unfounded or excessive → can charge a reasonable fee or refuse
 - Exemptions: legal obligation, vital interests, public interest, legal claims, freedom of expression, research
 - Must always: state the reason for refusal, inform the requester of their right to complain

6. Logging and audit:
 - Log every request: date received, type, identity verified (Y/N), date responded, outcome
 - Retain logs for at least 3 years
 - Never log the personal data provided in the response

Return: rights and deadline reference table, intake and verification workflow, system search procedure, response templates, and audit logging design. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin regulatory compliance work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Regulatory Compliance or the wider Compliance & Privacy Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Rights covered and deadlines:, Right of access (Art. 15): receive a copy of all personal data held, plus metadata, Right to rectification (Art. 16): correct inaccurate or incomplete data. The final answer should stay clear, actionable, and easy to review inside a regulatory compliance workflow for compliance & privacy analyst work. 

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

Once you have the first result, continue deeper with related prompts in Regulatory Compliance.
