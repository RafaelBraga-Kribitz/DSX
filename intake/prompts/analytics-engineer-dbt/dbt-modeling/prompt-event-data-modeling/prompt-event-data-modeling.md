# Event Data Modeling *AI Prompt *

Model raw event data (clickstream, product events) into analytics-ready tables using dbt. Event source: {{event_source}} (Segment, Amplitude, custom event log) Key events: {{eve... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Model raw event data (clickstream, product events) into analytics-ready tables using dbt.

Event source: {{event_source}} (Segment, Amplitude, custom event log)
Key events: {{events}} (page_viewed, button_clicked, signed_up, purchased)
Destination: {{warehouse}}

1. Raw event structure:
 Typical raw event schema:
 - event_id: unique identifier for each event
 - event_name: the event type
 - user_id: actor (may be anonymous pre-login)
 - anonymous_id: cookie or device identifier for pre-login events
 - properties: JSON blob of event-specific attributes
 - received_at, sent_at, original_timestamp: event timing

2. Staging layer — event-type-specific models:
 Create one staging model per event type to extract the relevant properties:

 stg_events__page_viewed:
 SELECT
 event_id,
 user_id,
 anonymous_id,
 received_at AS viewed_at,
 properties:page_url::varchar AS page_url,
 properties:referrer::varchar AS referrer
 FROM {{ source('segment', 'tracks') }}
 WHERE event_name = 'page_viewed'

3. Identity stitching (anonymous_id → user_id):
 Build an identity map:
 SELECT
 anonymous_id,
 FIRST_VALUE(user_id) OVER (
 PARTITION BY anonymous_id
 ORDER BY received_at
 ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
 ) AS resolved_user_id
 FROM {{ ref('stg_events__all') }}
 WHERE user_id IS NOT NULL

4. Session modeling:
 Define a session as: a group of events from the same user with < 30-minute gaps.
 USE LAG to find time since last event; a gap > 30 minutes = new session.

5. Funnel models:
 Build per-user, per-session event sequences:
 SELECT
 user_id,
 session_id,
 MIN(CASE WHEN event_name = 'viewed_product' THEN event_time END) AS viewed_product_at,
 MIN(CASE WHEN event_name = 'added_to_cart' THEN event_time END) AS added_cart_at,
 MIN(CASE WHEN event_name = 'purchased' THEN event_time END) AS purchased_at
 FROM {{ ref('int_events__sessionized') }}
 GROUP BY 1, 2

Return: staging model patterns for event data, identity stitching logic, session modeling SQL, and funnel model design. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin dbt modeling work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in dbt Modeling or the wider Analytics Engineer (dbt) library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Raw event structure:, event_id: unique identifier for each event, event_name: the event type. The final answer should stay clear, actionable, and easy to review inside a dbt modeling workflow for analytics engineer (dbt) work. 

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

Once you have the first result, continue deeper with related prompts in dbt Modeling.
