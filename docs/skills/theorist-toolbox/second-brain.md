<!-- DO NOT EDIT — auto-copied from skills/theorist-toolbox/details/second-brain.md -->

# `/second-brain`

Sets up and queries an agentic-RAG second brain over a local library of theory papers, with LaTeX-aware ingestion, theorem and proof lookup, and hybrid search.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../theorist-toolbox/">Theorist Toolbox</a></div><div><b>Category:</b> <code>literature</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07-31</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>literature-synthesis</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/morankor/theorist-toolbox/contents/skills/second-brain/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/theorist-toolbox/second-brain/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/morankor/theorist-toolbox/blob/main/skills/second-brain/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/morankor/theorist-toolbox?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Second Brain — setup and usage

> **Author:** Moran Koren, Ben-Gurion University of the Negev (korenmor@bgu.ac.il). Part of the [Theorist Toolbox](https://github.com/morankor/theorist-toolbox).

Sets up a self-contained agentic-RAG library in a target directory: papers are
ingested from LaTeX source (preferred), HTML, or PDF-OCR into a chunked,
QA-gated index; an agent (or Claude Code itself via MCP) answers questions by
reading exact theorems/proofs with custom macros and prerequisite definitions
auto-bundled. Full design: `package/` in this skill contains the complete
`brain` Python package.

Throughout, `$SKILL` means this skill's base directory (shown in the message
that loaded this file) and `$TARGET` means the directory the user wants the
second brain in (default: the current working directory; ask only if the cwd
is clearly wrong for a paper library, e.g. a code repo).

### Step 0 — detect state

`$TARGET/config.toml` exists AND `$TARGET/.venv/bin/brain` runs → already
initialized: skip to **Usage**. Otherwise run **Init**.

### Init

```bash
cd "$TARGET"
python3 -m venv .venv
.venv/bin/pip install -q "$SKILL/package[dev,providers,mcp,web]"
cp "$SKILL/templates/config.toml" config.toml
.venv/bin/brain status        # creates papers/ parsed_papers/ index/ scratchpad/
```

Then register the MCP server for Claude Code by writing `$TARGET/.mcp.json`
(absolute paths, no `~`):

```json
{
  "mcpServers": {
    "second-brain": {
      "command": "<ABS_TARGET>/.venv/bin/python",
      "args": ["-m", "brain.mcp_server"],
      "env": { "BRAIN_CONFIG": "<ABS_TARGET>/config.toml" }
    }
  }
}
```

Verify the install with the bundled fixture, then remove the test entry:

```bash
.venv/bin/brain ingest "$SKILL/package/tests/fixtures/mini_paper" --id selftest --no-llm
.venv/bin/brain search "monotone valuations"       # selftest must rank first
.venv/bin/python -c "
from pathlib import Path; from brain.config import load_config; from brain.index import store
import shutil
cfg = load_config(Path('config.toml')); idx = store.load_index(cfg.index_file)
idx.pop('selftest', None); store.save_index(cfg.index_file, idx)
shutil.rmtree(cfg.parsed_dir / 'selftest', ignore_errors=True)"
```

Finish by telling the user: (1) init is done and verified; (2) restarting
Claude Code in `$TARGET` and approving the "second-brain" MCP server lets them
ask about their library in any session, billed to their Claude subscription;
(3) the standalone CLI default (`claude-code` provider) also uses the
subscription — keep `ANTHROPIC_API_KEY` unset for that; and (4) offer to ingest
papers right away (see below). If the directory already contains PDFs or `.tex`
sources, list them and offer to ingest them.

### Usage

All commands run from `$TARGET` with `.venv/bin/brain`:

- **Ingest** — `brain ingest <arxiv-id | tex-dir | file.tex | url | file.pdf>`
  - Prefer arXiv ids / LaTeX source (Tier 0: exact math, no OCR). PDFs need
    `pip install "$SKILL/package[ocr]"` and are QA-flagged by default.
  - Idempotent; add `--force` to re-ingest, `--no-llm` to skip metadata
    enrichment (use `--no-llm` when the user wants speed or determinism).
  - After a batch, run `brain status` and report any ⚠ needs_review papers.
- **Search (no LLM)** — `brain search "query" -v`
- **Ask** — `brain ask "question" -v` (or `brain repl` for multi-turn).
  Inside Claude Code, prefer the MCP tools directly instead of shelling out
  to `brain ask` — same backend, no nested agent.
- **Health** — `brain status`; run `.venv/bin/pytest "$SKILL/package/tests" -q`
  if something seems broken.

When answering from MCP tools yourself, follow the library's grounding rules:
search first; use read_theorem_or_proof for any formal statement; record
notation with write_to_scratchpad after reading a Model section; cite
`[paper_id, Item]` for every mathematical claim; flag needs_review sources.

### Updating the bundled package

If the canonical copy in `papers_2nd_brain` evolves, refresh this skill with:
`rsync -a --exclude __pycache__ --exclude '*.egg-info' <canonical>/pyproject.toml <canonical>/src <canonical>/tests "$SKILL/package/"`
— then existing brains pick it up via
`.venv/bin/pip install -q --force-reinstall "$SKILL/package[dev,providers,mcp,web]"`.
