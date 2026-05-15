# Intellectual lineage

RISE is a new name for an old project. The threads that converge into
it have been developing for decades; this page situates them.

## e-Science and research infrastructure (2000s)

The first wave of *computing for science as an infrastructure
problem*: grid computing, cyberinfrastructure reports, the rise of
data-intensive science. The methodological commitments — durable
artifacts, shared standards, machine-readable provenance — survive
into RISE intact. What changed is the *unit of automation*: in
e-Science it was the computation; in RISE it is the research
*act* (a literature review, a paper draft, a review).

## Open and reproducible science (2010s)

The replicability crisis in psychology, the credibility revolution
in economics, pre-registration, open data and open code. This wave
established the *normative* commitments that distinguish RISE from
generic AI-for-science: a RISE artifact is judged not only on what
it claims but on whether others can verify the claim. The catalog's
[`outputs_reproducibility`](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md)
dimension is a direct descendant of this tradition.

## Information Systems as a discipline

The IS field has long defended the **sociotechnical** unit of
analysis — neither pure technology nor pure organization, but their
mutual constitution [@sarker2019sociotechnical]. The discipline's
*design-science research* tradition — building artifacts as
scientific contributions, with explicit methodological standards
for what that requires — is the most direct methodological parent
of RISE. The current ISR special issue [@abbasi2026isr] and the
Gopal et al. position piece [@gopal2025inventing] mark the IS
discipline's explicit engagement with GenAI's implications for its
own methods of inquiry.

## AI4Science and the agentic turn

A separate genealogy runs through machine learning. From narrow
predictive models (AlphaFold and its descendants) to **tool-using
agents** ([@schick2023toolformer]) to **autonomous "AI scientists"**
(SakanaAI's first release in 2024 was the inflection point), the
field has accumulated infrastructure for goal-directed,
tool-augmented LLM systems. The framework papers
([@wu2025agenticreasoning], [@park2023generative]) supply the
canonical primitives — planning loops, tool use, memory
streams — that nearly every RISE project in the catalog instantiates.

The catalog projects most squarely in this lineage:
[`sakana-ai-scientist-v1`](../projects/sakana-ai-scientist-v1.md),
[`sakana-ai-scientist`](../projects/sakana-ai-scientist.md),
[`agent-laboratory`](../projects/agent-laboratory.md),
[`robin`](../projects/robin.md).

## Critique and friction (mid-2020s)

Alongside the optimistic build-out, a critical literature emerged.
Concerns about **hallucination** ([@ji2023hallucination],
[@maynez2020faithfulness]), **reasoning faithfulness**
([@chen2025reasoning], [@matton2025walkthetalk]), the **debate
over understanding** ([@mitchell2023understanding]),
**anthropomorphism** ([@peter2025anthropomorphic]), and the
**reception of AI in scholarship** ([@naddaf2025aipeer],
[@gartenberg2026morebetter]) form a counter-current that RISE
must engage rather than route around.

This critical literature is over-represented in the
[papers catalog](../papers/index.md) by design: a knowledge base
that included only the optimistic line would mislead.

## Practitioner literature

A genre of *practitioner essays* has emerged in parallel to the
academic literature — Cunningham on Claude Code for causal
inference [@cunningham2025claudecode], Eberhardt on applied
economics [@eberhardt2025claudecode]. These are tracked in the
papers catalog with `kind: misc` because they are cite-worthy
records of how working researchers actually use these tools, even
when they would not appear in a traditional literature review.

## What RISE adds

The name. The threads above have all been visible for a decade or
more; what was missing was an *explicit subfield identity* that
makes the agentic research pipeline its primary object of design and
study, with sociotechnical accountability built into the
methodological norms. The hope is that naming it makes the work
easier to find, the comparisons easier to draw, and the standards
easier to enforce.
