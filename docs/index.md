# Research Information Systems Engineering

**RISE** is a public knowledge base introducing *Research Information
Systems Engineering* — the design and study of information systems
that **produce scholarly knowledge**, with a focus on agentic research
pipelines.

The repository maintains two curated catalogs:

1. an **academic-papers database** of structured notes on the literature
   that frames RISE;
2. a **projects database** that evaluates agentic research systems
   against a [standard rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).

---

## The RISE pipeline at a glance

```mermaid
%%{init: {'theme':'base','themeVariables': {
  'fontFamily':'-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif',
  'fontSize':'14px'
}}}%%
flowchart LR

    IN["<b>Inputs</b><br/>—<br/>human idea<br/>agentic idea<br/>research question<br/>replication target"]

    DATA["<b>Data layer</b><br/>—<br/>raw datasets<br/>macro · market<br/>administrative<br/>domain corpora"]

    KP["<b>Knowledge Production</b><br/>—<br/><i>Agentic research pipelines</i><br/><br/>ideation · literature synthesis<br/>research design · data analysis<br/>drafting · review"]

    KNOW["<b>Knowledge layer</b><br/>—<br/>literature<br/>prior artifacts<br/>theory · methods"]

    OUT["<b>Outputs</b><br/>—<br/>artifacts<br/>papers · preprints<br/>datasets<br/>replication reports"]

    IN ==> KP
    DATA --> KP
    KNOW --> KP
    KP ==> OUT

    classDef io fill:#e0f2f1,stroke:#00897b,stroke-width:2px,color:#004d40
    classDef side fill:#fffde7,stroke:#f9a825,stroke-width:1.5px,color:#5d4037
    classDef center fill:#fff8e1,stroke:#ff8f00,stroke-width:3px,color:#e65100

    class IN,OUT io
    class DATA,KNOW side
    class KP center
```

A RISE system is any information system that implements some non-trivial
portion of this diagram. Different systems differ in:

- **which inputs** they accept (some take only a fully specified RQ;
  others ideate from scratch);
- **how broadly** they cover the pipeline (single-stage tools vs.
  end-to-end pipelines);
- **how autonomously** the pipeline operates (copilot ↔ society of agents);
- **what artifacts** they produce, and to what reproducibility standard.

The [projects catalog](projects/index.md) scores every system on
these dimensions using the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).

---

## How to use this site

| If you are… | Start at |
|-------------|----------|
| New to the topic | [Concept → Definition](concept/definition.md) |
| Looking for the diagram explained | [Concept → Pipeline anatomy](concept/pipeline-anatomy.md) |
| Surveying existing systems | [Projects](projects/index.md) |
| Looking for the literature | [Papers](papers/index.md) |
| Wanting to contribute | [Contributing](contributing.md) |

## Provenance

This knowledge base is curated by [Björn Hanneke](https://github.com/bhanneke)
(Goethe University Frankfurt). It is licensed CC-BY-4.0; please cite per
[`CITATION.cff`](https://github.com/bhanneke/RISE/blob/main/CITATION.cff).
