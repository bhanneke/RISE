---
name: math-proof
description: Write clear, detailed mathematical proofs for academic papers. Use when
  the user asks to prove a result, derive an equation, justify a claim analytically,
  or expand a proof sketch into a full proof. Also trigger on "prove", "show analytically",
  "derive", "justify mathematically", or "write a proof".
author: Moran Koren <korenmor@bgu.ac.il> (Ben-Gurion University of the Negev)
---

# Math proof

> **Author:** Moran Koren, Ben-Gurion University of the Negev (korenmor@bgu.ac.il). Part of the [Theorist Toolbox](https://github.com/morankor/theorist-toolbox).


Write rigorous mathematical proofs suitable for peer-reviewed academic papers. Every step should be explicit enough that a reader can verify it without filling in gaps. The proof must be a complete proof, not a proof outline — each step should be carefully explained and documented.

## Trigger phrases

- `/math-proof`
- "prove this"
- "show analytically"
- "derive this result"
- "justify mathematically"
- "write a proof"
- "expand this proof"

## Proof strategy

Before writing a single line of algebra, invest time in planning:

### Choose an approach before committing

Consider at least two proof strategies and state why you chose one:
- **Direct proof**: Assume hypotheses, derive conclusion step by step.
- **Proof by contradiction**: Assume the negation; derive a contradiction.
- **Proof by contrapositive**: Prove $\neg Q \Rightarrow \neg P$ instead of $P \Rightarrow Q$.
- **Mathematical induction**: Base case plus inductive step.
- **Constructive proof**: Exhibit the object whose existence you claim.
- **Proof by exhaustion**: Enumerate all cases and handle each.

### Attack the hardest step first

Identify the single most technically demanding step before starting. If you cannot see how to close that step, the entire proof strategy may be wrong. Discovering this before writing three pages of algebra saves significant effort.

### Prove simpler cases as scaffolding

Before tackling the general claim, prove it for a simple special case ($n=1$, $x=0$, a symmetric configuration, etc.). The special case often reveals the structure of the general proof. Label these explicitly as "Special case" or "Warm-up" — they are scaffolding, not the proof itself.

### Retrieve before you generate (RAG)

Before writing any algebra, inventory your tools:
1. **List all theorems and lemmas** you expect to use, by name.
2. For each, confirm it is either (a) well-known (Wikipedia page, standard undergraduate course) or (b) something you will prove inline.
3. Check whether a weaker version of the claim — or a closely related result — is already proved earlier in the paper or in a standard reference. Reuse it rather than reprove it.

Do not attempt the main proof without first knowing which tools are in your kit. Discovering mid-proof that a key lemma is either false or requires its own long proof is the most common cause of a failed proof attempt.

### Sub-agent decomposition

For complex proofs, treat each major sub-claim as an independent proof task:
1. **Identify independent sub-claims**: What facts must be true for the main proof to go through? State each as a precise formal claim.
2. **Prove each sub-claim in isolation**: Each lemma proof stands alone — it should not assume facts from sibling lemmas unless they are explicitly passed in as hypotheses.
3. **Assemble the main proof last**: The main proof should be short and structural, citing the proved lemmas rather than re-deriving their content.
4. **Check the assembly**: Verify that the hypotheses of each lemma are actually satisfied at the call site in the main proof.

This mirrors how AlphaProof handled IMO problems: individual sub-goals are proved and verified independently, then composed into a complete solution. A gap in assembly — using a lemma whose hypotheses are not met — is as fatal as a gap in the lemma itself.

## AlphaProof-inspired pipeline

AlphaProof (DeepMind, 2024) solved IMO problems at silver-medal level using a five-stage loop. Apply the same loop to any proof task:

### Stage 1 — Formalize

Translate the natural-language claim into a precise formal statement before touching any algebra:
- Write hypotheses as a bulleted list of mathematical conditions.
- Write the conclusion as a single mathematical statement.
- Assign explicit names to all objects, functions, and parameters.
- Surface all implicit assumptions (e.g., $n \in \mathbb{N}$, $f$ continuous, $\varepsilon > 0$) and write them down.

If you cannot write a clean formal statement, the claim is ambiguous. Clarify with the user before proceeding.

### Stage 2 — Retrieve

Inventory relevant results (see "Retrieve before you generate" in Proof Strategy above). Do not enter Stage 3 until your toolkit is assembled.

### Stage 3 — Generate with sub-agent decomposition

Decompose into independent sub-claims and prove each in isolation (see "Sub-agent decomposition" above). Consider multiple proof strategies in parallel; abandon any path where the hardest step is not closable.

### Stage 4 — Verify

Apply the mechanistic verifiability check to every line (see Core Principles). For maximum rigor, translate the proof into Lean 4 (see "Lean verification" below). Only accept a step that survives this check.

### Stage 5 — Iterate

If verification fails at a step, do not patch around it. Return to Stage 3, understand why the step fails, and either find a new proof path or state explicitly what additional lemma would be needed to close the gap. A confident-sounding patch over a failed step is worse than an honest "this step requires further work."

## Core principles

### No gaps between steps

Every transition from one equation to the next must be justified. If you use the quotient rule, say so. If you substitute a definition, point to which definition. If a sign is negative, explain why. The reader should never need to work out an intermediate step on their own.

**Bad:**
$$\frac{d}{d\rho}\frac{n_G}{n_B} = \frac{2q-1}{n_B^2} > 0.$$

**Good:**
We compute $\frac{d}{d\rho}(n_G/n_B)$ using the quotient rule. First, the derivatives:
$$\frac{dn_G}{d\rho} = q, \qquad \frac{dn_B}{d\rho} = 1-q.$$
Applying the quotient rule:
$$\frac{d}{d\rho}\frac{n_G}{n_B} = \frac{q \cdot n_B - (1-q) \cdot n_G}{n_B^2}.$$
Expanding the numerator:
$$q[\rho + (1-\rho)q] - (1-q)[\rho + (1-\rho)(1-q)] = \rho(2q-1) + (1-\rho)(2q-1) = 2q-1.$$
Since $q > 1/2$, this is positive.

### State what you want to show before showing it

Open each step with a sentence explaining the goal: "We want to show that $t$ decreases with $\rho$." Then deliver the proof. The reader should know where you are headed before wading into algebra.

### Sign every term

When a derivative or expression appears, immediately state its sign and why. Do not leave sign determination as an exercise. If a quantity is negative because it is a log of a number less than 1, say so explicitly.

### Bridge definitions to usage

When you define a quantity (like a threshold $t$) and then use it in a derivative, explain the connection. Do not jump from "$Y \geq$ [some expression]" to "$t(K,\rho) =$ [formula]" without a sentence like: "Define $t(K,\rho)$ as the minimum number of yes votes required for allocation, i.e., the smallest integer $Y$ satisfying this inequality."

### Show intermediate algebra

Expand products, collect terms, cancel factors. Do not skip from a quotient rule setup to a simplified final form. Show at least one intermediate line where terms are expanded but not yet simplified.

### Explain why results are intuitive

After a formal derivation, add one sentence of economic or mathematical intuition. "The threshold drops because no votes carry less information, so fewer yes votes suffice to outweigh them." This helps the reader connect the math to the model.

### Mechanistic verifiability

Every step should be verifiable as if by a formal proof assistant (Lean, Coq, Isabelle). Before writing each line, ask: "Could this step, in principle, be encoded in formal logic without adding new assumptions?" If not, it is too vague and needs to be broken down further.

Concretely:
- "By continuity, the limit can be exchanged" → state which theorem justifies the exchange (dominated convergence, uniform convergence on compact sets, etc.)
- "The matrix is positive definite" → prove it: show all eigenvalues are positive, or verify the definition directly.
- "This sum converges absolutely" → bound the terms and invoke a comparison test or ratio test explicitly.
- "The two expressions are equal by symmetry" → state which symmetry, and verify it is exact, not approximate.

This principle is the main safeguard against producing a confident-sounding but subtly flawed argument. Natural language makes it easy to hallucinate plausible but incorrect intermediate steps — demanding mechanistic verifiability at each line blocks this failure mode.

### Self-contained proofs

The proof must be self-contained. Only cite well-known theorems — as a rule of thumb, a theorem must be famous enough to have a Wikipedia page or be taught in standard undergraduate courses. Do not invoke obscure or non-existent results. If you need a non-standard lemma, prove it inline.

### Prove the general case, not examples

Never prove a claim only for specific cases or small examples and then assert it holds in general. If you verify a property for $n=1,2,3$, that is evidence, not a proof. You must provide an argument that covers the full generality of the claim. If the general proof is beyond reach, state this explicitly: "We have verified this for $n \leq 5$; the general case remains open."

## Proof structure

### 1. Setup section

- Define all notation up front
- State the model primitives (distributions, parameters, decision rules)
- Write the key quantities as explicit functions of the parameters

### 2. Numbered steps

Each step should:
- **Open** with a plain-language statement of what will be shown
- **Derive** the result with full intermediate algebra
- **Sign** every derivative and explain the sign
- **Close** with boundary values or limiting cases where helpful

### 3. Connecting steps

When one step feeds into the next, say so explicitly: "Substituting the result from Step 1 into the expression for $c_K$..." Do not assume the reader tracks which results carry forward.

### 4. Edge cases and case analysis

Enumerate all cases explicitly. If you claim a result holds "for all $x > 0$", check boundary behavior at $x = 0$ and $x \to \infty$. Do not silently assume non-degeneracy. If the proof requires case splits (e.g., $n$ even vs odd, or an angle acute vs obtuse), handle every case — do not prove one case and assert "the other case is similar" unless the symmetry is genuinely obvious and you state the symmetry.

### 5. QED

End with $\square$ and optionally a one-sentence summary of the full result.

## Common patterns

### Differentiating a ratio $f/g$

Always use the quotient rule explicitly:
$$\frac{d}{dx}\frac{f}{g} = \frac{f'g - fg'}{g^2}.$$
Compute $f'$ and $g'$ separately first, then substitute.

### Signing a log

If $\beta = \log(a/b)$ and you claim $\beta < 0$, show that $a < b$ first with an explicit inequality.

### Chain rule through a CDF

When differentiating $P(Y \geq t(\rho))$ where both $t$ and the distribution parameter depend on $\rho$:
$$\frac{d}{d\rho}P(Y \geq t) = \frac{\partial P}{\partial t}\cdot\frac{dt}{d\rho} + \frac{\partial P}{\partial p}\cdot\frac{dp}{d\rho}.$$
Sign each term separately, then discuss which dominates.

### Discrete vs continuous

When a threshold must be an integer but you differentiate as if it were continuous, flag this: "Treating $t$ as continuous for tractability. In practice, $t$ is an integer, so small changes in $\rho$ can cause discrete jumps in $t$."

### Inequality manipulation

When manipulating inequalities, explicitly justify every direction change. Common errors include: reversing inequality signs when multiplying by a negative quantity without noting it, flipping bounds when taking reciprocals without checking sign, and applying Jensen's inequality in the wrong direction (convex vs concave). After each inequality transformation, re-state which direction the inequality points and why.

### Induction

When using induction, state the base case, the inductive hypothesis, and the inductive step separately. In the inductive step, explicitly mark where the inductive hypothesis is applied. Do not conflate "holds for $n = k$" (hypothesis) with "holds for $n = k+1$" (what you are proving).

### Proof by contradiction

State the negation explicitly: "Suppose, for contradiction, that $P$ does not hold, i.e., [write the negation formally]." Derive the contradiction step by step — do not assert "this leads to a contradiction" without showing the incompatible statements side by side.

### Proof by contrapositive

When proving $P \Rightarrow Q$ by contrapositive, state clearly: "We prove the contrapositive: $\neg Q \Rightarrow \neg P$." Assume $\neg Q$ formally and derive $\neg P$. Close with: "By contrapositive, $P \Rightarrow Q$. $\square$"

### Existence proofs (constructive vs. non-constructive)

When proving existence, prefer constructing the object explicitly. If you use a non-constructive argument (compactness, Zorn's lemma, pigeonhole principle, etc.), name the principle and verify its hypotheses are met. Never assert existence without either a construction or a named existence theorem whose conditions you have checked.

### Proof by cases (exhaustive)

Before proving each case, enumerate all cases and verify they are mutually exclusive and exhaustive. Only then prove each one. Never assert "the other cases are analogous" unless the symmetry is explicit: state which substitution or relabeling maps the proved case onto the others.

## Lean verification

Writing a Lean 4 skeleton is the strongest available correctness check. Use it when any step feels uncertain, when the proof involves intricate induction or non-trivial algebra, or when the user requests a machine-verifiable result.

### When to invoke Lean

- Any step where you are not fully confident.
- Proofs involving induction with non-obvious inductive hypotheses.
- Proofs of equalities or inequalities that require many algebraic manipulations.
- Any proof you are asked to certify as "fully rigorous."

### How to write a Lean 4 skeleton

Write the theorem statement and proof outline, using `sorry` as a placeholder for steps not yet filled in:

```lean
theorem my_claim (h₁ : hypothesis_1) (h₂ : hypothesis_2) : conclusion := by
  -- Stage 1: establish sub-claim A
  have hA : sub_claim_A := by
    sorry
  -- Stage 2: establish sub-claim B using hA
  have hB : sub_claim_B := by
    sorry
  -- Assembly: conclude from hA and hB
  exact final_step hA hB
```

Each `sorry` is a gap that must be closed. If a step in the natural-language proof cannot be expressed in Lean without `sorry`, that step is not rigorous — regardless of how natural it sounds in English.

### The diagnostic value

The points where Lean encoding fails are exactly the points where the proof has gaps. You do not need a complete, compiling Lean proof to benefit from this exercise: even writing the theorem statement forces precision about quantifiers, types, and implicit assumptions that natural language routinely obscures.

If you discover a `sorry` that cannot be eliminated, surface it explicitly in the natural-language proof: "This step has not been formally verified; it relies on [specific claim] which we have not proved."

## Format

- Use `$$` for display equations, `$` for inline
- Use `\triangleq` for definitions, `=` for equalities
- Label equations only if referenced later
- Use `\text{}` for words inside math mode
- Separate steps with `##` headings
- Write in markdown with LaTeX math
- Do not use unicode symbols for math — use LaTeX commands

## What NOT to do

- Do not write "it is easy to see" or "it follows trivially" — if a step is truly trivial, prove it anyway; a reader or reviewer will assume you cannot explain what you cannot be bothered to write
- Do not skip sign justifications
- Do not introduce shorthand notation mid-proof without defining it (e.g., writing $b$ for $|\beta|$ without warning)
- Do not combine multiple algebraic manipulations into one line
- Do not end a step by restating the setup of the next step
- Do not use "clearly" or "obviously"
- Do not assert that one effect "dominates" another without proving it. If the comparison is ambiguous, say so. If you claim A > B, show A > B with an inequality, not with an intuitive argument about where distributions "concentrate"
- Do not claim a monotonicity direction without either a derivative computation or a discrete comparison that establishes the sign
- Distinguish between what is proved and what is conjectured. If a step relies on a plausible but unproved claim, flag it explicitly: "We conjecture that..." or "Numerical evidence suggests..."
- Do not overgeneralize from examples. Proving a statement for specific values ($n = 1, 2, 3$) does not constitute a proof for all $n$ — it is evidence at best. If you cannot prove the general case, say so
- Do not cite theorems or results that are not well-known. If a result would not be taught in a standard undergraduate course and does not have a Wikipedia article, either prove it from scratch or explicitly provide a verifiable reference. Fabricating citations is worse than having a longer proof
- Do not silently omit edge cases or degenerate configurations. If your proof assumes $x \neq 0$ or a matrix is invertible, state and justify the assumption
- If you are uncertain about a step, say so explicitly rather than producing a confident-sounding but potentially wrong argument. "We believe this holds because... but a complete proof requires..." is far better than a flawed claim presented as fact

## Workflow

Follow the AlphaProof-inspired pipeline:

1. **Formalize** (Stage 1): Write hypotheses and conclusion as precise mathematical statements. Surface all implicit assumptions. If the claim is ambiguous, stop and clarify.
2. **Retrieve** (Stage 2): List all theorems and lemmas you expect to use. Confirm each is well-known or provable inline. Check for reusable results already in the paper.
3. **Plan** (Stage 3 entry): Identify the hardest step. Choose a proof strategy (direct, contradiction, induction, etc.) and state why. Prove a simple special case first if it reveals structure.
4. **Decompose**: Identify independent sub-claims. Plan to prove each in isolation before assembling.
5. **Write the Setup section** with all definitions and key quantities as explicit functions of parameters.
6. **Write each sub-proof** with full algebra, signing every term. Apply the mechanistic verifiability check at each line.
7. **Verify** (Stage 4): Check that no step cites a result not yet established. Check boundary cases, edge cases, and limiting behavior. Write a Lean 4 skeleton for any uncertain step.
8. **Add intuition sentences** after key derivations.
9. **Assemble**: The main proof cites the proved lemmas. Verify that each lemma's hypotheses are satisfied at its call site.
10. **Iterate** (Stage 5): If any step fails verification, return to step 3 with a new approach — do not patch over a failed step.
11. **Self-check**: Re-read the full proof for gaps, unjustified sign claims, overgeneralizations from examples, unchecked existence assertions, and cited results that need verification. Translate any user-supplied intuitions into precise statements — do not merely restate the sketch in fancier notation.
