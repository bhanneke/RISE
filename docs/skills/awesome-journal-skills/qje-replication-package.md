<!-- DO NOT EDIT — auto-copied from skills/awesome-journal-skills/details/qje-replication-package.md -->

# `qje-replication-package`

Builds the reproducible data-and-code deposit required for accepted empirical papers under QJE's data-availability policy.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-journal-skills/">Awesome Journal Skills (AJS)</a></div><div><b>Category:</b> <code>replication</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>replication</code> · <code>dissemination</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Awesome-Journal-Skills/contents/Quarterly-Journal-of-Economics-Skills/skills/qje-replication-package/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-journal-skills/qje-replication-package/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/Quarterly-Journal-of-Economics-Skills/skills/qje-replication-package/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Awesome-Journal-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Replication Package (qje-replication-package)

### When to trigger

- The paper is heading toward acceptance and a data/code deposit is required
- You want a reproducible pipeline early, to pre-empt referee replication requests
- A reproducibility check or data editor asked for materials that regenerate every exhibit
- Raw data are restricted/proprietary and you need a disclosure-compliant plan

### Why this matters at QJE

QJE's policy: it **publishes papers only if the data are clearly documented and readily available for replication**, and authors of accepted empirical/simulation/experimental papers must, prior to publication, provide the **data, programs, and computation details** sufficient to replicate the results. These are posted to the **QJE Dataverse** (the journal's repository on Harvard Dataverse), not openICPSR — a concrete difference from the AEA journals, even though QJE explicitly **adopted the AER data availability policy**. Source: academic.oup.com/qje/pages/data_policy. Proprietary-data exemptions exist but are narrow: you must **flag proprietary data in the cover letter at submission**, and even with an approved exemption you must still deposit the **programs** (the exemption criterion is that another investigator could in principle obtain the data independently). A `README` PDF documenting each file and how to run replication is required. The durable requirement is fixed: a stranger should regenerate every number, table, and figure from your deposit. Funding/conflict disclosure follows the **AEA Disclosure Policy**.

### Package anatomy

```
replication/
  README.{md,pdf}        # the contract: data sources, software, run order, runtime
  data/
    raw/                 # as obtained (or access instructions if restricted)
    derived/             # built by code, never hand-edited
  code/
    00_setup            # installs/pins packages, sets paths
    01_build            # raw -> analysis sample
    02_analysis         # analysis sample -> estimates
    03_exhibits         # estimates -> every table & figure
  output/
    tables/  figures/    # regenerated, byte-checked against the paper
```

### README must specify

- **Data provenance**: every source, version/vintage, access date; for restricted data, exact application steps and who can obtain it.
- **Software environment**: Stata/R/Python versions and *pinned* package versions (e.g., a `requirements.txt`, `renv.lock`, or a list of `ssc`/`net` packages with versions).
- **Run instructions**: a single master script (`run_all`) and the order; expected wall-clock runtime and hardware.
- **Mapping**: a table linking every exhibit in the paper to the script and line that produces it.
- **Seeds**: set and report random seeds for any simulation, bootstrap, or randomization inference.

### Restricted-data plan

- State clearly which results can be reproduced with public data and which require restricted access. Per QJE policy, flag proprietary data in the **cover letter at submission**; even with an exemption you still deposit the **programs**, and the access path must let another investigator obtain the data in principle.
- Provide code that runs against the restricted data plus a synthetic or public subsample so the pipeline is checkable end-to-end.
- Include the data-use agreement constraints and a disclosure-review note where applicable.

### Checklist

- [ ] One master script regenerates every table and figure from raw inputs
- [ ] Software and package versions are pinned and documented
- [ ] Every exhibit maps to a specific script/line in the README
- [ ] Random seeds set and reported for all stochastic steps
- [ ] Restricted/proprietary data have documented access steps + a runnable proxy
- [ ] No hand-edited derived data; all derived files are code-produced
- [ ] Absolute paths removed; runs from a single configurable root
- [ ] Output regenerated and checked against the manuscript numbers
- [ ] Deposit staged for the **QJE Dataverse** (not openICPSR); README PDF included
- [ ] Proprietary data flagged in the cover letter; programs deposited even if data exempt

### Anti-patterns

- A zip of do-files with no README and no run order
- Hard-coded local paths (`/Users/me/Desktop/...`) that break on any other machine
- Derived datasets edited by hand and not reproducible from raw data
- Unpinned packages, so results drift with the next package update
- "Data available on request" with no access procedure for restricted sources
- Missing seeds, so bootstrap/RI numbers cannot be reproduced
- Assuming the deposit is optional — at QJE it gates publication of accepted empirical papers

### Output format

```
【Master script】run_all present? [Y/N]
【Env pinned】Stata/R/Python versions + package versions documented? [Y/N]
【Exhibit map】every table/figure mapped to code? [Y/N]
【Seeds】set + reported? [Y/N]
【Restricted data】access steps + runnable proxy? [Y/N / NA]
【Reproduced output】matches paper? [Y/N]
【Next step】qje-referee-strategy
```
