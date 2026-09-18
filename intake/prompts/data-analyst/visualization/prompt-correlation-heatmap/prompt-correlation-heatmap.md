# Correlation Heatmap *AI Prompt *

Correlation Heatmap is a beginner prompt for visualization. This prompt helps the AI turn raw data into charts or dashboards that communicate insight clearly. It goes beyond simply plotting values by asking for chart choice, layout, annotations, and business interpretation. Use it when you need visuals that are ready for exploration, reporting, or stakeholder communication. It is best suited for direct execution against a real dataset. The requested output should remain approachable and easy to review, even for someone with limited analytical background. Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Create a well-designed correlation heatmap for the numeric columns in this dataset:

1. Compute the Pearson correlation matrix for all numeric columns
2. Plot as a heatmap using a diverging colormap: dark blue for strong positive correlation, dark red for strong negative, white for zero
3. Show only the lower triangle (remove redundant upper triangle)
4. Add the correlation coefficient value inside each cell, rounded to 2 decimal places
5. Bold or highlight cells where |r| > 0.7
6. Sort columns and rows so that highly correlated variables are clustered together (use hierarchical clustering on the correlation matrix)
7. Set figure size so all labels are readable without overlapping

Add a subtitle explaining what the strongest correlation means in business terms. 
```

## When to use this prompt 
Use case 01 
When you need a chart or dashboard that highlights the key message clearly. 
Use case 02 
When a table alone is not enough for stakeholders to understand the result. 
Use case 03 
When you want a presentation-ready visual with labels, annotations, and styling guidance. 
Use case 04 
When comparing segments, trends, correlations, or composition visually. 

## What the AI should return 

The AI should return the recommended chart specification, plotting code when appropriate, and a short interpretation of what the visual is meant to show. Titles, labels, annotations, and layout choices should be explicit so the output is presentation-ready rather than generic. If multiple charts are requested, they should be organized in a logical order and tied back to a single story. The final answer should make it clear what the viewer should notice first. 

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

Once you have the first result, continue deeper with related prompts in Visualization.
