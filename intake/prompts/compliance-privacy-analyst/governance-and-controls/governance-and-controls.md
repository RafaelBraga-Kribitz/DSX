# Governance and Controls *AI Prompts *

3 Compliance & Privacy Analyst prompts in Governance and Controls. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 2 single prompts · 1 chain. 

## AI prompts in Governance and Controls 
3 prompts Beginner Single prompt 01 
### Data Retention Policy Writer 

Write a data retention policy for this organization that satisfies legal requirements and data minimization principles. Organization type: {{org_type}} Industries / jurisdiction... 
Prompt text Write a data retention policy for this organization that satisfies legal requirements and data minimization principles.

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

Return: retention schedule table (data type | legal basis | period | trigger | action | owner), policy clauses, legal hold procedure, and implementation checklist. Copy prompt Open prompt details Intermediate Single prompt 02 
### Privacy Notice Review 

Review this privacy notice / privacy policy for regulatory compliance and plain language quality. Privacy notice: {{privacy_notice_text}} Organization: {{organization}} Regulati... 
Prompt text Review this privacy notice / privacy policy for regulatory compliance and plain language quality.

Privacy notice: {{privacy_notice_text}}
Organization: {{organization}}
Regulation: {{regulation}} (GDPR, CCPA, PIPEDA, etc.)

A privacy notice must be provided to data subjects at the time of data collection (GDPR Art. 13/14). It must be concise, transparent, intelligible, and in plain language.

1. Required content audit (GDPR Art. 13/14 checklist):
 Check whether the notice includes each of the following. Mark: ✅ Present | ⚠️ Incomplete | ❌ Missing

 ❑ Controller identity and contact details
 ❑ DPO contact details (if applicable)
 ❑ Purposes of processing for each data category
 ❑ Legal basis for each processing purpose
 ❑ Legitimate interests assessment (if legitimate interests is the legal basis)
 ❑ Recipients or categories of recipients
 ❑ International transfer information and safeguards (if data transferred outside EEA)
 ❑ Retention periods (or criteria used to determine them)
 ❑ Data subject rights: access, rectification, erasure, restriction, portability, objection
 ❑ Right to withdraw consent (where consent is the legal basis)
 ❑ Right to lodge a complaint with the supervisory authority
 ❑ Whether provision of personal data is statutory or contractual, and consequences of not providing it
 ❑ Automated decision-making and profiling disclosure (if applicable)
 ❑ Source of data (Art. 14 only — where data not collected directly from the data subject)

 CCPA additional requirements:
 ❑ Categories of personal information collected
 ❑ Purposes for which categories are used
 ❑ Categories of third parties with whom data is shared or sold
 ❑ Link to 'Do Not Sell or Share My Personal Information'
 ❑ Consumer rights under CCPA
 ❑ Metrics for previous calendar year (for businesses above threshold)

2. Plain language assessment:
 - Reading level: compute Flesch-Kincaid grade level. Target: ≤ Grade 8 for consumer-facing notices.
 - Average sentence length: < 20 words per sentence
 - Passive voice: flag sentences using passive voice that obscure who does what to whose data
 - Vague language: flag phrases like 'we may share', 'certain partners', 'relevant purposes' — these are not specific enough
 - Jargon: flag legal or technical terms not explained in plain language

3. Layered notice assessment:
 - Is there a short-form summary (first layer) that gives key information at a glance?
 - Is the full detail available in the long-form notice (second layer)?
 - GDPR requires information to be provided 'in a concise, transparent, intelligible and easily accessible form'
 - A 10,000-word wall of text is not transparent, regardless of its content

4. Currency and accuracy check:
 - Does the notice reflect actual current practices? (Stale notices are a common violation)
 - Are all third-party recipients named? (Many notices are vague here)
 - Are retention periods specific? (Not just 'as long as necessary')
 - Is the DPO contact current?

5. Common violations to flag:
 - Consent bundled with accepting terms (not freely given)
 - 'We take your privacy seriously' with no substantive content
 - Legal basis listed as 'legitimate interests' without any description of what that interest is
 - No retention periods specified
 - Data subject rights described without instructions for how to exercise them

Return: content checklist with status per item, plain language assessment, specific missing elements, specific vague language identified, and priority remediation list. Copy prompt Open prompt details Advanced Chain 03 
### Privacy Program Maturity Assessment 

Step 1: Data inventory and mapping — assess the completeness of the organization's personal data inventory. Are all systems, all data flows, and all processors documented? Is th... 
Prompt text Step 1: Data inventory and mapping — assess the completeness of the organization's personal data inventory. Are all systems, all data flows, and all processors documented? Is the Record of Processing Activities (RoPA) current and comprehensive? Score: Incomplete (1) / Partial (2) / Documented (3) / Automated and maintained (4).

Step 2: Legal basis and consent — for each processing activity in the RoPA, is a valid legal basis documented? Has a Legitimate Interest Assessment been conducted where LI is claimed? Is consent management compliant (freely given, specific, informed, unambiguous, withdrawable, logged)? Score each on the 1–4 scale.

Step 3: Data subject rights — is there a documented DSAR intake process? Are response timelines met consistently? Is there a searchable data map enabling complete responses? Are all rights (access, erasure, portability, objection, restriction) operationalized? Score: No process (1) / Ad hoc (2) / Documented process (3) / Automated and tracked (4).

Step 4: Breach management — is there a documented breach detection and response process? Is the 72-hour notification timeline achievable? Is a breach log maintained? Has the team been trained and has a tabletop exercise been conducted in the last 12 months? Score on the 1–4 scale.

Step 5: Vendor management — is there a vendor inventory of all data processors? Is a compliant DPA in place with each processor? Are sub-processors tracked? Are international transfers documented with appropriate safeguards? Is there a vendor assessment process for new onboarding? Score on the 1–4 scale.

Step 6: Privacy by design — is privacy impact assessment (DPIA) embedded in the product and project development lifecycle? Is there a trigger list for when DPIAs are required? Is data minimization practiced in system design? Score on the 1–4 scale.

Step 7: Governance and accountability — is there a designated DPO (if required)? Is there a privacy steering committee or equivalent? Is privacy training mandatory and tracked? Is the privacy program subject to regular audit? Are board-level privacy risk reports produced? Score on the 1–4 scale.

Final output: maturity heatmap (category × score), top 3 highest-priority gaps, a 12-month roadmap with specific actions to advance each dimension by at least one level, and an overall maturity verdict: Initial (avg < 2) / Developing (2–2.9) / Defined (3–3.4) / Managed (3.5–3.9) / Optimized (4.0). Copy prompt Open prompt details 
## Recommended Governance and Controls workflow 
1 
### Data Retention Policy Writer 

Start with a focused prompt in Governance and Controls so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Privacy Notice Review 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Privacy Program Maturity Assessment 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
