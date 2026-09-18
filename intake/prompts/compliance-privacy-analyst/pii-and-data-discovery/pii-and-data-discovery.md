# PII and Data Discovery *AI Prompts *

3 Compliance & Privacy Analyst prompts in PII and Data Discovery. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → intermediate levels and 3 single prompts. 

## AI prompts in PII and Data Discovery 
3 prompts Intermediate Single prompt 01 
### Automated PII Detection Prompt 

Design a prompt and validation framework for using LLMs to detect PII in unstructured text at scale. Data type: {{data_type}} (customer emails, support tickets, free-text form f... 
Prompt text Design a prompt and validation framework for using LLMs to detect PII in unstructured text at scale.

Data type: {{data_type}} (customer emails, support tickets, free-text form fields, documents)
Volume: {{volume}}
Acceptable false negative rate: {{fnr}} (missed PII — lower is better for compliance)

1. The detection prompt (to be applied to each text sample):

 System instruction:
 'You are a privacy compliance assistant. Identify all personally identifiable information (PII) in the following text. Be conservative — when in doubt, flag it.'

 Task instruction:
 'Scan this text and identify every instance of PII. For each instance found:
 - Quote the exact text
 - Classify the PII type: name / email / phone / address / SSN / date-of-birth / financial / health / government-ID / IP-address / username / other
 - Confidence: High (clearly PII) / Medium (likely PII, context-dependent) / Low (possible PII, may be fictional or generic)

 If no PII is found, return: {"pii_found": false}

 Return ONLY a JSON object matching this schema:
 {
 "pii_found": true,
 "instances": [
 {"text": "...", "type": "...", "confidence": "High|Medium|Low", "start_char": N, "end_char": N}
 ]
 }'

2. Sensitivity settings by use case:
 - For compliance scanning (minimize false negatives): flag all Medium and Low confidence instances
 - For redaction workflows (minimize false positives): flag only High confidence instances
 - For audit sampling: flag High + Medium; review Low manually

3. Validation framework:
 - Create a golden test set of 200 labeled text samples (100 with PII, 100 without)
 - Measure: precision, recall, F1 at each confidence threshold
 - Acceptable recall for compliance: ≥ 95% (missing < 5% of true PII)
 - Measure false positive rate: flag non-PII flagged as PII (acceptable up to 15% for initial triage)

4. Known failure modes to test:
 - Fictional PII (novel character names, example data) — should not be flagged
 - Partial PII (first name only with no other context) — judgment call, document the policy
 - PII in non-English text — test language coverage
 - Obfuscated PII (john[at]email[dot]com) — should be flagged
 - PII in code or SQL queries embedded in text

5. Redaction approach (after detection):
 - Replace detected PII with: [REDACTED-{type}] (e.g. [REDACTED-EMAIL])
 - Log: original text hash, PII types found, redaction timestamp, operator ID
 - Never log the actual PII values in the audit log

Return: the detection prompt, JSON schema, validation framework, golden test set design, and redaction specification. Copy prompt Open prompt details Intermediate Single prompt 02 
### Data Flow Mapping 

Map the flow of personal data through this system or business process for regulatory compliance. Process / system: {{process_name}} Regulation: {{regulation}} (GDPR Article 30,... 
Prompt text Map the flow of personal data through this system or business process for regulatory compliance.

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

Return: processing activity table, legal basis mapping, data flow diagram, retention schedule, and RoPA entry. Copy prompt Open prompt details Beginner Single prompt 03 
### PII Inventory Builder 

Build a structured PII inventory for this system or dataset. System / dataset: {{system_name}} Data source description: {{source_description}} Applicable regulations: {{regulati... 
Prompt text Build a structured PII inventory for this system or dataset.

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

Return: PII inventory table, sensitive category flags, re-identification risk assessment, and gap list with recommended remediation. Copy prompt Open prompt details 
## Recommended PII and Data Discovery workflow 
1 
### Automated PII Detection Prompt 

Start with a focused prompt in PII and Data Discovery so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Data Flow Mapping 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### PII Inventory Builder 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
