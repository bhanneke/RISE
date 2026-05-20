<!-- DO NOT EDIT — auto-copied from skills/claudeblattman/details/tips-bookmarks.md -->

# `/tips-bookmarks`

Save and retrieve tips / bookmarks

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../claudeblattman/">claudeblattman (Chris Blattman)</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-04</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/chrisblattman/claudeblattman/contents/skills/tips-bookmarks.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/claudeblattman/tips-bookmarks/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/chrisblattman/claudeblattman/blob/main/skills/tips-bookmarks.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/chrisblattman/claudeblattman?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Tips Bookmarks
*v1.0 — Initial build.*

Pull X/Twitter bookmarks via `twitter-cli` and feed new ones into a tips pipeline log. Replaces the manual copy-paste-email loop for surfacing AI/dev tips you've bookmarked but haven't acted on.

Designed to run independently from a Gmail-based curate skill (e.g., `/tips-curate`) — a Twitter auth failure never blocks email-based tips processing, and vice versa.

### CRITICAL: No Permission Prompts

**Do NOT use Task agents or ToolSearch.** All required tools are pre-approved. Call them directly:

- Bash (for `twitter bookmarks --json`)
- Read, Edit, Write (for the state file and the tips log)

### Arguments

`$ARGUMENTS` can include:

- `dryrun` — Show what would be processed without saving or updating state
- `limit:N` — Max new bookmarks to process (default: 10)
- `init` — First-run initialization: mark all current bookmarks as seen, process only the 10 most recent

### Instructions

#### Step 0: Pre-Checks

1. **Test twitter-cli auth:**
   ```bash
   twitter bookmarks --json 2>/dev/null | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'OK: {len(d[\"data\"])} bookmarks')" 2>&1
   ```
   If this fails or prints an error: report `TWITTER AUTH EXPIRED — refresh cookies (see your twitter-cli setup notes).` and **stop**. Do NOT write to log or update state.

2. **Read state file** (`~/.claude-assistant/state/twitter-bookmarks-seen.json`):
   - If it doesn't exist and `init` was NOT given: report "No state file found. Run `/tips-bookmarks init` for first-time setup." and **stop**.
   - If it doesn't exist and `init` WAS given: proceed to Step 1 (init mode).
   - If it exists: load `seen_ids` list.

3. **Read tips log for dedup:** Read `~/.claude-assistant/tips/collected-tips-log.md` and note existing URLs (to avoid duplicates from both Twitter and email paths).

#### Step 1: Fetch Bookmarks

```bash
twitter bookmarks --json 2>/dev/null
```

Parse the JSON. The structure is:
```json
{
  "ok": true,
  "data": [
    {
      "id": "...",
      "text": "...",
      "author": {"name": "...", "screenName": "..."},
      "createdAt": "Fri Mar 06 18:33:43 +0000 2026",
      "urls": ["..."],
      "articleTitle": "...",
      "quotedTweet": {"text": "...", "author": {...}}
    }
  ]
}
```

**If `init` mode:**
- Write ALL bookmark IDs to `seen_ids` in state file
- Process only the 10 most recent (or `limit:N`) through Steps 2–3
- Report: "Initialized state with [N] existing bookmarks. Processing [M] most recent."

**Normal mode:**
- Filter out any bookmark whose `id` is already in `seen_ids`
- If zero new bookmarks: report "No new bookmarks since last run ([last_run date])." and **stop**.
- Take up to `limit:N` (default 10) new bookmarks for processing.

#### Step 2: Assess & Classify

For each new bookmark, apply the same classification taxonomy as a sibling Gmail-based curate skill:

| Classification | Criteria |
|---------------|----------|
| `worth-reviewing` | Claude Code tip, AI workflow technique, useful dev/productivity pattern, prompting strategy |
| `not-relevant` | Personal, social, general news, memes, not related to AI/dev workflows |
| `needs-manual` | Can't determine (video/audio only with no text, link-only tweet with no context) |

**Quality filter (for `worth-reviewing` items):**

- **High** — Novel + actionable + backed by real usage
- **Medium** — Interesting technique but may not apply directly
- **Low** — Already known, superficial, or too vague (treat as `not-relevant`)

**For High/Medium items, generate:**
- **Insight** (1–3 sentences): What's the technique? Be specific.
- **Action** (1 sentence): What should you change, try, or compare?
- **Tags**: 1–3 from: `[skill-design]` `[prompting]` `[agent-pattern]` `[tool]` `[workflow]` `[mcp]` `[context-management]` `[coding]` `[productivity]`

**Enrichment:** If a bookmark has non-X URLs in its `urls` array, attempt WebFetch for additional context. If WebFetch fails, classify based on tweet text alone.

#### Step 3: Present Recommendations

```
────────────────────
BOOKMARKS REVIEW ([N] new of [M] total)
────────────────────

RECOMMENDED:

  1. @handle — [tweet snippet] (High)
     Insight: [what's useful]
     Action: [what to try]

  2. @handle — [tweet snippet] (Medium)
     Insight: [insight]
     Action: [suggestion]

SKIP (not relevant):
  3. @handle — [tweet snippet] — [reason]

NEEDS YOUR HELP:
  4. @handle — [tweet snippet] — video/link only, no text context
────────────────────
Which to save? (e.g., "save 1,2" / "save all recommended" / "skip all")
```

**Wait for the user's response before proceeding.**

#### Step 4: Save Approved Items

Based on the user's response:

1. **Append approved items** to `~/.claude-assistant/tips/collected-tips-log.md`:

   ```markdown
   ### [Descriptive Title] [tag1] [tag2] [quality]
   - **Source:** @screenName on X ([date])
   - **Insight:** [1-3 sentence description]
   - **Action:** [Concrete next step]
   - **URL:** https://x.com/screenName/status/[tweet_id]
   ```

   Group under today's date heading. Check if today's date heading already exists.

2. **Update state file** — add ALL processed bookmark IDs (saved, skipped, and not-relevant) to `seen_ids`. Update `last_run` timestamp.

3. **If `dryrun`:** Skip saving and state update. Just show the report.

4. **Report:**
   ```
   Saved [N] tips to collected-tips-log.md.
   State updated: [total seen_ids] bookmarks tracked.
   [K] remaining in current bookmark fetch not yet processed.
   ```

#### Step 5: Log Performance

```bash
echo "$(date +%Y-%m-%d),tips-bookmarks,TOOL_CALLS,NOTES" >> ~/.claude-assistant/logs/skill-performance.csv
```

Replace TOOL_CALLS with exact count. Replace NOTES with volume info (e.g., "50-fetched-8-new-3-saved").

### State File Schema

`~/.claude-assistant/state/twitter-bookmarks-seen.json`:
```json
{
  "schema_version": 1,
  "last_run": "2026-03-14T12:00:00Z",
  "seen_ids": ["id1", "id2", "..."]
}
```

Prune `seen_ids` older than 90 days only if the list exceeds 1000 entries (bookmark IDs are small; no urgency to prune).

### Error Handling

| Condition | Behavior |
|-----------|----------|
| Auth failure (twitter-cli errors) | Print auth-expired message, stop. Do NOT update state. |
| State file missing (no `init`) | Prompt to run with `init` argument |
| Tips log missing | Create with standard header, continue |
| Zero new bookmarks | Report "no new bookmarks" with last_run date, stop |
| WebFetch fails on URL | Classify from tweet text alone |

### Examples

```
/tips-bookmarks init        # First run: initialize state, process 10 most recent
/tips-bookmarks             # Normal run: process new bookmarks since last run
/tips-bookmarks dryrun      # Preview without saving
/tips-bookmarks limit:5     # Process at most 5 new bookmarks
```

### Customization Points

- **State file location:** Default `~/.claude-assistant/state/twitter-bookmarks-seen.json`. Adjust to wherever you keep small per-skill state files.
- **Tips log location:** Default `~/.claude-assistant/tips/collected-tips-log.md`. Match to whatever path your `/tips-curate` (or equivalent) uses, so both Twitter and email paths feed the same log.
- **Classification taxonomy:** The `worth-reviewing` / `not-relevant` / `needs-manual` split and the High/Medium/Low quality filter are designed to mirror a sibling email-based curate skill. Edit the criteria table to match your own tip-quality bar.
- **Tag vocabulary:** Defined inline in Step 2. Add or remove tags so they line up with your tips log's existing tag conventions.
- **Default `limit`:** 10 new bookmarks per run. Lower it (e.g., 5) for noisier feeds; raise it for sparser ones.
- **`twitter-cli` binary:** Assumes a `twitter` CLI on `$PATH` that accepts `bookmarks --json`. Substitute any equivalent CLI that emits the same JSON shape (id, text, author, urls, articleTitle, quotedTweet).
