# GA4 Event Tracking Audit *AI Prompt *

Audit the Google Analytics 4 event tracking implementation for completeness and data quality. GA4 property: {{property}} Business goals: {{goals}} Current events tracked: {{even... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Audit the Google Analytics 4 event tracking implementation for completeness and data quality.

GA4 property: {{property}}
Business goals: {{goals}}
Current events tracked: {{events_list}}

1. Key events audit:
 For each business goal, is the corresponding key event being tracked?
 - Lead generation: form_submit event with form_id, form_type parameters
 - E-commerce: purchase event with transaction_id, value, currency, items array
 - Engagement: video_start, video_complete, scroll depth (75% minimum), file_download
 - Account actions: sign_up, login, subscription_start, subscription_cancel
 - Content: outbound_click, internal_search, search_results_viewed

2. Data quality checks:
 - Are event parameters consistently named? (purchase vs Purchase vs PURCHASE = three separate events)
 - Are revenue events double-counting? (Both client-side and server-side firing)
 - Are null values appearing in required parameters? (item_id = null in purchase events)
 - Are session and user counts plausible given actual traffic?

3. Conversion tracking verification:
 - Test each key event in DebugView: fires at the right moment, with correct parameters?
 - Compare GA4 conversions to CRM / payment processor records: within 10% variance?
 - Are conversions cross-device (GA4 uses Google Signals)? Is cross-device linking enabled?

4. Audience building for remarketing:
 - Are the right events configured as key events for audience building?
 - Recommended audiences: all visitors, product viewers, cart abandoners, past purchasers, high-value customers

5. Data retention settings:
 - Event data retention: set to 14 months (not the default 2 months for comparative analysis)
 - User data: review for GDPR/CCPA compliance

6. Missing event recommendations:
 Based on the audit, list the top 5 events that are missing or misconfigured, with:
 - Event name and parameters
 - Implementation priority
 - Business value of tracking this event

Return: key events audit table, data quality findings, conversion verification results, and top 5 missing event recommendations. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin web and digital analytics work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Web and Digital Analytics or the wider Marketing Analyst library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Key events audit:, Lead generation: form_submit event with form_id, form_type parameters, E-commerce: purchase event with transaction_id, value, currency, items array. The final answer should stay clear, actionable, and easy to review inside a web and digital analytics workflow for marketing analyst work. 

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

Once you have the first result, continue deeper with related prompts in Web and Digital Analytics.
