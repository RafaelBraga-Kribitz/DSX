# Assets

Images used by the README and the docs.

| File | What it is |
|---|---|
| `hero.png` | The banner at the top of the README. It is the committed output; nothing in this repository regenerates it. |
| `hero.layout.json` | The layout record for that banner: canvas size, fonts, and the text and position of each block. It was written by the author's portfolio banner generator, a tool that lives outside this repository (the commit history calls it the "portfolio hero generator"). Nothing here reads it; it is kept so the banner can be regenerated with the same layout. The file paths inside it point at the author's machine. |
| `Author_MDS_Rafael_Braga-Kribitz_kroped.png` | The author's portrait. |

To change the banner, edit it with the external generator and commit the new
`hero.png` together with its `hero.layout.json`.

The chart font is a separate asset: the Lato typeface in
[`styles/fonts/`](../../styles/fonts/) (regular and bold), used by the chart
style sheets and registered by `templates/dsx_plotstyle.py`. Its licence is the
SIL Open Font License 1.1, in [`styles/fonts/OFL.txt`](../../styles/fonts/OFL.txt).
