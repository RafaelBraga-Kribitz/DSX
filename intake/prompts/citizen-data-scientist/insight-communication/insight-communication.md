# Insight Communication *AI Prompts *

5 Citizen Data Scientist prompts in Insight Communication. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 5 single prompts. 

## AI prompts in Insight Communication 
5 prompts Beginner Single prompt 01 
### Chart Caption Writer 

Write a clear, insightful caption for this data visualization that tells the audience what to notice and what it means. Chart description: {{chart_description}} Audience: {{audi... 
Prompt text Write a clear, insightful caption for this data visualization that tells the audience what to notice and what it means.

Chart description: {{chart_description}}
Audience: {{audience}}
Key finding in the chart: {{key_finding}}

Most chart captions are bad because they describe what the chart shows rather than what it means. A good caption answers: 'So what?'

1. The headline caption (1 sentence, bold):
 - State the insight, not a description of the chart
 - Wrong: 'Monthly revenue from January to December 2024'
 - Right: 'Revenue peaked in March before falling steadily — Q4 is 23% below Q1'
 - The headline should be a complete sentence with a verb, not a label

2. The supporting caption (1–2 sentences):
 - Add the most important context or implication that the headline did not capture
 - Point the reader to something specific: 'Note the sharp drop in August, which coincides with the system outage'
 - If the finding is surprising: explain briefly why that matters

3. Data note (optional, smaller text):
 - Source of the data
 - Any important caveat about how to read the chart (e.g. 'revenue excludes refunds')

4. Write 3 alternative headline options:
 - Option A: factual and neutral
 - Option B: action-oriented (implies what should happen)
 - Option C: question-framing (poses the key question the chart raises)

For each option, explain in one sentence who it would be most appropriate for (analyst audience, executive audience, public-facing report). Copy prompt Open prompt details Intermediate Single prompt 02 
### Data Story Builder 

Help me build a data story that takes my audience from the current situation to a clear recommendation. My data findings: {{findings}} My audience: {{audience}} The decision I w... 
Prompt text Help me build a data story that takes my audience from the current situation to a clear recommendation.

My data findings: {{findings}}
My audience: {{audience}}
The decision I want them to make: {{desired_decision}}

A data story is not a data dump. It is a narrative that uses data as evidence to make a persuasive case.

1. The opening hook (1–2 sentences):
 - Start with something that makes the audience care: a surprising number, a relatable scenario, or the cost of inaction
 - Do not start with 'The purpose of this analysis is...'

2. The context (2–3 sentences):
 - What is the situation? Why are we looking at this now?
 - What were we expecting or hoping for?

3. The finding (the heart of the story):
 - What does the data actually show?
 - Present the key insight with supporting evidence — not a list of all findings, just the most important one
 - Acknowledge any counterintuitive or surprising element — it builds credibility

4. The implication (so what?):
 - What does this finding mean for the business?
 - What happens if we ignore it?
 - Quantify the impact if possible: revenue at risk, cost savings available, customers affected

5. The recommendation (the ask):
 - State one clear, specific action
 - Say who should do it, by when, and what the expected outcome is
 - Acknowledge the main objection your audience might have and address it briefly

6. The narrative structure check:
 - Does each section naturally lead to the next?
 - Could someone who did not see the data repeat your key point accurately to a colleague?

Write the complete data story following this structure. Copy prompt Open prompt details Beginner Single prompt 03 
### Findings to Executive Summary 

Turn my data findings into a clear executive summary that a non-technical leader can understand and act on. My findings: {{findings}} Audience: {{audience}} (e.g. VP of Sales, C... 
Prompt text Turn my data findings into a clear executive summary that a non-technical leader can understand and act on.

My findings: {{findings}}
Audience: {{audience}} (e.g. VP of Sales, CFO, Operations Director)
Decision needed: {{decision_needed}}

1. Lead with the so-what — not the analysis:
 - The first sentence must state the business implication, not the data finding
 - Wrong: 'Revenue declined 14% in Q3 compared to Q2'
 - Right: 'We are at risk of missing the annual target by $2.3M if Q4 revenue does not recover — here is what drove Q3's decline'

2. Use the SCR structure (Situation, Complication, Resolution):
 - Situation (1–2 sentences): what is the context? What were we expecting or hoping for?
 - Complication (2–3 sentences): what did the data reveal that is different from expectations? Include the key numbers.
 - Resolution (2–3 sentences): what does this mean for the decision at hand? What do you recommend?

3. Make every number meaningful:
 - Every statistic must have context: '14% decline' should be '14% decline — the largest quarter-over-quarter drop in 3 years'
 - Translate percentages to absolute impact where possible: '14% decline = $1.8M less than the same period last year'
 - Replace 'significant' with the actual number

4. One clear ask:
 - End with a single, specific request: a decision, an action, or a resource
 - Do not list 5 options — give one recommendation with a brief rationale

5. Length and format:
 - Maximum 200 words for the summary
 - One supporting table or chart description if needed
 - No bullet lists of raw statistics — write in paragraphs

Write the executive summary now, following these principles. Copy prompt Open prompt details Advanced Single prompt 04 
### Handling Stakeholder Pushback 

A business stakeholder is pushing back on my data findings. Help me respond thoughtfully and maintain credibility. My finding: {{my_finding}} Stakeholder's objection: {{objectio... 
Prompt text A business stakeholder is pushing back on my data findings. Help me respond thoughtfully and maintain credibility.

My finding: {{my_finding}}
Stakeholder's objection: {{objection}}

1. First, take the objection seriously:
 Before preparing a rebuttal, ask: is the stakeholder raising a legitimate concern?
 - 'The data might be wrong' → Check: is there a reason the data quality could be an issue here?
 - 'This does not match what I see on the ground' → Check: is there a segment or time period the data is missing?
 - 'That cannot be right' → Check: have you double-checked the calculation?
 - 'The analysis method is wrong' → Check: is there a better method you should consider?

2. Classify the objection:
 - Factual objection (they dispute the data itself) → Respond with evidence and methodology
 - Interpretation objection (they agree on the data but disagree on the conclusion) → Explore the alternative interpretation together
 - Emotional objection (the finding is inconvenient or threatening) → Acknowledge the difficulty while holding the finding
 - Expertise objection (they know the domain better) → Listen carefully — they may be right

3. Prepare your response:
 For each objection type, draft a response that:
 - Acknowledges their perspective genuinely: 'That is a fair challenge to raise'
 - Addresses the substance of the concern with evidence
 - Does not become defensive or dismissive
 - Leaves the conversation open rather than closing it: 'What data would change your view?'

4. When to concede:
 - If the stakeholder raises a point that genuinely undermines the finding: concede it clearly and update your conclusion
 - Conceding when warranted builds far more credibility than defending a flawed finding

5. Draft the actual response:
 Write a 3–5 sentence response to the specific objection above that is confident but not combative. Copy prompt Open prompt details Intermediate Single prompt 05 
### Simplify Technical Findings 

I have technical analysis results that I need to explain to a non-technical business audience. Help me translate them into plain language without losing the key insights. Techni... 
Prompt text I have technical analysis results that I need to explain to a non-technical business audience. Help me translate them into plain language without losing the key insights.

Technical findings: {{technical_findings}}
Audience: {{audience}} (their background: {{audience_background}})

1. Jargon replacement guide:
 For each technical term in my findings, provide the plain English replacement:
 - 'Statistically significant' → 'We can be confident this difference is real, not just random'
 - 'Correlation of 0.73' → 'When X goes up, Y tends to go up about 73% of the time'
 - 'Regression model' → 'A mathematical formula that calculates the predicted value based on other factors'
 - 'Confidence interval' → 'The range within which the true answer almost certainly falls'
 - 'Null hypothesis rejected' → 'The data shows a clear difference — it is not just chance'
 Apply this principle to every technical term in my specific findings.

2. Translate each finding:
 For each technical finding, write:
 - The plain English version (1–2 sentences, no jargon)
 - A concrete analogy or example that makes it tangible
 - The business implication in one sentence

3. What to leave out:
 - Methodological details your audience does not need to evaluate the conclusion
 - Intermediate results that do not change the recommendation
 - Caveats that are technically important but would not change the action taken
 (note separately: caveats that ARE important enough to share, and how to phrase them without undermining your findings)

4. The 'can they repeat it?' test:
 After writing the simplified version, check: could your audience repeat the key finding accurately in a conversation with their own colleagues?
 If no: simplify further. If yes: you are done.

Return: the translated findings, the jargon glossary, and a 3-bullet 'take-away' summary for the audience. Copy prompt Open prompt details 
## Recommended Insight Communication workflow 
1 
### Chart Caption Writer 

Start with a focused prompt in Insight Communication so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Data Story Builder 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Findings to Executive Summary 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Handling Stakeholder Pushback 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
