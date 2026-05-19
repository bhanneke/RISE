# Skill: Paper Parsing

You are extracting structured content from an academic paper. Follow these rules:

## Section Identification
- Look for numbered sections (1., 2., 1.1, etc.) or named headings
- Common structure: Abstract, Introduction, Literature Review, Data, Methodology, Results, Discussion, Conclusion
- Some papers use "Empirical Strategy" or "Identification" instead of "Methodology"
- Appendices are separate sections — capture them

## Table Extraction
- Academic tables have: number (Table 1), caption, column headers, data rows, notes
- Notes typically contain: SE format ("Standard errors in parentheses"), significance stars, sample info
- Regression tables: dependent variable in column header, regressors in rows
- Summary statistics tables: Variable, N, Mean, SD, Min, Max

## Equation Extraction
- Look for numbered equations: (1), (2), etc.
- Convert to LaTeX notation: subscripts, superscripts, Greek letters
- Capture the context: what the equation represents

## Figure Identification
- Capture figure number, caption, and what the figure depicts
- For time series plots: note the axes and time range
- For scatter plots: note the variables
- You cannot see the actual figure content from text — describe based on caption and surrounding text

## Reference Extraction
- Extract from the bibliography/references section
- Format: Author(s) (Year). Title. Journal, Volume(Issue), Pages.
- Note DOIs when present
