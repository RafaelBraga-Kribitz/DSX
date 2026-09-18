# Web and Digital Analytics *AI Prompts *

4 Marketing Analyst prompts in Web and Digital Analytics. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 4 single prompts. 

## AI prompts in Web and Digital Analytics 
4 prompts Intermediate Single prompt 01 
### Conversion Rate Optimization Analysis 

Identify conversion rate optimization (CRO) opportunities across this website. Analytics data: {{analytics_data}} Heatmap and session recording data: {{heatmap_data}} (if availa... 
Prompt text Identify conversion rate optimization (CRO) opportunities across this website.

Analytics data: {{analytics_data}}
Heatmap and session recording data: {{heatmap_data}} (if available)
Key conversion goal: {{conversion_goal}}

1. Funnel visualization:
 Map the steps from landing to conversion:
 - Step 1: landing page entry
 - Step 2: [next step]
 - ...
 - Final step: conversion complete
 - Drop-off rate at each step
 - Identify the single biggest drop-off: this is the priority for CRO

2. Page-level analysis for priority pages:
 For each high-traffic, high-drop-off page:
 - Exit rate: what % leave the site from this page?
 - Time on page: are users engaging or bouncing quickly?
 - Scroll depth: how far down the page do users scroll?
 - Click distribution (from heatmap): are users clicking the right elements?

3. Form analysis (if applicable):
 - Form abandonment rate: started but not submitted
 - Which form field has the highest abandonment rate? (Indicates friction or required information concerns)
 - Time to complete the form
 - Error rate per field

4. Mobile vs desktop conversion gap:
 - Mobile conversion rate vs desktop conversion rate
 - If mobile is significantly lower: mobile UX is a priority
 - Page speed on mobile: Core Web Vitals for mobile specifically

5. Traffic source conversion rate comparison:
 - Conversion rate by acquisition channel
 - If paid traffic converts much lower than organic: landing page relevance may be poor
 - Are paid campaign landing pages dedicated pages or generic product pages?

6. Prioritized CRO test backlog:
 - Generate 10 specific test hypotheses
 - Each with: page, element to test, hypothesis, expected lift, effort (Low/Medium/High)
 - Score by ICE and prioritize

Return: funnel drop-off analysis, page-level insights, form analysis, mobile gap, source conversion comparison, and prioritized CRO test backlog. Copy prompt Open prompt details Intermediate Single prompt 02 
### GA4 Event Tracking Audit 

Audit the Google Analytics 4 event tracking implementation for completeness and data quality. GA4 property: {{property}} Business goals: {{goals}} Current events tracked: {{even... 
Prompt text Audit the Google Analytics 4 event tracking implementation for completeness and data quality.

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

Return: key events audit table, data quality findings, conversion verification results, and top 5 missing event recommendations. Copy prompt Open prompt details Advanced Single prompt 03 
### Marketing Analytics Stack Audit 

Audit the marketing analytics stack for this organization and identify gaps, redundancies, and improvement opportunities. Current tools: {{tools_list}} Data flows: {{data_flows}... 
Prompt text Audit the marketing analytics stack for this organization and identify gaps, redundancies, and improvement opportunities.

Current tools: {{tools_list}}
Data flows: {{data_flows}}
Team capability: {{team_capability}}

1. Analytics stack layers:
 Map the current stack against these layers:
 - Data collection: (pixels, SDKs, server-side tagging, webhooks)
 - Data transport: (tag management, event streaming, APIs)
 - Data storage: (data warehouse, CDP, CRM, platform-native storage)
 - Data transformation: (dbt, Fivetran, custom ETL)
 - Analytics and reporting: (BI tool, platform dashboards, spreadsheets)
 - Activation: (email platform, ad platforms, personalization engine)

2. Data quality assessment per layer:
 - Collection: are all key events tracked? Are there data gaps?
 - Storage: is there a single source of truth or multiple conflicting sources?
 - Transformation: is business logic documented and version-controlled?
 - Reporting: do different teams use different definitions for the same metric?

3. Redundancy identification:
 - Are multiple tools doing the same job? (Two CDPs, two email platforms)
 - Can any tools be consolidated without loss of capability?
 - What is the total annual cost of the current stack?

4. Critical gaps:
 - Multi-touch attribution: is there a cross-channel attribution solution beyond platform-reported ROAS?
 - Customer identity resolution: can you link the same person across devices and channels?
 - Offline-to-online: is offline (store, call center) data connected to digital behavior?
 - Incrementality measurement: is there any program to measure true causal marketing impact?

5. Priority improvements:
 - Top 3 gaps with highest impact on marketing decision quality
 - For each: recommended solution, estimated implementation effort, expected ROI

6. Data governance:
 - Is there a marketing data dictionary? (Agreed definitions for all metrics)
 - Who owns each data source and is responsible for its quality?

Return: stack layer map, quality assessment, redundancy analysis, critical gaps, priority improvements, and governance recommendations. Copy prompt Open prompt details Beginner Single prompt 04 
### Website Traffic Analysis 

Analyze website traffic data and identify key trends and opportunities. GA4 or analytics data: {{analytics_data}} Time period: {{period}} Business goal: {{goal}} 1. Traffic over... 
Prompt text Analyze website traffic data and identify key trends and opportunities.

GA4 or analytics data: {{analytics_data}}
Time period: {{period}}
Business goal: {{goal}}

1. Traffic overview:
 - Total sessions, users, and page views
 - YoY and MoM trend for each
 - Sessions per user: how often do users return?
 - Average session duration and pages per session

2. Traffic source breakdown:
 - Sessions by channel: organic search, paid search, direct, referral, social, email, other
 - % of sessions by channel (channel mix)
 - YoY change in each channel's share: which channels are growing or shrinking?
 - Are we over-reliant on any single channel (> 40% from one source = concentration risk)?

3. Engagement quality by channel:
 - Bounce rate (or engagement rate in GA4) by channel
 - Session duration by channel
 - Pages per session by channel
 - Conversion rate by channel
 - Which channel drives the most engaged visitors? The least engaged?

4. Landing page analysis:
 - Top 20 landing pages by entry sessions
 - Bounce/engagement rate per landing page
 - Landing pages with high traffic but low engagement: content-traffic mismatch

5. Device and geography:
 - Mobile vs desktop vs tablet: sessions, engagement rate, conversion rate
 - Mobile share trend: is mobile growing? Does mobile convert at a lower rate?
 - Top geographies by traffic: any unexpected sources or gaps?

6. Conversion funnel from traffic:
 - Traffic to lead/sign-up/purchase conversion rate overall and by channel
 - Which pages are the top conversion exit points?

Return: traffic overview, channel mix analysis, engagement quality table, landing page insights, and conversion funnel summary. Copy prompt Open prompt details 
## Recommended Web and Digital Analytics workflow 
1 
### Conversion Rate Optimization Analysis 

Start with a focused prompt in Web and Digital Analytics so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### GA4 Event Tracking Audit 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Marketing Analytics Stack Audit 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Website Traffic Analysis 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
