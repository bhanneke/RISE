---
name: research
description: Search for academic papers, references, and methodology literature using Perplexity MCP
user_invocable: true
---

# Research Skill

Search for academic papers and references using the Perplexity MCP server.

## Examples
- `/research corporate bond measurement error bias` -- broad literature search
- `/research Blume Stambaugh 1983` -- find a specific paper
- `/research recent working papers on [topic]` -- recent work
- `/research Smith Jones 2023 bibtex` -- search and generate BibTeX

## Tool Selection
- Use `perplexity_research` for broad literature surveys
- Use `perplexity_search` for specific paper/author lookups
- Use `perplexity_ask` for quick methodology questions
- Use `perplexity_reason` for analytical comparisons

## Workflow

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

## Output Format

```
**Title** (Year)
Authors: ...
Journal: ...
DOI/URL: ...
Status: VERIFIED / UNVERIFIED / PARTIAL
Relevance: [brief note on relation to the current project]
```
