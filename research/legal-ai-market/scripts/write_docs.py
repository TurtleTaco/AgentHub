#!/usr/bin/env python3
"""Generate markdown reference docs from the final dataset (reproducible)."""
import json
import os
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(ROOT, *p)  # noqa: E731


def fm(v):
    if v is None:
        return "—"
    return f"${v / 1000:.1f}B" if v >= 1000 else f"${v:.0f}M" if v >= 10 else f"${v:.1f}M"


def main():
    C = json.load(open(J("data", "companies.json")))
    ont = json.load(open(J("ontology", "ontology.json")))
    mm = json.load(open(J("ontology", "mindmap.json")))
    stats = json.load(open(J("report", "stats.json")))
    take = json.load(open(J("report", "takeaways.json")))
    light = json.load(open(J("data", "acquired_defunct.json")))
    excl = json.load(open(J("data", "excluded.json")))
    by = {c["cid"]: c for c in C}
    doms = ont["facets"]["A_domain"]["domains"]
    tree = {d["id"]: d for d in mm["tree"]["children"]}
    ncat = sum(len(d["categories"]) for d in doms)
    emp_proxy = {"5001+": 5000, "1001-5000": 1500, "501-1000": 400, "201-500": 120}
    raise_key = lambda c: -(c["total_raised_usd_m"] if c.get("total_raised_usd_m") is not None else emp_proxy.get(c.get("employees_bin"), 0))  # noqa: E731

    # ---------- ontology/README.md ----------
    L = [f"# Legal AI ontology (v{ont.get('version')}, {ont.get('as_of')})", "",
         f"{len(doms)} workflow domains → {ncat} categories. Each company has one **main** category and any number of **active** categories.", "",
         "Other facets: customer segment · practice area · business model (platform / point / suite / services / infra).", "",
         "| Domain | Active | Main focus |", "|---|---:|---:|"]
    for d in doms:
        L.append(f"| {d['name']} (`{d['id']}`) | {tree[d['id']]['count']} | {sum(c['primary_domain'] == d['id'] for c in C)} |")
    for d in doms:
        L += ["", f"## {d['name']} (`{d['id']}`)", ""]
        tc = {c["id"]: c for c in tree[d["id"]]["children"]}
        for cat in d["categories"]:
            t = tc.get(cat["id"], {"count": 0, "primary_companies": []})
            prim = sorted((by[x] for x in t.get("primary_companies", []) if x in by), key=raise_key)
            names = ", ".join(p["name"] for p in prim[:8]) + (f" +{len(prim) - 8} more" if len(prim) > 8 else "")
            L.append(f"- **{cat['name']}** (`{cat['id']}`) · {t['count']} active / {len(prim)} main  ")
            L.append(f"  _{cat['def']}_  ")
            if names:
                L.append(f"  Main players: {names}")
    open(J("ontology", "README.md"), "w").write("\n".join(L) + "\n")

    # ---------- report/summary.md ----------
    ind = [c for c in C if c["status"] != "acquired" and c["stage"] != "Public" and c.get("total_raised_usd_m")]
    S = [f"# Legal AI market summary ({ont.get('as_of')})", "",
         f"- **{len(C)}** companies profiled ({sum(c['scope'] == 'core' for c in C)} core, {sum(c['scope'] == 'adjacent' for c in C)} adjacent) in **{stats['countries']}** countries",
         f"- **{len(light)}** more absorbed/defunct companies tracked for M&A; **{len(excl)}** candidates excluded with reasons",
         f"- **{len(doms)}** workflow domains, **{ncat}** categories", "", "## Key takeaways", ""]
    S += [f"{i}. {t}" for i, t in enumerate(take, 1)]
    S += ["", "## Most crowded categories", "", "| Category | Active | Main focus |", "|---|---:|---:|"]
    for r in sorted(mm["categories"], key=lambda x: -x["players"])[:15]:
        S.append(f"| {r['name']} | {r['players']} | {r['primary_players']} |")
    S += ["", "## Thinnest categories (white space)", "", "| Category | Active | Main focus |", "|---|---:|---:|"]
    for r in sorted(mm["categories"], key=lambda x: x["players"])[:15]:
        S.append(f"| {r['name']} | {r['players']} | {r['primary_players']} |")
    S += ["", "## Most-funded independent companies", "", "| # | Company | Main category | HQ | Stage | Raised | Valuation |", "|---:|---|---|---|---|---:|---:|"]
    cn = {c["id"]: c["name"] for d in doms for c in d["categories"]}
    for i, c in enumerate(sorted(ind, key=lambda c: -(c.get("total_raised_usd_m") or 0))[:25], 1):
        S.append(f"| {i} | {c['name']} | {cn.get(c['primary'], '—')} | {c['hq_country'] or '—'} | {c['stage']} | {fm(c['total_raised_usd_m'])} | {fm(c['valuation_usd_m'])} |")
    S += ["", "## Distribution", "", "| Region | Companies |", "|---|---:|"] + [f"| {r} | {n} |" for r, n in stats["by_region"]]
    S += ["", "| Stage | Companies |", "|---|---:|"] + [f"| {r} | {n} |" for r, n in stats["by_stage"] if n]
    S += ["", "| Business model | Companies |", "|---|---:|"] + [f"| {r} | {n} |" for r, n in Counter(c["model"] for c in C).most_common()]
    open(J("report", "summary.md"), "w").write("\n".join(S) + "\n")

    # ---------- README.md ----------
    R = f"""# Legal AI market research ({ont.get('as_of')})

Exhaustive map of companies building AI for legal work: who they are, what they build, where they overlap.

**Open the report:** `report/legal-ai-atlas.html` (self-contained; also published as a Claude artifact).
**Quick read:** `report/summary.md` · **Ontology:** `ontology/README.md`

## Numbers
- {len(C)} companies profiled ({sum(c['scope'] == 'core' for c in C)} core legal AI, {sum(c['scope'] == 'adjacent' for c in C)} adjacent), {stats['countries']} HQ countries
- {len(doms)} workflow domains, {ncat} categories
- {len(light)} absorbed/defunct companies (M&A view), {len(excl)} excluded candidates (with reasons)

## Folder layout
| Path | What |
|---|---|
| `data/companies.json` | **Main dataset.** One record per company: focus, HQ, founded, funding, headcount, products, capabilities, ontology tags, sources |
| `data/companies.csv` | Same, flattened for spreadsheets |
| `data/companies_verified.json` | Verified universe incl. scope (core/adjacent) and status |
| `data/excluded.json`, `data/excluded_during_profiling.json` | Dropped candidates and why |
| `data/acquired_defunct.json` | Companies folded into acquirers or shut down |
| `data/manual_overrides.json` | The few hand corrections (documented) |
| `ontology/ontology.json` | Ontology: domains → categories (+ customer, practice, model facets) |
| `ontology/mindmap.json` | Mind-map tree, domain overlap matrix, category pairs, category stats |
| `report/` | HTML report, template, takeaways, summary, stats |
| `raw/discovery/` | 10 discovery-agent outputs (1,061 raw records + gap hunt) |
| `raw/verification/` | 4 verification-agent outputs |
| `raw/profiles/` | 24 profiling-agent outputs |
| `raw/tags/` | 4 tagging-agent outputs |
| `scripts/` | Pipeline scripts and the agent briefs used |

## Pipeline (re-run to refresh)
1. Discovery agents → `raw/discovery/*.json`; `python3 scripts/merge_discovery.py`
2. Verification agents → `raw/verification/*.json`; `python3 scripts/consolidate_verified.py`
3. Profiling agents (brief: `scripts/profiling_prompt.md`, schema: `scripts/profile_schema.md`) → `raw/profiles/`
4. Tagging agents (brief: `scripts/tagging_prompt.md`) → `raw/tags/`
5. `python3 scripts/build_dataset.py && python3 scripts/build_artifact.py && python3 scripts/write_docs.py`

## Caveats
- Snapshot as of {ont.get('as_of')}. Funding/headcount move fast.
- Web access was search-only and rate-capped; long-tail profiles may rely on model knowledge (see each record's `confidence`).
- Funding = disclosed amounts. Incumbents/PE-owned companies often show none.
- Ontology v1.1–1.3 added 4 categories after tagging (marketing, trial prep, legal translation, AI governance); assignments for those use documented keyword rules in `scripts/build_dataset.py`.
"""
    open(J("README.md"), "w").write(R)
    print("wrote README.md, ontology/README.md, report/summary.md")


if __name__ == "__main__":
    main()
