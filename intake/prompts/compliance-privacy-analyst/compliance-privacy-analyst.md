# Compliance & Privacy Analyst *AI Prompts *

Compliance & Privacy Analyst AI prompt library with 12 prompts in 4 categories. Copy templates for real workflows in analysis, modeling, and reporting. Browse 4 categories and copy prompts you can use as-is or adapt to your stack. 

## Browse Compliance & Privacy Analyst prompt categories 
4 categories 
### Governance and Controls 

AI prompts for governance and controls, including policy mapping, control evaluation, accountability design, and audit-ready operating practices. 
3 prompts Data Retention Policy Writer Privacy Notice Review → 
### PII and Data Discovery 

AI prompts for PII and data discovery, including sensitive-field detection, risk labeling, and privacy-aware data inventory workflows. 
3 prompts Automated PII Detection Prompt Data Flow Mapping → 
### Privacy Impact and Risk 

AI prompts for privacy impact and risk analysis, including risk scoring, mitigation planning, and compliance-aligned review workflows. 
3 prompts Anonymization and Pseudonymization Assessment DPIA Template and Guidance → 
### Regulatory Compliance 

AI prompts for regulatory compliance workflows, including requirement interpretation, control mapping, evidence preparation, and readiness assessments. 
3 prompts Consent Management Audit Data Breach Response Playbook → 
## Advanced search and filtering 

Browse all prompts in this role with category, skill-level, type, and text filtering. 
Categories All categories 12 Governance and Controls 3 PII and Data Discovery 3 Privacy Impact and Risk 3 Regulatory Compliance 3 Skill level All levels Beginner Intermediate Advanced Prompt type All types Prompt Chain Template Showing **12 **of 12 prompts 
## Governance and Controls 
3 prompt s Governance and Controls Beginner Prompt 01 
### Data Retention Policy Writer 
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

Return: retention schedule table (data type | legal basis | period | trigger | action | owner), policy clauses, legal hold procedure, and implementation checklist. Copy prompt View page Show more ↓ Governance and Controls Intermediate Prompt 02 
### Privacy Notice Review 
Review this privacy notice / privacy policy for regulatory compliance and plain language quality.

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

Return: content checklist with status per item, plain language assessment, specific missing elements, specific vague language identified, and priority remediation list. Copy prompt View page Show more ↓ Governance and Controls Advanced Chain 03 
### Privacy Program Maturity Assessment 
Step 1: Data inventory and mapping — assess the completeness of the organization's personal data inventory. Are all systems, all data flows, and all processors documented? Is the Record of Processing Activities (RoPA) current and comprehensive? Score: Incomplete (1) / Partial (2) / Documented (3) / Automated and maintained (4).

Step 2: Legal basis and consent — for each processing activity in the RoPA, is a valid legal basis documented? Has a Legitimate Interest Assessment been conducted where LI is claimed? Is consent management compliant (freely given, specific, informed, unambiguous, withdrawable, logged)? Score each on the 1–4 scale.

Step 3: Data subject rights — is there a documented DSAR intake process? Are response timelines met consistently? Is there a searchable data map enabling complete responses? Are all rights (access, erasure, portability, objection, restriction) operationalized? Score: No process (1) / Ad hoc (2) / Documented process (3) / Automated and tracked (4).

Step 4: Breach management — is there a documented breach detection and response process? Is the 72-hour notification timeline achievable? Is a breach log maintained? Has the team been trained and has a tabletop exercise been conducted in the last 12 months? Score on the 1–4 scale.

Step 5: Vendor management — is there a vendor inventory of all data processors? Is a compliant DPA in place with each processor? Are sub-processors tracked? Are international transfers documented with appropriate safeguards? Is there a vendor assessment process for new onboarding? Score on the 1–4 scale.

Step 6: Privacy by design — is privacy impact assessment (DPIA) embedded in the product and project development lifecycle? Is there a trigger list for when DPIAs are required? Is data minimization practiced in system design? Score on the 1–4 scale.

Step 7: Governance and accountability — is there a designated DPO (if required)? Is there a privacy steering committee or equivalent? Is privacy training mandatory and tracked? Is the privacy program subject to regular audit? Are board-level privacy risk reports produced? Score on the 1–4 scale.

Final output: maturity heatmap (category × score), top 3 highest-priority gaps, a 12-month roadmap with specific actions to advance each dimension by at least one level, and an overall maturity verdict: Initial (avg < 2) / Developing (2–2.9) / Defined (3–3.4) / Managed (3.5–3.9) / Optimized (4.0). Copy prompt View page Show more ↓ 
## PII and Data Discovery 
3 prompt s PII and Data Discovery Intermediate Prompt 01 
### Automated PII Detection Prompt 
Design a prompt and validation framework for using LLMs to detect PII in unstructured text at scale.

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

Return: the detection prompt, JSON schema, validation framework, golden test set design, and redaction specification. Copy prompt View page Show more ↓ PII and Data Discovery Intermediate Prompt 02 
### Data Flow Mapping 
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

Return: processing activity table, legal basis mapping, data flow diagram, retention schedule, and RoPA entry. Copy prompt View page Show more ↓ PII and Data Discovery Beginner Prompt 03 
### PII Inventory Builder 
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

Return: PII inventory table, sensitive category flags, re-identification risk assessment, and gap list with recommended remediation. Copy prompt View page Show more ↓ 
## Privacy Impact and Risk 
3 prompt s Privacy Impact and Risk Advanced Prompt 01 
### Anonymization and Pseudonymization Assessment 
Assess whether this data is truly anonymized or only pseudonymized, and evaluate the re-identification risk.

Dataset: {{dataset_description}}
Claimed status: {{claimed_status}} (anonymized / pseudonymized / de-identified)
Intended use: {{intended_use}}

This distinction is critical: anonymized data falls outside GDPR's scope. Pseudonymized data is still personal data.

1. Definitions and legal significance:

 Anonymization (GDPR Recital 26):
 - Data that 'cannot be attributed to an identified or identifiable natural person'
 - The key test: is re-identification reasonably likely, taking into account all means reasonably likely to be used?
 - If truly anonymous: GDPR does not apply → can be used freely, shared openly, retained indefinitely
 - Caveat: near-impossible to prove true anonymization for complex datasets

 Pseudonymization (GDPR Art. 4(5)):
 - Data that 'can no longer be attributed to a specific data subject without the use of additional information'
 - Additional information (e.g. key linking pseudonym to identity) must be kept separately
 - Still personal data under GDPR — but reduces risk and is encouraged as a security measure
 - Examples: replacing name with a hash or random token, while retaining age and zip code

2. Re-identification risk evaluation:

 Apply the ICO's three-part test for anonymization:
 - Singling out: can you isolate one or more records that identify an individual?
 - Linkability: can you link records relating to the same individual or group?
 - Inference: can you deduce information about an individual with high probability?

 Specific techniques to assess:

 k-Anonymity:
 - For each combination of quasi-identifiers, at least k records share the same values
 - k = 1: not anonymous (individual is unique in the dataset)
 - Minimum acceptable k: typically 5 for general use, 10+ for sensitive data
 - Compute k for this dataset across the most identifying quasi-identifier combinations

 l-Diversity:
 - Extension of k-anonymity: within each equivalence class, the sensitive attribute has at least l distinct values
 - Protects against homogeneity attacks (all k records in a group share the same sensitive value)

 t-Closeness:
 - The distribution of the sensitive attribute in each group is close (within threshold t) to the distribution in the full dataset
 - Prevents skewness attacks

 Differential Privacy:
 - Mathematical guarantee: adding or removing one individual's record changes the output by at most a factor of e^ε
 - ε (epsilon): privacy budget. Lower ε = stronger privacy, less utility.
 - Ask: has differential privacy noise been applied? What is the epsilon value?

3. Common pseudo-anonymization mistakes:
 - Hashing without salting: SHA-256 of 'john.doe@email.com' is easily reversed by dictionary attack
 - Truncating postal codes: 5-digit zip may still be unique for small populations
 - Aggregation without k-anonymity: 'CEO of Company X, age 52, female' is identifiable
 - Releasing multiple 'anonymized' datasets that can be joined to re-identify
 - Unique record counts: if only 3 people in the dataset have a given combination, they are identifiable

4. Assessment verdict:
 - Is this data anonymized (GDPR does not apply) or pseudonymized (GDPR applies)?
 - If claimed to be anonymized: what is the re-identification risk level? (Negligible / Low / Medium / High)
 - What additional steps would be needed to achieve a defensible anonymization claim?

Return: anonymization vs pseudonymization classification, k-anonymity calculation, re-identification risk rating, specific vulnerabilities identified, and recommended additional protections. Copy prompt View page Show more ↓ Privacy Impact and Risk Intermediate Prompt 02 
### DPIA Template and Guidance 
Conduct a Data Protection Impact Assessment (DPIA) for this new processing activity.

Processing activity: {{activity_description}}
Organization: {{organization}}
Regulation: GDPR Article 35 (or equivalent: HIPAA PIA, CCPA risk assessment)

A DPIA is mandatory under GDPR Article 35 when processing is 'likely to result in a high risk.' Conduct one proactively for any new processing of personal data.

1. Is a DPIA required? (Screening)
 Mandatory triggers under GDPR Art. 35(3) — a DPIA IS required if the processing involves:
 - Systematic and extensive profiling or automated decision-making with significant effects
 - Large-scale processing of special category data (health, biometric, genetic, etc.)
 - Systematic monitoring of a publicly accessible area
 Supervisory authority criteria (high risk) — DPIA recommended if ≥ 2 apply:
 - Evaluation or scoring of individuals
 - Automated decision-making with legal or similarly significant effects
 - Systematic monitoring
 - Sensitive or highly personal data
 - Data processed at large scale
 - Matching or combining datasets
 - Data about vulnerable data subjects (children, elderly, employees)
 - Innovative technology (AI, biometrics, IoT)
 - Data transfer outside the EEA
 - Processing that prevents individuals from exercising their rights

2. Describe the processing:
 - Nature: how is data collected, stored, used, transmitted, and deleted?
 - Scope: volume of data subjects, data categories, geographic extent, duration
 - Context: what are the data subjects' reasonable expectations? Are they in a vulnerable position?
 - Purpose: what is the stated purpose? Is it legitimate, specific, and explicit?

3. Necessity and proportionality assessment:
 - Is this processing necessary to achieve the stated purpose? Could a less privacy-intrusive alternative achieve the same goal?
 - Is the data collected proportionate — only what is strictly necessary?
 - Is the retention period proportionate?
 - Is consent or another appropriate legal basis in place?

4. Risk identification:
 For each identified risk, assess likelihood and severity:

 Risk categories to consider:
 - Unauthorized access (breach, hacking, insider threat)
 - Unauthorized disclosure (accidental sharing, over-broad access)
 - Data loss or destruction (ransomware, accidental deletion)
 - Inaccuracy (incorrect data leading to wrong decisions about individuals)
 - Denial of rights (inability of data subjects to exercise access, deletion, or portation rights)
 - Function creep (data used for purposes beyond stated purpose)
 - Re-identification (supposedly anonymized data re-identified)
 - Automated decision-making harm (discriminatory or unfair algorithmic outcomes)

 Risk rating: Likelihood (Low/Medium/High) × Severity (Low/Medium/High) = Risk level

5. Risk mitigation measures:
 For each identified high risk, specify:
 - Technical measure (encryption, pseudonymization, access controls, audit logging)
 - Organizational measure (training, policy, DPA with processor, contractual clauses)
 - Residual risk after mitigation: is it acceptable?

6. DPO consultation and sign-off:
 - Has the Data Protection Officer been consulted? (Required under GDPR)
 - If residual risk remains high after mitigation: consult the supervisory authority before proceeding

7. DPIA outcome:
 - Proceed: residual risks are acceptable
 - Proceed with conditions: specific mitigations must be implemented before processing begins
 - Do not proceed: risks cannot be adequately mitigated

Return: DPIA screening outcome, processing description, necessity assessment, risk register with ratings, mitigation measures, residual risk assessment, and outcome recommendation. Copy prompt View page Show more ↓ Privacy Impact and Risk Intermediate Prompt 03 
### Vendor Privacy Risk Assessment 
Assess the privacy and data protection risk of engaging this third-party vendor who will process personal data on our behalf.

Vendor: {{vendor_name}}
Service description: {{service}}
Personal data involved: {{data_types}}
Contract type: {{contract_type}} (data processor, joint controller, independent controller)

Under GDPR Article 28, organizations are responsible for ensuring processors provide 'sufficient guarantees' of appropriate technical and organizational measures. This assessment validates those guarantees.

1. Determine the processing relationship:
 - Data Processor: vendor processes data only on our instructions, for our purposes → requires a Data Processing Agreement (DPA) under GDPR Art. 28
 - Joint Controller: both parties determine the purposes and means of processing → requires a joint controller agreement under GDPR Art. 26
 - Independent Controller: vendor uses data for their own purposes → they have independent obligations; a DPA alone is insufficient
 - Classify this vendor correctly — misclassification is a common compliance failure

2. Legal and contractual requirements:
 - Is a Data Processing Agreement (DPA) in place?
 - Does the DPA cover all GDPR Art. 28(3) required elements?
 ☐ Processes data only on documented instructions
 ☐ Ensures persons authorized to process are bound by confidentiality
 ☐ Implements appropriate technical and organizational security measures (Art. 32)
 ☐ Assists with data subject rights requests
 ☐ Assists with breach notification
 ☐ Deletes or returns all personal data after service ends
 ☐ Provides information for audits / compliance demonstrations
 ☐ Sub-processor restrictions: must obtain prior written authorization
 - If the DPA is missing any of the above: flag as a compliance gap

3. Sub-processor risk:
 - Does the vendor use sub-processors? List them.
 - Are sub-processors disclosed? Does the vendor notify of changes to sub-processors?
 - Are there DPAs in place between the vendor and their sub-processors?

4. International data transfer risk:
 - Is data transferred outside the EEA (for GDPR) or outside a jurisdiction with adequate protection?
 - If yes: what transfer mechanism is in place?
 - EU adequacy decision (check if still current — Schrems II invalidated Privacy Shield)
 - Standard Contractual Clauses (SCCs) — are the 2021 SCCs used?
 - Binding Corporate Rules (BCRs)
 - Other (derogations under Art. 49 — limited circumstances only)
 - Transfer impact assessment (TIA): has one been conducted for transfers to high-risk countries?

5. Security assessment:
 - What certifications does the vendor hold? (ISO 27001, SOC 2 Type II, CSA STAR, HIPAA BAA)
 - Request and review the vendor's most recent security audit report or SOC 2 report
 - Key controls to verify: encryption at rest and in transit, access controls, MFA, incident response plan, penetration testing frequency
 - Data segregation: is our data logically or physically isolated from other customers?

6. Data subject rights assistance:
 - Can the vendor respond to data subject access requests (DSARs) within 72 hours?
 - Can they support deletion requests? What is the deletion SLA?
 - Can they provide data portability in machine-readable format?

7. Risk rating and recommendation:
 - Overall risk: Low / Medium / High / Critical
 - Contractual gaps identified
 - Technical gaps identified
 - Recommendation: approve / approve with conditions / reject pending remediation

Return: processing relationship classification, DPA gap analysis, sub-processor list, transfer mechanism assessment, security control summary, and risk rating with recommendation. Copy prompt View page Show more ↓ 
## Regulatory Compliance 
3 prompt s Regulatory Compliance Advanced Prompt 01 
### Consent Management Audit 
Audit the consent management practices of this organization against GDPR and applicable regulations.

Organization: {{organization}}
Consent mechanisms in use: {{mechanisms}} (cookie banners, sign-up forms, marketing opt-ins, etc.)
Regulation: {{regulation}}

Consent under GDPR Article 7 must be freely given, specific, informed, and unambiguous. Pre-ticked boxes, bundled consent, and dark patterns are unlawful. Regulators have imposed significant fines for invalid consent.

1. Cookie consent audit:

 Check each element against GDPR requirements:
 - Is a cookie banner presented before any non-essential cookies are set?
 Violation: non-essential cookies active before consent is obtained
 - Does the banner present a genuine, equal choice? (Accept vs Reject — both equally prominent)
 Violation: 'Accept all' is a large bright button; 'Reject' requires multiple clicks or is hidden
 - Is there a 'Reject all' option at the first layer? (Required in France, Spain, Germany guidance)
 Violation: user must click through to 'manage preferences' to reject — a dark pattern
 - Are cookie categories described clearly? (Strictly necessary, analytics, marketing, personalization)
 Violation: vague descriptions like 'third-party cookies' without specifying purpose or cookie names
 - Can consent be withdrawn as easily as it was given?
 Violation: consent withdrawal requires contacting support; no accessible preference center
 - Is consent renewed at appropriate intervals? (ICO recommends no longer than 12 months)

 Common dark patterns to flag:
 - Pre-ticked boxes (unlawful)
 - Consent buried in terms and conditions (unlawful)
 - Guilt-tripping or emotionally manipulative language ('I don't want the best experience')
 - Hiding reject/withdraw options
 - Consent bundled with terms acceptance

2. Marketing consent audit:
 - Is marketing consent obtained separately from service terms? (Cannot be a condition of service)
 - Is the purpose of marketing communications specified at the point of consent?
 - Is the granularity appropriate? (Email marketing, SMS, phone, third-party sharing — each separately)
 - Is a timestamp recorded for when consent was given?
 - Is the exact consent text (as shown to the user) recorded?
 - Is there an easy unsubscribe mechanism in every marketing communication?
 - Is unsubscribe actioned within 10 business days?

3. Consent record requirements:
 Each consent record must capture:
 - Who gave consent (pseudonymous user ID or email)
 - When consent was given (timestamp)
 - What they consented to (exact purpose and scope)
 - How consent was obtained (mechanism, version of the consent text)
 - Proof that valid consent conditions were met
 - Whether consent has been withdrawn and when

4. Consent for sensitive data (GDPR Art. 9):
 - Health, genetic, biometric, religious, political, sexual orientation data: requires explicit consent
 - Explicit consent: active affirmation, cannot be implied — tick box or written statement required
 - Is explicit consent documented separately from standard consent?

5. Children's consent:
 - GDPR Art. 8: consent for information society services requires parental consent for under-16 (member states may lower to 13)
 - COPPA (US): verifiable parental consent required for under-13
 - Is there an age verification mechanism? How reliable is it?
 - What happens if a minor is identified after consent is given?

6. Audit findings format:
 For each issue: violation type | severity (critical/major/minor) | specific evidence | required remediation | deadline

Return: cookie consent audit checklist with findings, marketing consent audit, dark pattern violations, consent record requirements, children's consent assessment, and remediation priority list. Copy prompt View page Show more ↓ Regulatory Compliance Intermediate Prompt 02 
### Data Breach Response Playbook 
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

Return: breach classification matrix, 72-hour timeline with actions, risk assessment framework, notification templates, and post-breach logging requirements. Copy prompt View page Show more ↓ Regulatory Compliance Beginner Prompt 03 
### Data Subject Rights Request Handler 
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

Return: rights and deadline reference table, intake and verification workflow, system search procedure, response templates, and audit logging design. Copy prompt View page Show more ↓ 
## Other AI prompt roles 
Analytics Engineer (dbt) 20 prompts Browse Analytics Engineer (dbt) prompts Business Analyst 50 prompts Browse Business Analyst prompts Citizen Data Scientist 24 prompts Browse Citizen Data Scientist prompts Cloud Data Engineer 20 prompts Browse Cloud Data Engineer prompts Data Analyst 72 prompts Browse Data Analyst prompts Data Engineer 35 prompts Browse Data Engineer prompts Data Scientist 50 prompts Browse Data Scientist prompts Data Visualization Specialist 23 prompts Browse Data Visualization Specialist prompts Database Engineer 18 prompts Browse Database Engineer prompts DataOps Engineer 16 prompts Browse DataOps Engineer prompts Ecommerce Analyst 20 prompts Browse Ecommerce Analyst prompts Financial Analyst 22 prompts Browse Financial Analyst prompts Healthcare Data Analyst 25 prompts Browse Healthcare Data Analyst prompts LLM Engineer 20 prompts Browse LLM Engineer prompts Marketing Analyst 30 prompts Browse Marketing Analyst prompts ML Engineer 42 prompts Browse ML Engineer prompts MLOps 35 prompts Browse MLOps prompts Product Analyst 16 prompts Browse Product Analyst prompts Prompt Engineer 18 prompts Browse Prompt Engineer prompts Prompts Engineer 18 prompts Browse Prompts Engineer prompts Quantitative Analyst 27 prompts Browse Quantitative Analyst prompts Research Scientist 32 prompts Browse Research Scientist prompts SQL Developer 16 prompts Browse SQL Developer prompts Statistician 17 prompts Browse Statistician prompts MLJAR Studio AI for Data Analysis 
- Terms of Service 
- Privacy Policy 
- AI Policy 
- Licenses 
### AI Data Analysis Examples 

- LLM Benchmark on AI Data Analysis 
- Air Passengers Forecast 
- Iris Classification 
- Customer Churn Prediction 
- Energy Consumption Forecast 
### Resources 

- Example Python notebooks 
- Fix ModuleNotFoundError 
- Glossary 
- Brand 
- Answers 
- ML Algorithm Comparison 
- Research 
- Solutions 
### Products 

- MLJAR Studio 
- MLJAR AutoML 
- AI Data Analyst 
- AutoLab Experiments 
- Mercury 
### Tutorials 

- AutoML in Python: Beginner Tutorial with House Prices 
### Open Source 

- MLJAR AutoML 
- Mercury 
- More ... 
### AI Prompts 

- Prompts for Data Professionals 
- Data Analyst prompts 
- Business Analyst prompts 
- Data Scientist prompts 
- ML Engineer prompts 
- Data Engineer prompts 
- MLOps prompts 
### Compare 

- MLJAR Studio vs Julius 
- MLJAR Studio vs H2O 
- MLJAR Studio vs DataRobot 
- MLJAR Studio vs Jupyter 
- MLJAR Studio vs ChatGPT 
- MLJAR Studio vs Cursor 
### Company 

- Contact us 
- Services 
- About us 
- Blog Made by MLJAR. All rights reserved. Created in 🇵🇱 We ❤ you! 
We collect traffic information to improve the site. 

Data is collected in a privacy-friendly way (IP anonymization, no ads, no cross-site tracking). 
Analytics are only enabled if you accept. 
Read Privacy Policy Reject Accept
