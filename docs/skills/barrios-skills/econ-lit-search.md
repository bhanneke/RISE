<!-- DO NOT EDIT — auto-copied from skills/barrios-skills/details/econ-lit-search.md -->

# `econ-lit-search`

Staged search over a Meilisearch index of about 51k economics papers (NBER working papers plus JEL-coded journal articles): a cheap broad scan with citation-sorted snippets, then full abstracts, body-passage snippets, and full text only when needed, with filters by exact author string, JEL code, journal and year range. Caveat: the public copy redacts the index host to a placeholder URL and reads the key from `MEILI_API_KEY`, so it does not run without access to the author's index.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../barrios-skills/">Barrios Skills (John Manuel Barrios)</a></div><div><b>Category:</b> <code>literature</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2026 John Barrios"). The vendored third-party skills keep their own terms: the Anthropic document skills say "Proprietary. LICENSE.txt has complete terms", and the K-Dense skills carry per-library licence lines.</code></div><div><b>Updated:</b> 2026-05-26</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>literature-discovery</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Barrios88/barrios-skills/contents/skills/research-tools/econ-lit-search/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/barrios-skills/econ-lit-search/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Barrios88/barrios-skills/blob/main/skills/research-tools/econ-lit-search/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Barrios88/barrios-skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

> **Barrios Skills** — John Barrios's curated workflow for economists and accountants. Prioritize reproducible empirical work, clear identification language, and journal-ready output.

## Econ-Lit Search

Search a Meilisearch-powered index of ~51k economics papers. The corpus covers NBER working papers and JEL-coded journal articles with full text, abstracts, author metadata, citation counts, JEL codes, and DOIs.

### Setup

The helper script at `scripts/econ_lit_search.py` handles all API interaction. Import it like this:

```python
import sys
sys.path.insert(0, "<this skill's directory>/scripts")
from econ_lit_search import EconLitSearch

api = EconLitSearch()
```

The API key and endpoint are baked into the script. No environment variables needed.

### Workflow: how to run a literature search

Follow this progression from broad to narrow. Each step uses more tokens, so start lean and drill in only where needed.

#### 1. Broad scan (cheap — metadata + short snippet)

Start here. Returns titles, authors, journal, year, citation count, DOI, and a ~60-word abstract snippet. Sorted by citations by default.

```python
results = api.scan("gig economy entrepreneurship", limit=10, filter="year > 2015")
api.print_hits(results, show_abstract=True)
```

Use this to orient: which authors keep appearing? Which journals? What's the citation landscape?

#### 2. Narrow with full abstracts (moderate)

Once you've spotted a thread, switch to `read_abstracts()`. This uses `matchingStrategy: "all"` so every query term must appear. Returns full abstracts with keyword highlighting.

```python
results = api.read_abstracts("occupational licensing labor market regulation", limit=5, filter="year > 2005")
api.print_hits(results, show_abstract=True)
```

#### 3. Body snippets (moderate — see how papers discuss a method/concept)

Want to see how papers talk about a specific method or idea without downloading full text? `body_snippets()` returns a ~300-char window from inside the paper centered on the best match.

```python
results = api.body_snippets("staggered difference in differences treatment effects", limit=5, filter="year > 2015")
api.print_hits(results, show_body=True)
```

#### 4. Full text (expensive — use sparingly)

Only when you've identified a specific paper you need to read in full. Responses can be 10k–50k+ chars. Always target a specific paper by DOI.

```python
result = api.full_text("10.3386/w26783")
paper = result["hits"][0]
print(paper["body"])
```

#### 5. Explore the corpus (free — no documents returned)

Use `facets()` to understand coverage before searching. Returns counts per journal, year, JEL code — zero document content.

```python
results = api.facets("corporate disclosure", facet_fields=["journal", "year"])
print(results["facetDistribution"])
```

### Common patterns

#### Search by author
```python
results = api.by_author("Yael V. Hochberg", limit=20)
api.print_hits(results)
```

#### Filter by JEL codes
```python
results = api.search(
    "regulation entry barriers",
    limit=10,
    filter='jel_codes IN ["L26", "M41", "J44"] AND year > 2015',
    attributesToRetrieve=["title", "authors", "year", "jel_codes", "cited_by_count"],
    sort=["cited_by_count:desc"],
)
```

#### Filter by journal
```python
results = api.search(
    "",
    limit=10,
    filter='journal = "Journal of Accounting Research"',
    attributesToRetrieve=["title", "authors", "year", "cited_by_count"],
    sort=["cited_by_count:desc"],
)
```

#### Year ranges
```python
results = api.search(
    "financial reporting quality",
    limit=10,
    filter="year >= 2018 AND year <= 2025",
    attributesToRetrieve=["title", "authors", "year", "cited_by_count"],
    sort=["year:desc"],
)
```

#### Most-cited in a journal
```python
results = api.search(
    "",
    limit=10,
    filter='journal = "Journal of Financial Economics"',
    attributesToRetrieve=["title", "authors", "year", "cited_by_count"],
    sort=["cited_by_count:desc"],
)
```

### Presenting results to the user

When showing search results, format them cleanly. For a broad scan, a table or numbered list works well:

```
1. "Paper Title" — Card, et al. (2021) — QJE — Cited 342x
2. "Another Paper" — Autor (2019) — AER — Cited 218x
```

When the user asks for detail on specific papers, show the abstract or body snippet inline. For full text, summarize key sections rather than dumping the entire body unless they explicitly ask for it.

### Field reference

| Field | Type | Filterable | Sortable |
|---|---|---|---|
| title | string | no | no |
| authors | string[] | yes | no |
| abstract | string | no | no |
| body | string | no | no |
| journal | string | yes | no |
| year | number | yes | yes |
| jel_codes | string[] | yes | no |
| cited_by_count | number | no | yes |
| doi | string | yes | no |
| url | string | no | no |
| text_char_count | number | no | yes |

### Important constraints

- **Rate limit**: 2 requests/second, burst of 5. Space requests if doing multiple sequential searches.
- **Max results per request**: 50.
- **Full text is large**: 10k–50k+ chars per paper. Only fetch `body` when you need it, and keep `limit` low (1–3).
- **Author names must match exactly** in filters. Use the `scan()` results to find the exact name string before filtering.
- **`body` is only in `_formatted`** when using crops/highlights. The raw `body` field must be explicitly requested via `attributesToRetrieve`.
