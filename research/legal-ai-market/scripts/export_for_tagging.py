#!/usr/bin/env python3
"""Export compact profile views for the ontology-tagging agents.
Usage: python3 scripts/export_for_tagging.py T1 P01 P02 ... P07
"""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tag_id, chunks = sys.argv[1], sys.argv[2:]
out = []
for ch in chunks:
    for p in json.load(open(os.path.join(ROOT, "raw", "profiles", f"{ch}_profiles.json"))):
        if p.get("exclude"):
            continue
        out.append({
            "cid": p["cid"], "name": p["name"],
            "status": p.get("status"), "parent_company": p.get("parent_company") or p.get("acquired_by"),
            "focus": p.get("focus_summary"), "problem": p.get("primary_problem"),
            "products": [f"{x.get('name')}: {x.get('description')}" for x in (p.get("products") or [])],
            "capabilities": p.get("capabilities") or [],
            "customers": p.get("target_customers") or [], "practice": p.get("practice_areas") or [],
            "delivery": p.get("delivery") or [], "differentiators": p.get("differentiators") or [],
        })
path = os.path.join(ROOT, "data", "tag_inputs", f"{tag_id}.json")
json.dump(out, open(path, "w"), indent=0, ensure_ascii=False)
print(f"{tag_id}: {len(out)} companies -> {path}")
