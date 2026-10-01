---
name: latex-doc
description: Create, edit, fix, or review LaTeX documents (papers, proposals, writeups). Use when asked to build, create, add content to, fix errors in, or review/proofread a LaTeX document.
argument-hint: <task: init|add|fix|check> [--path <output_path>] [--context <path_to_notes_or_files>] [--graphs <graph_folder>]
---

# LaTeX Document Manager

Create, edit, fix, and review LaTeX documents for academic work.

## Trigger conditions

Invoke this skill when the user asks to:
- Create / build / start / set up a LaTeX document, paper, proposal, or writeup
- Add graphs, tables, sections, equations, or content to an existing document
- Fix / debug / resolve compilation errors in a document
- Review / check / proofread / audit a document
- Any task involving an article-class `.tex` file

## Task routing

Determine which task the user wants from `$ARGUMENTS` or their message:

| Keywords | Task |
|----------|------|
| create, build, start, initialize, new document, new paper | **Initialize** |
| add, insert, include, put, new section, new figure, new table | **Add** |
| fix, debug, error, broken, won't compile, doesn't compile | **Fix** |
| review, check, audit, proofread, typo, inconsistency | **Check** |

If the intent is ambiguous, ask the user which task they need.

## Style guide

All tasks must follow these formatting rules.

### Document structure convention
Standard academic paper ordering:
1. Title, author, date
2. Abstract
3. Introduction
4. Literature Review (or embedded in Introduction)
5. Model / Framework / Theory
6. Data
7. Empirical Strategy / Identification
8. Results
9. Mechanisms / Discussion
10. Conclusion
11. Bibliography
12. Appendix (if any)

### Graphs and figures
- Format: `\includegraphics[width=X\textwidth]{absolute_path.pdf}`
- Default width: `0.7\textwidth` for single figures
- Always wrap in a `figure` environment with `\centering`, `\caption{}`, and `\label{fig:name}`
- Place figures near the text that references them
- Use `\ref{fig:name}` in text to reference figures
- For side-by-side figures, use `subfigure` or `subcaption` with minipages
- After compiling, audit figures: check they fit within margins, adjust width if needed

### Tables
- Use `booktabs` style: `\toprule`, `\midrule`, `\bottomrule`
- Wrap in `table` environment with `\centering`, `\caption{}`, `\label{tab:name}`
- For regression tables from images: `\includegraphics` inside a `table` float
- For raw data: build with `tabular`, use `\footnotesize` or `\small` if dense
- Add table notes below with `\vspace{0.2cm} \footnotesize \textit{Notes:} ...`

### Math
- Use `align*` or `align` (numbered) for displayed equations
- Label important equations: `\label{eq:name}`
- Use the math shortcuts defined in the template: `\Exp`, `\Prob`, `\Ind`, `\Var`, `\Cov`
- Assumptions use the `assumption` environment
- Propositions, lemmas, theorems use their respective environments

### Citations
- Citekeys follow Zotero/Better BibTeX pattern: `authorShorttitleYear`
- Master bibliography: `<REFERENCES_BIB>`
- Style: `aer` (American Economic Review)
- Use `\cite{}` for in-text, `\citep{}` for parenthetical, `\citet{}` for textual

### Content philosophy
- Academic writing: precise, rigorous, concise
- Avoid filler phrases ("It is worth noting that...", "Interestingly...")
- Every paragraph should advance the argument
- Figures and tables should be self-contained (caption tells the full story)

---

## Task 1: Initialize

Create a new LaTeX document from scratch.

### Step 1.1: Confirm output path
Ask the user where the `.tex` file should be created if not already clear from the prompt or `$ARGUMENTS`.
- Default convention: `<PROJECTS_DIR>/<project_name>/<filename>.tex`
- Accept the path if the user specifies it explicitly.
- Never overwrite an existing file without asking first.

### Step 1.2: Read the template
Read the template at `<SKILLS_DIR>/latex-doc/template.tex`. This is the user's current preferred LaTeX template. Always use it as the base — never hardcode an older copy.

### Step 1.3: Gather context
Determine whether to pre-generate document sections. Sources of context (check all that apply):

1. **User prompt**: What did the user describe in their message? Extract the topic, purpose, and any structural hints (e.g., "with an empirical section", "a short proposal").
2. **Current working directory**: Read relevant files in the current path (e.g., `notes.md`, other `.md` or `.tex` files) that may inform the document structure. Use the Glob tool to scan for `*.md` and `*.tex` files in the working directory.
3. **Explicit context files**: If the user provides a path to notes, a markdown file, or any reference material (via `--context` argument or mentioned in the prompt), read those files.
4. **Graph folder**: If `--graphs` is provided, scan the folder to understand what figures are available.
5. **Conversation context**: Use any prior conversation context about the project.

### Step 1.4: Decide on sections
Based on gathered context, decide whether to pre-generate sections:

- **If sufficient context exists**: Generate a section skeleton with `\section{}`, `\subsection{}`, and `% comment` annotations explaining what each section should contain. Tailor the structure to the document type:
  - *Research proposal*: Introduction, Background, Research Questions, Data, Empirical Strategy, Mechanisms, Expected Contributions, Timeline, Conclusion
  - *Paper/draft*: Introduction, Literature Review, Model/Framework, Data, Results, Discussion, Conclusion
  - *Short writeup*: Introduction, Main Body sections as needed, Conclusion
  - *Custom*: Follow any structural cues from the user's prompt or notes

- **If minimal context**: Create the document with just `\section{Introduction}` and `\section{Conclusion}` as starting points, and tell the user they can provide more context for a richer skeleton.

### Step 1.5: Customize the template
Starting from the template file, make these replacements:

1. **Title**: Replace `TITLE` with an appropriate title derived from the prompt/context. If unclear, use a placeholder like `Working Title` and flag it.
2. **Author**: Keep the template's default author. Add co-authors only if the user specifies them.
3. **Sections**: Replace `% SECTIONS_PLACEHOLDER` with the generated section structure from Step 1.4.
4. **Bibliography**: The template already points to the user's master `.bib` file via the `<REFERENCES_PATH>` placeholder. Do NOT change this path. Do NOT create symlinks.

### Step 1.6: Write the file
Write the final `.tex` file to the confirmed output path. Do NOT overwrite an existing file without asking first.

### Step 1.7: Compile and verify
Follow the compilation protocol (see below). The document should compile with 0 errors. Common init-time issues: undefined citations (expected if no `\cite{}` added yet — this is fine).

### Step 1.8: Summary
Tell the user:
- Where the file was created
- What sections were generated and why
- Suggest next steps (e.g., "you can start filling in the Introduction" or "provide more context for richer sections")

---

## Task 2: Add

Add new content to an existing LaTeX document.

### Step 2.1: Parse what to add
Identify the content type:
- **Graphs/figures**: image files (PDF, PNG) to include as figures
- **Tables**: regression tables, summary statistics (as images or raw tabular)
- **Sections**: new section or subsection with content
- **Model/theory**: mathematical framework, propositions, proofs
- **Literature**: citations and discussion of papers
- **Text content**: paragraphs, bullet points, equations

Identify source material: file paths, folder of graphs, URLs, conversation context.

### Step 2.2: Read the current document
Read the full `.tex` file. Understand:
- Existing sections and their order
- Current label namespace (grep for `\label{`)
- Where new content logically fits
- Existing figure/table numbering

### Step 2.3: Decide placement
- If the user specifies where → obey exactly.
- If the user says "results" → add to the Results section.
- If no guidance: place content in the most logical section based on content type (figures near their discussion, tables in results, model in framework section).
- For graphs from a folder: the user may say "add these to the paper." Use subagents to analyze graphs (read images, check producing code), determine which section each belongs in, and place accordingly. Main results go in the body; robustness and auxiliary analysis go in the appendix.

### Step 2.4: Create the content

**Graphs/figures**:
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.7\textwidth]{absolute/path/to/graph.pdf}
    \caption{Descriptive caption that tells the full story.}
    \label{fig:descriptive_name}
\end{figure}
```
- Add `\ref{fig:descriptive_name}` reference in the surrounding text.
- For side-by-side figures, use `subfigure` or minipage layout.
- For a folder of graphs: organize main results as body figures, robustness/supplementary as appendix figures.

**Tables**:
```latex
\begin{table}[htbp]
    \centering
    \caption{Table title.}
    \label{tab:descriptive_name}
    \begin{tabular}{lcc}
        \toprule
        ...
        \bottomrule
    \end{tabular}
    \vspace{0.2cm}
    \footnotesize
    \textit{Notes:} Explanation of the table.
\end{table}
```
- If table is a PDF image: use `\includegraphics` inside the `table` float instead of `tabular`.

**Model/theory slides**: Use `assumption`, `proposition`, `lemma`, `theorem` environments. Write precise mathematical statements with `align*`. Label key equations.

**Literature**: Add `\cite{}` / `\citep{}` references. Search `<REFERENCES_BIB>` for citekeys. If a paper isn't in the bib file, flag it. Write concise discussion — not verbose summaries.

**Text content**: Write in academic style. Every paragraph should advance the argument. If from markdown notes, distill — don't copy verbatim.

### Step 2.5: Add cross-references
- Every new figure gets `\label{fig:...}` and at least one `\ref{fig:...}` in text
- Every new table gets `\label{tab:...}` and at least one `\ref{tab:...}` in text
- Important equations get `\label{eq:...}`
- Check that new labels don't collide with existing ones

### Step 2.6: Compile and audit
1. Compile the document (see compilation protocol).
2. Check for overflow warnings in the log — fix by adjusting figure widths or table font sizes.
3. Verify all new `\ref{}` and `\cite{}` commands resolve (no "undefined reference" warnings).
4. Audit figures: do they fit within margins? Adjust `width` multiplier if needed.

### Step 2.7: Summary
Report: what was added, where it was placed, any cross-references created, any issues found.

---

## Task 3: Fix

Diagnose and fix compilation errors or broken references.

### Step 3.1: Read the error
If the user provides error output, parse it. If not:
1. Compile the document with `pdflatex -interaction=nonstopmode`
2. Read the `.log` file, search for lines starting with `! ` (errors)
3. Identify the first error

### Step 3.2: Diagnose
Do NOT do trial-and-error. Understand the root cause:

- **Changed citekeys**: Search `<REFERENCES_BIB>` for the author surname to find the current citekey. Common cause: the user updated a paper in Zotero (working paper → published), changing the citekey.

- **Undefined references**: Grep for all `\ref{X}` and `\label{X}` pairs. Find mismatches. Fix the reference or add the missing label.

- **Moved graph/table files**: Search the filesystem (cloud-storage directory, projects directories) for the filename. Update the path. Common locations:
  - `<CLOUD_STORAGE_DIR>`
  - `<PROJECTS_DIR>`

- **Stale auxiliary files**: If the error seems like corruption, clean with `latexmk -c` or remove `.aux`, `.bbl`, `.blg`, `.out`, `.toc`, `.lof`, `.lot` files and recompile.

- **Package conflicts or undefined control sequences**: Check if a package is missing from the preamble. Search the web for the specific error message if unfamiliar.

- **Bibliography errors**: Check `.blg` file for bibtex errors. Common: malformed bib entries, encoding issues in author names, duplicate keys.

- **Missing `$` errors**: Usually a `_` or `^` outside math mode. Find the line and wrap in `$...$` or escape with `\_`.

### Step 3.3: Fix
Apply the minimal fix. Do not refactor or restructure unrelated content. If obvious (wrong citekey, wrong path, wrong label), fix it directly. If uncertain, flag to the user with your diagnosis.

### Step 3.4: Compile and verify
Full compile cycle. Read the log. If errors remain, diagnose and fix the next one. Iterate: fix → compile → check → fix until 0 errors.

### Step 3.5: Escalate if stuck
If stuck after genuine investigation, flag to the user:
- What was tried
- What the error means
- What information you need

---

## Task 4: Check

Comprehensive review for publication-quality standards.

### Step 4.1: Read the full document
Read the entire `.tex` file. Understand the argument structure. If project notes exist (check working directory for `*.md` files, especially `notes.md`, `notes/README.md`), read those too for context.

### Step 4.2: Pass 1 — English and prose
- Fix typos, grammar errors, and awkward phrasing
- Ensure academic tone: precise, concise, no filler
- Check consistency: tense (past for results, present for model), capitalization in section titles, terminology used consistently throughout
- Check that every paragraph has a clear purpose and advances the argument
- Flag verbose passages that could be tightened

### Step 4.3: Pass 2 — Math
- Check all equations for correctness: matching subscripts/superscripts, correct operators, consistent notation
- Verify notation is defined before first use
- Cross-reference with project notes or model documentation if available
- Check that equation labels match their content
- Verify theorem/proposition/lemma numbering is consistent

### Step 4.4: Pass 3 — Figures, tables, and formatting
- Compile and check log for `Overfull \hbox` / `Overfull \vbox` warnings
- Verify all figures have: `\caption{}`, `\label{}`, at least one `\ref{}` in text
- Verify all tables have: `\caption{}`, `\label{}`, at least one `\ref{}` in text, notes where appropriate
- Check figure widths: do they fit within margins? Are they large enough to read?
- Check table formatting: consistent use of `booktabs`, appropriate font sizes
- Verify figure/table placement makes sense relative to the text discussing them

### Step 4.5: Pass 4 — References and cross-references
- Verify every `\cite{}` / `\citep{}` / `\citet{}` resolves (no "?" in compiled output)
- Verify every `\ref{}` resolves
- Check that the bibliography compiles correctly
- Search for common citation issues: author name variants, duplicate entries
- Verify section references (if any) point to the right sections

### Step 4.6: Pass 5 — Editorial and substance
This is the most important pass. Think like a referee at a top-5 economics journal:
- Does the introduction clearly state the research question, contribution, and key findings?
- Is the literature review comprehensive? Are key papers missing?
- Does the identification strategy have obvious holes?
- Are the results presented clearly? Do the figures/tables tell a coherent story?
- Is there analysis in the project notes that belongs in the paper but is missing?
- Are there logical gaps in the argument?
- Is the conclusion more than just a summary?
- Flag: "Your notes mention X analysis, but it's not in the paper. Consider adding it."
- Suggest structural improvements: "Consider moving X before Y for better flow."
- Identify claims that need stronger evidence or hedging

### Step 4.7: Apply and report
- Passes 1-4 are mechanical: apply fixes directly
- Pass 5 is editorial: report suggestions to the user for approval, do not apply unilaterally
- Compile and verify after all fixes
- Present a summary: what was fixed, what is suggested

---

## Compilation protocol

Use this protocol after every structural change.

```
1. Primary: latexmk -pdf -interaction=nonstopmode <file>.tex
2. If latexmk unavailable or fails unexpectedly:
   a. pdflatex -interaction=nonstopmode <file>.tex
   b. bibtex <file>
   c. pdflatex -interaction=nonstopmode <file>.tex
   d. pdflatex -interaction=nonstopmode <file>.tex
3. If stale aux files suspected:
   a. latexmk -c  (clean auxiliary files)
   b. OR: rm <file>.aux <file>.bbl <file>.blg <file>.out <file>.toc <file>.lof <file>.lot
   c. Retry from step 1
4. After compile: read <file>.log
   - Search for "! " (errors) — must be 0
   - Search for "Overfull" (warnings) — fix if they cause visible problems
5. Iterate until 0 errors
```

---

## Important rules

- **Always read the template fresh** from `<SKILLS_DIR>/latex-doc/template.tex` — never use a cached/memorized version. The user may update this template over time.
- **Never create symlinks** for the bibliography. The template already has the absolute path.
- **Never overwrite** an existing `.tex` file without confirmation.
- **Use `aer` bibliography style** (already in template).
- **Preserve all preamble content** from the template (packages, theorems, shortcuts, info boxes). Only modify the title, author, date, and document body.
- **Always use absolute paths** for graph/figure files.
- **After every structural change, compile and verify.**
- **Do not do trial-and-error when fixing errors.** Understand the problem first, then fix.
- **Use subagents** to analyze graphs, explore project structure, or check references in parallel when the task involves multiple independent sub-tasks.
- **Zotero BibTeX**: The master bibliography is at `<REFERENCES_BIB>`. Citekeys follow the Better BibTeX pattern: `authorShorttitleYear` (e.g., `cardMinimumWagesEmployment1994`). When a citekey doesn't resolve, search this file by author surname.
- **No verbose writing.** Academic prose should be precise and concise. Every sentence earns its place.
