"""Write the markdown report, the full directory and the README from built data.
Usage: python3 make_report.py <notes_dir> <atlas_json> <report_md>
"""
import json, sys, os, collections, re
notes, atlas, report = sys.argv[1:4]
P = lambda *a: os.path.join(notes, *a)
d = json.load(open(atlas)); C = d["companies"]; N = {n["id"]: n for n in d["niches"]}
by_n = collections.defaultdict(list)
for c in C:
    for i, n in enumerate([c["primary"]] + c["secondary"]): by_n[n].append((c, i > 0))
fm = lambda m: "—" if m is None else (f"${m/1000:.1f}B" if m >= 1000 else f"${m:.0f}M")
strip = lambda t: re.sub(r"\*\*", "", t)
rank = lambda c: (c["fund"] or 0) + (c["emp"] or 0) / 10
L = ["# Local AI Atlas", "", f"*Market map of companies that run AI on customer-controlled hardware · as of {d['meta']['asOfLabel']}*", "",
     "Interactive version: the **Local AI Atlas** artifact (built from `reports/local-ai-atlas/`).", "", "## Key takeaways", ""]
L += [f"- {t}" for t in d["insights"]]
L += ["", "## Ontology: 8 domains → niches", "", "| Domain | Problem it solves | Main | Niches |", "|---|---|---|---|"]
for dm in d["domains"]:
    ns = [n for n in d["niches"] if n["domain"] == dm["id"]]
    main = sum(1 for c in C if N[c["primary"]]["domain"] == dm["id"])
    L.append(f"| **{dm['code']}. {dm['name']}** | {dm['q']} | {main} | " + "; ".join(f"{n['id']} {n['name']} ({len(by_n[n['id']])})" for n in ns) + " |")
L += ["", "## Big-tech collaborations", ""] + [f"- **{p['parties']}** ({p['date']}): {p['what']}" for p in d["partnerships"]]
acq = collections.Counter(x["buyer"] for x in d["deals"])
L += ["", "## Consolidation", "", f"- {len(d['deals'])} acquisitions tracked; top buyers: " + ", ".join(f"{b} ({n})" for b, n in acq.most_common(8))]
L += ["", "## Method & caveats", ""] + [f"{i}. **{s[0]}**: {s[1]}" for i, s in enumerate(d["method"]["steps"], 1)]
L += [""] + [f"- **{k}**: {strip(v)}" for k, v in d["method"]["caveats"]]
L += ["", "## Files", "", "- `research_notes/Local AI Atlas/data/companies.json`: master dataset (all fields)",
      "- `research_notes/Local AI Atlas/data/companies.csv`: spreadsheet version", "- `research_notes/Local AI Atlas/data/directory.md`: every company by niche",
      "- `research_notes/Local AI Atlas/data/ontology.json`, `deals.json`, `narrative.json`", "- `research_notes/Local AI Atlas/profiles/`, `verification/`, `discovery/`: raw agent outputs and notes", ""]
open(report, "w").write("\n".join(L))
# directory
D = ["# Local AI Atlas: company directory", "", f"{len(C)} companies by niche. Main-niche companies first, then *secondary* (italic). Funding = total disclosed; staff = estimate.", ""]
for dm in d["domains"]:
    D += [f"## {dm['code']}. {dm['name']}", f"*{dm['q']}*", ""]
    for n in [n for n in d["niches"] if n["domain"] == dm["id"]]:
        D += [f"### {n['id']} {n['name']} ({len(by_n[n['id']])})", f"{n['desc']}", "", "| Company | HQ | Founded | Stage | Raised | Staff | Focus | Key products |", "|---|---|---|---|---|---|---|---|"]
        for c, sec in sorted(by_n[n["id"]], key=lambda x: (x[1], -rank(x[0]))):
            nm = f"*{c['name']}*" if sec else f"**{c['name']}**"
            if c["status"] != "active": nm += f" ({c['status']})"
            D.append(f"| {nm} | {c['city'] or ''}{', ' if c['city'] and c['country'] else ''}{c['country'] or ''} | {c['founded'] or '—'} | {c['stage'] or '—'} | {fm(c['fund'])} | {c['emp'] or c['empBand'] or '—'} | {(c['focus'] or '').replace('|', '/')} | {'; '.join(p[0] for p in c['products'][:5]).replace('|', '/')} |")
        D.append("")
open(P("data", "directory.md"), "w").write("\n".join(D))
R = ["# Local AI Atlas: research workspace", "", "Market research on companies enabling local AI (on-device, edge, on-prem, private cloud, air-gapped, sovereign). As of Nov 2026.", "",
     "## Pipeline", "", "1. `discovery/`: 11 segment sweeps (JSON + notes) → `scripts/merge_discovery.py` → `data/candidates.json`",
     "2. `scripts/curate.py` → `data/curated_candidates.json`, `data/excluded_at_curation.json`, `profiles/input/`",
     "3. `profiles/batch-*.json|md`: verification + profile per company (prompt: `scripts/profile_prompt.txt`)",
     "4. `verification/factcheck-*.json`: independent fact-checks (prompt: `scripts/factcheck_prompt.txt`)",
     "5. `data/ontology.json` + `data/classification-*.json` (prompt: `scripts/classify_prompt.txt`; overrides in `classification-overrides.json`)",
     "6. `scripts/build_atlas.py` → `data/companies.json|csv`, `data/out_of_scope.json`, `data/deals.json`, `reports/local-ai-atlas/atlas-data.json`",
     "7. `scripts/make_narrative.py` → `data/narrative.json`; `scripts/make_report.py` → `reports/Local AI Atlas.md`, `data/directory.md`", "",
     "## Rebuild", "", "```bash", "cd \"research_notes/Local AI Atlas\"", "python3 scripts/build_atlas.py . ../../reports/local-ai-atlas/atlas-data.json",
     "python3 scripts/make_narrative.py . ../../reports/local-ai-atlas/atlas-data.json", "python3 scripts/build_atlas.py . ../../reports/local-ai-atlas/atlas-data.json",
     "python3 scripts/make_report.py . ../../reports/local-ai-atlas/atlas-data.json \"../../reports/Local AI Atlas.md\"", "```", "",
     "## Record fields (data/companies.json)", "", "id, name, legalName, verdict (in/borderline), web, city, country, region, founded, type, status, statusDetail, parent, stage, fund (USD M), lastRound, val, mcap, investors, emp, empBand, focus, problem, diff, products [name, category, description], dep (deployment targets), layers, mod (modalities), cust (customer segments), partners, customers, primary/secondary (niche ids), conf (per-field confidence), basis, src, factchecked (fields corrected by fact-check)", ""]
open(P("README.md"), "w").write("\n".join(R))
print("report", len(L), "lines; directory", len(D), "lines")
