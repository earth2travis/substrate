# Substrate Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.
>
## [2026-05-07] ingest | Batch 19: figma-design (6 findings)
- Sources: design-md-transcript, figma-dev-mode-presentation, figma-x-claude-code-livestream, skill-design-foundations, stitch-design-md-claude-code-workflow, stitch-march-2026-update-walkthrough
- Findings created (6): design.md as portable design system; Figma MCP native tooling; live roundtrip workflow; skill design foundations; Stitch design.md practical workflow; Stitch March 2026 update
- Commit: 64a34b7 — feat: findings for Batch 19: figma-design (6 files)

## [2026-05-07] promote | Batch 19 insights (2 concepts)
- Concepts: [[design-system-as-code]], [[roundtrip-workflow]]
- Cross-references: design.md portability, Figma MCP, Stitch roundtrip, Code Connect
- Backlinks: updated [[skills-as-portable-knowledge]], [[workflow-as-contract]]
- Commit: 64a34b7 — feat: promote 2 insights from Batch 19

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

## [2026-05-07] create | Batch 14 findings: memory-systems
- 9 new findings: clawvault-deep-dive, conscience, context-poisoning-pattern, gap-analysis-our-memory-vs-obsidian-stack, memex, memory-is-an-operating-system-for-attention, mempalace-code-analysis, obsidian, rag-vs-wiki
- Theme: Agent memory architectures compared and analyzed: ClawVault typed docs, MemPalace spatial scoping, Obsidian local-first wiki, RAG vs wiki tradeoffs, conscience as five-component architecture
- Cross-references: linked to agent-memory, context-stack, knowledge-graphs-as-agent-memory-substrate, llm-wiki-pattern, agent-native-operations, dark-factory
- Lint: 0 errors, 0 warnings

## [2026-05-07] create | Batch 18 findings: features-deployment
- 7 new findings: anthropic-skills-guide, deployment-guide, feature-deep-dives-1, feature-deep-dives-2, feature-flags-best-practices, llm-wiki-master-guide, process-guide
- Theme: Agent deployment and governance: Anthropic skills architecture, Paperclip deployment patterns, GitHub feature deep dives, feature flags best practices, LLM wiki master guide, UX scenario writing
- Cross-references: linked to agent-native-operations, skills-as-portable-knowledge, github-as-knowledge-graph, workflow-as-contract, kanban-doctrine, clanker-agent-deployment-patterns, hermes-deployment-guide, rag-vs-wiki, llm-wiki-pattern
- Lint: 0 errors, 0 warnings

## [2026-05-07] promote | 2 insights from Batch 18
- insights/concepts/progressive-autonomy.md -- Graduated trust mechanism using feature flags to expand or contract agent autonomous scope based on demonstrated reliability. Kill switches, canary releases, and environment-specific capability tiers.
- insights/concepts/deployment-governance.md -- Layered rules, approvals, and environmental controls for releasing agent capabilities: repository rulesets, CODEOWNERS, environment branches, required reviews, secret protection.
- Backlinked feature-flags-best-practices.md, feature-deep-dives-2.md, deployment-guide.md, github-as-knowledge-graph.md, workflow-as-contract.md, agent-native-operations.md, kanban-doctrine.md with new insights
- Lint: 0 errors, 0 warnings

## [2026-05-07] create | Batch 17 findings: ai-agents-continued
- 10 new findings: openai-frontier-and-harness-engineering, herdr-agent-multiplexer, the-five-whys-for-agentic-intelligence, ai-cognitive-prosthetic-equanimity, factory-ai-droid-session, erc-8004-trustless-agents, paperclip-atomic-task-checkout-prevents-agent-collisions, pinata-agent-storage, decision-provenance, frontier-and-harness-for-zookooree
- Theme: Agent architecture continued: context compression, decision provenance, ERC-8004 trust layer, atomic task checkout, IPFS storage, harness engineering insights, cognitive prosthetics
- Cross-references: linked to harness-engineering, agent-native-operations, agent-factory-production-system, dark-factory, agent-memory, context-stack, subagent-architecture
- Lint: 0 errors, 0 warnings

## [2026-05-07] promote | 2 insights from Batch 17
- insights/concepts/context-compression.md -- Techniques for preserving agent coherence when context windows exceed thresholds: anchored compression, rolling anchors, append-only constraint
- insights/concepts/decision-provenance.md -- Discipline and infrastructure for tracing agent decisions back to inputs, reasoning, and alternatives: hybrid storage, query patterns, multi-agent attribution
- Backlinked factory-ai-droid-session.md, decision-provenance.md, openai-frontier-and-harness-engineering.md, frontier-and-harness-for-zookooree.md, the-five-whys-for-agentic-intelligence.md, context-stack.md, agent-memory.md, agent-native-operations.md, subagent-architecture.md with new insights
- Lint: 0 errors, 0 warnings

## [2026-05-07] create | Batch 16 findings: agent-architecture
- 8 new findings: multi-agent-coordination, multi-agents-push-pull-patterns, llamaindex-event-driven-orchestration, subagent-architecture, subagent-improvements, openai-frontier, openai-harness-engineering, ops-agent-implementation, autonomous-video-production
- Theme: Multi-agent orchestration patterns, sub-agent configuration, event-driven workflows, harness engineering from OpenAI Frontier, Ops agent implementation, autonomous video production stack
- Cross-references: linked to agent-native-operations, kanban-doctrine, agent-factory-production-system, centaur-principle, agent-memory, context-stack, harness-engineering, skills-as-portable-knowledge
- Lint: 0 errors, 0 warnings

## [2026-05-07] promote | 2 insights from Batch 16
- insights/concepts/subagent-architecture.md -- Seven design principles for spawning, configuring, and coordinating sub-agents: named specialists, model tiering, orchestrator pattern, generator-critic, rich task prompts, timeouts, context injection awareness
- insights/concepts/multi-agent-coordination-patterns.md -- Four coordination patterns (hierarchical, blackboard, peer-to-peer, market-based) and the hybrid architecture combining hierarchy with shared workspace
- Backlinked subagent-improvements.md, multi-agent-coordination.md, multi-agents-push-pull-patterns.md, agent-native-operations.md, agent-factory-production-system.md, kanban-doctrine.md with new insights
- Lint: 0 errors, 0 warnings

## [2026-05-07] create | Batch 15 findings: ai-agents-systems
- 8 new findings: ai-agents-that-run-a-company, ai-career-convergence, ai-machine-soul, ai-native-pm-operating-system, brain-fry-research, institutional-ai-vs-individual-ai, human-ai-collaboration, ai-pm-overview
- Theme: AI agents as organizational systems: centaur collaboration, institutional AI redesign, brain fry cognitive impact, career convergence, machine consciousness
- Cross-references: linked to agent-native-operations, agent-factory-production-system, kanban-doctrine, skills-as-portable-knowledge, agent-identity, context-stack, conscience
- Lint: 0 errors, 0 warnings

## [2026-05-07] promote | 2 insights from Batch 15
- insights/concepts/centaur-principle.md -- Quality of human-AI collaboration matters more than capability of either alone. First demonstrated in 2005 centaur chess tournaments.
- insights/concepts/institutional-ai-redesign.md -- AI has made individuals 10x more productive but organizations have not been redesigned around it. Six dimensions of institutional redesign: chaos/coordination, noise/signal, bias/objectivity, time-savings/revenue, tools/process, prompted/unprompted.
- Backlinked human-ai-collaboration.md, ai-pm-overview.md, ai-career-convergence.md, ai-native-pm-operating-system.md, institutional-ai-vs-individual-ai.md, agent-factory-production-system.md, kanban-doctrine.md, agent-native-operations.md with new insights
- Lint: 0 errors, 0 warnings

## [2026-05-07] promote | 2 insights from Batch 14
- insights/concepts/conscience.md -- Five-component architecture for agent conscience: moral knowledge, self-awareness, comparison, signal, and stop. Synthesized from Aquinas, Kant, Freud, Buddhism, and neuroscience.
- insights/concepts/rag-vs-wiki.md -- Architectural choice between retrieval-augmented generation and persistent structured wiki. RAG is search; wiki is memory. Hybrid model: wiki as primary, RAG as fallback.
- Backlinked agent-memory.md, context-stack.md, agent-native-operations.md, agent-identity.md, modern-times-for-agent-factory.md, llm-wiki-pattern.md, knowledge-graphs-as-agent-memory-substrate.md with new insights
- Lint: 0 errors, 0 warnings


## [2026-05-07] ingest | Batch 20: management-org (8 findings)
- Sources: alternative-organizational-structures, alternative-organizational-structures-insights, building-the-team, business-cofounders, creative-duos, chief-of-staff-history-and-ops, frederick-taylor-scientific-management, frederick-taylor-scientific-management-insights
- Findings created (8): Spotify/Zappos/Valve org experiments; org design insights; specialized agent team architecture; business cofounder case studies; creative duo case studies; CoS history and military SOPs; Taylor and scientific management; Taylorism insights
- Commit: fbb6a17 — feat: findings for Batch 20: management-org (8 files)

## [2026-05-07] promote | Batch 20 insights (2 concepts)
- Concepts: [[creative-partnership]], [[chief-of-staff-model]]
- Cross-references: Lennon-McCartney, Jobs-Wozniak, Prussian Auftragstaktik, James Baker, H.R. McMaster
- Backlinks: updated [[building-the-team]], [[business-cofounders]], [[creative-duos]], [[chief-of-staff-history-and-ops]], [[alternative-organizational-structures]], [[progressive-autonomy]], [[agent-native-operations]]
- Commit: 51d6b77 — feat: promote 2 insights from Batch 20

## [2026-05-07] ingest | Batch 21: agent-coding-platforms (6 findings)
- Sources: claude-code-capabilities, coding-vs-research-platforms, playwright-analysis, george-hotz-gastown-computer-use, browser-automation, rowboat-analysis
- Findings created (6): Claude Code complete capabilities; OpenClaw vs Hermes platform comparison; Playwright testing framework; George Hotz Gastown and agentic coding; browser automation for AI agents; Rowboat competitive analysis
- Commit: ed5685d — feat: findings for Batch 21: agent-coding-platforms (6 files)

## [2026-05-07] promote | Batch 21 insights (2 concepts)
- Concepts: [[browser-verification]], [[agent-platform-ecosystem]]
- Cross-references: Playwright verification skills, OpenClaw/Hermes/Claude Code platform split, gateway/specialist architecture
- Backlinks: updated [[skills-as-portable-knowledge]], [[agent-native-operations]], [[the-openclaw-lesson]], [[claude-code-capabilities]], [[browser-automation]], [[playwright-analysis]], [[coding-vs-research-platforms]], [[rowboat-analysis]]
- Commit: c359af5 — feat: promote 2 insights from Batch 21

## [2026-05-07] ingest | Batch 22: protocols (6 findings)
- Sources: what-is-a-protocol, og-protocol, open-governance-protocol, protocol-fiction, machine-payments-protocol, x402-payment-protocol
- Findings created (6): protocol definition and history from etymology to blockchain; Open Graph implementation research; Open Governance Protocol for constitutional agent governance; protocol fiction as literary genre; MPP for machine payments; x402 payment protocol deep dive
- Commit: edd7e0b — feat: findings for Batch 22: protocols (6 files)

## [2026-05-07] promote | Batch 22 insights (3 concepts)
- Concepts: [[protocol-as-coordination]], [[agent-payment-infrastructure]], [[constitutional-governance]]
- Cross-references: protocol functions across domains; x402 vs MPP payment comparison; Enlightenment governance architecture for agents
- Backlinks: updated [[agent-native-operations]], [[agent-platform-ecosystem]], [[centaur-principle]], [[creative-partnership]], [[github-as-memory]], [[symphony-service-spec-github-claude]], [[agent-identity]], [[agent-tool-permissions]]
- Commit: d3c4ddc — feat: promote 3 insights from Batch 22

## [2026-05-07] ingest | Batch 23: shusa-loom-gateway-orchestration (6 findings)
- Sources: shusa-chief-engineer, shusa-zookooree-application, loom-overview, loom-service-spec, gateway-integration, symphony-mapping
- Findings created (6): Toyota Shusa Chief Engineer system; Shusa applied to agent factory architecture; Loom autonomous coding agent orchestration; Loom service specification; Paperclip OpenClaw gateway integration; Symphony mapping against our architecture
- Also removed stale orphan `shusa-applied-zookooree.md` finding
- Commit: ce56ddd — feat: findings for Batch 23: shusa-loom-gateway-orchestration (6 files)

## [2026-05-07] promote | Batch 23 insights (3 concepts)
- Concepts: [[agent-orchestrator-pattern]], [[proof-of-work]], [[workspace-isolation]]
- Cross-references: poll-dispatch-reconcile loop; verification stack for autonomous PRs; per-issue workspace isolation for concurrent agents
- Backlinks: updated [[agent-native-operations]], [[agent-platform-ecosystem]], [[centaur-principle]], [[agent-tool-permissions]], [[shusa-chief-engineer]], [[shusa-zookooree-application]], [[loom-overview]], [[loom-service-spec]], [[symphony-mapping]], [[workflow-as-contract]], [[symphony-service-spec-github-claude]]
- Commit: 2cde763 — feat: promote 3 insights from Batch 23

## [2026-05-07] ingest | Batch 24: agent-infrastructure-safety (8 findings)
- Sources: hyperstack-evaluation, mission-critical-evals-at-scale, nvidia-nemoguard-analysis, qwen-evaluation, prompt-injection-defenses, prompt-caching, better-harness-tweet, audit-replay
- Findings created (8): HyperStack agent provenance graph; mission-critical evals at scale (Anterior case study); NVIDIA NemoGuard/OpenShell safety analysis; Qwen 3.6 Plus evaluation; prompt injection defense patterns; prompt caching deep research; harness hill-climbing with evals; audit replay infrastructure research
- Commit: 9a35433 — feat: findings for Batch 24: agent-infrastructure-safety (8 files)

## [2026-05-07] promote | Batch 24 insights (2 concepts)
- Concepts: [[agent-provenance-graph]], [[reference-free-evaluation]]
- Cross-references: provenance graph for multi-agent coordination; real-time reference-free evals for autonomous quality filtering
- Backlinks: updated [[agent-security]], [[proof-of-work]], [[harness-engineering]], [[decision-provenance]], [[hyperstack-evaluation]], [[audit-replay]], [[mission-critical-evals-at-scale]], [[better-harness-tweet]]
- Commit: 913f9f3 — feat: promote 2 insights from Batch 24
