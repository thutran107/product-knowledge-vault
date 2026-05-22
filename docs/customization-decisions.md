# Customization Decisions: Generic Setup vs. This Vault

The generic Obsidian + Claude Code setup gets you a working knowledge base in an hour.
This vault extends that baseline with ten deliberate changes — each one addressing a
specific failure mode that shows up as the knowledge base grows or gets used by a team.

| Decision | Generic setup | This vault | Why it matters |
|----------|--------------|------------|----------------|
| **Wiki folder structure** | Flat topic folders (`wiki/ai-agents/`, `wiki/rag-systems/`) | Typed entity folders (`products/`, `features/`, `customers/`, `concepts/`, `competitors/`, `analyses/`) | At 50+ pages, flat folders collapse — you can't ask "what does this customer use?" without a namespace for customers |
| **CLAUDE.md purpose** | Navigation rules — where to find files, how to link pages | Full schema — page templates with frontmatter, ingest workflow, query workflow, lint workflow, trust hierarchy | Schema-driven output is consistent across every session; ad-hoc prompting isn't |
| **Source tracking** | No provenance — claims written directly onto wiki pages | `wiki/sources/` — one page per ingested document with `trust_level`, `as_of_date`, `source_type` | Every claim traces back to a source; when something looks wrong you know exactly where it came from |
| **Conflict handling** | None — newer ingest silently overwrites older claims | Explicit conflict detection: quotes both claims side by side, applies trust hierarchy, waits for user resolution before writing | Prevents a low-trust sales deck from silently overwriting a high-trust implementation spec |
| **Index file location** | `master_index.md` lives inside `wiki/` | `index.md` at vault root, structured as typed tables by entity type | Claude reads it first every session — root placement removes one navigation step; typed tables let Claude identify the right pages before reading them |
| **Ingest process** | Ad-hoc prompt each time — output quality varies | 8-step structured workflow: assess → summarize to user → conflict check → dedup check → write pages → update index → append to log | Consistent quality regardless of how the prompt is phrased; same output on Monday as on Friday |
| **Document trust hierarchy** | None — all sources treated equally | 12-level ranked list: spec (1) → implementation guide (2) → pricing doc (3) → FAQ (4) → sales deck (5) → ... → roadmap (12) | Conflict resolution is deterministic — no judgment call needed when two sources disagree |
| **Audit log** | None | Append-only `log.md` — every ingest, query, and lint run recorded with source file, document type, as-of date, and conflicts found | Full traceability — any wiki page can be traced back to the session and source that created it |
| **Health checks** | Manual, whenever you remember | Lint auto-triggers after every 5th ingest; checks for orphan pages, stale claims, missing cross-references | Issues get caught while the context is fresh, not after they've compounded across 30 ingests |
| **Onboarding page** | None | `wiki/onboarding.md` — curated must-read list maintained by the AI, updated after each ingest | New team members get a single entry point rather than navigating 50+ pages cold |

---

## How to read this as a build checklist

If you're adapting the [starter CLAUDE.md template](starter-claude-md.md) for your own domain,
these are the decisions to make — in rough order of impact:

1. **Name your entity folders** — what are the typed namespaces for your domain? (products, customers, competitors — or matters, statutes, firms — or papers, authors, concepts)
2. **Write your page templates** — define frontmatter fields and section headings for each entity type; the more precise, the more consistent
3. **Define your trust hierarchy** — which document types are most authoritative in your domain when sources conflict?
4. **Decide what to track as sources** — will you maintain a `wiki/sources/` provenance layer, or write claims directly onto entity pages?
5. **Write your ingest workflow** — how many steps, what gates, what gets confirmed before writing?
6. **Set up your index** — root-level `index.md` with typed tables, or a simpler `master_index.md`?
7. **Add a lint schedule** — after every Nth ingest, or on demand?

The [starter CLAUDE.md template](starter-claude-md.md) includes defaults for all of these.
Swap out the domain-specific parts and you have a working schema.

---

## Related

- [Generic Obsidian + Claude Code setup](guide-generic-obsidian-setup.md) — the baseline this table extends
- [Full vault guide](guide-obsidian-claude-code.md) — end-to-end operational guide
- [Starter CLAUDE.md template](starter-claude-md.md) — copy-ready schema implementing these decisions
