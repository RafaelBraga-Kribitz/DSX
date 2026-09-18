# Style Guide for Data Visualization *AI Prompt *

Create a data visualization style guide for this organization. Organization: {{organization}} Brand colors: {{brand_colors}} Primary tools: {{tools}} Typography system: {{typogr... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Create a data visualization style guide for this organization.

Organization: {{organization}}
Brand colors: {{brand_colors}}
Primary tools: {{tools}}
Typography system: {{typography}}
Audience for the style guide: {{audience}} (data analysts, developers, designers)

A style guide ensures all visualizations across the organization look coherent, communicate clearly, and meet accessibility standards.

1. Color system:
 PRIMARY PALETTE (for data encoding):
 - Primary: {{primary_color}} — use for the most important series or highlight
 - Secondary: 3–5 supporting colors for categorical series
 - Neutral: grey scale for non-data elements (axes, gridlines, background text)
 - Alert: one red/orange for negative values or warnings

 SEQUENTIAL PALETTES:
 - Single-hue: light-to-dark of the primary color
 - Multi-hue: define the start and end color (perceptually uniform progression)

 DIVERGING PALETTES:
 - Define: negative color, neutral midpoint color, positive color

 RULES:
 - Maximum 8 colors in any single chart
 - Never use color as the only encoding (add labels, patterns, or shapes)
 - All palettes must pass colorblind-safe test

2. Typography:
 - Chart title: {{heading_font}}, {{title_size}}pt, bold
 - Axis labels: {{body_font}}, 11pt, regular
 - Data labels: {{body_font}}, 10pt, regular
 - Annotations: {{body_font}}, 10pt, italic
 - Numbers: use tabular figures (all same width) for alignment in tables

3. Chart formatting standards:
 - Minimum chart width: 480px (for web); 3 inches (for print)
 - Minimum height: 60% of width for most charts
 - Background: white (#FFFFFF) or transparent
 - Gridlines: horizontal only, light grey (#E0E0E0), 0.5pt
 - No chart borders or shadows
 - Axis lines: left axis only (y-axis), light grey, 0.5pt
 - Tick marks: none unless necessary

4. Chart title standards:
 - Format: insight statement (not a label)
 - Length: 1 line maximum for presentation; 2 lines for reports
 - Capitalization: sentence case (not title case)
 - No period at end of title

5. Number formatting:
 - Revenue: $1.2M (> $1M), $456K (> $1K), $123 (< $1K)
 - Percentages: 23.4% (1 decimal), 100% (no decimal)
 - Counts: comma separator every 3 digits
 - Dates: 'Jan 2024' for months, 'Q1 2024' for quarters, '2024' for years
 - Ratios: 2.3× (not 2.3x)

6. Template files:
 - Provide: Tableau workbook template, Power BI template file, Python rcParams settings

Return: complete style guide document with all specifications, hex codes, template settings for each tool, and a one-page quick reference card. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin accessibility and standards work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Accessibility and Standards or the wider Data Visualization Specialist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Color system:, Primary: {{primary_color}} — use for the most important series or highlight, Secondary: 3–5 supporting colors for categorical series. The final answer should stay clear, actionable, and easy to review inside a accessibility and standards workflow for data visualization specialist work. 

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

Once you have the first result, continue deeper with related prompts in Accessibility and Standards.
