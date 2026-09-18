# Data Breach Response Playbook *AI Prompt *

Build a data breach response playbook for this organization. Organization: {{organization}} Applicable regulations: {{regulations}} (GDPR, CCPA, HIPAA, state breach notification... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a data breach response playbook for this organization.

Organization: {{organization}}
Applicable regulations: {{regulations}} (GDPR, CCPA, HIPAA, state breach notification laws)
Data types held: {{data_types}}

Under GDPR Article 33, personal data breaches must be reported to the supervisory authority within 72 hours of becoming aware. Under Article 34, affected data subjects must be notified without undue delay when the breach is likely to result in a high risk to their rights and freedoms.

1. Breach classification:
 Define what constitutes a reportable breach:
 - Confidentiality breach: unauthorized disclosure of personal data
 - Integrity breach: unauthorized alteration of personal data
 - Availability breach: accidental or unauthorized loss or destruction of personal data

 NOT every breach requires notification — assess risk:
 - Is personal data involved? (If only non-personal data: not a personal data breach)
 - What is the risk to data subjects? (Low / Medium / High)
 - High risk triggers mandatory data subject notification

2. The 72-hour clock:
 - Clock starts: when the organization 'becomes aware' — i.e. when a responsible person has a reasonable degree of certainty that a breach has occurred
 - Suspicion is NOT awareness — but do not delay investigation to avoid starting the clock
 - If full information is not available within 72 hours: report what you know and supplement later
 - Document the exact time of awareness

3. Incident response phases:

 Phase 1 — Detect and contain (Hours 0–4):
 - Incident confirmed by IT/security team
 - Contain the breach: revoke compromised credentials, isolate affected systems, preserve evidence
 - Notify the Privacy/DPO team immediately
 - Do NOT delete potentially breached data — preserve for forensics
 - Assign an incident lead

 Phase 2 — Assess (Hours 4–24):
 - Determine: what data was affected? How many data subjects? What categories of data?
 - Determine: how did the breach occur? What is the root cause?
 - Assess risk to data subjects using ENISA risk methodology:
 - Nature of data (special category = higher risk)
 - Volume of records affected
 - Ease of identification of data subjects
 - Severity of consequences (financial loss, discrimination, physical harm, reputational damage)
 - Risk level: Low → No notification required. Medium → Regulator notification only. High → Regulator + data subject notification.

 Phase 3 — Notify (Hours 24–72 for regulator; as soon as possible for data subjects):
 Supervisory authority notification (GDPR Art. 33) must include:
 - Description of the breach (nature, categories, approximate number of data subjects and records)
 - Name and contact of the DPO
 - Likely consequences of the breach
 - Measures taken or proposed to address the breach and mitigate effects

 Data subject notification (GDPR Art. 34) must include:
 - Plain-language description of the breach
 - Name and contact of the DPO
 - Likely consequences for the data subject
 - Steps taken to address the breach
 - Steps the data subject should take to protect themselves

4. Notification templates:

 Regulator notification summary:
 'On [date] at [time], [Organization] became aware of a [type] breach affecting approximately [N] data subjects. The breach involved [data categories]. The breach occurred due to [brief cause]. We have taken the following immediate steps: [actions]. We estimate the impact as [risk level] because [reasons]. We will provide further updates as our investigation progresses.'

 Data subject notification:
 'We are writing to inform you of an incident involving your personal data. On [date], [description of what happened in plain language]. The data involved included [specific data types]. We have taken the following steps to address the incident: [actions]. To protect yourself, we recommend: [specific steps]. If you have questions, contact our Data Protection Officer at [contact].'

5. Post-breach requirements:
 - Internal breach log: maintain a record of ALL breaches, including those below notification threshold (GDPR Art. 33(5))
 - Root cause analysis: within 30 days
 - Regulatory follow-up: respond to any supervisory authority inquiries within stated deadlines
 - Remediation tracking: document all corrective actions and their completion dates

Return: breach classification matrix, 72-hour timeline with actions, risk assessment framework, notification templates, and post-breach logging requirements. 
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

The AI should return a structured result that covers the main requested outputs, such as Breach classification:, Confidentiality breach: unauthorized disclosure of personal data, Integrity breach: unauthorized alteration of personal data. The final answer should stay clear, actionable, and easy to review inside a regulatory compliance workflow for compliance & privacy analyst work. 

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
