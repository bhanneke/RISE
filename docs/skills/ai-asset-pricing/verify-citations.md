<!-- DO NOT EDIT — auto-copied from skills/ai-asset-pricing/details/verify-citations.md -->

# `/verify-citations`

Checks that every citation key in the LaTeX files exists in the .bib file and verifies the references through Perplexity.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-asset-pricing/">ai-asset-pricing (Alex Dickerson)</a></div><div><b>Category:</b> <code>audit</code></div><div><b>Field:</b> finance</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")</code></div><div><b>Updated:</b> 2026-03-12</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>literature-discovery</code> · <code>revision-editing</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Alexander-M-Dickerson/ai-asset-pricing/contents/.claude/skills/verify-citations/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-asset-pricing/verify-citations/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/verify-citations/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Alexander-M-Dickerson/ai-asset-pricing?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Verify Citations Skill

Audit citations for correctness. Checks that every \cite{KEY} has a matching BibTeX entry and verifies each entry against Perplexity web search.

### Examples
- `/verify-citations` -- audit all citations in main.tex
- `/verify-citations --key blume1983` -- verify single entry

### Workflow

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
