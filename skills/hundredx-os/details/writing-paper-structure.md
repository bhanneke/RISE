# Paper Structure for IS & Management Science Journals

Standard structure for papers targeting Management Science, Information Systems
Research, MIS Quarterly, JMIS, and BISE. Deviations should be deliberate and
justified. The order below reflects what referees at these outlets expect.

---

## 1. Introduction (2--3 pages)

The introduction is the most important section. Referees form their judgment
here. It must accomplish five things in a tight sequence:

**Opening paragraph: The phenomenon.**
Start with a concrete phenomenon, puzzle, or paradox from the real world -- not
a grand statement about technology's importance and not a gap in the literature.
Anchor in something specific that demands explanation: a market failure, a design
choice with non-obvious consequences, an empirical regularity that contradicts
theory, or a tension between what we observe and what we would expect. The reader
should think "that's surprising -- why does that happen?" before they see any
citations.

**The question and why existing knowledge falls short.**
Within the first half-page, state clearly what is unknown or unresolved about
the phenomenon. Frame it as a question the paper answers: "This paper asks
whether..." is stronger than "This paper contributes to the literature on..."
The literature enters here in a supporting role: it confirms that the phenomenon
is not yet explained, not that "no one has studied X." A gap in the literature
is not a motivation -- it is an observation. The motivation is that a real
phenomenon lacks explanation, and existing work does not (fully) provide one.

**What this paper does.**
State the contribution in one or two sentences. Be precise about the method,
data, and setting. Use active voice: "We develop a game-theoretic model of..."
or "We exploit variation in protocol design across DeFi platforms..."

**Preview of results.**
Summarize the main findings in plain economic language. Use magnitudes that
a non-specialist can interpret: "a 12 percent increase," "roughly twice the
baseline rate," "no statistically significant effect." Do NOT report
coefficients ($\hat{\beta}$), p-values, t-statistics, standard errors, or
confidence intervals in the introduction. Those belong in the Results section.
The introduction conveys the story and its direction, not the regression
output. A reader should understand the finding without knowing what a
coefficient is.

Good: "We find that a one-standard-deviation increase in X raises Y by
12 percent."
Bad: "We find $\hat{\beta} = 0.12$ ($p = 0.003$, $t = 2.97$)."
Bad: "The coefficient is significant at the 1% level with Newey-West
standard errors."

**Roadmap.**
Brief final paragraph mapping the rest of the paper. Short and functional.

**Common mistakes:**
- Motivating the paper with a literature gap instead of a phenomenon. "No paper
  has studied X" is not a reason to study X. "X happens and we don't understand
  why" is. The literature should confirm the gap, not create the motivation.
- Spending a full page on background before stating the question.
- Burying the contribution in paragraph four or later.
- Listing contributions without making clear which is the main one.
- Excessive hedging: "This paper attempts to shed some light on..."
- Literature review disguised as an introduction.
- Dumping regression output into the introduction. The introduction previews
  results in plain language (direction + magnitude in interpretable units).
  Coefficients, p-values, t-statistics, and standard errors belong in the
  Results section and its tables, not in the introduction.

---

## 2. Related Work (2--3 pages)

IS journals typically expect a standalone Related Work section (unlike pure
economics journals where it is often folded into the introduction).

**Principles:**
- Organize by contribution strand, not chronologically. Common strands for
  IS research: (a) the phenomenon studied, (b) the theoretical lens used,
  (c) the methodological approach, (d) the empirical setting.
- For each strand, cite the 3--5 most relevant papers and explain how your
  paper differs or extends their work.
- Position relative to both IS and economics literatures. Management Science
  and ISR referees expect awareness of both communities.
- End with a clear statement of how your paper fills the gap across these
  strands. The last paragraph should make the contribution feel inevitable.
- Use phrases like "Most closely related to our work is..." or "We build on
  the framework of..." to signal direct intellectual debts.
- Avoid exhaustive listing. Quality over quantity.

---

## 3. Analytical Model (if applicable)

For papers with a formal model. This section is expected when the paper makes
theoretical contributions or when empirical predictions are derived from a model.

**Structure:**
1. **Setup**: Players, actions, information structure, timing. Define all
   notation in one place. Tie model primitives to the institutional setting
   (e.g., "The platform sets fee f charged to sellers" maps to an observable
   design choice).
2. **Analysis**: Derive equilibrium. State the equilibrium concept. Present
   results as numbered Propositions with formal statements. Provide intuition
   after each proposition.
3. **Predictions**: If empirical tests follow, explicitly list the testable
   predictions as numbered Hypotheses or Predictions derived from the model.
   Map each prediction to the comparative static that generates it.
4. **Proofs**: Relegate to appendix unless short and illuminating.

**For papers without a formal model:**
Skip this section entirely. If you use a conceptual framework without formal
math, integrate it into the methodology section or present it as a brief
"Conceptual Framework" subsection in the introduction. Do not write a model
section that has no equations.

---

## 4. Methodology (including Data)

This section covers both the data and the empirical strategy. The goal is to
convince the reader that your estimates are credible.

### 4.1 Data

1. **Data sources.** Where does the data come from? Administrative records,
   on-chain data, platform APIs, surveys? Is it publicly available?
2. **Sample construction.** How did you arrive at the analysis sample? What
   restrictions did you impose and why? Show sample attrition if applicable.
3. **Variable definitions.** Define all key variables precisely. If you
   constructed indices or transformed variables, explain the procedure.
4. **Summary statistics.** Table 1: means, SDs, sample sizes. Show statistics
   for the full sample and relevant subsamples (treatment vs. control, etc.).

**IS-specific data conventions:**
- For on-chain data: specify chain, block/time range, contract addresses,
  event filters, and data provider (Etherscan, Dune, The Graph).
- For platform data: specify API version, rate limits, and whether data
  represents the full population or a sample.
- For scraped data: describe the scraping methodology, coverage, and any
  deduplication procedures.

### 4.2 Empirical Strategy / Identification

**For all methods:**
- Write out the estimating equation(s) explicitly.
- Define every variable in the equation.
- State the identifying assumption in plain language and formally.
- Discuss threats to identification and how you address them.

**Method-specific guidance:**
- **DiD**: Show parallel trends evidence (event-study plot). Address staggered
  timing with modern estimators (Callaway-Sant'Anna, Sun-Abraham, etc.).
- **IV**: Report first-stage F-statistic. Argue exclusion restriction on
  substantive grounds. Discuss complier population for LATE.
- **RD**: Describe running variable and cutoff. Show bandwidth robustness.
  Test for manipulation (McCrary/Cattaneo density test).
- **Structural estimation**: Specify the model being estimated. Discuss
  identification of structural parameters.

---

## 5. Empirical Estimation Results

**Main results first.** Present the core finding in the first table. Walk the
reader through the table column by column. Discuss magnitude (economic
significance), not just statistical significance.

**Build tables progressively:**
- Column 1: baseline specification.
- Column 2: add controls.
- Column 3: add fixed effects.
- Column 4: preferred specification.
- Column 5: alternative measures or additional controls.

**Robustness and extensions** (subsections within results or separate section):
alternative specifications, samples, variable definitions; placebo and
falsification tests; heterogeneity analysis (state whether pre-specified);
mechanism evidence (be clear this is typically suggestive); sensitivity
analysis (Oster 2019, Conley et al. bounds where applicable).

**Interpretation:**
Translate coefficients into economically meaningful units. Compare
magnitudes to existing estimates in the literature. Be honest about
statistical significance -- a marginally significant result is not
"highly significant."

**Results must be written as prose paragraphs.** Never report results as
bullet points or numbered lists. Each robustness check, heterogeneity
result, or mechanism test is discussed in a paragraph that interprets
the finding and connects it to the paper's argument. Do not write
"Result 1: ..., Result 2: ..., Result 3: ..." — write connected prose.

---

## 6. Discussion (1--2 pages)

IS journals value a Discussion section more than pure economics journals do.
This is where you connect findings back to theory and practice.

**Structure:**
1. **Summary of findings.** What did you find? One paragraph.
2. **Theoretical implications.** How do results advance or challenge existing
   theory? What do they imply for the model (if you have one)?
   **Critical:** Go beyond the specific setting. If your finding implies
   something about a broader class of markets, institutions, or behaviors,
   this is potentially the paper's most important contribution. A null result
   in one setting can be profoundly informative about what drives effects
   in another setting (e.g., if retail-only markets lack seasonality, stock
   market seasonality must be driven by institutional factors — that is a
   general insight, not a setting-specific footnote).
3. **Practical implications.** What should platform designers, regulators,
   or market participants do differently? Be concrete but do not overclaim.
4. **Limitations.** 1-2 paragraphs (150-300 words maximum). Acknowledge the
   3-4 most important scope conditions. Frame constructively, not
   defensively. Write as **flowing prose, NOT as a numbered or bulleted list**.
5. **Future research.** 1 short paragraph (100-150 words). 2-3 specific
   answerable questions. Write as **prose, NOT as a list**.

---

## 7. Conclusion (0.5--1 page)

Short and punchy. Three purposes:

1. **Restate the main finding.** One or two sentences.
2. **Broader significance.** Why does this matter beyond the specific setting?
3. **One-sentence takeaway.** What should the reader remember?

**Do not:**
- Introduce new results or analysis.
- Repeat the introduction verbatim.
- Make sweeping policy recommendations beyond your evidence.
- End with "more research is needed" without specifics.

---

## Formatting Conventions

- **Tables and figures** are numbered sequentially and referenced in the text.
  Every table and figure must be discussed.
- **Appendix** contains supplementary tables, proofs, data construction
  details, and additional robustness checks. Label A1, A2, etc.
- **Online Appendix** for extensive supplementary material (Management Science
  and ISR support this). Put additional robustness, extensions, and
  replication details here.
- **Footnotes** should be used sparingly. If important enough to say, put it
  in the text.
- **Length:** Management Science expects ~30 pages main text. ISR/MISQ similar.
  Appendices and online appendices can be longer.

### No Bullet Points in the Body — MANDATORY

Results, discussion, limitations, future research, and conclusion sections
must be written as **flowing prose paragraphs**. Bullet points and numbered
lists are absolutely forbidden in these sections. This rule has no exceptions.

The only acceptable numbered items in the paper body are: equations,
propositions, hypotheses, and table/figure labels. Everything else is prose.

If you are tempted to write a bulleted list of results or limitations,
restructure as connected paragraphs where each point flows into the next
with proper transitions.

### Em-dash Restraint

Use em-dashes sparingly — at most 1-2 per page. Prefer commas, semicolons,
or parentheticals. Overuse of em-dashes makes text look informal and
AI-generated.

---

## Section-Level Checklist

- [ ] Introduction opens with a phenomenon, puzzle, or paradox (not a literature gap)
- [ ] Introduction states the question within the first half-page
- [ ] Contribution is clearly distinguished from prior work
- [ ] Main results are previewed with magnitudes
- [ ] Related work covers both IS and economics literatures
- [ ] Model predictions map explicitly to empirical tests (if applicable)
- [ ] Data section includes summary statistics table
- [ ] Estimating equation is written out explicitly
- [ ] Identifying assumption is stated in plain language
- [ ] Main results table is discussed column by column
- [ ] Robustness checks address the most plausible threats
- [ ] Discussion connects findings to theory and practice
- [ ] Conclusion does not introduce new material
- [ ] Every table and figure is referenced in the text

---

## Publication Readiness: What Makes Reviewers Say Yes

High-quality papers at Q1 journals are less about "interesting" and more about proof. Before submitting, verify that the paper passes every item below. These are the inverse of the most common rejection reasons.

### Motivation and Contribution Clarity

- [ ] The paper is motivated by a real-world phenomenon, puzzle, or paradox -- not by a gap in the literature
- [ ] The literature is used to confirm the question is open, not to generate the motivation
- [ ] The contribution is stated as one clear, testable sentence: "We show X because Y, validated by Z"
- [ ] The contribution is substantive, not cosmetic (new mechanism or insight, not just a new label on an existing approach)
- [ ] It is clear what the paper adds beyond the 3-5 closest prior papers

### Methods-Claim Alignment

- [ ] The empirical strategy supports the headline claim -- no scope mismatch between what the method identifies and what the paper claims to show
- [ ] Causal language is used only when the identification strategy warrants it
- [ ] If the paper tests a model, the empirical tests map directly to model predictions

### Fair Benchmarking

- [ ] Baselines are state-of-the-art, not outdated or weak
- [ ] All comparisons use matched conditions: same data, same metrics, same time period
- [ ] Exclusions of competing approaches are explained and justified
- [ ] The paper does not cherry-pick which comparisons to report

### Uncertainty and Robustness

- [ ] Sensitivity analysis on the top 3 assumptions that drive the result
- [ ] At least one robustness check per major threat to identification
- [ ] Error analysis or confidence intervals reported, not just point estimates
- [ ] Placebo or falsification tests included where applicable
- [ ] The paper is explicit about what the results are NOT robust to

### Assumption Transparency

- [ ] All key identifying assumptions are stated in plain language (not only in notation)
- [ ] Each assumption is justified on substantive grounds with evidence or institutional knowledge
- [ ] The paper discusses what happens if the most critical assumption is violated

### Auditability

- [ ] Methods are described in the order they were executed
- [ ] Key methodological decisions are in the main text, not buried in footnotes
- [ ] Results can be traced from the estimating equation to the coefficient in the table
- [ ] Reproduction is possible: data availability statement, code, or enough procedural detail to replicate the workflow

### Interpretation Discipline

- [ ] Results are separated from interpretation; speculation is labeled as speculation
- [ ] Magnitude claims are benchmarked (against means, prior estimates, or policy-relevant thresholds)
- [ ] Null results are described accurately ("no evidence that X" rather than "X does not exist")
- [ ] The conclusion does not introduce claims beyond the paper's evidence
