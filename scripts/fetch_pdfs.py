"""Fetch open-access PDFs for every paper in papers/references.bib.

Sources, in order of preference:
  1. arXiv (for entries with `eprint = {YYMM.NNNNN}`)
  2. AISeL direct (for JAIS DOIs of the form 10.17705/1jais.NNNNN)
  3. NBER (for techreport entries with `number = {wNNNNN}`)
  4. Unpaywall API (any DOI — finds the best open-access copy)

Output: papers/pdfs/<citekey>.pdf  (gitignored — large binary)
        papers/pdfs/FETCH_LOG.csv  (citekey, status, source, url, bytes)

Usage:
    python scripts/fetch_pdfs.py                  # fetch all
    python scripts/fetch_pdfs.py --citekey foo    # one paper
    python scripts/fetch_pdfs.py --dry-run        # only print what would be fetched
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BIB = ROOT / "papers" / "references.bib"
OUT_DIR = ROOT / "papers" / "pdfs"
LOG = OUT_DIR / "FETCH_LOG.csv"

UA = "RISE-fetcher/0.1 (mailto:hanneke@wiwi.uni-frankfurt.de)"
# Some publishers (AISeL, Tandfonline) reject our polite UA — use a browser one
# when fetching their PDFs. We still set a proper UA for API calls.
BROWSER_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


def parse_bib() -> list[dict[str, str]]:
    """Parse references.bib into a list of dicts."""
    text = BIB.read_text(encoding="utf-8")
    entries = []
    for m in re.finditer(r"@(\w+)\{([^,]+),(.+?)\n\}", text, re.DOTALL):
        kind, citekey, body = m.group(1), m.group(2).strip(), m.group(3)
        fields = {"_kind": kind, "_citekey": citekey}
        for fm in re.finditer(
            r"^\s*(\w+)\s*=\s*[\{\"]([^}\"\n]+)", body, re.MULTILINE
        ):
            fields[fm.group(1)] = fm.group(2).strip().strip(",")
        entries.append(fields)
    return entries


def download(url: str, dest: Path, browser_ua: bool = False) -> tuple[bool, str]:
    """Download a URL to dest. Returns (ok, message)."""
    ua = BROWSER_UA if browser_ua else UA
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": ua, "Accept": "application/pdf,*/*"}
        )
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
        if len(data) < 1000:
            return False, f"too small ({len(data)} bytes)"
        if not (data[:5] == b"%PDF-" or data[:4] == b"%PDF"):
            return False, f"not a PDF ({data[:20]!r})"
        dest.write_bytes(data)
        return True, f"{len(data)} bytes"
    except urllib.error.HTTPError as e:
        # Retry once with browser UA if we haven't already
        if e.code in (403, 406) and not browser_ua:
            return download(url, dest, browser_ua=True)
        return False, f"HTTP {e.code}"
    except Exception as e:
        return False, str(e)[:80]


def try_arxiv(arxiv_id: str, dest: Path) -> tuple[bool, str, str]:
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    ok, msg = download(url, dest)
    return ok, "arxiv", url if ok else msg


def try_aisel(doi: str, dest: Path) -> tuple[bool, str, str]:
    """JAIS DOIs (10.17705/1jais.NNNNN) and similar AISeL-hosted papers.

    bepress article IDs are not the DOI suffix — must scrape the
    abstract page (followed via doi.org redirect) for the viewcontent.cgi
    download URL.
    """
    if not (doi.startswith("10.17705/") or doi.startswith("10.17705 ")):
        return False, "aisel", "not an AISeL DOI"
    # Resolve DOI → AISeL abstract page
    try:
        req = urllib.request.Request(
            f"https://doi.org/{doi}", headers={"User-Agent": UA}
        )
        with urllib.request.urlopen(req, timeout=30) as r:
            html = r.read().decode("utf-8", errors="ignore")
            abstract_url = r.url
    except Exception as e:
        return False, "aisel", f"doi-redirect: {str(e)[:60]}"

    # Find viewcontent.cgi link in the abstract page HTML
    m = re.search(
        r'href="(https?://aisel\.aisnet\.org/cgi/viewcontent\.cgi\?[^"]+context=jais[^"]*)"',
        html,
    )
    if not m:
        # Sometimes the URL is relative
        m = re.search(
            r'href="(/cgi/viewcontent\.cgi\?[^"]+context=jais[^"]*)"', html
        )
        if m:
            pdf_url = "https://aisel.aisnet.org" + m.group(1)
        else:
            return False, "aisel", f"no PDF link in {abstract_url}"
    else:
        pdf_url = m.group(1)

    # bepress uses HTML entity for ampersand sometimes
    pdf_url = pdf_url.replace("&amp;", "&")
    ok, msg = download(pdf_url, dest)
    return ok, "aisel", pdf_url if ok else msg


def try_aisel_url(url: str, dest: Path) -> tuple[bool, str, str]:
    """For ICIS proceedings entries that have only a URL (no DOI)."""
    if "aisel.aisnet.org" not in url:
        return False, "aisel-url", "not an AISeL URL"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            html = r.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return False, "aisel-url", f"fetch: {str(e)[:60]}"
    m = re.search(
        r'href="(/cgi/viewcontent\.cgi\?[^"]+)"', html
    )
    if not m:
        return False, "aisel-url", "no PDF link"
    pdf_url = "https://aisel.aisnet.org" + m.group(1).replace("&amp;", "&")
    ok, msg = download(pdf_url, dest)
    return ok, "aisel-url", pdf_url if ok else msg


def try_nber(number: str, dest: Path) -> tuple[bool, str, str]:
    m = re.match(r"w?(\d+)", number)
    if not m:
        return False, "nber", "not a w-number"
    url = f"https://www.nber.org/system/files/working_papers/{number}/{number}.pdf"
    ok, msg = download(url, dest)
    return ok, "nber", url if ok else msg


def try_unpaywall(doi: str, dest: Path) -> tuple[bool, str, str]:
    """Find the best open-access copy via Unpaywall."""
    api = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi, safe='/')}?email=hanneke@wiwi.uni-frankfurt.de"
    try:
        with urllib.request.urlopen(api, timeout=30) as r:
            data = json.loads(r.read())
    except Exception as e:
        return False, "unpaywall", f"api: {str(e)[:60]}"
    best = data.get("best_oa_location") or {}
    pdf_url = best.get("url_for_pdf")
    if not pdf_url:
        return False, "unpaywall", "no OA copy"
    ok, msg = download(pdf_url, dest)
    return ok, f"unpaywall→{best.get('host_type','?')}", pdf_url if ok else msg


def fetch_one(entry: dict[str, str], dry: bool) -> dict[str, str]:
    citekey = entry["_citekey"]
    dest = OUT_DIR / f"{citekey}.pdf"
    if dest.exists():
        return {"citekey": citekey, "status": "exists",
                "source": "cached", "detail": f"{dest.stat().st_size} bytes"}

    if dry:
        return {"citekey": citekey, "status": "dry-run",
                "source": "—", "detail": "would attempt fetch"}

    # 1. arXiv
    aid = entry.get("eprint")
    if aid:
        ok, src, detail = try_arxiv(aid, dest)
        if ok:
            return {"citekey": citekey, "status": "ok",
                    "source": src, "detail": detail}

    # 2. AISeL (JAIS)
    doi = entry.get("doi")
    if doi:
        ok, src, detail = try_aisel(doi, dest)
        if ok:
            return {"citekey": citekey, "status": "ok",
                    "source": src, "detail": detail}

    # 3. NBER
    if entry.get("_kind") == "techreport" and entry.get("number"):
        ok, src, detail = try_nber(entry["number"], dest)
        if ok:
            return {"citekey": citekey, "status": "ok",
                    "source": src, "detail": detail}

    # 4. Unpaywall
    if doi:
        ok, src, detail = try_unpaywall(doi, dest)
        if ok:
            return {"citekey": citekey, "status": "ok",
                    "source": src, "detail": detail}

    # 5. URL-based AISeL (ICIS / AMCIS proceedings without DOI)
    url = entry.get("url", "")
    if "aisel.aisnet.org" in url:
        ok, src, detail = try_aisel_url(url, dest)
        if ok:
            return {"citekey": citekey, "status": "ok",
                    "source": src, "detail": detail}

    # Classify the reason so the user knows what to do manually
    reason = "no open-access copy located"
    if doi:
        if doi.startswith("10.17705/"):
            reason = (
                "AISeL paper — publicly hosted but blocked by AWS WAF challenge. "
                f"Manual download: resolve https://doi.org/{doi} in a browser."
            )
        elif doi.startswith("10.1287/"):
            reason = f"INFORMS paywall — manual access needed via library: https://doi.org/{doi}"
        elif doi.startswith("10.1080/0960085X"):
            reason = f"EJIS (Tandfonline) paywall — manual access needed via library: https://doi.org/{doi}"
        elif doi.startswith("10.25300/misq"):
            reason = f"MISQ paywall — manual access needed via library: https://doi.org/{doi}"
        elif doi.startswith("10.1073/pnas"):
            reason = f"PNAS — usually open after 6 months; check https://doi.org/{doi}"
        elif doi.startswith("10.1145/"):
            reason = f"ACM Digital Library — paywall; manual access: https://doi.org/{doi}"
        else:
            reason = f"No OA copy via Unpaywall. Manual: https://doi.org/{doi}"
    elif "ssrn.com" in (url or ""):
        reason = (
            "SSRN — abstract page is Cloudflare-protected against bots. "
            f"Manual download: {url} (sign-in may be required)"
        )

    return {"citekey": citekey, "status": "no-oa",
            "source": "—", "detail": reason}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--citekey", help="fetch only this entry")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    entries = parse_bib()
    if args.citekey:
        entries = [e for e in entries if e["_citekey"] == args.citekey]
        if not entries:
            print(f"No bib entry with citekey: {args.citekey}", file=sys.stderr)
            return 1

    results = []
    for e in entries:
        print(f"  {e['_citekey']:36}", end=" ", flush=True)
        r = fetch_one(e, args.dry_run)
        results.append(r)
        print(f"{r['status']:8} {r['source']:20} {r['detail']}")
        time.sleep(0.5)  # be polite

    # Write log
    if not args.dry_run:
        with LOG.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["citekey", "status", "source", "detail"])
            w.writeheader()
            w.writerows(results)

    ok = sum(1 for r in results if r["status"] == "ok")
    cached = sum(1 for r in results if r["status"] == "exists")
    failed = sum(1 for r in results if r["status"] == "no-oa")
    print(f"\n=== Summary ===")
    print(f"Fetched: {ok}")
    print(f"Already cached: {cached}")
    print(f"No OA copy: {failed}")
    print(f"Total entries: {len(results)}")
    print(f"Log: {LOG.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
