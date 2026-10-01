---
name: lit-review
description: Explore literature on a topic, assess novelty, trace citation genealogy, and position research strategically. Dispatches parallel Opus sub-agents across three search dimensions, screens and reads papers, synthesizes the literature gap, and stress-tests it with an adversarial referee until convergence.
argument-hint: <topic or research question> [--paper <path_or_citekey>] [--depth deep|standard]
---

# Literature Review

Rigorous, multi-agent literature review for economics research. Searches across three dimensions, reads and classifies papers, identifies the literature gap, and validates it through adversarial audit. Designed for high-stakes novelty assessment — if this skill says "novel," the user will invest months and present at seminars.

## Trigger conditions

Invoke this skill when the user asks to:
- Explore literature on a topic or research question
- Check whether an idea, mechanism, or contribution is novel
- Understand where a paper fits in the genealogy of a literature
- Find related work for a paper, model, or methodology
- Assess whether they've been scooped
- Strategically position their research relative to existing work
- Any variation of "lit review," "literature review," "what's been done on..."

## Defaults and configuration

| Setting | Default | Override |
|---------|---------|----------|
| Phase 1 | the orchestrator searches directly | — |
| Screening model | Sonnet | — |
| Deep reading / synthesis / referee | Opus | — |
| Depth | Standard (2 iteration rounds) | `--depth deep` (3+ rounds, expanded Phase 4) |
| Source hierarchy | Top 5 > NBER/Fed > Other journals > Web | Not overridable |

### Resource strategy

Not every phase needs Opus. The orchestrator conserves resources by doing lightweight work itself and reserving Opus for high-reasoning tasks:

| Task | Who does it | Why |
|------|------------|-----|
| Keyword search, WebSearch queries | the orchestrator directly | Search is mechanical — no reasoning needed |
| Commentary search (blogs, VoxEU) | the orchestrator directly | Same — WebSearch queries |
| Abstract screening & classification | Sonnet sub-agents | Classification from abstracts is pattern-matching |
| Citation chain expansion | Sonnet sub-agents (batched) | Search + extraction, batch 3-4 papers per agent |
| Deep paper reading | **Opus** sub-agents | Requires nuanced judgment on novelty threats |
| Focused exploration | **Opus** sub-agents | Requires synthesis and targeted reasoning |
| Gap synthesis | **Opus** sub-agent | High-stakes assessment — must be precise |
| Adversarial referee | **Opus** sub-agent | Requires the strongest adversarial reasoning |

**Escalation rule**: When a paper looks threatening to novelty at ANY phase — even during screening — escalate immediately to an Opus deep-reading agent. Do not wait for Phase 3. A threatening paper is one that appears to study the same topic with the same method, or one that formalizes the same mechanism.

**User override**: If the user says "use Opus for everything," "max effort," "this is very important," or similar — promote ALL sub-agents to Opus, including screening (T3) and citation chains (T2). The table above is the default; the user can always escalate.

## Arguments

Arguments: $ARGUMENTS

Parse:
- **topic**: the research question, idea, mechanism, or topic to review (required)
- **--paper <path_or_citekey>**: the user's own paper or notes, to position against the literature (optional)
- **--depth deep|standard**: how many iteration rounds to run (default: standard)

If no topic is given, ask the user what to review.

If `--paper` is provided, read it (or dispatch a sub-agent to read it) to understand what the user is working on. This context is passed to all subsequent sub-agents.

## Three Dimensions of Search

Every literature review must cover three dimensions. These are not optional — all three must be searched even if results are sparse in some.

### Dimension 1: Topic x Method

Papers that study the **same question** using the **same approach** as the user. This is the highest novelty threat — if a paper exists here, the user may be scooped.

Example: If the user studies the employment effects of minimum-wage increases using a bunching estimator, this dimension searches for papers on minimum-wage employment effects identified via bunching at the kink.

### Dimension 2: Topic Only

Papers that study the **same question** but with **different methods or models**. These are essential for positioning — the user must know what the literature says about their topic, regardless of methodology.

Example: Papers on minimum-wage employment effects using any method (border discontinuities, synthetic control, event studies, structural models).

### Dimension 3: Method Only

Papers that use the **same methodology or model** but on a **different topic**. These are useful for citing and justifying the approach, or they may threaten methodological novelty.

Example: Papers using bunching estimators on topics other than the minimum wage (e.g., taxation kinks, retirement age, social security earnings tests).

### Three nuances within each dimension

For each dimension, assess:
1. **Analysis novelty**: Has this exact exercise been done? By whom, where, when?
2. **Mechanism novelty**: Is the economic mechanism the user proposes already known, formalized, or tested?
3. **Topical positioning**: Where does this fit in the ongoing conversation? Which literature does it speak to?

## Source Hierarchy

When reporting papers, always flag their prestige tier. A paper in a Top 5 journal or NBER signals that the profession has deeply engaged with that finding — this matters for positioning.

| Tier | Venues | Flag |
|------|--------|------|
| 1 — Top 5 | AER, QJE, Econometrica, JPE, ReStud | `[TOP 5]` |
| 2 — Frontier WP | NBER, Fed/central bank, CEPR, IZA | `[NBER]` / `[FED]` / `[CEPR]` |
| 3 — Other journals | All peer-reviewed journals | (no flag) |
| 4 — Web/commentary | Blog posts, VoxEU, policy reports, news | `[WEB]` |

**Double emphasis rule**: When a finding directly relevant to the user's work was published in Tier 1 or Tier 2, call it out explicitly in the Summary paragraph and in the Gap Assessment. This is not just a bibliography entry — it signals professional consensus.

Never limit the search to these tiers. Search broadly across all journals and sources. The tiers only affect how results are flagged and emphasized.

---

## Phase 1: Broad Discovery

### Step 1.1: Parse the user's research

Understand what the user is studying:
- What is the research question?
- What is the methodology / model?
- What is the claimed or intended contribution?
- What is the economic mechanism?

If `--paper` was provided, extract this from the paper. Otherwise, extract from the topic description and conversation context. If ambiguous, ask the user to clarify before proceeding.

### Step 1.2: Generate keyword sets

For each dimension, generate 5-10 keyword combinations:

- **Dimension 1** (Topic x Method): combine topic-specific AND method-specific terms
  - e.g., "minimum wage employment bunching estimator"
- **Dimension 2** (Topic Only): topic-specific terms, broadly
  - e.g., "minimum wage employment effects", "minimum wage spillovers"
- **Dimension 3** (Method Only): method/model-specific terms, broadly
  - e.g., "bunching estimator kinks", "bunching at notches earnings"

Include variations: synonyms, abbreviations, related concepts. If the user mentioned specific authors, include their names.

### Step 1.3: Search directly (no sub-agents)

The orchestrator performs all Phase 1 searches itself. This is mechanical work — keyword queries and result collection — that does not require sub-agent reasoning.

For **each dimension**, run at least 5 WebSearch queries using the keyword sets from Step 1.2. Include:
- Direct keyword combinations: `"[keyword1] [keyword2] economics"`
- Journal-targeted: `"[keywords] American Economic Review OR Econometrica OR QJE OR JPE OR Review of Economic Studies"`
- Working paper searches: `"[keywords] NBER working paper"` and `"[keywords] site:nber.org"`
- Recent papers: `"[keywords] 2024 2025 2026 working paper"`
- Author-targeted (if the orchestrator knows key authors): `"[author surname] [topic keywords]"`

Also search for **commentary and non-academic sources**:
- `"[topic] VoxEU"`, `"[topic] NBER Digest"`, `"[topic] Marginal Revolution"`, `"[topic] Brookings"`
- `"[topic] Federal Reserve working paper"`, `"[topic] World Bank policy"`

Also Grep `<REFERENCES_BIB>` for author surnames and topic keywords to find papers already in the local library.

### Step 1.4: Collect and deduplicate

Collect all candidate papers from the searches. Deduplicate by author + year + title (fuzzy match — same paper may appear with slightly different titles across sources). Build the **master paper list**.

For each paper, record: title, authors, year, venue, abstract snippet (if available from search results), URL, prestige flag (`[TOP 5]`, `[NBER]`, etc.).

**Early threat detection**: While collecting results, if any paper looks like it could be a direct novelty threat (same topic AND same method), flag it immediately for Opus deep reading in Phase 3. Do not wait for formal screening.

---

## Phase 2: Screening & Citation Chains

### Step 2.1: Abstract screening

Dispatch screening agents (model: **"sonnet"**) using Template 3 from `references/subagent-prompts.md`. Sonnet is sufficient for classifying papers from abstracts — this is pattern-matching, not deep reasoning.

Split the master list across agents if > 20 papers (one agent per batch of ~15-20 papers). Each agent receives its batch plus the user's research description.

Each agent classifies every paper:
- **[C] Critical**: same topic x method, direct novelty threat, or essential/influential reference
- **[M] Methodological**: same model/technique, different topic
- **[T] Topical**: same broad topic, useful for positioning
- **[X] Not relevant**: discard

**Immediate escalation**: If any paper is classified [C] and its abstract suggests a direct novelty threat (same topic AND same method/mechanism), the orchestrator flags it for immediate Opus deep reading in Phase 3. Do not wait for citation chains.

### Step 2.2: Citation chain expansion

Batch citation chain work into **1-2 Sonnet agents** (model: **"sonnet"**) using Template 2 from `references/subagent-prompts.md`. Each agent handles 3-4 papers. Do NOT dispatch one agent per paper — batch them to conserve resources.

Each agent:
- Searches for papers this paper cites (backward citations — via the paper's reference list)
- Searches for papers that cite this paper (forward citations — via Google Scholar / Semantic Scholar queries)
- Returns new candidate papers not already in the master list

### Step 2.3: Screen new candidates

Run the newly discovered papers through Step 2.1 again (Sonnet screening). This completes one round of expansion.

The orchestrator decides whether a second round is needed:
- If 3+ new [C] papers emerged → run another citation chain round
- If < 3 new [C] papers → proceed to Phase 3

---

## Phase 3: Deep Reading

### Step 3.1: Select papers for deep reading

The orchestrator selects papers for deep reading from the screened list:
- **All [C] papers** — must be read
- **Top [M] papers** (those from Top 5 or NBER, or those most methodologically similar)
- Cap at ~10 papers per round to manage sub-agent load

Prioritize: Top 5 journals first, then NBER/WP, then others.

### Step 3.2: Dispatch deep reading agents

Launch reading agents in parallel (model: "opus") using Template 4 from `references/subagent-prompts.md`. One agent per paper.

Each agent:
1. Searches `<REFERENCES_BIB>` for the paper by author surname + year
2. If found: extracts the PDF path from the `file` field and reads it using the Read tool (with `pages` parameter for large papers — read introduction + methodology first, max 20 pages per call)
3. If not in bib: attempts WebFetch on the paper's landing page, NBER page, or open-access version
4. Returns structured summary: research question, methodology, key results, novelty threat assessment, mechanism comparison, data/setting, journal/prestige flag

### Step 3.3: Collect deep reading results

The orchestrator assembles the deep reading summaries. Updates the master paper list with enriched information. Identifies:
- Which papers are genuinely close to the user's work
- Where the gap might be
- Which papers need even deeper investigation

---

## Phase 4: Focused Exploration (Second Wave)

### Step 4.1: Synthesize Phases 1-3

The orchestrator reviews all findings and identifies:
- Which strand of literature is most relevant
- Where the gap appears to be forming
- What questions remain unanswered (e.g., "Does Paper X actually use the same identification strategy?" or "What happened after Paper Y — did anyone follow up?")
- Which papers need deeper reading (specific sections)

### Step 4.2: Dispatch focused exploration agents

Launch agents (model: "opus") using Template 5 from `references/subagent-prompts.md`. Each agent receives:
- The current state of knowledge (the orchestrator's synthesis)
- A specific question or investigation task
- Papers to read more deeply or narrow sub-topics to search

These agents go deeper: they read specific sections of papers, search for follow-up work, trace how a conversation evolved over time.

### Step 4.3: Update and assess

The orchestrator integrates the focused exploration results. The picture should now be substantially clearer:
- The conversation in the literature is mapped
- The gap is taking shape
- The closest papers are identified and understood

If `--depth deep`: run another round of Step 4.2 with narrower, more targeted questions.

---

## Phase 5: Gap Synthesis

### Step 5.1: Dispatch gap synthesis agent

Launch ONE agent (model: "opus") using Template 6 from `references/subagent-prompts.md`. This agent receives:
- The user's research question, methodology, and contribution
- The complete classified and summarized paper list
- The three-dimensional search results
- The orchestrator's current assessment of where the gap might be

The agent returns:
- Literature landscape (what has been done, main strands, key authors)
- The gap (precise statement: "No paper has [X] using [Y] in the context of [Z]")
- Novelty assessment across all three nuances (analysis, mechanism, positioning)
- Closest 2-3 papers and exactly what differs
- Risk assessment (Low / Medium / High / Critical)
- Prestige presence (are closest papers in Top 5 / NBER?)

### Step 5.2: The orchestrator reviews

The orchestrator examines the gap synthesis for completeness:
- Does it address all three dimensions?
- Does it assess all three nuances?
- Is the gap claim precise and falsifiable?
- Are the closest papers actually the closest, or did the agent miss one?

If gaps in the synthesis → send follow-up questions to the gap agent or dispatch a new focused exploration agent. Do not proceed to Phase 6 with an incomplete gap claim.

---

## Phase 6: Adversarial Audit

### Step 6.1: Dispatch adversarial referee

Launch ONE agent (model: "opus") using Template 7 from `references/subagent-prompts.md`. The referee receives:
- What the user's paper does (topic, method, mechanism, contribution)
- The claimed literature gap (full text from the gap synthesis agent)
- The evidence supporting the gap (classified paper list with summaries)

The referee's mandate: demolish the gap claim if possible. Find missing papers, false novelty, trivial extensions, mechanisms already known under different names, concurrent work.

### Step 6.2: The orchestrator responds

For each challenge the referee raises:
- **If valid and investigatable**: dispatch new search or reading agents to check. Report findings back to the referee.
- **If addressable with existing evidence**: draft a rebuttal with specific citations.
- **If the referee found a genuinely threatening paper**: update the gap claim and revisit Phase 5.

### Step 6.3: Iterate until convergence

Send the orchestrator's response back to the referee agent (via SendMessage to continue the same agent). Continue the exchange until one of:
- **Referee concedes**: "I find this gap to be genuine because..." → proceed to output
- **Referee finds a fatal flaw**: the orchestrator revises the gap claim, re-runs Phase 5, dispatches a new referee
- **Maximum 3 rounds reached**: the orchestrator reports the final state of the debate, flagging any unresolved challenges

If the gap survives the adversarial audit → it is a validated gap. If not → the output honestly reports that the gap is contested and explains why.

---

## Phase 7: Opportunistic Iteration

This is not a sequential phase but a standing instruction that applies throughout Phases 4-6:

- If any agent mentions a paper the orchestrator hasn't seen → dispatch a search or reading agent
- If a new keyword or sub-topic emerges → dispatch a keyword search agent
- If the adversarial referee mentions a specific adjacent literature → dispatch a focused exploration agent

Continue until the orchestrator has a coherent, verified picture with no loose ends.

### Convergence criteria

All of the following must be true before proceeding to output:
1. All three dimensions have been searched
2. All three nuances have been assessed
3. The adversarial audit has passed (or been iterated to the maximum)
4. No new [C] papers emerged in the last round
5. The orchestrator can state the gap precisely and defend it

---

## Phase 8: Present Results

### Step 8.1: Assemble the response

Use Template A from `references/response-templates.md` to build the full literature review response.

### Step 8.2: Format paper entries

Each paper uses Template B from `references/response-templates.md`. Order within each section:
1. Top 5 journal papers (most relevant first)
2. NBER / frontier working papers (most relevant first)
3. Other journal papers (most relevant first)
4. Web sources

### Step 8.3: Write the gap assessment

Use Template C from `references/response-templates.md`. This must be factual, precise, and cite specific papers. No hedging beyond what is warranted.

### Step 8.4: Write the novelty verdict

Use Template D from `references/response-templates.md`. This is the structured assessment table: dimension x assessment x confidence, plus risk level and recommendation.

### Step 8.5: Proactive suggestions

At the end of the response:
- Suggest pivots or angles the user may not have considered
- Recommend 2-3 papers worth reading in full
- Flag any upcoming conferences or special issues relevant to the topic
- If the gap is weak, suggest how to strengthen it (reframe, narrow, pivot)

---

## Important rules

- **The orchestrator does Phase 1 itself.** Keyword searches and commentary searches are mechanical — the orchestrator runs WebSearch and Grep directly. No sub-agents needed for search queries.
- **Right model for the task.** Sonnet for screening (T3) and citation chains (T2) — these are classification and search tasks. Opus for deep reading (T4), focused exploration (T5), gap synthesis (T6), and adversarial referee (T7) — these require nuanced reasoning.
- **Batch citation chain agents.** Do not dispatch one agent per paper. Batch 3-4 papers per Sonnet agent.
- **Escalate threats immediately.** When a paper looks threatening to novelty at ANY phase — even during Phase 1 collection or Phase 2 screening — escalate immediately to an Opus deep-reading agent. Do not wait for the normal Phase 3 queue. A threatening paper is one that appears to study the same topic with the same method, or formalizes the same mechanism.
- **All critical papers get Opus deep reading.** Every paper classified [C] must be read by an Opus agent. No exceptions, no shortcuts.
- **Never skip deep iteration.** Phase 4 (Focused Exploration) is mandatory. The second wave of agents always runs, regardless of how clear the picture seems after Phase 3.
- **Never present guesswork as fact.** If uncertain about a paper's existence, relevance, or content, say "I am uncertain" and explain why. Flag your confidence level. Guessing and presenting as fact is the single worst failure mode of this skill.
- **Double-flag Top 5 and NBER presence.** When a finding directly relevant to the user's work was published in Top 5 or NBER, flag it with `[TOP 5]` or `[NBER]` in every output and call it out in the Summary and Gap Assessment.
- **Search the local library first.** Always Grep `<REFERENCES_BIB>` before concluding a paper is unknown. If it's in the bib, extract the PDF path and read it.
- **Replicate the /read-paper lookup pattern.** Sub-agents reading papers should: search references.bib by author surname + year → extract PDF path from `file` field → read via Read tool with `pages` parameter. If not in bib, use WebFetch.
- **Iterate until convergence.** Do not stop after one pass. The adversarial audit must pass before output is generated. If new leads emerge, pursue them.
- **Spend tokens wisely but thoroughly.** Conserve on mechanical tasks (the orchestrator does searches, Sonnet screens). Spend freely on reasoning tasks (Opus reads, synthesizes, and audits). The goal is correct and comprehensive, not cheap.
- **Report format is sacred.** Follow the response templates exactly. The structured output is how the user processes the information.
- **The stakes are high.** If this skill says "this is novel," the user will invest months of work and present at seminars. If it says "this has been done," the user will pivot. Either way, the answer must be correct.
- **Never limit to Top 5 journals.** Search all venues. The source hierarchy affects flagging, not search scope.
- **Check for concurrent work.** Always include searches for 2024-2026 working papers. The most dangerous scooping comes from papers in progress.
