# Vault Insight Dashboard — how it's produced

`breakdown.html` is a one-page dashboard that turns the Product Knowledge Vault
into an at-a-glance **health check** (Zone A) and **product briefing** (Zone B).
It is built by joining the knowledge-graph topology with each page's frontmatter.

## How the breakdown view is produced

### Step 0 — Starting point: the vault
The vault is ~135 Markdown pages under `wiki/` (products, features, customers,
concepts, competitors, sources, analyses). Two things make the dashboard possible:
- **Wikilinks** between pages (`[[wiki/products/fundsub]]`) → these become the graph's *edges*.
- **Frontmatter** on every page (`trust_level`, `as_of_date`, `source_type`,
  `target_audience`, `status`, `source_count`…) → these become the *attributes* we analyze.

### Step 1 — Build the knowledge graph (`/graphify`)
Running graphify on the vault reads every page, resolves the wikilinks, and
detects communities. It writes three things into `graphify-out/`:
- `graph.json` — **the data**: nodes, edges (each tagged EXTRACTED/INFERRED),
  communities, hyperedges.
- `graph.html` — interactive force-directed view.
- `GRAPH_REPORT.md` — plain-language audit (god nodes, gaps, etc.).

`graph.json` is the key output — it captures *topology* (who links to whom) but
**not** the page metadata.

### Step 2 — Join topology with frontmatter (`breakdown.py`)
This is the step that creates the insight. The script:
1. **Parses frontmatter** from all `wiki/**/*.md` files, keyed by file path.
2. **Loads `graph.json`** and maps each node → its source file, then builds a
   *file-level adjacency map* (which pages connect to which).
3. **Joins them on `source_file`** — so for any product we know both its
   neighbors (from the graph) *and* its trust/date/type (from frontmatter).
4. **Computes the panels:**
   - Freshness → bucket each page's date vs. today
   - Trust profile → histogram of source `trust_level`
   - Coverage matrix → for each product, which `source_type`s exist among its linked sources
   - Product cards → degree + neighbors + frontmatter per product
   - Customer × product → customer↔product edges from the graph

### Step 3 — Render to a self-contained page
The script writes everything into `breakdown.html` — inline CSS, no
dependencies, opens in any browser.

### Step 4 — View & refresh
```bash
# generate (or regenerate after the vault changes)
python3 "graphify-out/breakdown.py"

# open it
open "graphify-out/breakdown.html"
```

If you've **added or edited pages**, refresh in two steps: re-run `/graphify`
first (to rebuild `graph.json` with new links), then `breakdown.py` (to re-join).
If you only changed **frontmatter** on existing pages, just re-run `breakdown.py`.

## Mental model

> Vault (pages + links + frontmatter) → `/graphify` → `graph.json` (topology)
> → `breakdown.py` joins topology + frontmatter → `breakdown.html` (dashboard).

## What's in the dashboard

- **Zone A — Vault Health** (for maintainers): freshness/undated pages, source
  trust profile, product × source-type coverage matrix, products lacking an
  authoritative source, fragile single-source and weakly-connected pages.
- **Zone B — Topical Briefing** (for CS / Sales / RM): a profile card per
  product, a customer × product matrix, the content audience split, and the
  onboarding must-read list.

> Note: the customer × product matrix is edge-derived, so it reflects
> *documented* links — an empty (amber) row means under-documentation, not
> necessarily that the customer runs no products.
