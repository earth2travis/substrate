# Substrate Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-05-06] no-op | Daily synthesis — no new/changed sources
- Ingest: 311 files scanned, 0 new, 0 changed, 2 orphan findings (`five-whys.md`, `28-openclaw-mistakes.md`)
- No synthesis required. Exiting cleanly.

## [2026-05-05] no-op | Daily synthesis — no new/changed sources
- Ingest: 311 files scanned, 0 new, 0 changed, 2 orphan findings (false positives: stem mismatch on five-whys and 28-openclaw-mistakes)
- No synthesis required. Exiting cleanly.

## [2026-05-05] create | Kanban Operating Manual
- File created: guides/kanban-operating-manual.md (~10KB)
- Content: Unified field manual combining Doctrine (3 Rules) and Tooling (full CLI reference, metadata schemas, lifecycle, workspace kinds)
- Cross-references: [[kanban-doctrine]], [[kanban-vs-delegate-task]], [[kanban-metadata-rules]]
- Updated INDEX.md with new guide entry
- Status: committed to main

## [2026-05-05] create | Kanban Doctrine
- Source: research/raw/auftragstaktik-mission-command.md
- File created: insights/concepts/kanban-doctrine.md (133 lines, ~5.5KB)
- Content: Seven principles drawn from Auftragstaktik mapped to our Kanban operating model
  1. Commander's Intent (the "Why")
  2. Kanban vs delegate_task decision rules
  3. Backbrief and metadata schema
  4. Disciplined Initiative
  5. Shared Mental Models via Substrate
  6. Stop-the-Line Authority (kanban_block)
  7. Speed over Perfect Coordination
- Cross-references: [[auftragstaktik-mission-command]], [[agentic-architecture]], [[toyota-production-system]], [[hermes-kanban-deep-dive]]
- Commit: 37ef008 on main

## [2026-05-04] no-op | Daily synthesis — no new/changed sources
- Ingest: 311 files scanned, 0 new, 0 changed, 0 orphan findings
- No synthesis required. Exiting cleanly.

## [2026-05-04] create | Cron job: substrate-daily-synthesis
- Automated daily synthesis pipeline wired
- Runs daily at 06:00 UTC via cron job `89294cb62751`
- Flow: `_ingest.py` generates digest → agent reads digest → synthesizes findings → creates/updates insights → commits → opens PR
- Branch naming: `auto/ingest-YYYYMMDD-HHMMSS`
- Early exit if no new/changed/orphan files
- Constraint: never modifies `research/raw/`

## [2026-05-04] ingest | Hermes Kanban deep dive
- Sources: Hermes Agent Kanban docs (overview + tutorial), kanban-worker skill, kanban-orchestrator skill
- File created: research/raw/hermes-kanban-deep-dive.md (29KB)
- Content: Hermes Kanban capabilities, CLI reference, REST surface, collaboration patterns, plus history and philosophy of Kanban (Toyota TPS origins, Lean, David Anderson's Kanban Method)
- Cross-references to existing pages: [[taiichi-ohno]], [[toyota-production-system]], [[value-stream-mapping]]

## [2026-05-05] create | Kanban Doctrine from Auftragstaktik
- Insight: insights/concepts/kanban-doctrine.md — Auftragstaktik mapped to agent operations (Intent Over Instruction, Block Before Guess, Handoff Is Signal)
- Guide: guides/kanban-vs-delegate-task.md — Decision matrix for Kanban vs delegate_task
- Decision: decisions/kanban-metadata-rules.md — Metadata schemas by work type (coding, research, review, infra, docs)
- Source: research/raw/auftragstaktik-mission-command.md
- Updated INDEX.md with cross-references

## [2026-05-04] create | Repository initialization
- Repository: https://github.com/earth2travis/substrate
- Local path: /home/sivart/substrate
- WIKI_PATH set in ~/.hermes/.env
- Existing structure: SCHEMA.md, INDEX.md, research/raw/, insights/, decisions/, guides/, retros/, specs/, skills/
- Note: repo already contains extensive raw sources and insights structure

## [2026-05-06] create | Batch 2 findings: process-philosophy cluster
- 11 new findings: becoming, dependent-origination, duration-duree, elan-vital, gilles-deleuze, henri-bergson, intuition-vs-intellect, nagarjuna, rhizome, sunyata-emptiness, virtual-and-actual
- Theme: Bergson/Deleuze/Nagarjuna process philosophy mapped to AI architecture
- Cross-references: linked to process-philosophy, actual-occasions, prehension, concrescence
- Lint: 0 errors, 0 warnings

## [2026-05-06] promote | 3 insights from Batch 2
- insights/concepts/emptiness-and-dependent-origination.md — Nagarjuna's emptiness as computational architecture
- insights/concepts/duration-and-living-time.md — Bergson's durée mapped to tokenization and attention
- insights/concepts/deleuzian-becoming.md — becoming as AI design principle vs fixed identity
- Updated process-philosophy.md with backlinks to new insights
- Lint: 0 errors, 0 warnings

## [2026-05-06] create | Batch 3 findings: manufacturing-history cluster
- 8 new findings: craft-production, industry-4.0, mass-customization, mass-production, scientific-management, chief-engineer-system, obeya, shusa-applied-zookooree
- Theme: production paradigms (craft → mass → lean → industry 4.0) and Toyota integration systems
- Cross-references: linked to toyota-production-system, lean-doctrine, dark-factory, harness-engineering, symphony-orchestrator
- Lint: 0 errors, 0 warnings

## [2026-05-06] promote | 2 insights from Batch 3
- insights/concepts/chief-engineer-system.md — Toyota Shusa as integration pattern for agent orchestration
- insights/concepts/production-paradigms.md — craft/mass/lean/industry-4.0 arc applied to agent systems
- Backlinked lean-doctrine.md, dark-factory.md, harness-engineering.md, toyota-production-system.md with new insights
- Lint: 0 errors, 0 warnings
