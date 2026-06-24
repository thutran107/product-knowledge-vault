---
type: source
title: "Automated Document Repository (Box)"
date_ingested: 2026-04-20
as_of_date: undated
source_type: spec
trust_level: 1
original_file: raw/Automated document repository.md
products: [Integration Hub, FundSub]
target_audience: CS
onboarding_required: No
tags: [integration, box, document-retrieval, fundsub]
---

## Summary
Describes the Box integration that automatically transfers subscription and supporting documents from Anduin FundSub to a customer's Box storage, organized by document type (main subscription, AML/KYC, tax, etc.).

## Key Takeaways
- Pattern: **Document Retrieval** — Anduin → Box.
- Self-configured: customers enter their own Box credentials; no password sharing with Anduin.
- Supports folder customization by document type: main subscription, AML/KYC, tax documents, etc.
- Target persona: FundSub customers who need to move documents out of Anduin for downstream workflows, especially those preferring self-service.
- Prerequisite: customer must retrieve Box credentials; customer must have admin access to intended funds (or know someone who does).

## Connections
- [[concepts/integration-patterns|Integration Patterns]] — Document Retrieval pattern.
- [[entities/box|Box]] — the third-party system.
- [[products/fundsub|FundSub]] — the Anduin source.
- [[concepts/configuration-vs-permission|Configuration vs Permission]] — permission flow applies here.

## Conflicts & Supersessions
None identified at time of ingest.

## Raw Notes
- Setup flow (Install → Name → Link to funds → Configure → Validate) is the same as the SFTP integration; guide cross-references SFTP steps.
