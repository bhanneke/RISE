<!-- DO NOT EDIT — auto-copied from skills/claudeblattman/details/setup-project-management.md -->

# `/setup-project-management`

Bootstrap a project-management workspace

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

# Setup Project Management

*v1.1 — Simplified: reduced redundancy and verbosity*

Sets up: folder structure, TODO.md, PROJECT_INDEX.md, .claude/CLAUDE.md, Google Doc hub, and meeting transcript workflow.

## Instructions

### Phase 1: Discovery (DO THIS FIRST)

Before making ANY changes, assess the current state:

1. **Explore existing folder structure** — list files/folders, note organizational system, identify where documents/data/code live
2. **Check for existing docs** — README, INDEX, .claude/, Google Docs, Notion
3. **Identify tools and workflows** — Google Docs, Overleaf, Box, GitHub, WhatsApp groups, meeting notes, scripts
4. **Check external file sources** — shared drives, cloud storage (Box, OneDrive, etc.). If found, get: web URL, local path, sync status. Identify high-priority files for local copies.
5. **Assess data sensitivity** — IRB status, identifiable data locations

### Phase 2: Gap Analysis

Present findings to user covering: existing structure, existing docs/tools, gaps vs. template, and potential conflicts.

### Phase 3: Design Discussion

**STOP AND DISCUSS WITH USER** before proceeding. Gather:

0. **Project type** — determines folder structure, Google Doc setup, config fields:
   - a) **Quantitative RCT** — full folders with IRB, Survey Instruments, Field Materials
   - b) **Qualitative/Ethnographic** — Fieldwork folder replaces IRB; may skip survey/field folders
   - c) **Theory/Writing** — minimal structure; may skip Google Doc hub and WhatsApp if solo

1. **Folder structure** — adopt numbered system, keep current naming, or hybrid?
2. **Central document hub** — existing Google Doc or create new? Structure?
3. **Meeting transcripts** — storage location, tool (Granola, Zoom, manual)?
4. **Communication channels** — WhatsApp group names (exact), email keywords/senders
5. **Team and workflow** — key members, meeting cadence
6. **Sensitivity screening** — any PI-only or personnel groups to flag?
7. **Related projects** — shared team members, overlapping keywords, cross-project email handling?
8. **External file sources** — shared drive details; which files to copy locally (typically: research design, IRB, key lit; NOT: raw data, admin budgets); sync vs. unsync preference

### Phase 4: Propose Customized Plan

Present a specific plan covering: folder changes, files to create, Google Doc structure, WhatsApp config, external file sources (if any), workflow adaptations, and what stays unchanged. **Get user approval before proceeding.**

### Phase 5: Implementation

Only after user approval:

1. **Create folder structure** (new folders only; never reorganize without permission)
   - **Quantitative RCT**: Full numbered folders with IRB, Survey Instruments, Field Materials
   - **Qualitative/Ethnographic**: Fieldwork folder (Interview Memos, Transcripts, Consent Forms); may skip survey/field folders; add Decision_Log.md
   - **Theory/Writing**: Minimal (Paper, Presentations, Literature, AI_Collaboration); skip Google Doc hub/WhatsApp if solo
   - Skip inapplicable folder numbers — this is expected.

2. **Create TODO.md** in `AI_Collaboration/`. Replace project name and date placeholders.

3. **Create PROJECT_INDEX.md** — project overview, Google Doc links, transcript workflow, folder map

4. **Create .claude/CLAUDE.md** with:
   - Project overview, WhatsApp groups (exact names), Google Doc ID/URL
   - Folder paths for transcripts, weekly reviews, dashboard archive
   - Gmail keywords (include/exclude), sensitivity guidelines, cross-project notes
   - Team roster, project status, project-specific workflows
   - External file sources section if applicable (source info, files copied vs. not copied, "If Not Found" guidance)

5. **Copy external files** (if approved) and document in PROJECT_INDEX.md

6. **Set up or document Google Doc hub** (don't restructure without explicit permission)

7. **Create AI collaboration subfolders** if missing: `Transcripts/`, `Weekly_Reviews/`, `Dashboard_Archive/`

8. **Create submissions subfolders** if applicable: `Grants/`, `Journal/`, `Pre_Registration/`, `Conference/`

### Phase 6: Verification

After implementation:

1. **Verify files** — all created files in correct locations, paths accurate, TODO.md routing links work
2. **Verify external sources** (if configured) — path in CLAUDE.md, files copied, "If Not Found" section present
3. **Verify Google Doc markers** (3-marker system):
   - Research projects need: `=== PROJECT STATUS DASHBOARD ===`, `=== DASHBOARD END ===`, `=== WEEKLY SUMMARIES START ===`
   - Institutional projects need: same first two + `=== MEETING LOG START ===`
   - All 3 required in Tab 1 — advise user to add any missing markers
4. **Summary for user** — list what was created, configured, external sources status, marker compatibility, next steps

## Key Principles

- **Explore first, change later** — never overwrite or reorganize without permission
- **Iterate** until user is satisfied; document tradeoffs when template conflicts with existing setup

## Arguments

`$ARGUMENTS` can include:
- `discover` — Only run Phases 1-2 (assessment, no changes)
- `plan` — Run through Phase 4 (stop before implementation)
- `full` — Complete setup with all phases
- `minimal` — Create only .claude/CLAUDE.md and essential config

## Examples

```
/setup-project-management discover
# Just assess current state, report findings

/setup-project-management plan
# Assess and propose plan, wait for approval

/setup-project-management
# Full interactive setup with all phases

/setup-project-management minimal
# Quick setup of just Claude config file
```

## Limitations

- Does NOT create Google Docs, restructure folders, delete/move files, configure MCP servers, or create WhatsApp groups
- Only configures existing integrations

## Troubleshooting

- **WhatsApp groups not found** — names must be exact and case-sensitive; try partial search first
- **Google Doc access** — verify Google Workspace MCP is configured; extract document ID from URL correctly
- **Meeting transcripts** — if using Granola, MCP gives summaries only; export from Granola app for full transcripts

## Customization Points

- **Folder structure:** Adapt the numbered folder system to match your conventions
- **Document hub:** Configure for Google Docs, Notion, or other platforms
- **Team channels:** Add WhatsApp groups, Slack channels, or other communication tools
- **Data sensitivity:** Add IRB-specific handling rules for sensitive projects


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/chrisblattman/claudeblattman/contents/skills/setup-project-management.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>chrisblattman/claudeblattman</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../claudeblattman.md">claudeblattman (Chris Blattman)</a></dd>
<dt><b>Category</b></dt><dd><code>infra</code></dd>
<dt><b>Field</b></dt><dd>general</dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/chrisblattman/claudeblattman">⭐ chrisblattman/claudeblattman</a><br><img src="https://img.shields.io/github/stars/chrisblattman/claudeblattman?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/chrisblattman/claudeblattman/blob/main/skills/setup-project-management.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/claudeblattman/setup-project-management/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/claudeblattman.yml">edit on GitHub</a>.</p>
</div>

</div>
