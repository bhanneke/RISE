# Get started

> *A starter guide for researchers who have used ChatGPT for editing
> or quick lookups, but have not yet integrated a coding agent into
> their day-to-day research workflow.*

This page is **not** about building an autonomous AI scientist.
It is about adopting a small, opinionated stack that lets a working
researcher delegate the *mechanical* parts of research to an agent
while keeping the *intellectual* parts firmly under your own
control. Think of it as moving from *prompt-and-paste* to
*direct-and-verify*.

The conceptual frame for what this is, why it matters, and where it
sits in the discipline lives under [Concept](concept/definition.md).
The catalogs of [papers](papers/index.md), [projects](projects/index.md),
and [skills](skills/index.md) are what you draw on once you have a
working setup. This page is the bridge.

---

## What changes when you add an agent

A non-agentic AI workflow looks like this: you write a prompt, paste
some text into a chat window, copy the answer back into your
document. The unit of interaction is **the message**. The agent
cannot see your files, run your code, or check its own work.

An agentic workflow looks different. The agent has a **terminal**, a
**working directory**, and **tools** — it can read your files, edit
them in place, run scripts, install packages, and inspect the output
of what it just did. The unit of interaction is **the task**. You
say "rewrite the introduction to lead with the identification
strategy, then check that the bibliography still compiles" and the
agent does all of it, reporting back what it changed.

This raises the leverage substantially — and raises the stakes. An
agent that can edit your files can also corrupt them; an agent that
can run code can also burn a weekend of compute on the wrong job; an
agent that cites a paper can also invent it. **Augmentation, not
automation** is the operating mode this guide assumes. You stay in
charge. The agent earns trust task by task.

---

## A starter stack

There is no single right setup. The one described here is
deliberately small, runs locally, and works for an empirical-paper
workflow that uses LaTeX. Substitute components as your discipline
demands.

### Manuscript layer — Overleaf ↔ GitHub

- **Overleaf** for the LaTeX writing surface — what you actually
  look at, edit, and compile.
- **GitHub** as the durable store of the manuscript, code, data
  scripts, and history. Overleaf's GitHub integration syncs the
  Overleaf project to a GitHub repo on demand, so every co-author
  (and every agent) can read and write the same source.

The point of the integration is that **the manuscript becomes a
real repository**, not a black-box cloud document. Your agent —
running locally — can clone the repo, propose edits as commits,
and you can review the diff before pushing back to Overleaf.

### Agent layer — local Claude Code / Codex

Pick one to start. They are interchangeable enough for a first
setup; you can switch later.

- **[Claude Code](https://docs.claude.com/en/docs/claude-code)** —
  Anthropic's terminal agent. Runs in your shell, reads your
  project, edits files, executes commands. Most of the RISE
  [skills catalog](skills/index.md) is written for this harness.
- **[OpenAI Codex CLI](https://github.com/openai/codex)** — OpenAI's
  equivalent. Different model family, similar interaction model.

Either is sufficient. The reason to run *locally* rather than in a
hosted IDE is that your data stays on your machine, your file
permissions are visible, and the failure modes are easier to debug
when something goes wrong.

### Optional but recommended

- A **literature manager** (Zotero, Paperpile) that exports BibTeX
  to the same repository. Agents are much better at citation work
  when there is a canonical `.bib` file to operate on.
- A **plain-text scratchpad** in the same repo (`NOTES.md`, `TODO.md`)
  where you and the agent keep track of decisions, open questions,
  and follow-ups. This is the lowest-effort form of agent memory.

---

## First workflows to try

Pick *one* and do it end-to-end before adding a second. Resist the
urge to wire up everything at once.

### 1. Literature scan and structured note

Hand the agent a PDF (or a DOI). Ask it to produce a 200-word
structured summary covering: contribution, method, key claim, and
the strongest critique. Save the result as `notes/<citekey>.md`
alongside the BibTeX entry.

This is the single most useful first task because the verification
is fast (you read the PDF too) and the output is immediately
reusable. The RISE [papers catalog](papers/index.md) is built
exactly this way; the curator schema lives at
[`papers/schema.md`](https://github.com/bhanneke/RISE/blob/main/papers/schema.md).

### 2. Replication of a small published result

Pick a paper with publicly available code and data. Ask the agent
to clone the replication package, install dependencies, run the
main analysis, and report which tables and figures match the
published versions. This is harder than it sounds — the agent will
hit broken paths, missing packages, deprecated APIs — and that is
the point. You learn how to direct an agent through real
engineering friction, and you learn what your discipline's
replication packages actually look like.

The [projects catalog](projects/index.md) has two systems that
attempt this end-to-end:
[`social-science-replicability`](projects/social-science-replicability.md)
and [`recast-causal-ai`](projects/recast-causal-ai.md). Reading
their READMEs is a useful prelude to attempting your own.

### 3. Manuscript editing through the GitHub roundtrip

In Overleaf, push your project to GitHub. Locally, ask the agent to
make a specific, bounded edit — *"tighten the contribution paragraph
to three sentences and surface the empirical strategy in the first
sentence"*. The agent edits the `.tex` file, commits with a clear
message. You pull into Overleaf, read the diff, accept or revert.

The discipline of writing **bounded edit requests** is what
distinguishes useful agent-assisted writing from generic
LLM-generated prose. Specificity travels much further than length
in the prompt.

---

## Common pitfalls

- **Hallucinated citations.** Coding agents will confidently invent
  papers, DOIs, and quotations. **Never accept a citation an agent
  produces without independently verifying it.** A canonical `.bib`
  file the agent reads from (rather than generates) helps; but the
  rule is firm.
- **Plausible-sounding wrong code.** Code that compiles is not code
  that is correct. For statistical results in particular, ask the
  agent to print intermediate values, then check at least one
  against a hand-computed or independently-replicated reference.
- **Scope creep.** A vague request ("improve this section") will be
  answered with broad, often unwelcome rewrites. A specific request
  ("change passive voice to active in the next paragraph; leave
  everything else") respects your judgment as the author.
- **Tool-use cost.** Agents can spend real money on API calls
  quickly. Set a budget for any long-running task and check on it.
  Local model alternatives (e.g., a small Llama for routine
  literature triage) are worth knowing about, even if your default
  stack is hosted.

---

## What this guide deliberately does not cover

- **Building your own agentic pipeline.** That is the subject of the
  [Projects catalog](projects/index.md) and the underlying
  [literature](papers/index.md). This guide is for *using*, not
  *building*.
- **Domain-specific workflows beyond empirical economics / IS.**
  Biomedical, mathematics, NLP, and other disciplines have their own
  conventions. The [Concept pages](concept/definition.md) discuss
  cross-disciplinary patterns; the catalogs feature systems from
  several fields.
- **Fully autonomous, end-to-end paper generation.** A few systems
  in the catalog ([`agent-laboratory`](projects/agent-laboratory.md),
  [`sakana-ai-scientist`](projects/sakana-ai-scientist.md),
  [`evoscientist`](projects/evoscientist.md),
  [`aris`](projects/aris.md), [`robin`](projects/robin.md)) attempt
  this. They are research artifacts, not yet practical replacements
  for a working researcher's day-to-day stack.

---

## Where to go next

- Browse the [Skills catalog](skills/index.md) for ready-made
  patterns — DID with Claude, paper-rebuttal drafting, replication
  audits — that you can adapt to your own work.
- Read the [Concept](concept/definition.md) pages to put what you
  are building in context with the broader RISE framing.
- Survey the [Projects catalog](projects/index.md) when you want to
  see how others have already wired up end-to-end pipelines.
- For the IS-discipline reading list specifically, see
  [Concept → The IS discipline and RISE](concept/is-discipline.md).
