<!-- DO NOT EDIT — auto-copied from skills/barrios-skills/details/financial-text-nlp.md -->

# `financial-text-nlp`

Sentiment and stance measurement for 10-K/10-Q MD&A, risk factors, 8-Ks, earnings-call transcripts and central-bank communication, using FinBERT (ProsusAI) as the main classifier and FinVADER as a transparent lexicon robustness check. Its iron law is to define the unit of text and the label before scoring. Scores are tied to accession or transcript IDs, boilerplate dilution is flagged, and the research design must state whether sentiment enters as outcome, covariate or instrument, with NLP error treated as measurement error.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../barrios-skills/">Barrios Skills (John Manuel Barrios)</a></div><div><b>Category:</b> <code>analysis</code></div><div><b>Field:</b> finance</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2026 John Barrios"). The vendored third-party skills keep their own terms: the Anthropic document skills say "Proprietary. LICENSE.txt has complete terms", and the K-Dense skills carry per-library licence lines.</code></div><div><b>Updated:</b> 2026-07-23</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-analysis</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Barrios88/barrios-skills/contents/skills/research-tools/financial-text-nlp/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/barrios-skills/financial-text-nlp/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Barrios88/barrios-skills/blob/main/skills/research-tools/financial-text-nlp/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Barrios88/barrios-skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

> **Barrios Skills** — John Barrios's curated workflow for economists and accountants. Prioritize reproducible empirical work, clear identification language, and journal-ready output.

## Financial & economic text NLP

### When to use

- Tone of MD&A, risk factors, 8-K text, or ESG/boilerplate sections
- Earnings-call transcripts (prepare/Q&A separately when possible)
- Central-bank or supervisory communications (hawkish/dovish stance)
- Building panel covariates (firm–year sentiment) for regressions in `pyfixest` or Stata

**Not for:** casual product reviews or generic Twitter sentiment without a finance lexicon/model.

### Tool map

| Task | Tool | Notes |
|------|------|-------|
| General financial tone | [FinBERT](https://huggingface.co/ProsusAI/finbert) (ProsusAI) | Sentence/chunk classification: positive/negative/neutral |
| Lexicon baseline | [FinVADER](https://github.com/PetrKorab/FinVADER) | Fast, transparent; good robustness check |
| Central-bank stance | [CentralBankRoBERTa](https://github.com/Moritz-Pfeifer/CentralBankRoBERTa), [WorldCentralBanks](https://github.com/gtfintechlab/WorldCentralBanks) | Domain labels ≠ FinBERT polarity |
| Econ NER / domain LM | [EconBERTa](https://github.com/worldbank/econberta-econie) | Entity/paper domain — not a drop-in sentiment score |
| Document → text | `sec-edgar`, markitdown/Docling | Get clean text before scoring |

### Iron law: define the unit and the label

1. **Unit of analysis:** sentence, paragraph, section, or full document (document scores need aggregation rules)
2. **Label meaning:** polarity ≠ hawkishness ≠ forward-looking statements
3. **Train/test hygiene:** do not tune thresholds on the same sample used for causal estimates
4. **Inspect:** print 10 scored excerpts before merging to Compustat

### Minimal FinBERT pattern

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_id = "ProsusAI/finbert"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)

def score_texts(texts: list[str], max_length: int = 256):
    inputs = tokenizer(
        texts, padding=True, truncation=True, max_length=max_length, return_tensors="pt"
    )
    with torch.no_grad():
        probs = torch.nn.functional.softmax(model(**inputs).logits, dim=-1)
    # labels: positive, negative, neutral (confirm order via model.config.id2label)
    return probs
```

Aggregate to firm–year with an explicit rule (mean of sentence scores; or net positivity = pos − neg). Document the rule in the paper.

### Accounting / finance research notes

- **Boilerplate:** length and legalese dilute tone — consider section fixed effects or residuals
- **Attribution:** link scores to accession IDs / transcript IDs for replication
- **Identification:** sentiment as outcome vs covariate vs instrument — state which; NLP error is measurement error
- **Robustness:** report FinBERT + lexicon (FinVADER) or alternative chunking

### Checklist

- [ ] Text source and cleaning steps logged
- [ ] Model id + revision pinned
- [ ] Aggregation rule written down
- [ ] Hand-checked excerpts saved
- [ ] Merge keys to firm identifiers validated (CIK / gvkey / ticker map)
