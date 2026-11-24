<!-- DO NOT EDIT — auto-copied from skills/claudeblattman/details/done.md -->

# `/done`

Close out current work by saving decisions, unresolved tasks, useful artifacts, a session log and a current-state handoff for the next session.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../claudeblattman/">claudeblattman (Chris Blattman)</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-11-18</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/chrisblattman/claudeblattman/contents/starter-kit-source/skills/done/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/claudeblattman/done/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/chrisblattman/claudeblattman/blob/main/starter-kit-source/skills/done/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/chrisblattman/claudeblattman?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Save the session and handoff

A clear wrap-up request authorizes ordinary reversible continuity writes to the task's unambiguous working folder. Capture what happened; do not rerun the task or infer completion from silence. This public workflow uses the project-oriented capture shared with the live Codex adaptation. It does not require a private router, global log, cleanup script or terminal integration.

### 1. Resolve the destination

Read applicable project instructions, the existing `HANDOFF.md`, and relevant recent log entries. Use the user's named destination first. Otherwise use the actual task folder, not merely the desktop app's launch directory. An existing handoff in the current task's subfolder takes precedence over a stale global active-project pointer.

If the project has an active-subproject record, use it only when its target exists, is still relevant to this session, and is fresh under that project's policy. Permanent does not mean relevant to every topic. Do not overwrite an unrelated subproject's handoff. When the session is broader than an existing scoped snapshot, append to the project log and preserve that snapshot unless the user clearly asks to update it. If the destination is materially ambiguous, resolve it before writing. Do not ask for confirmation again when the user has already named the destination.

Default outputs are `HANDOFF.md` and sibling `SESSION_LOG.md`. Respect explicit alternate paths and logging opt-outs in project instructions. Global logs are optional configured destinations, not defaults; never create a personal global logging system on your own.

### 2. Extract and preserve useful work

Capture the current objective and status, accepted decisions and active constraints, consequential rejected approaches, unresolved questions, blockers, tests actually run, key files, and concrete follow-ups. Keep the most important next action prominent. Distinguish completed work from suggestions and unverified claims. Preserve unrelated unfinished tasks and other sessions' active constraints from the existing handoff.

Save substantial unsaved working artifacts, such as a draft or council report that exists only in this conversation, in the project's existing working-notes area (default `working-notes/`). Use unique dated names and link existing files instead of duplicating them. Keep artifacts with the project they belong to; do not collect private material into an unrelated public repository.

`quick` abbreviates narrative and optional artifact scanning, but still preserves necessary continuity, decisions, constraints and next actions. A brief lookup with nothing to hand off needs no files. `retro` explicitly adds the watch-list check; it never runs just because a session was long.

### 3. Save the history and current snapshot

Read the templates and write procedure. Obtain one timezone-precise `CAPTURE_ID` from the clock and reuse it across destinations and retries. Include `SESSLOG:<CAPTURE_ID>` in the dated log entry and handoff. Use the bundled continuity writer for conflict-checked atomic writes; it needs only Python 3's standard library.

Append the session entry to `SESSION_LOG.md` at the bottom, preserving existing ordering and content. Record the origin of new constraints and links to saved artifacts. Check for the exact capture marker before a retry in each destination; a successful write to one log does not prove another destination was written.

Update `HANDOFF.md` as a bounded **current-state snapshot**, never an appended transcript. Include `<!-- LIFECYCLE: snapshot-only -->`. Aim for roughly 30 lines, but preserve necessary continuity rather than obeying a rigid cap. Put historical detail in the session log. Archive an old snapshot when project policy requires it. The log must be saved successfully before replacing the snapshot; on a partial failure, retain the same capture ID and report what remains.

Capture the file hash when reading the version used to prepare each write. Never refresh the expected hash without reconciling the prepared content. On a conflict, reread, reconcile and retry with the new hash; do not blindly force an overwrite or remove another writer's lock. The helper coordinates its own writers; it cannot control every editor or cloud-sync process, so inspect sync conflicts and verify the result too.

### 4. Verify and report

Reopen the intended outputs. Verify the capture marker, next action, artifact links, and preservation of other active work. Report the actual paths, the next action, and any incomplete write. Tell the user to open the project in a new session and ask the agent to read the handoff.

No commit, push, publication, email, global-instruction change, automatic rule promotion, scratch deletion or log pruning is implied by `/done`. Existing logs can feed `/tips-integrate` when the user later requests it; capture alone does not launch that workflow.
