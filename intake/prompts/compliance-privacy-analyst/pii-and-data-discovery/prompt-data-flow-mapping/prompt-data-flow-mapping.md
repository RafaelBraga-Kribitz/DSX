# Data Flow Mapping *AI Prompt *

Map the flow of personal data through this system or business process for regulatory compliance. Process / system: {{process_name}} Regulation: {{regulation}} (GDPR Article 30,... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Map the flow of personal data through this system or business process for regulatory compliance.

Process / system: {{process_name}}
Regulation: {{regulation}} (GDPR Article 30, CCPA, HIPAA, etc.)

Data flow mapping (also called data mapping or processing inventory) is required by GDPR Article 30 and forms the basis of any DPIA. It answers: what personal data flows where, for what purpose, with what legal basis.

1. Identify all processing activities:
 For each distinct processing activity in this process:
 - Activity name: what happens to the data? (collection, storage, analysis, sharing, deletion)
 - Data subjects: whose data is processed? (customers, employees, website visitors, children)
 - Personal data categories: what types of personal data? (contact info, financial, health, behavioral)
 - Sensitive data: does this activity involve special category data (GDPR Art. 9) or children's data?

2. Legal basis mapping (GDPR Art. 6 — required for each processing activity):
 Identify and document which legal basis applies:
 - Consent (Art. 6(1)(a)): is freely given, specific, informed, unambiguous consent obtained? Is it documented?
 - Contract (Art. 6(1)(b)): is processing necessary for contract performance?
 - Legal obligation (Art. 6(1)(c)): is processing required by law? Which law?
 - Vital interests (Art. 6(1)(d)): is processing necessary to protect life?
 - Public task (Art. 6(1)(e)): is the controller a public authority?
 - Legitimate interests (Art. 6(1)(f)): has a legitimate interest assessment (LIA) been conducted and documented?

 Red flag: if the documented basis is 'legitimate interests' without a LIA, this is a compliance gap.

3. Data flow diagram (text-based):
 Map the journey of personal data:
 [Data Subject] → [Collection point] → [Primary system] → [Third parties] → [Deletion/archival]

 For each arrow (transfer):
 - What data is transferred?
 - Is the transfer to a third party? If yes: is there a Data Processing Agreement (DPA)?
 - Is the transfer outside the EEA (for GDPR)? If yes: what transfer mechanism applies? (SCCs, adequacy decision, BCRs)

4. Retention periods:
 - For each data category: how long is it retained?
 - Is the retention period documented and justified?
 - Is there an automated deletion process, or is it manual?
 - What happens to data after the retention period — deleted, anonymized, or archived?

5. Record of Processing Activities (RoPA) entry:
 Produce a structured RoPA entry for GDPR Article 30:
 - Controller name and contact
 - Processing activity name
 - Purpose of processing
 - Data subject categories
 - Personal data categories
 - Recipients / third parties
 - International transfers and safeguards
 - Retention periods
 - Security measures (high-level)

Return: processing activity table, legal basis mapping, data flow diagram, retention schedule, and RoPA entry. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin pii and data discovery work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in PII and Data Discovery or the wider Compliance & Privacy Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Identify all processing activities:, Activity name: what happens to the data? (collection, storage, analysis, sharing, deletion), Data subjects: whose data is processed? (customers, employees, website visitors, children). The final answer should stay clear, actionable, and easy to review inside a pii and data discovery workflow for compliance & privacy analyst work. 

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

Once you have the first result, continue deeper with related prompts in PII and Data Discovery.
