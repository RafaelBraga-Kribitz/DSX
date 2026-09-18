# Table Parsing Prompt *AI Prompt *

Design prompts that extract structured data from tables in various formats — HTML, Markdown, PDF text, and ASCII. Tables from documents are often the richest data source but are... Copy this prompt template, run it in your AI tool, and use related prompts to continue the workflow. 
Prompt with Instructions 
```
Design prompts that extract structured data from tables in various formats — HTML, Markdown, PDF text, and ASCII.

Tables from documents are often the richest data source but are structurally complex. LLMs can parse them, but need explicit instructions to do so reliably.

1. Table parsing challenges:
 - Multi-row headers (the column meaning is in 2 rows, not 1)
 - Merged cells (a cell spans multiple rows or columns)
 - Implicit structure (blank cells mean 'same as above')
 - Footnotes that modify cell values (values marked with * have different meaning)
 - Mixed data types in the same column

2. Table parsing prompt structure:

 Step 1 — Table understanding:
 'First, describe the structure of this table: how many rows and columns, what the headers mean, and any structural complexity (merged cells, multi-row headers, footnotes).'

 Step 2 — Header normalization:
 'List the column headers as they will appear in the output. If headers span multiple rows, combine them into a single descriptive name. Example: a table with "Revenue" in row 1 and "Q1 | Q2 | Q3" in row 2 produces columns: revenue_q1, revenue_q2, revenue_q3.'

 Step 3 — Row extraction:
 'Extract each data row as a JSON object. Resolve all implicit structure: fill in blank cells with the value from the cell above. Handle footnotes: if a cell has a footnote marker, include a footnote_[column] field with the footnote text.'

 Step 4 — Output:
 'Return a JSON array of objects, one per data row (excluding headers). Column names must match Step 2.'

3. Format-specific instructions:

 HTML tables:
 'Parse the <table> element. Handle colspan and rowspan attributes to correctly assign values to cells.'

 Markdown tables:
 'Parse the pipe-delimited table. The first row after |---|---| is the header. Each subsequent row is a data row.'

 PDF extracted text (hardest):
 'The table has been extracted from a PDF and may have alignment artifacts. Use column position context to assign values to the correct column even if whitespace is irregular.'

4. Validation:
 - After extraction: 'Verify that the number of values in each row matches the number of headers. Flag any row with a mismatch.'

Return: parsing prompts for each format, a test with a complex table (merged cells, footnotes), expected JSON output, and validation code. 
```

## When to use this prompt 
Use case 01 
Use it when you want to begin output formatting and extraction work without writing the first draft from scratch. 
Use case 02 
Use it when you want a more consistent structure for AI output across projects or datasets. 
Use case 03 
Use it when you want prompt-driven work to turn into a reusable notebook or repeatable workflow later. 
Use case 04 
Use it when you want a clear next step into adjacent prompts in Output Formatting and Extraction or the wider Prompts Engineer library. 

## What the AI should return 

The AI should return a structured result that covers the main requested outputs, such as Table parsing challenges:, Multi-row headers (the column meaning is in 2 rows, not 1), Merged cells (a cell spans multiple rows or columns). The final answer should stay clear, actionable, and easy to review inside a output formatting and extraction workflow for prompts engineer work. 

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

Once you have the first result, continue deeper with related prompts in Output Formatting and Extraction.
