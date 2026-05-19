# LaTeX Tables for Economics Publications

Guidelines for producing publication-ready regression tables, summary statistics,
and other tabular output in economics papers. These conventions follow the style
of top economics journals (AER, QJE, Econometrica, REStud, JPE).

## Required packages

```latex
\usepackage{booktabs}     % Professional rules: \toprule, \midrule, \bottomrule
\usepackage{siunitx}      % Number alignment, decimal alignment, formatting
\usepackage{multirow}     % Span rows
\usepackage{multicol}     % Span columns (standard LaTeX, no package needed)
\usepackage{threeparttable} % Table + notes in a unified structure
\usepackage{tabularx}     % Tables with flexible-width columns
\usepackage{dcolumn}      % Alternative to siunitx for decimal alignment
\usepackage{adjustbox}    % Scale oversized tables
```

## Core principles

1. **Never use vertical rules.** No `|` in column specs. Ever. This is the single
   most important rule for professional tables.
2. **Use only three horizontal rules:** `\toprule`, `\midrule`, `\bottomrule` from
   booktabs, plus occasional `\cmidrule` for sub-headers.
3. **Align numbers on the decimal point** using siunitx `S` columns.
4. **Notes go below the table** inside `threeparttable`, not as footnotes.
5. **Keep tables self-contained.** A reader should understand the table without
   reading the surrounding text.

## Basic regression table

```latex
\begin{table}[htbp]
  \centering
  \caption{Effect of Education on Log Earnings}\label{tab:returns-education}
  \begin{threeparttable}
    \begin{tabular}{l S[table-format=-1.3] S[table-format=-1.3] S[table-format=-1.3]}
      \toprule
      & {(1)} & {(2)} & {(3)} \\
      & {OLS} & {OLS} & {IV} \\
      \midrule
      Years of education & 0.089{***} & 0.072{***} & 0.132{**} \\
                         & {(0.004)}  & {(0.005)}  & {(0.052)} \\[6pt]
      Experience         &            & 0.034{***} & 0.029{***} \\
                         &            & {(0.002)}  & {(0.003)} \\[6pt]
      Experience$^2$/100 &            & {-0.054}{***} & {-0.048}{***} \\
                         &            & {(0.004)}  & {(0.006)} \\
      \midrule
      Controls           & {No}  & {Yes} & {Yes} \\
      Observations       & {45,320} & {45,320} & {42,118} \\
      $R^2$              & 0.148 & 0.312 &       \\
      First-stage $F$    &       &       & 24.6  \\
      \bottomrule
    \end{tabular}
    \begin{tablenotes}[flushleft]
      \small
      \item \textit{Notes:} Dependent variable is log hourly earnings.
        Standard errors clustered at the state level in parentheses.
        Controls include age, race, marital status, and region fixed effects.
        The instrument in column~(3) is compulsory schooling laws.
        {*}~$p<0.10$, {**}~$p<0.05$, {***}~$p<0.01$.
    \end{tablenotes}
  \end{threeparttable}
\end{table}
```

## Significance stars conventions

The standard in economics (and what journals expect):

| Symbol | Threshold | Meaning |
|--------|-----------|---------|
| `*`    | $p < 0.10$ | Significant at 10% level |
| `**`   | $p < 0.05$ | Significant at 5% level |
| `***`  | $p < 0.01$ | Significant at 1% level |

Always define the convention in the table notes. Some journals and some
subfields use only two levels (5% and 1%). Be consistent within a paper.

When using siunitx `S` columns, wrap stars in braces to prevent parsing errors:

```latex
0.089{***}    % Correct: siunitx ignores braced content
0.089***      % WRONG: siunitx will choke on the asterisks
```

Similarly, wrap text entries in `S` columns with braces:

```latex
{(0.004)}     % Standard error in parentheses
{Yes}         % Text entry in a numeric column
{--}          % Em-dash for missing values
```

## Standard errors and confidence intervals

Standard errors go on the line below the coefficient, in parentheses. This is
the universal convention in economics.

```latex
Education     & 0.089{***} \\
              & {(0.004)}  \\[6pt]  % Small vertical space between variables
```

Brackets `[...]` are reserved for confidence intervals or t-statistics.
Do not mix conventions within a paper. State which you use in the notes.

```latex
% Alternative: 95% confidence intervals in brackets
Education     & 0.089{***} \\
              & {[0.081, 0.097]}  \\
```

## siunitx configuration

Set up siunitx in the preamble for consistent number formatting:

```latex
\sisetup{
  group-separator = {,},          % Thousands separator
  group-minimum-digits = 4,       % Apply grouping for 4+ digit numbers
  input-symbols = {()},           % Allow parentheses in S columns
  input-open-uncertainty  = (,
  input-close-uncertainty = ),
  table-align-text-before = false,
  table-align-text-after  = false,
}
```

### Column type specifications

```latex
S[table-format=1.3]         % One digit before decimal, three after (e.g., 0.089)
S[table-format=-1.3]        % Allow negative sign (e.g., -0.054)
S[table-format=5.0]         % Integer up to 5 digits (e.g., 45320)
S[table-format=1.3e1]       % Scientific notation
S[table-format=2.1]         % Two digits, one decimal (e.g., 24.6)
```

## Panel tables

Panel tables group related regressions. Use `\cmidrule` to visually separate panels.

```latex
\begin{table}[htbp]
  \centering
  \caption{Heterogeneous Effects by Gender and Education}\label{tab:heterogeneity}
  \begin{threeparttable}
    \begin{tabular}{l S[table-format=-1.3] S[table-format=-1.3] S[table-format=-1.3] S[table-format=-1.3]}
      \toprule
      & {(1)} & {(2)} & {(3)} & {(4)} \\
      & {All} & {Male} & {Female} & {College+} \\
      \midrule
      \multicolumn{5}{l}{\textit{Panel A: Log earnings}} \\[3pt]
      Treatment       & 0.045{**}  & 0.038{*}   & 0.056{**}  & 0.023 \\
                      & {(0.019)}  & {(0.022)}  & {(0.028)}  & {(0.031)} \\[6pt]
      Observations    & {12,450}   & {6,830}    & {5,620}    & {4,210} \\
      $R^2$           & 0.245      & 0.231      & 0.268      & 0.198 \\
      \midrule
      \multicolumn{5}{l}{\textit{Panel B: Employment}} \\[3pt]
      Treatment       & 0.032{***} & 0.028{**}  & 0.039{***} & 0.018 \\
                      & {(0.011)}  & {(0.013)}  & {(0.015)}  & {(0.017)} \\[6pt]
      Observations    & {15,200}   & {8,100}    & {7,100}    & {5,430} \\
      $R^2$           & 0.178      & 0.165      & 0.195      & 0.142 \\
      \midrule
      Controls        & {Yes} & {Yes} & {Yes} & {Yes} \\
      State FE        & {Yes} & {Yes} & {Yes} & {Yes} \\
      Year FE         & {Yes} & {Yes} & {Yes} & {Yes} \\
      \bottomrule
    \end{tabular}
    \begin{tablenotes}[flushleft]
      \small
      \item \textit{Notes:} Each column-panel is a separate regression.
        Robust standard errors in parentheses. Controls include age,
        race, and marital status. {*}~$p<0.10$, {**}~$p<0.05$, {***}~$p<0.01$.
    \end{tablenotes}
  \end{threeparttable}
\end{table}
```

## Summary statistics table

```latex
\begin{table}[htbp]
  \centering
  \caption{Summary Statistics}\label{tab:sumstats}
  \begin{threeparttable}
    \begin{tabular}{l S[table-format=2.2] S[table-format=2.2] S[table-format=2.2] S[table-format=2.2] S[table-format=6.0]}
      \toprule
      & {Mean} & {SD} & {Min} & {Max} & {$N$} \\
      \midrule
      Log hourly wage       & 2.89  & 0.67  & 0.34  & 6.21  & 45320 \\
      Years of education    & 13.21 & 2.84  & 0     & 20    & 45320 \\
      Experience (years)    & 19.45 & 11.32 & 0     & 48    & 45320 \\
      Female                & 0.47  & 0.50  & 0     & 1     & 45320 \\
      Married               & 0.58  & 0.49  & 0     & 1     & 45312 \\
      Union member          & 0.21  & 0.41  & 0     & 1     & 44890 \\
      \bottomrule
    \end{tabular}
    \begin{tablenotes}[flushleft]
      \small
      \item \textit{Notes:} Sample is prime-age workers (25--54) from the
        2015--2019 CPS. Hourly wages are in 2019 dollars.
    \end{tablenotes}
  \end{threeparttable}
\end{table>
```

## Balance table (for RCTs and quasi-experiments)

```latex
\begin{table}[htbp]
  \centering
  \caption{Baseline Balance}\label{tab:balance}
  \begin{threeparttable}
    \begin{tabular}{l S[table-format=2.2] S[table-format=2.2] S[table-format=-1.2] S[table-format=1.3]}
      \toprule
      & {Control} & {Treatment} & {Difference} & {$p$-value} \\
      & {mean}    & {mean}      &              &             \\
      \midrule
      Age                & 34.21 & 34.58 & 0.37    & 0.412 \\
      Female             & 0.51  & 0.49  & {-0.02} & 0.583 \\
      Years of education & 12.84 & 12.91 & 0.07    & 0.718 \\
      Baseline earnings  & 28450 & 28890 & 440     & 0.651 \\
      Employed           & 0.72  & 0.71  & {-0.01} & 0.804 \\
      \midrule
      $N$                & {3,200} & {3,180} & & \\
      Joint $F$-test $p$ &         &         & & 0.892 \\
      \bottomrule
    \end{tabular}
    \begin{tablenotes}[flushleft]
      \small
      \item \textit{Notes:} Differences estimated by OLS regression of each
        variable on the treatment indicator. $p$-values from robust standard
        errors. Joint test is the $p$-value from an $F$-test of regressing
        treatment on all baseline covariates.
    \end{tablenotes}
  \end{threeparttable}
\end{table>
```

## Difference-in-differences table

```latex
\begin{table}[htbp]
  \centering
  \caption{Difference-in-Differences Estimates}\label{tab:did}
  \begin{threeparttable}
    \begin{tabular}{l S[table-format=-1.3] S[table-format=-1.3] S[table-format=-1.3]}
      \toprule
      & {(1)} & {(2)} & {(3)} \\
      \midrule
      Treated $\times$ Post & 0.078{**}  & 0.065{**}  & 0.071{**} \\
                             & {(0.032)}  & {(0.029)}  & {(0.031)} \\[6pt]
      \midrule
      Unit FE               & {Yes} & {Yes} & {Yes} \\
      Time FE               & {Yes} & {Yes} & {Yes} \\
      Controls               & {No}  & {Yes} & {Yes} \\
      Unit-specific trends   & {No}  & {No}  & {Yes} \\
      Observations           & {24,800} & {24,800} & {24,800} \\
      \bottomrule
    \end{tabular}
    \begin{tablenotes}[flushleft]
      \small
      \item \textit{Notes:} Dependent variable is log employment.
        Standard errors clustered at the state level in parentheses.
        {*}~$p<0.10$, {**}~$p<0.05$, {***}~$p<0.01$.
    \end{tablenotes}
  \end{threeparttable}
\end{table}
```

## Column spanning headers

Use `\multicolumn` with `\cmidrule` to group columns under a shared header:

```latex
\begin{tabular}{l S S S S}
  \toprule
  & \multicolumn{2}{c}{Developed countries} & \multicolumn{2}{c}{Developing countries} \\
  \cmidrule(lr){2-3} \cmidrule(lr){4-5}
  & {(1)} & {(2)} & {(3)} & {(4)} \\
  & {OLS} & {IV}  & {OLS} & {IV} \\
  \midrule
  ...
\end{tabular}
```

Note `\cmidrule(lr)` trims the rule on both sides to create a visual gap
between groups. This is important for readability.

## Notes conventions

The notes block should follow a consistent structure:

1. **"Notes:"** in italics, followed by a description of the dependent variable
2. Specification details (standard error type, clustering, fixed effects)
3. Sample restrictions if not obvious
4. Significance star definitions (always last)

```latex
\begin{tablenotes}[flushleft]
  \small
  \item \textit{Notes:} Dependent variable is log hourly earnings in 2019 dollars.
    All regressions include state and year fixed effects.
    Standard errors clustered at the state level in parentheses.
    The sample includes prime-age workers (25--54) from the CPS.
    {*}~$p<0.10$, {**}~$p<0.05$, {***}~$p<0.01$.
\end{tablenotes}
```

## Landscape tables

For wide tables that do not fit in portrait mode:

```latex
\usepackage{pdflscape}    % or \usepackage{lscape}

\begin{landscape}
\begin{table}
  ...
\end{table}
\end{landscape}
```

## Scaling oversized tables

When a table is slightly too wide, use `adjustbox`:

```latex
\begin{adjustbox}{max width=\textwidth}
  \begin{tabular}{...}
    ...
  \end{tabular}
\end{adjustbox}
```

Prefer this over `\resizebox` because `adjustbox` preserves font size when the
table already fits.

## Exporting tables from statistical software

When generating tables from Stata, R, or Python:

- **Stata:** `esttab` / `estout` with `booktabs` option produces compatible output.
  Use `fragment` to get just the tabular body, then wrap in your own table environment.
- **R:** `stargazer`, `modelsummary`, or `kableExtra` with booktabs style.
  `modelsummary` is the modern choice and handles S columns well.
- **Python:** `stargazer` port, or build tables with pandas `.to_latex()`
  and post-process. The `pystout` package follows economics conventions.

Always review and adjust generated output. Automated tools rarely get every detail
right (decimal alignment, note formatting, star placement in S columns).

## Common mistakes to avoid

1. Using vertical lines (`|`) in column specifications.
2. Using `\hline` instead of booktabs rules (`\toprule`, `\midrule`, `\bottomrule`).
3. Inconsistent decimal places across columns.
4. Reporting too many decimal places. Two or three significant digits is usually enough
   for coefficients. Match precision to the standard error.
5. Missing standard errors or confidence intervals.
6. Not defining significance stars.
7. Placing notes as footnotes instead of inside `threeparttable`.
8. Misaligned numbers (not using `S` columns or `dcolumn`).
9. Reporting $R^2$ with four decimal places. Two is sufficient.
10. Not reporting the number of observations or clusters.
