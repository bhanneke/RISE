<!-- DO NOT EDIT — auto-copied from skills/theorist-toolbox/details/co-math-init.md -->

# `/co-math-init`

Scaffolds a structured proof-building project (paper.tex, goals, decisions log, workstreams) with strict mode: every gap flagged unproven, nothing complete without reviewer sign-off.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../theorist-toolbox/">Theorist Toolbox</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>formal-modeling</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/morankor/theorist-toolbox/contents/skills/co-math-init/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/theorist-toolbox/co-math-init/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/morankor/theorist-toolbox/blob/main/skills/co-math-init/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/morankor/theorist-toolbox?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

> **Author:** Moran Koren, Ben-Gurion University of the Negev (korenmor@bgu.ac.il). Part of the [Theorist Toolbox](https://github.com/morankor/theorist-toolbox).


## co-math-init

Bootstrap a new research project for the personal AI co-mathematician system, modelled after the Google DeepMind AI Co-Mathematician paper (Zheng et al., 2026-05-07).

This skill creates the directory layout, copies the LaTeX template, initializes the per-project hook configuration, and sets up the workstream registry. After init, the user can spawn workstreams via the `project-coordinator` sub-agent.

### When to invoke

Trigger phrases:
- `/co-math-init`
- "start a new co-math project"
- "init a research project"
- "new mathematician project"

### Steps

#### 1. Gather inputs from the user

Ask via `AskUserQuestion`:

1. **Project name** — short, lowercase-kebab-case (e.g., `ambidextrous-sofa`). This becomes the directory name.
2. **Initial research question** — one sentence. Goes into `goals.md`. The user can refine later.
3. **Strict mode** — strict (default) or pragmatic. Strict means the prover sub-agent must mark every gap with `\unproven{...}` and never hand-wave. Pragmatic allows informal prose for minor steps. Default is **strict** unless the user explicitly says otherwise; this default is recorded in user memory and must be respected.
4. **Parent directory** — where to create the project. Default: current working directory.

#### 2. Create the directory structure

Inside `<parent>/<project-name>/`:

```
paper.tex
goals.md
decisions.md
PROJECT_README.md
co-math-config.json
workstreams/
  .gitkeep
references/
  .gitkeep
failed-explorations/
  .gitkeep
.co-math/
  approvals/
    .gitkeep
  workstream-registry.json
.claude/
  settings.json        # per-project hooks (Phase 3 — empty for now)
```

#### 3. Populate files from templates

Templates live in this skill's `templates/` directory. For each entry below, Read the template, do placeholder substitution, then Write to the project path:

| Template | Destination in project |
|---|---|
| `templates/paper.tex` | `paper.tex` |
| `templates/goals.md` | `goals.md` |
| `templates/decisions.md` | `decisions.md` |
| `templates/PROJECT_README.md` | `README.md` |
| `templates/co-math-config.json` | `co-math-config.json` |
| `templates/claude-settings.json` | `.claude/settings.json` |

Placeholders to substitute in each file:

| Placeholder | Replace with |
|---|---|
| `{{PROJECT_NAME}}` | the project name |
| `{{RESEARCH_QUESTION}}` | the user's initial question |
| `{{DATE}}` | today's date in YYYY-MM-DD |
| `{{STRICT_MODE}}` | `true` or `false` (lowercase, JSON literal) |

#### 4. Initialize the workstream registry

Write `.co-math/workstream-registry.json`:
```json
{
  "project": "<project-name>",
  "created": "<DATE>",
  "strict_mode": <true|false>,
  "next_id": 1,
  "workstreams": []
}
```

#### 5. Print next steps to the user

After scaffolding, output a concise message:
- Confirm the directory was created (with absolute path).
- Explain the files: `goals.md` for refining the question, `paper.tex` is the living working paper, `workstreams/` will fill up as the project-coordinator spawns work.
- Tell them to invoke the `project-coordinator` sub-agent (once Phase 2 ships) to start the first workstream, OR — if Phase 2 isn't built yet — to manually edit `goals.md` and start drafting in `paper.tex`.
- Note the verification ladder available to the coordinator: an informal `prover` proof (`\unproven{}` for any gap), or — for results worth machine-checking — a `lean-prover` workstream that formalises the lemma in Lean 4 and verifies it with `lake build`, closing the theorem with `\leanproved{W{NNN}}`. After any proof is APPROVED, a `proof-readability` pass can polish the exposition without touching the mathematics.
- Note that hooks are not yet wired up (Phase 3 deliverable).

### What this skill does NOT do

- It does not start any workstream itself. That is the `project-coordinator` sub-agent's job.
- It does not invoke any agent. Pure scaffolding.
- It does not modify global Claude Code settings, only writes a per-project `.claude/settings.json`.

### Notes on respecting prior user decisions

The default strict_mode value is **always strict**. If the user has previously asked to relax this for a specific project, that is recorded in that project's `decisions.md`, not as a global default. Each new project starts strict.
