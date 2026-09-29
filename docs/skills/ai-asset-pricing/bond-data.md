<!-- DO NOT EDIT — auto-copied from skills/ai-asset-pricing/details/bond-data.md -->

# `/bond-data`

Reference for the Dickerson corporate bond dataset as used with PyBondLab: WRDS-to-PyBondLab column mapping, alternative return columns, value-weight choices, the 1-22 rating encoding, signal clusters and known data traps.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-asset-pricing/">ai-asset-pricing (Alex Dickerson)</a></div><div><b>Category:</b> <code>data-handling</code></div><div><b>Field:</b> finance</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")</code></div><div><b>Updated:</b> 2026-03-11</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-acquisition</code> · <code>data-analysis</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Alexander-M-Dickerson/ai-asset-pricing/contents/.claude/skills/bond-data/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-asset-pricing/bond-data/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/bond-data/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Alexander-M-Dickerson/ai-asset-pricing?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Bond Data Reference

The Dickerson cleaned TRACE corporate bond panel (141 columns, 2.83M rows, 1973-01 to 2025-03). Fetch via `bonds-wrds-expert`, stored in `data/` as Parquet.

### PyBondLab Column Mapping

| Parquet Column | PBL Name | Description |
|---------------|----------|-------------|
| `cusip` | `ID` | 9-digit bond CUSIP |
| `ret_vw` | `ret` | Month-end total return (primary) |
| `mcap_e` | `VW` | Bond market cap at month-end |
| `spc_rat` | `RATING_NUM` | S&P composite rating (1-22) |
| `permno` | `PERMNO` | CRSP equity link (for WithinFirmSort) |

#### Three Mapping Approaches

```python
## Option 1: fit() params (StrategyFormation)
result = sf.fit(IDvar='cusip', RETvar='ret_vw', VWvar='mcap_e', RATINGvar='spc_rat')

## Option 2: rename upfront
data = data.rename(columns={'cusip': 'ID', 'ret_vw': 'ret', 'mcap_e': 'VW', 'spc_rat': 'RATING_NUM'})

## Option 3: Batch columns= dict (pbl_name -> user_name)
batch = pbl.BatchStrategyFormation(
    data=data,
    columns={'ID': 'cusip', 'ret': 'ret_vw', 'VW': 'mcap_e', 'RATING_NUM': 'spc_rat'},
    ...
)
```

#### Real Data Prep

```python
data['spc_rat'] = data['spc_rat'].astype('float64')  # nullable IntegerArray breaks numba
```

### Alternate Return Columns

| Column | When to Use |
|--------|-------------|
| `ret_vw` | **Default.** Use with MMN-adjusted signals |
| `ret_vw_bgn` | Use ONLY with noisy/unadjusted signals (`_mmn` suffix) |
| `ret_vwx` | Excess return (ret_vw minus duration-matched Treasury) |

### VW Column: `mcap_e` vs `mcap_s`

| Column | Definition | When to Use |
|--------|-----------|-------------|
| `mcap_e` | Market cap at end of month t | **Default.** Contemporary with signal |
| `mcap_s` | Market cap at end of month t-1 | Lagged market cap |

### Rating Encoding

`spc_rat`: S&P composite rating (S&P first, Moody's fallback).

| Numeric | Rating | Grade |
|---------|--------|-------|
| 1 | AAA | IG |
| 2-4 | AA+/AA/AA- | IG |
| 5-7 | A+/A/A- | IG |
| 8-10 | BBB+/BBB/BBB- | IG |
| 11-13 | BB+/BB/BB- | HY |
| 14-16 | B+/B/B- | HY |
| 17-19 | CCC+/CCC/CCC- | HY |
| 20-22 | CC/C/D | HY/Default |

**PyBondLab filters:** `rating='IG'` → spc_rat ≤ 10, `rating='NIG'` → spc_rat > 10.

### Signal Clusters

141 columns in 9 clusters:

| Cluster | Key Signals | Count |
|---------|------------|-------|
| Identifiers & Returns | cusip, date, ret_vw, ret_type, rfret | 22 |
| Bond Characteristics | spc_rat, call, fce_val, 144a | 8 |
| Size | mcap_s, mcap_e, sze | 3 |
| Spreads & Duration | cs, md_dur, tmat, ytm, convx, age | 8 |
| Value | bbtm, val_hz, val_ipr | 5 |
| Momentum & Reversal | mom3_1, mom6_1, mom12_1, str, ltr* | 21 |
| Illiquidity | pi, ami, roll, spd_abs, spd_rel | 13 |
| Volatility & Risk | dvol, rvol, ivol_*, var_95, es_90 | 16 |
| Factor Betas | b_mktb, b_dvix, b_defb, b_psb | 41 |

Common test signals: `cs, tmat, mom3_1, mom6_1, mom12_1, bbtm, md_dur, dvol, ami, var_95`

### Data Subsets

| Subset | Filter | Rows | Use Case |
|--------|--------|------|----------|
| Full | None | 2.83M | Includes pre-TRACE (1973+) |
| **TRACE-only** | `date >= '2002-08-01'` | **1.86M** | **Recommended** |
| IG | `spc_rat <= 10` | ~1.6M | Investment grade |
| HY | `spc_rat > 10` | ~1.2M | High yield |

### Gotchas

1. **Multiple bonds per issuer** — one row per tranche per month. Aggregate by `issuer_cusip` or `permno` for firm-level.
2. **`cs_sprd` ≠ credit spread** — it's Corwin-Schultz high-low spread (liquidity). Actual credit spread is `cs`.
3. **`ar_sprd` ≠ adjusted return spread** — it's Abdi-Ranaldo closing price spread (liquidity).
4. **No lead/lag** — all variables sampled at end of month t.
5. **`tret` NULL on recent dates** — use `ret_vw - rfret` for excess returns instead.
6. **19% of bonds lack `permno`** (11% in TRACE-only) — dropped in WithinFirmSort.
7. **`144a` column name** — starts with digit, use `data['144a']`.
8. **`ret_type` values** — `standard`, `default_evnt`, `trad_in_def`. Filter `ret_type == 'standard'` to exclude defaults.
9. **Composite ratings** — `spc_rat` uses S&P first, Moody's fallback. Not pure S&P.
10. **`lib`/`libd` = Latent Implementation Bias** — NOT LIBOR.
11. **Pre-TRACE era (before 2002-08)** — lower quality. Use TRACE-only subset.
12. **Rolling beta start dates** — betas use 36-month windows, start ~2003-08.
