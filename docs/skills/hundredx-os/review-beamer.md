<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/review-beamer.md -->

# `beamer`

*Pack: [100xOS shared skills](../hundredx-os.md) · category `review` · field `economics`*

---

# Beamer Presentation Review Checklist

Multi-pass review checklist for academic Beamer presentations.
Covers rhetoric quality, visual quality, and LaTeX correctness.

---

## Pass 1: Rhetoric Review (The "Referee 2" Pass)

### Narrative Structure

- [ ] The deck tells a three-act story: Problem (tension) → Investigation (development) → Resolution (release)
- [ ] The opening slide (after title) grabs attention — not "Today I will talk about..." or a 12-item agenda
- [ ] The closing slide is a single memorable takeaway or call to action — not "Questions?" or "Thank You"
- [ ] The Pyramid Principle is followed: conclusions first, then evidence. Not: background → background → finding
- [ ] A "Devil's Advocate" slide addresses the strongest objection before the audience raises it

### MB/MC Equivalence

- [ ] Cognitive load is balanced across all slides — no slide is overloaded while another is sparse
- [ ] Each slide has approximately the same marginal benefit-to-cost ratio
- [ ] Any deliberate "jump scares" (density spikes) are clearly intentional rhetorical effects
- [ ] The deck "breathes" — dense technical slides are followed by lighter rest slides
- [ ] **One idea per slide.** Any slide with multiple competing ideas must be split

### Titles

- [ ] Every slide title is an assertion, not a label. "Treatment increased X by Y" not "Results"
- [ ] Reading only the slide titles in sequence conveys the complete argument
- [ ] No generic titles: "Motivation", "Data", "Methods", "Conclusion" are all banned
- [ ] Title text fits on one line (two max) — trim if needed

### Content Quality

- [ ] Bullet points are used only when items are genuinely parallel and equal-weight
- [ ] Where structure exists (sequence, contrast, hierarchy, causal chain), it is made visible through layout, not bullets
- [ ] Text is minimal — keywords and short phrases, not full sentences
- [ ] Every claim has evidence (data, citation, figure). No unsupported assertions
- [ ] Equations appear one per slide with surrounding context explaining each term

### Audience Fit

- [ ] Ethos/Pathos/Logos balance is appropriate for the audience (seminar vs. conference vs. job market)
- [ ] Technical depth matches the audience — not too deep for a broad audience, not too shallow for specialists
- [ ] Jargon is appropriate for the target audience
- [ ] Backup slides cover anticipated questions

---

## Pass 2: Visual Quality (The "Graphics Specialist" Pass)

### Color and Typography

- [ ] A custom color palette is defined with semantic roles (not default Beamer theme)
- [ ] Colors are used consistently: structural color for key terms, alert color for emphasis, gray for de-emphasis
- [ ] Minimum 24pt body text (20pt absolute floor)
- [ ] Maximum two font families used
- [ ] White space is generous — content fills 60–80% of the slide, not 100%

### Visual Hierarchy

- [ ] Each slide has clear primary/secondary/tertiary information hierarchy
- [ ] Primary information is large and prominent (above the fold)
- [ ] Supporting evidence is smaller and subordinate
- [ ] Context and sourcing is smallest (footer/caption area)
- [ ] If everything on a slide is the same size, something is wrong

### Figures

- [ ] Every figure title states the finding: "X increased Y by Z%" not "Chart of X"
- [ ] Figures use PDF (vector) format when possible, PNG at 300 DPI as fallback
- [ ] No chartjunk: no 3D effects, excessive gridlines, or decorative elements
- [ ] Labels are placed directly on lines/bars (no separate legends requiring eye movement)
- [ ] Axis labels include units: "Wage (2019 USD)" not just "Wage"
- [ ] Font sizes in figures are readable when projected (consistent with slide text)
- [ ] Color palette in figures matches the LaTeX deck palette exactly
- [ ] Confidence intervals or bands are shown where appropriate

### Tables

- [ ] 2–4 columns maximum (rest in appendix)
- [ ] Font size is `\small` or larger — readable from back row
- [ ] Key coefficient is highlighted (bold, color, or both)
- [ ] Numbers are rounded aggressively (two significant digits)
- [ ] Only `booktabs` horizontal rules (`\toprule`, `\midrule`, `\bottomrule`) — no vertical rules

### TikZ and Diagrams

- [ ] **Box uniformity**: All boxes in the same diagram have identical dimensions — no exceptions
- [ ] Boxes use `text width` (hard-fixed), NEVER `minimum width` (which grows with content)
- [ ] **Arrow routing**: No arrows pass through boxes. No TikZ shorthand (`|-`, `-|`) — use explicit coordinate paths (`--++(dx,0)--++(0,dy)--`) routed outside all nodes
- [ ] **Text fitting**: All text fits on one line within its box. If not, text is shortened — box is NOT resized
- [ ] TikZ node positions correspond to their intended visual appearance
- [ ] Coordinate values are verified (not just syntactically correct but visually correct)
- [ ] Timeline endpoints align with content
- [ ] Arrows point to the correct nodes
- [ ] Transition slides use full-bleed backgrounds (not just centered text on white)
- [ ] Flow diagrams are readable left-to-right or top-to-bottom
- [ ] Original layout aesthetic is preserved — don't "clean up" into a grid unless asked
- [ ] **Visually verified after compilation**: arrows connect, boxes align, text fits, no overlaps

---

## Pass 3: Content Accuracy (The "Fact-Check" Pass)

- [ ] No future plans invented for things that already exist (e.g., don't say "we plan to build X" if X is operational)
- [ ] All stated facts (dataset sizes, system capabilities, infrastructure) are verified against actual state
- [ ] ALL feedback items from previous rounds are fully addressed — no partial fixes
- [ ] Every fix described as "done" has been visually verified in the compiled PDF

---

## Pass 4: LaTeX Correctness (The "Compilation" Pass)

### Zero-Warning Policy

- [ ] No overfull `\hbox` warnings (content too wide — pushes text into margins)
- [ ] No underfull `\hbox` warnings (content too sparse — stretches whitespace awkwardly)
- [ ] No overfull `\vbox` warnings (content overflows page bottom)
- [ ] No underfull `\vbox` warnings (awkward vertical gaps)
- [ ] **All warnings, no matter how small, must be fixed**

### Structural Correctness

- [ ] All `\begin{...}` environments have matching `\end{...}`
- [ ] All braces `{ }` are balanced
- [ ] No empty `\ref{}` or `\cite{}` commands
- [ ] No `??` undefined references in compiled output
- [ ] Frame numbers display correctly
- [ ] Appendix frame counter is properly reset

### Package and Command Hygiene

- [ ] No deprecated packages (e.g., `subfig` → use `subcaption`)
- [ ] `\usepackage{hyperref}` is loaded last
- [ ] Custom math operators use `\DeclareMathOperator` not ad hoc formatting
- [ ] Navigation symbols are removed (`\setbeamertemplate{navigation symbols}{}`)
- [ ] `aspectratio=169` is set for 16:9 widescreen

---

## Scoring

Rate each pass independently on a scale of 1–10:

- **Rhetoric score**: Narrative structure, MB/MC balance, assertion titles, audience fit
- **Visual score**: Color palette, hierarchy, figure quality, TikZ correctness
- **Accuracy score**: Facts verified, feedback fully addressed, no invented plans
- **LaTeX score**: Zero warnings, structural correctness, package hygiene

**Overall score** = min(rhetoric, visual, accuracy, latex)

The weakest pass determines the overall score. A deck with perfect rhetoric
but broken LaTeX is not presentable, and vice versa.

**Pass threshold**: Overall score ≥ 9

---

## Review Output Format

```
RHETORIC_SCORE: [1-10]
VISUAL_SCORE: [1-10]
ACCURACY_SCORE: [1-10]
LATEX_SCORE: [1-10]
OVERALL_SCORE: [1-10]
PASSED: [YES/NO] (YES if overall score >= 9)
ISSUES:
- [RHETORIC] issue description -> suggestion
- [VISUAL] issue description -> suggestion
- [ACCURACY] issue description -> suggestion
- [LATEX] issue description -> suggestion
SUMMARY: [2-3 sentence assessment covering all four passes]
```
