# README Rewrite Design

**Date:** 2026-05-22
**Branch:** memory-wiki

## Goal

Rewrite the vault README to be engaging and instructive for Hivemind learners — people who are AI-native and comfortable with vibe-coding but new to Obsidian as a knowledge management tool.

## Audience

AI-native knowledge workers who already use Claude Code / LLMs but haven't built a persistent local knowledge base before. They don't need convincing about the AI angle; they need to understand why Obsidian + a schema-driven CLAUDE.md is more powerful than ad-hoc prompting.

## Approach: "The Upgrade Path"

Open with the generic 6-step Obsidian + Claude Code setup as the baseline, then walk through each design decision that extends it — framing each as "here's the standard approach, here's the problem it hits, here's what's different here." The Anduin vault is the worked example throughout.

## Structure

1. **Opening hook** — what the vault can answer right now (3 example queries), one-line framing of the pattern
2. **The pattern** — Karpathy wiki method in plain language, stack table
3. **The starting point** — compact 6-step generic setup with link to full guide
4. **The upgrade: 5 design decisions** — the core of the README
   - Typed entity folders vs. flat topic folders
   - CLAUDE.md as a schema vs. navigation rules
   - Source provenance + trust hierarchy
   - Structured ingest with conflict detection
   - Root-level index.md as a structured catalog
5. **What's in this vault** — product coverage table (13 products, 54 sources, 17 customers)
6. **Navigation + queries** — how to use the vault, 3 example queries
7. **Build your own** — links to both guide docs

## Design Decisions

Each "upgrade" block uses a consistent three-part structure:
- **Standard approach** — what the generic setup does
- **The problem** — where it breaks down at scale or under team use
- **Decision here** — what this vault does differently and why

This respects the reader's intelligence (they know the basic pattern) and makes the design rationale explicit rather than buried in CLAUDE.md.

## Related Files

- `README.md` — the output
- `docs/guide-generic-obsidian-setup.md` — the generic baseline referenced in section 3
- `docs/guide-obsidian-claude-code.md` — the full end-to-end guide referenced in the footer
- `CLAUDE.md` — the schema the README describes
