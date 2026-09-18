# Business Case and Prioritization *AI Prompts *

3 Business Analyst prompts in Business Case and Prioritization. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 2 single prompts · 1 chain. 

## AI prompts in Business Case and Prioritization 
3 prompts Advanced Chain 01 
### Full Business Case Chain 

This prompt helps compare initiatives and justify investments using structured business reasoning. It is useful when teams need to decide what to do first, how much value a proposal could create, or whether a case is strong enough for approval. The output should combine financial logic, prioritization discipline, and an executive-friendly recommendation. It builds a full executive business case from problem statement through options, financials, risks, and ask. 
Prompt text Step 1: Problem statement — define the business problem or opportunity with quantified impact. What is the cost of doing nothing?
Step 2: Options analysis — identify 3 solution options including a 'do nothing' baseline. For each: description, pros, cons, rough cost, and rough benefit.
Step 3: Recommended option — select the best option with a clear rationale. Why does it outperform the alternatives?
Step 4: Detailed financials — build the full ROI model for the recommended option: implementation costs, ongoing costs, benefits by category, NPV, ROI, and payback period.
Step 5: Risk assessment — identify the top 5 risks to the business case. For each: probability, impact, mitigation strategy, and residual risk.
Step 6: Implementation overview — high-level timeline, key milestones, resource requirements, and dependencies.
Step 7: Write the executive business case: one-page summary covering — problem, recommended solution, financial case (3 key numbers), key risks, and the ask (decision required, investment needed, timeline to decide). Copy prompt Open prompt details Intermediate Single prompt 02 
### Prioritization Framework 

This prompt helps compare initiatives and justify investments using structured business reasoning. It is useful when teams need to decide what to do first, how much value a proposal could create, or whether a case is strong enough for approval. The output should combine financial logic, prioritization discipline, and an executive-friendly recommendation. It compares initiatives using multiple prioritization methods so trade-offs become visible and discussable. 
Prompt text Prioritize this backlog of initiatives or features: {{backlog_list}}

Apply three prioritization frameworks and compare:

1. RICE Score: (Reach × Impact × Confidence) / Effort
 - Reach: how many users or customers affected per period?
 - Impact: how much does it move the key metric? (1=minimal, 2=low, 3=medium, 4=high, 5=massive)
 - Confidence: how sure are we? (100%=high, 80%=medium, 50%=low)
 - Effort: person-months to implement

2. Value vs Effort matrix:
 - Plot each initiative on a 2×2: value on y-axis, effort on x-axis
 - Quadrants: Quick Wins (high value, low effort), Big Bets (high value, high effort), Fill-ins (low value, low effort), Money Pits (low value, high effort)

3. Strategic alignment score:
 - Rate each initiative 1–5 on alignment to each of the top 3 strategic objectives
 - Total score = sum of alignment ratings

After scoring with all three frameworks:
4. Identify the consensus top 5: initiatives ranked highly across all three methods
5. Flag any that appear in only one framework's top 5 — these need more discussion

Return: scoring table for all three frameworks, priority quadrant assignments, consensus top 5, and a recommended sequence. Copy prompt Open prompt details Beginner Single prompt 03 
### ROI Calculator 

This prompt helps compare initiatives and justify investments using structured business reasoning. It is useful when teams need to decide what to do first, how much value a proposal could create, or whether a case is strong enough for approval. The output should combine financial logic, prioritization discipline, and an executive-friendly recommendation. It structures the cost, benefit, risk, and payback case for a proposed initiative. 
Prompt text Build an ROI analysis for this proposed initiative: {{initiative_description}}

1. Costs (one-time):
 - Implementation cost: technology, professional services, internal labor
 - Training and change management
 - Testing and validation

2. Costs (ongoing annual):
 - Licensing or subscription fees
 - Maintenance and support
 - Ongoing internal labor

3. Benefits (annual):
 - Revenue increase: quantify and explain the mechanism
 - Cost reduction: quantify and explain what costs are reduced
 - Risk reduction: convert risk probability × impact to expected annual cost
 - Productivity gain: hours saved × hourly cost

4. Financial summary:
 - Total 3-year cost
 - Total 3-year benefit
 - Net benefit (benefit - cost)
 - ROI = (net benefit / total cost) × 100%
 - Payback period: months to break even
 - NPV at 10% discount rate

5. Sensitivity analysis:
 - What if benefits are 25% lower than expected?
 - What if costs are 25% higher?
 - At what benefit level does ROI turn negative?

Return: ROI model table, payback calculation, NPV, and sensitivity analysis. Copy prompt Open prompt details 
## Recommended Business Case and Prioritization workflow 
1 
### Full Business Case Chain 

Start with a focused prompt in Business Case and Prioritization so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Prioritization Framework 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### ROI Calculator 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt
