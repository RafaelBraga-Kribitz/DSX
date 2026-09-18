# PII Inventory Builder *AI Prompt *

Build a structured PII inventory for this system or dataset. System / dataset: {{system_name}} Data source description: {{source_description}} Applicable regulations: {{regulati... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Build a structured PII inventory for this system or dataset.

System / dataset: {{system_name}}
Data source description: {{source_description}}
Applicable regulations: {{regulations}} (GDPR, CCPA, HIPAA, etc.)

A PII inventory is the foundation of any privacy program. You cannot protect data you do not know you have.

1. Identify all personal data elements:
 For each data element present in the system, classify it:

 DIRECT IDENTIFIERS (identify a person alone):
 - Full name, first name + last name
 - Government ID numbers (SSN, passport, driver's license, national ID)
 - Financial account numbers (bank account, credit card)
 - Medical record numbers, health plan numbers
 - Email address, phone number, home address
 - Biometric data (fingerprint, facial recognition, voice print)
 - Precise geolocation

 INDIRECT / QUASI-IDENTIFIERS (identify when combined):
 - Date of birth, age, age range
 - Gender, race, ethnicity
 - Job title, employer, department
 - Zip code, city, country
 - IP address, device ID, cookie ID, advertising ID
 - Username, user ID

 SENSITIVE SPECIAL CATEGORIES (require heightened protection under GDPR Art. 9 / similar):
 - Health and medical data
 - Genetic data
 - Sexual orientation or gender identity
 - Religious or philosophical beliefs
 - Political opinions
 - Trade union membership
 - Criminal convictions and offenses

 CHILDREN'S DATA (requires additional protections under COPPA, GDPR Art. 8):
 - Any data about individuals under 13 (COPPA) or under 16 (GDPR)

2. For each identified data element, record:
 - Field name in the system
 - PII category (direct identifier / quasi-identifier / sensitive / children's)
 - Applicable regulation(s)
 - Business purpose for collecting this data
 - Who can access it (roles)
 - Where it is stored (table, system, cloud region)
 - Is it encrypted at rest? In transit?
 - Retention period
 - Is it shared with third parties? Which ones?

3. Re-identification risk assessment:
 - Even if no single field is a direct identifier, can combinations re-identify individuals?
 - Apply the 'motivated intruder' test: could a determined person identify someone using only the data in this system?
 - Flag any combination of 3+ quasi-identifiers as a re-identification risk

4. Gaps and recommendations:
 - Which data elements lack a documented business purpose? (Violates data minimization principle)
 - Which data elements have no defined retention period?
 - Which sensitive categories lack explicit consent documentation?

Return: PII inventory table, sensitive category flags, re-identification risk assessment, and gap list with recommended remediation. 
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

The AI should return a structured result that covers the main requested outputs, such as Identify all personal data elements:, Full name, first name + last name, Government ID numbers (SSN, passport, driver's license, national ID). The final answer should stay clear, actionable, and easy to review inside a pii and data discovery workflow for compliance & privacy analyst work. 

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
