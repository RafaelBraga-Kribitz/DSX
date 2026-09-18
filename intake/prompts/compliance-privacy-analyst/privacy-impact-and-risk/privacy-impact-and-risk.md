# Privacy Impact and Risk *AI Prompts *

3 Compliance & Privacy Analyst prompts in Privacy Impact and Risk. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 3 single prompts. 

## AI prompts in Privacy Impact and Risk 
3 prompts Advanced Single prompt 01 
### Anonymization and Pseudonymization Assessment 

Assess whether this data is truly anonymized or only pseudonymized, and evaluate the re-identification risk. Dataset: {{dataset_description}} Claimed status: {{claimed_status}}... 
Prompt text Assess whether this data is truly anonymized or only pseudonymized, and evaluate the re-identification risk.

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

Return: anonymization vs pseudonymization classification, k-anonymity calculation, re-identification risk rating, specific vulnerabilities identified, and recommended additional protections. Copy prompt Open prompt details Intermediate Single prompt 02 
### DPIA Template and Guidance 

Conduct a Data Protection Impact Assessment (DPIA) for this new processing activity. Processing activity: {{activity_description}} Organization: {{organization}} Regulation: GDP... 
Prompt text Conduct a Data Protection Impact Assessment (DPIA) for this new processing activity.

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

Return: DPIA screening outcome, processing description, necessity assessment, risk register with ratings, mitigation measures, residual risk assessment, and outcome recommendation. Copy prompt Open prompt details Intermediate Single prompt 03 
### Vendor Privacy Risk Assessment 

Assess the privacy and data protection risk of engaging this third-party vendor who will process personal data on our behalf. Vendor: {{vendor_name}} Service description: {{serv... 
Prompt text Assess the privacy and data protection risk of engaging this third-party vendor who will process personal data on our behalf.

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

Return: processing relationship classification, DPA gap analysis, sub-processor list, transfer mechanism assessment, security control summary, and risk rating with recommendation. Copy prompt Open prompt details 
## Recommended Privacy Impact and Risk workflow 
1 
### Anonymization and Pseudonymization Assessment 

Start with a focused prompt in Privacy Impact and Risk so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### DPIA Template and Guidance 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Vendor Privacy Risk Assessment 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
