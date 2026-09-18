# DPIA Template and Guidance *AI Prompt *

Conduct a Data Protection Impact Assessment (DPIA) for this new processing activity. Processing activity: {{activity_description}} Organization: {{organization}} Regulation: GDP... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: DPIA screening outcome, processing description, necessity assessment, risk register with ratings, mitigation measures, residual risk assessment, and outcome recommendation. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin privacy impact and risk work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Privacy Impact and Risk or the wider Compliance & Privacy Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Is a DPIA required? (Screening), Systematic and extensive profiling or automated decision-making with significant effects, Large-scale processing of special category data (health, biometric, genetic, etc.). The final answer should stay clear, actionable, and easy to review inside a privacy impact and risk workflow for compliance & privacy analyst work. 

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

Once you have the first result, continue deeper with related prompts in Privacy Impact and Risk.
