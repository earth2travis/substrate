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

## [2026-05-06] create | Batch 4 findings: devops-lean-software cluster
- 6 new findings: continuous-delivery, devops, dora-metrics, lean-software-development-study, lean-startup, seven-software-wastes
- Theme: DevOps practices, DORA metrics, continuous delivery, and lean software waste elimination
- Cross-references: linked to lean-doctrine, dark-factory, harness-engineering, toyota-production-system, lean-production
- Lint: 0 errors, 0 warnings

## [2026-05-06] create | Batch 5 findings: cloudflare-agent-factory cluster
- 11 new findings: cloudflare-ai-platform-inference-layer, cloudflare-workers-ai-edge-inference, cloudflare-queues-decoupling-layer, cloudflare-queues-ai-batch-optimization, cloudflare-email-service-for-agents, cloudflare-ai-gateway-observability, factory-architecture-cloudflare, synthweave-harness-readiness, synthweave-mcp-analysis, ai-sdk-research, paperclip-is-an-os-for-autonomous-agent-companies
- Theme: Cloudflare developer platform as agent factory infrastructure: inference, queues, email, observability, and architecture specs
- Cross-references: linked to harness-engineering, dark-factory, lean-software-delivery, codex
- Lint: 0 errors, 0 warnings

## [2026-05-06] promote | 1 insight from Batch 5
- insights/concepts/cloudflare-first-agent-factory.md — Cloudflare platform as complete substrate for agent operations: inference, queues, email, observability, versioned memory
- Backlinked harness-engineering.md, dark-factory.md, lean-software-delivery.md with new insight
- Lint: 0 errors, 0 warnings

## [2026-05-06] create | Batch 6 findings: openclaw-hermes-agent-platform cluster
- 10 new findings: openclaw-report, openclaw-vs-hermes, openclaw-vs-hermes-coding, openclaw-community, openclaw-platform-state-2026, hermes-agent-report, hermes-agent-platform-analysis, hermes-self-evolution, hermes-deployment-guide, autoresearchclaw-analysis
- Theme: OpenClaw crisis, Hermes Agent secure successor, community dynamics, and auto-research tooling
- Cross-references: linked to openclaw, hermes-agent, clawhavoc-security-crisis, nous-research
- Lint: 0 errors, 0 warnings

## [2026-05-06] promote | 1 insight from Batch 6
- insights/concepts/the-openclaw-lesson.md — Security as foundational, not reactive, traced through pioneer-crisis-succession arc
- Backlinked harness-engineering.md, dark-factory.md, lean-software-delivery.md, cloudflare-first-agent-factory.md with new insight
- Backlinked openclaw.md, hermes-agent.md, clawhavoc-security-crisis.md, nous-research.md with new insight
- Lint: 0 errors, 0 warnings

## [2026-05-06] create | Batch 7 findings: social-layer-community-infrastructure
- 11 new findings: clanker-event-driven-architecture, clanker-agent-deployment-patterns, neynar-platform, stay-on-base-proposal-genuinejack, memetics-as-engineered-cultural-transmission, github-as-memory, project-board-configuration, telegram-group-setup, custom-tooling-opportunities, email-management, current-costs
- Theme: Farcaster/Neynar decentralized social layer, Clanker event-driven architecture, community governance, memetics, agent-native operations tooling
- Cross-references: linked to farcaster-protocol, harness-engineering, dark-factory, kanban-doctrine, the-openclaw-lesson
- Lint: 0 errors, 0 warnings

## [2026-05-06] promote | 2 insights from Batch 7
- insights/concepts/decentralized-social.md — Decentralized social protocols as agent ingestion layer: Farcaster, Neynar, Clanker architecture
- insights/concepts/agent-native-operations.md — Agent-native operations: tools designed for AI-human partnership, session affordances, process automation
- Backlinked harness-engineering.md, dark-factory.md, lean-software-delivery.md, kanban-doctrine.md, cloudflare-first-agent-factory.md with new insights
- Backlinked farcaster-protocol.md, neynar-platform.md, clanker-event-driven-architecture.md, github-as-memory.md, custom-tooling-opportunities.md with new insights
- Lint: 0 errors, 0 warnings

## [2026-05-06] create | Batch 9 findings: context-stack-memory-systems cluster
- 10 new findings: the-context-stack-spec, interchangeable-context, context-stack-as-conscience, context-stack-observations, knowledge-graphs-as-agent-memory-substrate, mempalace-analysis, solving-memory, memory-is-context-not-storage-obsidian-analysis, mempalace-spatial-scoping-for-context-stack
- Theme: Context Stack specification, interchangeable context, conscience architecture, and agent memory systems (ClawVault, MemPalace, knowledge graphs, Obsidian)
- Cross-references: linked to agent-identity, memory-systems, agent-native-operations, the-openclaw-lesson
- Lint: 0 errors, 0 warnings

## [2026-05-06] promote | 2 insights from Batch 9
- insights/concepts/context-stack.md — Portable identity for agents: four-layer markdown specification, interchangeable context, precondition for conscience
- insights/concepts/agent-memory.md — From flat files to structured continuity: hybrid memory architectures, vault index pattern, intent-preserving compaction
- Backlinked agent-identity.md, agent-native-operations.md, the-openclaw-lesson.md, memory-systems.md with new insights
- Lint: 0 errors, 0 warnings

## [2026-05-06] create | Batch 10 findings: lean-manufacturing-infrastructure (post-interrupt)
- 4 new findings: craft-mass-lean-production, production-systems-compared, toyota-factory-planning, value-stream-mapping
- Theme: Toyota production paradigms, greenfield factory planning, and value stream mapping as diagnostics
- Cross-references: linked to production-paradigms, lean-doctrine, toyota-production-system, kaizen, just-in-time
- Lint: 0 errors, 0 warnings

## [2026-05-06] create | Batch 11 findings: synthweave-skills-tools-workflows
- 11 new findings: our-skills-audit, skills-landscape, tools-landscape, workflows-landscape, gstack-analysis, just-bash-analysis, composio-analysis, tool-provisioning-contract, paperclip-patterns-worth-adopting-for-synthweave, browser-efficiency-from-gstack, mak-prompt-engineering-skills
- Theme: Agent skills, tools (MCP), workflows (Symphony/LangGraph/CrewAI), sandboxing, provisioning, browser efficiency, composable pipelines
- Cross-references: linked to agent-native-operations, harness-engineering, dark-factory, the-openclaw-lesson, cloudflare-first-agent-factory, kanban-doctrine
- Lint: 0 errors, 0 warnings

## [2026-05-06] promote | 2 insights from Batch 11
- insights/concepts/skills-as-portable-knowledge.md — Skills as the instruction set for agent systems: progressive disclosure, composability, MCP enhancement
- insights/concepts/agent-tool-permissions.md — Permission models as the weakest link in agent tooling: least privilege, audit trails, budget enforcement
- Backlinked skills-landscape.md, tools-landscape.md, agent-native-operations.md with new insights
- Lint: 0 errors, 0 warnings

## [2026-05-06] create | Batch 12 findings: github-project-management
- 8 new findings: figma-github-projects-plugin, github-capabilities-audit, github-issues-best-practices, github-knowledge-graph-second-brain, github-practices, github-project-best-practices, github-project-management-overview, symphony-service-spec-github-claude
- Theme: GitHub as knowledge graph, issue best practices, project management, Figma plugin architecture, Symphony workflow-as-contract spec
- Cross-references: linked to github-as-memory, project-board-configuration, symphony-orchestrator, agent-native-operations, kanban-doctrine
- Lint: 0 errors, 0 warnings

## [2026-05-06] promote | 2 insights from Batch 12
- insights/concepts/github-as-knowledge-graph.md — GitHub Issues as nodes in an institutional knowledge graph: the memory quality problem and the closure discipline
- insights/concepts/workflow-as-contract.md — Agent behavior versioned in-repo via WORKFLOW.md: separation of policy from orchestration
- Backlinked github-as-memory.md, github-knowledge-graph-second-brain.md, github-issues-best-practices.md, github-practices.md, github-project-best-practices.md, symphony-service-spec-github-claude.md with new insights
- Lint: 0 errors, 0 warnings

## [2026-05-07] create | Batch 13 findings: agent-factory-manufacturing-metaphors
- 8 new findings: heijunka-for-agent-orchestration, heijunka-level-scheduling, kaizen-for-the-agent-factory, modern-times-for-agent-factory, price-minus-for-the-agent-factory, production-systems-for-agent-factories, dark-factory-lights-out-manufacturing, synthesis-agent-factory
- Theme: Toyota production metaphors applied to agent factory operations: Heijunka scheduling, Kaizen improvement, Price-Minus economics, Modern Times conscience, production system evolution
- Cross-references: linked to lean-doctrine, toyota-production-system, dark-factory, production-paradigms, agent-native-operations, kanban-doctrine, context-stack
- Lint: 0 errors, 0 warnings

## [2026-05-07] promote | 2 insights from Batch 13
- insights/concepts/heijunka.md — Production leveling for agent orchestration: interleaving work types, defining takt time, and the Heijunka Box as scheduling framework
- insights/concepts/agent-factory-production-system.md — AFPS modeled on Toyota Production System: JIT agent production, Jidoka oversight, seven wastes translated, six-phase factory planning
- Backlinked toyota-production-system.md, lean-doctrine.md, dark-factory.md, production-paradigms.md with new insights
- Lint: 0 errors, 0 warnings

