# Accessibility and Standards *AI Prompts *

2 Data Visualization Specialist prompts in Accessibility and Standards. Copy ready-to-use templates and run them in your AI workflow. Covers intermediate → advanced levels and 2 single prompts. 

## AI prompts in Accessibility and Standards 
2 prompts Intermediate Single prompt 01 
### Accessibility Audit for Data Viz 

Audit this visualization for accessibility and recommend improvements. Visualization: {{visualization_description}} Deployment context: {{context}} (web, print, presentation, em... 
Prompt text Audit this visualization for accessibility and recommend improvements.

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

Return: accessibility audit table (issue, WCAG criterion, severity, fix), specific fixes for the visualization described, and alt text for the chart. Copy prompt Open prompt details Advanced Single prompt 02 
### Style Guide for Data Visualization 

Create a data visualization style guide for this organization. Organization: {{organization}} Brand colors: {{brand_colors}} Primary tools: {{tools}} Typography system: {{typogr... 
Prompt text Create a data visualization style guide for this organization.

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

Return: complete style guide document with all specifications, hex codes, template settings for each tool, and a one-page quick reference card. Copy prompt Open prompt details 
## Recommended Accessibility and Standards workflow 
1 
### Accessibility Audit for Data Viz 

Start with a focused prompt in Accessibility and Standards so you establish the first reliable signal before doing broader work. 
Jump to this prompt 2 
### Style Guide for Data Visualization 

Review the output and identify what needs follow-up, cleanup, explanation, or deeper analysis. 
Jump to this prompt
