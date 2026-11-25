"""Compute headline stats from the built atlas and write data/narrative.json (insights, partnerships, method).
Run build_atlas.py first, then this, then build_atlas.py again.
Usage: python3 make_narrative.py <notes_dir> <atlas_json>
"""
import json, sys, os, glob, itertools, collections
notes, atlas = sys.argv[1], sys.argv[2]
P = lambda *a: os.path.join(notes, *a)
d = json.load(open(atlas)); C = d["companies"]; N = {n["id"]: n for n in d["niches"]}; D = {x["id"]: x for x in d["domains"]}
dom = lambda c: N[c["primary"]]["domain"]
doms = lambda c: {N[x]["domain"] for x in [c["primary"]] + c["secondary"]}
indep = [c for c in C if c["status"] == "active" and c["type"] not in ("public", "big-tech", "subsidiary")]
by = collections.defaultdict(list)
for c in C: by[dom(c)].append(c)
young = {k: sum(1 for c in v if (c["founded"] or 0) >= 2020) for k, v in by.items()}
fund = {k: sum(c["fund"] or 0 for c in v if c in indep) for k, v in by.items()}
dep = collections.Counter(x for c in C for x in c["dep"])
pairs = collections.Counter()
for c in C:
    for a, b in itertools.combinations(sorted(doms(c)), 2): pairs[(a, b)] += 1
(pa, pb), pv = pairs.most_common(1)[0]; (qa, qb), qv = pairs.most_common(2)[1]
single = sum(1 for c in C if not c["secondary"])
cnt = collections.Counter(x for c in C for x in [c["primary"]] + c["secondary"])
thin = [N[k]["name"][0].lower() + N[k]["name"][1:] for k, v in sorted(cnt.items(), key=lambda kv: kv[1]) if v < 10 and k not in ("2f", "2g", "3g")][:4]
deals = d["deals"]; buyers = collections.Counter(x["buyer"] for x in deals)
top3 = buyers.most_common(3)
osx = [c["name"] for c in C if "6a" in [c["primary"]] + c["secondary"]]
topf = sorted(by["D7"], key=lambda c: -(c["fund"] or 0))[:3]
fmtB = lambda m: f"${m/1000:.0f}B" if m >= 10000 else f"${m/1000:.1f}B"
fc = [r for f in glob.glob(P("verification", "factcheck-*.json")) for r in json.load(open(f))]
fcc = collections.Counter(r.get("result") for r in fc)
searched = sum(1 for c in C if c["basis"] in ("searched", "mixed"))
ins = [
 f"**{len(C)} companies, {len(D)} domains, {len(N)} niches.** Local AI is a full stack, from NPUs to personal apps, not one market.",
 f"**On-prem beats on-device.** {dep['datacenter-onprem']} companies target customer datacenters vs {dep['mobile']} for phones. \"Local\" mostly means private infrastructure.",
 f"**Silicon is crowded and mature; software is young.** {young['D3']} of {len(by['D3'])} model companies and {young['D8']} of {len(by['D8'])} personal-AI players were founded 2020+, vs {young['D1']} of {len(by['D1'])} chip firms.",
 f"**Money follows physical AI.** Vertical & Physical AI raised the most ({fmtB(fund['D7'])}, led by {', '.join(c['name'] for c in topf)}); personal local AI the least ({fmtB(fund['D8'])}).",
 f"**NVIDIA is the gravity well.** Top acquirer ({buyers['NVIDIA']} deals incl. Run:ai, Deci, OctoAI) and co-builder of Palantir's Sovereign AI OS: five joint launches in 11 months.",
 f"**Chipmakers are buying the software layer.** {', '.join(f'{b} {n}' for b, n in top3)} of {len(deals)} tracked deals: runtimes, compilers, dev platforms (Edge Impulse, Modular, Nexa AI, Silo AI).",
 f"**Biggest overlaps: {D[pa]['short']} × {D[pb]['short']} ({pv}) and {D[qa]['short']} × {D[qb]['short']} ({qv}).** Model makers ship engines and apps; platforms bundle models.",
 f"**Focus is the norm.** {single} of {len(C)} companies sit in a single niche; the multi-domain players are mostly big tech.",
 f"**White space:** {', '.join(thin)} each have fewer than 10 companies.",
 f"**Shakudo's niche (private AI OS) has {len(osx)} players**, from Dataiku, Domino and Cloudera to Kamiwaza, webAI and Zylon. The battle is open-source breadth plus run-anywhere Kubernetes.",
]
partnerships = [
 {"parties": "NVIDIA × Palantir", "date": "Oct 2025 → Sep 2026", "what": "Five joint launches: AIP on NVIDIA's stack, a Sovereign AI OS reference architecture, Nemotron in air-gapped US agencies."},
 {"parties": "Dell × Palantir × NVIDIA", "date": "May 2026", "what": "Palantir Foundry/AIP ships on-prem inside Dell AI Factory."},
 {"parties": "NVIDIA AI Factory for Government", "date": "Oct 2025", "what": "Reference design for federal on-prem AI with Dell, HPE, Cisco and others."},
 {"parties": "NVIDIA × 7 PC makers", "date": "Oct 2025", "what": "DGX Spark-class desktops (Acer, ASUS, Dell, GIGABYTE, HP, Lenovo, MSI) put a petaflop on the desk."},
 {"parties": "Microsoft Sovereign Private Cloud", "date": "Feb 2026", "what": "Azure Local + Foundry Local run large models fully disconnected."},
 {"parties": "Google Distributed Cloud × NVIDIA / Cirrascale", "date": "Apr 2026", "what": "Gemini offered on-prem, including air-gapped."},
 {"parties": "Qualcomm × Humain", "date": "Oct 2025", "what": "200 MW of AI200/AI250 inference racks for Saudi sovereign AI."},
 {"parties": "Microsoft × Qualcomm, Intel, AMD", "date": "2024 →", "what": "Copilot+ PCs set the 40-TOPS NPU bar for AI PCs."},
 {"parties": "Meta × Arm", "date": "Oct 2025", "what": "ExecuTorch 1.0 with Arm backends for on-device Llama."},
 {"parties": "Huawei × DeepSeek", "date": "2025–2026", "what": "Open models tuned for Ascend chips: China's domestic local stack."},
]
cand = json.load(open(P("data", "candidates.json"))); cur = json.load(open(P("data", "curated_candidates.json")))
prof = [p for f in glob.glob(P("profiles", "batch-*.json")) for p in json.load(open(f))]
border = sum(1 for p in prof if p.get("verdict") == "borderline")
method = {
 "steps": [
  ["Discover", f"11 research agents swept market maps, partner directories and funding news, one segment each: {sum(len(json.load(open(f))) for f in glob.glob(P('discovery', '*.json')))} mentions, {len(cand)} unique candidates."],
  ["Curate", f"Merged duplicates; removed community projects, consortia and generic tooling: {len(cur)} candidates."],
  ["Verify & profile", f"21 agent batches confirmed scope and status, then profiled each company: {len(C)} in scope, {len(prof) - len(C)} rejected."],
  ["Fact-check", f"10 independent agents re-checked funding, status, founding, HQ and headcount for {len(fc)} key independents: {fcc['confirmed']} confirmed, {fcc['corrected']} corrected, {fcc['unverifiable'] + fcc['unchecked']} unverifiable."],
  ["Build the ontology", f"{len(D)} problem-framed domains and {len(N)} niches derived from what companies do. Agents mapped every company (1 main + up to 3 secondary niches); weak fits drove v2."],
  ["Map overlaps", "Overlap = a company active in 2+ domains. Crowding and white space = companies per niche. Everything is saved as JSON/CSV."],
 ],
 "caveats": [
  ["Scope", "Inference on hardware the customer controls: device, edge, on-prem, private cloud, air-gapped, sovereign. Cloud-API-only vendors excluded."],
  ["Borderline", f"{border} companies where local AI is a secondary line are kept and labelled **borderline**."],
  ["Funding", "Total disclosed equity in USD for independent companies, all purposes (not only local AI). Public and big-tech firms show 'Public'."],
  ["Headcount", "Estimates from LinkedIn and aggregator snippets; treat as ±30%."],
  ["Confidence", f"Each profile carries per-field confidence and a basis. {searched} of {len(C)} profiles used live web search; the rest rely on model knowledge and are flagged low/medium."],
  ["Freshness", "As of 25 Nov 2026. Events after mid-2026 depend on web search coverage and may be incomplete."],
  ["Files", "research_notes/Local AI Atlas/: data/companies.json & .csv, ontology.json, deals.json, profiles/, verification/, discovery/."],
 ],
}
json.dump({"insights": ins, "partnerships": partnerships, "method": method}, open(P("data", "narrative.json"), "w"), indent=1, ensure_ascii=False)
print("\n".join(ins)); print(method["steps"][3])
