#!/usr/bin/env python3
"""Generate an insight dashboard (breakdown.html) by joining graphify's
graph.json topology with the frontmatter of every wiki page.

Run:  python3 breakdown.py            # expects ../wiki and ./graph.json
      python3 breakdown.py <vault_root> <graph.json>
Writes breakdown.html next to graph.json.
"""
import json, collections, sys, html, re, datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
VAULT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE.parent
GRAPH = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else HERE / "graph.json"
TODAY = datetime.date.today()

# ---------------------------------------------------------------- frontmatter
def parse_fm(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm = {}
    for line in text[3:end].splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        k, v = k.strip(), v.strip()
        if not k:
            continue
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip().strip('"').strip("'") for x in v[1:-1].split(",") if x.strip()]
        else:
            v = v.strip('"').strip("'")
        fm[k] = v
    return fm

# meta keyed by source_file path relative to vault, e.g. "wiki/products/fundsub.md"
# body keeps the full markdown so we can read [[wikilinks]] (ground truth the
# graph extraction does not reliably capture).
meta = {}
body = {}
for p in (VAULT / "wiki").rglob("*.md"):
    rel = p.relative_to(VAULT).as_posix()
    txt = p.read_text(encoding="utf-8", errors="ignore")
    meta[rel] = parse_fm(txt)
    body[rel] = txt

# customer <-> product links from wikilinks, in BOTH directions:
#   customer body links [[wiki/products/X]]  AND  product body links [[wiki/customers/Y]]
_WIKILINK = re.compile(r"\[\[wiki/(products|customers)/([a-z0-9-]+)")
cust2prods = collections.defaultdict(set)   # "wiki/customers/foo.md" -> {product stems}
for rel, txt in body.items():
    t = meta.get(rel, {}).get("type")
    if t == "customer":
        for kind, slug in _WIKILINK.findall(txt):
            if kind == "products":
                cust2prods[rel].add(slug)
    elif t == "product":
        pslug = Path(rel).stem
        for kind, slug in _WIKILINK.findall(txt):
            if kind == "customers":
                cust2prods[f"wiki/customers/{slug}.md"].add(pslug)
prod2custs = collections.defaultdict(set)   # product stem -> {customer "title"}
for cf, pslugs in cust2prods.items():
    for ps in pslugs:
        prod2custs[ps].add(cf)

# ---------------------------------------------------------------- graph
g = json.load(open(GRAPH))
nodes, links = g["nodes"], g["links"]
hyper = g.get("hyperedges", [])
id2file = {n["id"]: n["source_file"] for n in nodes}
id2label = {n["id"]: n.get("label", n["id"]) for n in nodes}
file2ids = collections.defaultdict(list)
for n in nodes:
    file2ids[n["source_file"]].append(n["id"])

# node-level degree + file-level adjacency
deg = collections.Counter()
fadj = collections.defaultdict(set)   # source_file -> set of neighbor source_files
for l in links:
    s, t = l["source"], l["target"]
    deg[s] += 1; deg[t] += 1
    fs, ft = id2file.get(s), id2file.get(t)
    if fs and ft and fs != ft:
        fadj[fs].add(ft); fadj[ft].add(fs)

def folder(sf):
    p = sf.split("/")
    return p[1] if len(p) > 2 else "root"

def ftype(sf):                       # authoritative type from frontmatter, else folder
    return meta.get(sf, {}).get("type") or folder(sf)

def file_degree(sf):
    return sum(deg.get(i, 0) for i in file2ids.get(sf, []))

# distinct page files actually present in the graph, by category
files_by_type = collections.defaultdict(list)
for sf in {n["source_file"] for n in nodes}:
    files_by_type[ftype(sf)].append(sf)

# ---------------------------------------------------------------- core counts
n_nodes, n_edges, n_comm = len(nodes), len(links), len({n.get("community") for n in nodes if n.get("community") is not None})
n_pages = len(meta)
conf = collections.Counter(l.get("confidence", "?") for l in links)
EXTRACTED, INFERRED, AMBIGUOUS = conf.get("EXTRACTED", 0), conf.get("INFERRED", 0), conf.get("AMBIGUOUS", 0)
relations = collections.Counter(l.get("relation") for l in links)

# ---------------------------------------------------------------- dates / freshness
def page_date(sf):
    m = meta.get(sf, {})
    raw = m.get("as_of_date") if m.get("type") == "source" else m.get("last_updated")
    if not raw or raw == "undated":
        return None
    try:
        return datetime.date.fromisoformat(raw)
    except ValueError:
        return None

def age_days(d):
    return (TODAY - d).days

FRESH_BUCKETS = [("Fresh (<30d)", 0, 30), ("Recent (30-90d)", 30, 90),
                 ("Aging (90-180d)", 90, 180), ("Stale (>180d)", 180, 10**6)]
fresh = collections.Counter()
undated = 0
dated_pages = []   # (sf, date, age)
for sf in meta:
    d = page_date(sf)
    if d is None:
        undated += 1
        continue
    a = age_days(d)
    dated_pages.append((sf, d, a))
    for name, lo, hi in FRESH_BUCKETS:
        if lo <= a < hi:
            fresh[name] += 1
            break
stalest = sorted(dated_pages, key=lambda x: -x[2])[:10]

# ---------------------------------------------------------------- trust
TRUST_LABEL = {1: "Spec / How-it-works", 2: "Impl guide / SOP", 3: "Pricing", 4: "FAQ",
               5: "GTM / Sales deck", 6: "CS / GTM training", 7: "Client training",
               8: "Security whitepaper", 9: "Case study", 10: "Release notes / one-pager",
               11: "RFP", 12: "Roadmap"}
trust_hist = collections.Counter()
for sf, m in meta.items():
    if m.get("type") == "source" and str(m.get("trust_level", "")).isdigit():
        trust_hist[int(m["trust_level"])] += 1

# ---------------------------------------------------------------- product joins
# All product PAGES on disk — not just those that became graph nodes. The graph
# extraction misses some product pages (e.g. fundsub, data-room, IDM), which
# would otherwise drop entire columns/rows from the matrices below.
PRODUCT_FILES = sorted([sf for sf, m in meta.items() if m.get("type") == "product"],
                       key=lambda sf: -file_degree(sf))
# Coverage is a CONTENT-gap signal, so derive it from each source's frontmatter
# `products:` field (ground truth) rather than graph adjacency — the graph does
# not reliably wire every product node to its source pages.
def _pnorm(s):
    return str(s).lower().strip().strip('"').strip("'")
PRODUCT_ALIASES = {
    "integration-hub": {"integration hub"},
    "fundsub": {"fundsub", "fund subscription"},
    "data-room": {"data room"},
    "investor-data-management": {"idm", "investor data management"},
    "investor-access": {"investor access"},
    "platform": {"platform"},
    "e-signature": {"e-signature", "esignature", "e signature"},
    "investor-portal": {"investor portal", "portal"},
    "ocr-data-extraction": {"ocr data extraction", "ocr", "data extraction"},
    "aaa": {"aaa", "advisor advantage"},
    "landing-page": {"landing page"},
    "side-letter": {"side letter"},
    "engagement-hub": {"engagement hub"},
}
def product_sources(sf):
    stem = Path(sf).stem
    aliases = PRODUCT_ALIASES.get(stem, {stem.replace("-", " ")})
    out = []
    for f, fmeta in meta.items():
        if fmeta.get("type") != "source":
            continue
        prods = fmeta.get("products", [])
        prods = [prods] if isinstance(prods, str) else prods
        if any(_pnorm(p) in aliases for p in prods):
            out.append(f)
    return out
def neighbors_type(sf, t):
    return [f for f in fadj.get(sf, ()) if ftype(f) == t]

# source-type coverage buckets
COV_COLS = [("Spec", {"spec"}), ("Impl", {"implementation-guide", "sop"}),
            ("Pricing", {"pricing"}), ("FAQ", {"faq"}),
            ("Sales/GTM", {"sales-deck", "gtm-training", "cs-training", "client-training", "one-pager"}),
            ("Security", {"security-whitepaper"})]

product_rows = []
for sf in PRODUCT_FILES:
    m = meta.get(sf, {})
    srcs = product_sources(sf)
    trusts = [int(meta[s]["trust_level"]) for s in srcs
              if str(meta.get(s, {}).get("trust_level", "")).isdigit()]
    stypes = {meta.get(s, {}).get("source_type") for s in srcs}
    cov = [(col, bool(stypes & vals)) for col, vals in COV_COLS]
    d = page_date(sf)
    product_rows.append({
        "title": m.get("title", id2label.get(Path(sf).stem, sf)),
        "status": m.get("status", "?"),
        "sc": m.get("source_count", str(len(srcs))),
        "feat": len([f for f in files_by_type.get("feature", [])
                     if meta.get(f, {}).get("parent_product", "") == m.get("title", "")]),
        "cust": sorted(prod2custs.get(Path(sf).stem, set())),
        "concepts": neighbors_type(sf, "concept"),
        "trust_min": min(trusts) if trusts else None,
        "trust_max": max(trusts) if trusts else None,
        "age": age_days(d) if d else None,
        "cov": cov,
    })

# low-trust products: no source ranked 1-3 (spec/impl/pricing)
low_trust_products = [r for r in product_rows
                      if r["trust_min"] is None or r["trust_min"] >= 4]

# ---------------------------------------------------------------- fragile pages
fragile = sorted({meta[sf].get("title", Path(sf).stem)
                  for sf in meta if str(meta[sf].get("source_count", "")) == "1"})
isolated = sorted({id2label[i] for i in id2label if deg.get(i, 0) <= 1})

# ---------------------------------------------------------------- customer x product
CUST_FILES = sorted(files_by_type.get("customer", []),
                    key=lambda sf: meta.get(sf, {}).get("title", sf))
cust_matrix = []
for sf in CUST_FILES:
    prods = set(cust2prods.get(sf, set()))   # from wikilinks, both directions
    cust_matrix.append((meta.get(sf, {}).get("title", Path(sf).stem), prods))
PROD_COLS = [(meta.get(sf, {}).get("title", Path(sf).stem).split(" (")[0], Path(sf).stem)
             for sf in PRODUCT_FILES]

# ---------------------------------------------------------------- audience
aud = collections.Counter()
onboarding = collections.Counter()
onboarding_titles = []
for sf, m in meta.items():
    if m.get("type") != "source":
        continue
    a = m.get("target_audience", "Unspecified") or "Unspecified"
    aud[a] += 1
    if str(m.get("onboarding_required", "")).lower() == "yes":
        onboarding[a] += 1
        onboarding_titles.append(m.get("title", Path(sf).stem))

# ================================================================ render
esc = html.escape
def bars(rows, maxv, fmt=lambda v: str(v)):
    out = []
    for label, val in rows:
        pct = round(val / maxv * 100) if maxv else 0
        out.append(f'<div class="bar-row"><div class="bar-label" title="{esc(str(label))}">{esc(str(label))}</div>'
                   f'<div class="bar-track"><div class="bar-fill" style="width:{pct}%"></div></div>'
                   f'<div class="bar-val">{fmt(val)}</div></div>')
    return "\n".join(out)

# freshness
fresh_rows = [(n, fresh.get(n, 0)) for n, *_ in FRESH_BUCKETS] + [("Undated", undated)]
fresh_html = bars(fresh_rows, max(v for _, v in fresh_rows))
stale_html = "".join(
    f'<div class="god"><span class="god-deg" style="font-size:12px">{a}d</span>'
    f'<span class="god-name">{esc(meta[sf].get("title", sf))} '
    f'<em style="color:var(--muted)">· {d.isoformat()}</em></span></div>'
    for sf, d, a in stalest)

# trust
trust_rows = [(f"{k} · {TRUST_LABEL.get(k, '')}", trust_hist[k]) for k in sorted(trust_hist)]
trust_html = bars(trust_rows, max(trust_hist.values()) if trust_hist else 1)
lowtrust_html = "".join(
    f'<span class="pill warn">{esc(r["title"])}'
    f'{" · no sources" if r["trust_min"] is None else " · best=T"+str(r["trust_min"])}</span>'
    for r in low_trust_products) or '<span class="muted">None — every product has a top-3 source.</span>'

# coverage matrix
cov_head = "".join(f"<th>{c}</th>" for c, _ in COV_COLS)
cov_body = ""
for r in product_rows:
    cells = "".join(
        f'<td class="{"ok" if has else "gap"}">{"✓" if has else "·"}</td>' for _, has in r["cov"])
    cov_body += f'<tr><td class="rowname">{esc(r["title"])}</td>{cells}</tr>'

# product cards
def status_badge(s):
    cls = {"GA": "ga", "beta": "beta", "deprecated": "dep"}.get(s, "ga")
    return f'<span class="badge {cls}">{esc(s)}</span>'
cards_html = ""
for r in product_rows:
    trust = "—" if r["trust_min"] is None else (f"T{r['trust_min']}" if r["trust_min"] == r["trust_max"] else f"T{r['trust_min']}–T{r['trust_max']}")
    age = "undated" if r["age"] is None else f"{r['age']}d old"
    concepts = ", ".join(sorted(meta.get(c, {}).get("title", Path(c).stem) for c in r["concepts"])[:4]) or "—"
    cards_html += f'''<div class="pcard">
      <div class="pcard-top"><span class="pcard-title">{esc(r["title"])}</span>{status_badge(r["status"])}</div>
      <div class="pcard-stats">
        <span><b>{r["sc"]}</b> sources</span><span><b>{r["feat"]}</b> features</span>
        <span><b>{len(r["cust"])}</b> customers</span><span class="trust"><b>{trust}</b> trust</span>
      </div>
      <div class="pcard-meta">{age} · concepts: {esc(concepts)}</div>
    </div>'''

# customer matrix
cm_head = "".join(f'<th class="rot"><span>{esc(c)}</span></th>' for c, _ in PROD_COLS)
cm_body = ""
for name, prods in cust_matrix:
    cells = "".join(f'<td class="{"ok" if pid in prods else ""}">{"●" if pid in prods else ""}</td>'
                    for _, pid in PROD_COLS)
    cls = ' class="empty"' if not prods else ""
    cm_body += f'<tr{cls}><td class="rowname">{esc(name)}</td>{cells}</tr>'

# competitor × product overlap matrix (rows = competitor pages, cols = products)
CONF_RANK = {"high": 0, "medium": 1, "low": 2}
CONF_CHIP = {"high": '<span class="cf hi">high</span>',
             "medium": '<span class="cf md">med</span>',
             "low": '<span class="cf lo">low</span>'}
comp_rows = []
for sf, m in meta.items():
    if m.get("type") != "competitor" or Path(sf).stem == "competitor-landscape-watchlist":
        continue
    prods = {slug for kind, slug in _WIKILINK.findall(body[sf]) if kind == "products"}
    comp_rows.append((m.get("title", Path(sf).stem), m.get("confidence", "—"), prods))
comp_rows.sort(key=lambda r: (CONF_RANK.get(r[1], 3), -len(r[2]), r[0]))
n_competitors = sum(1 for m in meta.values() if m.get("type") == "competitor")
threat = collections.Counter()
for _, _, prods in comp_rows:
    for p in prods:
        threat[p] += 1

comp_head = "".join(f'<th class="rot"><span>{esc(c)}</span></th>' for c, _ in PROD_COLS)
comp_body = ""
for title, conf, prods in comp_rows:
    cells = "".join(f'<td class="{"ok" if pid in prods else ""}">{"●" if pid in prods else ""}</td>'
                    for _, pid in PROD_COLS)
    comp_body += f'<tr><td class="rowname">{esc(title)} {CONF_CHIP.get(conf, "")}</td>{cells}</tr>'
threat_row = "".join(f'<td class="threat">{threat.get(pid, 0) or ""}</td>' for _, pid in PROD_COLS)

# ---------------------------------------------------------------- competitive intel: pricing + win/loss
# Parsed from the structured raw tracking-table entries (Intel type / summary /
# segment / date). Gracefully skipped if raw/ is not present (it is gitignored).
INTEL_DIR = VAULT / "raw" / "notion-competitive-intel-tracking-table"
def _parse_intel_date(s):
    for f in ("%B %d, %Y", "%B %Y"):
        try:
            return datetime.datetime.strptime(s.strip(), f).date()
        except ValueError:
            pass
    return None
pricing_rows = []
winloss = collections.defaultdict(lambda: {"won": 0, "lost": 0, "deals": []})
won_total = lost_total = 0
intel_present = INTEL_DIR.is_dir()
if intel_present:
    for p in sorted(INTEL_DIR.glob("*.md")):
        txt = p.read_text(encoding="utf-8", errors="ignore")
        props, title = {}, ""
        for line in txt.splitlines():
            if line.startswith("# ") and not title:
                title = line[2:].strip()
            mm = re.match(r"^(Company name|Intel type|Intel summary|Date|Product/Market|Segment):\s*(.*)$", line)
            if mm:
                props[mm.group(1)] = mm.group(2).strip()
        itype = props.get("Intel type", "")
        comp = props.get("Company name", "").strip()
        summ = props.get("Intel summary", "").strip() or title
        date = props.get("Date", "")
        if "Pricing" in itype and comp:
            pricing_rows.append({"comp": comp, "seg": props.get("Segment", ""),
                                 "prod": props.get("Product/Market", ""), "summ": summ,
                                 "date": date, "d": _parse_intel_date(date)})
        if "Win/loss" in itype:
            who = comp or "?"
            tl = title.lower()
            if tl.startswith("won") or tl.startswith("renewed"):
                winloss[who]["won"] += 1; won_total += 1; winloss[who]["deals"].append(("W", title))
            elif tl.startswith("lost"):
                winloss[who]["lost"] += 1; lost_total += 1; winloss[who]["deals"].append(("L", title))
    pricing_rows.sort(key=lambda r: (r["comp"], r["d"] or datetime.date(1900, 1, 1)))

if pricing_rows:
    price_body = "".join(
        f'<tr><td class="rowname">{esc(r["comp"])}</td><td>{esc(r["seg"] or "—")}</td>'
        f'<td>{esc(r["prod"] or "—")}</td><td>{esc(r["summ"][:150])}</td>'
        f'<td class="muted nowrap">{esc(r["date"] or "—")}</td></tr>' for r in pricing_rows)
    pricing_card = (f'<div class="card"><h3>Competitor pricing benchmarks — {len(pricing_rows)} '
                    'directional data points (individual deal quotes, not list prices)</h3>'
                    '<table><thead><tr><th class="rowname">Competitor</th><th>Segment</th>'
                    '<th>Product</th><th>Quote / detail</th><th>Date</th></tr></thead>'
                    f'<tbody>{price_body}</tbody></table></div>')
else:
    pricing_card = ('<div class="card"><h3>Competitor pricing benchmarks</h3>'
                    '<p class="muted">Raw tracking-table not present at generation time — '
                    'regenerate with <code>raw/</code> available to populate.</p></div>')

if won_total or lost_total:
    wl_sorted = sorted(winloss.items(), key=lambda kv: -(kv[1]["won"] + kv[1]["lost"]))
    wl_body = "".join(
        f'<tr><td class="rowname">{esc(c)}</td>'
        f'<td class="win" title="{esc(chr(10).join(t for s,t in v["deals"] if s=="W"))}">{v["won"] or ""}</td>'
        f'<td class="loss" title="{esc(chr(10).join(t for s,t in v["deals"] if s=="L"))}">{v["lost"] or ""}</td>'
        f'<td class="muted">{v["won"]-v["lost"]:+d}</td></tr>' for c, v in wl_sorted)
    winloss_card = (f'<div class="card"><h3>Anduin win / loss vs competitor — {won_total} won · {lost_total} lost '
                    f'(net {won_total-lost_total:+d}) across {len(wl_sorted)} competitors</h3>'
                    '<table><thead><tr><th class="rowname">Competitor</th><th>Anduin won</th><th>Anduin lost</th><th>Net</th></tr></thead>'
                    f'<tbody>{wl_body}</tbody></table>'
                    '<p class="muted" style="margin:10px 2px 0;font-size:12px">Anduin\'s outcome in deals where this competitor was named. '
                    'Hover a number to see the deals. Renewals counted as wins. <b>Directional, not a complete record</b> — '
                    'logged intel skews toward losses (teams log competitive losses more often than wins).</p></div>')
else:
    winloss_card = ('<div class="card"><h3>Win / loss by competitor</h3>'
                    '<p class="muted">Raw tracking-table not present at generation time.</p></div>')

# audience
aud_rows = sorted(aud.items(), key=lambda x: -x[1])
aud_html = bars(aud_rows, max(aud.values()) if aud else 1)
onb_html = "".join(f'<span class="pill">{esc(t)}</span>' for t in sorted(onboarding_titles)) or '<span class="muted">None flagged.</span>'

DOC = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Anduin Vault — knowledge graph insight dashboard</title>
<style>
:root{{--bg:#15110e;--panel:#1f1813;--panel2:#251c16;--line:#3a2c22;--ink:#f3eadf;
--muted:#a98e7d;--coral:#ff6b3d;--coral2:#ff9166;--blue:#5b8cff;--green:#3fd09a;--amber:#ffcf5c}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}
.wrap{{max-width:1140px;margin:0 auto;padding:44px 32px 90px}}
.eyebrow{{letter-spacing:.22em;font-size:11px;color:var(--coral);text-transform:uppercase;font-weight:700}}
h1{{font-size:36px;line-height:1.15;margin:10px 0 6px;font-weight:800}}
h1 .accent{{color:var(--coral)}}
.sub{{color:var(--muted);max-width:720px;margin-bottom:30px}}
.muted{{color:var(--muted)}}
.stats{{display:grid;grid-template-columns:repeat(6,1fr);gap:14px;margin-bottom:14px}}
.cf{{font-size:10px;font-weight:700;padding:1px 6px;border-radius:8px;vertical-align:middle;text-transform:uppercase;letter-spacing:.05em}}
.cf.hi{{background:#3a1410;color:var(--coral2);border:1px solid var(--coral)}}
.cf.md{{background:#2b2410;color:var(--amber);border:1px solid #6b561f}}
.cf.lo{{background:#1c2433;color:var(--blue);border:1px solid #2f4470}}
td.threat{{text-align:center;font-weight:800;color:var(--coral2)}}
td.win{{text-align:center;font-weight:800;color:var(--green)}}
td.loss{{text-align:center;font-weight:800;color:var(--coral2)}}
td.nowrap{{white-space:nowrap}}
tr.threatrow td{{border-top:2px solid var(--line);color:var(--coral2)}}
tr.threatrow .rowname{{font-weight:700;color:var(--muted)}}
.stat{{background:var(--panel);border:1px solid var(--line);border-radius:13px;padding:18px}}
.stat.hot{{background:linear-gradient(160deg,#2a1a12,#3a2113);border-color:var(--coral)}}
.stat .num{{font-size:32px;font-weight:800;line-height:1}}
.stat.hot .num{{color:var(--coral2)}}
.stat .lbl{{color:var(--muted);font-size:11px;letter-spacing:.1em;text-transform:uppercase;margin-top:7px}}
.zone{{margin-top:46px}}
.zone-h{{display:flex;align-items:baseline;gap:14px;border-bottom:2px solid var(--coral);padding-bottom:10px;margin-bottom:22px}}
.zone-h .tag{{background:var(--coral);color:#1a0f08;font-weight:800;padding:3px 10px;border-radius:6px;font-size:13px}}
.zone-h h2{{margin:0;font-size:22px}}.zone-h .why{{color:var(--muted);font-size:13px;margin-left:auto}}
.grid2{{display:grid;grid-template-columns:1fr 1fr;gap:18px}}
.grid3{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}
.card{{background:var(--panel);border:1px solid var(--line);border-radius:13px;padding:22px;margin-bottom:18px}}
.card h3{{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:0 0 16px;font-weight:700}}
.bar-row{{display:grid;grid-template-columns:185px 1fr 40px;align-items:center;gap:11px;margin-bottom:9px}}
.bar-label{{font-size:13px;color:#e9ddd0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
.bar-track{{background:var(--panel2);border-radius:6px;height:13px;overflow:hidden}}
.bar-fill{{height:100%;background:linear-gradient(90deg,var(--coral),var(--coral2));border-radius:6px}}
.bar-val{{text-align:right;color:var(--muted);font-size:13px;font-variant-numeric:tabular-nums}}
.god{{display:flex;align-items:center;gap:11px;padding:7px 0;border-bottom:1px solid var(--line)}}
.god:last-child{{border:0}}
.god-deg{{min-width:40px;height:30px;padding:0 6px;display:flex;align-items:center;justify-content:center;background:var(--panel2);border-radius:8px;font-weight:800;color:var(--coral2)}}
.god-name{{font-size:13.5px}}
.pill{{display:inline-block;background:var(--panel2);border:1px solid var(--line);border-radius:18px;padding:4px 11px;font-size:12px;color:#d8c8b8;margin:0 5px 7px 0}}
.pill.warn{{border-color:var(--amber);color:var(--amber)}}
table{{width:100%;border-collapse:collapse;font-size:13px}}
th,td{{padding:6px 8px;text-align:center;border-bottom:1px solid var(--line)}}
td.rowname,th.rowname{{text-align:left;color:#e9ddd0;white-space:nowrap}}
td.ok{{color:var(--green);font-weight:700}} td.gap{{color:#5a4636}}
tr.empty td.rowname{{color:var(--amber)}}
th.rot{{height:96px;vertical-align:bottom;padding:0}}
th.rot span{{display:inline-block;transform:rotate(-60deg);transform-origin:left;white-space:nowrap;font-size:11px;color:var(--muted);width:18px}}
.pcard{{background:var(--panel2);border:1px solid var(--line);border-radius:11px;padding:15px}}
.pcard-top{{display:flex;justify-content:space-between;align-items:center;gap:8px;margin-bottom:9px}}
.pcard-title{{font-weight:700;font-size:14.5px}}
.badge{{font-size:10px;font-weight:800;padding:2px 7px;border-radius:5px;text-transform:uppercase;letter-spacing:.04em}}
.badge.ga{{background:#16402f;color:var(--green)}}.badge.beta{{background:#1d3358;color:var(--blue)}}.badge.dep{{background:#4a2018;color:var(--coral2)}}
.pcard-stats{{display:flex;flex-wrap:wrap;gap:10px;font-size:12px;color:var(--muted);margin-bottom:7px}}
.pcard-stats b{{color:var(--ink);font-size:14px}}
.pcard-meta{{font-size:11.5px;color:var(--muted)}}
.honesty-bar{{display:flex;height:20px;border-radius:6px;overflow:hidden;margin-bottom:14px}}
.seg.extracted{{background:var(--green)}}.seg.inferred{{background:var(--blue)}}.seg.ambiguous{{background:var(--coral)}}
.legend{{display:flex;gap:18px;font-size:13px;flex-wrap:wrap}}
.dot{{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:7px}}
.dot.extracted{{background:var(--green)}}.dot.inferred{{background:var(--blue)}}.dot.ambiguous{{background:var(--coral)}}
.foot{{margin-top:40px;color:var(--muted);font-size:12px;border-top:1px solid var(--line);padding-top:16px}}
a{{color:var(--coral2)}}
@media(max-width:820px){{.stats{{grid-template-columns:repeat(2,1fr)}}.grid2,.grid3{{grid-template-columns:1fr}}}}
</style></head><body><div class="wrap">

<div class="eyebrow">Graphify · Product Knowledge Vault · {TODAY.isoformat()}</div>
<h1>Vault Insight Dashboard <span class="accent">— health & briefing</span></h1>
<p class="sub">{n_pages} wiki pages · {n_edges} edges · {n_comm} communities. Topology from
<code>graph.json</code> joined with page frontmatter (trust, dates, source type, audience).</p>

<div class="stats">
  <div class="stat"><div class="num">{n_pages}</div><div class="lbl">Pages</div></div>
  <div class="stat hot"><div class="num">{len(PRODUCT_FILES)}</div><div class="lbl">Products</div></div>
  <div class="stat"><div class="num">{len(files_by_type.get("source", []))}</div><div class="lbl">Sources</div></div>
  <div class="stat"><div class="num">{len(CUST_FILES)}</div><div class="lbl">Customers</div></div>
  <div class="stat"><div class="num">{n_competitors}</div><div class="lbl">Competitors</div></div>
  <div class="stat"><div class="num">{n_comm}</div><div class="lbl">Communities</div></div>
</div>

<!-- ============================== ZONE A ============================== -->
<div class="zone">
  <div class="zone-h"><span class="tag">A</span><h2>Vault Health</h2>
    <span class="why">What to fix &amp; document next</span></div>

  <div class="grid2">
    <div class="card"><h3>Freshness — pages by age (today {TODAY.isoformat()})</h3>{fresh_html}</div>
    <div class="card"><h3>Stalest dated pages</h3>{stale_html}</div>
  </div>

  <div class="grid2">
    <div class="card"><h3>Trust profile — sources by trust level</h3>{trust_html}</div>
    <div class="card"><h3>Edge honesty</h3>
      <div class="honesty-bar">
        <div class="seg extracted" style="width:{EXTRACTED/max(n_edges,1)*100:.1f}%"></div>
        <div class="seg inferred" style="width:{INFERRED/max(n_edges,1)*100:.1f}%"></div>
        <div class="seg ambiguous" style="width:{AMBIGUOUS/max(n_edges,1)*100:.1f}%"></div></div>
      <div class="legend">
        <span><i class="dot extracted"></i>Extracted {EXTRACTED}</span>
        <span><i class="dot inferred"></i>Inferred {INFERRED}</span>
        <span><i class="dot ambiguous"></i>Ambiguous {AMBIGUOUS}</span></div>
      <p class="muted" style="margin:14px 0 0;font-size:12px">Relations: {esc(", ".join(f"{k} {v}" for k,v in relations.most_common()))}</p>
    </div>
  </div>

  <div class="card"><h3>Coverage matrix — product × source type (· = gap)</h3>
    <table><thead><tr><th class="rowname">Product</th>{cov_head}</tr></thead><tbody>{cov_body}</tbody></table>
  </div>

  <div class="grid2">
    <div class="card"><h3>Products lacking a top-3 source (spec/impl/pricing)</h3>{lowtrust_html}</div>
    <div class="card"><h3>Fragile pages — single source ({len(fragile)})</h3>
      {''.join(f'<span class="pill warn">{esc(x)}</span>' for x in fragile[:30])}</div>
  </div>

  <div class="card"><h3>Knowledge gaps — {len(isolated)} weakly-connected pages (≤1 link)</h3>
    {''.join(f'<span class="pill">{esc(x)}</span>' for x in isolated[:30])}</div>
</div>

<!-- ============================== ZONE B ============================== -->
<div class="zone">
  <div class="zone-h"><span class="tag">B</span><h2>Topical Briefing</h2>
    <span class="why">Per-product &amp; customer view for CS / Sales / RM</span></div>

  <div class="card"><h3>Product profiles ({len(product_rows)})</h3>
    <div class="grid3">{cards_html}</div></div>

  <div class="card"><h3>Customer × product — ● = documented link (amber row = none documented)</h3>
    <table><thead><tr><th class="rowname">Customer</th>{cm_head}</tr></thead><tbody>{cm_body}</tbody></table>
  </div>

  <div class="card"><h3>Competitor × product overlap — ● = competes here · chip = intel confidence · bottom row = competitors per product</h3>
    <table><thead><tr><th class="rowname">Competitor</th>{comp_head}</tr></thead><tbody>{comp_body}
    <tr class="threatrow"><td class="rowname">Competitors / product</td>{threat_row}</tr></tbody></table>
    <p class="muted" style="margin:10px 2px 0;font-size:12px">Source: <a href="graph.html">{n_competitors} competitor pages</a> from the Competitive Intel Repository. Confidence reflects how many corroborating intel entries back the page. The watchlist of single-mention firms is excluded from rows.</p>
  </div>

  {pricing_card}

  {winloss_card}

  <div class="grid2">
    <div class="card"><h3>Audience split — sources by target audience</h3>{aud_html}</div>
    <div class="card"><h3>Onboarding must-reads ({len(onboarding_titles)})</h3>{onb_html}</div>
  </div>
</div>

<div class="foot">Generated from graph.json + {n_pages} page frontmatters ·
<a href="graph.html">interactive graph</a> · <a href="GRAPH_REPORT.md">audit report</a></div>
</div></body></html>"""

OUT = GRAPH.with_name("breakdown.html")
OUT.write_text(DOC, encoding="utf-8")
print(f"Wrote {OUT}  ({len(DOC):,} bytes)")
print(f"  pages={n_pages} products={len(PRODUCT_FILES)} sources={len(files_by_type.get('source', []))} "
      f"customers={len(CUST_FILES)} undated={undated} fragile={len(fragile)} isolated={len(isolated)} "
      f"low_trust_products={len(low_trust_products)}")
