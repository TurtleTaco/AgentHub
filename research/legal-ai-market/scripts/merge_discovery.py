#!/usr/bin/env python3
"""Merge + dedupe raw discovery files into one candidate list.

Usage: python3 scripts/merge_discovery.py
Reads  raw/discovery/*.json
Writes data/candidates_merged.json, data/candidates_merged.csv
"""
import csv
import glob
import json
import os
import re
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "raw", "discovery")
OUT_JSON = os.path.join(ROOT, "data", "candidates_merged.json")
OUT_CSV = os.path.join(ROOT, "data", "candidates_merged.csv")

GENERIC_HOSTS = {
    "linkedin.com", "crunchbase.com", "github.com", "medium.com", "apps.apple.com",
    "chrome.google.com", "appsource.microsoft.com", "ycombinator.com", "producthunt.com",
    "twitter.com", "x.com", "facebook.com", "notion.site", "substack.com",
}
NAME_SUFFIXES = [
    " inc", " ltd", " llc", " gmbh", " sas", " ab", " bv", " plc", " co", " corp",
    " technologies", " technology", " labs", " ai", " legal", " law", " hq", " app", " io",
]


def norm_domain(url):
    if not url:
        return None
    u = url.strip()
    if not re.match(r"^[a-z]+://", u, re.I):
        u = "https://" + u
    try:
        host = urlparse(u).netloc.lower()
    except Exception:
        return None
    host = host.split(":")[0]
    if host.startswith("www."):
        host = host[4:]
    if not host or "." not in host:
        return None
    parts = host.split(".")
    # keep registrable-ish domain: last 2 labels, or 3 for co.uk style
    if len(parts) >= 3 and parts[-2] in {"co", "com", "org", "net", "gov", "ac"} and len(parts[-1]) == 2:
        host = ".".join(parts[-3:])
    else:
        host = ".".join(parts[-2:])
    if host in GENERIC_HOSTS:
        return None
    return host


def norm_name(name):
    n = name.lower()
    n = re.sub(r"\(.*?\)", " ", n)          # drop parentheticals
    n = n.replace("&", " and ")
    n = re.sub(r"\.(ai|io|com|law|legal|co)\b", r" \1", n)
    n = re.sub(r"[^a-z0-9 ]+", " ", n)
    n = re.sub(r"\s+", " ", n).strip()
    changed = True
    while changed:
        changed = False
        for s in NAME_SUFFIXES:
            if n.endswith(s) and len(n) > len(s) + 2:
                n = n[: -len(s)].strip()
                changed = True
    return n.replace(" ", "")


def main():
    files = sorted(glob.glob(os.path.join(RAW, "*.json")))
    records = []
    for f in files:
        slice_id = os.path.basename(f).split("_")[0]
        try:
            data = json.load(open(f))
        except Exception as e:
            print(f"!! could not parse {f}: {e}")
            continue
        for item in data:
            if not isinstance(item, dict) or not item.get("name"):
                continue
            item["_slice"] = slice_id
            records.append(item)
    print(f"loaded {len(records)} raw records from {len(files)} files")

    groups = []          # list of dicts
    by_domain, by_name = {}, {}
    for r in records:
        d = norm_domain(r.get("website"))
        n = norm_name(r["name"])
        gi = None
        if d and d in by_domain:
            gi = by_domain[d]
        elif n and n in by_name:
            gi = by_name[n]
        if gi is None:
            gi = len(groups)
            groups.append({"items": []})
        groups[gi]["items"].append(r)
        if d:
            by_domain.setdefault(d, gi)
        if n:
            by_name.setdefault(n, gi)

    merged = []
    for g in groups:
        items = g["items"]
        names = [i["name"] for i in items]
        # canonical name: most common, tie -> shortest
        name = sorted(set(names), key=lambda x: (-names.count(x), len(x)))[0]
        websites = [i.get("website") for i in items if i.get("website")]
        one_liners = [i.get("one_liner") for i in items if i.get("one_liner")]
        statuses = [i.get("status") for i in items if i.get("status") and i.get("status") != "unknown"]
        acq = [i.get("acquired_by") for i in items if i.get("acquired_by")]
        countries = [i.get("hq_country") for i in items if i.get("hq_country")]
        funding = [i.get("last_known_funding") for i in items if i.get("last_known_funding")]
        srcs = []
        for i in items:
            for s in i.get("source_urls") or []:
                if s not in srcs:
                    srcs.append(s)
        merged.append({
            "name": name,
            "aliases": sorted(set(names) - {name}),
            "website": websites[0] if websites else None,
            "domain": norm_domain(websites[0]) if websites else None,
            "one_liner": max(one_liners, key=len) if one_liners else None,
            "segment_guesses": sorted({i.get("segment_guess") for i in items if i.get("segment_guess")}),
            "hq_country": max(set(countries), key=countries.count) if countries else None,
            "status": max(set(statuses), key=statuses.count) if statuses else "unknown",
            "acquired_by": acq[0] if acq else None,
            "last_known_funding": funding[0] if funding else None,
            "found_by": sorted({i["_slice"] for i in items}),
            "source_urls": srcs[:6],
        })
    merged.sort(key=lambda m: m["name"].lower())
    for idx, m in enumerate(merged, 1):
        m["cid"] = f"C{idx:04d}"

    json.dump(merged, open(OUT_JSON, "w"), indent=1, ensure_ascii=False)
    with open(OUT_CSV, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["cid", "name", "website", "hq_country", "status", "acquired_by", "found_by", "one_liner"])
        for m in merged:
            w.writerow([m["cid"], m["name"], m["website"], m["hq_country"], m["status"],
                        m["acquired_by"], "|".join(m["found_by"]), m["one_liner"]])
    multi = sum(1 for m in merged if len(m["found_by"]) > 1)
    print(f"merged -> {len(merged)} unique candidates ({multi} found by 2+ agents)")


if __name__ == "__main__":
    main()
