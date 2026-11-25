"""Build the master dataset + Atlas data file.
Usage: python3 build_atlas.py <notes_dir> <atlas_out_json>
Inputs : profiles/batch-*.json, data/ontology.json, data/classification*.json (optional),
         data/factcheck*.json (optional corrections), data/narrative.json (insights, partnerships, method)
Outputs: data/companies.json (master, in+borderline), data/companies.csv, data/out_of_scope.json, <atlas_out_json>
"""
import json, glob, os, sys, csv, re
notes, out_path = sys.argv[1], sys.argv[2]
P = lambda *a: os.path.join(notes, *a)

REGION = {}
for c in "United States|USA|US|Canada".split("|"): REGION[c] = "North America"
for c in ("United Kingdom|UK|France|Germany|Netherlands|Spain|Sweden|Switzerland|Finland|Norway|Denmark|Italy|Poland|Austria|Belgium|Ireland|Portugal|Czech Republic|Czechia|Estonia|Lithuania|Latvia|Luxembourg|Greece|Romania|Hungary|Bulgaria|Slovenia|Croatia|Serbia|Ukraine|Iceland|Slovakia").split("|"): REGION[c] = "Europe"
for c in "Israel|United Arab Emirates|UAE|Saudi Arabia|Qatar|Turkey|Türkiye|Jordan|Egypt|Bahrain|Oman|Kuwait".split("|"): REGION[c] = "Middle East"
for c in "China|Hong Kong|Taiwan".split("|"): REGION[c] = "Greater China"
for c in "Japan|South Korea|Korea".split("|"): REGION[c] = "Japan & Korea"
for c in "India|Sri Lanka|Pakistan|Bangladesh".split("|"): REGION[c] = "South Asia"
for c in "Singapore|Indonesia|Thailand|Vietnam|Malaysia|Philippines|Australia|New Zealand".split("|"): REGION[c] = "SE Asia & Oceania"
for c in "Brazil|Mexico|Chile|Argentina|Colombia|Uruguay|Peru".split("|"): REGION[c] = "Latin America"
for c in "Kenya|South Africa|Nigeria|Ghana|Rwanda|Morocco".split("|"): REGION[c] = "Africa"
COUNTRY_FIX = {"USA": "United States", "US": "United States", "UK": "United Kingdom", "UAE": "United Arab Emirates", "Korea": "South Korea", "Czechia": "Czech Republic", "Türkiye": "Turkey"}

def norm_country(c):
    if not c: return None
    c = c.strip()
    return COUNTRY_FIX.get(c, c)


LEGAL = re.compile(r",?\s+(inc\.?|incorporated|llc|l\.l\.c\.|ltd\.?|limited|co\.,?\s*ltd\.?|corp\.?|corporation|gmbh|ag|s\.a\.?|sas|s\.a\.s\.|b\.v\.?|bv|plc|oy|ab|a/s|s\.r\.l\.|srl|pte\.?\s*ltd\.?|pvt\.?\s*ltd\.?|private limited|k\.k\.)\.?$", re.I)
CUR = {r["id"]: r["name"] for r in json.load(open(P("data", "curated_candidates.json")))}
def clean(n):
    if not n: return n
    n = re.sub(r"\s*\(.*?\)\s*", " ", n).strip()
    for _ in range(3):
        n2 = LEGAL.sub("", n).strip().rstrip(",")
        if n2 == n: break
        n = n2
    return n
def display_name(p):
    b = clean(CUR.get(p.get("id"), "") or "")
    return b or clean(p.get("name") or "") or p.get("name")
PARENT_ALIAS = {"Amazon.com": "Amazon", "Advanced Micro Devices": "AMD", "Alphabet": "Google (Alphabet)"}

profiles = []
for f in sorted(glob.glob(P("profiles", "batch-*.json"))):
    profiles += json.load(open(f))
seen, uniq = set(), []
for p in profiles:
    if p.get("id") in seen: continue
    seen.add(p.get("id")); uniq.append(p)
profiles = uniq

# fact-check corrections: list of {id, field, value, note}
for f in sorted(glob.glob(P("data", "factcheck*.json"))) + sorted(glob.glob(P("verification", "factcheck-*.json"))):
    fixes = json.load(open(f))
    byid = {p["id"]: p for p in profiles}
    for fx in fixes:
        p = byid.get(fx.get("id"))
        if not p: continue
        for k, v in (fx.get("corrections") or {}).items():
            p.setdefault("_fc", []).append({"field": k, "old": p.get(k), "new": v})
            if k == "confidence" and isinstance(v, dict):
                p[k] = {**(p.get(k) or {}), **v}
            else:
                p[k] = v
        if fx.get("verdict"): p["verdict"] = fx["verdict"]

onto = json.load(open(P("data", "ontology.json")))
niche_ids = {n["id"] for n in onto["niches"]}
cls = {}
for f in sorted(glob.glob(P("data", "classification*.json"))):
    for row in json.load(open(f)):
        cls[row["id"]] = row

def heuristic(p):
    L = set(p.get("layers") or []); D = set(p.get("deployment") or []); M = set(p.get("modalities") or []); C = set(p.get("customers") or [])
    if "silicon" in L: return "1a" if D & {"edge-server", "camera"} else ("1e" if D & {"mobile", "pc-workstation", "vehicle-robot-drone"} else ("2a" if "datacenter-onprem" in D else "1b"))
    if "hardware-systems" in L: return "2b" if "datacenter-onprem" in D else "2c"
    if "model-optimization" in L: return "3a"
    if "models" in L: return "3d" if "speech-audio" in M else "3c"
    if "inference-runtime" in L: return "4c" if "speech-audio" in M else ("4a" if D & {"mobile", "pc-workstation"} else "4d")
    if "infra-orchestration" in L: return "5c" if D & {"edge-server", "embedded-iot", "camera"} else "5a"
    if "security-privacy" in L: return "6g"
    if "consumers" in C: return "8a"
    if "government-defense" in C: return "7d"
    if "camera" in D or "security-surveillance" in C: return "7a"
    return "6b"

def infer_parent(p):
    if p.get("parent"): return p["parent"]
    if (p.get("status") or "").lower() in ("acquired", "merged"):
        m = re.search(r"(?:[Aa]cquired|[Bb]ought|[Mm]erged into|[Mm]erged with|IP to|team to|joined)\s+(?:by\s+)?([A-Z][\w.&\- ]+?)(?:\s*[(,;]|\s+in\s|\s+for\s|$)", p.get("status_detail") or "")
        if m: return m.group(1).strip()
    return None

companies, out_scope = [], []
for p in profiles:
    if p.get("verdict") not in ("in", "borderline"):
        out_scope.append({"id": p.get("id"), "name": p.get("name"), "verdict": p.get("verdict"), "reason": p.get("verdict_reason"), "status": p.get("status_detail") or p.get("status")})
        continue
    c = cls.get(p["id"], {})
    prim = c.get("primary") if c.get("primary") in niche_ids else heuristic(p)
    sec = [s for s in (c.get("secondary") or []) if s in niche_ids and s != prim][:3]
    country = norm_country(p.get("hq_country"))
    prods = [[x.get("name"), x.get("category"), x.get("description")] for x in (p.get("products") or []) if isinstance(x, dict) and x.get("name")]
    companies.append({
        "id": p["id"], "name": display_name(p), "legalName": p.get("name"), "verdict": p.get("verdict"), "web": p.get("website"),
        "city": p.get("hq_city"), "country": country, "region": REGION.get(country, "Other" if country else None),
        "founded": p.get("founded") if isinstance(p.get("founded"), int) else None,
        "type": p.get("org_type"), "status": (p.get("status") or "active").lower(), "statusDetail": p.get("status_detail"), "parent": PARENT_ALIAS.get(clean(infer_parent(p)), clean(infer_parent(p))) if infer_parent(p) else None,
        "stage": p.get("funding_stage"), "fund": p.get("total_funding_usd_m") if isinstance(p.get("total_funding_usd_m"), (int, float)) else None,
        "lastRound": p.get("last_round"), "val": p.get("valuation_usd_m") if isinstance(p.get("valuation_usd_m"), (int, float)) else None,
        "mcap": p.get("market_cap_or_revenue"), "investors": (p.get("key_investors") or [])[:8],
        "emp": p.get("employees") if isinstance(p.get("employees"), int) else None, "empBand": p.get("employees_band"),
        "focus": p.get("focus"), "problem": p.get("problem"), "diff": p.get("differentiator"), "products": prods,
        "dep": p.get("deployment") or [], "layers": p.get("layers") or [], "mod": p.get("modalities") or [], "cust": p.get("customers") or [],
        "partners": (p.get("partners") or [])[:10], "customers": (p.get("notable_customers") or [])[:10],
        "primary": prim, "secondary": sec, "classified": bool(c),
        "conf": {"f": (p.get("confidence") or {}).get("funding"), "e": (p.get("confidence") or {}).get("employees"), "y": (p.get("confidence") or {}).get("founded")},
        "basis": p.get("basis"), "src": [s for s in (p.get("sources") or []) if isinstance(s, str)][:8],
        "factchecked": [x["field"] for x in p.get("_fc", [])],
    })
companies.sort(key=lambda c: c["name"].lower())

# master files
json.dump(companies, open(P("data", "companies.json"), "w"), indent=1, ensure_ascii=False)
json.dump(out_scope, open(P("data", "out_of_scope.json"), "w"), indent=1, ensure_ascii=False)
nm = {n["id"]: n["name"] for n in onto["niches"]}
with open(P("data", "companies.csv"), "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["name", "verdict", "status", "status_detail", "main_niche", "secondary_niches", "hq_city", "hq_country", "region", "founded", "org_type",
                "funding_stage", "total_funding_usd_m", "last_round", "valuation_usd_m", "employees", "employees_band", "focus", "problem",
                "products", "deployment", "customers", "differentiator", "website", "confidence_funding", "confidence_employees", "basis"])
    for c in companies:
        w.writerow([c["name"], c["verdict"], c["status"], c["statusDetail"], f'{c["primary"]} {nm.get(c["primary"], "")}', "; ".join(f"{s} {nm.get(s, '')}" for s in c["secondary"]),
                    c["city"], c["country"], c["region"], c["founded"], c["type"], c["stage"], c["fund"], c["lastRound"], c["val"], c["emp"], c["empBand"],
                    c["focus"], c["problem"], " | ".join(p[0] for p in c["products"]), ", ".join(c["dep"]), ", ".join(c["cust"]), c["diff"], c["web"],
                    c["conf"]["f"], c["conf"]["e"], c["basis"]])

deals = []
for p in profiles:
    if (p.get("status") or "").lower() in ("acquired", "merged") and infer_parent(p):
        buyer = clean(infer_parent(p)); buyer = PARENT_ALIAS.get(buyer, buyer)
        m = re.search(r"(19|20)\d\d", p.get("status_detail") or "")
        deals.append({"target": display_name(p), "id": p["id"] if p.get("verdict") in ("in", "borderline") else None,
                      "buyer": buyer, "year": int(m.group(0)) if m else None, "detail": p.get("status_detail")})
json.dump(deals, open(P("data", "deals.json"), "w"), indent=1, ensure_ascii=False)

narr = json.load(open(P("data", "narrative.json"))) if os.path.exists(P("data", "narrative.json")) else {"insights": [], "partnerships": [], "method": {"steps": [], "caveats": []}}
cand = json.load(open(P("data", "candidates.json")))
indep = [c for c in companies if c["status"] == "active" and c["type"] not in ("public", "big-tech", "subsidiary")]
atlas = {
    "meta": {"asOfLabel": "Nov 2026", "candidates": len(cand), "countries": len({c["country"] for c in companies if c["country"]}),
             "fundingTotal": round(sum(c["fund"] or 0 for c in indep)), "acquired": sum(1 for c in companies if c["status"] in ("acquired", "merged", "defunct"))},
    "domains": onto["domains"], "niches": onto["niches"],
    "companies": [{k: v for k, v in c.items() if k not in ("layers", "mod", "classified", "verdict")} for c in companies],
    "deals": deals, "insights": narr["insights"], "partnerships": narr["partnerships"], "method": narr["method"],
}
json.dump(atlas, open(out_path, "w"), ensure_ascii=False, separators=(",", ":"))
print(f"profiles {len(profiles)} | in-scope {len(companies)} | out {len(out_scope)} | classified {sum(c['classified'] for c in companies)} | atlas {os.path.getsize(out_path)//1024} KB")
