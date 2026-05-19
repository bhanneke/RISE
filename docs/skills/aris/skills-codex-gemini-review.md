<!-- DO NOT EDIT — auto-copied from skills/aris/details/skills-codex-gemini-review.md -->

# `skills-codex-gemini-review`



<style>
.skill-layout { display: grid; grid-template-columns: minmax(0, 2fr) 18em; gap: 2em; }
@media (max-width: 900px) { .skill-layout { grid-template-columns: 1fr; } }
.skill-sidebar { background: #fafafa; border:1px solid #eaeaea; border-radius:8px; padding:1em; position:sticky; top:1em; align-self:start; font-size:0.95em; }
.skill-sidebar h3, .skill-sidebar h4 { color:#00695c; }
.skill-sidebar dl dt { margin-top:0.5em; }
.skill-sidebar dl dd { margin:0.1em 0 0 0; }
</style>

<div class="skill-layout">
<div class="skill-content" markdown>

---

# skills-codex-gemini-review

This package is a **thin override layer** for users who want:

- **Codex** as the main executor
- **Gemini** as the reviewer
- the local `gemini-review` MCP bridge instead of a second Codex reviewer

It is designed to sit on top of the upstream Codex-native package at `skills/skills-codex/`.

## What this package contains

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

## Core 8 vs Full 15

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

## Direct Consumers vs Wrappers

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

## Install

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

## Why this exists

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

## Validation Summary

This overlay was validated in two ways:

- **Coverage check**: all `15` predefined reviewer-aware skill overrides in this package were checked to confirm they target `gemini-review`
- **Runtime check**:
  - the underlying bridge completed sync, async, threaded follow-up, and multimodal local-image review tests
  - representative Codex-side runs on a private, non-public research repository confirmed that real skill executions could reach the Gemini reviewer path for research-review, idea-generation, and paper-planning style tasks

Operational note:

- Gemini free tier was usable for this workflow in practice, but bursty stress tests could still produce temporary `429` responses
- on the same setup, a later retry completed sync review, async `review_start` -> `review_status`, and threaded `review_reply_start` -> `review_status` successfully with `GEMINI_REVIEW_MODEL=gemini-flash-latest`
- for long prompts, prefer the async `review_start` / `review_reply_start` + `review_status` path

## References

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


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/skills-codex-gemini-review/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>wanshuiyin/Auto-claude-code-research-in-sleep</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../aris.md">ARIS skills</a></dd>
<dt><b>Category</b></dt><dd><code>review</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>referee-simulation</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-05-18</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep">⭐ wanshuiyin/Auto-claude-code-research-in-sleep</a><br><img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/aris/skills-codex-gemini-review/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/aris.yml">edit on GitHub</a>.</p>
</div>

</div>
