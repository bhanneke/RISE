<!-- DO NOT EDIT — auto-copied from skills/aris/details/skills-codex-gemini-review.md -->

# `skills-codex-gemini-review`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../aris/">ARIS skills</a></div><div><b>Category:</b> <code>review</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-05-18</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>referee-simulation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/skills-codex-gemini-review/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/aris/skills-codex-gemini-review/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## skills-codex-gemini-review

This package is a **thin override layer** for users who want:

- **Codex** as the main executor
- **Gemini** as the reviewer
- the local `gemini-review` MCP bridge instead of a second Codex reviewer

It is designed to sit on top of the upstream Codex-native package at `skills/skills-codex/`.

### What this package contains

- Only the reviewer-aware skill overrides that need a different reviewer backend
- No duplicate templates or resource directories
- No replacement for the base `skills/skills-codex/` installation

Current overrides:

- `idea-creator`
- `idea-discovery`
- `idea-discovery-robot`
- `research-review`
- `novelty-check`
- `research-refine`
- `auto-review-loop`
- `grant-proposal`
- `paper-plan`
- `paper-figure`
- `paper-poster`
- `paper-slides`
- `paper-write`
- `paper-writing`
- `auto-paper-improvement-loop`

### Core 8 vs Full 15

To avoid confusion, there are two useful ways to describe this overlay:

- **Core 8**: the direct reviewer-heavy overlay set that maps one-to-one to the earlier Claude-review route
- **Full 15**: the current reviewer-aware Codex skill surface routed to Gemini in this repository

The **core 8** are:

- `research-review`
- `novelty-check`
- `research-refine`
- `auto-review-loop`
- `paper-plan`
- `paper-figure`
- `paper-write`
- `auto-paper-improvement-loop`

The additional **7** routed reviewer-aware entry points are:

- `idea-creator`
- `idea-discovery`
- `idea-discovery-robot`
- `grant-proposal`
- `paper-writing`
- `paper-slides`
- `paper-poster`

So when comparing against the Claude overlay, the cleanest statement is:

> The Gemini route preserves the same core 8-skill reviewer overlay shape, but expands the practical reviewer-facing surface to 15 skills in the current repo.

### Direct Consumers vs Wrappers

- **12 direct consumers** call `mcp__gemini-review__review_start` / `review_reply_start` / `review_status` themselves:
  - `research-review`
  - `novelty-check`
  - `research-refine`
  - `auto-review-loop`
  - `paper-plan`
  - `paper-figure`
  - `paper-write`
  - `auto-paper-improvement-loop`
  - `idea-creator`
  - `grant-proposal`
  - `paper-slides`
  - `paper-poster`
- **3 wrappers** mostly orchestrate downstream reviewer-aware skills and pass `REVIEWER_MODEL=gemini-review` through:
  - `idea-discovery`
  - `idea-discovery-robot`
  - `paper-writing`

### Install

Before registering the bridge, prepare the direct Gemini API path:

- **Gemini API**: set `GEMINI_API_KEY` or `GOOGLE_API_KEY` (for example in `~/.gemini/.env`)

Optional fallback only:

- **Gemini CLI**: install `gemini` and complete login/auth if you explicitly want `GEMINI_REVIEW_BACKEND=cli`

1. Install the base Codex-native mirror first:

```bash
bash ~/aris_repo/tools/install_aris_codex.sh ~/your-project
```

2. Re-run with the Gemini overlay enabled:

```bash
bash ~/aris_repo/tools/install_aris_codex.sh ~/your-project --reconcile --with-gemini-review-overlay
```

3. Register the local reviewer bridge:

```bash
mkdir -p ~/.codex/mcp-servers/gemini-review
cp mcp-servers/gemini-review/server.py ~/.codex/mcp-servers/gemini-review/server.py
codex mcp add gemini-review --env GEMINI_REVIEW_BACKEND=api -- python3 ~/.codex/mcp-servers/gemini-review/server.py
```

The bridge defaults to the direct Gemini API path. This is the intended reviewer backend for this overlay.

If the default API model is temporarily rate-limited on your current free-tier window, keep the same overlay and bridge, and override only the reviewer model:

```bash
codex mcp remove gemini-review
codex mcp add gemini-review --env GEMINI_REVIEW_BACKEND=api --env GEMINI_REVIEW_MODEL=gemini-flash-latest -- python3 ~/.codex/mcp-servers/gemini-review/server.py
```

### Why this exists

The upstream `skills/skills-codex/` path already supports Codex-native execution with a second Codex reviewer via `spawn_agent`.

This package adds a different split:

- executor: Codex
- reviewer: Gemini direct API
- transport: `gemini-review` MCP

For long paper and review prompts, the reviewer path uses:

- `review_start`
- `review_reply_start`
- `review_status`

This avoids the observed Codex-hosted timeout issue when Gemini is invoked synchronously through a local bridge.

### Validation Summary

This overlay was validated in two ways:

- **Coverage check**: all `15` predefined reviewer-aware skill overrides in this package were checked to confirm they target `gemini-review`
- **Runtime check**:
  - the underlying bridge completed sync, async, threaded follow-up, and multimodal local-image review tests
  - representative Codex-side runs on a private, non-public research repository confirmed that real skill executions could reach the Gemini reviewer path for research-review, idea-generation, and paper-planning style tasks

Operational note:

- Gemini free tier was usable for this workflow in practice, but bursty stress tests could still produce temporary `429` responses
- on the same setup, a later retry completed sync review, async `review_start` -> `review_status`, and threaded `review_reply_start` -> `review_status` successfully with `GEMINI_REVIEW_MODEL=gemini-flash-latest`
- for long prompts, prefer the async `review_start` / `review_reply_start` + `review_status` path

### References

- Upstream overlay pattern from ARIS:
  - <https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/main/skills/skills-codex-claude-review>
  - <https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/tree/main/mcp-servers/claude-review>
- Local Gemini reviewer bridge in this repo:
  - `mcp-servers/gemini-review/README.md`
- Gemini backends referenced by this overlay:
  - Official Gemini API: <https://ai.google.dev/api>
  - Official Gemini CLI: <https://github.com/google-gemini/gemini-cli>
  - AI Studio API key entry: <https://aistudio.google.com/apikey>

This package keeps the upstream ARIS skill shape, but swaps the reviewer transport to the local `gemini-review` bridge. It now covers every predefined Codex skill in this repo that previously depended on a secondary Codex reviewer or `mcp__codex__codex` review step. We intentionally did not directly depend on a generic Gemini MCP server package because the ARIS review skills rely on the narrow `review*` tool contract, resumable review-thread behavior, and now optional local-image review for poster PNGs.
