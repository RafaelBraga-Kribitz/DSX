# Consent Management Audit *AI Prompt *

Audit the consent management practices of this organization against GDPR and applicable regulations. Organization: {{organization}} Consent mechanisms in use: {{mechanisms}} (co... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
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

Return: cookie consent audit checklist with findings, marketing consent audit, dark pattern violations, consent record requirements, children's consent assessment, and remediation priority list. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin regulatory compliance work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Regulatory Compliance or the wider Compliance & Privacy Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Cookie consent audit:, Is a cookie banner presented before any non-essential cookies are set?, Does the banner present a genuine, equal choice? (Accept vs Reject — both equally prominent). The final answer should stay clear, actionable, and easy to review inside a regulatory compliance workflow for compliance & privacy analyst work. 

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

Once you have the first result, continue deeper with related prompts in Regulatory Compliance.
