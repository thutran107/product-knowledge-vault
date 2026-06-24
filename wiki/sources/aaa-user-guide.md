---
type: source
title: "AAA (Advisor Advantage) — User Guide (RIA User Guide)"
date_ingested: 2026-06-15
as_of_date: 2025-12-31
source_type: implementation-guide
trust_level: 2
original_file: Notion — RIA User Guide (15f3f653b1df80979bcce41a69c61de5)
products: [AAA]
target_audience: CS | Sales + RM
onboarding_required: Yes
tags: [aaa, advisor, ria, implementation, help-docs]
---

## Summary
The index of published end-user help articles for Advisor Advantage, mirrored from Anduin's HelpJuice support site (support.anduintransact.com/en_US/advisor-advantage). It is a curated link hub rather than prose, organizing the canonical how-to guides for both fund managers and advisors into Published, Needs-update, and Archived buckets.

## Key Takeaways
- **Published guides** (canonical):
  - Fund Manager Guide: Invite Advisor Entity to your fund
  - How to view the advisor's contribution to the fund
  - Explained: Advisor entity whitelist email domain
  - Advisor Guide: Permission
  - Error Handling: "The account has no access as an advisor"
- **Needs update** (use with caution): How to create an advisor entity; How to accept the fund's link invitation; Advisor Guide: Accepting an Invitation from a Fund Manager.
- **Archived** (do not use): Fund manager: Managing Advisor Invitations.
- Public help content lives on HelpJuice at `support.anduintransact.com/en_US/advisor-advantage`.

## Connections
- Implementation/how-to backbone for [[products/aaa|AAA (Advisor Advantage)]]; complements the deeper [[sources/aaa-cs-training|CS Training]] (which explains the concepts the user guides operationalize).
- The "whitelist email domain" and "Advisor Permission" articles map to the email-domain automation and permission model documented in the sales/CS decks.

## Conflicts & Supersessions
- None. This is a pointer to externally-published help docs; no claims conflict with other pages. Note the "Needs update" bucket — entity-creation and invitation-acceptance articles may lag current UX.

## Raw Notes
- The Notion row is a blank shell; content is the linked "RIA User Guide" page (last viewed 2025-12-31), itself a list of HelpJuice-published articles. Dated here as 2025-12-31; the underlying row has no as-of date.
- Document Type = "Implementation Guide" (trust 2). Per CLAUDE.md §7, ingesting a trust 1–3 source auto-triggers a lint.
- onboarding_required: Yes.
- Individual HelpJuice article bodies were not fetched into the vault (they live on the public support site).
