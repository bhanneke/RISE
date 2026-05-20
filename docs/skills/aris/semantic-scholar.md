<!-- DO NOT EDIT — auto-copied from skills/aris/details/semantic-scholar.md -->

# `semantic-scholar`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../aris/">ARIS skills</a></div><div><b>Category:</b> <code>literature</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-05-18</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>literature-discovery</code> · <code>literature-synthesis</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/semantic-scholar/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/aris/semantic-scholar/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Semantic Scholar Paper Search

Search topic or paper ID: $ARGUMENTS

### Role & Positioning

This skill is the **published venue** counterpart to `/arxiv`:

| Skill | Source | Best for |
|-------|--------|----------|
| `/arxiv` | arXiv API | Latest preprints, cutting-edge unrefereed work |
| `/semantic-scholar` | Semantic Scholar API | **Published** journal/conference papers (IEEE, ACM, Springer, etc.) with citation counts, venue info, TLDR |

**Do NOT duplicate arXiv's job.** If results contain an `externalIds.ArXiv` field, the paper is also on arXiv — note this but do not re-fetch from arXiv.

### Constants

- **MAX_RESULTS = 10** — Default number of search results.
- **S2_FETCHER** — canonical name `semantic_scholar_fetch.py`, resolved per
  [`shared-references/integration-contract.md`](../shared-references/integration-contract.md) §2
  (Policy D1 — primary + fallback cascade). If unresolved (canonical
  chain exhausted), fall back to the inline Python alternative
  documented in Step 2.
- **DEFAULT_FILTERS** — For general research queries, apply these by default to reduce noise:
  - `--fields-of-study "Computer Science,Engineering"`
  - `--publication-types JournalArticle,Conference`

> Overrides (append to arguments):
> - `/semantic-scholar "topic" - max: 20` — return up to 20 results
> - `/semantic-scholar "topic" - type: journal` — only journal articles
> - `/semantic-scholar "topic" - type: conference` — only conference papers
> - `/semantic-scholar "topic" - min-citations: 50` — only highly-cited papers
> - `/semantic-scholar "topic" - year: 2022-` — papers from 2022 onward
> - `/semantic-scholar "topic" - fields: all` — remove default field-of-study filter
> - `/semantic-scholar "topic" - sort: citations` — bulk search sorted by citation count
> - `/semantic-scholar "DOI:10.1109/..."` — fetch a single paper by DOI

### Workflow

#### Step 1: Parse Arguments

Parse `$ARGUMENTS` for directives:

- **Query or ID**: main search term, or a paper identifier:
  - DOI: `10.1109/TWC.2024.1234567`
  - Semantic Scholar ID: `f9314fd99be5f2b1b3efcfab87197d578160d553`
  - ArXiv: `ARXIV:2006.10685`
  - Corpus: `CorpusId:219792180`
- **`- max: N`**: override MAX_RESULTS
- **`- type: journal|conference|review|all`**: map to `--publication-types`
- **`- min-citations: N`**: map to `--min-citations`
- **`- year: RANGE`**: map to `--year` (e.g. `2022-`, `2020-2024`)
- **`- fields: FIELDS`**: override `--fields-of-study` (use `all` to remove filter)
- **`- sort: citations|date`**: use `search-bulk` with `--sort citationCount:desc` or `publicationDate:desc`

If the argument matches a DOI pattern (`10.XXXX/...`), a Semantic Scholar ID (40-char hex), or a prefixed ID (`ARXIV:...`, `CorpusId:...`), skip search and go directly to Step 3.

#### Step 2: Search Papers

Resolve `$S2_FETCHER` via the canonical strict-safe chain (see
[`shared-references/integration-contract.md`](../shared-references/integration-contract.md) §2):

```bash
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)" || exit 1
if [ -z "${ARIS_REPO:-}" ] && [ -f .aris/installed-skills.txt ]; then
    ARIS_REPO=$(awk -F'\t' '$1=="repo_root"{print $2; exit}' .aris/installed-skills.txt 2>/dev/null) || true
fi
S2_FETCHER=".aris/tools/semantic_scholar_fetch.py"
[ -f "$S2_FETCHER" ] || S2_FETCHER="tools/semantic_scholar_fetch.py"
[ -f "$S2_FETCHER" ] || { [ -n "${ARIS_REPO:-}" ] && S2_FETCHER="$ARIS_REPO/tools/semantic_scholar_fetch.py"; }
[ -f "$S2_FETCHER" ] || S2_FETCHER=""
```

**Standard search** (default — relevance-ranked):

```bash
python3 "$S2_FETCHER" search "QUERY" --max MAX_RESULTS \
  --fields-of-study "Computer Science,Engineering" \
  --publication-types JournalArticle,Conference
```

**Bulk search** (when `- sort:` is specified, or MAX_RESULTS > 100):

```bash
python3 "$S2_FETCHER" search-bulk "QUERY" --max MAX_RESULTS \
  --sort citationCount:desc \
  --fields-of-study "Computer Science" \
  --year "2020-"
```

If `$S2_FETCHER` is empty (Policy D1 cascade), fall back to inline Python using `urllib` against `https://api.semanticscholar.org/graph/v1/paper/search`.

**Recommended filter combos** (from testing):

| Goal | Flags |
|------|-------|
| High-quality journal papers | `--publication-types JournalArticle --min-citations 10` |
| CS/EE papers, recent | `--fields-of-study "Computer Science,Engineering" --year "2022-"` |
| Foundational / high-impact | `search-bulk --sort citationCount:desc --fields-of-study "Computer Science"` |
| Conference papers only | `--publication-types Conference` |

> **Note**: `--venue` requires exact venue names (e.g. "IEEE Transactions on Signal Processing"), not partial matches like "IEEE". Avoid using `--venue` in automated flows — prefer `--publication-types` + `--fields-of-study`.

#### Step 3: Fetch Details for a Specific Paper

When a single paper ID is requested:

```bash
python3 "$S2_FETCHER" paper "PAPER_ID"
```

Where PAPER_ID can be:
- DOI: `10.1109/TSP.2021.3071210`
- ArXiv: `ARXIV:2006.10685`
- CorpusId: `CorpusId:219792180`
- S2 ID: `f9314fd99be5f2b1b3efcfab87197d578160d553`

#### Step 4: De-duplicate Against arXiv

For each result, check `externalIds.ArXiv`:
- If present → paper is also on arXiv. Note this in output but do NOT re-fetch via `/arxiv`.
- If absent → paper is **venue-only** (e.g. IEEE without preprint). This is the unique value of this skill.

#### Step 5: Present Results

Present results as a table:

```text
| # | Title | Venue | Year | Citations | Authors | Type |
|---|-------|-------|------|-----------|---------|------|
| 1 | Deep Learning Enabled... | IEEE Trans. Signal Process. | 2021 | 1364 | Xie et al. | Journal |
```

For each paper, also show:
- **DOI link**: `https://doi.org/DOI` (for IEEE/ACM papers, this is the canonical link)
- **Open Access PDF**: if `openAccessPdf.url` is non-empty, show it
- **TLDR**: if available, show the one-line summary
- **Also on arXiv**: if `externalIds.ArXiv` exists, note the arXiv ID

#### Step 6: Detailed Summary

For each paper (or top 5 if many results):

```markdown
### [Title]

- **Venue**: [venue name] ([publicationVenue.type]: journal/conference)
- **Year**: [year] | **Citations**: [citationCount]
- **Authors**: [full author list]
- **DOI**: [doi link]
- **Fields**: [fieldsOfStudy]
- **TLDR**: [tldr.text if available]
- **Abstract**: [abstract]
- **Open Access**: [openAccessPdf.url or "Not available"]
- **Also on arXiv**: [ArXiv ID if exists, else "No"]
```

#### Step 7: Update Research Wiki (if active)

**Required when `research-wiki/` exists in the project**; skip silently
otherwise. When the wiki dir exists, resolve `$WIKI_SCRIPT` per the
canonical chain at
[`shared-references/wiki-helper-resolution.md`](../shared-references/wiki-helper-resolution.md)
(Variant B — warn-and-skip). For results with an `externalIds.ArXiv`
field, use `--arxiv-id`; for venue-only papers (no arXiv mirror —
common for IEEE/ACM), fall back to manual metadata:

```bash
if [ -d research-wiki/ ]; then
  cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)" || exit 1
  ARIS_REPO="${ARIS_REPO:-$(awk -F'\t' '$1=="repo_root"{print $2; exit}' .aris/installed-skills.txt 2>/dev/null)}"
  WIKI_SCRIPT=".aris/tools/research_wiki.py"
  [ -f "$WIKI_SCRIPT" ] || WIKI_SCRIPT="tools/research_wiki.py"
  [ -f "$WIKI_SCRIPT" ] || { [ -n "${ARIS_REPO:-}" ] && WIKI_SCRIPT="$ARIS_REPO/tools/research_wiki.py"; }
  [ -f "$WIKI_SCRIPT" ] || {
    echo "WARN: research_wiki.py not found; semantic-scholar results delivered, wiki ingest skipped. Fix: bash tools/install_aris.sh, export ARIS_REPO, or cp <ARIS-repo>/tools/research_wiki.py tools/." >&2
    WIKI_SCRIPT=""
  }
  [ -n "$WIKI_SCRIPT" ] && for each paper in results:
        if paper.externalIds.ArXiv:
            python3 "$WIKI_SCRIPT" ingest_paper research-wiki/ \
                --arxiv-id "<ArXiv>"
        else:
            python3 "$WIKI_SCRIPT" ingest_paper research-wiki/ \
                --title "<title>" --authors "<authors joined by , >" \
                --year <year> --venue "<venue>" \
                [--external-id-doi "<externalIds.DOI>"]
fi
```

The helper handles slug / dedup / page / index / log — **do not
handwrite `papers/<slug>.md`**. See
[`shared-references/integration-contract.md`](../shared-references/integration-contract.md).
Backfill with `/research-wiki sync --arxiv-ids <id1>,<id2>,...` for
arXiv-available papers.

#### Step 8: Final Output

Summarize what was done:

- `Found N published papers for "query"`
- `Filters applied: [publication types, fields, year range, etc.]`
- `N papers are venue-only (not on arXiv)`
- `Wiki-ingested N papers` (if `research-wiki/` was present)

Suggest follow-up skills:

```text
/arxiv "topic"           - search arXiv preprints (complements this search)
/research-lit "topic"    - multi-source review: Zotero + local PDFs + arXiv + S2
/novelty-check "idea"    - verify novelty against literature
```

### Key Rules

- **Default to filtered search**: Always apply `--fields-of-study` and `--publication-types` unless user says `- fields: all`. Without filters, S2 returns cross-discipline noise (linguistics, psychology, etc.).
- **Citation count is gold**: S2's citation data is its main advantage over arXiv. Always show `citationCount` prominently and use it to rank/prioritize results.
- **Venue metadata matters**: Show `venue` and `publicationVenue.type` (journal vs conference) — this helps users assess paper quality.
- **DOI is the canonical ID for published papers**: Always show DOI links for IEEE/ACM/Springer papers.
- **Rate limiting**: S2 API without key is heavily rate-limited (~1 req/s, strict cooldown). If HTTP 429 occurs, wait and retry. Recommend users set `SEMANTIC_SCHOLAR_API_KEY` env var for higher limits (free at https://www.semanticscholar.org/product/api#api-key-form).
- **TLDR may be null**: Some publishers (notably IEEE) elide the TLDR field. Fall back to showing the first sentence of the abstract.
- **openAccessPdf may be empty**: Many IEEE papers are closed access. Always provide the DOI link as fallback.
- If the S2 API is unreachable, suggest using `/arxiv` or `/research-lit "topic" - sources: web` as fallback.
