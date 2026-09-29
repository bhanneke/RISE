<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/blast-radius.md -->

# `/blast-radius`

Before and after changing anything shared (a function, signature, schema, config default or constant), finds every consumer and runs it to catch silent downstream breakage.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../psantanna-workflow/">Pedro Sant'Anna's Claude Code Workflow</a></div><div><b>Category:</b> <code>audit</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-08-23</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>code-generation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/blast-radius/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/psantanna-workflow/blast-radius/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/blast-radius/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Know the blast radius before you change it

The dangerous change is not the risky-looking one. It is the one that **looks purely additive** — adding a returned value, a column, an option — and quietly violates a contract three files away that nobody re-read. Compilation and type checks will not catch a positional or length contract; you get either a crash far from the edit, or worse, silently wrong output.

**Rule: if you change a shared interface, run its consumers. Reading them is not running them.**

### 1. Enumerate consumers before editing

Grep for every call site, import, and downstream reference — including tests, notebooks, scripts, docs, and anything that regenerates reported results. Note which ones produce numbers that appear in a paper, dashboard, or release: those are the ones where silent breakage is most costly.

If a consumer lives in another repo, another language, or a generated artifact, write it down now; you will not remember at verification time.

**A consumer in another repo pins this one by commit SHA.** Its verification receipt records the *revision* it was built against — not a branch, not a version string, both of which keep moving under it. So **a change here that moves a number the downstream reports is not finished when this repo goes green**: before/after evidence for what moved, regeneration of the downstream artifact, and the re-pin all belong to the *same round* as the change — `release-engineering.md` §6 has the ordering within it. A downstream left pinned to the old SHA is an honest, inspectable state; one pointed at a moving reference silently inherits a number nobody re-verified.

### 2. Name the contract you are about to change

Ask explicitly what downstream code is entitled to assume:

- **Arity / length** — does anything index positionally, zip against a fixed list, or preallocate a matrix of known width? *Adding an element breaks all three.*
- **Names and order** — does anything match by name, by position, or pair your output against a separate parallel list of labels?
- **Types, units, scale** — dollars vs cents, rate vs percent, seconds vs ms, 0-indexed vs 1-indexed.
- **Nullability and sentinels** — new empty/NA cases a consumer will not expect.
- **Defaults** — changing a default silently changes every caller that relied on it.
- **Identity/ordering guarantees** — row order, sort stability, key uniqueness.

The classic failure: a returned vector grows from 6 to 7, while a consumer pairs it against a hard-coded list of 6 labels. Nothing errors at the edit site; the consumer either throws far away or, worse, recycles and mislabels every row.

### 3. Prefer changes that cannot break a contract

Additive-and-named beats additive-and-positional. Where you control the consumer, match by name rather than position. Where you cannot, version the interface rather than widening it in place.

Do **not** "fix" a mismatch by deriving labels/config from the new data if the old labels were deliberately different — deliberate relabeling exists (display names differing from internal names), and auto-deriving silently changes published output.

### 4. Run the consumers — end to end, on real inputs

A consumer that merely imports is not exercised. Run at least one full path per distinct consumer pattern, and prefer the one that regenerates reported numbers.

Then verify **both** directions:
- The new thing works.
- **The old things are unchanged.** Diff previously-reported outputs; anything that moved must have a reason you can state. If the change was supposed to be behavior-preserving, byte-identical or within a declared tolerance is the evidence — not "it ran".

### 5. Green is uninformative if nothing ran

Confirm the check actually executed and could have failed: a skipped test, a filtered-out case, an exception swallowed into a default, or a tolerance widened after the comparison are all indistinguishable from success in a log. Where the change is consequential, **seed a defect** and confirm the check goes red — a comparison that cannot fail is not evidence.

### 6. Record the contract change

If the interface genuinely changed, say so where consumers will look: a NEWS/CHANGELOG entry, a versioned interface note, or a comment at the definition naming what downstream code may assume. For anything reused or released, freeze inputs (versions, hashes, seeds) and record declared tolerances so the next comparison is reproducible rather than renegotiated.

### Minimum checklist

1. Grep all consumers, including tests, scripts, docs, other repos/languages.
2. Write down the contract: arity, names, order, types, units, defaults, ordering.
3. Make the change name-based/versioned where you can.
4. Run at least one full path per consumer pattern.
5. Diff previously-reported outputs; explain any movement.
6. Seed a defect to prove the check can fail.
7. Record the contract change where consumers will see it.
8. Re-pin every cross-repo consumer to the new SHA — regenerated and re-verified in this round, not the next one.

### Cross-references

- `verification-ladder.md` — rung 2 (wiring)
- `provenance-and-ground-truth.md` — never re-bless a baseline in the commit that moves it
- `release-engineering.md` — pinning downstream consumers by SHA, and what a number-moving change owes them in the same round
