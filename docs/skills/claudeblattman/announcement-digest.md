<!-- DO NOT EDIT — auto-copied from skills/claudeblattman/details/announcement-digest.md -->

# `/announcement-digest`

Triage and digest announcements / newsletters / Slack-equivalent feeds

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

# Announcement Digest
# Adapt for your source — swap the @[SOURCE] label, names, and classification rules.
# This is a sanitized version of a working school-email digest skill.
# Full walkthrough: https://claudeblattman.com/workflows/school-digest/

*v1.0 — Announcement email digest skill*

Compile a digest of high-volume announcement emails from a single source (school, employer, nonprofit, professional association). Extract what matters, skip the noise, send a summary.

## Prerequisites

- **Gmail MCP** — for searching and reading emails
- **Gmail label + filter** — all source emails auto-labeled (e.g., `@School`, `@CompanyNews`)
- **Classification rules** — a config file with your calibrated rules (see walkthrough)
- **send-email.py** or equivalent — for sending the compiled digest

## Config & State Files

- **Rules:** `[YOUR_CONFIG_PATH]/digest-rules.md`
- **State:** `[YOUR_STATE_PATH]/digest-state.json`

State file tracks: `last_digest_date`, `digest_count`, `reported_message_ids`, `reported_message_ids_ttl_days` (default 30).

## Execution Steps

### Step 1: Read State & Check Frequency

1. Read `digest-state.json`.
2. If `last_digest_date` is not null and fewer than 2 days have passed:
   - Output: "Nothing new since [last_digest_date]. Next digest available [date]."
   - **Exit.**
3. Store `digest_count` (needed for first-time intro check at Step 5).

### Step 2: Fetch Labeled Emails

1. Compute lookback date: `last_digest_date` if set, otherwise 14 days ago.
2. Search Gmail: `label:[YOUR_LABEL] after:[lookback_date in YYYY/MM/DD]`
   - **Do NOT use `is:unread`** — labeled emails may or may not be marked read. Query by date range.
   - Page through all results (follow `next_page_token`).
3. Filter out any message IDs already in `reported_message_ids`.
4. If no new emails remain, exit with message.

### Step 3: Fetch Email Content

1. For each new message, fetch full content via `get_gmail_message_content`.
   - Fetch in parallel batches of 10.
2. Group messages by Gmail thread ID. Keep only the most recent non-you message per thread.
3. Accumulate total word count across all fetched message bodies.
4. **Prune `reported_message_ids`**: Remove IDs older than `reported_message_ids_ttl_days`.

### Step 4: Classify Each Email

Read your rules config for the full rule set. For each email (or thread), apply classification in this order:

#### 4a. Skip Check
Apply SKIP rules first. If any match, mark as `skip` and record `skip_reason`.

#### 4b. Source Assignment
Determine which sub-category the email belongs to (e.g., which child's school, which department, which program).

#### 4c. Urgency Classification
Apply rules from config using this priority order:
1. **Sender pattern override:** Personal sender (not `noreply@`) → HIGH
2. **HIGH keyword match** in subject + first 200 chars → HIGH
3. **LLM extraction** for everything else:

> Extract from this email. Return as JSON.
> (1) category: action_required / calendar_event / fyi / skip
> (2) urgency: high / medium / low
> (3) summary: 1-2 sentences of what you need to know
> (4) deadline: specific date/time if any, else null
> (5) deadline_quote: verbatim text from email stating the date/deadline — copy exact wording, do not paraphrase. null if no deadline.
> (6) skip_reason: if skip, one phrase why

4. **HIGH keyword overrides LLM urgency** upward (never downward).
5. **SKIP keyword overrides to skip** unless LLM said `action_required`.

### Step 4.5: Write Classified Artifact

Write full classified data to `/tmp/digest-classified.json`. This serves as:
- A **compaction safeguard** — if context is lost, re-compose from this file
- A **debug artifact** — review classification accuracy after the fact

### Step 5: Compose Digest

Format as plain text. Structure:

```
[YOUR SOURCE] EMAIL DIGEST
[date range]
Compressed ~[W] words across [N] emails ([M] threads) into this digest.
──────────────────────────────

[CATEGORY 1]

▶ ACTION ITEMS
  • [summary] — deadline: [date]
    Source: "[deadline_quote]"

📅 UPCOMING
  • [event/date]

ℹ️ FYI
  • [1-line summary]


[CATEGORY 2]

▶ ACTION ITEMS
  ...

+ [N] lower-priority items not shown
──────────────────────────────
```

**Rules:**
- Action items (HIGH) first, deadlines noted inline
- For HIGH items with a `deadline_quote`, include: `Source: "[deadline_quote]"` — makes factual errors visible
- Calendar events (MEDIUM) second
- FYI (LOW) third, 1 line each
- Omit empty sections
- **First-time send** (if `digest_count` was 0): Prepend intro explaining what this automated digest is and who it's from.

### Step 6: Save State & Send

1. **Write state file FIRST** (before sending):
   - Add ALL processed message IDs to `reported_message_ids` (including skipped)
   - Set `last_digest_date` to today
   - Increment `digest_count`

2. **Send the digest** via your preferred method.

3. **Do NOT mark source emails as read.** The digest is additive — it doesn't replace checking the source.

### Step 7: Log Performance

Log tool call count, duration, and volume for future optimization.

## Edge Cases

- **No emails:** Exit with message at Step 2.
- **All already reported:** Exit with message at Step 2.
- **Send failure after state write:** State is already saved (prevents duplicate digests). Log the error and retry manually.

## What This Skill Does NOT Do

- Does not mark emails as read
- Does not apply Gmail labels
- Does not modify any emails

## Building Your Own Rules Config

The classification rules are the hardest part. Don't try to write them upfront — calibrate from real data:

1. Pull 20 recent emails from your source
2. Rate each: action_required / calendar / fyi / skip
3. Note where you disagree with your own first instinct
4. Pull 30 more and refine
5. Write the rules that emerge

See the [full walkthrough](https://claudeblattman.com/workflows/school-digest/) for the calibration method.

---

*Sanitized from a working skill. Adapt the label, categories, and rules for your source.*


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/chrisblattman/claudeblattman/contents/skills/announcement-digest.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>chrisblattman/claudeblattman</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../claudeblattman.md">claudeblattman (Chris Blattman)</a></dd>
<dt><b>Category</b></dt><dd><code>literature</code></dd>
<dt><b>Field</b></dt><dd>general</dd>
<dt><b>Pipeline stages</b></dt><dd><code>literature-discovery</code> <code>literature-synthesis</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/chrisblattman/claudeblattman">⭐ chrisblattman/claudeblattman</a><br><img src="https://img.shields.io/github/stars/chrisblattman/claudeblattman?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/chrisblattman/claudeblattman/blob/main/skills/announcement-digest.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/claudeblattman/announcement-digest/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/claudeblattman.yml">edit on GitHub</a>.</p>
</div>

</div>
