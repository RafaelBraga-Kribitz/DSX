# Color Strategy for Data Viz *AI Prompt *

Design a color strategy for this data visualization or dashboard. Visualization type: {{viz_type}} Data encoding needs: {{encoding_needs}} (categorical groups, sequential scale,... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design a color strategy for this data visualization or dashboard.

Visualization type: {{viz_type}}
Data encoding needs: {{encoding_needs}} (categorical groups, sequential scale, diverging scale, highlighting)
Brand colors: {{brand_colors}}
Accessibility requirement: {{accessibility}} (must pass WCAG AA color contrast, colorblind-safe)

1. Choose the right color palette type:

 CATEGORICAL (for distinguishing unordered groups):
 - Max 8 colors (human perceptual limit for distinct hues)
 - Colors should be equally distinct — avoid mixing light and dark versions of similar hues
 - Recommended: ColorBrewer Qualitative, Okabe-Ito (colorblind-safe), Tableau 10
 - Primary choice for: bar charts with multiple categories, multi-line charts, map choropleth regions

 SEQUENTIAL (for ordered numeric data, low to high):
 - Single hue: light (low values) → dark (high values)
 - Or perceptually uniform multi-hue: e.g. yellow → green → blue
 - Avoid: rainbow (jet) colormap — perceptually non-uniform, not colorblind-safe
 - Primary choice for: heatmaps, choropleth maps, scatter plots with continuous color encoding

 DIVERGING (for data with a meaningful midpoint):
 - Two hues diverging from a neutral center: e.g. blue — white — red
 - Center (zero or baseline) must be a neutral color (white, light grey)
 - Primary choice for: correlation matrices, market share vs benchmark, profit/loss maps

 HIGHLIGHT (single color to draw attention):
 - Use one accent color for the key data point or series; make everything else grey
 - Most powerful technique for directing viewer attention

2. Colorblind accessibility:
 Approximately 8% of males have red-green color blindness (deuteranopia/protanopia).
 - NEVER rely on red vs green alone to encode meaning (e.g. positive vs negative)
 - Safe alternatives for red/green distinction: use blue vs orange, or add symbols/patterns
 - Test: convert the palette to greyscale — can values still be distinguished?
 - Use: Okabe-Ito palette, Viridis, Cividis — these are designed to be distinguishable by all
 - Tool: Sim Daltonism, Color Oracle, or Coblis for simulating colorblind views

3. Color contrast (WCAG AA):
 - Text on colored background: minimum contrast ratio 4.5:1 (3:1 for large text)
 - Data elements (bars, lines, dots): minimum 3:1 contrast ratio against the background
 - Test using: WebAIM Contrast Checker or Figma plugins

4. Brand color integration:
 - Use the primary brand color for the most important data series only
 - Avoid using brand colors if they are not colorblind-safe (common for red-dominant brands)
 - Build a secondary palette around the brand primary using ColorBrewer rules

5. Color encoding rules:
 - Encode one thing at a time: don't use color AND size AND shape all for different dimensions
 - Be consistent: the same color always means the same thing across the dashboard
 - Don't use color for ordinal data: use sequential shades, not arbitrary colors

Return: palette specification (hex codes), palette type with rationale, colorblind test plan, contrast check, and usage rules. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin chart design principles work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Chart Design Principles or the wider Data Visualization Specialist library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Choose the right color palette type:, Max 8 colors (human perceptual limit for distinct hues), Colors should be equally distinct — avoid mixing light and dark versions of similar hues. The final answer should stay clear, actionable, and easy to review inside a chart design principles workflow for data visualization specialist work. 

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

Once you have the first result, continue deeper with related prompts in Chart Design Principles.
