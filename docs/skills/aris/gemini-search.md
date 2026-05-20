<!-- DO NOT EDIT — auto-copied from skills/aris/details/gemini-search.md -->

# `gemini-search`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../aris/">ARIS skills</a></div><div><b>Category:</b> <code>literature</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-05-18</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>literature-discovery</code> · <code>literature-synthesis</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/gemini-search/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/aris/gemini-search/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Gemini Literature Search

Search query: $ARGUMENTS

### Role & Positioning

This skill uses Gemini as a **broad literature discovery** source:

| Skill | Source | Best for |
|-------|--------|----------|
| `/arxiv` | arXiv API | Latest preprints, cutting-edge unrefereed work |
| `/semantic-scholar` | Semantic Scholar API | Published venue papers (IEEE, ACM, Springer) with citation counts |
| `/deepxiv` | DeepXiv CLI | Layered reading: search, brief, section map, section reads |
| `/exa-search` | Exa API | Broad web search: blogs, docs, news, companies, research papers |
| `/gemini-search` | Gemini MCP / CLI | **AI-powered broad literature discovery** — searches across multiple angles, aliases, and sub-problems |

Use Gemini when you want AI-driven discovery that goes beyond keyword matching — Gemini decomposes topics into sub-problems, explores naming variants, and surfaces papers that traditional API searches may miss.

### Constants

- **MAX_RESULTS = 15** — Target number of papers Gemini should find.
- **MIN_YEAR = 2022** — Default minimum publication year. Override with `— year: 2020-`.
- **DEFAULT_MODEL = gemini-3-pro-preview** — Strongest available Gemini option (Gemini 3 Pro). Requires `gemini-cli` v0.40+ and `mcp__gemini-cli__ask-gemini` accepting Gemini 3 aliases (verified). Override with `— model: gemini-3-flash-preview` (Gemini 3 Flash, faster, higher quota), `— model: auto-gemini-3` (auto-routes inside the Gemini 3 family by load), or `— model: gemini-2.5-pro` / `gemini-2.5-flash` (legacy, for users on older `gemini-cli` < v0.40). The MCP tool accepts all of these verbatim.

> Overrides (append to arguments):
> - `/gemini-search "topic" — max: 20` — request up to 20 papers
> - `/gemini-search "topic" — year: 2020-` — papers from 2020 onward
> - `/gemini-search "topic" — code-only` — only papers with open-source code
> - `/gemini-search "topic" — venues: NeurIPS,ICML,ICLR` — focus on specific venues
> - `/gemini-search "topic" — model: gemini-3-flash-preview` — Gemini 3 Flash (faster, higher quota, less capable than Pro)
> - `/gemini-search "topic" — model: auto-gemini-3` — auto-routes within the Gemini 3 family by load
> - `/gemini-search "topic" — model: gemini-2.5-pro` — legacy (only if your `gemini-cli` < v0.40)

### Environment & Setup

#### Prerequisites

1. **Node.js** v16.0.0+
2. **Google Gemini CLI** — installed and authenticated
   ```bash
   npm install -g @google/gemini-cli
   gemini auth
   ```
3. **gemini-mcp-tool** — MCP bridge for Claude Code ([jamubc/gemini-mcp-tool](https://github.com/jamubc/gemini-mcp-tool))
   ```bash
   npm install -g gemini-mcp-tool
   ```

#### MCP Configuration

In `~/.claude.json` (or `%APPDATA%\Claude\claude_desktop_config.json` for Claude Desktop), add:

```json
{
  "mcpServers": {
    "gemini-cli": {
      "command": "gemini-mcp"
    }
  }
}
```

Alternative via `npx` (auto-install):
```json
{
  "mcpServers": {
    "gemini-cli": {
      "command": "npx",
      "args": ["-y", "gemini-mcp-tool"]
    }
  }
}
```

Or one-line setup:
```bash
claude mcp add gemini-cli -- npx -y gemini-mcp-tool
```

#### Authentication

Gemini CLI uses your Google account or an API key. Add to `.claude/.env`:

```bash
## .claude/.env
GEMINI_API_KEY=your-key-here
```

Claude Code automatically loads `.claude/.env` as environment variables.

- Free key from [Google AI Studio](https://aistudio.google.com/apikey)
- Flash model (`gemini-2.5-flash`) has a generous free tier (500 req/min)

#### Available MCP Tools

| Tool | Parameters | Description |
|------|-----------|-------------|
| `mcp__gemini-cli__ask-gemini` | `prompt` (required), `model` (optional), `sandbox` (optional) | Ask Gemini for analysis or research; supports `@file` syntax |
| `mcp__gemini-cli__sandbox-test` | `prompt` (required), `model` (optional) | Safe code execution in sandbox |
| `mcp__gemini-cli__ping` | — | Connection test |
| `mcp__gemini-cli__help` | — | Show Gemini CLI help |

#### Verify Setup

```bash
gemini --version
```

### Workflow

#### Step 1: Parse Arguments

Parse `$ARGUMENTS` for:
- **query**: The research topic (required)
- **max**: Override MAX_RESULTS
- **year**: Minimum publication year (e.g., `2020-`)
- **code-only**: Only include papers with open-source code
- **venues**: Comma-separated venue filter
- **model**: Override DEFAULT_MODEL

#### Step 2: Execute Search (MCP Priority)

**Priority 1 — Gemini MCP** (preferred):

Try calling `mcp__gemini-cli__ask-gemini` with the search prompt:

```
mcp__gemini-cli__ask-gemini({
  prompt: 'You are a research literature scout. Search comprehensively for papers on: "QUERY"

IMPORTANT CONSTRAINTS:
1. Search from MULTIPLE angles — do not just use the exact query. Decompose the topic into sub-problems, aliases, neighboring tasks, and common benchmark/settings variants.
2. Prefer papers that are genuinely relevant, not merely keyword-adjacent.
3. Include top venues, journals, surveys, recent preprints, and papers with code when available.
4. Focus on papers from MIN_YEAR onward unless older foundational work is necessary.

For EACH paper found, provide ALL of the following in this exact format:
- Title: [exact title]
- Authors: [full author list]
- Year: [publication year]
- Venue: [exact conference/journal name + year, or "arXiv preprint" if not published]
- arXiv ID: [format 2401.12345, or "N/A"]
- DOI: [if available, or "N/A"]
- Code URL: [GitHub/GitLab link if available, or "No code"]
- Summary: [one-sentence core contribution]

Find at least MAX_RESULTS papers with good coverage across:
- strong recent papers from top venues
- surveys/reviews if they exist
- papers with open-source code
- closely related variants of the topic

Format as a numbered list with all fields for each paper.',
  model: 'DEFAULT_MODEL'
})
```

**Priority 2 — Gemini CLI fallback** (if MCP unavailable):

If `mcp__gemini-cli__ask-gemini` fails or is not configured, fall back to CLI:

```bash
gemini -p 'You are a research literature scout. Search comprehensively for papers on: "QUERY"
...same prompt as above...' 2>/dev/null
```

- **Timeout**: 120 seconds
- **Stderr**: Pipe to `/dev/null` — contains hook warnings, not part of the response

**When to use which:**
- MCP is preferred because it integrates natively with Claude Code's tool system, handles model selection, and avoids shell escaping issues.
- CLI fallback ensures the skill works even when MCP is not configured or the MCP server process has crashed.

#### Step 3: Parse Results

Extract structured paper information from Gemini's response. For each paper, normalize to:

```
{
  title, authors, year, venue,
  arxiv_id,    // "N/A" if not available
  doi,         // "N/A" if not available
  code_url,    // "No code" if not available
  summary      // one-sentence contribution
}
```

If Gemini returns fewer papers than requested, note this but do not re-query.

#### Step 4: Present Results

Format results as a structured table:

```
| # | Title | Venue | Year | Code | Summary |
|---|-------|-------|------|------|---------|
| 1 | ... | NeurIPS 2024 | 2024 | GitHub | ... |
| 2 | ... | IEEE TWC | 2023 | No | ... |
```

For each paper, also show:
- **arXiv ID**: if available (for cross-reference with `/arxiv`)
- **DOI**: if available (canonical link for published papers)
- **Code**: GitHub/GitLab link or "No"

#### Step 5: Offer Follow-up

After presenting results, suggest:

```text
/semantic-scholar "topic"    — search published venue papers with citation counts
/arxiv "arXiv:XXXX.XXXXX"   — fetch specific preprint details
/research-lit "topic" — sources: gemini, semantic-scholar  — combined multi-source review
/novelty-check "idea"       — verify novelty against literature
```

### Key Rules

- **MCP first, CLI second.** Always try `mcp__gemini-cli__ask-gemini` before falling back to `gemini -p`.
- **Gemini is a discovery source, not a database.** Its results may include papers it "knows about" from training data. Always cross-verify critical details (exact titles, venues, years) via `/semantic-scholar` or `/arxiv` when precision matters.
- **Do not use Gemini for citation counts.** It may hallucinate citation numbers. Use Semantic Scholar for authoritative citation data.
- **Pipe stderr to `/dev/null` in CLI mode** — Gemini CLI emits hook warnings on stderr.
- **Timeout generously in CLI mode** — Gemini's thorough search can take 30-60 seconds. Set timeout to 120s.
- If both MCP and CLI are unreachable, suggest using `/semantic-scholar`, `/arxiv`, or `/research-lit "topic" — sources: web` as alternatives.
