#!/usr/bin/env python3
"""Combine discovery merge + verification verdicts + gap-hunter finds.

Writes:
  data/companies_verified.json   every included company (core + adjacent), with verification fields
  data/excluded.json             excluded / duplicate candidates with reasons (audit trail)
  data/profile_chunks/P##.json   batches for the profiling agents (companies that still operate)
"""
import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from merge_discovery import norm_name  # noqa: E402

CHUNK = int(os.environ.get("CHUNK", "28"))

COUNTRY_FIX = {"US": "United States", "USA": "United States", "UK": "United Kingdom",
               "unknown": None, "Unknown": None, "": None}


def main():
    cands = {c["cid"]: c for c in json.load(open(os.path.join(ROOT, "data", "candidates_merged.json")))}
    verdicts = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "raw", "verification", "V*_verified.json"))):
        for v in json.load(open(f)):
            verdicts[v["cid"]] = v

    included, excluded = [], []
    missing = [cid for cid in cands if cid not in verdicts]
    if missing:
        print(f"!! {len(missing)} candidates have no verdict (e.g. {missing[:5]})")

    for cid, c in cands.items():
        v = verdicts.get(cid)
        if not v:
            continue
        rec = {
            "cid": cid,
            "name": v.get("name") or c["name"],
            "aliases": c.get("aliases", []),
            "website": v.get("website") or c.get("website"),
            "hq_country": COUNTRY_FIX.get(v.get("hq_country"), v.get("hq_country")) or COUNTRY_FIX.get(c.get("hq_country"), c.get("hq_country")),
            "one_liner": v.get("one_liner") or c.get("one_liner"),
            "scope": v.get("scope"),
            "status": v.get("status"),
            "acquired_by": v.get("acquired_by"),
            "acquired_year": v.get("acquired_year"),
            "operates_as": v.get("operates_as"),
            "verify_confidence": v.get("confidence"),
            "verify_evidence": v.get("evidence"),
            "verify_notes": v.get("notes"),
            "found_by": c.get("found_by", []),
            "last_known_funding": c.get("last_known_funding"),
            "discovery_sources": c.get("source_urls", []),
        }
        if v.get("verdict") == "include" and v.get("scope") in ("core", "adjacent"):
            included.append(rec)
        else:
            rec["verdict"] = v.get("verdict")
            rec["duplicate_of"] = v.get("duplicate_of")
            rec["exclude_reason"] = v.get("exclude_reason")
            excluded.append(rec)

    # gap-hunter additions
    gap_path = os.path.join(ROOT, "raw", "discovery", "D10_gaps.json")
    if os.path.exists(gap_path):
        known = {norm_name(r["name"]) for r in included + excluded}
        for alias_list in (r.get("aliases", []) for r in included):
            known.update(norm_name(a) for a in alias_list)
        n_added = 0
        for i, g in enumerate(json.load(open(gap_path)), 1):
            if norm_name(g["name"]) in known:
                continue
            known.add(norm_name(g["name"]))
            n_added += 1
            included.append({
                "cid": f"G{i:03d}", "name": g["name"], "aliases": [], "website": g.get("website"),
                "hq_country": COUNTRY_FIX.get(g.get("hq_country"), g.get("hq_country")),
                "one_liner": g.get("one_liner"), "scope": g.get("scope", "core"),
                "status": g.get("status") if g.get("status") != "unknown" else "active",
                "acquired_by": g.get("acquired_by"), "acquired_year": None, "operates_as": None,
                "verify_confidence": "medium", "verify_evidence": "search", "verify_notes": "gap-hunter find",
                "found_by": ["D10"], "last_known_funding": g.get("last_known_funding"),
                "discovery_sources": g.get("source_urls", [])[:6],
            })
        print(f"gap-hunter: added {n_added} new companies")

    included.sort(key=lambda r: r["name"].lower())
    json.dump(included, open(os.path.join(ROOT, "data", "companies_verified.json"), "w"), indent=1, ensure_ascii=False)
    json.dump(excluded, open(os.path.join(ROOT, "data", "excluded.json"), "w"), indent=1, ensure_ascii=False)

    # profiling targets: still-operating companies/brands
    to_profile = [r for r in included if not (
        r["status"] == "defunct" or (r["status"] == "acquired" and r.get("operates_as") == "absorbed"))]
    light = [r for r in included if r not in to_profile]
    out_dir = os.path.join(ROOT, "data", "profile_chunks")
    os.makedirs(out_dir, exist_ok=True)
    for f in glob.glob(os.path.join(out_dir, "*.json")):
        os.remove(f)
    keys = ("cid", "name", "aliases", "website", "hq_country", "one_liner", "scope", "status",
            "acquired_by", "acquired_year", "operates_as", "last_known_funding", "discovery_sources")
    chunks = [to_profile[i:i + CHUNK] for i in range(0, len(to_profile), CHUNK)]
    for i, ch in enumerate(chunks, 1):
        json.dump([{k: r.get(k) for k in keys} for r in ch],
                  open(os.path.join(out_dir, f"P{i:02d}.json"), "w"), indent=1, ensure_ascii=False)

    core = sum(1 for r in included if r["scope"] == "core")
    print(f"included {len(included)} (core {core}, adjacent {len(included) - core}); excluded {len(excluded)}")
    print(f"to profile: {len(to_profile)} in {len(chunks)} chunks of <= {CHUNK}; light records (absorbed/defunct): {len(light)}")


if __name__ == "__main__":
    main()
