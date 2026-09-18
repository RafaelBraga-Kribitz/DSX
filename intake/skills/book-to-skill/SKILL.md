---
name: book-to-skill
description: Converts a technical book (PDF or EPUB) into a structured Claude Code skill — extracting frameworks, mental models, principles, techniques, and anti-patterns the author crystallized. Use when the user wants to study a book through Claude, apply an author's frameworks while working, or build a reusable knowledge base from any PDF or EPUB. Deeply integrated into all BMADS-MKT agents: every agent can say "Hey [Agent], convert this book to a skill" to grow the framework's knowledge base.
when_to_use: turn this book into a skill, create a skill from this PDF, create a skill from this EPUB, I want to study X book, add this book to my skills, convert PDF to skill, convert EPUB to skill, analyze this book, extract frameworks from this book, book to skill, learn from book, hey carla convert, hey diego convert, hey eva convert, hey marco convert, hey petra convert, hey otto convert
disable-model-invocation: true
context: fork
agent: general-purpose
allowed-tools: Bash(python3 *) Bash(pdftotext *) Bash(mkdir *) Bash(cp *) Bash(find *) Bash(wc *) Bash(echo *) Bash(cat *) Bash(date *) Read Write Glob Grep
argument-hint: <path-to-pdf-or-epub> [skill-name-slug]
arguments: [book_path, skill_name]
effort: high
---

# Book-to-Skill Converter

Transform written knowledge into actionable Claude Code skills by extracting structure — not producing summaries.

## Philosophy

Books contain crystallized expertise: frameworks, principles, and techniques that took years to develop. This skill extracts that knowledge into a format Claude can leverage repeatedly.

**Extract structure, not summaries.** A skill is a toolkit of:
- Named frameworks (mental models with clear application)
- Actionable principles (rules that guide decisions)
- Techniques (step-by-step methods)
- Anti-patterns (what to avoid and why)
- Voice calibration (how the author thinks and communicates)

**Preserve the author's precision.** "The 5 Whys" is not interchangeable with "ask why multiple times."

## MADS Integration

All BMADS-MKT agents can invoke this skill to grow the framework's domain knowledge.

### Suggested domains per agent:

**Carla (Marketing Strategist):**
- Marketing strategy, positioning, consumer psychology
- Causal inference for business
- Growth and retention frameworks

**Diego (Data Steward):**
- Data quality management and contracts
- Statistics and EDA methodology
- Database and analytics engineering

**Eva (Experiment Designer):**
- Causal inference textbooks
- A/B testing and experiment design
- Bayesian statistics for business

**Marco (DS/ML Engineer):**
- ML textbooks (ESL, ISLR, Hands-On ML)
- Feature engineering and MLOps
- Marketing Mix Modeling methodology

**Petra (Insights Lead):**
- Data storytelling (Knaflic, Few, Cairo)
- Executive communication and Minto Pyramid
- Dashboard design best practices

**Otto (MLOps Engineer):**
- Production ML systems
- Site Reliability Engineering
- Monitoring and observability

---

## Modes of Operation

Three paths available:

### 1. Full Conversion (Default)
Run all steps (0–10). Output: complete skill with SKILL.md, chapters/, glossary, patterns, cheatsheet.

### 2. Analyze Only
Run Steps 0–3, produce a structured extraction report. Stop — do NOT generate skill files.

### 3. Generate from Prior Analysis
Skip Steps 0–3, use provided analysis as input, run Steps 4–10.

---

## Step 0 — Out-of-scope check

If the argument is NOT a path to a PDF or EPUB file, stop and respond:
> "book-to-skill requires a PDF or EPUB path. Usage: `/book-to-skill /path/to/book.pdf [skill-name]`"

---

## Step 1 — Validate input

```bash
test -f "$0" && echo "FILE_OK" || echo "FILE_NOT_FOUND: $0"
```

Check file extension (`.pdf` or `.epub`) or magic bytes. If unsupported format, stop with clear error.

---

## Step 1.5 — Identify book type

Ask the user:
> "What kind of content does this book have?
> 1. **Technical** — code blocks, tables, formulas (programming books, academic papers)
> 2. **Text-heavy** — mostly prose (management, strategy, narrative non-fiction)
> 3. **Not sure** — use fast method"

Store as `BOOK_TYPE` (technical | text). Inform the user of the extraction method before proceeding.

---

## Step 2 — Extract text from PDF or EPUB

```bash
python3 ~/.claude/skills/book-to-skill/scripts/extract.py "$0" --mode <BOOK_TYPE>
```

- `--mode technical` → uses Docling (layout-aware, preserves tables and code)
- `--mode text` → uses pdftotext → PyPDF2 → pdfminer fallback chain

Outputs:
- `/tmp/book_skill_work/full_text.txt`
- `/tmp/book_skill_work/metadata.json`

---

## Step 2.5 — Pre-flight cost estimate

Present estimated token cost and files to be generated before proceeding. Wait for user confirmation.

---

## Step 3 — Analyze book structure

Read first 8,000 characters to identify: title, author(s), chapter structure, core themes.

**If Analyze Only mode:** produce extraction report and stop.

---

## Step 4 — Ask purpose

> "What should this skill help you do?
> 1. Apply the author's frameworks while working
> 2. Think with the author's mental models
> 3. Reference specific chapters and concepts
> 4. All of the above"

---

## Step 5 — Determine skill name

If `$1` provided, use it. Otherwise propose:
- **By author-concept**: `{author-lastname}-{core-concept}`
- **By title**: lowercase hyphens from title

Check that `~/.claude/skills/<skill_name>/` does NOT already exist.

---

## Step 6 — Create skill directory

```bash
mkdir -p ~/.claude/skills/<skill_name>/chapters
```

---

## Step 7 — Generate chapter summaries

For each chapter, create `~/.claude/skills/<skill_name>/chapters/ch<NN>-<slug>.md`:

```markdown
# Chapter N: <Full Title>

## Core Idea
<1–2 sentences>

## Frameworks Introduced
- **<Framework Name>**: <exact formulation>
  - When to use: <specific situation>
  - How: <steps or criteria>

## Key Concepts
- **<Term>**: <precise definition>

## Mental Models
<2–4 "Use X when Y" or "Think of X as Y">

## Anti-patterns
- **<What to avoid>**: <why it fails>

## Key Takeaways
1. <Actionable insight>
2. <Actionable insight>
```

TOKEN BUDGET: 800–1,200 tokens per chapter file.

---

## Step 8 — Generate supporting files

- `glossary.md` — all significant terms, alphabetically sorted (max 1,500 tokens)
- `patterns.md` — all concrete techniques and design patterns (max 2,000 tokens)
- `cheatsheet.md` — decision tables, quick-reference rules (max 1,000 tokens)

---

## Step 9 — Generate master SKILL.md

**CRITICAL: Keep SKILL.md body under 4,000 tokens.**

```markdown
---
name: <skill_name>
description: Knowledge base from "<Full Title>" by <Author(s)>. Use when applying <author>'s frameworks for <key topics>.
when_to_use: <10–15 trigger phrases>
allowed-tools: Read Grep
argument-hint: [topic, framework name, or chapter number]
---

# <Full Title>
**Author**: <Author(s)> | **Pages**: ~<N> | **Chapters**: <N>

## Core Frameworks & Mental Models
<~2,000 tokens of most critical frameworks — preserve exact names>

## Chapter Index
| # | Title | Key Frameworks |
|---|-------|----------------|
...

## Topic Index
- **<Term>** → ch<N>
...

## Supporting Files
- [glossary.md](glossary.md)
- [patterns.md](patterns.md)
- [cheatsheet.md](cheatsheet.md)
```

---

## Step 10 — Cleanup and report

```bash
rm -rf /tmp/book_skill_work
```

Report to the user: skill name, book title/author, files generated, total size, usage examples.

---

## Quality Rules

1. Extract structure, not summaries
2. Preserve the author's precision
3. Density over completeness
4. Practitioner voice: "Use X when Y"
5. Front-load SKILL.md
6. Never copy raw book text — synthesize, extract signal
