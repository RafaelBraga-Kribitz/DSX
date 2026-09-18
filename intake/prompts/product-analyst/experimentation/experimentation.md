# Experimentation *AI Prompts *

2 Product Analyst prompts in Experimentation. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 2 single prompts. 

## AI prompts in Experimentation 
2 prompts Advanced Single prompt 01 
### Experiment Readout Template 

Write a complete experiment readout for this concluded A/B test. Experiment: {{experiment_name}} Hypothesis: {{hypothesis}} Results data: {{results}} Audience: product team and... 
Prompt text Write a complete experiment readout for this concluded A/B test.

Experiment: {{experiment_name}}
Hypothesis: {{hypothesis}}
Results data: {{results}}
Audience: product team and leadership

1. TL;DR (3 sentences):
 - What was tested, what was the result, and what is the recommendation?

2. Background:
 - Problem being solved
 - Hypothesis and expected direction of change
 - Primary metric and guardrail metrics

3. Setup:
 - Variants: control and treatment description
 - Traffic allocation and targeting
 - Test duration and sample size achieved vs required

4. Results:
 - Primary metric: control value, treatment value, absolute difference, % difference, p-value, 95% CI
 - Secondary metrics: same format for each
 - Guardrail metrics: did any degrade significantly?
 - Segment breakdown: results by key segments (mobile/desktop, new/returning, plan type)

5. Interpretation:
 - Is the result statistically significant? Practically significant?
 - Are results consistent across segments or driven by one segment?
 - Any unexpected findings worth investigating?

6. Decision:
 - Ship / Do not ship / Iterate / Run follow-up test
 - If shipping: rollout plan (% of traffic, timeline)
 - If iterating: what specifically changes in the next version?

7. Learnings:
 - What did this test teach us about user behavior?
 - How does this inform future experiments or roadmap decisions?

Return: complete experiment readout document suitable for sharing with the product team. Copy prompt Open prompt details Intermediate Single prompt 02 
### Product Experiment Prioritization 

Prioritize this backlog of product experiments for the next quarter. Experiment ideas: {{experiment_list}} Current traffic: {{daily_active_users}} DAU Team capacity: {{capacity}... 
Prompt text Prioritize this backlog of product experiments for the next quarter.

Experiment ideas: {{experiment_list}}
Current traffic: {{daily_active_users}} DAU
Team capacity: {{capacity}} experiments per quarter

1. Score each experiment on ICE framework:
 - Impact (1-10): how much will this move the primary metric if it works?
 - Confidence (1-10): how sure are we the hypothesis is correct? (prior evidence, user research)
 - Ease (1-10): how quickly and cheaply can this be built and measured?
 - ICE score = (Impact + Confidence + Ease) / 3

2. Feasibility check:
 - For each experiment: calculate required sample size at 80% power, alpha=0.05, and the team's stated MDE
 - Calculate required duration: sample_size / (DAU x traffic_allocation_rate)
 - Flag experiments requiring > 8 weeks as impractical for the quarter

3. Dependency and conflict check:
 - Are any experiments testing overlapping UI elements or user flows? (Cannot run simultaneously)
 - Does any experiment depend on another being completed first?
 - Map experiment conflicts and dependencies

4. Learning value:
 - Even if a test is negative, what do we learn?
 - Prioritize experiments that resolve fundamental product questions over marginal optimizations

5. Recommended quarter plan:
 - Select experiments that fit within capacity, avoid conflicts, and maximize learning
 - Sequence them: which experiments must run first to unblock others?
 - Reserve 20% capacity for urgent or opportunistic tests

Return: ICE scoring table, feasibility check, conflict map, and recommended quarter experiment plan with sequencing. Copy prompt Open prompt details 
## Recommended Experimentation workflow 
1 
### Experiment Readout Template 

Start with a focused prompt in Experimentation so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Product Experiment Prioritization 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt
