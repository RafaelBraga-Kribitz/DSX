# Funnel Analysis *AI Prompts *

3 Product Analyst prompts in Funnel Analysis. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 3 single prompts. 

## AI prompts in Funnel Analysis 
3 prompts Beginner Single prompt 01 
### Conversion Funnel Audit 

Audit the conversion funnel for {{product_flow}} and identify the highest-impact drop-off points. Funnel stages provided: {{stages_and_counts}} 1. Compute conversion rates: - St... 
Prompt text Audit the conversion funnel for {{product_flow}} and identify the highest-impact drop-off points.

Funnel stages provided: {{stages_and_counts}}

1. Compute conversion rates:
 - Step-by-step conversion rate: users_at_step_N / users_at_step_N-1
 - Cumulative conversion rate: users_at_each_step / users_at_top_of_funnel
 - Overall funnel conversion: bottom_of_funnel / top_of_funnel

2. Identify the biggest drop-offs:
 - Rank steps by absolute user loss (not just % drop)
 - Rank steps by % conversion rate (lowest = most leaky)
 - Flag any step with conversion rate below {{threshold}}%

3. Benchmark against industry standards:
 - What is a typical conversion rate for each step in {{industry}}?
 - Which steps are performing below benchmark?

4. Segment the funnel:
 - Break conversion rates by: new vs returning users, device (mobile/desktop), traffic source, user cohort
 - Which segments have the lowest conversion at the biggest drop-off step?
 - Are any segments converting exceptionally well? (Best practice to replicate)

5. Qualitative context:
 - For the top 2 drop-off steps: list 3 possible reasons users are leaving
 - What data would confirm or rule out each reason?

6. Prioritized recommendations:
 - Top 3 interventions ranked by expected impact on overall funnel conversion
 - For each: hypothesis, test design, and expected lift

Return: funnel table with conversion rates, drop-off ranking, segment breakdown, and prioritized recommendations. Copy prompt Open prompt details Intermediate Single prompt 02 
### Funnel Segmentation Deep Dive 

Analyze how conversion rates differ across key user segments in this funnel. Funnel data: {{funnel_data}} Segmentation dimensions: {{dimensions}} (e.g. acquisition channel, devi... 
Prompt text Analyze how conversion rates differ across key user segments in this funnel.

Funnel data: {{funnel_data}}
Segmentation dimensions: {{dimensions}} (e.g. acquisition channel, device, plan type, geography, user tenure)

1. Per-segment funnel tables:
 For each dimension, produce a funnel table showing conversion at every step broken out by segment value.
 Highlight: which segment has the highest overall conversion? Which has the lowest?

2. Segment-step interaction:
 - Are drop-off patterns consistent across segments, or does one segment struggle at a specific step?
 - Example: mobile users may convert well at sign-up but drop at payment entry
 - Identify any step where segment A converts at more than 2x segment B

3. Volume-weighted impact:
 - A segment with 5% conversion but only 2% of volume has low total impact
 - Compute: (segment volume %) x (conversion gap vs best segment) = impact score
 - Rank segments by impact score to prioritize where improvement matters most

4. Cohort conversion analysis:
 - Do users acquired in recent months convert better or worse than older cohorts?
 - Is there a trend suggesting the product is getting easier or harder to convert?

5. Statistical significance:
 - For the largest conversion gap between segments: run a proportion z-test
 - Is the difference significant (p < 0.05) or within random variation?

6. Recommendations:
 - Which segment should be targeted for conversion improvement first and why?
 - What product or UX change would most help the lowest-converting high-volume segment?

Return: per-segment funnel tables, segment-step interaction analysis, impact scores, significance test, and top recommendations. Copy prompt Open prompt details Advanced Single prompt 03 
### Multi-Touch Attribution for Product 

Analyze which in-product touchpoints and features most contribute to conversion or activation. User journey data: {{journey_data}} (user_id, touchpoint_type, touchpoint_timestam... 
Prompt text Analyze which in-product touchpoints and features most contribute to conversion or activation.

User journey data: {{journey_data}} (user_id, touchpoint_type, touchpoint_timestamp, converted: Y/N)
Conversion event: {{conversion_event}} (e.g. first purchase, plan upgrade, feature activation)

1. Touchpoint inventory:
 - List all unique touchpoints users encounter before the conversion event
 - Count how often each appears in converting vs non-converting journeys
 - What % of converters touched each touchpoint?

2. Attribution models - compare all three:

 First touch:
 - 100% credit to the first touchpoint the user interacted with
 - Best for: understanding what initiates the conversion journey

 Last touch:
 - 100% credit to the touchpoint immediately before conversion
 - Best for: understanding what closes the conversion

 Linear:
 - Equal credit to all touchpoints in the path
 - Best for: understanding overall touchpoint contribution

3. Path analysis:
 - What are the top 10 most common touchpoint sequences for converters?
 - What sequences do non-converters follow? Where do they diverge?
 - Is there a specific touchpoint combination that strongly predicts conversion?

4. Time-to-conversion by path:
 - Do users with certain touchpoint paths convert faster?
 - Is there a touchpoint that accelerates conversion when added to the path?

5. Recommendations:
 - Which touchpoints should be promoted (high attribution, currently under-used)?
 - Which touchpoints appear to delay or interrupt conversion?
 - What is the optimal path to guide new users through?

Return: touchpoint attribution table (all three models), top conversion paths, path divergence analysis, and recommendations. Copy prompt Open prompt details 
## Recommended Funnel Analysis workflow 
1 
### Conversion Funnel Audit 

Start with a focused prompt in Funnel Analysis so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Funnel Segmentation Deep Dive 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Multi-Touch Attribution for Product 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
