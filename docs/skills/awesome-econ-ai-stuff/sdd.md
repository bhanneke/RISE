<!-- DO NOT EDIT — auto-copied from skills/awesome-econ-ai-stuff/details/sdd.md -->

# `sdd`

Spec-driven development framework for structured feature creation.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-econ-ai-stuff/">awesome-econ-ai-stuff (Antonio Mele)</a></div><div><b>Category:</b> <code>design</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>Other (see repo)</code></div><div><b>Updated:</b> 2026</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>research-design</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/meleantonio/awesome-econ-ai-stuff/contents/_skills/engineering/sdd/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-econ-ai-stuff/sdd/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/engineering/sdd/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/meleantonio/awesome-econ-ai-stuff?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Spec-Driven Development (SDD)

### Core Philosophy

1. **Clarity before Code:** Never generate code until requirements and design are approved.
2. **Iterative Refinement:** Loop through Req → Design → Tasks until solid.
3. **Code via Docs:** The truth is in the markdown files, not the chat.

### Commands

Execute in the **project root** (where `spec/` and `steering/` live).

#### `init`

Scaffold the SDD folder structure and template files.

1. If `spec/` already exists, skip or ask before overwriting.
2. Create `spec/` and `steering/`.
3. Create `spec/intent.md` (blank or minimal placeholder).
4. Copy templates from this skill’s `templates/` directory (in the same folder as `SKILL.md`, or from your install path under `~/.cursor/skills/sdd/` after copying the skill there) into the project:
   - `templates/spec/requirements.md` → `spec/requirements.md`
   - `templates/spec/design.md` → `spec/design.md`
   - `templates/spec/tasks.md` → `spec/tasks.md`
   - `templates/steering/coding-standards.md` → `steering/coding-standards.md`

#### `reqs`

Generate EARS requirements from intent.

1. Read `spec/intent.md` and `steering/*.md`.
2. Convert the intent into EARS requirements (see EARS Quick Reference below). Add a Properties (invariants) section.
3. Write to `spec/requirements.md`.
4. Ask for user approval before proceeding.

#### `design`

Generate technical design from requirements.

1. Read `spec/requirements.md` and `steering/*.md`.
2. Create a technical design: architecture, data models, component interfaces, error handling, security. Apply the Design Checklist below.
3. Write to `spec/design.md`.
4. Ask for user approval before proceeding.

#### `tasks`

Generate implementation tasks from design.

1. Read `spec/design.md` and `spec/requirements.md`.
2. Create a sequential task list: max two levels (Task > Subtask). Link each task to requirement IDs (e.g. `REQ-001`). Follow Task Rules below.
3. Write to `spec/tasks.md`.
4. Ask for user approval before proceeding.

#### `status`

Report current state of the spec.

1. List files in `spec/` (and optionally `steering/`).
2. If `spec/tasks.md` exists, count unchecked `[ ]` vs checked `[x]` and summarize.

### EARS Quick Reference

- **Ubiquitous:** `<system> shall <response>`
- **Event-Driven:** `WHEN <trigger> [precondition] the <system> shall <response>`
- **Unwanted:** `IF <unwanted condition> THEN the <system> shall <response>`
- **State-Driven:** `WHILE <system state>, the <system> shall <response>`
- **Optional:** `WHERE <feature is included>, the <system> shall <response>`

Use IDs like `[REQ-001]`; add a **Properties (Invariants)** section for universal correctness statements.

### Design Checklist

- Edit ruthlessly (remove over-engineering).
- Check for circular dependencies; fix via interface extraction, layering, or events.
- Ensure alignment with steering documents.

### Task Rules

- Two-level hierarchy maximum (Task > Subtask).
- Sequential order (each task builds on previous).
- Traceability: each task or subtask links back to requirement IDs (e.g. *Traceability:* Implements `REQ-001`).

### Additional Resources

- For full framework detail (workflow, refinement, iteration triggers), see reference.md.
