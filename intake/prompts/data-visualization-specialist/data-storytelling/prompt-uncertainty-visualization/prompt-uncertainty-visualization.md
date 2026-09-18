# Uncertainty and Error Visualization *AI Prompt *

Design visualizations that communicate uncertainty, ranges, and confidence intervals without misleading the audience. Data type: {{data_type}} (forecast, survey results, experim... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design visualizations that communicate uncertainty, ranges, and confidence intervals without misleading the audience.

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

Return: recommended uncertainty visualization for this specific data, design specification, labeling language, and a caption explaining the uncertainty to a non-technical audience. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin data storytelling work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Data Storytelling or the wider Data Visualization Specialist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Why uncertainty visualization matters:, A single line or point estimate implies false precision, Decision-makers need to understand the range of plausible outcomes. The final answer should stay clear, actionable, and easy to review inside a data storytelling workflow for data visualization specialist work. 

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

Once you have the first result, continue deeper with related prompts in Data Storytelling.
