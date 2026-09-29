---
name: verify-citations
description: Audit citations in LaTeX files -- check all \cite keys exist in .bib and verify via Perplexity
user_invocable: true
---

# Verify Citations Skill

Audit citations for correctness. Checks that every \cite{KEY} has a matching BibTeX entry and verifies each entry against Perplexity web search.

## Examples
- `/verify-citations` -- audit all citations in main.tex
- `/verify-citations --key blume1983` -- verify single entry

## Workflow

1. Read `main.tex` and extract all `\cite{KEY}` and `\citep{KEY}` commands
2. Read the .bib file to get the full BibTeX database
3. For each citation key:
   a. Check KEY exists in .bib -- if missing, flag as MISSING
   b. Extract: author, title, year, journal from the BibTeX entry
   c. Use `perplexity_search` to verify: `"{title}" {first author surname} {year}`
   d. Build comparison table:

      | Field | BibTeX value | Perplexity result | Match? |
      |-------|-------------|-------------------|--------|
      | Authors | {from .bib} | {from search} | Y/N/-- |
      | Title | ... | ... | Y/N/-- |
      | Year | ... | ... | Y/N/-- |
      | Journal | ... | ... | Y/N/-- |

      Use Y = confirmed, N = mismatch, -- = not found in search.
      CRITICAL: If Perplexity is blank for a field, write "NOT FOUND IN SEARCH" -- NEVER fill from memory.

4. Classify each citation:
   - **OK**: ALL fields confirmed
   - **PARTIAL**: Authors + title confirmed, journal/volume not found
   - **MISMATCH**: Fields contradict search results
   - **UNVERIFIED**: Cannot find paper online
   - **MISSING**: Key in \cite{} but not in .bib

5. For forthcoming papers: use `perplexity_ask` as fallback to check journal placement

6. Output verification report:
   ```
   Citation Audit: main.tex
   Total: N citations checked
   OK: X | Partial: Y | Mismatch: Z | Missing: W

   --- FLAGGED ENTRIES ---
   [KEY] STATUS: details...
   ```

Process citations in batches of 5 to respect Perplexity rate limits.
