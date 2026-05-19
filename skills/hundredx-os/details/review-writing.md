# Academic Writing Review Checklist

## Purpose

Good academic writing in economics is clear, precise, and efficient. It serves the argument -- it does not draw attention to itself. The goal is to communicate complex ideas so that a busy reader (a referee with 30 papers on their desk) can follow your logic without rereading sentences. This checklist identifies the most common writing problems in economics manuscripts and provides concrete guidance for fixing them.

---

## 1. Clarity

Clarity is the paramount virtue of academic writing. A sentence that a reader must parse twice has failed.

**Check these items:**

- [ ] Each sentence makes exactly one point. Sentences that try to do two things should be split.
- [ ] Technical terms are defined before they are used. Do not assume the reader shares your subfield's jargon.
- [ ] Pronouns have clear antecedents. "This suggests..." -- what does "this" refer to? Replace vague pronouns with specific nouns: "This coefficient suggests..." or "This pattern suggests..."
- [ ] Sentences are direct. Prefer "X causes Y" over "It can be observed that there exists a relationship whereby X is associated with Y in a manner that suggests a causal interpretation."
- [ ] Avoid nominalizations -- turning verbs into nouns. "We performed an estimation of the model" should be "We estimated the model." "The implementation of the policy" should be "Implementing the policy" or "The policy."
- [ ] Each paragraph begins with a topic sentence that tells the reader what the paragraph is about. A reader who reads only the first sentence of each paragraph should be able to follow the paper's argument.
- [ ] Avoid "it is" constructions (expletive "it"). "It is important to note that X" should be "X" -- or if the importance claim matters, "X is important because..."

---

## 2. Argument Flow

A well-structured paper reads like a logical proof: each point follows from the previous one and sets up the next. The reader should never wonder, "Why am I reading this now?"

**Check these items:**

- [ ] The paper follows a clear logical progression. Can you outline the argument in 5--7 bullet points? If not, the structure needs work.
- [ ] Transitions between paragraphs make the logical connection explicit. "Having established that X, we now examine whether Y" is better than a paragraph that simply starts discussing Y.
- [ ] Transitions between sections are smooth. The last paragraph of each section should set up the next section.
- [ ] The introduction's roadmap matches the actual paper structure. If you say "Section 3 presents the model," Section 3 must present the model.
- [ ] No key claim appears without having been motivated or set up. If the reader encounters a claim and thinks "where did this come from?", the flow is broken.
- [ ] The argument does not go in circles. A common problem: the introduction states the finding, the results section restates it, and the conclusion restates it again -- all in nearly identical language. Each section should add something new to the reader's understanding.
- [ ] Digressions are eliminated or moved to footnotes. If a paragraph could be removed without breaking the argument, it probably should be.

---

## 3. Evidence-Claim Alignment

Every empirical claim must be supported by evidence presented in the paper. Every piece of evidence should support a claim. Misalignment between claims and evidence is the most substantive writing problem in economics papers.

**Check these items:**

- [ ] Claims about magnitudes match the reported coefficients. If you say "large effect," quantify what "large" means relative to the mean or to estimates in the literature.
- [ ] Causal language matches the identification strategy. If you have an OLS regression without a credible identification strategy, do not use causal language ("X increases Y"). Use "X is associated with Y" or "X predicts Y."
- [ ] Null results are described accurately. "We find no evidence that X affects Y" is correct. "X does not affect Y" is a much stronger claim that your data may not support (absence of evidence vs. evidence of absence).
- [ ] Confidence intervals or standard errors support the stated precision. A coefficient of 0.05 with a standard error of 0.04 is not "precisely estimated."
- [ ] Subsample results are not overclaimed. Finding a significant effect in one of six subsamples does not constitute strong evidence of heterogeneity -- it may be a multiple-testing artifact.
- [ ] Literature claims are accurate. If you write "Smith (2020) finds that X," verify that Smith actually found X. Mischaracterizing others' results is a serious error.
- [ ] The conclusion does not introduce claims that go beyond the paper's evidence. Policy recommendations should follow directly from the findings.

---

## 4. Hedging Language

Academic writing requires appropriate hedging -- qualifying claims based on the strength of the evidence. But hedging can also weaken writing when overused.

**Appropriate hedging:**
- "Our results suggest that..." (when the evidence is suggestive but not definitive)
- "One possible interpretation is..." (when multiple interpretations exist)
- "Under the assumption that X, our estimates imply..." (when the result depends on an identifying assumption)

**Over-hedging (avoid):**
- "It could potentially be argued that there might be some evidence suggesting..." -- this communicates nothing.
- "We tentatively find..." -- if your finding is robust, do not undermine it.
- "It seems that perhaps..." -- either commit to the claim or explain why you cannot.

**Under-hedging (avoid):**
- "We prove that X causes Y" -- empirical economics rarely proves causal relationships; we provide evidence.
- "Our results definitively show..." -- be honest about limitations.
- Using "we find" when you mean "the data are consistent with." There is a difference.

**Guidelines:**
- [ ] Causal claims are hedged appropriately given the research design.
- [ ] Descriptive findings are stated confidently (no need to hedge a mean).
- [ ] Mechanism evidence is clearly labeled as suggestive.
- [ ] The level of hedging is consistent: do not hedge in one paragraph and overclaim in the next.

---

## 5. Passive Voice

The convention in economics has shifted. Active voice is now strongly preferred by most journals and editors. Passive voice obscures agency, adds words, and makes prose harder to follow.

**Passive (avoid):** "The model was estimated using OLS."
**Active (prefer):** "We estimate the model using OLS."

**Passive (avoid):** "It was found that the policy had a significant effect."
**Active (prefer):** "We find that the policy has a significant effect."

**When passive voice is acceptable:**
- When the agent is truly irrelevant: "The data were collected by Statistics Netherlands as part of a mandatory census." (Who collected the data is secondary.)
- In methods descriptions where the process matters more than who did it: "Standard errors are clustered at the state level."
- In describing institutional processes: "Applicants are randomly assigned to examiners."

**Check these items:**

- [ ] The default is active voice throughout the paper.
- [ ] "We" is used as the subject for the authors' actions (this is standard in economics, even for sole-authored papers, though "I" is also acceptable).
- [ ] Passive constructions are used only when the agent is genuinely unimportant.
- [ ] Search the document for "is estimated," "was found," "are shown," "it was" -- these often indicate unnecessary passive voice.

---

## 6. Paragraph Structure

A paragraph is a unit of thought. It should develop one idea, support it, and connect to the next idea.

**Check these items:**

- [ ] Each paragraph has a topic sentence (usually the first sentence) that states the paragraph's main point.
- [ ] Supporting sentences develop the topic sentence with evidence, examples, or reasoning.
- [ ] Paragraphs are between 3 and 8 sentences. A single-sentence paragraph is almost never appropriate in academic writing. A paragraph longer than 8 sentences probably combines multiple ideas and should be split.
- [ ] The last sentence of each paragraph connects to the next paragraph's topic (transition).
- [ ] Paragraphs within a section follow a logical order. Could the paragraphs be rearranged without loss? If so, the section needs restructuring.

---

## 7. Conciseness

Economics papers are too long. Referees value conciseness. Every sentence should earn its place.

**Common sources of unnecessary words:**

| Wordy | Concise |
|-------|---------|
| "in order to" | "to" |
| "due to the fact that" | "because" |
| "a large number of" | "many" |
| "in the case of" | "for" |
| "it is important to note that" | (delete -- just state the point) |
| "the results of the analysis show" | "the results show" or just state the result |
| "we conduct an analysis of" | "we analyze" |
| "there are several factors that" | "several factors" |
| "at the present time" | "now" or "currently" |
| "has the ability to" | "can" |

**Check these items:**

- [ ] Eliminate filler phrases and throat-clearing sentences.
- [ ] Remove redundant modifiers: "completely eliminated" (just "eliminated"), "very unique" (just "unique"), "past history" (just "history").
- [ ] Combine short sentences that make related points into one clear sentence.
- [ ] Delete sentences that merely announce what you are about to say. "In the next section, we discuss the results" followed immediately by the results section is redundant.
- [ ] Shorten relative clauses where possible: "the workers who were affected by the policy" becomes "affected workers" or "workers affected by the policy."

---

## 8. Consistency

Inconsistency distracts readers and signals carelessness.

**Check these items:**

- [ ] Terminology is consistent. If you call it "treatment group" in Section 3, do not switch to "exposed group" in Section 5 unless there is a reason.
- [ ] Tense is consistent within sections. Use present tense for general claims and discussion ("Table 3 shows..."), past tense for describing what you did ("We estimated...") and what others found ("Smith (2020) found...").
- [ ] Number formatting is consistent: "10 percent" vs. "10%" -- choose one. Numbers below ten are typically spelled out in text; larger numbers use digits.
- [ ] Serial comma usage is consistent (either always use it or never use it; most style guides recommend using it).
- [ ] Hyphenation is consistent: "firm-level data" (hyphenated as a compound modifier) but "at the firm level" (no hyphen when not modifying a noun).

---

## 9. Common Economics-Specific Writing Issues

- [ ] Do not start sentences with symbols or numbers: "10 percent of firms..." should be "Ten percent of firms..." or restructure the sentence.
- [ ] "Data" is treated as plural in formal academic writing: "the data show" not "the data shows." (This convention is fading in general usage but persists in economics journals.)
- [ ] "Significant" means statistically significant in economics papers. If you mean "important" or "substantial," use those words instead to avoid ambiguity.
- [ ] Distinguish between "affect" (verb) and "effect" (noun, usually). "The policy affects wages" vs. "The effect of the policy on wages."
- [ ] Use "fewer" for countable nouns ("fewer observations") and "less" for uncountable nouns ("less variation").
- [ ] "Compared to" introduces a general comparison; "compared with" introduces a specific, detailed comparison. Most economics usage calls for "compared with."

---

## Review Workflow

1. **First pass: Structure.** Read only the first sentence of each paragraph. Does the paper's argument emerge clearly?
2. **Second pass: Evidence-claim alignment.** For every claim, ask: where is the evidence? For every result, ask: what claim does this support?
3. **Third pass: Sentence-level editing.** Clarity, conciseness, active voice, consistency.
4. **Final pass: Read aloud.** Awkward phrasing becomes obvious when spoken. If you stumble over a sentence while reading it aloud, rewrite it.
