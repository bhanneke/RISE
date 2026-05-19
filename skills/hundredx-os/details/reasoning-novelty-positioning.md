# Novelty and Contribution Positioning

## Purpose

A paper's contribution is not what it does -- it's what it does that hasn't been done before. But the *motivation* for the paper must come from the world, not from the literature. The strongest papers start with a phenomenon, puzzle, or paradox that demands explanation, and only then show that existing knowledge does not resolve it. The literature check is confirmatory -- it verifies that the question is open, it does not generate the question.

This procedure structures the process from phenomenon to positioned contribution.

---

## Step 0: Anchor in a Phenomenon

Before touching the literature, answer these three questions:

1. **What real-world phenomenon, puzzle, or paradox motivates this paper?**
   State it in plain language that a non-specialist would understand. Examples:
   - "DeFi protocols lose billions to exploits despite being publicly auditable code"
   - "Platforms routinely subsidize one side of the market below cost -- why?"
   - "Resale restrictions reduce secondary-market liquidity yet sellers adopt them voluntarily"

2. **Why does this phenomenon need explanation?**
   It should be surprising, consequential, or both. If the phenomenon is obvious and well-understood, there may not be a paper here. The strongest motivations involve a tension: something that happens despite theory predicting it shouldn't, or something that doesn't happen despite incentives suggesting it should.

3. **Who cares and what changes if we understand this?**
   Policy implications, design choices, theoretical understanding -- at least one must be concrete and specific.

If you cannot answer these three questions without referencing other papers, the motivation is literature-driven rather than phenomenon-driven. This is a red flag. "No one has studied X" is not a motivation -- it is an observation about the literature. "X happens and we don't understand why" is a motivation.

**The role of the literature comes next:** once the phenomenon is established, the literature check confirms that existing knowledge does not already explain it. The literature is auxiliary to the motivation, not the source of it.

---

## Step 1: Confirm the Gap via Literature

Now -- and only now -- check whether existing work already resolves the phenomenon identified in Step 0.

Identify the 3-5 closest prior papers. These are NOT the most cited papers in the field. They are the papers a referee would point to and say "how is this different from X?"

Criteria for "closest":
- Same question or very similar question
- Same method applied to different setting (or different method applied to same setting)
- Same setting but different outcome variable
- Most recent paper in this exact space

For each prior paper, document:
- **Full citation** (authors, year, journal)
- **Their question**: What did they ask?
- **Their method**: How did they answer it?
- **Their finding**: What did they find?
- **Their limitation**: What couldn't they do? What did they acknowledge as a gap?

**Critical test:** After reviewing these papers, ask: does the phenomenon from Step 0 remain unexplained? If yes, the paper has a reason to exist -- the literature confirms the gap. If existing work already explains it, the paper needs a different angle or a different phenomenon.

---

## Step 2: Construct the Contribution Matrix

Create a comparison table:

| Dimension | This paper | Prior 1 | Prior 2 | Prior 3 |
|-----------|-----------|---------|---------|---------|
| Question | | | | |
| Setting/data | | | | |
| Method | | | | |
| Key finding | | | | |
| Mechanism | | | | |
| Policy implication | | | | |

The contribution lives in the cells where this paper differs from ALL prior work. If the paper only differs from prior work on one dimension (e.g., different country, same method), the contribution is incremental. If it differs on multiple dimensions, the contribution is potentially substantial -- but the paper must explain WHY the differences matter.

---

## Step 3: Classify the Contribution Type

Every economics paper's contribution falls into one or more categories:

### Empirical contributions
- **New fact**: Documents something that wasn't known (requires genuinely new data or measurement)
- **New identification**: Tests a known question with a more credible strategy
- **New setting**: Applies known methods to a setting where the answer might differ
- **Quantification**: Puts a number on something previously only theorized about
- **Mechanism**: Identifies WHY an established result holds, not just THAT it holds

### Theoretical contributions
- **New model**: A framework that generates predictions not available from existing models
- **New mechanism**: A theoretical channel that explains an empirical puzzle
- **Unification**: Shows that apparently different phenomena arise from the same mechanism
- **Impossibility/existence**: Proves something can or cannot happen under stated conditions

### Methodological contributions
- **New estimator**: A statistical method that solves a problem existing methods don't
- **New data**: Construction of a dataset that enables research not previously possible
- **New measurement**: A way to measure something previously unmeasurable

---

## Step 4: Stress-Test the Contribution Claim

For each claimed contribution, ask:

1. **Is it actually new?** Search for papers that may have done this. The most common rejection reason is "this has been done before."

2. **Is the difference meaningful?** "We use more recent data" is not a contribution unless the answer is expected to differ over time, and you explain why.

3. **Is the improvement substantial?** "We use a better instrument" -- how much better? Does it change the conclusion, or just narrow the confidence interval?

4. **Would the field care?** A technically correct contribution that answers a question nobody is asking is unlikely to be published in a good outlet.

5. **Is the answer derivative?** Could a reasonably informed reader have predicted this finding without seeing the evidence? If the paper confirms what most people already suspected, the contribution is incremental at best. The finding must teach something that could not have been guessed from prior work.

6. **Does it link to an archetypal problem?** A paper that documents a pattern in one specific setting ("X happens in NFT markets") without connecting it to a broader economic mechanism (market microstructure, information asymmetry, investor behavior, institutional design) is just description. The strongest papers use their specific setting as a lens onto a general phenomenon. Ask: "If I strip away the specific setting, what fundamental economic question does this paper illuminate?"

7. **Does it generate reverse insights?** Sometimes the most valuable contribution is what a null result implies about other settings. If a well-documented effect in market A does not appear in market B, that absence is informative — it tells us something about what drives the effect in market A. These "reverse insights" should be elevated, not buried. Ask: "What does the absence of this effect tell us about where the effect DOES appear?"

---

## Step 5: Write the Positioning Paragraph

The contribution paragraph (typically at the end of the introduction) must do three things:

1. **Acknowledge the closest prior work** by name. Never pretend you're the first to study something when you're not.

2. **State what you do differently** in concrete terms. Not "we extend their analysis" but "we exploit a policy reform in [country] that provides exogenous variation in X, allowing us to identify the causal effect that [Prior 1] could only estimate as a correlation."

3. **Explain why the difference matters**. Not just that you use different data, but why your data answers the question better or answers a different question worth answering.

### Template (adapt, don't copy verbatim):

"Our paper relates most closely to [Prior 1] and [Prior 2]. [Prior 1] [what they did]. We differ in [specific difference], which allows us to [what this enables]. [Prior 2] [what they did]. Relative to their work, our contribution is [specific contribution]. Our findings [complement/contradict/extend] theirs by showing that [specific finding]."

### Anti-patterns:
- "To the best of our knowledge, this is the first paper to..." -- Almost always false. Be specific about what's new instead.
- Listing 20 papers in the contribution paragraph. Focus on the 3-5 closest.
- Claiming contribution by combining dimensions: "We are the first to study X in country Y using method Z." This is technically true but usually not a real contribution unless you explain why the combination matters.
- Positioning against strawmen: comparing your careful analysis to a vague "existing literature" instead of specific papers.

---

## Step 6: Map Contribution to Outlet Standards

Different outlets value different types of contributions:

- **Top-5 journals**: Need either a new important fact, a new credible identification of a first-order question, or a model that changes how we think about something. Incremental improvements rarely suffice.
- **Top field journals**: Accept new settings and methods if the question is important to the field. Quality of execution matters more than novelty.
- **Good field journals**: Accept solid execution of established methods on questions relevant to the field. Still need a clear "what's new" statement.

Match the paper's actual contribution type against what the target outlet publishes. If there's a mismatch, flag it -- the paper may need to be repositioned or targeted to a different outlet.
