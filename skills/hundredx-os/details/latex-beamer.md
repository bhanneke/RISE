# The Rhetoric of Decks — Beamer Presentation Generation

A framework for creating effective academic presentations with AI assistance.
Based on principles from classical rhetoric, information economics, and
decades of tacit knowledge about what makes presentations work.

---

## Part I: Philosophy — The Three Laws

### Law 1: Beauty Is Function

Beautiful slides are not decorated slides. Beauty is *clarity made visible*.
A slide is beautiful when every element earns its presence, nothing distracts,
the eye knows where to go, and the mind grasps the idea instantly.

A gradient that serves no purpose, a stock photo that illustrates nothing,
an animation that delays comprehension — these are noise, not design.
The most beautiful slide may be three words on a blank background.

### Law 2: Cognitive Load Is the Enemy

The audience has limited working memory. Every unnecessary word, extraneous
data point, or "just in case" inclusion steals bandwidth from the actual message.

- Too many points → zero points retained
- Dense text → nothing read
- Complex charts → confusion, not insight

**One idea per slide. This is the law.**

### Law 3: The Slide Serves the Spoken Word

The slide is not what you say. It is the visual anchor — a focal point for
attention, a memory hook, evidence for the claim, a structural marker.

**If your slides can be understood without you speaking, you have written
a document and called it a presentation.**

---

## Part II: The Economics of Attention (MB/MC Equivalence)

Every deck is an optimization problem. Let MB be the marginal benefit of
adding information to a slide. Let MC be the marginal cost — the cognitive
load imposed, attention demanded, risk of overwhelming the audience.

**The optimal deck satisfies:**

    MB₁/MC₁ = MB₂/MC₂ = ⋯ = MBₙ/MCₙ

When one slide is overloaded while another is sparse, you have misallocated
the audience's attention budget.

### What this means in practice

**Overloaded slides** (MB/MC too low): Text running into footer, multiple
competing ideas, charts with too many series. The audience gives up.

**Underloaded slides** (MB/MC too high): A single word that could support
a sentence. Wasted opportunity.

**The audit**: For each slide ask: "If I added one more element, would the
benefit justify the cost? If I removed one, would I lose more than I gain
in clarity?" When every slide answers "I'm at the margin," you're optimized.

**Exception: Deliberate "jump scares"** — intentional spikes in density for
rhetorical effect. A sudden striking statistic. A provocative claim. These
must be *intentional*, not accidents of poor distribution.

---

## Part III: The Aristotelian Foundation

### Ethos (Credibility)

In decks: process diagrams showing methodology, acknowledged limitations,
the "Devil's Advocate" slide. Admitting weakness builds credibility.

### Pathos (Emotion)

In decks: opening with a problem the audience recognizes, validating
frustrations, connecting data to human impact. Pathos without logos
is demagoguery.

### Logos (Logic)

In decks: data visualizations that reveal patterns, comparison tables,
before/after examples, logical flow from problem to solution. Logos
without pathos is a lecture.

### Balance by context

| Context              | Logos | Ethos | Pathos |
|----------------------|-------|-------|--------|
| Academic seminar     | 45%   | 20%   | 35%    |
| Conference talk      | 50%   | 25%   | 25%    |
| Job market talk      | 40%   | 35%   | 25%    |
| Teaching lecture      | 35%   | 25%   | 40%    |

---

## Part IV: Titles Are Assertions, Not Labels

Slide titles carry the argument. They are claims, not labels.

**Weak → Strong:**
- "Results" → "Treatment increased distance by 61 miles on average"
- "Literature Review" → "Prior work ignores the supply-side margin"
- "Methods" → "We exploit county-level variation in clinic closures"
- "Data" → "We combine three administrative datasets covering 2M workers"

**If someone reads only your slide titles in sequence, they should
understand your argument.** The titles *are* the argument. Everything
else is evidence and elaboration.

---

## Part V: Narrative Structure

### The Arc (Three Acts)

**Act I — Problem (Tension):** Establish status quo, introduce the
disruption/question, make the audience feel the problem.

**Act II — Investigation (Development):** Show what you tried, present
what you learned, build the logical case.

**Act III — Resolution (Release):** Deliver the insight, show implications,
call to action.

### The Pyramid Principle

Lead with the conclusion. Then support it. Humans want the punchline,
then they want to understand why it's true.

**Do this:** Claim → Evidence → Why it matters

**Not this:** Background → More background → Analysis → Finding (finally)

### The Opening

The first slide after the title is the most important. It must grab
attention, establish stakes, and preview the journey.

Bad: "Today I'm going to talk about..." / Agenda with 12 items / Definitions

Good: A provocative question / A surprising statistic / A concrete problem
the audience recognizes / A bold claim you'll defend

### The Closing

Bad: "Questions?" / Summary repeating everything / "Thank You"

Good: A single memorable takeaway / A concrete call to action / A question
that provokes continued thought / Return to the opening, now resolved

---

## Part VI: Bullets Are a Confession of Defeat

A list of bullets says "I couldn't figure out the relationship between
these ideas." Usually there's a structure hiding in your bullets:

- A sequence → use a numbered list or timeline diagram
- A contrast → use a two-column comparison layout
- A hierarchy → use size/color to show main point vs. supporting detail
- A causal chain → use a flow diagram with arrows

Find the structure. Make it visible. Use layout, not bullets.

---

## Part VII: The Devil's Advocate

Before presenting your argument, present its strongest critique:

- "A skeptic would say..."
- "Here's what could go wrong..."
- "The strongest objection is..."

Then: your response, your mitigation, your acknowledgment of residual risk.

This builds ethos (you've done the hard thinking), preempts objections,
and signals you're not hiding from problems.

---

## Part VIII: Visual Grammar

### Hierarchy

Not all information is equal. Design must reflect this:

- **Primary**: The one thing to remember (large, prominent, above the fold)
- **Secondary**: Supporting evidence (smaller, subordinate)
- **Tertiary**: Context and sourcing (smallest, footer area)

If everything is emphasized, nothing is emphasized.

### White Space

Empty space is rest for the eye, emphasis for content, and confidence
in your message. Crowded slides signal fear. White space signals confidence.

### Typography

- Minimum 24pt for body text (20pt absolute floor)
- Maximum two fonts (one headings, one body)
- Sans-serif for projection (serif details disappear at distance)
- Never justify text (ragged right is easier to read)

### Data Visualization

Charts are arguments, not decorations. Every chart must answer:
"what am I supposed to conclude from this?"

- One message per chart
- Remove chartjunk (3D effects, excessive gridlines, decorative elements)
- Label directly on the line (no legends requiring eye movement)
- Use color to highlight the key comparison
- State the finding in the title

If you can't explain what the chart proves in one sentence, it's too complex.

---

## Part IX: LaTeX Implementation

### Document class and aspect ratio

```latex
\documentclass[aspectratio=169, 11pt]{beamer}  % 16:9 widescreen standard
```

### Custom Color Palette

Never use default Beamer themes. Define a professional, harmonious palette
with semantic color roles:

```latex
% --- Professional Academic Palette ---
% Primary: text, headings, main structural elements
\definecolor{DeepNavy}{HTML}{2E4057}
% Structural: key terms, positive examples, itemize bullets
\definecolor{Teal}{HTML}{048A81}
% Alert/accent: emphasis, negative examples, key findings
\definecolor{WarmOrange}{HTML}{E85D04}
% Tertiary accent: occasional variety
\definecolor{SoftPurple}{HTML}{9D4EDD}
% De-emphasis: footnotes, captions, secondary text
\definecolor{WarmGray}{HTML}{6C757D}
% Background tiers
\definecolor{LightGray}{HTML}{E9ECEF}
\definecolor{Cream}{HTML}{FBF8F1}
\definecolor{SoftWhite}{HTML}{FAFAFA}
% Negative/contrast
\definecolor{DeepRed}{HTML}{D62828}

% --- Apply to Beamer elements ---
\setbeamercolor{normal text}{fg=DeepNavy, bg=SoftWhite}
\setbeamercolor{structure}{fg=DeepNavy}
\setbeamercolor{alerted text}{fg=WarmOrange}
\setbeamercolor{example text}{fg=Teal}
\setbeamercolor{frametitle}{fg=DeepNavy, bg=SoftWhite}
\setbeamercolor{title}{fg=DeepNavy}
\setbeamercolor{subtitle}{fg=WarmGray}
\setbeamercolor{block title}{bg=DeepNavy, fg=white}
\setbeamercolor{block body}{bg=LightGray, fg=DeepNavy}
\setbeamercolor{block title example}{bg=Teal, fg=white}
\setbeamercolor{block body example}{bg=LightGray, fg=DeepNavy}
\setbeamercolor{itemize item}{fg=Teal}
\setbeamercolor{itemize subitem}{fg=WarmOrange}
\setbeamercolor{enumerate item}{fg=Teal}
```

### Custom Theme Configuration

```latex
% Remove chrome
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{headline}{}

% Typography
\usefonttheme{professionalfonts}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{microtype}

% Custom frame title with generous spacing
\setbeamertemplate{frametitle}{%
    \vspace{0.5cm}
    \begin{beamercolorbox}[wd=\paperwidth, leftskip=0.8cm]{frametitle}
        \usebeamerfont{frametitle}\insertframetitle
        \ifx\insertframesubtitle\empty\else
            \\[0.1cm]
            {\usebeamerfont{framesubtitle}%
             \usebeamercolor[fg]{subtitle}\insertframesubtitle}
        \fi
    \end{beamercolorbox}
}

% Minimal footline: page number only
\setbeamertemplate{footline}{%
    \hfill
    \begin{beamercolorbox}[wd=3cm, ht=2.5ex, dp=1ex, right, rightskip=0.5cm]%
        {page number}
        \usebeamercolor[fg]{WarmGray}\scriptsize\insertframenumber
    \end{beamercolorbox}
    \vspace{0.3cm}
}

% Custom bullets: colored circles
\setbeamertemplate{itemize item}{%
    \footnotesize\raisebox{0.3ex}{\tikz\fill[Teal] (0,0) circle (0.5ex);}}
\setbeamertemplate{itemize subitem}{%
    \footnotesize\raisebox{0.3ex}{\tikz\fill[WarmOrange] (0,0) circle (0.4ex);}}
\setbeamertemplate{enumerate item}{\textcolor{Teal}{\insertenumlabel.}}

% Font sizes
\setbeamerfont{title}{size=\LARGE, series=\bfseries}
\setbeamerfont{subtitle}{size=\normalsize, series=\mdseries}
\setbeamerfont{frametitle}{size=\Large, series=\bfseries}
\setbeamerfont{framesubtitle}{size=\small, series=\mdseries}
```

### Essential Packages

```latex
\usepackage{amsmath, amssymb}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{xcolor}
\usepackage{fontawesome5}
\usepackage{ragged2e}
\usepackage{colortbl}
\usepackage{array}
\usepackage{hyperref}

\usetikzlibrary{shapes.geometric, arrows.meta, positioning, calc,
                backgrounds, decorations.pathreplacing, shadows}
\pgfplotsset{compat=1.18}
```

### Custom Commands

```latex
% Inline emphasis
\newcommand{\emphcolor}[1]{\textcolor{WarmOrange}{\textbf{#1}}}
\newcommand{\tealtext}[1]{\textcolor{Teal}{#1}}
\newcommand{\graytext}[1]{\textcolor{WarmGray}{#1}}
\newcommand{\bigidea}[1]{%
    \begin{center}\Large\color{DeepNavy}\textbf{#1}\end{center}}

% Section transition slide (full-bleed colored background)
\newcommand{\transitionslide}[2]{%
    \begin{frame}[plain]
        \begin{tikzpicture}[remember picture, overlay]
            \fill[DeepNavy] (current page.south west) rectangle
                (current page.north east);
            \node[anchor=center, text=white, font=\Huge\bfseries,
                  text width=0.8\paperwidth, align=center]
                at (current page.center) {#1};
            \node[anchor=center, text=LightGray, font=\large,
                  text width=0.8\paperwidth, align=center,
                  below=1cm of current page.center] {#2};
        \end{tikzpicture}
    \end{frame}
}

% Math operators (define these for consistency)
\DeclareMathOperator{\E}{\mathbb{E}}
\DeclareMathOperator{\Var}{Var}
\DeclareMathOperator{\Cov}{Cov}
\newcommand{\indep}{\perp\!\!\!\perp}
\newcommand{\Prob}{\mathbb{P}}
```

---

## Part X: Slide Layout Patterns

### 1. Title Slide — Full TikZ Overlay

```latex
{
\setbeamertemplate{footline}{}
\begin{frame}[plain]
\begin{tikzpicture}[remember picture, overlay]
    \fill[DeepNavy] (current page.south west) rectangle
        (current page.north east);
    % Decorative accent circles
    \fill[Teal, opacity=0.3]
        ([xshift=-2cm, yshift=-3cm]current page.north east) circle (5cm);
    \fill[WarmOrange, opacity=0.2]
        ([xshift=3cm, yshift=2cm]current page.south west) circle (4cm);
    % Title
    \node[text=white, font=\fontsize{36}{40}\selectfont\bfseries,
          text width=0.8\paperwidth, align=center]
        at ([yshift=1cm]current page.center)
        {Your Title Here};
    % Decorative rule
    \draw[WarmOrange, line width=2pt]
        ([yshift=-0.3cm]current page.center) ++(-3cm,0) -- ++(6cm,0);
    % Subtitle
    \node[text=LightGray, font=\large,
          text width=0.7\paperwidth, align=center]
        at ([yshift=-1.5cm]current page.center)
        {Author Name \\ Institution \\ Date};
\end{tikzpicture}
\end{frame}
}
```

### 2. Two-Column Comparison (Bad vs. Good)

```latex
\begin{frame}{Assertion Title Describing the Comparison}
    \begin{columns}[T]
        \begin{column}{0.47\textwidth}
            \textcolor{DeepRed}{\textbf{Traditional Approach}}
            \vspace{0.3cm}
            \begin{itemize}
                \item Problem one
                \item Problem two
            \end{itemize}
        \end{column}
        \begin{column}{0.47\textwidth}
            \textcolor{Teal}{\textbf{Our Approach}}
            \vspace{0.3cm}
            \begin{itemize}
                \item Advantage one
                \item Advantage two
            \end{itemize}
        \end{column}
    \end{columns}
\end{frame}
```

### 3. TikZ Callout Box (Key Insight)

```latex
\begin{frame}{The Central Finding}
    \vspace{0.5cm}
    \begin{center}
    \begin{tikzpicture}
        \node[draw=Teal, rounded corners=5pt, inner sep=15pt,
              fill=Teal!5, text width=0.75\textwidth, align=center]
            {\Large\color{DeepNavy}\textbf{%
             Treatment increased distance by 61 miles on average}\\[0.3cm]
             \normalsize\color{WarmGray}%
             95\% CI: [42, 80] | $p < 0.001$ | $N = 12{,}450$};
    \end{tikzpicture}
    \end{center}

    \vspace{0.5cm}
    \small
    \begin{itemize}
        \item Robust to alternative specifications
        \item Effect concentrated among first-time users
    \end{itemize}
\end{frame}
```

### 4. Three-Pillar Framework

```latex
\begin{frame}{The Three Modes of Persuasion}
    \vspace{0.5cm}
    \begin{tikzpicture}[
        box/.style={rounded corners=3pt, minimum width=3.5cm,
                     minimum height=2.5cm, text width=3cm,
                     align=center, font=\small}
    ]
        \node[box, fill=Teal!15, draw=Teal]
            (ethos) at (0,0)
            {\textbf{\large Ethos}\\[4pt]Credibility\\Process \& rigor};
        \node[box, fill=WarmOrange!15, draw=WarmOrange]
            (pathos) at (4.5,0)
            {\textbf{\large Pathos}\\[4pt]Emotion\\Why it matters};
        \node[box, fill=SoftPurple!15, draw=SoftPurple]
            (logos) at (9,0)
            {\textbf{\large Logos}\\[4pt]Logic\\Evidence \& data};
    \end{tikzpicture}
\end{frame}
```

### 5. Figure Slide

```latex
\begin{frame}{Treatment Increased Distance by 61 Miles}
\framesubtitle{Event-study estimates with 95\% confidence intervals}
    \begin{figure}
        \centering
        \includegraphics[width=0.78\textwidth,
                         height=0.72\textheight,
                         keepaspectratio]{figures/event_study.pdf}
    \end{figure}
    \vspace{-0.5em}
    \graytext{\scriptsize Base period: $t = -1$. Standard errors
    clustered at the county level.}
\end{frame>
```

### 6. Final Slide (Mirrors Title)

```latex
\begin{frame}[plain]
\begin{tikzpicture}[remember picture, overlay]
    \fill[DeepNavy] (current page.south west) rectangle
        (current page.north east);
    \fill[Teal, opacity=0.2]
        ([xshift=-2cm, yshift=-3cm]current page.north east) circle (5cm);
    \node[text=white, font=\Large, text width=0.7\paperwidth,
          align=center] at ([yshift=1cm]current page.center)
        {Your one-sentence takeaway goes here};
    \draw[WarmOrange, line width=2pt]
        ([yshift=-0.3cm]current page.center) ++(-3cm,0) -- ++(6cm,0);
    \node[text=LightGray, font=\large,
          text width=0.7\paperwidth, align=center]
        at ([yshift=-1.5cm]current page.center)
        {author@institution.edu};
\end{tikzpicture}
\end{frame}
```

---

## Part XI: Figure Generation (R / ggplot2)

When generating figures, the R script should use a custom theme that
matches the LaTeX palette exactly:

```r
# Color palette matching LaTeX
palette <- c(
  primary   = "#2E4057",  # DeepNavy
  secondary = "#048A81",  # Teal
  accent    = "#E85D04",  # WarmOrange
  highlight = "#9D4EDD",  # SoftPurple
  neutral   = "#6C757D",  # WarmGray
  negative  = "#D62828"   # DeepRed
)

theme_rhetoric <- function(base_size = 14) {
  theme_minimal(base_size = base_size) +
    theme(
      text = element_text(color = "#2E4057"),
      plot.title = element_text(size = rel(1.3), face = "bold",
                                hjust = 0, margin = margin(b = 15)),
      plot.subtitle = element_text(size = rel(1.0), color = "#6C757D",
                                   hjust = 0, margin = margin(b = 20)),
      axis.title = element_text(size = rel(0.95), face = "bold"),
      axis.text = element_text(size = rel(0.9), color = "#2E4057"),
      panel.grid.major = element_line(color = "#E9ECEF", linewidth = 0.4),
      panel.grid.minor = element_blank(),
      legend.position = "bottom",
      plot.background = element_rect(fill = "white", color = NA),
      panel.background = element_rect(fill = "white", color = NA)
    )
}
```

### Figure design rules

- Output both PDF (vector) and PNG (300 DPI) for every figure
- Dimensions: 10 × 6.5 inches for standard, 8 × 5 for smaller
- **Direct labeling**: annotate lines directly instead of using legends
- **Titles state findings**: "Q4 Performance: 28% Growth" not "Quarterly Data"
- Shaded annotation rectangles for period highlights
- Confidence interval ribbons with 20% opacity fill
- Reference lines (dashed) for baselines or treatment dates

---

## Part XII: Tables in Presentations

Tables must be dramatically simpler than in papers.

- Show 2–4 columns maximum (move rest to appendix)
- Use `\small` minimum font size
- Round aggressively (two significant digits)
- Bold or color the key coefficient: `\textbf{\textcolor{Teal}{0.123**}}`
- Use `booktabs` rules only (`\toprule`, `\midrule`, `\bottomrule`)
- No vertical rules ever

---

## Part XIII: Overlays and Animation

Use sparingly. Overlays are for building complex arguments, not decoration.

**When to use:** Building a diagram step by step, argument where order
matters, revealing results after showing empirical strategy.

**When NOT to use:** Every bullet point, tables, figures.

---

## Part XIV: Appendix / Backup Slides

```latex
\appendix
\newcounter{finalframe}
\setcounter{finalframe}{\value{framenumber}}
\setcounter{framenumber}{\value{finalframe}}
```

Link from main slides: `\hyperlink{robustness}{\beamergotobutton{Details}}`

Back-link from appendix: `\hyperlink{main-results}{\beamerreturnbutton{Back}}`

---

## Part XV: Timing and Length

| Context                | Slides | Notes |
|------------------------|--------|-------|
| Seminar (75–90 min)    | 35–50  | Plan for extensive Q&A throughout |
| Conference (15–20 min) | 15–20  | Cut aggressively. Identification + results only |
| Job market (90 min)    | 40–50  | Your most important talk. Backup for every question |
| Teaching lecture        | 50–80  | Repetition allowed. Show reasoning, not just conclusions |

General rule: 2–3 minutes per substantive slide. Title, outline, and
divider slides take less time.

---

## Part XVI: TikZ Diagram Rules (Non-Negotiable)

### Box uniformity

All boxes in the same diagram MUST have identical dimensions. Use `text width`
(hard-fixed) to control box size — NEVER `minimum width` (which grows with
content and breaks uniformity). Define a single style and apply it to every node:

```latex
box/.style={draw, rounded corners=3pt,
            text width=3cm, minimum height=1.2cm,
            align=center, font=\small}
```

### Arrow routing

Arrows must NEVER pass through boxes. Never use TikZ shorthand like `|-` or
`-|` for routing — these go vertical-first or horizontal-first and will cross
boxes in complex layouts. Always use explicit coordinate paths routed far
enough outside all nodes to guarantee clearance:

```latex
% BAD — may cross intermediate nodes:
\draw[->] (A) |- (C);

% GOOD — explicit routing with clearance:
\draw[->] (A.east) --++(1,0) --++(0,-2) -- (C.west);
```

### Text fitting

All text MUST fit on one line within its box. If it doesn't, shorten the text
— do NOT resize the box. Uniform box size trumps showing every word. Verify
after compilation that no text overflows.

### Respect existing layouts

Don't "clean up" a chaotic or organic layout into a grid unless explicitly
asked. The original visual aesthetic and spatial relationships are intentional.
When editing existing TikZ diagrams, preserve the overall structure and only
modify the specific elements requested.

### Visual verification

After every TikZ edit, compile and visually verify:
- Arrows actually connect to the intended nodes
- Boxes actually align as intended
- Text actually fits within all boxes
- No arrows pass through or behind any box

Never describe a fix as done if the geometry doesn't work in the compiled PDF.

---

## Part XVII: Content Accuracy Rules

1. **Don't invent future plans.** If something already exists (e.g., a large
   literature catalog, running datasets, operational infrastructure), present
   it as what it is — don't frame it as a future goal or aspiration.

2. **Verify facts against what's operational.** When presenting system
   capabilities, datasets, or infrastructure, check the actual state rather
   than guessing or embellishing.

3. **Implement feedback fully in one pass.** Don't partially address feedback
   items — every piece of feedback must be resolved before presenting the next
   version. Half-fixes waste review cycles.

---

## Part XVIII: The Iterative Multi-Pass Workflow

### Step 1: Build deck with MB/MC equivalence

Create the full deck. Check that cognitive load is balanced across all slides.
No slide should be overloaded while another is sparse.

### Step 2: Fix ALL compilation warnings

Check and eliminate every overfull/underfull hbox and vbox. No matter how
small. These indicate LaTeX making compromises you did not authorize.

### Step 3: Check silent visual errors

LaTeX warnings catch box overflow but NOT coordinate/positioning problems
in TikZ, ggplot2, or matplotlib. These compile silently but look wrong:

**TikZ silent errors:**
- Labels not where intended (coordinates miscalculated)
- Timeline endpoints misaligned
- Arrows pointing to wrong nodes
- Shape constraints forcing misplacement

**Figure silent errors:**
- Axis labels cut off at boundary
- Legends obscuring data
- Text sizing inconsistent across panels

### Step 4: Recompile and verify

After fixing, recompile and check flow, MB/MC balance, and label positioning.

### Step 5: Repeat until all tests pass

```
while (not all_tests_pass):
    fix_issues()
    recompile()
    check_flow_and_equivalence()
    check_label_positioning()
```

---

## Part XIX: Common Failures

1. **Text walls**: slides that could be printed as paragraphs → extract key phrase
2. **Burying the lede**: key point on slide 15 → state conclusion on slide 2
3. **Chartjunk**: 3D bars with gradients → remove until removing more removes meaning
4. **Label titles**: "Results" → assertion stating the finding
5. **"Questions?" ending**: → end with key takeaway or call to action
6. **Anxiety overload**: dense slides as security blanket → sparse slides force authority
7. **Default themes**: generic Beamer templates → custom palette with semantic color roles
8. **Bullet-only slides**: → find the structure, use TikZ diagrams or layouts
9. **No backup slides**: → have appendix slide for every anticipated question
10. **Figures without finding in title**: → title states what the chart proves
