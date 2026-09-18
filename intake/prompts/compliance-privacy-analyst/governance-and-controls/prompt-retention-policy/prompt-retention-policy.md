# Data Retention Policy Writer *AI Prompt *

Write a data retention policy for this organization that satisfies legal requirements and data minimization principles. Organization type: {{org_type}} Industries / jurisdiction... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write a data retention policy for this organization that satisfies legal requirements and data minimization principles.

Organization type: {{org_type}}
Industries / jurisdictions: {{jurisdictions}}
Key data categories held: {{data_categories}}

The storage limitation principle (GDPR Art. 5(1)(e)) requires that personal data be kept 'no longer than is necessary for the purposes for which the personal data are processed.' A retention policy operationalizes this principle.

1. Retention schedule structure:
 For each data category, define:
 - Data type: what is it? (customer records, employee records, financial transactions, marketing data, CCTV footage, etc.)
 - Legal / regulatory basis for retention: what law or regulation requires or permits this retention period?
 - Business purpose basis: if no legal basis, what is the business justification?
 - Retention period: specific duration (not vague like 'as long as necessary')
 - Trigger event: when does the clock start? (contract end date, last interaction, account closure, employment termination, etc.)
 - Action at end of period: secure deletion, anonymization, or archival
 - Owner: which team is responsible for enforcing retention for this data type?

2. Common retention periods by category:

 Financial and tax records:
 - Invoices, receipts, financial statements: 7 years (US IRS, UK HMRC)
 - Payroll records: 3–7 years depending on jurisdiction
 - Tax returns: 7 years minimum (US)

 Employment records:
 - Active employees: duration of employment + 7 years
 - Recruitment records (unsuccessful applicants): 6 months–1 year (EEOC guidance)
 - Health and safety records: up to 40 years for some occupational exposure records

 Customer records:
 - Active customer data: duration of relationship + retention period for disputes
 - Inactive customers: last interaction date + 3 years (typical legitimate interest period)
 - Marketing consent records: 3 years from consent withdrawal (for dispute evidence)

 Regulated industries:
 - Healthcare (HIPAA): medical records 6 years from creation or last use
 - Financial services: trade records 5–7 years (MiFID II, SEC Rule 17a-4)
 - Legal: client files 7 years post-matter close (jurisdiction-dependent)

3. Retention policy clauses to include:
 - Scope: which data and which systems this policy covers
 - Legal hold: retention schedules are suspended when data is subject to litigation hold
 - Exceptions process: who may grant exceptions and under what conditions
 - Deletion verification: how is deletion confirmed and logged?
 - Third parties: retention requirements flow down to processors through DPAs
 - Review cycle: policy reviewed annually

4. Legal hold provision:
 - When litigation is anticipated or in progress: all destruction of relevant data must stop
 - Legal hold notice procedure: how is a hold issued? To whom? How is compliance confirmed?
 - Hold release: who authorizes release and what records are produced?

5. Implementation guidance:
 - Automated deletion: preferred over manual processes — specify which systems have automated deletion
 - Manual deletion: for systems without automation — specify the schedule and responsible party
 - Deletion certificate: for sensitive data, document what was deleted, when, and by whom

Return: retention schedule table (data type | legal basis | period | trigger | action | owner), policy clauses, legal hold procedure, and implementation checklist. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin governance and controls work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Governance and Controls or the wider Compliance & Privacy Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Retention schedule structure:, Data type: what is it? (customer records, employee records, financial transactions, marketing data, CCTV footage, etc.), Legal / regulatory basis for retention: what law or regulation requires or permits this retention period?. The final answer should stay clear, actionable, and easy to review inside a governance and controls workflow for compliance & privacy analyst work. 

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

Once you have the first result, continue deeper with related prompts in Governance and Controls.
