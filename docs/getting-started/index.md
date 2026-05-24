# Get started

> *A step-by-step guide for researchers who have used ChatGPT for
> editing or quick lookups, but have not yet integrated a coding
> agent into their day-to-day research workflow.*

This is not a guide to building an autonomous AI scientist. It is a
guide to standing up a small, opinionated stack that lets a working
researcher delegate the *mechanical* parts of research to an agent
while keeping the *intellectual* parts firmly under your own
control. **Augmentation, not automation** is the operating mode
throughout.

The conceptual frame for what this is and why it matters lives
under [Concept](../concept/definition.md). The catalogs of
[papers](../papers/index.md), [projects](../projects/index.md),
and [skills](../skills/index.md) are what you draw on once you
have a working setup. This section is the bridge.

---

## What you will have at the end

A laptop set up to do this:

1. Your manuscript lives as a real Git repository — every change
   tracked, every co-author and every agent reading the same
   source.
2. A coding agent (Claude Code or Codex) running in your terminal,
   able to read your files, edit them, run scripts, and report
   what it changed.
3. A first concrete workflow you have actually completed — turning
   a PDF into a structured curator note — with the discipline of
   *direct-and-verify* baked in.

Expect to spend **about an hour** end-to-end, longer if you are
new to the command line.

---

## The three steps

1. [**Manuscript stack** — Overleaf ↔ GitHub](manuscript.md)
   <br/>Set up a Git-backed manuscript so the agent has something
   real to operate on.
2. [**Agent stack** — Claude Code or Codex](agent.md)
   <br/>Install a coding agent on your laptop and authenticate it.
3. [**First workflow** — turn a PDF into a curator note](first-workflow.md)
   <br/>Hand the agent a paper, get back a structured note, verify it,
   commit it.

Do them in order. Resist wiring up everything at once.

---

## Prerequisites

- A laptop (macOS, Linux, or Windows with WSL).
- A willingness to use the terminal. You will type commands like
  `cd ~/Projects/my-paper` and `git push`. If that sounds
  intimidating, that is fine — the steps will show you exactly what
  to type.
- A working email address. You will create or reuse accounts on
  GitHub, Overleaf, and either Anthropic (for Claude Code) or
  OpenAI (for Codex).
- Optional but useful: a paper PDF you actually want to read for
  the first-workflow walkthrough.

What you do *not* need: prior experience with Git, LaTeX, Node.js,
or any agent framework. Each step explains what it does and why.

---

## A note on cost

The agent layer uses commercial APIs that charge per token. Typical
costs for the workflows in this guide are small (tens of US cents
per literature note, a few dollars for a full replication attempt),
but they are real. Set a monthly cap in your provider's billing
dashboard before you start. Both Anthropic and OpenAI let you do
this in two clicks.

---

## What this guide deliberately does not cover

- **Building your own agentic pipeline.** That is the subject of the
  [projects catalog](../projects/index.md) and the underlying
  [literature](../papers/index.md). This guide is for *using*, not
  *building*.
- **Fully autonomous, end-to-end paper generation.** A few systems
  in the catalog ([`agent-laboratory`](../projects/agent-laboratory.md),
  [`sakana-ai-scientist`](../projects/sakana-ai-scientist.md),
  [`robin`](../projects/robin.md),
  [`aris`](../projects/aris.md)) attempt this. They are research
  artifacts, not yet practical replacements for a working
  researcher's day-to-day stack.
- **Discipline-specific patterns** beyond a generic LaTeX-paper
  workflow. The [skills catalog](../skills/index.md) collects
  patterns for specific methods (DID, RDD, replication audits,
  paper rebuttals, …).
