# 3. First workflow — turn a PDF into a curator note

> *Hand the agent a paper, get back a structured note, verify it,
> commit it.*

## Why this step matters

The single most useful first task with a coding agent is **reading
a paper for you and producing a structured summary you can
verify in five minutes**. It exercises the full loop — file
input, agent reasoning, file output, human verification, version
control — on a low-stakes deliverable. It is also exactly how the
[papers catalog](../papers/index.md) of this site is maintained.

At the end of this step you will have:

- A PDF of a paper in your repository.
- A markdown note at `notes/<citekey>.md` with a structured
  summary the agent produced.
- A verified commit of both files to GitHub.

Time: ~15–20 minutes (most of which is reading the PDF yourself
to verify).

---

## 3.1 Pick a paper and drop it in the repo

Pick a paper you actually want to read — ideally one in your own
research area, so the verification step is real work, not
make-believe.

In a Finder / Explorer window (or via `cp` on the command line),
drop the PDF into your manuscript repository under a `papers/`
subdirectory. If the directory does not exist, create it:

```bash
cd ~/Projects/crypto-momentum-paper
mkdir -p papers notes
# Then drag the PDF into papers/ via Finder, or:
cp ~/Downloads/some-paper.pdf papers/
ls papers/
```

The exact filename does not matter for the agent step (the agent
will read whatever is there); but a convention like
`<lastname><year><word>.pdf` (e.g., `ghareeb2026robin.pdf`) makes
later citation work easier.

> ![Screenshot placeholder: Finder showing PDF dropped into papers/]
> *Drop screenshot at `docs/assets/screenshots/finder-papers-dir.png` and replace this line.*

---

## 3.2 Start the agent in the repository

```bash
cd ~/Projects/crypto-momentum-paper
claude     # or `codex` if that's what you installed
```

You should see the agent's welcome screen. Confirm it sees the
papers directory:

```text
list the files under papers/
```

The agent reports the PDF you just dropped in.

---

## 3.3 Ask for a structured note

Type a single, bounded request. Be specific about both the
**format** and the **constraints**:

```text
Read papers/<your-pdf-filename>. Extract the bibliographic
metadata (authors, title, year, venue, DOI if present) and produce
a 200-word structured note with these sections:

1. Summary — what the paper is about, in 2-3 sentences.
2. Contribution — what is new vs. prior work.
3. Method — how the claim is established (data, identification,
   model).
4. Key quotes — 2-3 verbatim quotes (in quotation marks) that
   capture the central claim.
5. Critique — one open question or weakness.

Save the result as notes/<lastname><year><word>.md with a YAML
front-matter block containing the bibliographic metadata.
Do not invent citations, DOIs, or quotes — if you cannot find
something in the PDF, write "not stated".
```

The agent will:

1. Read the PDF (it may print a "reading file…" status).
2. Show you the proposed `notes/...md` content.
3. **Ask for permission** to write the file. Approve.

> ![Screenshot placeholder: agent showing proposed note + permission prompt]
> *Drop screenshot at `docs/assets/screenshots/agent-note-permission.png` and replace this line.*

If the agent invents a section or rambles past 200 words, push
back in the chat:

```text
Re-do it. Strict 200-word limit, drop the editorial commentary,
keep only the five sections I asked for.
```

Agents do what you tell them; vague instructions produce vague
output. The discipline of bounded, specific requests is the most
important skill in agentic work.

---

## 3.4 Verify the note

This is the step that distinguishes augmentation from credulity.
**Open the PDF yourself** in your normal reader, and read at least:

- The title and author block (do they match the YAML front-matter
  the agent wrote?).
- The abstract (does the agent's *Summary* section match what the
  abstract actually says?).
- One of the *Key quotes* — search the PDF for that quote string
  to confirm it appears verbatim.

The most common failure modes you will catch:

- **Citation invention.** The agent attaches a DOI it could not
  actually find in the PDF — verify against the PDF cover page or
  CrossRef.
- **Subtly wrong quotes.** The agent paraphrases a passage and
  leaves it in quotation marks. Run a literal text search.
- **Summary drift.** The agent foregrounds a minor finding in the
  paper as if it were the headline result.

If any of these are present, ask for a fix:

```text
The DOI you wrote is not on page 1 of the PDF. Re-check, and if
you cannot find it, leave the doi field empty.
```

---

## 3.5 Commit the result

When the note is verified, ask the agent to commit:

```text
Stage papers/<filename>.pdf and notes/<citekey>.md and commit
with a clear message. Then push.
```

The agent shows the staged files and the proposed commit message,
asks permission, and (after you approve) runs `git add`,
`git commit`, and `git push`.

> ![Screenshot placeholder: git commit message preview from agent]
> *Drop screenshot at `docs/assets/screenshots/agent-commit-preview.png` and replace this line.*

Visit your repo on GitHub. Your new files are there. If you set up
Overleaf sync in [step 1.5](manuscript.md#15-connect-overleaf-to-github),
click **Sync → Pull from GitHub** in Overleaf and the new files
appear there too.

---

## What you have now

- A working agent loop in a real repository.
- A verified structured note, committed to GitHub.
- A concrete sense of which agent steps need close supervision
  (citations, quotes) and which can be trusted (file listing,
  bibliographic extraction, commit messages).

---

## Next workflows to try

The same pattern — *bounded request → agent produces artifact →
human verifies → commit* — scales to most research tasks. A few
natural progressions, in increasing difficulty:

- **Convert your existing reading-notes into structured notes.**
  Point the agent at a folder of unstructured markdown, ask it
  to refactor each into the same template. Spot-check.
- **Outline a related-work section** from five papers you have
  already noted, using the YAML themes/methods fields you have
  built up.
- **Attempt a small replication.** Pick a paper with publicly
  available code and data. Ask the agent to clone the replication
  package, install dependencies, run the main analysis, and
  report which tables and figures match. This is where the friction
  is real; the [`social-science-replicability`](../projects/social-science-replicability.md)
  and [`recast-causal-ai`](../projects/recast-causal-ai.md) projects
  attempt this end-to-end.
- **Manuscript editing through the Overleaf round-trip.** In
  Overleaf, push your project to GitHub. Locally, ask the agent
  to make a specific, bounded edit ("tighten the contribution
  paragraph to three sentences and surface the empirical strategy
  in the first sentence"). The agent edits the `.tex` file,
  commits; you pull into Overleaf, read the diff, accept or revert.

---

## Common pitfalls

- **The agent never finds the PDF.** Check the path. Agents read
  *relative* paths from the directory you started them in. If you
  ran `claude` from your home directory, `papers/foo.pdf` will
  not resolve — `cd` into the repo first.
- **PDF extraction fails on scanned documents.** Older or scanned
  PDFs may have no embedded text. The agent will report
  empty pages. Use a tool like `ocrmypdf` to add a text layer
  first; or pick a different PDF for the walkthrough.
- **The note's YAML front-matter does not parse.** Look for an
  unmatched quote, a stray colon, or a tab character. Tell the
  agent: "the YAML at the top of notes/foo.md is not valid; fix it
  and re-save".
- **`git push` fails with authentication errors.** Your local Git
  is not yet authenticated to GitHub. Either configure a Personal
  Access Token (GitHub → Settings → Developer settings → Personal
  Access Tokens → Tokens (classic)) or set up the
  [GitHub CLI](https://cli.github.com/) and run `gh auth login`.

---

## Where to go from here

- [**Skills catalog**](../skills/index.md) — ready-made patterns
  for specific methods (DID, RDD, replication audits, paper
  rebuttals, …).
- [**Projects catalog**](../projects/index.md) — survey of
  end-to-end agentic-research systems if you want to see how
  others have wired up larger pipelines.
- [**Concept pages**](../concept/definition.md) — the conceptual
  frame for what you are building.
- [**IS-discipline reading list**](../concept/is-discipline.md) —
  the scholarly literature on what GenAI in research practice
  *means* for the field.
