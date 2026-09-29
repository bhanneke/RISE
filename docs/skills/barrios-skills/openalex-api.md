<!-- DO NOT EDIT — auto-copied from skills/barrios-skills/details/openalex-api.md -->

# `openalex-api`

Turns bibliometric questions into reproducible OpenAlex REST pulls (works, authors, institutions, sources, concepts, topics, funders, publishers) through a bundled `scripts/query_openalex.py` that builds filter-safe URLs, handles cursor pagination, and writes JSON/JSONL. Keep the raw export before cleaning, use repeated `--filter` flags for AND logic, and validate IDs, dates, citation counts and authorships before analysis.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../barrios-skills/">Barrios Skills (John Manuel Barrios)</a></div><div><b>Category:</b> <code>literature</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2026 John Barrios"). The vendored third-party skills keep their own terms: the Anthropic document skills say "Proprietary. LICENSE.txt has complete terms", and the K-Dense skills carry per-library licence lines.</code></div><div><b>Updated:</b> 2026-05-26</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>literature-discovery</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Barrios88/barrios-skills/contents/skills/research-tools/openalex-api/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/barrios-skills/openalex-api/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Barrios88/barrios-skills/blob/main/skills/research-tools/openalex-api/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Barrios88/barrios-skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

> **Barrios Skills** — John Barrios's curated workflow for economists and accountants. Prioritize reproducible empirical work, clear identification language, and journal-ready output.

## OpenAlex API

### Overview

Use this skill to turn research questions into reliable OpenAlex API queries and structured outputs. Prefer `scripts/query_openalex.py` for repeatable retrieval, pagination, and filter-safe URL construction.

### Workflow

1. Define the target entity: `works`, `authors`, `institutions`, `sources`, `concepts`, `topics`, `funders`, or `publishers`.
2. Define retrieval scope: exact ID lookup, search, or filtered dataset pull.
3. Build query parameters with `scripts/query_openalex.py` instead of handcrafting URLs.
4. Retrieve data to JSON/JSONL and keep the raw export before downstream cleaning.
5. Validate key fields (IDs, dates, citation counts, authorships) before analysis.

### Query Rules

- Use repeated `--filter` flags for AND logic.
- Use OpenAlex pipe syntax (for example `value1|value2`) inside one filter for OR logic.
- Use `--select` to reduce payload size for large pulls.
- Use `--cursor '*'` for deep paging beyond basic page limits.
- Include `--mailto you@domain.edu` for polite-pool style identification.
- Use `OPENALEX_API_KEY` or `--api-key` when available for higher-rate access.

### Common Commands

```bash
## Fetch one work by OpenAlex ID
python3 scripts/query_openalex.py works --entity-id W2741809807 --select "id,display_name,publication_year,cited_by_count"

## Search works and save first 200 records
python3 scripts/query_openalex.py works \
  --search "political polarization" \
  --filter "from_publication_date:2020-01-01" \
  --sort "cited_by_count:desc" \
  --per-page 100 \
  --pages 2 \
  --output polarization_works.json

## Cursor-paginate author records to JSONL
python3 scripts/query_openalex.py authors \
  --filter "last_known_institutions.country_code:US" \
  --cursor "*" \
  --max-results 500 \
  --format jsonl \
  --output us_authors.jsonl
```

### Output Guidance

- Prefer JSON for full response bundles and JSONL for row-wise pipelines.
- Keep original IDs (`id`, `ids.openalex`, DOI fields) unchanged in exports.
- When reporting findings, cite exact query parameters used to ensure reproducibility.

### Resources

- Use `scripts/query_openalex.py` for all API calls.
- Use `references/openalex-query-patterns.md` for entity routing, filter templates, and reusable query patterns.
