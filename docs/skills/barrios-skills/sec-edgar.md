<!-- DO NOT EDIT — auto-copied from skills/barrios-skills/details/sec-edgar.md -->

# `sec-edgar`

Companion skill for Stefano Amorelli's sec-edgar-mcp (not vendored because it is AGPL). Covers CIK resolution, 10-K/10-Q/8-K retrieval, XBRL financial-statement facts, and Form 3/4/5 insider trades. It sets an iron law of no claim without sample inspection, requires a real SEC User-Agent, and warns that filing date and event date can differ for 8-Ks and that XBRL history is restated, so accession numbers must be pinned for replication. Sends Compustat/CRSP panel work to the `wrds` skill.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../barrios-skills/">Barrios Skills (John Manuel Barrios)</a></div><div><b>Category:</b> <code>data-handling</code></div><div><b>Field:</b> accounting</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2026 John Barrios"). The vendored third-party skills keep their own terms: the Anthropic document skills say "Proprietary. LICENSE.txt has complete terms", and the K-Dense skills carry per-library licence lines.</code></div><div><b>Updated:</b> 2026-07-23</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-acquisition</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Barrios88/barrios-skills/contents/skills/research-tools/sec-edgar/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/barrios-skills/sec-edgar/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Barrios88/barrios-skills/blob/main/skills/research-tools/sec-edgar/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Barrios88/barrios-skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

> **Barrios Skills** — John Barrios's curated workflow for economists and accountants. Prioritize reproducible empirical work, clear identification language, and journal-ready output.

### SEC EDGAR MCP (recommended for AI agents)

Use Stefano Amorelli's **sec-edgar-mcp** (built on edgartools) when the agent needs live filings.

**Before querying EDGAR, the user must:**

1. Follow **install/sec-edgar-mcp.md**
2. Set a real User-Agent: `SEC_EDGAR_USER_AGENT="Name (email@institution.edu)"` (SEC fair-access requirement)
3. Prefer MCP tools over ad-hoc scraping when the server is registered

**When to use WRDS instead:** Compustat fundamentals panels, CRSP returns, CCM links, ExecuComp, ISS, TRACE/TAQ — use the `wrds` skill + wrds-mcp. EDGAR is for filing text, XBRL facts, 8-K events, and public insider Forms 3/4/5 when you do not need WRDS panel infrastructure.

---

## SEC EDGAR for accounting & finance research

### Iron law: no claim without sample inspection

Before asserting that a filing pull "worked":

1. **IDENTIFY** the firm (CIK or ticker → CIK) and form type
2. **VALIDATE** the accession / period you intended
3. **EXECUTE** the pull
4. **INSPECT** a sample (company name, filing date, section heading, one numeric fact)
5. **CITE** the EDGAR URL in notes so numbers are auditable

#### Rationalization table — stop if you think

| Excuse | Reality | Do instead |
|--------|---------|------------|
| "Ticker is enough" | Tickers recycle; CIK is stable | Resolve CIK first, store it |
| "XBRL equals Compustat" | Tag coverage and restatements differ | Document source; reconcile if both used |
| "I'll scrape HTML tables" | Layout breaks; XBRL/MCP is stabler | Prefer XBRL facts or MCP financials tools |
| "Form 4 = Insider Trading database" | Public EDGAR ≠ cleaned WRDS panels | Use WRDS for research panels when available |

### Typical workflows

#### 1. Company → filings

- Resolve **CIK** from name or ticker
- List recent **10-K / 10-Q / 8-K** with filing dates
- Extract a section (e.g. Item 1A, MD&A) only when needed — avoid dumping full HTML into context

#### 2. Financial statement facts

- Prefer XBRL-parsed balance sheet / income / cash flow from MCP
- Record units, scale, and period end
- Flag: never invent a ratio; compute from retrieved facts and show the formula

#### 3. Insider trades (Form 3/4/5)

- Pull transactions for a CIK and date window
- Note: open-market vs award/grant; role of reporting person
- For large-sample insider studies, prefer WRDS/Thomson when the user has access

### Accounting / finance research notes

- **Identification language:** filing date ≠ event date for some 8-Ks; use the relevant timestamp the paper needs
- **Restatements:** XBRL history can change; pin accession numbers in replication folders
- **Fair access:** respect SEC rate limits; never share another researcher's User-Agent email
- **Replication:** save accession numbers + URLs alongside any extracted table

### Output checklist

- [ ] CIK recorded
- [ ] Form type and accession (or filing URL) recorded
- [ ] Sample row/section inspected
- [ ] WRDS vs EDGAR choice justified if both could apply
