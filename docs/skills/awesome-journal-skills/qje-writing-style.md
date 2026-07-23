<!-- DO NOT EDIT — auto-copied from skills/awesome-journal-skills/details/qje-writing-style.md -->

# `qje-writing-style`

Polishes prose, abstract, and introduction so the big idea lands fast for a general-interest reader, reflecting QJE's house style of long, ambitious, narrative-driven empirical papers.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-journal-skills/">Awesome Journal Skills (AJS)</a></div><div><b>Category:</b> <code>editing</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>revision-editing</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Awesome-Journal-Skills/contents/Quarterly-Journal-of-Economics-Skills/skills/qje-writing-style/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-journal-skills/qje-writing-style/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/Quarterly-Journal-of-Economics-Skills/skills/qje-writing-style/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Awesome-Journal-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Writing Style (qje-writing-style)

### When to trigger

- The prose buries the idea; a reader cannot find the contribution quickly
- The abstract does not state the finding, or leads with method
- The introduction wanders before reaching the question and the result
- Sentences are technical-jargon-dense for a general-interest audience

### QJE house style: ambitious, narrative, long

QJE is read across all of economics, and its papers are characteristically **long, narrative-driven, and ambitious** — there is **no hard page limit**, and an extensive online appendix is the norm. That freedom is a trap: the *body* must still make a **big idea legible to a smart non-specialist** in the first two pages, with the heavy machinery pushed to the appendix. The model is the canonical QJE empirical-micro paper (e.g., Chetty, Hendren, Kline & Saez on mobility, QJE 2014): a sharp question stated plainly, a clean source of variation, a memorable headline number, and a broad lesson — all before the reader hits the data section. Format facts that shape the writing: the **abstract is short (~150 words)**, citations are **author-date (Chicago)**, and double-blind review means the prose must not out the authors. Late-stage skill: only polish once identification and results are settled.

### The introduction arc (QJE template)

1. **The question** — one or two sentences, plain language, stakes clear.
2. **Why it is hard** — the identification problem that has blocked a clean answer.
3. **The setting & variation** — the natural experiment / data that solves it, in one paragraph.
4. **The headline result** — the number, with units, stated early and memorably.
5. **Interpretation & mechanism** — what it means; the conceptual frame in a sentence.
6. **Contribution & broad lesson** — placement in the literature + "beyond this setting."
7. **Roadmap** — brief; do not over-signpost.

### Abstract: state the finding (keep it ~150 words)

- Open with the question and the design in one breath, then **state the result with a number**.
- Close with the broad lesson. No throat-clearing, no "this paper studies the important issue of."
- Keep it to roughly the QJE abstract length (~150 words); a general-interest reader should know what you found from the abstract alone.

### Sentence-level craft

- Active voice; short declaratives for the key claims.
- Define notation once; do not make the reader hold five symbols to parse a sentence.
- Quantify ("raises earnings by 8%") rather than vague intensifiers ("substantially affects").
- Hedge only where the evidence requires it; calibrated confidence reads as competence.
- The license to write long is not a license to wander — every long stretch should earn its place, with technical detail relocated to the online appendix.

### Checklist

- [ ] Abstract states the actual finding with a number, not just the topic, and is ~150 words
- [ ] The question is on page one in plain language
- [ ] The headline result appears early in the introduction, with units
- [ ] The broad lesson ("beyond this setting") is explicit
- [ ] Jargon minimized; a non-specialist top-5 reader can follow the intro
- [ ] Claims are quantified, not vaguely intensified
- [ ] Author-date (Chicago) citations; numbers and units consistent throughout

### Anti-patterns

- An abstract that describes the topic but never states the result (or runs well past ~150 words)
- Leading the intro with method ("We use a Sun–Abraham estimator ...") instead of the question
- "This paper is the first to study the important question of ..." throat-clearing
- Using QJE's no-page-limit freedom to ramble instead of relocating detail to the appendix
- Vague magnitude language ("significantly", "substantially") with no number
- Notation overload in the introduction

### Output format

```
【Abstract verdict】states finding+number, ~150 words? [Y/N] — fix: ...
【Intro arc】question / hardness / variation / result / interpretation / contribution present? [Y/N each]
【Headline number in intro】present + units? [Y/N]
【Broad lesson stated】[Y/N]
【Jargon flags】[...]
【Next step】qje-replication-package or qje-referee-strategy
```
