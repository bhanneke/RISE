# Personal Academic Writing Style

This skill captures the principal's academic writing voice as extracted from four published papers (BISE, IJRM, JMIS, ECIS 2025). Every draft you produce must match these patterns.

---

## Voice and Tone

- **Formal but accessible.** The writing is academic but avoids unnecessary jargon. Technical terms (e.g., "tokenization," "vector autoregressive model," "pseudonymous addresses") are introduced with brief inline explanations the first time they appear, making the text readable for a broad IS/management audience.
- **Confident and assertive, with calibrated hedging.** Claims are stated directly: "blockchain data provides unprecedented transparency," "the exchange rate plays a prominent role." Hedging appears only where genuinely warranted: "may," "might," "potentially," "could" — never stacked ("it could potentially perhaps").
- **Third-person and first-person plural.** Use "we argue," "we demonstrate," "our findings suggest." Never use first-person singular ("I") or passive constructions where "we" works. Reserve passive voice for methodological descriptions ("data were collected," "the model is estimated") where the agent is obvious or irrelevant.
- **Present tense for claims and contributions**, past tense for describing what was done empirically: "We find that..." (present for the finding), "We analyzed over 4.5 million transactions" (past for the action).

---

## Sentence Structure

- **Medium-length sentences (20–35 words typical), with occasional long sentences (40–50 words) for complex argumentative chains.** Short punchy sentences (<15 words) are rare and used only for emphasis or transition.
- **Front-load the point.** The main claim or finding goes at the beginning of the sentence; qualifications and elaboration follow. Example: "The exchange rate influences the total number of economic actors; however, only new actors had a reciprocal relation."
- **Use semicolons and em-dashes for mid-sentence pivots** rather than starting a new sentence. Example: "While certain privacy-focused blockchains are designed to prioritize anonymity, most public blockchains store transaction data — including pseudonymous addresses — in an immutable and transparent way."
- **Enumerations within sentences use "e.g.," freely.** Lists of examples are woven into sentences rather than broken into bullet points: "...various studies focused on blockchains', smart contracts', and tokens' potential applications, e.g., their impact on business models, value chains, and ecosystems."
- **Parenthetical asides for supplementary detail.** Parentheses carry definitions, clarifications, and cross-references: "(i.e., distributed ledgers with restricted access to their network and data)," "(see Figure 1)."

---

## Argumentation Flow

- **Problem → gap → "against this background" → contribution.** Introductions open with a concrete, grounded description of the phenomenon (often with dollar figures, market sizes, or regulatory milestones), then identify what the literature has not yet addressed, then pivot with a phrase like "against this background" or "building on these insights" to the paper's contribution.
- **Literature as infrastructure, not decoration.** Prior work is cited to build the argument's foundation, not to show breadth. Each citation cluster serves a specific argumentative purpose — establishing a phenomenon, identifying a gap, or anchoring a method. Avoid "many scholars have studied X" without saying what they found.
- **Layered specificity.** Arguments proceed from general to specific. Example pattern: broad phenomenon → specific manifestation → concrete example → the paper's angle on it.
- **Explicit roadmap sentences at the end of introductions.** "The remainder of this study is structured as follows: In the next section, we present... Afterward, we... Then, we..."

---

## Transition Patterns

- **Between paragraphs:** "However," "Moreover," "That said," "In contrast," "Building on these insights," "Against this background," "Thus," "Therefore," "In conclusion,"
- **Between ideas within paragraphs:** "While... , ...," (concessive clause first), "Yet," "Nevertheless," "In the same vein," "Notably," "Additionally,"
- **Between sections:** The last sentence of a section often previews or motivates the next. The first sentence of a new section either picks up that thread or resets context with a crisp topic sentence.
- **"First, ... Second, ... Third, ..."** for structured enumerations of contributions, implications, or findings. Often introduced with a lead-in sentence: "Our research makes several practical and theoretical contributions."
- **Avoid** "Furthermore," "It is worth noting that," "Interestingly," as standalone transitions — these are filler.

---

## Literature Integration

- **High citation density in introductions** (often 3–6 citations per paragraph), tapering in results and discussion.
- **Inline citations woven into the argument**, not dumped at the end of a sentence. Example: "research has deepened our understanding of how blockchain technology may create value (Chen, 2023) and how it might interoperate with existing digital infrastructure via oracles (Cong, 2024) or sensors (Bakos, 2023)."
- **Citation clusters for established claims:** When an idea is well-established, a cluster of 2–4 citations appears in a single parenthetical: "(Tonnissen, 2020b; Weking, 2020; Witt, 2023)."
- **Active citation for key papers:** When a specific paper is central to the argument, cite it actively: "As Castañeda (2024) demonstrates..." or "Building on the DeFi tech stack (Schär, 2021), we propose..."
- **Never cite without purpose.** Every citation either (a) establishes a fact the argument depends on, (b) positions the paper relative to prior work, or (c) identifies the gap the paper fills.

---

## Presenting Findings

- **Lead with the direction, then quantify.** "We find that involuntary switchers experience an initial wage penalty of 8 percent." Not: "The coefficient was 0.08, which indicates..."
- **Name the variables and their relationships in plain language** before giving model numbers. Example: "The uniform relationship across firms shows a negligible coefficient (0.025)." The interpretation precedes or accompanies the number.
- **Explicit hypothesis verdicts:** "These results collectively suggest that size of wallet fails as a valid indicator of potential wallet." State plainly whether the hypothesis is supported or not.
- **Comparisons to prior work are concrete:** "These values are lower than the one by Du et al. (2007), who found no relation between these two metrics."
- **Tables and figures are referenced conversationally:** "Table 5 reveals the strong market position of OpenSea," "Figure 4 illustrates the share of wallet distribution." The text tells the reader what to see, not just where to look.

### Introduction vs. Results: different levels of statistical detail

The **introduction** previews findings in plain economic language only: direction, magnitude in interpretable units (percentages, multiples, dollar amounts), and whether the effect is significant or not. No coefficients ($\hat{\beta}$), no p-values, no t-statistics, no standard errors. The reader should understand the main findings without any statistical training.

The **Results section** is where coefficients, standard errors, t-statistics, p-values, and table references belong. Walk through tables column by column, interpret magnitudes, and discuss significance. The full statistical apparatus lives here, not in the introduction.

---

## Positioning Contributions

- **Contributions are numbered and explicitly stated:** "Our research makes several practical and theoretical contributions. First, ... Second, ... Third, ..."
- **Each contribution is framed relative to what existed before:** "Our research is the first to derive the total wallet for all customers of all major firms in a specific market." The novelty is made explicit by contrasting with the prior state: "Unlike prior studies that relied on survey data or statistical models, our study uses decoded blockchain data."
- **Practical and theoretical contributions are separated.** The writing distinguishes between "what practitioners can now do" and "what scholars now understand."
- **Contributions are previewed in the introduction and echoed in the discussion.** The introduction lists them; the discussion elaborates on each one with evidence from the results.

---

## Characteristic Constructions

- "This transparency enables..." / "These unique features provide new opportunities to..."
- "We refer to X as Y" — for introducing paper-specific terminology
- "Against this background, this paper..." — canonical pivot to contribution
- "The remainder of this study is structured as follows:"
- "Our empirical results underline..." / "Our analysis reveals..."
- "For instance," and "For example," used frequently to ground abstractions
- "...thereby..." as a connector within sentences: "...thereby merging the physical and digital"
- "...thus..." for causal conclusions: "Thus, tokenized assets are digital representations..."

---

## Anti-Patterns (What NOT to Do)

- **Do NOT use "delve into," "dive into," "unpack," "landscape," "paradigm shift," "game-changer," "cutting-edge," or "groundbreaking."** These are AI slop markers absent from the principal's writing.
- **Do NOT start paragraphs with "It is important to note that..." or "It should be noted that..."** — get to the point.
- **Do NOT use rhetorical questions** in academic prose. The principal never asks "But what does this mean for practitioners?" — state it directly.
- **Do NOT hedge excessively.** One hedge per claim is enough. "This could potentially suggest that it might be possible" is forbidden.
- **Do NOT use "the authors" to refer to the paper's own team.** Always "we."
- **Do NOT write overly short, choppy paragraphs.** Academic paragraphs in this style run 100–200 words, developing a single point fully before moving on.
- **Do NOT frontload empty topic sentences** like "This section discusses the results." Instead, lead with substance: "Our estimation results underscore the exchange rate's prominent role."
- **Do NOT add filler connectives** between every sentence. Let the logical structure carry the flow. Not every sentence needs "Additionally," or "Furthermore."
- **Do NOT use exclamation marks.** Ever.

---

## Formatting Rules — MANDATORY

These rules override any structural convenience. Violation of these rules makes the paper look like an AI-generated report rather than a scholarly article.

### No bullet points in the body of the paper

Results, discussion, limitations, future research, and conclusion sections must be written as **flowing prose paragraphs**. Bullet points and numbered lists are forbidden in these sections. This is non-negotiable.

- Tables and figures use their own formatting conventions.
- The introduction roadmap ("The remainder of this paper...") may use inline enumeration ("First, ... Second, ...") woven into sentences, NOT as a bullet list.
- The only acceptable numbered items in a paper are: equations, propositions, hypotheses, and table/figure labels.

If you find yourself wanting to write a bulleted list of limitations or results, that is a signal to restructure the content as connected paragraphs where each point flows into the next.

**Bad:**
```
Our study has several limitations:
- First, our data covers only 2020-2023...
- Second, we cannot observe...
- Third, our identification strategy assumes...
```

**Good:**
```
Our analysis is subject to several scope conditions. The sample covers
2020-2023, capturing the full boom-bust cycle but not the mature market
that emerged afterward; extending the analysis to later periods would
test whether the patterns we document persist as market structure
evolves. We observe transaction-level data but cannot identify the
same investor across platforms, which limits our ability to measure
portfolio-level effects. Finally, our identification strategy rests on
the assumption that..., which would be violated if...
```

### Em-dash restraint

Use em-dashes very selectively — at most one or two per page. When you reach for an em-dash, first consider whether a comma, semicolon, or parenthetical would serve better. Em-dashes are a spice, not a staple. Overuse (more than 2-3 in a section) makes text look informal and fragmented.

### Limitations and future research: brevity

The limitations subsection should be 1-2 paragraphs (150-300 words), not a catalogue. Each limitation should be framed as a scope condition with a constructive forward reference, not as an apology. Do not enumerate more than 3-4 limitations.

Future research should be 1 short paragraph (100-150 words) identifying 2-3 specific, answerable questions. It is not a wish list. Keep it tight.
