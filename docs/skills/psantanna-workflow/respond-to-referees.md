<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/respond-to-referees.md -->

# `/respond-to-referees`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../psantanna-workflow/">Pedro Sant'Anna's Claude Code Workflow</a></div><div><b>Category:</b> <code>revision</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-04</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>revision-editing</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/respond-to-referees/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/psantanna-workflow/respond-to-referees/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/respond-to-referees/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Respond to Referees

Produce a complete response-to-referees document by cross-referencing the referee report against the revised manuscript. Classify every concern, draft a courteous response for each, and flag anything unaddressed before submission.

### Inputs

- `$0` — path to the referee report
- `$1` — path to the revised manuscript

Supported formats and how to read them. In the commands below, `FILE` stands for the input path being converted — either `$0` (referee report) or `$1` (revised manuscript). Always use `mktemp` for the temp file (not a predictable `/tmp/...` name) so paths with spaces and concurrent runs don't collide, and so untrusted `FILE` paths can't clobber other temp files via symlink races.

| Format | How to extract text |
| --- | --- |
| `.tex`, `.qmd`, `.md`, `.txt` | Read directly with the `Read` tool. |
| `.pdf` | `TMP=$(mktemp --suffix=.txt) && pdftotext "FILE" "$TMP"` (poppler-utils; use `mktemp -t ...` on macOS if `--suffix` is unsupported). Grep `"$TMP"`. |
| `.docx` | `TMP=$(mktemp --suffix=.txt) && pandoc "FILE" -t plain -o "$TMP"` (or `docx2txt "FILE" "$TMP"`). Grep `"$TMP"`. |
| `.html` | `TMP=$(mktemp --suffix=.txt) && pandoc "FILE" -t plain -o "$TMP"`. Grep `"$TMP"`. |

If a required tool is missing or extraction fails, ask the user to provide a plain-text version (`.txt` or `.md`) and stop.

### Workflow

#### Step 0: Convert Inputs to Plain Text

Before any parsing or grep, convert non-text inputs (`.pdf`, `.docx`, `.html`) to plain text using the table above. Keep both the temp text file (for grep) and the original (for citation page references).

#### Step 1: Parse the Referee Report

1. Read the report end-to-end.
2. Decompose into discrete numbered concerns. Common patterns:
   - Numbered or bulleted enumerations ("1.", "(a)", "Comment 1", etc.).
   - Section headers ("Major comments", "Minor comments").
   - Implicit concerns embedded in prose paragraphs — extract these too.
3. For each concern, capture:
   - **Concern ID** (R{n}.{m} = referee n, comment m)
   - **Severity** the referee assigned (major / minor / typographic)
   - **Verbatim quote** of the most representative sentence (~25 words max)
   - **One-line summary** in your own words

#### Step 2: Locate Each Concern in the Revised Manuscript

For every concern:

1. Extract the key terms from the referee's wording.
2. `Grep` the **plain-text version** of the revised manuscript for those terms (and synonyms). Note: Grep only works on text — if the original was any non-text format (for example, `.pdf`, `.docx`, or `.html`), grep the converted temp file from Step 0.
3. `Read` the surrounding context (±20 lines) to confirm the change addresses the concern.
4. Note the page/section/line numbers in the **original** file (not the temp file) for the response document.

#### Step 3: Classify Coverage

Assign one of four labels to each concern:

| Label | Meaning |
| --- | --- |
| **Addressed** | The revision directly resolves the concern with a specific change you can point to. |
| **Partially addressed** | The revision moves in the requested direction but does not fully resolve the concern (e.g., added one robustness check when the referee asked for two). |
| **Deferred** | The revision does not change the manuscript on this point but the response will explain why (out of scope, separate paper, conflicting referee, etc.). |
| **Disagreement** | The author respectfully disagrees with the referee's premise. The response will explain the reasoning and any compromise. |

If you cannot find any evidence of a revision OR a deliberate decision to defer/disagree, mark the concern **UNADDRESSED — REQUIRES AUTHOR INPUT** and surface it in the warning summary at the end.

#### Step 4: Draft Each Response

For every concern, write a 3–6 sentence response in this structure:

1. **Acknowledge** the concern (one sentence, no paraphrasing flattery).
2. **State the change** (or the reason for not changing).
3. **Point to the location** in the revised manuscript (page, section, line range, or table/figure number).
4. **(Optional) Justify** the choice if the change diverges from the referee's exact ask.

Tone conventions: courteous but firm; never defensive; never quote the referee back at length; use "we" for the author team; avoid "the referee is wrong" — prefer "we respectfully retain our original framing because…".

#### Step 5: Produce the Response Document

Write the output to `response-to-referees.md` (matching the template filename) or a path the user specifies. Use the structure in `templates/response-to-referees.md`:

1. **Header** — journal, manuscript ID, revision round, date.
2. **Cover paragraph** — one paragraph thanking the editor and referees, summarizing the major changes at a high level.
3. **Per-referee sections** — for each referee, a numbered list of responses produced in Step 4.
4. **Concern matrix** — at the end, a single table summarizing every concern, classification, and response location for editor convenience.

#### Step 5.5: Post-Flight Verification (MANDATORY, CoVe)

The response document's most hallucination-prone content is the set of "we added X on page Y" claims. Hallucinating these gets a paper desk-rejected on sight. Before declaring the response document final, run the Post-Flight Verification protocol from [`.claude/rules/post-flight-verification.md`](../../rules/post-flight-verification.md).

**Steps:**

1. **Extract revision-location claims** — every "we added / we modified / we revised X (page Y, line Z / Section N)" assertion in the response document.
2. **Generate verification questions** — "Does the revised manuscript actually contain the revision claimed at page Y, line Z? Does it match the description?"
3. **Spawn `claim-verifier`** via `Task` with `subagent_type=claim-verifier` and `context=fork`. Hand it: the claims table, the verification questions, the path to the revised manuscript. Do NOT include the response draft.
4. **Reconcile:** PASS → attach green block. PARTIAL / FAIL → rewrite the affected response entries using the verifier's evidence. A response that says "we added robustness check X on page 34" when X is actually on page 27 (or not at all) is worse than a "Deferred" classification.

Downgrade to the classification the evidence supports:

- Claim verified at location → `Addressed`
- Claim verified at different location → update the location in the response
- Claim not verifiable in manuscript → downgrade to `Partially addressed` or `Deferred` with an honest rationale

Opt-out: `--no-verify` flag. Not recommended — the referee will run this check themselves.

#### Step 6: Warning Summary (MANDATORY)

After the document is written, include this summary in your **final chat message to the user** (NOT inside the response document):

```
### Unaddressed concerns requiring author input

- R1.3: [summary] — no evidence of revision found
- R2.7: [summary] — flagged as deferred but no rationale yet drafted
```

If everything is covered, the final message should say `All concerns addressed or explicitly classified.`

### Output Files

- `response-to-referees.md` — the deliverable (filename matches `templates/response-to-referees.md`)
- (Optional) `response-to-referees-matrix.csv` — machine-readable concern-to-response mapping for tracking across revisions

### Pre-submission rehearsal

**Tip.** Before drafting your response, consider running `/review-paper --peer --r2 <journal>` on the *revised* manuscript first. It simulates the next referee round against your revisions — catching the "Resolved / Partial / Not addressed" classification mistakes before the real referee does. See [`.claude/skills/review-paper/SKILL.md`](../review-paper/SKILL.md).

### Cross-References

- For first-pass manuscript review **before** receiving referee comments, use `/review-paper`.
- For substantive content audits during revision, use `/slide-excellence` (works on `.tex` manuscripts via the domain-reviewer agent).
- Save the response to `quality_reports/` if you want a permanent record alongside other quality reports.

### Verification

Before reporting completion:

1. Confirm every concern has a classification (no orphans).
2. Confirm every "Addressed" or "Partially addressed" classification cites a specific page/section/line.
3. Confirm the warning summary was emitted (even if empty).
4. Confirm the cover paragraph names the journal and manuscript ID correctly.
