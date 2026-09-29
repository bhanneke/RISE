---
name: build-deck
description: Create and compile Beamer presentations following the Rhetoric of Decks philosophy. Use when making seminar or conference slides.
---

# Build Deck: Beamer Presentations with the Rhetoric of Decks

Create, edit, and compile academic presentations for seminars, conferences, and working sessions.

## Examples
- `/build-deck` -- start a new deck (asks audience/tone questions first)
- `/build-deck decks/seminar.tex` -- compile an existing deck
- `/build-deck --working` -- create a working deck for coauthors (denser, more detail)

## Step 1: Ask Two Questions

Before creating or significantly editing a deck, ask:

> **Question 1: Who is the audience?**
> 1. **External** -- Seminar, conference, discussant role (sparse, performative, one idea per slide)
> 2. **Working** -- Coauthors, internal meeting (detailed, documentary, preserves uncertainty)

> **Question 2: What's the visual tone?**
> 1. **Professional/Academic** -- Use the house palette (navy/crimson/forest)
> 2. **Colorful/Expressive** -- Design something unique for this specific deck

These determine density and visual style. If the user specifies `--working`, skip Question 1 (answer is Working).

## Step 2: Read the Philosophy

Before building, internalize the rules from `.claude/rules/presentation-rules.md`. The key principles:

1. **One idea per slide** -- non-negotiable for external decks
2. **Titles are assertions** -- "Transaction costs halve momentum alpha" not "Results"
3. **MB/MC equivalence** -- equalize cognitive load across all slides
4. **The slide serves the spoken word** -- if slides work without a speaker, you made a document

## Step 3: Build the Deck

### For New Decks

Create the `.tex` file in the project's `decks/` directory (create if needed):
```
decks/
+-- seminar.tex             # Main Beamer file
+-- seminar.pdf             # Compiled output
```

### Beamer Preamble (Professional Style)

```latex
\documentclass[aspectratio=169,11pt]{beamer}
\usetheme{default}
\usecolortheme{default}

% --- Strip navigation chrome ---
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}{%
  \hfill\insertframenumber/\inserttotalframenumber\hspace*{4pt}\vspace{2pt}%
}

% --- House palette ---
\definecolor{navy}{HTML}{1A365D}
\definecolor{darkgray}{HTML}{2D3748}
\definecolor{crimson}{HTML}{9B2335}
\definecolor{forest}{HTML}{276749}
\definecolor{steel}{HTML}{4A5568}
\definecolor{lightgray}{HTML}{F7FAFC}
\definecolor{warmgray}{HTML}{E2E8F0}

% --- Beamer colors ---
\setbeamercolor{frametitle}{fg=navy,bg=white}
\setbeamercolor{title}{fg=navy}
\setbeamercolor{subtitle}{fg=steel}
\setbeamercolor{author}{fg=darkgray}
\setbeamercolor{date}{fg=steel}
\setbeamercolor{normal text}{fg=darkgray}
\setbeamercolor{itemize item}{fg=steel}
\setbeamercolor{itemize subitem}{fg=steel!60}
\setbeamercolor{alerted text}{fg=crimson}
\setbeamercolor{block title}{fg=white,bg=navy}
\setbeamercolor{block body}{fg=darkgray,bg=lightgray}

% --- Fonts ---
\setbeamerfont{frametitle}{series=\bfseries,size=\large}
\setbeamerfont{title}{series=\bfseries,size=\Large}

% --- Custom commands ---
\newcommand{\emphnum}[1]{\textcolor{crimson}{\textbf{#1}}}
\newcommand{\goodnum}[1]{\textcolor{forest}{\textbf{#1}}}
\newcommand{\transitionslide}[1]{%
  {\setbeamercolor{background canvas}{bg=navy}
   \begin{frame}[plain]
   \centering\vfill
   {\color{white}\LARGE\bfseries #1}
   \vfill
   \end{frame}}
}
\newcommand{\takeaway}[1]{%
  \begin{center}
  \colorbox{warmgray}{\parbox{0.88\textwidth}{\centering\vspace{4pt}%
    \color{navy}\bfseries #1\vspace{4pt}}}
  \end{center}
}

% --- Packages ---
\usepackage{booktabs}
\usepackage{tikz}
\usepackage{graphicx}
\usepackage{amsmath,amssymb}
```

### Color Usage Convention

| Color | Purpose | Command |
|-------|---------|---------|
| `crimson` | Emphasis, alerts, pre-cost/gross values | `\emphnum{0.82\%}` |
| `forest` | Positive outcomes, post-cost/net values | `\goodnum{0.33\%}` |
| `navy` | Headers, section transitions, primary branding | -- |
| `steel` | Secondary text, captions | -- |
| `darkgray` | Body text | -- |
| `warmgray` | Takeaway box background | `\takeaway{...}` |

### Slide Patterns

**Results slide with assertion title:**
```latex
\begin{frame}{Transaction costs halve momentum alpha}
\centering
\begin{tabular}{lccc}
\toprule
 & Gross & Net & Cost (\%) \\
\midrule
UMD & \emphnum{0.65\%} & \goodnum{0.31\%} & 52\% \\
\bottomrule
\end{tabular}

\vspace{1em}
\small The assertion is in the title. The table is evidence.
\end{frame}
```

**Transition slide:**
```latex
\transitionslide{Main Results}
```

## Step 4: The Compile Loop

**ZERO TOLERANCE FOR WARNINGS.**

Use the pdflatex path from canonical local state reported by `tools/bootstrap.py audit` (or a repo-root `CLAUDE.local.md` compatibility shim if present):
```bash
cd {decks_dir} && pdflatex -interaction=nonstopmode {file}.tex
```

### Compile checklist:
1. **Compile** -- `pdflatex -interaction=nonstopmode`
2. **Check errors** -- lines starting with `!` (fatal)
3. **Fix ALL warnings** -- overfull/underfull hbox/vbox, even 0.5pt
4. **Check figures/tables** -- labels positioned correctly? Text cut off?
5. **Recompile** until zero warnings

Do not consider the deck finished until compile is completely clean.

## Step 5: Self-Review

After clean compile, review the deck against these criteria:

- [ ] Can someone in the back row read every slide?
- [ ] Does every slide advance the argument?
- [ ] Is there only ONE idea per slide (external decks)?
- [ ] Do titles carry the argument when read in sequence?
- [ ] Is MB/MC equalized -- no overloaded or underloaded slides?
- [ ] Have you included a devil's advocate slide?
- [ ] Does the opening grab attention in 60 seconds?
- [ ] Does the closing give ONE memorable takeaway (not "Questions?")?
- [ ] Are colors used consistently (crimson = emphasis, forest = positive)?

## Output

```
DECK BUILD REPORT
=================

File: {decks_dir}/{name}.tex
Status: SUCCESS / FAILED
Slides: N
Warnings: 0 (must be zero)
Errors: 0

Output: {decks_dir}/{name}.pdf
```

## Narrative Templates

> **Project-specific narrative arcs belong in each project's `CLAUDE.md`.** Below are generic templates.

### 45-Minute Seminar (~30 slides)
1. Title
2. Hook: one surprising concrete fact
3. Roadmap (3 items max)
4-5. Motivation: why this question matters
6-7. Data: scope, source, sample period
8-10. Methodology: identification strategy
11. Transition
12-17. Main results with assertion titles
18. Transition
19-22. Mechanism / decomposition
23-25. Robustness (one summary slide preferred)
26. Devil's advocate
27. The one takeaway
28-30. Backup slides

### 20-Minute Conference (~18 slides)
1. Title
2. Hook + key number
3. Framework overview
4-5. Data
6-8. Methodology
9-13. Main results
14. Robustness summary
15. The one takeaway
16-18. Backup
