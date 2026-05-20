<!-- DO NOT EDIT — auto-copied from skills/aris/details/deepxiv.md -->

# `deepxiv`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../aris/">ARIS skills</a></div><div><b>Category:</b> <code>literature</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-05-18</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>literature-discovery</code> · <code>literature-synthesis</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/deepxiv/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/aris/deepxiv/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## DeepXiv Paper Search & Progressive Reading

Search topic or paper ID: $ARGUMENTS

### Role & Positioning

DeepXiv is the **progressive-reading** literature source:

| Skill | Best for |
|------|----------|
| `/arxiv` | Direct preprint search and PDF download |
| `/semantic-scholar` | Published venue metadata, citation counts, DOI links |
| `/deepxiv` | Layered reading: search → brief → head → section, plus trending and web search |

Use DeepXiv when you want to avoid loading full papers too early.

### Constants

- **DEEPXIV_FETCHER** — canonical name `deepxiv_fetch.py`, resolved per
  `shared-references/integration-contract.md` §2
  (Policy D1 — primary + fallback cascade). If unresolved (canonical
  chain exhausted), fall back to the raw `deepxiv` CLI (documented per
  command below).
- **MAX_RESULTS = 10** — Default number of results to return.

> Overrides (append to arguments):
> - `/deepxiv "agent memory" - max: 5` — top 5 results
> - `/deepxiv "2409.05591" - brief` — quick paper summary
> - `/deepxiv "2409.05591" - head` — metadata + section overview
> - `/deepxiv "2409.05591" - section: Introduction` — read one section only
> - `/deepxiv "trending" - days: 14 - max: 10` — trending papers
> - `/deepxiv "karpathy" - web` — DeepXiv web search
> - `/deepxiv "258001" - sc` — Semantic Scholar metadata by ID

### Setup

DeepXiv is optional. If the CLI is not installed, tell the user:

```bash
pip install deepxiv-sdk
```

On first use, `deepxiv` auto-registers a free token and stores it in `~/.env`.

### Workflow

#### Step 1: Parse Arguments

Parse `$ARGUMENTS` for:

- **Query or ID**: a paper topic, arXiv ID, or Semantic Scholar ID
- **`- max: N`**: override `MAX_RESULTS`
- **`- brief`**: fetch paper brief
- **`- head`**: fetch metadata and section map
- **`- section: NAME`**: fetch one named section
- **`- trending`** or query `trending`: fetch trending papers
- **`- days: 7|14|30`**: trending time window
- **`- web`**: run DeepXiv web search
- **`- sc`**: fetch Semantic Scholar metadata by ID

If the main argument looks like an arXiv ID and no explicit mode is given, default to `- brief`.

#### Step 2: Locate the Adapter

Resolve `$DEEPXIV_FETCHER` via the canonical strict-safe chain (see
`shared-references/integration-contract.md` §2).
Policy D1 cascade: the resolved adapter is preferred; if unresolved
(canonical chain exhausted), fall back to raw `deepxiv` CLI commands
documented in Step 3.

```bash
cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)" || exit 1
if [ -z "${ARIS_REPO:-}" ] && [ -f .aris/installed-skills.txt ]; then
    ARIS_REPO=$(awk -F'\t' '$1=="repo_root"{print $2; exit}' .aris/installed-skills.txt 2>/dev/null) || true
fi
DEEPXIV_FETCHER=".aris/tools/deepxiv_fetch.py"
[ -f "$DEEPXIV_FETCHER" ] || DEEPXIV_FETCHER="tools/deepxiv_fetch.py"
[ -f "$DEEPXIV_FETCHER" ] || { [ -n "${ARIS_REPO:-}" ] && DEEPXIV_FETCHER="$ARIS_REPO/tools/deepxiv_fetch.py"; }
[ -f "$DEEPXIV_FETCHER" ] || DEEPXIV_FETCHER=""

## Smoke test (optional — adapter resolution shown to user). The cascade
## in Step 3 below branches purely on `[ -n "$DEEPXIV_FETCHER" ]`; a
## resolved-but-non-functional adapter is not currently auto-demoted.
if [ -n "$DEEPXIV_FETCHER" ]; then
  echo "DeepXiv adapter resolved at: $DEEPXIV_FETCHER" >&2
else
  echo "DeepXiv adapter unresolved (canonical chain exhausted); raw deepxiv CLI fallback will be used." >&2
fi
```

#### Step 3: Execute the Minimal Command

**Search papers**

```bash
python3 "$DEEPXIV_FETCHER" search "QUERY" --max MAX_RESULTS
```

Fallback:

```bash
deepxiv search "QUERY" --limit MAX_RESULTS --format json
```

**Brief summary**

```bash
python3 "$DEEPXIV_FETCHER" paper-brief ARXIV_ID
```

Fallback:

```bash
deepxiv paper ARXIV_ID --brief --format json
```

**Section map**

```bash
python3 "$DEEPXIV_FETCHER" paper-head ARXIV_ID
```

Fallback:

```bash
deepxiv paper ARXIV_ID --head --format json
```

**Specific section**

```bash
python3 "$DEEPXIV_FETCHER" paper-section ARXIV_ID "SECTION_NAME"
```

Fallback:

```bash
deepxiv paper ARXIV_ID --section "SECTION_NAME" --format json
```

**Trending**

```bash
python3 "$DEEPXIV_FETCHER" trending --days 7 --max MAX_RESULTS
```

Fallback:

```bash
deepxiv trending --days 7 --limit MAX_RESULTS --output json
```

**Web search**

```bash
python3 "$DEEPXIV_FETCHER" wsearch "QUERY"
```

Fallback:

```bash
deepxiv wsearch "QUERY" --output json
```

**Semantic Scholar metadata**

```bash
python3 "$DEEPXIV_FETCHER" sc "SEMANTIC_SCHOLAR_ID"
```

Fallback:

```bash
deepxiv sc "SEMANTIC_SCHOLAR_ID" --output json
```

#### Step 4: Present Results

When searching, present a compact table:

```text
| # | ID | Title | Year | Citations | Notes |
|---|----|-------|------|-----------|-------|
```

When reading a paper, show:

- title
- arXiv ID
- authors
- venue/date if available
- TLDR or abstract summary
- suggested next step: `brief` → `head` → `section`

#### Step 5: Escalate Depth Only When Needed

Use this progression:

1. `search`
2. `paper-brief`
3. `paper-head`
4. `paper-section`
5. full paper only if necessary

Do not jump to full-paper reads when a brief or one section answers the question.

#### Step 6: Update Research Wiki (if active)

**Required when `research-wiki/` exists in the project**; skip silently
otherwise. When the wiki dir exists, resolve `$WIKI_SCRIPT` per the
canonical chain at
`shared-references/wiki-helper-resolution.md`
(Variant B — warn-and-skip). Ingest papers that were meaningfully
read (brief / head / section / full) during this invocation — mere
`search` hits without a depth read do not need ingestion:

```bash
if [ -d research-wiki/ ]; then
  cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)" || exit 1
  ARIS_REPO="${ARIS_REPO:-$(awk -F'\t' '$1=="repo_root"{print $2; exit}' .aris/installed-skills.txt 2>/dev/null)}"
  WIKI_SCRIPT=".aris/tools/research_wiki.py"
  [ -f "$WIKI_SCRIPT" ] || WIKI_SCRIPT="tools/research_wiki.py"
  [ -f "$WIKI_SCRIPT" ] || { [ -n "${ARIS_REPO:-}" ] && WIKI_SCRIPT="$ARIS_REPO/tools/research_wiki.py"; }
  [ -f "$WIKI_SCRIPT" ] || {
    echo "WARN: research_wiki.py not found; depth-read summary delivered, wiki ingest skipped. Fix: bash tools/install_aris.sh, export ARIS_REPO, or cp <ARIS-repo>/tools/research_wiki.py tools/." >&2
    WIKI_SCRIPT=""
  }
  if [ -n "$WIKI_SCRIPT" ]; then
    for each arxiv_id the user asked this skill to read in depth:
        python3 "$WIKI_SCRIPT" ingest_paper research-wiki/ \
            --arxiv-id "<arxiv_id>"
  fi
fi
```

The helper handles metadata / slug / dedup / page / index / log in one
call — **do not handwrite `papers/<slug>.md`**. See
`shared-references/integration-contract.md`.
Backfill missed ingests with
`python3 "$WIKI_SCRIPT" sync research-wiki/ --arxiv-ids <id1>,<id2>,...`
after resolving `$WIKI_SCRIPT` as above.

### Key Rules

- Prefer the adapter script over raw `deepxiv` commands when available.
- DeepXiv is optional. If unavailable, give the install command and suggest `/arxiv` or `/research-lit "topic" - sources: web`.
- Use section-level reads to save tokens.
- Treat DeepXiv as complementary to `/arxiv` and `/semantic-scholar`, not a replacement.
- If the result overlaps with a published venue paper from Semantic Scholar, keep the richer venue metadata in the final summary.
