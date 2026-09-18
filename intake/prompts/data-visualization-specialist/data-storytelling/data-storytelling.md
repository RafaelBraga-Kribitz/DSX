# Data Storytelling *AI Prompts *

4 Data Visualization Specialist prompts in Data Storytelling. Copy ready-to-use templates and run them in your AI workflow. Covers beginner → advanced levels and 4 single prompts. 

## AI prompts in Data Storytelling 
4 prompts Intermediate Single prompt 01 
### Before and After Comparison Design 

Design a visualization that effectively communicates before-and-after comparison. Scenario: {{scenario}} (policy change, product launch, intervention, etc.) Before period: {{bef... 
Prompt text Design a visualization that effectively communicates before-and-after comparison.

Scenario: {{scenario}} (policy change, product launch, intervention, etc.)
Before period: {{before}}
After period: {{after}}
Metric: {{metric}}

1. Chart options for before/after:

 Slope chart (most effective for 2-point comparison):
 - Two vertical axes (Before | After)
 - Each entity is a line connecting its before value to its after value
 - Lines going up = improved, lines going down = declined
 - Color-code by direction: green for improvement, red for decline, grey for neutral
 - Best for: comparing many entities before/after a single event

 Paired bar chart:
 - Two bars per entity (before in grey, after in color)
 - Sort by the change magnitude (largest improvement first)
 - Add a difference annotation between each pair
 - Best for: few entities with absolute value comparison needed

 Dumbbell chart:
 - A horizontal dot plot variant
 - One dot for before, one dot for after, connected by a line
 - Dot size can encode a third variable (e.g. sample size)
 - Best for: clean, minimal presentation of many entities

 Difference area chart:
 - Two lines (before and after) with the area between them shaded
 - Green shading where after > before, red shading where after < before
 - Best for: showing the cumulative effect over time

 Bump chart:
 - Showing rank changes rather than absolute changes
 - Lines connecting before-rank to after-rank for each entity
 - Best for: rankings, leaderboards, or relative position changes

2. Choosing the right chart:
 - 2 entities: paired bar or slope chart
 - 3–10 entities: slope chart or dumbbell
 - > 10 entities: dumbbell or filtered slope (highlight top/bottom movers)
 - Rank focus: bump chart
 - Time series with intervention line: annotated line chart with shaded 'after' region

3. Statistical context:
 - Is the before-after difference statistically significant?
 - Add error bars or confidence intervals where sample sizes are small
 - Label the change magnitude on the chart (not just the before and after values)

4. Intervention line:
 - On a time series: mark the exact intervention date with a vertical dashed line
 - Label the line: 'Campaign launch (Mar 15)'
 - Shade the before period lightly grey, the after period white

Return: recommended chart type with rationale, design specification, and statistical context requirements. Copy prompt Open prompt details Intermediate Single prompt 02 
### Executive Presentation Chart Set 

Design a set of 3–5 charts for an executive presentation on this topic. Topic: {{topic}} Key message: {{key_message}} Audience: C-suite / senior leadership Time available: {{tim... 
Prompt text Design a set of 3–5 charts for an executive presentation on this topic.

Topic: {{topic}}
Key message: {{key_message}}
Audience: C-suite / senior leadership
Time available: {{time}} minutes
Data available: {{data_available}}

Executive audiences have specific needs: they want the conclusion first, they need context without detail overload, and they make decisions — so every chart must point to an action.

1. Chart 1 — The headline chart (30 seconds):
 - Must communicate the single most important finding
 - Should be readable in < 5 seconds
 - Title IS the conclusion: 'EMEA Revenue Is 23% Below Target — Driven by Germany'
 - Minimal detail — highlight only the critical element
 - Maximum 1 annotation

2. Chart 2 — The context chart (60 seconds):
 - Shows the trend or baseline that explains why the headline matters
 - Answers: 'Is this getting better or worse?'
 - Time series with the key threshold or target line shown

3. Chart 3 — The breakdown chart (60 seconds):
 - Decomposes the headline into its components
 - Answers: 'Where is this concentrated?'
 - A ranked breakdown by the most actionable dimension (by team, by product, by region)

4. Chart 4 (optional) — The root cause chart (60 seconds):
 - Shows what is driving the breakdown
 - Answers: 'Why is this happening?'
 - A correlation, funnel, or attribution chart

5. Chart 5 (optional) — The implication chart (30 seconds):
 - Projects the impact if no action is taken
 - Or shows the potential gain if the recommended action is taken
 - Answers: 'What happens if we do / don't act?'

6. Executive chart design rules:
 - Use only one key message per chart — no chart with two conclusions
 - No table with more than 5 rows (executives do not read tables in presentations)
 - Font size minimum 18pt for any text in the chart
 - Never show error bars, confidence intervals, or p-values in executive presentations
 - Remove every axis, gridline, and label that is not strictly necessary
 - Color: use brand colors + one highlight color only

Return: chart set specification (title, chart type, data elements, key message per chart) and presentation flow narrative. Copy prompt Open prompt details Beginner Single prompt 03 
### Insight Narrative Builder 

Build a visual narrative around this data insight for a presentation or report. Key insight: {{insight}} Supporting data: {{data}} Audience: {{audience}} Medium: {{medium}} (sli... 
Prompt text Build a visual narrative around this data insight for a presentation or report.

Key insight: {{insight}}
Supporting data: {{data}}
Audience: {{audience}}
Medium: {{medium}} (slide deck, scrollytelling web page, printed report, video)

1. The one-chart story structure:
 Every visualization that tells a story has three parts:
 - Setup: what is the context? What should the audience expect or know before seeing the data?
 - Tension: what is the surprising or important finding?
 - Resolution: what does this mean and what should we do?

 Apply these three parts to my specific insight.

2. Chart sequence for presentations (one chart per slide):
 Slide 1 — Context chart:
 - Show the baseline situation: the overall trend or the 'before' state
 - No highlighting yet — just the context
 - Title: a neutral statement of what is shown

 Slide 2 — Revelation chart:
 - Same chart, but now highlight the key finding
 - Grey out everything except the critical data point, region, or series
 - Title: the insight stated as a declarative sentence
 - Annotation: 1–2 callouts explaining the highlighted element

 Slide 3 — Implication chart:
 - A different chart showing the consequences or the 'so what'
 - If the finding is a problem: show the cost or impact
 - If the finding is an opportunity: show the potential gain
 - Title: the action or question this finding raises

3. Progressive disclosure technique:
 - Build the chart incrementally: start with one line/bar, add the others one by one
 - Each addition is a new point in the story
 - Reveal the key comparison last, after the audience understands the baseline

4. The scrollytelling version (for web):
 - Section 1: static chart with neutral context
 - Section 2: as user scrolls, highlight the anomaly
 - Section 3: annotate with the explanation
 - Section 4: transition to a different view showing the implication

5. What NOT to do:
 - Do not show all the data at once and hope the audience finds the insight
 - Do not use a single chart with 5 callouts — one chart, one point
 - Do not let the title be a label ('Revenue by Quarter') — make it the insight

Return: three-slide story structure with specific chart descriptions, title for each slide, and annotation text. Copy prompt Open prompt details Advanced Single prompt 04 
### Uncertainty and Error Visualization 

Design visualizations that communicate uncertainty, ranges, and confidence intervals without misleading the audience. Data type: {{data_type}} (forecast, survey results, experim... 
Prompt text Design visualizations that communicate uncertainty, ranges, and confidence intervals without misleading the audience.

Data type: {{data_type}} (forecast, survey results, experimental results, model output)
Audience: {{audience}}
Uncertainty type: {{uncertainty_type}} (sampling uncertainty, forecast range, measurement error)

1. Why uncertainty visualization matters:
 - A single line or point estimate implies false precision
 - Decision-makers need to understand the range of plausible outcomes
 - But: uncertainty visualizations are often misread — design for correct interpretation

2. Chart options for uncertainty:

 Error bars:
 - Show ±1 SD, ±1 SE, or 95% CI around a point estimate
 - Common mistake: error bars are often mislabeled — always state what they represent in the caption
 - Better for: point estimates with few comparisons

 Confidence bands:
 - Semi-transparent shaded region around a line
 - The line represents the central estimate; the band is the interval
 - Use low opacity (20–30%) to avoid obscuring the data
 - Better for: time series forecasts with uncertainty growing over time

 Gradient bands:
 - Multiple nested bands for different confidence levels (e.g. 50%, 80%, 95%)
 - Darker center = higher confidence; lighter outer = wider range
 - Better for: forecast fans where showing multiple scenarios is important

 Violin plots:
 - Show the full probability distribution of values for each group
 - Better than box plots for showing bimodal or skewed distributions
 - Combine with a box plot overlay to show median and quartiles

 Dot plots with distribution:
 - Individual observations as dots with a density curve overlay
 - Shows both the spread and any outliers
 - Better than summary statistics alone for small samples

 Hypothetical outcome plots (HOPs):
 - Animate multiple possible outcomes sampled from the distribution
 - Studies show HOPs lead to more accurate uncertainty interpretation than static bands
 - Suitable for: interactive web visualizations, not static reports

3. Common mistakes to avoid:
 - Showing only the point estimate without any range
 - Using error bars without labeling what they represent
 - Showing 95% CI and calling it 'possible range' — it excludes 5% of outcomes
 - Making the uncertainty band so wide it is useless
 - Hiding uncertainty because it 'looks bad' — this is dishonest and dangerous

4. Language for uncertainty:
 - Label: '95% confidence interval' not 'margin of error' (unless you mean exactly that)
 - Caption: always explain what the shaded region represents in plain language
 - For forecasts: show a plain-language probability statement: 'There is a 20% chance of exceeding $10M'

Return: recommended uncertainty visualization for this specific data, design specification, labeling language, and a caption explaining the uncertainty to a non-technical audience. Copy prompt Open prompt details 
## Recommended Data Storytelling workflow 
1 
### Before and After Comparison Design 

Start with a focused prompt in Data Storytelling so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Executive Presentation Chart Set 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt 3 
### Insight Narrative Builder 

Continue with the next prompt in the category to turn the result into a more complete workflow. 
Jump to this prompt 4 
### Uncertainty and Error Visualization 

When the category has done its job, move into the next adjacent category or role-specific workflow. 
Jump to this prompt
