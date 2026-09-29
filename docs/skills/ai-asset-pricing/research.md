<!-- DO NOT EDIT — auto-copied from skills/ai-asset-pricing/details/research.md -->

# `/research`

Searches for papers, references and methodology literature through the Perplexity MCP tools and returns them in a fixed format.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-asset-pricing/">ai-asset-pricing (Alex Dickerson)</a></div><div><b>Category:</b> <code>literature</code></div><div><b>Field:</b> finance</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")</code></div><div><b>Updated:</b> 2026-03-12</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>literature-discovery</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Alexander-M-Dickerson/ai-asset-pricing/contents/.claude/skills/research/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-asset-pricing/research/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/research/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Alexander-M-Dickerson/ai-asset-pricing?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Research Skill

Search for academic papers and references using the Perplexity MCP server.

### Examples
- `/research corporate bond measurement error bias` -- broad literature search
- `/research Blume Stambaugh 1983` -- find a specific paper
- `/research recent working papers on [topic]` -- recent work
- `/research Smith Jones 2023 bibtex` -- search and generate BibTeX

### Tool Selection
- Use `perplexity_research` for broad literature surveys
- Use `perplexity_search` for specific paper/author lookups
- Use `perplexity_ask` for quick methodology questions
- Use `perplexity_reason` for analytical comparisons

### Workflow

1. Parse the user's query from $ARGUMENTS
2. Choose the appropriate Perplexity tool based on query type
3. Execute the search
4. Format results:
   - Title, Authors, Year, Journal/Venue
   - DOI or URL when available
   - Brief summary of relevance to the current project (check `guidance/paper-context.md` for themes)
5. **Verify each paper** (MANDATORY before any BibTeX generation):
   - Run a second `perplexity_search` with the EXACT title in quotes
   - Confirm: all author names, year, journal, volume/pages if published
   - Check if paper already exists in the .bib file
   - If any detail cannot be confirmed, mark as UNVERIFIED
   - CRITICAL: For each field, only report what Perplexity explicitly returns.
     If search results confirm authors + title but DO NOT mention a journal,
     write "Journal: UNCONFIRMED" -- NEVER fill from training data.
6. If "bibtex" is in the query, generate **verified** BibTeX entries and offer to append to .bib
7. Note which of the project's themes each result relates to (check `guidance/paper-context.md` if available)

### Output Format

```
**Title** (Year)
Authors: ...
Journal: ...
DOI/URL: ...
Status: VERIFIED / UNVERIFIED / PARTIAL
Relevance: [brief note on relation to the current project]
```
