<!-- DO NOT EDIT — auto-copied from skills/awesome-econ-ai-stuff/details/sdd.md -->

# `sdd`

Spec-driven development framework for structured feature creation.

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

---
name: sdd
description: >
  Implements the Spec-Driven Development lifecycle (Intent, Requirements, Design, Tasks, Build)
  for structured feature development. Use when the user wants to scaffold a new feature spec,
  generate EARS requirements, create a technical design, break work into tasks, or check spec status.
  Trigger on keywords: sdd, spec-driven, ears requirements, feature spec.
workflow_stage: engineering
compatibility:
  - claude-code
  - cursor
  - codex
  - gemini-cli
author: Awesome Econ AI Community
version: 1.0.0
tags:
  - spec-driven-development
  - requirements
  - design
  - documentation
---

# Spec-Driven Development (SDD)

## Core Philosophy

1. **Clarity before Code:** Never generate code until requirements and design are approved.
2. **Iterative Refinement:** Loop through Req → Design → Tasks until solid.
3. **Code via Docs:** The truth is in the markdown files, not the chat.

## Commands

Execute in the **project root** (where `spec/` and `steering/` live).

### `init`

Scaffold the SDD folder structure and template files.

1. If `spec/` already exists, skip or ask before overwriting.
2. Create `spec/` and `steering/`.
3. Create `spec/intent.md` (blank or minimal placeholder).
4. Copy templates from this skill’s `templates/` directory (in the same folder as `SKILL.md`, or from your install path under `~/.cursor/skills/sdd/` after copying the skill there) into the project:
   - `templates/spec/requirements.md` → `spec/requirements.md`
   - `templates/spec/design.md` → `spec/design.md`
   - `templates/spec/tasks.md` → `spec/tasks.md`
   - `templates/steering/coding-standards.md` → `steering/coding-standards.md`

### `reqs`

Generate EARS requirements from intent.

1. Read `spec/intent.md` and `steering/*.md`.
2. Convert the intent into EARS requirements (see EARS Quick Reference below). Add a Properties (invariants) section.
3. Write to `spec/requirements.md`.
4. Ask for user approval before proceeding.

### `design`

Generate technical design from requirements.

1. Read `spec/requirements.md` and `steering/*.md`.
2. Create a technical design: architecture, data models, component interfaces, error handling, security. Apply the Design Checklist below.
3. Write to `spec/design.md`.
4. Ask for user approval before proceeding.

### `tasks`

Generate implementation tasks from design.

1. Read `spec/design.md` and `spec/requirements.md`.
2. Create a sequential task list: max two levels (Task > Subtask). Link each task to requirement IDs (e.g. `REQ-001`). Follow Task Rules below.
3. Write to `spec/tasks.md`.
4. Ask for user approval before proceeding.

### `status`

Report current state of the spec.

1. List files in `spec/` (and optionally `steering/`).
2. If `spec/tasks.md` exists, count unchecked `[ ]` vs checked `[x]` and summarize.

## EARS Quick Reference

- **Ubiquitous:** `<system> shall <response>`
- **Event-Driven:** `WHEN <trigger> [precondition] the <system> shall <response>`
- **Unwanted:** `IF <unwanted condition> THEN the <system> shall <response>`
- **State-Driven:** `WHILE <system state>, the <system> shall <response>`
- **Optional:** `WHERE <feature is included>, the <system> shall <response>`

Use IDs like `[REQ-001]`; add a **Properties (Invariants)** section for universal correctness statements.

## Design Checklist

- Edit ruthlessly (remove over-engineering).
- Check for circular dependencies; fix via interface extraction, layering, or events.
- Ensure alignment with steering documents.

## Task Rules

- Two-level hierarchy maximum (Task > Subtask).
- Sequential order (each task builds on previous).
- Traceability: each task or subtask links back to requirement IDs (e.g. *Traceability:* Implements `REQ-001`).

## Additional Resources

- For full framework detail (workflow, refinement, iteration triggers), see [reference.md](reference.md).


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/meleantonio/awesome-econ-ai-stuff/contents/_skills/engineering/sdd/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>meleantonio/awesome-econ-ai-stuff</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../awesome-econ-ai-stuff.md">awesome-econ-ai-stuff (Antonio Mele)</a></dd>
<dt><b>Category</b></dt><dd><code>design</code></dd>
<dt><b>Field</b></dt><dd>general</dd>
<dt><b>Pipeline stages</b></dt><dd><code>research-design</code></dd>
<dt><b>License</b></dt><dd>Other (see repo)</dd>
<dt><b>Last update</b></dt><dd>2026</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff">⭐ meleantonio/awesome-econ-ai-stuff</a><br><img src="https://img.shields.io/github/stars/meleantonio/awesome-econ-ai-stuff?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/engineering/sdd/SKILL.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/awesome-econ-ai-stuff/sdd/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/awesome-econ-ai-stuff.yml">edit on GitHub</a>.</p>
</div>

</div>
