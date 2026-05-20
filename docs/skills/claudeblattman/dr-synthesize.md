<!-- DO NOT EDIT — auto-copied from skills/claudeblattman/details/dr-synthesize.md -->

# `/dr-synthesize`

Synthesize results from a deep-research run

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

<!-- dr-synthesize v1 | sanitized from private skill -->
# /dr-synthesize

*Synthesize 2+ deep-research raw reports into a single markdown synthesis with a mandatory `## Source Reports` header preserving absolute paths to originals.*

Combine 2+ deep-research raw reports into a single synthesis. The synthesis is always a **new file** — raw inputs are never edited.

**Companion to `/deep-research`.** This skill consumes `/deep-research` outputs (or any deep-research raw reports with the canonical frontmatter). Called automatically by `/deep-research --synthesize`, but also usable standalone for ad-hoc synthesis of older reports.

## Argument hint

`<archived-path-1> <archived-path-2> [<archived-path-N>...] [--out <output-path>] [--topic <override>]`

You need at least 2 input paths. Reports must already be archived in canonical project locations (frontmatter with `date:`, `topic:`, `tool:` fields).

**Risk escalation:** Auto for synthesis writes (new file in archive). Per-item confirm if `--out` overwrites an existing file.

---

## Phase 1 — Validate inputs

For each path argument:
- Exists and is non-empty
- Has YAML frontmatter (`date`, `topic`, `tool` fields present)
- Lives in a project `raw-inputs/` folder, e.g.:
  - `~/projects/*/raw-inputs/`
  - `~/Documents/research/*/raw-inputs/`
  - `~/Documents/research/*/<paper-folder>/raw-inputs/`
- Legacy paths (e.g., a single central archive directory) are warned about; the central directory should hold INDEX only after federated migration.

If `--topic` is not provided, infer from frontmatter (must match across inputs; warn on mismatch).

**Determine output project folder** (Phase 3 `--out` default):
- If all inputs share the same parent `raw-inputs/` directory → write synthesis there.
- If inputs span multiple project folders → use the *commissioning* project (the folder of the first argument). Cross-project synthesis stubs are out of scope for v1.

## Phase 2 — Build synthesis prompt

Construct an internal prompt that:
1. Lists each input with its absolute path + tool + date + 1-line preview
2. Asks the model to identify: agreements, contradictions, gaps, unique insights per source
3. Produces a synthesis matching the schema in Phase 3

## Phase 3 — Write synthesis file

Output: `$PROJECT_DIR/${DATE}_${SLUG}_synthesis.md` where `$PROJECT_DIR` is the resolved project folder from Phase 1 (or `--out` override).

Frontmatter must include `project: <name>` so the INDEX row in Phase 4 can be generated without re-parsing the path.

**Required schema** — first section MUST be `## Source Reports` with absolute paths:

```markdown
---
date: YYYY-MM-DD
topic: <topic>
type: synthesis
sources: <count>
project: <project-name>
---

# <Topic> — Synthesis

## Source Reports
- [<tool> run, <date>] <abs-path-to-input-1>
- [<tool> run, <date>] <abs-path-to-input-2>
- [Original prompt] <abs-path-to-prompt>   # if available

## Headline Findings
<2-4 bullet points; what every source agreed on or what was the most important emergent insight>

## Agreements
<where sources converge; cite which sources>

## Contradictions
<where sources disagree; cite which sources said what; do NOT pick a winner unless evidence is clearly one-sided>

## Gaps & Open Questions
<what no source addressed; what still needs investigation>

## Unique Per-Source Insights
### From <tool-1>
- <insight>
### From <tool-2>
- <insight>
```

## Phase 4 — INDEX update (pointer rows)

Append a pointer row to the central INDEX.md and a JSONL companion row. The path column is the **canonical project location**, expressed relative to `$HOME` for portability.

```bash
INDEX=~/research-archive/INDEX.md
JSONL=~/research-archive/INDEX.jsonl

REL_PATH="${SYNTH_PATH/#$HOME\//~/}"

echo "| $DATE | $TOPIC | synthesis | — | $PROJECT | [$(basename "$SYNTH_PATH")]($REL_PATH) |" >> "$INDEX"

jq -nc \
  --arg date "$DATE" --arg topic "$TOPIC" --arg project "$PROJECT" \
  --arg path "$REL_PATH" --arg sources "$COUNT" \
  '{date:$date, topic:$topic, tool:"synthesis", project:$project, path:$path, sources:($sources|tonumber)}' \
  >> "$JSONL"
```

## Phase 5 — Telemetry

```bash
echo "$(date +%Y-%m-%d),dr-synthesize,$TOOL_CALLS,${COUNT}-sources" >> ~/.claude-assistant/logs/skill-performance.csv
```

---

## Invariants

- Synthesis NEVER overwrites or modifies raw inputs.
- The `## Source Reports` block is mandatory and must use absolute paths (not relative).
- If a source path no longer exists at synthesis time, **fail loud** — do not silently drop it.
- Synthesis is markdown only; no embedded raw-input content (paths are pointers, not copies).

## Smoke test

```bash
/dr-synthesize \
  ~/projects/working-notes/raw-inputs/2026-04-17_long-context-risks_claude.md \
  ~/projects/working-notes/raw-inputs/2026-04-17_long-context-risks_codex.md
```

Verify:
- Synthesis at `~/projects/working-notes/raw-inputs/2026-04-17_long-context-risks_synthesis.md` exists (same project folder as inputs)
- First section is `## Source Reports` with both absolute paths listed
- Frontmatter includes `project: working-notes`
- Raw inputs unchanged (compare hash before/after)
- INDEX.md row appended; INDEX.jsonl row appended (verify with `jq -c '.tool=="synthesis"' ~/research-archive/INDEX.jsonl | tail -1`)
- No `.md` content file created in `~/research-archive/`

## Customization Points

- **Project folder bases:** Default `~/projects/<name>/raw-inputs/`. Adjust to match your `/deep-research` routing config.
- **Central index location:** `~/research-archive/INDEX.md` and `INDEX.jsonl`. Should match the `/deep-research` skill's index paths.
- **Synthesis model:** Whatever model is available in your runtime — typically the same as your default Claude Code model. No special config needed; the synthesis runs in-context.

## Related skills

- `/deep-research` — produces the raw reports this skill consumes. Pass `--synthesize` to chain them automatically.
- `/prompt` — useful for refining the synthesis topic if `--topic` override is needed.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/chrisblattman/claudeblattman/contents/skills/dr-synthesize.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>chrisblattman/claudeblattman</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../claudeblattman.md">claudeblattman (Chris Blattman)</a></dd>
<dt><b>Category</b></dt><dd><code>literature</code></dd>
<dt><b>Field</b></dt><dd>social-sciences</dd>
<dt><b>Pipeline stages</b></dt><dd><code>literature-discovery</code> <code>literature-synthesis</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/chrisblattman/claudeblattman">⭐ chrisblattman/claudeblattman</a><br><img src="https://img.shields.io/github/stars/chrisblattman/claudeblattman?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/chrisblattman/claudeblattman/blob/main/skills/dr-synthesize.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/claudeblattman/dr-synthesize/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/claudeblattman.yml">edit on GitHub</a>.</p>
</div>

</div>
