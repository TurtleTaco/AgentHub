#!/usr/bin/env python3
"""Assemble the final legal-AI market dataset.

Inputs : data/companies_verified.json, raw/profiles/*_profiles.json, raw/tags/*_tags.json, ontology/ontology.json
Outputs: data/companies.json      full records (profile + tags + verification)
         data/companies.csv       flat table for spreadsheets
         data/acquired_defunct.json  light records for absorbed/defunct companies (M&A view)
         ontology/mindmap.json    tree (domain -> category -> companies) + overlap matrices + white space
         report/stats.json        aggregate numbers for the report
"""
import csv
import glob
import json
import os
import re
from collections import Counter, defaultdict
from itertools import combinations

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(ROOT, *p)  # noqa: E731

COUNTRY = {"US": "United States", "USA": "United States", "U.S.": "United States", "United States of America": "United States",
           "UK": "United Kingdom", "England": "United Kingdom", "Korea": "South Korea", "Republic of Korea": "South Korea",
           "UAE": "United Arab Emirates", "Czechia": "Czech Republic", "Holland": "Netherlands"}
REGION = {
    "North America": ["United States", "Canada"],
    "Europe": ["United Kingdom", "Ireland", "France", "Germany", "Sweden", "Norway", "Denmark", "Finland", "Iceland", "Netherlands",
               "Belgium", "Luxembourg", "Switzerland", "Austria", "Spain", "Portugal", "Italy", "Poland", "Czech Republic", "Estonia",
               "Latvia", "Lithuania", "Ukraine", "Greece", "Romania", "Hungary", "Slovakia", "Slovenia", "Croatia", "Bulgaria", "Serbia", "Cyprus", "Malta"],
    "Asia-Pacific": ["India", "China", "Japan", "South Korea", "Singapore", "Australia", "New Zealand", "Hong Kong", "Taiwan", "Malaysia",
                     "Indonesia", "Vietnam", "Philippines", "Thailand", "Pakistan", "Bangladesh", "Sri Lanka"],
    "Latin America": ["Brazil", "Mexico", "Argentina", "Chile", "Colombia", "Peru", "Uruguay", "Ecuador", "Costa Rica"],
    "Middle East & Africa": ["Israel", "United Arab Emirates", "Saudi Arabia", "Qatar", "Lebanon", "Egypt", "Jordan", "Turkey",
                             "Nigeria", "Kenya", "South Africa", "Ghana", "Morocco", "Rwanda", "Bahrain", "Kuwait", "Oman"],
}
C2R = {c: r for r, cs in REGION.items() for c in cs}

STAGE_ORDER = ["Bootstrapped", "Pre-seed/Seed", "Series A", "Series B", "Series C", "Series D+", "Growth/PE",
               "Public", "Subsidiary/Acquired", "Non-profit", "Unknown"]
EMP_BINS = ["1-10", "11-50", "51-200", "201-500", "501-1000", "1001-5000", "5001+", "Unknown"]


def norm_country(c):
    if not c:
        return None
    c = c.strip()
    return COUNTRY.get(c, c)


def norm_stage(s, status=None, parent=None):
    t = (s or "").lower()
    if status == "acquired" or "acquired" in t or "subsidiary" in t or (parent and not t):
        return "Subsidiary/Acquired"
    if "public" in t or "ipo" in t or "listed" in t:
        return "Public"
    if "non-profit" in t or "nonprofit" in t:
        return "Non-profit"
    if "bootstrap" in t or "self-funded" in t:
        return "Bootstrapped"
    if "growth" in t or "pe" == t.strip() or "private equity" in t or "pe-backed" in t or "pe backed" in t:
        return "Growth/PE"
    m = re.search(r"series\s*([a-z])", t)
    if m:
        letter = m.group(1)
        return {"a": "Series A", "b": "Series B", "c": "Series C"}.get(letter, "Series D+")
    if "seed" in t or "angel" in t or "grant" in t or "accelerator" in t or "y combinator" in t:
        return "Pre-seed/Seed"
    return "Unknown"


def norm_emp(e):
    if not isinstance(e, dict):
        return "Unknown", None
    approx = e.get("approx")
    rng = (e.get("range") or "").replace("–", "-").replace(" ", "")
    if isinstance(approx, (int, float)) and approx > 0:
        a = approx
        for b, hi in (("1-10", 10), ("11-50", 50), ("51-200", 200), ("201-500", 500), ("501-1000", 1000), ("1001-5000", 5000)):
            if a <= hi:
                return b, int(a)
        return "5001+", int(a)
    for b in EMP_BINS:
        if rng.startswith(b) or rng == b:
            return b, None
    m = re.match(r"(\d+)", rng)
    if m:
        return norm_emp({"approx": int(m.group(1))})[0], None
    return "Unknown", None


SPLITS = [  # (old category, new category, keywords for new, keywords that keep old)
    ("FIRM.intake", "FIRM.marketing",
     ["marketing", "seo", "advertis", "lead generation", "content", "review management", "ppc", "google ads", "social media"],
     ["intake", "receptionist", "answering", "call", "scheduling", "appointment", "qualif", "conflict", "chat"]),
    ("LIT.depo", "LIT.trial",
     ["trial", "jury", "juror", "mock", "simulat", "exhibit", "courtroom", "argument"],
     ["deposition", "transcri", "testimony", "court report", "page-line", "witness", "summar"]),
]


def apply_splits(tag, profile):
    """Re-sort tags made before the two split categories existed (documented in ontology README)."""
    if not tag:
        return tag
    cats = list(tag.get("categories") or [])
    text = " ".join((profile.get("capabilities") or []) + [f"{x.get('name')} {x.get('description')}" for x in profile.get("products") or []]).lower()
    prim = tag.get("primary")
    for old, new, kw_new, kw_old in SPLITS:
        if old in cats:
            if any(k in text for k in kw_new) and new not in cats:
                cats.append(new)
            if new in cats and not any(k in text for k in kw_old):
                cats.remove(old)
                if prim == old:
                    prim = new
    # derived category: legal translation (added after tagging, ontology v1.2)
    focus = (profile.get("focus_summary") or "").lower()
    if any("translat" in c.lower() for c in profile.get("capabilities") or []) or "translat" in focus:
        if "DRAFT.translate" not in cats:
            cats.append("DRAFT.translate")
        if "translat" in focus and prim in ("DRAFT.write", "ASSIST.copilot", None):
            prim = "DRAFT.translate"
    return {**tag, "categories": cats, "primary": prim}


def num(x):
    try:
        return float(x) if x is not None and x != "" else None
    except (TypeError, ValueError):
        return None


def main():
    ont = json.load(open(J("ontology", "ontology.json")))
    domains = ont["facets"]["A_domain"]["domains"]
    cat_info = {c["id"]: {"name": c["name"], "domain": d["id"], "def": c["def"]} for d in domains for c in d["categories"]}

    verified = {r["cid"]: r for r in json.load(open(J("data", "companies_verified.json")))}
    profiles, excluded_late = {}, []
    for f in sorted(glob.glob(J("raw", "profiles", "*_profiles.json"))):
        for p in json.load(open(f)):
            if p.get("exclude"):
                excluded_late.append({"cid": p.get("cid"), "name": p.get("name"), "reason": p.get("exclude_reason")})
            else:
                profiles[p["cid"]] = p
    tags = {}
    for f in sorted(glob.glob(J("raw", "tags", "*_tags.json"))):
        for t in json.load(open(f)):
            tags[t["cid"]] = t

    companies, light = [], []
    for cid, v in verified.items():
        p = profiles.get(cid)
        if not p:
            if v["status"] == "defunct" or (v["status"] == "acquired" and v.get("operates_as") == "absorbed"):
                light.append({"cid": cid, "name": v["name"], "status": v["status"], "acquired_by": v.get("acquired_by"),
                              "acquired_year": v.get("acquired_year"), "hq_country": norm_country(v.get("hq_country")),
                              "one_liner": v.get("one_liner"), "website": v.get("website")})
            continue
        t = apply_splits(tags.get(cid, {}), p)
        fund = p.get("funding") or {}
        last = fund.get("last_round") or {}
        status = p.get("status") or v.get("status")
        parent = p.get("parent_company") or p.get("acquired_by") or v.get("acquired_by")
        emp_bin, emp_n = norm_emp(p.get("employees"))
        country = norm_country(p.get("hq_country") or v.get("hq_country"))
        rec = {
            "cid": cid, "name": p.get("name") or v["name"], "website": p.get("website") or v.get("website"),
            "scope": v.get("scope"), "status": status, "parent": parent,
            "hq_city": p.get("hq_city"), "hq_country": country, "region": C2R.get(country, "Other/Unknown"),
            "founded": p.get("founded_year") if isinstance(p.get("founded_year"), int) else None,
            "founders": p.get("founders") or [],
            "employees_bin": emp_bin, "employees_approx": emp_n,
            "employees_as_of": (p.get("employees") or {}).get("as_of") if isinstance(p.get("employees"), dict) else None,
            "stage_raw": fund.get("stage"),
            "stage": (lambda st: norm_stage(last.get("type"), status) if st == "Unknown" and last.get("type") else st)(
                norm_stage(fund.get("stage"), status, parent if status == "acquired" else None)),
            "total_raised_usd_m": num(fund.get("total_raised_usd_m")), "total_raised_text": fund.get("total_raised_text"),
            "last_round": {"type": last.get("type"), "amount_usd_m": num(last.get("amount_usd_m")), "date": last.get("date"),
                           "leads": last.get("lead_investors") or []},
            "valuation_usd_m": num(fund.get("valuation_usd_m")), "investors": fund.get("key_investors") or [],
            "focus": p.get("focus_summary"), "problem": p.get("primary_problem"),
            "customers": t.get("customers") or p.get("target_customers") or [],
            "practice": t.get("practice") or p.get("practice_areas") or [],
            "jurisdictions": p.get("jurisdictions") or [],
            "products": p.get("products") or [], "capabilities": p.get("capabilities") or [],
            "delivery": p.get("delivery") or [], "ai_approach": p.get("ai_approach"),
            "integrations": p.get("key_integrations") or [], "customers_named": p.get("notable_customers") or [],
            "differentiators": p.get("differentiators") or [], "news": p.get("recent_news") or [],
            "primary": t.get("primary"), "categories": t.get("categories") or [], "model": t.get("model"),
            "unique_angle": t.get("unique_angle"),
            "domains": sorted({cat_info[c]["domain"] for c in (t.get("categories") or []) if c in cat_info}),
            "primary_domain": cat_info.get(t.get("primary"), {}).get("domain"),
            "confidence": p.get("confidence"), "sources": (p.get("sources") or [])[:6], "notes": p.get("notes"),
        }
        companies.append(rec)
    companies.sort(key=lambda r: r["name"].lower())

    json.dump(companies, open(J("data", "companies.json"), "w"), indent=1, ensure_ascii=False)
    json.dump(light, open(J("data", "acquired_defunct.json"), "w"), indent=1, ensure_ascii=False)
    if excluded_late:
        json.dump(excluded_late, open(J("data", "excluded_during_profiling.json"), "w"), indent=1, ensure_ascii=False)

    cols = ["cid", "name", "website", "scope", "status", "parent", "hq_city", "hq_country", "region", "founded", "employees_bin",
            "employees_approx", "stage", "total_raised_usd_m", "valuation_usd_m", "model", "primary", "primary_domain",
            "categories", "customers", "practice", "focus", "unique_angle", "products", "capabilities", "confidence"]
    with open(J("data", "companies.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for r in companies:
            row = []
            for c in cols:
                val = r.get(c)
                if c == "products":
                    val = " | ".join(x.get("name", "") for x in val)
                elif isinstance(val, list):
                    val = " | ".join(map(str, val))
                row.append(val)
            w.writerow(row)

    # ---------- mind map + overlaps ----------
    tagged = [r for r in companies if r["categories"]]
    by_cat = defaultdict(list)
    for r in tagged:
        for c in r["categories"]:
            by_cat[c].append(r["cid"])
    tree = {"name": "Legal AI", "children": []}
    for d in domains:
        dnode = {"id": d["id"], "name": d["name"], "color": d.get("color"), "children": []}
        dset = set()
        for c in d["categories"]:
            members = by_cat.get(c["id"], [])
            prim = [cid for cid in members if next(x for x in tagged if x["cid"] == cid)["primary"] == c["id"]]
            dset.update(members)
            dnode["children"].append({"id": c["id"], "name": c["name"], "def": c["def"], "count": len(members),
                                      "primary_count": len(prim), "companies": members, "primary_companies": prim})
        dnode["count"] = len(dset)
        tree["children"].append(dnode)

    dom_ids = [d["id"] for d in domains]
    dom_matrix = {a: {b: 0 for b in dom_ids} for a in dom_ids}
    for r in tagged:
        ds = r["domains"]
        for a in ds:
            dom_matrix[a][a] += 1
        for a, b in combinations(sorted(ds), 2):
            dom_matrix[a][b] += 1
            dom_matrix[b][a] += 1
    pair = Counter()
    for r in tagged:
        for a, b in combinations(sorted(set(r["categories"])), 2):
            pair[(a, b)] += 1
    top_pairs = [{"a": a, "b": b, "count": n} for (a, b), n in pair.most_common(40)]

    cat_rows = []
    for cid_, info in cat_info.items():
        members = by_cat.get(cid_, [])
        specialists = [x for x in members if len(next(t for t in tagged if t["cid"] == x)["categories"]) <= 2]
        prim = [x for x in members if next(t for t in tagged if t["cid"] == x)["primary"] == cid_]
        raised = sum((next(t for t in tagged if t["cid"] == x)["total_raised_usd_m"] or 0) for x in prim)
        cat_rows.append({"id": cid_, "name": info["name"], "domain": info["domain"], "players": len(members),
                         "primary_players": len(prim), "specialists": len(specialists), "primary_raised_usd_m": round(raised, 1)})
    cat_rows.sort(key=lambda x: -x["players"])

    json.dump({"tree": tree, "domain_matrix": dom_matrix, "domain_ids": dom_ids,
               "domain_names": {d["id"]: d["name"] for d in domains}, "category_pairs": top_pairs,
               "categories": cat_rows}, open(J("ontology", "mindmap.json"), "w"), indent=1, ensure_ascii=False)

    # ---------- stats ----------
    stats = {
        "companies_profiled": len(companies), "tagged": len(tagged), "acquired_or_defunct_light": len(light),
        "core": sum(r["scope"] == "core" for r in companies), "adjacent": sum(r["scope"] == "adjacent" for r in companies),
        "countries": len({r["hq_country"] for r in companies if r["hq_country"]}),
        "by_region": Counter(r["region"] for r in companies).most_common(),
        "by_country": Counter(r["hq_country"] or "Unknown" for r in companies).most_common(40),
        "by_stage": [(s, sum(r["stage"] == s for r in companies)) for s in STAGE_ORDER],
        "by_employees": [(b, sum(r["employees_bin"] == b for r in companies)) for b in EMP_BINS],
        "by_founded": sorted(Counter(r["founded"] for r in companies if r["founded"]).items()),
        "by_model": Counter(r["model"] or "untagged" for r in companies).most_common(),
        "total_raised_usd_m": round(sum(r["total_raised_usd_m"] or 0 for r in companies if r["status"] != "acquired"), 1),
        "top_funded": [{"name": r["name"], "raised": r["total_raised_usd_m"], "valuation": r["valuation_usd_m"], "stage": r["stage"]}
                       for r in sorted(companies, key=lambda r: -(r["total_raised_usd_m"] or 0))[:30]],
        "excluded_during_profiling": len(excluded_late),
    }
    json.dump(stats, open(J("report", "stats.json"), "w"), indent=1, ensure_ascii=False)
    print(f"companies {len(companies)} (tagged {len(tagged)}), light {len(light)}, excluded late {len(excluded_late)}")
    print("by_stage", stats["by_stage"])
    print("by_region", stats["by_region"])


if __name__ == "__main__":
    main()
