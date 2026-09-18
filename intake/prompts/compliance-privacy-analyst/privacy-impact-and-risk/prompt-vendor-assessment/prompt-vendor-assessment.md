# Vendor Privacy Risk Assessment *AI Prompt *

Assess the privacy and data protection risk of engaging this third-party vendor who will process personal data on our behalf. Vendor: {{vendor_name}} Service description: {{serv... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: processing relationship classification, DPA gap analysis, sub-processor list, transfer mechanism assessment, security control summary, and risk rating with recommendation. 
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

The AI should return a structured result that covers the main requested outputs, such as Determine the processing relationship:, Data Processor: vendor processes data only on our instructions, for our purposes → requires a Data Processing Agreement (DPA) under GDPR Art. 28, Joint Controller: both parties determine the purposes and means of processing → requires a joint controller agreement under GDPR Art. 26. The final answer should stay clear, actionable, and easy to review inside a privacy impact and risk workflow for compliance & privacy analyst work. 

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
