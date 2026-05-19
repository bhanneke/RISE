# Idea Expansion: From Raw Idea to Structured Research Brief

## Purpose

Transform a raw research idea — which may be as sparse as a single sentence — into a structured research brief rich enough to drive the full research pipeline. The brief must contain testable propositions, concrete data sources, identification strategies, and explicit scope constraints.

The goal is NOT to write the paper or design the full strategy. It is to ensure the Research Designer receives input of consistently high quality, regardless of how detailed the original idea was.

---

## Core Principles

### 1. Phenomenon-First Thinking

Start from an observable behavior in the world, not from a gap in the literature.

- **Ask:** "What actually happens that is surprising, consequential, or unexplained?"
- **Do not ask:** "What has no one studied yet?"

The phenomenon is the anchor. Everything else — propositions, data, identification — flows from it. If you cannot state the phenomenon in one sentence without referencing a paper, you are thinking backwards.

**Test:** Would a smart non-academic find this interesting? If yes, the phenomenon is real. If you need to explain three papers before the question makes sense, it is literature-driven.

### 2. Proposition Generation

Each proposition must have four components:

1. **Direction:** What do you expect? (X increases Y / X decreases Y / nonlinear / threshold)
2. **Mechanism:** Why? What economic logic drives this relationship?
3. **Testable implication:** What pattern in data would you observe if true?
4. **Discriminating power:** What alternative explanation would produce a different pattern?

**Good proposition:** "Early NFT collection entrants earn higher returns than late entrants (direction: positive timing premium), because early entrants face lower competition for attention and liquidity (mechanism: first-mover advantage in thin markets). We would observe a declining returns curve as entry order increases within a collection (testable implication), which would NOT be explained by selection on quality if we control for creator characteristics (discriminating power)."

**Bad proposition:** "NFTs are related to creator earnings." (No direction, no mechanism, not testable)

Aim for 3-6 propositions. Fewer than 3 suggests the idea is underdeveloped. More than 6 suggests the scope is too broad for one paper.

### 3. Anti-Streetlight Discipline

The "streetlight effect" is researching where the data is easy rather than where the answer is important. For every idea, explicitly identify:

- **The boring version:** What would a lazy researcher do with this topic? (e.g., "regress returns on a time trend and call it a day")
- **Why it's insufficient:** What question does the boring version fail to answer?
- **The interesting version:** What makes this paper worth reading?
- **Forbidden framings:** Specific angles that are too obvious, too incremental, or too descriptive

This section is not optional. It forces the research design away from low-hanging fruit and toward genuine insight.

### 4. Data Reality Check

Only propose data sources that actually exist and are accessible:

- **Name the source specifically:** Not "blockchain data" but "Flipside Crypto `ethereum.core.ez_nft_sales`" or "Allium `ethereum.raw.transactions`"
- **Verify availability:** Can you actually query this? Is there an API? What does access cost?
- **Check coverage:** Does the data cover the relevant time period and population?
- **Note limitations:** Survivorship bias, missing variables, measurement error

Do NOT propose data that would require building a new dataset from scratch unless you explain exactly how to construct it and estimate the effort.

### 5. Scope Discipline

A paper that tries to do everything does nothing well. Define explicit boundaries:

- **In scope:** The specific question, population, time period, and mechanism
- **Out of scope:** Adjacent questions that require separate papers
- **Not claiming:** What the paper deliberately does NOT test or prove

---

## Web Research Protocol

When expanding an idea, use web search to:

1. **Verify the phenomenon:** Search for evidence that the behavior actually occurs. News articles, blog posts, data dashboards, and industry reports all count. If you cannot find evidence of the phenomenon, it may not exist.

2. **Scout the literature:** Search for recent papers on the topic (Google Scholar, SSRN, arXiv, NBER). Identify the 3-5 closest papers. Note what they found and what they left open.

3. **Check data availability:** Search for the specific databases and APIs mentioned. Verify they exist, check documentation, confirm the variables are available.

4. **Find natural experiments:** Search for policy changes, protocol upgrades, regulatory shocks, or other events that create exogenous variation useful for identification.

---

## Output Format

The structured brief should be a Markdown document following the 8-section structure:

1. PHENOMENON — One paragraph, plain language
2. RESEARCH QUESTION — One sentence, specific and falsifiable
3. PROPOSITIONS — 3-6 numbered propositions with direction/mechanism/test/discrimination
4. DATA SOURCES — Table or list with name, variables, coverage, access, limitations
5. IDENTIFICATION SKETCH — Source of variation, identifying assumption, threats
6. ANTI-STREETLIGHT — Boring version, why insufficient, interesting version, forbidden framings
7. LITERATURE ANCHORS — 3-5 closest papers with what they found and how this differs
8. SCOPE CONSTRAINTS — Explicit exclusions and adjacent-but-separate questions

---

## Quality Checklist

Before finalizing the brief, verify:

- [ ] The phenomenon can be stated without referencing any paper
- [ ] Each proposition specifies direction AND mechanism
- [ ] At least one data source has been verified as accessible
- [ ] The identification strategy names a specific source of exogenous variation
- [ ] The anti-streetlight section names the boring version explicitly
- [ ] Scope constraints exclude at least one adjacent question
- [ ] Literature anchors include papers from the last 3 years
- [ ] The brief is rich enough that a researcher could start designing a study from it alone
