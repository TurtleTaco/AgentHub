#!/usr/bin/env python3
"""Inject the dataset into report/template.html -> report/legal-ai-atlas.html (self-contained page)."""
import json
import os
import re
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(ROOT, *p)  # noqa: E731

# Mid-tone categorical palette that reads on both light and dark backgrounds
PALETTE = {"RES": "#3d7be0", "ASSIST": "#8a5cf0", "DRAFT": "#d05fa8", "CON": "#e08a2e", "DEAL": "#c2a01e",
           "LIT": "#d64545", "CLAIM": "#f07c6c", "IP": "#17a398", "COMP": "#44a85c", "OPS": "#7c8ea3",
           "FIRM": "#a0703f", "CONS": "#36b3d9", "GOV": "#5f63d1", "SERV": "#2fbf8f", "INFRA": "#9aa0a6"}
ACQ_ALIASES = {"relx": "LexisNexis (RELX)", "lexisnexis": "LexisNexis (RELX)", "thomson reuters": "Thomson Reuters",
               "wolters kluwer": "Wolters Kluwer", "clio": "Clio", "litera": "Litera", "docusign": "Docusign",
               "legora": "Legora", "harvey": "Harvey", "filevine": "Filevine", "relativity": "Relativity", "onit": "Onit",
               "legalsifter": "LegalSifter", "doctrine": "Doctrine", "affinipay": "AffiniPay", "workday": "Workday",
               "sirion": "Sirion", "dilitrust": "DiliTrust", "opus 2": "Opus 2", "clarivate": "Clarivate",
               "questel": "Questel", "epiq": "Epiq", "cube": "CUBE", "icertis": "Icertis", "lawvu": "LawVu",
               "barbri": "BARBRI", "haystackid": "HaystackID", "rev": "Rev", "elevate": "Elevate", "reveal": "Reveal",
               "datasite": "Datasite", "lexroom": "Lexroom", "mitratech": "Mitratech", "netdocuments": "NetDocuments",
               "imanage": "iManage", "aderant": "Aderant", "legalon": "LegalOn", "eve": "Eve", "evenup": "EvenUp"}
KEEP = ["cid", "name", "website", "scope", "status", "parent", "hq_city", "hq_country", "region", "founded", "founders",
        "employees_bin", "employees_approx", "stage", "stage_raw", "total_raised_usd_m", "total_raised_text", "last_round",
        "valuation_usd_m", "investors", "focus", "problem", "customers", "practice", "jurisdictions", "products",
        "capabilities", "delivery", "ai_approach", "integrations", "customers_named", "differentiators", "news",
        "primary", "categories", "model", "unique_angle", "domains", "primary_domain", "confidence", "sources", "notes"]


def norm_acquirer(s):
    if not s:
        return None
    base = re.sub(r"\(.*?\)", "", s).strip()
    base = re.split(r"\s+(?:in|on)\s+\d{4}|,|;| - ", base)[0].strip()
    low = base.lower()
    for k, v in ACQ_ALIASES.items():
        if low == k or low.startswith(k + " ") or low.startswith(k + "'"):
            return v
    return base or None


def year_of(*vals):
    for v in vals:
        m = re.search(r"(19|20)\d{2}", str(v or ""))
        if m:
            return int(m.group(0))
    return None


def main():
    companies = json.load(open(J("data", "companies.json")))
    mm = json.load(open(J("ontology", "mindmap.json")))
    stats = json.load(open(J("report", "stats.json")))
    ont = json.load(open(J("ontology", "ontology.json")))
    light = json.load(open(J("data", "acquired_defunct.json")))
    takeaways_path = J("report", "takeaways.json")
    takeaways = json.load(open(takeaways_path)) if os.path.exists(takeaways_path) else []

    tree_by_dom = {d["id"]: d for d in mm["tree"]["children"]}
    domains = []
    for d in ont["facets"]["A_domain"]["domains"]:
        td = tree_by_dom.get(d["id"], {"children": [], "count": 0})
        tc = {c["id"]: c for c in td["children"]}
        prim_dom = sum(1 for c in companies if c.get("primary_domain") == d["id"])
        domains.append({"id": d["id"], "name": d["name"], "color": PALETTE.get(d["id"], d.get("color")),
                        "count": td.get("count", 0), "primary_count": prim_dom,
                        "categories": [{"id": c["id"], "name": c["name"], "def": c["def"],
                                        "count": tc.get(c["id"], {}).get("count", 0),
                                        "primary_count": tc.get(c["id"], {}).get("primary_count", 0)} for c in d["categories"]]})

    acq = defaultdict(list)
    seen = set()
    for c in companies:
        if c.get("status") == "acquired" and c.get("parent"):
            a = norm_acquirer(c["parent"])
            if a and (a, c["name"]) not in seen:
                seen.add((a, c["name"]))
                acq[a].append({"name": c["name"], "cid": c["cid"], "year": year_of(c.get("notes"), *(c.get("news") or []))})
    for l in light:
        if l.get("status") == "acquired" and l.get("acquired_by"):
            a = norm_acquirer(l["acquired_by"])
            if a and (a, l["name"]) not in seen:
                seen.add((a, l["name"]))
                acq[a].append({"name": l["name"], "cid": None, "year": l.get("acquired_year") or year_of(l.get("acquired_by"))})
    acquirers = sorted([{"name": k, "items": sorted(v, key=lambda x: -(x["year"] or 0))} for k, v in acq.items() if len(v) >= 2],
                       key=lambda x: (-len(x["items"]), x["name"]))

    data = {
        "asOf": ont.get("as_of", "2026-11-14"),
        "stats": stats,
        "domains": domains,
        "domain_ids": mm["domain_ids"],
        "domain_matrix": mm["domain_matrix"],
        "pairs": mm["category_pairs"],
        "catRows": mm["categories"],
        "companies": [{k: c.get(k) for k in KEEP} for c in companies if c.get("categories")],
        "acquirers": acquirers,
        "models": ont["facets"]["D_model"]["values"],
        "customers": ont["facets"]["B_customer"]["values"],
        "takeaways": takeaways,
        "method": {
            "steps": [
                ["Discovery: 9 parallel agents", "Each swept one slice (BigLaw platforms, contracts, litigation, plaintiff/SMB, in-house & compliance, IP/AI law firms/justice, Europe, rest of world, funding trackers). 1,061 raw records."],
                ["Merge & dedupe", "Domain and name normalisation plus manual alias fixes → 690 unique candidates."],
                ["Verification: 4 agents + 1 gap hunter", "Checked existence, legal-AI scope (core / adjacent / out), status, acquirer, duplicates. Gap hunter added 68 missed companies."],
                ["Profiling: 24 agents", "Focus, HQ, founding year, funding, headcount, and an exhaustive product + capability list per company, from web search plus model knowledge."],
                ["Ontology design", "Built bottom-up from ~1,900 distinct capability phrases, grouped into 15 workflow domains and 66 categories."],
                ["Tagging: 4 agents", "Each company assigned a main category, all active categories, business model, customers, practice areas and a one-line unique angle."],
                ["Assembly", "Scripts join everything into one dataset and compute the mind map, overlap matrix and white-space metrics."],
            ],
            "facets": [
                "A · Workflow domain → category: what job the product does (the mind map).",
                "B · Customer segment: who buys it (BigLaw, in-house, PI firms, consumers…).",
                "C · Practice area: litigation, corporate, IP, immigration, etc.",
                "D · Business model: horizontal platform, point solution, incumbent suite, AI-native services, infrastructure.",
            ],
            "caveats": [
                "Snapshot as of mid-November 2026. Funding and headcount change fast.",
                "Web access was search-only (no page fetches), capped per turn. Some long-tail profiles rely on model knowledge and are marked low confidence.",
                "Funding totals are disclosed amounts only. Incumbents show parent-company figures or none.",
                "Headcount is an estimate (LinkedIn-style ranges), not audited.",
                "Category tags reflect shipped capabilities as described publicly, not product quality.",
                "Acquired companies that still sell under their own brand are kept, flagged 'acquired'. Fully absorbed or defunct ones appear only in the consolidation view.",
            ],
            "files": [
                ["data/companies.json", "full profiles + tags (source of this page)"],
                ["data/companies.csv", "flat table for spreadsheets"],
                ["data/companies_verified.json", "verified universe incl. scope & status"],
                ["data/excluded.json", "excluded candidates with reasons"],
                ["data/acquired_defunct.json", "absorbed / defunct companies"],
                ["ontology/ontology.json", "the ontology (domains, categories, facets)"],
                ["ontology/mindmap.json", "tree, overlap matrix, category stats"],
                ["raw/", "every agent's raw output (discovery, verification, profiles, tags)"],
                ["scripts/", "merge, consolidate, build scripts + agent briefs"],
            ],
        },
    }
    blob = json.dumps(data, separators=(",", ":"), ensure_ascii=False).replace("</", "<\\/")
    tpl = open(J("report", "template.html")).read()
    assert "/*__DATA__*/null" in tpl
    out = tpl.replace("/*__DATA__*/null", blob)
    path = J("report", "legal-ai-atlas.html")
    open(path, "w").write(out)
    print(f"wrote {path} ({len(out) / 1e6:.2f} MB), companies {len(data['companies'])}, acquirers {len(acquirers)}")


if __name__ == "__main__":
    main()
