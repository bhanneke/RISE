<!-- DO NOT EDIT — auto-copied from skills/claudeblattman/details/deep-research.md -->

# `/deep-research`

Multi-agent deep research with paste-loop UX and subagent template

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../claudeblattman/">claudeblattman (Chris Blattman)</a></div><div><b>Category:</b> <code>literature</code></div><div><b>Field:</b> social-sciences</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-04</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>literature-discovery</code> · <code>literature-synthesis</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/chrisblattman/claudeblattman/contents/skills/deep-research.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/claudeblattman/deep-research/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/chrisblattman/claudeblattman/blob/main/skills/deep-research.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/chrisblattman/claudeblattman?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

<!-- deep-research v3 | sanitized from private skill -->
## /deep-research

*Federated deep-research workflow. Reports live in their project folder; a thin pointer INDEX in a central archive directory enables cross-project discovery.*

Run end-to-end deep research on a topic. Two invocation modes:

1. **Dispatch** — `/deep-research <topic> [--tool ...]` builds a DR-tuned prompt, routes to a project folder, dispatches to one or more research tools, and archives results there.
2. **Absorb** — `/deep-research --absorb [<file>]` scans `Projects/*/raw-inputs/` for unindexed files (drag-dropped from external tools) and processes them into canonical form.

**Automatic tools** (no paste-loop): Claude WebSearch subagent, OpenAI Codex CLI, Gemini 2.5 Pro CLI.
**Paste-loop tools** (opt-in only): ChatGPT, Grok, Perplexity, Gemini Deep Research (browser).

### Argument hint

`<topic> [--quick | --tool claude|codex|gemini|chatgpt|grok|perplexity|gemini-deep|both|all-auto] [--depth standard|deep] [--project <name>] [--no-prestructure] | --absorb [<file>] [--project <name>] [--synthesize]`

### Read first

- `deep-research-references/config.md` — paths, defaults, routing config
- `deep-research-references/dr-prompt-schema.md` — the 8-element prompt schema
- `deep-research-references/paste-loop-ux.md` — emit-and-exit messaging convention for paste-loop tools
- `deep-research-references/claude-subagent-template.md` — Claude WebSearch dispatch template

**Risk escalation:** Archive writes are Auto. Codex dispatches are Auto unless Phase 2's inline quota check returns RED (>85% of the 5-hour bucket); RED blocks unless `--force`.

---

### Dispatch mode

#### Phase 0.5 — Pre-structure via /prompt (mandatory; no skip on well-formed inputs)

**Invoke `/prompt` on every `$TOPIC`.** Even tight questions have implicit audience/context/output-shape that `/prompt` surfaces. The latency (5–15s) is worth the quality lift.

Procedure:
1. Skill tool call: `skill="prompt"`, args = `$TOPIC depth:deep hold` (the `hold` token tells `/prompt` to format and show but NOT execute)
2. Capture the formatted/restructured version from `/prompt`'s output
3. Show the user: "Restructured as:

[formatted]

Use this for the DR schema? [y/N/edit]"
4. If `y`: use formatted version as effective `$TOPIC` for Phase 1
5. If `edit`: open in `$EDITOR`, then proceed with edited version
6. If `n`: use raw `$TOPIC` (user override, not a skip-decision by the skill)

**The only skip condition is the explicit `--no-prestructure` CLI flag.** Do not infer a skip from input quality, length, or efficiency.

#### Phase 1 — Prompt build

Apply the 8-element DR Prompt Schema (`deep-research-references/dr-prompt-schema.md`). Default depth = `deep`. `--depth standard` drops elements 6+7 and the "research current best practices" preamble.

Print the full built prompt to stdout, then prompt:

```bash
read -p "Send this prompt? [y/N/edit]: " ans
case "$ans" in
  [yY]*) ;;
  edit)  ${EDITOR:-vi} /tmp/dr-prompt-<run-id>.md; exec $0 "$@" ;;
  *)     echo "Aborted."; exit 0 ;;
esac
```

#### Phase 1.4 — Project routing

Decide `$PROJECT_DIR` BEFORE Phase 1.5. Logic:

```bash
ROUTING_CONFIG=~/.claude-assistant/config/deep-research-routing.json

if [ -n "$PROJECT_FLAG" ]; then
  # Explicit --project <name> passed
  PROJECT_DIR=$(jq -r --arg p "$PROJECT_FLAG" '.routes[$p].path // empty' "$ROUTING_CONFIG")
  if [ -z "$PROJECT_DIR" ]; then
    if [ -d "$HOME/projects/$PROJECT_FLAG" ]; then
      PROJECT_DIR="$HOME/projects/$PROJECT_FLAG/raw-inputs/"
    else
      echo "No routing entry for '$PROJECT_FLAG'."
      read -p "Use ~/projects/working-notes/raw-inputs/ instead? [Y/n]: " ans
      [ "$ans" = "n" ] && exit 1
      PROJECT_DIR="$HOME/projects/working-notes/raw-inputs/"
    fi
  fi
else
  # Infer via keyword match against routing config
  MATCHES=$(jq -r --arg t "$TOPIC" '
    .routes | to_entries[] |
    select(.value.title_patterns // [] | any(. as $p | $t | ascii_downcase | contains($p))) |
    select(.value.exclude_patterns // [] | any(. as $p | $t | ascii_downcase | contains($p)) | not) |
    .key
  ' "$ROUTING_CONFIG")
  N_MATCHES=$(echo "$MATCHES" | grep -c .)

  case "$N_MATCHES" in
    1)
      PROJECT_KEY="$MATCHES"
      read -p "Topic matches project '$PROJECT_KEY'. File there? [Y/n/other]: " ans
      case "$ans" in
        n|N)        PROJECT_KEY="working-notes" ;;
        other)      read -p "Project name: " PROJECT_KEY ;;
        *)          ;;  # accept default
      esac
      ;;
    0)
      echo "No project match for topic. Save to working-notes? [Y/n/specify]"
      read -p "> " ans
      case "$ans" in
        n|N)        echo "Aborted."; exit 1 ;;
        specify)    read -p "Project name: " PROJECT_KEY ;;
        *)          PROJECT_KEY="working-notes" ;;
      esac
      ;;
    *)
      echo "Multiple project matches:"
      echo "$MATCHES" | nl
      read -p "Pick [1-N/other]: " pick
      PROJECT_KEY=$(echo "$MATCHES" | sed -n "${pick}p")
      ;;
  esac

  PROJECT_DIR=$(jq -r --arg p "$PROJECT_KEY" '.routes[$p].path' "$ROUTING_CONFIG")
fi

PROJECT_DIR="${PROJECT_DIR/#\~/$HOME}"
mkdir -p "$PROJECT_DIR"
```

#### Phase 1.5 — Archive prompt to project folder

Before any dispatch:

```bash
RUN_ID=$(date +%Y%m%d%H%M%S)-$(openssl rand -hex 3)
SLUG=$(echo "$TOPIC" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | cut -c1-50)
DATE=$(date +%Y-%m-%d)

cat > "/tmp/dr-prompt-$RUN_ID.md" <<EOF
---
date: $DATE
topic: $TOPIC
type: prompt
project: $PROJECT_KEY
run_id: $RUN_ID
---
EOF
cat /tmp/dr-built-prompt-$RUN_ID.txt >> "/tmp/dr-prompt-$RUN_ID.md"

cp "/tmp/dr-prompt-$RUN_ID.md" "$PROJECT_DIR/${DATE}_${SLUG}_prompt.md"
```

#### Phase 2 — Codex pre-flight (only if `--tool` includes codex)

Inline lightweight quota guard. **Two-tier only: GREEN / RED.**

Behavior: if `ccusage` + `jq` are available AND the reported quota is ≥ `THRESHOLD_RED`, BLOCK (unless `--force`). Otherwise proceed silently. Missing deps = missing signal = proceed (advisory, not mandatory; the Claude arm is the fallback anyway).

```bash
source ~/.claude-assistant/config/codex-thresholds.sh 2>/dev/null || {
  PRO_5H_TOKEN_BUDGET=400000
  THRESHOLD_RED=0.85
}

USAGE_RAW=$(ccusage codex window 5h --json 2>/dev/null | jq -r '.percent // .tokens // .tokens_used // empty' 2>/dev/null)
if [ -n "$USAGE_RAW" ] && [ "$USAGE_RAW" != "null" ]; then
  RED_HIT=$(awk -v p="$USAGE_RAW" -v b="$PRO_5H_TOKEN_BUDGET" -v t="$THRESHOLD_RED" \
    'BEGIN { n = (p > 100) ? p/b : (p > 1 ? p/100 : p); print (n >= t) ? 1 : 0 }')
  if [ "$RED_HIT" = "1" ] && [ -z "$FORCE" ]; then
    echo "RED: Codex 5h bucket >= ${THRESHOLD_RED}. Use --force or --tool claude."
    exit 1
  fi
fi
## Happy path: no output. Proceed to Phase 3.
```

#### Phase 3 — Dispatch

**`--tool claude`** — Spawn a subagent with `context:fork` using the template at `deep-research-references/claude-subagent-template.md`. Pass:
- Prompt path: `/tmp/dr-prompt-$RUN_ID.md`
- Schema path: `~/.claude/references/dr-prompt-schema.md`
- Output target: `/tmp/dr-claude-$RUN_ID.md`

The subagent uses WebSearch + WebFetch and writes its report to the output target. It does NOT report inline.

**`--tool codex`** — Single Bash call. **Pipe the prompt via stdin redirect** — do NOT pass it as a `-- "$(cat …)"` positional. The positional+`--` form has caused Codex CLI to fall into `Reading additional input from stdin...` and hang indefinitely.

```bash
"$CODEX_BIN" exec --model "$CODEX_MODEL" $CODEX_SANDBOX \
  $CODEX_UNATTENDED_FLAG \
  -o /tmp/dr-codex-$RUN_ID.md \
  < /tmp/dr-prompt-$RUN_ID.md \
  > /tmp/dr-codex-$RUN_ID.stdout 2>/tmp/dr-codex-$RUN_ID.stderr
CODEX_EXIT=$?
```

`CODEX_BIN`, `CODEX_MODEL`, `CODEX_SANDBOX`, and `CODEX_UNATTENDED_FLAG` come from `deep-research-references/config.md`.

**Permission denial handling.** Claude Code's sandbox may deny a Codex Bash call with a heuristic message about "executing code derived from untrusted research content," even when `Bash(*)` is in the allow-list. The fix: add explicit binary-path rules to `~/.claude/settings.json` → `permissions.allow` (see `deep-research-references/config.md` § Permission prerequisites).

If a permission denial still occurs at runtime, detect via the literal string "Permission for this action has been denied" in the tool result, then **fall back to paste-loop** for the Codex arm. Set `CODEX_OK=0` for Phase 3.5 and continue any other arms uninterrupted.

**`--tool gemini`** — Single Bash call to Gemini 2.5 Pro CLI (fully automatic; NOT the browser Deep Research product — that's `--tool gemini-deep`). Model pinning matters: the OAuth default is `gemini-2.5-flash-lite`, which is materially weaker.

```bash
"$GEMINI_BIN" -p "$(cat /tmp/dr-prompt-$RUN_ID.md)" -m gemini-2.5-pro \
  --output-format "$GEMINI_OUTPUT_FORMAT" \
  > /tmp/dr-gemini-$RUN_ID.json 2>/tmp/dr-gemini-$RUN_ID.stderr
GEMINI_EXIT=$?
jq -r '.response' /tmp/dr-gemini-$RUN_ID.json > /tmp/dr-gemini-$RUN_ID.md 2>/dev/null
```

If `$GEMINI_BIN` is empty, skip with note ("Gemini CLI not installed; run `npm install -g @google/gemini-cli`"). Do not silently fall back to paste-loop.

**`--tool chatgpt|grok|perplexity|gemini-deep`** (paste-loop, opt-in only). Save the prompt to `/tmp/dr-prompt-$RUN_ID.md` (already done in Phase 1.5). Print the paste-loop hint per `deep-research-references/paste-loop-ux.md`. **Exit cleanly. No inline wait.** When the user returns with the pasted file, they run `/deep-research --absorb`.

**Important — do NOT volunteer paste-loop arms.** Never add ChatGPT, Grok, Perplexity, or Gemini Deep Research as a "bonus arm" unless the user explicitly passed the flag (or used an unambiguous natural-language trigger like "include gemini deep research").

**`--tool both`** — Two **concurrent tool calls** in a single message: one Task spawn for the Claude subagent, one Bash for Codex. Does NOT include Gemini CLI. Do NOT use Bash `&` + `wait` (fragile error propagation).

**`--tool all-auto`** — Three **concurrent tool calls** in a single message: one Task (Claude subagent), two Bash (Codex, Gemini CLI). All automatic, no paste-loop.

#### Phase 3.5 — Hard exit-code gate

For each non-paste tool:

```bash
if [ "$CODEX_EXIT" -ne 0 ] || [ ! -s /tmp/dr-codex-$RUN_ID.md ]; then
  echo "Codex dispatch failed (exit=$CODEX_EXIT). stderr:"
  cat /tmp/dr-codex-$RUN_ID.stderr
  CODEX_OK=0
else
  CODEX_OK=1
fi
```

Same pattern for the Claude subagent (output file must exist + be non-empty). Synthesis includes only `*_OK=1` arms.

#### Phase 4 — Federated archive (write to project folder)

For each successful tool output:

```bash
DEST="$PROJECT_DIR/${DATE}_${SLUG}_${TOOL}.md"
cat > "$DEST" <<EOF
---
date: $DATE
topic: $TOPIC
tool: $TOOL
model: $MODEL
prompt_file: ${DATE}_${SLUG}_prompt.md
project: $PROJECT_KEY
run_id: $RUN_ID
---

EOF
cat "/tmp/dr-${TOOL}-$RUN_ID.md" >> "$DEST"
```

**INDEX update** (serialized AFTER all parallel arms complete — do not write from inside parallel tasks):

```bash
INDEX=~/research-archive/INDEX.md
INDEX_JSONL=~/research-archive/INDEX.jsonl

echo "| $DATE | $TOPIC | $TOOL | $MODEL | $PROJECT_KEY | $DEST |" >> "$INDEX"

jq -n --arg date "$DATE" --arg topic "$TOPIC" --arg tool "$TOOL" \
       --arg model "$MODEL" --arg project "$PROJECT_KEY" --arg path "$DEST" \
       --arg run_id "$RUN_ID" \
  '{date:$date, topic:$topic, tool:$tool, model:$model, project:$project, path:$path, run_id:$run_id}' \
  >> "$INDEX_JSONL"
```

**No mirror writes.** The project folder is the canonical location. The central archive holds only the index.

**Cleanup:**
```bash
find /tmp -name "dr-*-$RUN_ID*" -mtime +1 -delete
```

#### Phase 5 — Synthesis (opt-in, with `--synthesize`)

Thin wrapper that calls `/dr-synthesize <project-paths...>` as a subprocess. Synthesis writes to the SAME project folder as its primary input(s):

`$PROJECT_DIR/${DATE}_${SLUG}_synthesis.md`

`/dr-synthesize` enforces the mandatory `## Source Reports` header with absolute paths. Synthesis is a *new* file; never edits raw inputs. After write, append a synthesis row to INDEX.md/jsonl.

#### Phase 6 — Telemetry

```bash
echo "$(date +%Y-%m-%d),deep-research,$TOOL_CALLS,${TOOL}-${SLUG}" >> ~/.claude-assistant/logs/skill-performance.csv
```

If Codex was used, append to `codex-usage.csv`:
```bash
ROLLOUT=$(ls -t ~/.codex/sessions/$(date +%Y/%m/%d)/rollout-*.jsonl 2>/dev/null | head -1)
DELTA=$(jq -s 'map(.tokens_used // 0) | add' "$ROLLOUT" 2>/dev/null || echo "")
echo "$DATE,$RUN_ID,$WINDOW_BEFORE,$WINDOW_AFTER,$DELTA" >> ~/.claude-assistant/logs/codex-usage.csv
```

---

### Absorb mode

`/deep-research --absorb [<file>] [--project <name>] [--synthesize]`

For external Deep Research outputs (you ran ChatGPT / Grok / Perplexity / Gemini Deep Research in the browser, or any other tool). Two paths:

#### Path A — Drag-and-drop, then absorb

Drop one or more `.md` files into a project's `raw-inputs/` folder via your editor's file explorer (e.g., `~/projects/<paper-name>/raw-inputs/test.md`). Then in the integrated terminal:

```
/deep-research --absorb
```

The skill scans every `raw-inputs/` folder for `.md` files lacking canonical frontmatter (no `date:` + `topic:` + `tool:` + `run_id:` block). For each found file:

1. **Preview** first ~30 lines
2. **Prompt:**
   - `Topic / slug? [auto-suggest from filename]`
   - `Source tool? [chatgpt/codex/grok/perplexity/other]`
3. **Clean** if `chatgpt`: pipe through a ChatGPT-artifact stripper (PUA characters in the ``–`` range), if available
4. **Rename** to canonical pattern: `${DATE}_${SLUG}_${TOOL}.md` (preserving the project folder location)
5. **Prepend frontmatter:**
   ```
   ---
   date: <inferred-from-mtime-or-asked>
   topic: <slug>
   tool: <tool>
   ingested_from: <original-filename>
   project: <inferred-from-folder>
   run_id: absorb-$(date +%s)
   ---
   ```
6. **Append rows** to INDEX.md and INDEX.jsonl
7. **Report:** `Absorbed N file(s). Skipped M (already indexed).`

#### Path B — Single-file with explicit path

```
/deep-research --absorb /path/to/external-report.md --project "<paper-name>"
```

Same as Path A but processes one specified file. Moves it into `$PROJECT_DIR` after canonicalization.

#### Phase 5 — Synthesis (with `--synthesize`)

If `--synthesize` is passed, after absorbing call `/dr-synthesize` on the absorbed file(s).

---

### Defaults

- `--tool` default: `both` (Claude WebSearch + Codex in parallel). Both arms fully automatic. Codex arm is RED-gated per Phase 2 (5h bucket). For 3-arm automatic dispatch including Gemini 2.5 Pro CLI, pass `--tool all-auto`. Paste-loop arms (`chatgpt`, `grok`, `perplexity`, `gemini-deep`) are opt-in only — never volunteered.
- `--depth` default: `deep` (all 8 schema elements + "research current best practices" preamble)
- `--project` default: keyword inference; **if no match, prompt the user to pick** — do NOT silently fall back to `working-notes`.

**`--quick` shortcut:** One-flag override = `--tool claude --depth standard` (the cheap/fast mode). Combines with other flags: `--quick --project X` is valid.

**Individual overrides:** `--tool <name>` changes only the tool (depth stays `deep`). `--depth standard` lowers only depth (tool stays `both`).

---

### Smoke tests

**1. Routing inference + federated write:**
```bash
/deep-research "What are the top 3 risks of long-context agentic coding setups?" --tool claude
## Expect:
##   Phase 1 prints schema'd prompt; [y/N/edit] gate fires
##   Phase 1.4 keyword match prompts a project, or falls back to working-notes
##   Phase 1.5: prompt file at $PROJECT_DIR/<date>_<slug>_prompt.md
##   Phase 4: claude report at $PROJECT_DIR/<date>_<slug>_claude.md
##   INDEX.md and INDEX.jsonl have new pointer rows
##   research-archive/ contains NO .md content files (only INDEX.md, INDEX.jsonl)
```

**2. Absorb workflow:**
```bash
echo "fake report content" > "$HOME/projects/working-notes/raw-inputs/test-paste.md"
/deep-research --absorb
## Expect: prompts for slug + tool, renames to canonical, adds frontmatter, INDEX updated
```

**3. Cross-project discovery:**
```bash
## Open ~/research-archive/INDEX.md, find-in-file for any topic keyword
## Expect: row visible, path clickable to project folder
```

---

### Customization Points

- **Routing config:** `~/.claude-assistant/config/deep-research-routing.json`. Maps project keys → `path` + `title_patterns` + `exclude_patterns` for keyword inference.
- **Project folder layout:** Default base is `~/projects/<name>/raw-inputs/`. Adjust if your projects live elsewhere (e.g., `~/Documents/research/...`).
- **Central index location:** `~/research-archive/` holds only `INDEX.md` and `INDEX.jsonl`. Should stay under 1 MB indefinitely.
- **Codex thresholds:** `~/.claude-assistant/config/codex-thresholds.sh` is the single source of truth for `PRO_5H_TOKEN_BUDGET` and `THRESHOLD_RED`. Recalibrate quarterly.
- **CLI binaries:** Set `CODEX_BIN`, `GEMINI_BIN` paths in `deep-research-references/config.md` to match your install.
- **ChatGPT artifact stripper:** Optional Python helper invoked during `--absorb` for ChatGPT exports (PUA character range ``–``). Skip if you don't ingest ChatGPT outputs.
