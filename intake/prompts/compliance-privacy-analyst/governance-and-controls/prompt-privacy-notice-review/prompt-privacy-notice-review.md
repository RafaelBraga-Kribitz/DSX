# Privacy Notice Review *AI Prompt *

Review this privacy notice / privacy policy for regulatory compliance and plain language quality. Privacy notice: {{privacy_notice_text}} Organization: {{organization}} Regulati... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: content checklist with status per item, plain language assessment, specific missing elements, specific vague language identified, and priority remediation list. 
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

The AI should return a structured result that covers the main requested outputs, such as Required content audit (GDPR Art. 13/14 checklist):, Plain language assessment:, Reading level: compute Flesch-Kincaid grade level. Target: ≤ Grade 8 for consumer-facing notices.. The final answer should stay clear, actionable, and easy to review inside a governance and controls workflow for compliance & privacy analyst work. 

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
