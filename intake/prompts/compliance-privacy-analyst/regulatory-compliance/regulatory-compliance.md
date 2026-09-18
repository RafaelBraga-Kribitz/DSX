# Regulatory Compliance *AI Prompts *

3 Compliance & Privacy Analyst prompts in Regulatory Compliance. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 3 single prompts. 

## AI prompts in Regulatory Compliance 
3 prompts Advanced Single prompt 01 
### Consent Management Audit 

Audit the consent management practices of this organization against GDPR and applicable regulations. Organization: {{organization}} Consent mechanisms in use: {{mechanisms}} (co... 
Prompt text Audit the consent management practices of this organization against GDPR and applicable regulations.

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

Return: cookie consent audit checklist with findings, marketing consent audit, dark pattern violations, consent record requirements, children's consent assessment, and remediation priority list. Copy prompt Open prompt details Intermediate Single prompt 02 
### Data Breach Response Playbook 

Build a data breach response playbook for this organization. Organization: {{organization}} Applicable regulations: {{regulations}} (GDPR, CCPA, HIPAA, state breach notification... 
Prompt text Build a data breach response playbook for this organization.

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

Return: breach classification matrix, 72-hour timeline with actions, risk assessment framework, notification templates, and post-breach logging requirements. Copy prompt Open prompt details Beginner Single prompt 03 
### Data Subject Rights Request Handler 

Design a workflow and response template for handling Data Subject Access Requests (DSARs) and other data subject rights requests. Regulation: {{regulation}} (GDPR, CCPA, PIPEDA,... 
Prompt text Design a workflow and response template for handling Data Subject Access Requests (DSARs) and other data subject rights requests.

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

Return: rights and deadline reference table, intake and verification workflow, system search procedure, response templates, and audit logging design. Copy prompt Open prompt details 
## Recommended Regulatory Compliance workflow 
1 
### Consent Management Audit 

Start with a focused prompt in Regulatory Compliance so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Data Breach Response Playbook 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Data Subject Rights Request Handler 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
