# Prioritization Framework *AI Prompt *

This prompt helps compare initiatives and justify investments using structured business reasoning. It is useful when teams need to decide what to do first, how much value a proposal could create, or whether a case is strong enough for approval. The output should combine financial logic, prioritization discipline, and an executive-friendly recommendation. It compares initiatives using multiple prioritization methods so trade-offs become visible and discussable. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Prioritize this backlog of initiatives or features: {{backlog_list}}

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

Return: scoring table for all three frameworks, priority quadrant assignments, consensus top 5, and a recommended sequence. 
```

## When to use this prompt 
Use case 01 
Use when several initiatives compete for limited budget, time, or team capacity. 
Use case 02 
Use when you need a more disciplined way to justify an investment or recommendation. 
Use case 03 
Use when stakeholders will ask for value, cost, risk, and payback before approving work. 
Use case 04 
Use when you need both a quantitative assessment and an executive recommendation. 

## What the AI should return 

The AI should return a structured business recommendation with the requested scoring, financial logic, or prioritization framework clearly shown. Assumptions should be visible, trade-offs should be explicit, and the final recommendation should be practical for decision-makers. The result should support approval, sequencing, or investment discussion rather than just analysis for its own sake. 

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

Once you have the first result, continue deeper with related prompts in Business Case and Prioritization.
