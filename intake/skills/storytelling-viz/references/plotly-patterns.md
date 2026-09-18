# Shared Plotly Patterns

Use these defaults for all BMADS-MKT visualizations unless the dataset needs something more specific.

## Layout Defaults

```python
layout = dict(
    font=dict(family="Inter, Helvetica Neue, Arial, sans-serif", size=12),
    title=dict(font=dict(size=16, color="#2E4057"), x=0.05, xanchor="left"),
    paper_bgcolor="#FAFAFA",
    plot_bgcolor="#FFFFFF",
    margin=dict(l=60, r=40, t=80, b=60),
    showlegend=True,
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
)
```

## Hover Templates

```python
# For line/bar charts with currency
hovertemplate = "<b>%{x}</b><br>%{y:,.0f}<extra></extra>"

# For percentage metrics
hovertemplate = "<b>%{x}</b><br>%{y:.1%}<extra></extra>"

# For scatter with labels
hovertemplate = "<b>%{text}</b><br>x: %{x:.2f}<br>y: %{y:.2f}<extra></extra>"
```

## Color Palette

```python
MADS_COLORS = {
    "primary": "#2E4057",
    "accent": "#E84855",
    "positive": "#3BB273",
    "neutral": "#8D99AE",
    "light": "#C8D3DF",
}

MADS_SEQUENCE = [
    "#2E4057", "#3BB273", "#E84855", "#8D99AE", "#F4A261", "#A8DADC"
]
```

## Confidence Interval Pattern

```python
# For experiment results — always show CI
def add_confidence_interval(fig, x, y, lower, upper, color="#2E4057"):
    fig.add_trace(go.Scatter(
        x=x + x[::-1],
        y=upper + lower[::-1],
        fill="toself",
        fillcolor=f"rgba({hex_to_rgb(color)},0.15)",
        line=dict(color="rgba(255,255,255,0)"),
        showlegend=False,
        hoverinfo="skip",
    ))
```

## Reference Line Pattern

```python
# Baseline / target line
fig.add_hline(
    y=baseline_value,
    line_dash="dash",
    line_color=MADS_COLORS["neutral"],
    annotation_text=f"Baseline: {baseline_value:.1%}",
    annotation_position="bottom right",
)
```

## Annotations

```python
fig.add_annotation(
    x=x_pos,
    y=y_pos,
    text="Key insight here",
    showarrow=True,
    arrowhead=2,
    arrowcolor=MADS_COLORS["accent"],
    font=dict(size=11, color=MADS_COLORS["accent"]),
    bgcolor="white",
    bordercolor=MADS_COLORS["accent"],
    borderwidth=1,
)
```

## Responsive Embed Wrapper

```html
<!-- preview.html wrapper pattern -->
<iframe
  id="viz"
  src="index.html"
  style="width:100%; border:none;"
  onload="resizeIframe(this)"
></iframe>
<script>
function resizeIframe(iframe) {
  iframe.style.height = iframe.contentWindow.document.documentElement.scrollHeight + 'px';
}
</script>
```

## Output Structure for MADS Projects

```
reports/viz/{chart-slug}/
├── index.html       ← the visualization
├── preview.html     ← local review wrapper
└── source-data.csv  ← if user provided local source file
```

## Source Line

Every chart must include a source line outside the plotting area:

```python
fig.add_annotation(
    text=f"Source: {source} | Date range: {date_range}",
    xref="paper", yref="paper",
    x=0, y=-0.08,
    showarrow=False,
    font=dict(size=10, color=MADS_COLORS["neutral"]),
    xanchor="left",
)
```
