<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/review-latex.md -->

# `latex`

*Pack: [100xOS shared skills](../hundredx-os.md) · category `review` · field `economics`*

---

# LaTeX Review Checklist for Economics Papers

## Purpose

LaTeX is the standard typesetting system for economics papers. A well-formatted manuscript signals professionalism and reduces friction for referees. Formatting errors -- inconsistent notation, broken cross-references, misaligned tables -- distract from the content and can give a negative impression before the referee reads a single sentence of substance.

This checklist covers the most common LaTeX issues in economics manuscripts.

---

## 1. Mathematical Notation

Inconsistent notation is one of the most frequent problems in economics manuscripts. Referees notice.

**Check these items:**

- [ ] Every variable is defined the first time it appears in an equation, and the definition is consistent throughout the paper.
- [ ] Scalars, vectors, and matrices have visually distinct formatting. Common convention: lowercase italic for scalars ($x$), bold lowercase for vectors ($\mathbf{x}$), bold uppercase for matrices ($\mathbf{X}$).
- [ ] Subscripts and superscripts are used consistently: $Y_{it}$ vs $Y_{i,t}$ -- pick one and stick with it.
- [ ] Operators use `\operatorname{}` or predefined commands: `\log`, `\exp`, `\max`, `\Pr`, `\E` (defined as `\DeclareMathOperator{\E}{\mathbb{E}}`). Do not write `log` in italics as if it were a variable.
- [ ] Greek letters are used consistently: if $\beta$ is the treatment effect in Section 3, it should not suddenly become the discount factor in Section 4.
- [ ] Equation numbering is consistent: number all equations, or number only those referenced in the text. Do not number some arbitrarily.
- [ ] Multi-line equations use `align` or `aligned`, not `eqnarray` (which has known spacing issues).
- [ ] Parentheses and brackets scale correctly: use `\left(` and `\right)` or `\big`, `\Big`, etc. for expressions that extend vertically.
- [ ] Error terms ($\varepsilon$ vs $\epsilon$) are consistent. The economics convention is typically $\varepsilon_{it}$.
- [ ] Expectations, variances, and covariances use consistent notation: $\mathbb{E}[\cdot]$, $\text{Var}(\cdot)$, $\text{Cov}(\cdot, \cdot)$.

### Recommended practice: define custom commands

Define notation at the top of your document to ensure consistency and make global changes easy:

```latex
\newcommand{\E}{\mathbb{E}}
\newcommand{\Var}{\operatorname{Var}}
\newcommand{\Cov}{\operatorname{Cov}}
\newcommand{\indep}{\perp\!\!\!\perp}
\newcommand{\plim}{\operatorname{plim}}
```

---

## 2. Document Structure and Environments

**Check these items:**

- [ ] Sections are numbered and follow a logical hierarchy: `\section`, `\subsection`, `\subsubsection`. Do not skip levels (e.g., `\section` directly to `\subsubsection`).
- [ ] Theorems, propositions, lemmas, and assumptions use `\newtheorem` environments, not ad hoc formatting.
- [ ] Proofs use the `proof` environment (from `amsthm`), which adds the QED symbol automatically.
- [ ] The appendix uses `\appendix` command, which switches section numbering to A, B, C automatically.
- [ ] Online appendix (if separate) is clearly labeled and has its own self-contained references section.
- [ ] Title page includes: title, author(s), affiliation(s), date, abstract, JEL codes, keywords, and acknowledgments (often as a footnote on the title).
- [ ] Double-spacing is applied for submission (use `\usepackage{setspace}` and `\doublespacing`), but check journal requirements.

---

## 3. Tables

Tables are the primary vehicle for results in empirical economics. They must be readable, well-labeled, and self-contained.

**Check these items:**

- [ ] Every table has a descriptive title (caption) that allows the reader to understand it without reading the text.
- [ ] Table notes (below the table) explain variable definitions, sample restrictions, standard error clustering, and significance levels.
- [ ] Standard errors are in parentheses below coefficients. Do not use square brackets for standard errors (brackets are conventionally reserved for other statistics, e.g., t-statistics or confidence intervals).
- [ ] Significance stars are defined consistently: `* p < 0.10, ** p < 0.05, *** p < 0.01`. Use the same thresholds throughout the paper. Consider omitting stars entirely and reporting confidence intervals instead.
- [ ] Alignment: decimal-align numbers using the `siunitx` package (`S` column type) or `dcolumn`. Misaligned decimals make tables hard to scan.
- [ ] Number of observations (N) and R-squared are reported for each column.
- [ ] Column headers clearly identify the dependent variable and the specification.
- [ ] Horizontal rules use `\toprule`, `\midrule`, and `\bottomrule` from the `booktabs` package. Never use vertical rules in economics tables.
- [ ] Tables do not overflow the page margins. Use `\resizebox` or `\adjustbox` sparingly -- if you need to shrink a table significantly, it has too many columns.
- [ ] Table placement uses `[t]` or `[htbp]` -- never `[H]` (from the `float` package), which forces exact placement and creates bad page breaks.
- [ ] Regression tables produced by software (Stata's `esttab`, R's `stargazer`, Python's `statsmodels`) are manually reviewed for formatting consistency with the rest of the paper.

### Recommended table structure

```latex
\begin{table}[t]
\centering
\caption{Effect of Policy on Wages}
\label{tab:main_results}
\begin{tabular}{lccc}
\toprule
                        & (1)       & (2)       & (3) \\
                        & OLS       & IV        & IV \\
\midrule
Treatment               & 0.034***  & 0.052**   & 0.048** \\
                        & (0.008)   & (0.022)   & (0.020) \\
Controls                & No        & No        & Yes \\
Fixed effects           & Year      & Year      & Year + Firm \\
\midrule
Observations            & 125,430   & 125,430   & 125,430 \\
R-squared               & 0.142     & ---       & --- \\
First-stage F           & ---       & 42.3      & 38.7 \\
\bottomrule
\end{tabular}
\begin{tablenotes}
\small
\item \textit{Notes:} Standard errors clustered at the firm level in
parentheses. The dependent variable is log hourly wage. The instrument
is the municipality-level lockdown severity index. * $p<0.10$,
** $p<0.05$, *** $p<0.01$.
\end{tablenotes}
\end{table}
```

---

## 4. Figures

**Check these items:**

- [ ] Figures are vector format (PDF) when possible, not raster (PNG, JPG). This ensures they look sharp at any resolution.
- [ ] Axes are labeled with units: "Wage (2019 USD)" not just "Wage."
- [ ] Font size in figures is readable at the printed size. A common mistake is generating figures with tiny axis labels.
- [ ] Legends do not obscure data. Place legends outside the plot area or use direct labeling of lines.
- [ ] Color is used meaningfully and the figure is interpretable in grayscale (many referees print in black and white). Use different line styles (solid, dashed, dotted) in addition to colors.
- [ ] Confidence intervals or bands are shown where appropriate (e.g., event-study plots).
- [ ] The caption is informative: "Figure 3: Event-study estimates of the effect of policy reform on firm-level employment. Bars indicate 95% confidence intervals. The dashed vertical line marks the reform date."
- [ ] Figure numbering is sequential and matches references in the text.
- [ ] Subfigures use the `subcaption` package and are labeled (a), (b), etc.

---

## 5. Cross-References

**Check these items:**

- [ ] All cross-references use `\ref{}`, `\eqref{}`, or `\autoref{}` -- never hardcoded numbers. Hardcoded references break when you reorder sections.
- [ ] Every `\label{}` has at least one corresponding `\ref{}`. Unused labels are clutter.
- [ ] Labels follow a consistent naming convention: `tab:summary_stats`, `fig:event_study`, `eq:main_spec`, `sec:identification`.
- [ ] No "??" appears in the compiled document (a sign of undefined references). Compile twice to resolve forward references.
- [ ] Table and figure references in the text capitalize appropriately: "Table 1" and "Figure 3" (capitalized when used as proper nouns), not "table 1."
- [ ] Equation references use `\eqref{}` which adds parentheses automatically: "as shown in equation (3)" rather than "as shown in equation 3."

---

## 6. Bibliography

**Check these items:**

- [ ] All citations compile without errors. No "?" in the text from undefined citation keys.
- [ ] Every entry in the `.bib` file that is cited appears in the bibliography. Every entry in the bibliography is cited in the text (no phantom references).
- [ ] Author names are consistent: if the `.bib` file has "De Chaisemartin" in one entry and "de Chaisemartin" in another, they will appear as different authors.
- [ ] Journal names are abbreviated consistently (or not abbreviated consistently). Do not mix "American Economic Review" and "Am. Econ. Rev."
- [ ] Working papers include the series name and number: "NBER Working Paper No. 28543."
- [ ] Published papers include volume, issue, and page numbers.
- [ ] DOIs or URLs are included for online-only publications.
- [ ] The bibliography style matches the target journal. Most economics journals use author-year citation (`natbib` with `\citet` and `\citep`).
- [ ] In-text citations use the correct form:
  - Parenthetical: `\citep{author2020}` produces "(Author, 2020)"
  - Textual: `\citet{author2020}` produces "Author (2020)"
  - Do not write "Author (2020)" manually -- use `\citet`.
- [ ] Multiple citations are grouped: `\citep{author2020, otherauthor2021}` not `\citep{author2020}; \citep{otherauthor2021}`.

---

## 7. Typography and Formatting

**Check these items:**

- [ ] Hyphens (-), en-dashes (--), and em-dashes (---) are used correctly. En-dashes for ranges: "pages 15--32," "2010--2020." Em-dashes for parenthetical statements.
- [ ] Quotation marks use LaTeX convention: `` `single' `` and ``` ``double'' ```, not straight quotes.
- [ ] Percent signs use `\%` in text and are consistent: "10 percent" or "10\%" throughout, not a mix.
- [ ] Thousands separators are used for large numbers: "125,430" not "125430."
- [ ] Non-breaking spaces (`~`) are used before references: `Table~\ref{tab:main}`, `Section~\ref{sec:data}`.
- [ ] Acronyms are defined on first use: "randomized controlled trial (RCT)" then "RCT" thereafter.
- [ ] The paper compiles without warnings (not just without errors). Overfull hbox warnings indicate text running into margins.

---

## 8. Common Package Recommendations

| Purpose | Package | Notes |
|---------|---------|-------|
| Table formatting | `booktabs` | `\toprule`, `\midrule`, `\bottomrule` |
| Number alignment | `siunitx` | `S` column type for decimal alignment |
| Citations | `natbib` | `\citet`, `\citep` for author-year |
| Subfigures | `subcaption` | Replaces deprecated `subfig` |
| Hyperlinks | `hyperref` | Load last; makes refs clickable |
| Colors | `xcolor` | For figure-matching colors in text |
| Spacing | `setspace` | `\doublespacing` for submission |
| Margins | `geometry` | Standard: 1-inch margins |
| Code listings | `listings` or `minted` | For appendix code display |

---

## Pre-Submission Checklist

- [ ] Compile from scratch (delete `.aux`, `.bbl`, `.log` files) and verify clean build
- [ ] No "??" from undefined references or citations
- [ ] No overfull hbox warnings wider than 1pt
- [ ] All figures render correctly (check embedded fonts)
- [ ] Abstract fits within the journal's word limit
- [ ] Page count is within the journal's limit (including appendix if counted)
- [ ] Author information is anonymized if the journal uses double-blind review
- [ ] Supplementary materials (online appendix, replication files) are referenced in the main text
