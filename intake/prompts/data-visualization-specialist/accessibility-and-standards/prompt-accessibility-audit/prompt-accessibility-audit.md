# Accessibility Audit for Data Viz *AI Prompt *

Audit this visualization for accessibility and recommend improvements. Visualization: {{visualization_description}} Deployment context: {{context}} (web, print, presentation, em... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Audit this visualization for accessibility and recommend improvements.

Visualization: {{visualization_description}}
Deployment context: {{context}} (web, print, presentation, embedded application)
Target WCAG level: {{wcag_level}} (AA is the standard; AAA for government/public sector)

1. Color accessibility:
 - Color contrast: check foreground vs background for all text and key visual elements
 - Normal text: minimum 4.5:1 contrast ratio (WCAG AA)
 - Large text (18pt+ or 14pt bold): minimum 3:1
 - Visual elements (charts, icons): minimum 3:1 against adjacent colors
 - Color independence: can the chart be understood by someone who cannot see color?
 - Add: patterns, shapes, textures, or direct labels as alternatives to color-only encoding
 - Colorblind simulation: run the chart through a deuteranopia / protanopia simulator

2. Text accessibility:
 - Minimum font size: 12pt for body text, 10pt minimum for chart labels
 - Font choice: avoid decorative or condensed fonts for data labels
 - Text alternatives: all charts need alt text describing the key finding (not just 'a bar chart')
 - Alt text format: 'Bar chart showing [metric] by [dimension]. [Key insight in one sentence]. [Data source and date range].'

3. Chart-specific accessibility:
 - Tables as alternatives: complex visualizations should have a data table option for screen readers
 - Keyboard navigation: interactive charts must be navigable by keyboard (Tab, Enter, Arrow keys)
 - Focus indicators: visible focus highlight for all interactive elements
 - ARIA labels: for web-based charts, add aria-label attributes to chart containers

4. Motion and animation:
 - Respect 'prefers-reduced-motion' media query — animations should be disableable
 - No flashing content at > 3Hz (seizure risk)
 - Provide static alternative for all animated charts

5. Cognitive accessibility:
 - Consistent layout: same chart types in the same position across pages/dashboards
 - Clear headings: descriptive titles and section headings
 - Plain language: chart titles use plain language, not industry jargon
 - Consistent color coding: same color always means the same thing
 - Avoid information overload: maximum 5–7 items requiring comparison per chart

6. Testing tools:
 - WebAIM Contrast Checker for color contrast
 - Deque's aXe browser extension for WCAG compliance
 - Screen reader testing: NVDA (Windows), VoiceOver (Mac/iOS)
 - Colorblind simulators: Coblis, Sim Daltonism

Return: accessibility audit table (issue, WCAG criterion, severity, fix), specific fixes for the visualization described, and alt text for the chart. 
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

The AI should return a structured result that covers the main requested outputs, such as Color accessibility:, Color contrast: check foreground vs background for all text and key visual elements, Normal text: minimum 4.5:1 contrast ratio (WCAG AA). The final answer should stay clear, actionable, and easy to review inside a accessibility and standards workflow for data visualization specialist work. 

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
