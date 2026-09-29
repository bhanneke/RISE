---
name: respond-to-referee
description: Draft response letter text and LaTeX edits for referee points, or generate a complete reply document
---

# Respond to Referee Skill

Structured workflow for addressing referee comments. Operates in two modes:
1. **Single-point mode**: Draft a response paragraph + LaTeX edits for one referee point
2. **Full-reply mode**: Generate a complete standalone reply LaTeX document

## Examples
- `/respond-to-referee referee2.md point 3` -- address a specific point from a referee file
- `/respond-to-referee referee2.md` -- generate complete reply to all points in the file
- `/respond-to-referee identification` -- address a point by topic keyword

## Input

The user provides:
- A referee report file (markdown or text)
- Either a specific point number, a topic keyword, or no argument (full reply)

---

## Core Principles

These principles, distilled from journal editor guidelines and published advice (Noble 2017, PLOS Comp Bio; Review of Finance "Tips for Authors"), govern all referee responses.

### Tone
- **Grateful but not obsequious**: "We thank the referee for this suggestion" (good) vs. "We are deeply grateful for this invaluable insight" (too much)
- **Accept blame for misunderstandings**: If the referee misread something, it is our exposition failure. "We realize our original text was ambiguous and have revised it as follows..."
- **Never dismissive**: No bare "we respectfully disagree." Every disagreement must be backed by evidence, data, or a reference.
- **Direct answers first**: Start each response with what you did ("We have added...", "We agree and now show..."), then explain why.
- **Remember the audience**: You are writing to the *editor*, not (only) the referee.

### Structure
- **Respond to every point**: No exceptions, including minor ones.
- **Self-contained responses**: Quote or paraphrase the revised manuscript text directly in the letter.
- **Reference by section name**: Not page numbers (which shift between drafts).
- **Group related points**: When two comments address the same underlying issue, respond jointly.

### Substance
- **Do what the referee asks, even if you disagree**: Run the requested analysis, report results in the letter, then explain why you believe the main text should differ.
- **Don't over-revise**: Restrict changes to what is requested.
- **Address general criticisms globally**: If the referee cites two examples, fix the problem paper-wide.

### Common Mistakes to Avoid
| Mistake | Why it fails |
|---------|-------------|
| Bare "we respectfully disagree" | Editor has no basis to overrule |
| Sarcasm or condescension | Poisons the review relationship |
| Fixing only the specific examples cited | Signals you missed the general point |
| Long defensive paragraphs before stating what you did | Buries the lede |
| Page-number references | Numbers shift between drafts |
| Over-revising (large unrequested changes) | Creates new attack surface |
| Em-dashes (`---`) in prose | AI hallmark; see `academic-writing.md` |
| Hard-banned words (delve, crucial, etc.) | LLM tells; see `academic-writing.md` Section 1 |
| Hedge words (somewhat, quite, very, arguably) | Weaken claims; give magnitudes instead |

---

## Mode 1: Single-Point Workflow

### Step 1: Load Context
1. Read the referee report file
2. Read the project's `CLAUDE.md` for paper state and claims
3. Read `.claude/rules/academic-writing.md` for style rules
4. Identify the specific referee point

### Step 2: Map to Affected Sections
1. Identify which section(s) in the `.tex` file are affected
2. Read the affected passage(s)
3. Check if the point has already been partially addressed

### Step 3: Draft Response Letter Paragraph

```latex
\item[\textbf{Referee:}] \textit{``[abbreviated quote of referee comment]''}

\item[Reply:] [We thank the referee for... / We agree that...]
[1-2 sentences explaining what we did and where]
[If helpful: quote the revised text in a \begin{quote} block]
[1-2 sentences explaining the rationale]
```

### Step 4: Draft LaTeX Edits
1. Write proposed edits using the paper's terminology
2. Follow all rules from `academic-writing.md`
3. Show old text -> new text for each edit

### Step 5: Consistency Check
Verify proposed edits do not:
- Contradict claims in other sections
- Change quantitative results that appear elsewhere
- Introduce terminology violations
- Break cross-references

### Step 6: Output

```
REFEREE RESPONSE: Point [N] -- [topic]
======================================

REFEREE SAID:
[brief summary]

RESPONSE LETTER TEXT:
[draft LaTeX paragraph]

PROPOSED EDITS:
  File: [filename]
  Location: Section [key], ~line [N]
  OLD: [existing text]
  NEW: [proposed replacement]

CONSISTENCY NOTES:
- [any cross-section impacts]

STATUS: [Ready / Needs human review on X]
```

---

## Mode 2: Full-Reply Workflow

### Step 1: Load Context
1. Read the referee report file (all points)
2. Read the project's `CLAUDE.md` and `academic-writing.md`

### Step 2: Plan the Reply
1. Enumerate all referee points (substantive + minor)
2. Check which have already been addressed
3. Group related points
4. Flag any points where paper edits are still needed vs. reply-only

### Step 3: Create Reply Document
1. Create `_replies/reply_referee{N}.tex` using the LaTeX template below
2. Point-by-point responses with `\item[\textbf{Referee:}]` / `\item[Reply:]`
3. Opening and closing paragraphs

### Step 4: Compile and Verify
1. Run pdflatex + bibtex + pdflatex + pdflatex (paths from canonical local state reported by `tools/bootstrap.py audit`, or a repo-root compatibility shim if present)
2. Check for undefined citations or references
3. Read through for tone, completeness, accuracy

### Step 5: Output
Report the compiled PDF location, page count, and any issues.

---

## LaTeX Template (for full replies)

```latex
\documentclass[12pt,letterpaper]{article}
\usepackage[top=1.0in, bottom=1.0in, left=0.90in, right=0.90in]{geometry}
\usepackage{amsfonts,amsmath,amssymb}
\usepackage{setspace,titlesec,xcolor,booktabs,enumerate}
\usepackage{natbib}
\usepackage{hyperref}

\renewcommand{\baselinestretch}{1.10}
\titleformat{\section}{\centering\large\bfseries}{\thesection.}{1em}{}
\renewcommand{\thesection}{\Roman{section}}

\begin{document}

\noindent \textbf{{\large Reply to Referee [N] for ``{Paper Title}''}}
\medskip

\noindent Manuscript [ID]

\bigskip

\noindent [Opening paragraph: thank referee, brief overview of revision scope]

\section{Response to the Referee's comments}

\noindent
\begin{enumerate}

\item[\textbf{Referee:}] \textit{``[quoted comment]''}

\item[Reply:] [response]

% ... repeat for each point ...

\end{enumerate}

\bigskip
\noindent [Closing paragraph]

{\footnotesize
\singlespacing
\setlength{\bibsep}{6pt}
\bibliographystyle{jf}
\bibliography{../latex/references}
}

\end{document}
```
