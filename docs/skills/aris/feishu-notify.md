<!-- DO NOT EDIT — auto-copied from skills/aris/details/feishu-notify.md -->

# `feishu-notify`



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
name: feishu-notify
description: "Send notifications to Feishu/Lark. Internal utility used by other skills, or manually via /feishu-notify. Supports push-only (webhook) and interactive (bidirectional) modes. Use when user says \"发飞书\", \"notify feishu\", or other skills need to send status updates."
argument-hint: [message-text]
allowed-tools: Bash(curl *), Bash(cat *), Read, Glob
---

# Feishu/Lark Notification

Send a notification: **$ARGUMENTS**

## Overview

This skill provides Feishu/Lark integration for ARIS. It is designed as an **internal utility** — other skills call it at key events (experiment done, review scored, checkpoint waiting). It can also be invoked manually.

**Zero-impact guarantee**: If no `feishu.json` config exists, this skill does nothing and returns silently. All existing workflows are completely unaffected.

## Configuration

The skill reads `~/.claude/feishu.json`. If this file does not exist, **all Feishu functionality is disabled** — skills behave exactly as before.

### Config Format

```json
{
  "mode": "push",
  "webhook_url": "https://open.feishu.cn/open-apis/bot/v2/hook/YOUR_WEBHOOK_ID",
  "interactive": {
    "bridge_url": "http://localhost:5000",
    "timeout_seconds": 300
  }
}
```

### Modes

| Mode | `"mode"` value | What it does | Requires |
|------|----------------|--------------|----------|
| **Off** | `"off"` or file absent | Nothing. Pure CLI as-is | Nothing |
| **Push only** | `"push"` | Send webhook notifications at key events. Mobile push, no reply | Feishu bot webhook URL |
| **Interactive** | `"interactive"` | Full bidirectional. Approve/reject from Feishu, reply to checkpoints | [feishu-claude-code](https://github.com/joewongjc/feishu-claude-code) running |

## Workflow

### Step 1: Read Config

```bash
cat ~/.claude/feishu.json 2>/dev/null
```

- **File not found** → return silently, do nothing
- **`"mode": "off"`** → return silently, do nothing
- **`"mode": "push"`** → proceed to Step 2 (push)
- **`"mode": "interactive"`** → proceed to Step 3 (interactive)

### Step 2: Push Notification (webhook)

Send a rich card to the Feishu webhook:

```bash
curl -s -X POST "$WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d '{
    "msg_type": "interactive",
    "card": {
      "header": {
        "title": {"tag": "plain_text", "content": "TITLE"},
        "template": "COLOR"
      },
      "elements": [
        {"tag": "markdown", "content": "BODY"}
      ]
    }
  }'
```

**Card templates by event type:**

| Event | Title | Color | Body |
|-------|-------|-------|------|
| `experiment_done` | Experiment Complete | `green` | Results table, delta vs baseline |
| `review_scored` | Review Round N: X/10 | `blue` (≥6) / `orange` (<6) | Score, verdict, top 3 weaknesses |
| `checkpoint` | Checkpoint: Waiting for Input | `yellow` | Question, options, context |
| `error` | Error: [type] | `red` | Error message, what failed |
| `pipeline_done` | Pipeline Complete | `purple` | Final summary, deliverables |
| `custom` | Custom | `blue` | Free-form message from $ARGUMENTS |

**Return immediately after curl** — push mode never waits for a response.

### Step 3: Interactive Notification (bidirectional)

Interactive mode uses [feishu-claude-code](https://github.com/joewongjc/feishu-claude-code) as a bridge:

1. **Send message** to the bridge:
   ```bash
   curl -s -X POST "$BRIDGE_URL/send" \
     -H "Content-Type: application/json" \
     -d '{"type": "EVENT_TYPE", "title": "TITLE", "body": "BODY", "options": ["approve", "reject", "custom"]}'
   ```

2. **Wait for reply** (with timeout):
   ```bash
   curl -s "$BRIDGE_URL/poll?timeout=$TIMEOUT_SECONDS"
   ```
   Returns: `{"reply": "approve"}` or `{"reply": "reject"}` or `{"reply": "user typed message"}` or `{"timeout": true}`

3. **On timeout**: Fall back to `AUTO_PROCEED` behavior (proceed with default option).

4. **Return the user's reply** to the calling skill so it can act on it.

### Step 4: Verify Delivery

- **Push mode**: Check curl exit code. If non-zero, log warning but do NOT block the workflow.
- **Interactive mode**: If bridge is unreachable, fall back to push mode (if webhook configured) or skip silently.

## Helper Function (for other skills)

Other skills should use this pattern to send notifications:

```markdown
### Feishu Notification (if configured)

Check if `~/.claude/feishu.json` exists and mode is not "off":
- If **push** mode: send webhook notification with event summary
- If **interactive** mode: send notification and wait for user reply
- If **off** or file absent: skip entirely (no-op)
```

**This check is always guarded.** If the config file doesn't exist, the skill skips the notification block entirely — zero overhead, zero side effects.

## Event Catalog

Skills send these events at these moments:

| Skill | Event | When |
|-------|-------|------|
| `/auto-review-loop` | `review_scored` | After each round's review score |
| `/auto-review-loop` | `pipeline_done` | Loop complete (positive or max rounds) |
| `/auto-paper-improvement-loop` | `review_scored` | After each round's review score |
| `/auto-paper-improvement-loop` | `pipeline_done` | All rounds complete |
| `/run-experiment` | `experiment_done` | Screen session finishes |
| `/idea-discovery` | `checkpoint` | Between phases (if interactive) |
| `/idea-discovery` | `pipeline_done` | Final report ready |
| `/monitor-experiment` | `experiment_done` | Results collected |
| `/research-pipeline` | `checkpoint` | Between workflow stages |
| `/research-pipeline` | `pipeline_done` | Full pipeline complete |

## Key Rules

- **NEVER block a workflow** because Feishu is unreachable. Always fail open.
- **NEVER require Feishu config** — all skills must work without it.
- **Config file absent = mode off.** No error, no warning, no log.
- **Push mode is fire-and-forget.** Send curl, check exit code, move on.
- **Interactive timeout = auto-proceed.** Don't hang forever waiting for a reply.
- **Respect `AUTO_PROCEED`**: In interactive mode, if the user doesn't reply within timeout, use the same auto-proceed logic as the calling skill.
- **No secrets in notifications.** Never include API keys, tokens, or passwords in Feishu messages.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/feishu-notify/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>wanshuiyin/Auto-claude-code-research-in-sleep</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../aris.md">ARIS skills</a></dd>
<dt><b>Category</b></dt><dd><code>infra</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-05-18</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep">⭐ wanshuiyin/Auto-claude-code-research-in-sleep</a><br><img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/aris/feishu-notify/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/aris.yml">edit on GitHub</a>.</p>
</div>

</div>
