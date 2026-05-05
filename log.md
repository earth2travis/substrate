# Substrate Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

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
- Cross-references: [[auftragstaktik-mission-command]], [[agentic-architecture]], [[toyota-production-system]], [[research/raw/hermes-kanban-deep-dive]]
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
