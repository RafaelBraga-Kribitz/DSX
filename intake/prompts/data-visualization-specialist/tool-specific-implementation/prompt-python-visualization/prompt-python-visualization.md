# Python Visualization Code *AI Prompt *

Write production-quality Python visualization code for this chart. Chart type: {{chart_type}} Data: {{data_description}} Library preference: {{library}} (matplotlib, seaborn, pl... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Write production-quality Python visualization code for this chart.

Chart type: {{chart_type}}
Data: {{data_description}}
Library preference: {{library}} (matplotlib, seaborn, plotly, altair, bokeh)
Output format: {{output}} (static PNG/PDF, interactive HTML, Jupyter notebook)

1. Library selection guide:

 Matplotlib:
 - Best for: publication-quality static charts, full control over every element
 - Pros: complete control, widely supported, PDF/SVG export
 - Cons: verbose API, interactive features require additional work

 Seaborn:
 - Best for: statistical charts (distributions, regressions, heatmaps)
 - Pros: high-level API, beautiful defaults, statistical integration
 - Cons: built on matplotlib, limited interactivity

 Plotly:
 - Best for: interactive web-based charts
 - Pros: interactive by default, Plotly Express high-level API, Dash integration
 - Cons: larger files, not ideal for publication

 Altair:
 - Best for: declarative grammar-of-graphics style charts
 - Pros: concise code, vega-altair grammar, responsive
 - Cons: data size limit in browser (5000 rows default)

2. Code standards:
 - Use matplotlib style sheets or seaborn themes for consistent styling
 - Set figure size explicitly: fig, ax = plt.subplots(figsize=(10, 6))
 - Use clear variable names that match the data (not ax1, ax2)
 - Add docstring explaining what the function produces
 - Save with appropriate DPI: plt.savefig('chart.png', dpi=300, bbox_inches='tight')

3. Accessibility in code:
 - Set colorblind-safe palette: plt.rcParams['axes.prop_cycle'] = cycler(color=okabe_ito_palette)
 - Add alt text for web outputs
 - Ensure minimum font sizes: plt.rcParams['font.size'] = 12

4. Reusable function template:
 Write the chart as a function that accepts data and styling parameters:
 def create_[chart_name](data, title, color_col=None, highlight=None, save_path=None):
 'Creates a [description] chart from the provided DataFrame.'
 ...
 return fig, ax

5. For this specific chart:
 - Import statements needed
 - Data preparation steps
 - Chart creation code with full styling
 - Annotation code
 - Save/display code

Return: complete, runnable Python code with comments, color palette definition, and example usage. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin tool-specific implementation work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Tool-Specific Implementation or the wider Data Visualization Specialist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Library selection guide:, Best for: publication-quality static charts, full control over every element, Pros: complete control, widely supported, PDF/SVG export. The final answer should stay clear, actionable, and easy to review inside a tool-specific implementation workflow for data visualization specialist work. 

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

Once you have the first result, continue deeper with related prompts in Tool-Specific Implementation.
