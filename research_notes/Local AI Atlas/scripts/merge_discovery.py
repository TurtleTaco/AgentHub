"""Merge discovery JSON files into a deduplicated candidate list.

Usage: python3 merge_discovery.py <notes_dir>
Writes <notes_dir>/data/candidates.json and candidates.tsv
"""
import json, re, sys, glob, os
from collections import Counter, defaultdict
from urllib.parse import urlparse

notes = sys.argv[1]
GENERIC = {"github.com", "huggingface.co", "medium.com", "linkedin.com", "x.com", "twitter.com",
           "crunchbase.com", "apps.apple.com", "play.google.com", "producthunt.com", "gitlab.com",
           "substack.com", "notion.site", "sites.google.com", "ycombinator.com", "kickstarter.com"}
SUFFIX = r"\b(inc|incorporated|llc|ltd|limited|gmbh|ag|sa|sas|bv|plc|corp|corporation|co|company|the|technologies|technology|tech|systems|labs|lab|ai|a\.i\.|io|hq|group|holdings)\b"

def name_key(n):
    n = n.lower()
    n = re.sub(r"\(.*?\)", " ", n)           # drop parentheticals
    n = n.replace("&", " and ")
    n = re.sub(SUFFIX, " ", n)
    n = re.sub(r"[^a-z0-9]+", "", n)
    return n

def dom_key(url):
    if not url or not isinstance(url, str):
        return None
    if not url.startswith("http"):
        url = "https://" + url
    try:
        p = urlparse(url)
    except Exception:
        return None
    host = (p.netloc or "").lower().split(":")[0]
    if host.startswith("www."):
        host = host[4:]
    if not host:
        return None
    parts = host.split(".")
    reg = ".".join(parts[-2:]) if len(parts) >= 2 else host
    if len(parts) >= 3 and parts[-2] in {"co", "com", "ac", "org", "net"} and len(parts[-1]) == 2:
        reg = ".".join(parts[-3:])
    if reg in GENERIC or host in GENERIC:
        seg = [s for s in p.path.split("/") if s]
        return f"{reg}/{seg[0].lower()}" if seg else None
    return reg

rows = []
for f in sorted(glob.glob(os.path.join(notes, "discovery", "*.json"))):
    src = os.path.basename(f)[:-5]
    try:
        data = json.load(open(f))
    except Exception as e:
        print("BAD JSON", f, e); continue
    for r in data:
        if not isinstance(r, dict) or not r.get("name"):
            continue
        r["_file"] = src
        rows.append(r)

# union-find
parent = list(range(len(rows)))
def find(i):
    while parent[i] != i:
        parent[i] = parent[parent[i]]; i = parent[i]
    return i
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb: parent[rb] = ra

by_name, by_dom = {}, {}
for i, r in enumerate(rows):
    nk = name_key(r["name"])
    if nk:
        if nk in by_name: union(by_name[nk], i)
        else: by_name[nk] = i
    dk = dom_key(r.get("website"))
    if dk:
        if dk in by_dom: union(by_dom[dk], i)
        else: by_dom[dk] = i

groups = defaultdict(list)
for i in range(len(rows)):
    groups[find(i)].append(rows[i])

def mode(vals):
    vals = [v for v in vals if v]
    return Counter(vals).most_common(1)[0][0] if vals else None

out = []
for g in groups.values():
    names = Counter(r["name"].strip() for r in g)
    name = sorted(names.items(), key=lambda kv: (-kv[1], len(kv[0])))[0][0]
    rec = {
        "name": name,
        "aliases": sorted(set(names) - {name}),
        "website": mode(r.get("website") for r in g),
        "hq_country": mode(r.get("hq_country") for r in g),
        "type": mode(r.get("type") for r in g),
        "status": mode(r.get("status") for r in g),
        "segments": sorted(set(r.get("segment") or r["_file"] for r in g)),
        "found_by": sorted(set(r["_file"] for r in g)),
        "one_liners": list(dict.fromkeys(r.get("one_liner") for r in g if r.get("one_liner")))[:3],
        "local_ai_angles": list(dict.fromkeys(r.get("local_ai_angle") for r in g if r.get("local_ai_angle")))[:3],
        "sources": list(dict.fromkeys(s for r in g for s in (r.get("sources") or []) if isinstance(s, str)))[:8],
    }
    out.append(rec)

out.sort(key=lambda r: r["name"].lower())
for i, r in enumerate(out):
    slug = re.sub(r"[^a-z0-9]+", "-", r["name"].lower()).strip("-")
    r["id"] = slug
os.makedirs(os.path.join(notes, "data"), exist_ok=True)
json.dump(out, open(os.path.join(notes, "data", "candidates.json"), "w"), indent=1, ensure_ascii=False)
with open(os.path.join(notes, "data", "candidates.tsv"), "w") as fh:
    for r in out:
        fh.write("\t".join([r["id"], r["name"], r["hq_country"] or "", r["status"] or "", ",".join(r["segments"]),
                            (r["one_liners"][0] if r["one_liners"] else "")[:110]]) + "\n")
print(f"raw rows: {len(rows)}  unique: {len(out)}")
print(Counter(s for r in out for s in r["segments"]).most_common())
