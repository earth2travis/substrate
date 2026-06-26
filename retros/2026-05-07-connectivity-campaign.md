---
title: "Connectivity Campaign and Concept Promotion Retro"
tags: [retro, maintenance, connectivity, concept-promotion, lint, wikilinks]
related:
- kanban-doctrine
- llm-wiki-pattern
- agent-memory
- kaizen
source: internal-process
---

# Connectivity Campaign and Concept Promotion Retro

## 2026-05-07

## What Was Attempted

This maintenance cycle had one goal: move the Substrate from a pile of files to a connected knowledge graph. The work broke into four phases.

**Phase 0: Ingest backfill.** 311 raw files produced 313 findings and 73 concepts. Branch `auto/ingest-20260506-040805`, merged.

**Phase 1: Structural repair.** Frontmatter was malformed across 388 files. The linter reported 366 errors. We repaired them to 0.

**Phase 2: Connectivity campaign.** Three passes over the graph inserted 214 new wikilinks through 60 bridge concepts. Before: orphan findings existed. After: zero.

**Phase 3: Concept promotion.** We audited findings by graph centrality and elevated 8 to durable concept pages.

Tools used: `scripts/_lint.py` for structural validation, `scripts/_ingest.py` for digest generation, agent-driven synthesis via the `llm-wiki` skill, and GitHub for version control.

---

## What Worked

**Lint automation was the floor.** The linter gave us a binary signal. Without it, frontmatter rot would have spread silently. Auto-fix for `naming-convention` and `fm-tags-empty` saved manual drudgery. Running lint before every commit prevented regressions.

**Bridge concept selection was the lever.** Instead of linking findings to findings directly, we used existing concepts as bridges. A finding about Toyota Shusa links to `[[chief-engineer-system]]`, which links to `[[agent-orchestrator-pattern]]`, which links to `[[kanban-doctrine]]`. This creates readable paths, not just connections.

**Batch link insertion was the throughput.** Doing connectivity in three phases let us validate the pattern before scaling. Phase 1 proved the method. Phase 2 scaled it. Phase 3 mopped up edge cases. Each phase was committed separately, which made rollback possible if a bridge concept turned out to be wrong.

**Centrality beats frequency.** The 8 promoted concepts were not the most frequently mentioned. They were the most connected. `[[kaizen]]` and `[[llm-wiki-pattern]]` act as hubs. Promoting them strengthened the graph more than promoting any niche topic would have.

---

## What Was Harder Than Expected

**Frontmatter edge cases.** The YAML parser is minimal. It choked on colons in titles, unquoted strings, and inline comments. Files with complex frontmatter needed hand repair. We should have caught these during ingest, not during lint.

**Duplicate frontmatter blocks.** Some files, notably `insights/concepts/the-openclaw-lesson.md`, had two frontmatter blocks separated by body text. The linter saw the first and ignored the second. The parser saw both and failed. Root cause: manual edits that appended a second block instead of replacing the first. Fix: replace, do not append.

**Counting discrepancies.** The initial SCHEMA.md reported 388 total files. The actual count of `.md` files in structured directories was lower. The difference came from including root files (`SCHEMA.md`, `INDEX.md`, `log.md`) and non-markdown assets. We fixed the count logic to count `.md` files only in structured directories (`research/`, `insights/`, `decisions/`, `guides/`, `retros/`, `specs/`).

**Raw file forward references.** Raw files may reference concepts not yet in Substrate. These are intentional forward references, not errors. But the linter reports them as `broken-wikilink`, which clutters the output. We reclassified these to INFO level, not ERROR, but the noise remains.

---

## Surprises

**The graph was denser but less connected than assumed.** We had 313 findings and 81 concepts. That sounds like a graph. But many findings had zero inbound links. They were islands. The density of content masked the sparsity of connectivity.

**Thematic groups emerged organically.** During Phase 2, clusters became visible: manufacturing metaphors, memory systems, governance patterns, creative partnerships. These were not planned. They were discovered by tracing link density. This suggests the graph knows more about its own structure than the curator does.

**Concept promotion is lossy.** Elevating a finding to a concept page means the original finding still exists. Two versions of the same knowledge now live in the repo. We have not decided whether findings should be archived, redirected, or left as historical anchors.

---

## Decisions Made

**Promote by centrality, not frequency.** A concept mentioned 50 times in raw files but linked twice in the graph is less valuable than a concept mentioned 10 times but linked 30 times. Centrality measures structural importance. Frequency measures mention noise.

**Fix counts to count `.md` only.** Root files and non-markdown assets are excluded from the knowledge graph inventory. SCHEMA.md and INDEX.md now reflect `.md` files in structured directories only.

**Replace, do not append, for duplicate frontmatter.** When a file already has frontmatter, any new frontmatter must replace the old block entirely. Appending creates an invalid dual-block state that parsers reject.

**Three phases of connectivity, not one.** A single pass would have missed edge cases. Phases allowed us to learn the graph's shape as we worked.

---

## Open Questions / Next Work

**Remaining 65 high-centrality findings.** The promotion audit identified 65 findings with high centrality that were not promoted. They may deserve concept pages. They may not. The criteria for promotion remain fuzzy: centrality is necessary but not sufficient. A finding needs to be durable, not just connected.

**Empty `comparisons/` and `evals/` directories.** These directories exist in the repo structure but contain no files. Are they for future use, or should they be removed to reduce surface area?

**Thematic groups as tags.** The organic clusters discovered during connectivity are not formalized. Should they become a tag taxonomy? Should we create a `tags/` directory? Or should tags remain lightweight and emergent?

**Concept promotion cleanup.** When a finding is promoted to a concept, what happens to the original finding? Options: archive it, redirect it with a stub, or leave it as a secondary source. We have not chosen.

**Raw file grooming.** 311 raw files produce noise. Some are obsolete. Some are duplicates. A raw file audit is overdue.

**Daily synthesis pipeline noise.** The cron job runs at 06:00 UTC. On no-op days, it still opens and closes branches. This creates git noise. Should no-op days skip branch creation entirely?

---

## Metrics

| Metric | Before | After |
|---|---|---|
| Total `.md` files checked | 388 | 722 |
| Lint errors | 366 | 0 |
| Lint warnings | 0 | 0 |
| Orphan findings (no inbound links) | >50 | 0 |
| New wikilinks added | ~existing | +214 |
| Bridge concepts used | ~existing | 60 |
| Concepts promoted | 73 | 81 (+8) |
| Concepts created from Batch 19 | — | +2 (design-system-as-code, roundtrip-workflow) |
| Concepts created from Batch 20 | — | +2 (creative-partnership, chief-of-staff-model) |
| Concepts created from Batch 21 | — | +2 (browser-verification, agent-platform-ecosystem) |
| Concepts created from Batch 22 | — | +3 (protocol-as-coordination, agent-payment-infrastructure, constitutional-governance) |
| Concepts created from Batch 23 | — | +3 (agent-orchestrator-pattern, proof-of-work, workspace-isolation) |
| Concepts created from Batch 24 | — | +2 (agent-provenance-graph, reference-free-evaluation) |
| High-centrality findings promoted | 0 | 8 |
| Files with duplicate frontmatter | 1+ | 0 |

---

## The Map for the Next Traveler

1. Run lint before every commit. It is cheap and prevents rot.
2. Replace frontmatter; never append.
3. Count `.md` files in structured directories only.
4. Use bridge concepts, not direct finding-to-finding links.
5. Promote by centrality. Let the graph tell you what matters.
6. Do connectivity in phases. You will learn the graph's shape as you work.
7. Raw files are forward references, not errors. Do not chase their broken links.
8. The graph knows more than you do. Trace its density to discover structure you did not plan.

---

*Retro written: 2026-05-07*
*Next retro due: after the next maintenance cycle or when the Substrate exceeds 1000 nodes.*
