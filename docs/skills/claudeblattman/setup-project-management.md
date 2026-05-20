<!-- DO NOT EDIT — auto-copied from skills/claudeblattman/details/setup-project-management.md -->

# `/setup-project-management`

Bootstrap a project-management workspace

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../claudeblattman/">claudeblattman (Chris Blattman)</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-04</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/chrisblattman/claudeblattman/contents/skills/setup-project-management.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/claudeblattman/setup-project-management/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/chrisblattman/claudeblattman/blob/main/skills/setup-project-management.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/chrisblattman/claudeblattman?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Setup Project Management

*v1.1 — Simplified: reduced redundancy and verbosity*

Sets up: folder structure, TODO.md, PROJECT_INDEX.md, .claude/CLAUDE.md, Google Doc hub, and meeting transcript workflow.

### Instructions

#### Phase 1: Discovery (DO THIS FIRST)

Before making ANY changes, assess the current state:

1. **Explore existing folder structure** — list files/folders, note organizational system, identify where documents/data/code live
2. **Check for existing docs** — README, INDEX, .claude/, Google Docs, Notion
3. **Identify tools and workflows** — Google Docs, Overleaf, Box, GitHub, WhatsApp groups, meeting notes, scripts
4. **Check external file sources** — shared drives, cloud storage (Box, OneDrive, etc.). If found, get: web URL, local path, sync status. Identify high-priority files for local copies.
5. **Assess data sensitivity** — IRB status, identifiable data locations

#### Phase 2: Gap Analysis

Present findings to user covering: existing structure, existing docs/tools, gaps vs. template, and potential conflicts.

#### Phase 3: Design Discussion

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

#### Phase 4: Propose Customized Plan

Present a specific plan covering: folder changes, files to create, Google Doc structure, WhatsApp config, external file sources (if any), workflow adaptations, and what stays unchanged. **Get user approval before proceeding.**

#### Phase 5: Implementation

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

#### Phase 6: Verification

After implementation:

1. **Verify files** — all created files in correct locations, paths accurate, TODO.md routing links work
2. **Verify external sources** (if configured) — path in CLAUDE.md, files copied, "If Not Found" section present
3. **Verify Google Doc markers** (3-marker system):
   - Research projects need: `=== PROJECT STATUS DASHBOARD ===`, `=== DASHBOARD END ===`, `=== WEEKLY SUMMARIES START ===`
   - Institutional projects need: same first two + `=== MEETING LOG START ===`
   - All 3 required in Tab 1 — advise user to add any missing markers
4. **Summary for user** — list what was created, configured, external sources status, marker compatibility, next steps

### Key Principles

- **Explore first, change later** — never overwrite or reorganize without permission
- **Iterate** until user is satisfied; document tradeoffs when template conflicts with existing setup

### Arguments

`$ARGUMENTS` can include:
- `discover` — Only run Phases 1-2 (assessment, no changes)
- `plan` — Run through Phase 4 (stop before implementation)
- `full` — Complete setup with all phases
- `minimal` — Create only .claude/CLAUDE.md and essential config

### Examples

```
/setup-project-management discover
## Just assess current state, report findings

/setup-project-management plan
## Assess and propose plan, wait for approval

/setup-project-management
## Full interactive setup with all phases

/setup-project-management minimal
## Quick setup of just Claude config file
```

### Limitations

- Does NOT create Google Docs, restructure folders, delete/move files, configure MCP servers, or create WhatsApp groups
- Only configures existing integrations

### Troubleshooting

- **WhatsApp groups not found** — names must be exact and case-sensitive; try partial search first
- **Google Doc access** — verify Google Workspace MCP is configured; extract document ID from URL correctly
- **Meeting transcripts** — if using Granola, MCP gives summaries only; export from Granola app for full transcripts

### Customization Points

- **Folder structure:** Adapt the numbered folder system to match your conventions
- **Document hub:** Configure for Google Docs, Notion, or other platforms
- **Team channels:** Add WhatsApp groups, Slack channels, or other communication tools
- **Data sensitivity:** Add IRB-specific handling rules for sensitive projects
