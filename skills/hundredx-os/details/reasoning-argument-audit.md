# Argument Coherence Audit

## Purpose

A publishable paper makes a single coherent argument. Every section exists to advance that argument. This procedure identifies where the argument breaks down -- where claims are unsupported, where sections don't connect, and where the reader would lose the thread.

---

## Step 0: Type III Error Diagnostic — Are We Solving the Right Problem?

Before auditing the argument's coherence, verify that the research question itself is worth answering. A Type III error (Rai, 2017) is answering the wrong question using the right methods. You can be precise, disciplined, and technically strong, yet fail to create value if the underlying problem does not matter.

Problem formulation is the most consequential decision a scholar makes. Run these five tests before proceeding:

### Test 1: Streetlight Effect

Is the paper studying what is important, or what is easy because the data are available? Signs of the streetlight effect:
- The research question follows directly from a dataset the authors happen to have
- The setting is chosen for convenience, not because it is where the phenomenon matters most
- The paper cannot articulate why *this* setting illuminates the problem better than alternatives

Ask: if this dataset did not exist, would anyone consider this question important?

### Test 2: Solution-Driven Research

Is the paper pushing a theory or method in search of a problem, rather than the other way around? Signs:
- The method or model is introduced before the research problem is established
- The contribution reads as "we apply X to Y" rather than "Y is puzzling because..."
- Removing the method/theory leaves no clear intellectual question

Ask: does the paper have a compelling problem independent of the tool used to solve it?

### Test 3: Consequential Gap

If the paper identifies a gap in the literature, does it explain why the gap is consequential? "No one has studied X" is an observation about the literature, not a reason to study X. The gap must matter:
- What decisions are made poorly because this knowledge is missing?
- What theoretical predictions are untested and could be wrong?
- What policy interventions are designed without evidence they work?

Ask: if we filled this gap, what would change in how people think, decide, or act?

### Test 4: Phenomenon-to-Archetype Link

Does the paper connect its immediate phenomenon to a broader, archetypal problem? The phenomenon is specific (e.g., "DeFi protocols lose billions despite public audits"). The archetypal problem is general (e.g., "transparency alone does not prevent exploitation when comprehension costs are high"). A paper that stays at the phenomenon level is a case study. A paper that links to the archetype produces transferable knowledge.

Ask: what general class of problems does this specific phenomenon represent?

### Test 5: Derivative Answer Risk

Will the answer advance knowledge, or essentially reaffirm what we already know in a new setting? Signs of a derivative answer:
- The expected finding is obvious given existing theory
- The paper's value depends entirely on the specific coefficient, not the insight
- A well-read scholar could predict the conclusion from the abstract alone

Ask: what would be surprising about the findings? If nothing, the question may not be worth asking at the current level of ambition.

### Scope Calibration

Finally, assess scope. Both extremes are pitfalls:
- **Too narrow**: The question is answerable but trivial. Only the authors care about the answer.
- **Too diffuse**: The question is important but unanswerable with the proposed methods. The paper promises an ocean and delivers a puddle.

A well-scoped question is one where the proposed methods can deliver a credible answer that matters beyond the specific setting.

**If two or more tests fail, flag this as a Type III error risk before proceeding to the argument audit. A coherent argument built on the wrong question is still the wrong paper.**

---

## Step 1: Extract the Core Claim and Check Motivation Source

Read the introduction and conclusion. State in one sentence:
- **What question does this paper answer?**
- **What is the specific answer?** (Not "we study X" -- what do you find?)
- **Why should the reader care?** (Policy relevance, theoretical implication, or empirical fact that changes how we think about something)

If you cannot state these in one sentence each, the paper has an identity problem. Flag it as the primary issue.

**Motivation source test:** Is the paper motivated by a real-world phenomenon (puzzle, paradox, unexplained observation) or by a gap in the literature? The strongest papers start with something surprising or consequential in the world and then show that existing knowledge does not explain it. If the motivation reads as "no one has studied X" rather than "X happens and we don't understand why," flag it -- the paper is gap-spotting rather than phenomenon-driven. The literature should confirm the question is open, not generate it.

---

## Step 2: Map the Argument Flow

For each section of the paper, identify:

| Section | Claim made | Evidence/logic provided | What it depends on (from earlier) | What it sets up (for later) |
|---------|-----------|------------------------|----------------------------------|---------------------------|

Fill in this table. The argument flows if:
- Each section's claim follows logically from what came before
- Each section provides evidence or reasoning that the reader needs for what comes next
- No section is orphaned (provides nothing that later sections use)

---

## Step 3: Identify Argument Jumps

An argument "jump" is where the paper moves from claim A to claim B without establishing the connection. Common patterns:

1. **The unstated assumption**: "Since X, it follows that Y" -- but X implies Y only if assumption Z holds, and Z is never stated or defended.

2. **The evidence gap**: Section 3 claims the model predicts X. Section 4 tests Y. The reader wonders: how does testing Y validate the prediction of X?

3. **The non sequitur transition**: "Having established X in the previous section, we now turn to Y" -- but Y doesn't follow from X. The transition sentence is doing rhetorical work that the logic doesn't support.

4. **The scope shift**: The introduction promises to explain A. The model explains B. The empirics test C. A, B, and C are related but not the same thing.

For each jump found:
- State what the paper claims the connection is
- State what connection is actually established
- Assess: is this a fixable gap (add a paragraph of reasoning) or a structural problem (the paper is trying to be two papers)?

---

## Step 4: Check Evidence-Claim Alignment

For each empirical result the paper presents:
- **What does the paper claim this result shows?**
- **What does the result actually show?** (Be precise about what the coefficient/statistic measures)
- **Is the leap from result to claim justified?** Common failures:
  - Claiming causation from a correlation
  - Interpreting a coefficient as "large" or "small" without a benchmark
  - Generalizing from a specific sample without discussing external validity
  - Cherry-picking which results to emphasize

---

## Step 5: Assess Justifiability of Each Jump

For each argument jump identified in Step 3, classify:

- **Justifiable**: The connection is standard in the literature and doesn't need explicit defense (e.g., "firms maximize profits" in an IO paper).
- **Needs one paragraph**: The connection can be established with a brief argument or reference to existing work.
- **Needs a subsection**: The connection requires non-trivial reasoning or additional evidence.
- **Structural problem**: The connection cannot be established without fundamentally changing the paper's approach.

---

## Step 6: Produce the Audit Output

For each issue found, provide:

```
ISSUE: [one-sentence description]
LOCATION: [section and paragraph]
SEVERITY: critical | major | minor
TYPE: type_iii_error | unstated_assumption | evidence_gap | non_sequitur | scope_shift | evidence_claim_mismatch
FIX: [specific action to resolve -- not "improve this section" but "add paragraph after Proposition 2 establishing that condition X holds when Y"]
```

Prioritize by severity. A paper with one critical issue and ten minor issues should fix the critical issue first -- fixing minor issues on a structurally broken paper is wasted effort.

---

## Anti-Patterns to Flag

- **The literature review that doesn't serve the argument**: Pages of "Author A found X, Author B found Y" without explaining how this positions the current paper's contribution.
- **The model that doesn't connect to the empirics**: A theoretical section that makes predictions, followed by an empirical section that tests different predictions.
- **The robustness section that undermines the main result**: "Our result is robust to X, Y, and Z" but not robust to the most obvious threat.
- **The conclusion that introduces new claims**: Claims in the conclusion that aren't supported anywhere in the paper.
- **The introduction that oversells**: Promising to "resolve a longstanding debate" when the paper provides one additional piece of evidence.
