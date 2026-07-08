# Substrate Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.
>
## [2026-06-25] no-op | Daily synthesis — no new/changed sources
- Ingest: 356 files scanned, 0 new, 0 changed, 0 SHA drift, HTML excluded: 0
- Lint: not run (no synthesis; lint is the gate for commits, none made)
- Orphan findings: 24 (unchanged from 2026-06-24)
- No synthesis required. Exiting cleanly.

## [2026-06-24] no-op | Daily synthesis — no new/changed sources
- Ingest: 356 files scanned, 0 new, 0 changed, 0 SHA drift, HTML excluded: 0
- Lint: not run (no synthesis; lint is the gate for commits, none made)
- Orphan findings: 24 (unchanged from 2026-06-23)
- No synthesis required. Exiting cleanly.

## [2026-06-23] no-op | Daily synthesis — no new/changed sources
- Ingest: 356 files scanned, 0 new, 0 changed, 0 SHA drift, HTML excluded: 0
- Lint: not run (no synthesis; lint is the gate for commits, none made)
- Orphan findings: 24 (unchanged from 2026-06-18)
- No synthesis required. Exiting cleanly.

## [2026-06-18] no-op | Daily synthesis — no new/changed sources
- Ingest: 356 files scanned, 0 new, 0 changed, 0 SHA drift, HTML excluded: 0
- Lint: not run (no synthesis; lint is the gate for commits, none made)
- Orphan findings: 24 (up from 2 on last no-op [2026-05-06])
  - Mission/linguistics batch (~2026-05-15, 12): robert-morrison-finding, adoniram-judson-finding, sequoyah-cherokee-finding, wycliffe-sil-finding, medieval-mission-concept, jesuit-missions-concept, missio-dei-concept, apostolic-mission-foundation, protestant-missions-concept, religious-mission-comparative, missionary-linguist-tool-inventor, james-evans-finding
  - NASA cluster (2): nasa-mission-model, nasa-lifecycle-gates-and-decadal-survey
  - Intent/business (4): grove-okrs-intent-architecture, mission-in-business, sinek-golden-circle, goal-primitive-three-implementations
  - Other (4): deseret-alphabet-finding, fable-5-loops-and-memory, run-worker-first-asset-misroute-masking, wrangler-3-vinext-handler-detection-failure
  - Known stem-mismatch false positives (2): five-whys, 28-openclaw-mistakes
- Assessment: 22 of 24 are genuine orphans from batches whose findings were written but never back-linked into the insight graph. Not synthesis work; a connectivity campaign (add incoming `[[wikilinks]]` to the orphan stems from bridge concepts) is the right remedy, recommended for a future session.
- No synthesis required. Exiting cleanly.

## [2026-06-16] ingest | Marc Andreessen's radical information diet
- Source: Marc Andreessen X article + tweet, March 9, 2026
- File created: research/raw/andreessen-information-diet.md (~13KB deep dive)
- Content: Four-quadrant information diet (1/4 X, 1/4 practitioner podcasts, 1/4 AI models, 1/4 old books), opportunity cost principle, Lindy Effect, barbell strategy, signal-to-noise optimization, connection to Andreessen's broader philosophy (agency, E-shaped careers, AI as philosopher's stone, time to build), implications for agent systems and missions architecture
- Cross-references: [[agent-memory]], [[intent-architecture]], [[lean-doctrine]], [[kanban-doctrine]], [[llm-wiki-pattern]]
- Research opportunities identified: Lindy Effect audit of the Substrate, practitioner mental models extraction pipeline, agent tool signal-to-noise audit, curation architecture problem, barbell strategy for agent risk
- Trigger: operator shared the tweet and requested deep dive

## [2026-06-14] ingest | myth-of-sisyphus-camus
- Source: Albert Camus, *The Myth of Sisyphus* (1942)
- File created: research/raw/myth-of-sisyphus-camus.md (~18KB deep dive)
- Content: The Absurd (definition, feeling of exile), central question of suicide, three responses (physical suicide, philosophical suicide, revolt), three consequences (revolt, freedom, passion), absurd man sketches (Don Juan, actor, conqueror), absurd creation and Dostoevsky critique, the myth of Sisyphus and "One must imagine Sisyphus happy," appendix on Kafka, philosophical context (Kierkegaard, Nietzsche, existentialism), critical reception (Nagel), relation to Camus's other works
Trigger: operator finished reading the work and requested deep dive for the Substrate

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

## [2026-05-07] promote | Connectivity campaign + concept promotion audit (8 concepts)
- Phase 1: 58 links via 10 bridge concepts
- Phase 2: 92 links via 21 bridge concepts
- Phase 3: 64 links via 29 bridge concepts
- All 313 findings now have at least 1 incoming link from a non-raw file. Zero orphans remain.
- Concept promotion audit identified 8 high-centrality findings elevated to concepts:
  [[openclaw]], [[hermes-agent]], [[kaizen]], [[llm-wiki-pattern]], [[github-as-memory]], [[process-without-substance]], [[browser-automation]], [[tools-landscape]]
- Fixed duplicate frontmatter in insights/concepts/the-openclaw-lesson.md
- Updated INDEX.md and SCHEMA.md with corrected counts
- Lint: 0 errors, 0 warnings
- Commits: b4baca2, 35684d1, cfa88ae (INDEX/SCHEMA), [this commit]

## [2026-05-07] promote | Batch 24 insights (2 concepts)
- Concepts: [[agent-provenance-graph]], [[reference-free-evaluation]]
- Cross-references: provenance graph for multi-agent coordination; real-time reference-free evals for autonomous quality filtering
- Backlinks: updated [[agent-security]], [[proof-of-work]], [[harness-engineering]], [[decision-provenance]], [[hyperstack-evaluation]], [[audit-replay]], [[mission-critical-evals-at-scale]], [[better-harness-tweet]]
- Commit: 913f9f3 — feat: promote 2 insights from Batch 24

## [2026-05-15] research | mission etymology
- Sources: etymonline.com, Wikipedia Mission-type tactics, Army War College Parameters
- Raw: etymology-of-mission.md (Latin root → Jesuit dispatch → diplomacy → aviation → Prussian philosophy)
- Finding: etymology-of-mission.md (mission vs. order structural distinction, Auftragstaktik history, British failure in Iraq)
- Concept updated: [[mission-command]] — added Mission vs. Order section, Etymological Note, backlink to [[etymology-of-mission]]
- Backlinks: updated [[auftragstaktik-mission-command]] finding to link to new finding
- Insight: the word 'mission' as military dispatch is 1929; the philosophy traces to 1806 Prussia

## [2026-05-15] research | OPORD and Mission Command deep dive (3 workstreams)
- Raw files: opord-format-deep-dive.md, mission-command-philosophy-deep-dive.md, opord-mission-command-synthesis.md
- Findings: same titles, synthesized from raw + web research
- Workstream A: OPORD format mechanical dive (5 paragraphs, annexes, echelon cascade, graphics, digital evolution, branch variations)
- Workstream B: Mission Command philosophy (ADP 6-0, Desert Storm, Basra 2003, Afghanistan, IDF, drone swarms, intent failure modes)
- Workstream C: Synthesis (Paragraph 2 Test, cascade problem, OKR/agile/agent parallels, Weick/Drucker/Marquet)
- Concept updated: [[mission-command]] — added deep-dive backlink section and OPORD-Agent parallel table
- Commits: ccb3b1b (etymology), 39ee6c1 (standardization), 7d8996b (deep dive), [this commit] (concept update)

## [2026-05-15] ingest | NASA mission model research (6 raw, 1 finding, 1 concept update)
- Raw sources created (6):
  - research/raw/nasa-npr-7120-5f-overview.md (NPR 7120.5F lifecycle standard from NODIS)
  - research/raw/nasa-discovery-program.md (Discovery Program: goals, cost cap, 16 missions, PI model)
  - research/raw/nasa-new-frontiers-program.md (New Frontiers: AO selection, PI responsibilities, 4 missions)
  - research/raw/nasa-mars-exploration-program.md (Mars Exploration: 60+ year program, habitability question)
  - research/raw/nasa-planetary-science-programs-overview.md (Program classification: Discovery/New Frontiers/Mars/Flagship)
  - research/raw/nasa-mission-taxonomy.md (nasa.gov/missions metadata taxonomy: status, type, target, program)
- Finding created: research/findings/nasa-mission-model.md (synthesized hierarchy: Directorate > Program > Project > Mission)
- Concept updated: insights/concepts/mission-command.md — added "The NASA Parallel" section linking NASA organizational architecture to mission command doctrine. Proved mission-based organization scales beyond military into science and public administration.
- Key insight: "Congress funds Projects. The public rallies around Missions." The PI is the distributed commander. NPR 7120.5F is the General Staff. The Decadal Survey is the commander's intent.

## [2026-05-15] ingest | Grove's OKRs deep research (1 raw, 1 finding, 1 concept)
- Raw source created: research/raw/grove-okrs-intel-high-output-management.md (Wikipedia OKR, Andrew Grove, High Output Management, MBO, What Matters examples)
- Finding created: research/findings/grove-okrs-intent-architecture.md (synthesized: MBO → iMBOs → OKR lineage, mechanics, spread Intel→Google→industry, NASA PI-led parallel, cascade problem, failure mode taxonomy, agent-native implications)
- Concept promoted: insights/concepts/objectives-and-key-results.md (OKR as civilian intent architecture: Objective = commander's intent, KR = verifiable outcome, Initiative = disciplined initiative)
- Cross-references: linked to [[mission-command]], [[mission-in-business]], [[opord-mission-command-synthesis]], [[nasa-mission-model]], [[principal-agent-theory]], [[kanban-doctrine]], [[progressive-autonomy]], [[centaur-principle]], [[institutional-ai-redesign]]
- Updated INDEX.md with new concept entry under "Mission and purpose"
- Lint: 0 errors, 0 warnings

- Sources: Wikipedia on mission statement, management by objectives, OKRs, Built to Last, Simon Sinek
- Raw file created: research/raw/mission-in-business-context.md
- Finding created: research/findings/mission-in-business.md
- Insight promoted: insights/concepts/mission-in-business.md
- Cross-references: links to [[mission-arc]], [[mission-command]], [[principal-agent-theory]], [[kanban-doctrine]], [[progressive-autonomy]], [[intelligence-graph-organization]]
- Backlinks: updated INDEX.md with new "Mission and purpose" section
- Inventory update: 314 findings, 82 concepts, 312 raw sources

## [2026-05-15] research | Drucker's Management by Objectives deep dive (1 raw, 1 finding, 1 concept)
- Raw source created: research/raw/drucker-management-by-objectives-deep-dive.md (Drucker biography, MBO five steps, Deming critique, OKR evolution, principal-agent contract mapping, military/NASA parallels)
- Finding created: research/findings/drucker-management-by-objectives-deep-dive.md (synthesized: MBO as civilian Auftragstaktik, structural inversion from Taylorism, Deming critique, OKR evolution, cascade problem, agent-native contract implications)
- Concept promoted: insights/concepts/management-by-objectives.md (MBO as incomplete contract for delegated execution, Objective-Intent Paradox, four-layer Intent Architecture mapping)
- Cross-references: linked to [[mission-command]], [[principal-agent-theory]], [[kanban-doctrine]], [[mission-in-business]], [[opord-mission-command-synthesis]], [[progressive-autonomy]], [[centaur-principle]], [[decision-provenance]], [[protocol-as-coordination]]
- Backlinks: updated [[mission-in-business]], [[principal-agent-theory]], [[mission-command]], [[kanban-doctrine]] with cross-references to new concept
- Updated INDEX.md with new concept entry under "Mission and purpose"
- Lint: TBD
- Inventory update: 315 findings, 83 concepts, 313 raw sources

## [2026-05-15] research | Collins/Porras BHAGs and Sinek's Why deep dive (3 raw, 3 findings, 1 concept)
- Raw sources created:
  - research/raw/collins-porras-bhag-mechanics.md (BHAG definition, 5 attributes, examples, Preserve the Core/Stimulate Progress paradox, Rosenzweig/Kahneman criticism, visionary company decline post-1994)
  - research/raw/sinek-golden-circle-deep-dive.md (Golden Circle model, biological claims, diffusion of innovation, criticism, NASA Decadal Survey parallel, Infinite Game extension)
  - research/raw/bhag-sinek-synthesis.md (hierarchy of intent, BHAG-OKR relationship, intent constraint, visionary company BHAG maintenance post-1994, agent-native implications)
- Findings created:
  - research/findings/collins-porras-bhag-mechanics.md
  - research/findings/sinek-golden-circle.md
  - research/findings/bhag-sinek-synthesis.md
- Concept promoted: insights/concepts/intent-architecture.md (Why + BHAG as the upstream intent layer above OKRs/tasks; cascade problem prevention; NASA parallel; agent-native design requirements)
- Cross-references: linked to [[mission-command]], [[mission-in-business]], [[opord-mission-command-synthesis]], [[nasa-mission-model]], [[principal-agent-theory]], [[kanban-doctrine]], [[objectives-and-key-results]], [[management-by-objectives]], [[progressive-autonomy]], [[centaur-principle]]
- Backlinks: updated [[mission-in-business]], [[INDEX.md]] with new concept entry under "Mission and purpose"
- Updated insights/concepts/objectives-and-key-results.md with intent-architecture backlink
- Lint: TBD
- Inventory update: 318 findings, 84 concepts, 316 raw sources

## [2026-05-15] promote | Mission Execution Chain synthesis
- Source: Sub-agent research findings across all five mission domains
- File created: insights/concepts/mission-execution-chain.md (~12KB)
- Content: Cross-domain map of the full chain (Why → Strategic Goal → Mission → Objectives → Projects → Tasks → Execution) with six handoff points where intent is preserved or lost
- Cross-references: links to [[mission-arc]], [[mission-command]], [[management-by-objectives]], [[objectives-and-key-results]], [[intent-architecture]], [[principal-agent-theory]], [[kanban-doctrine]], [[opord-mission-command-synthesis]], [[nasa-mission-model]], [[diplomatic-mission]], [[mission-in-business]], [[progressive-autonomy]], [[workflow-as-contract]], [[centaur-principle]], [[protocol-as-coordination]]
- Updated INDEX.md with new concept entry under "Mission and purpose"
- Inventory: 318 findings, 83 concepts, 312 raw sources

## [2026-05-22] synthesis | karpathy-autoresearch (1 finding)
- Source: research/raw/karpathy-autoresearch.md
- Finding created: research/findings/karpathy-autoresearch.md (133 lines)
- Content: Autonomous LLM pretraining loop by Karpathy — constraint architecture (one file to edit), fixed 5-minute wall-clock budget, NEVER STOP autonomy, git branch as proof-of-work ledger
- Cross-references: [[goal-primitive]], [[kanban-doctrine]], [[proof-of-work]], [[skills-as-portable-knowledge]], [[dark-factory]], [[harness-engineering]], [[management-by-objectives]]
- Lint: clean (0 errors, 15 warnings, 211 info)

## [2026-05-27] synthesis | 0 new files, 349 unchanged, 0 drift. 21 orphan findings noted. Pipeline exited cleanly.

## [2026-06-08] ingest | Loops deep dive: X conversation + lab research (1 raw)
- Source: Matt Van Horn X article on "WTF Is a Loop? Peter Steinberger vs. Boris Cherny"
- Subagent research: X conversation analysis, technical lineage (Ralph loops, /goal, orchestration), top lab papers
- Raw file created: research/raw/loops-x-conversation-june-2026.md (~12KB)
- Content: Five-stage loop lineage (ReAct 2022 → AutoGPT 2023 → Ralph 2025 → /goal 2026 → orchestration now), Boris Cherny definition, Steinberger skill thesis, cost/failure modes, Anthropic framework, arXiv paper references
- Relevant papers catalogued: Yao et al. ReAct (arXiv:2210.03629), Anthropic "Building Effective Agents" (Dec 2024), Robbes et al. Agentic Very Much! (arXiv:2606.07448), Xiao et al. Socratic-SWE (arXiv:2606.07412), Yang et al. How AI Agents Reshape Knowledge Work (arXiv:2606.07489)
- Key repos: gastownhall/gastown, mikeyobrien/ralph-orchestrator, openclawhq
- Lint: TBD
- Inventory update: 314 raw sources, 318 findings, 83 concepts

## [2026-06-09] capture | Cypherpunk Library (cypherpunkbooks.com)
- Raw source created: research/raw/cypherpunk-library.md (~2KB)
- Content: Curated digital library of foundational cypherpunk texts including Hughes manifesto, May's Crypto Anarchist Manifesto, Barlow's Declaration, Finney on eCash, Nash on Ideal Money, Zimmermann on PGP, and links to Anna's Archive / LibGen
- Cross-references: [[cypherpunk-library]], [[open-source-best-practices]], [[protocol-fiction]], [[crypto-as-property-rights]]
- Inventory update: 351 raw sources

## [2026-06-09] synthesis | 1 finding updated, lint: clean
- Ingest: 351 files scanned, 1 new, 0 changed
- New raw: cypherpunk-library.md (cypherpunkbooks.com catalog)
- Finding created: research/findings/cypherpunk-library.md
- Related links updated: insights/concepts/open-source-governance.md, insights/concepts/crypto-as-agent-infrastructure.md
- INDEX.md updated: 320 findings, 351 raw sources
- Lint: PASSED (0 errors, 16 warnings, 211 info)
- Commit: 9d7e762 — feat: cypherpunk-library finding + related link updates
- PR: not opened (main branch, push only)

## [2026-06-10] ingest | Designing loops with Fable 5 (1 raw)
- Source: Lance Martin X article, tweet ID 2064397389189071163
- Raw file created: research/raw/2026-06-10-designing-loops-with-fable-5.md (~10KB)
- Content: Full article text from archived mirror (SOTA Sync) + Claude Managed Agents technical context + synthesis notes
- Key topics: Self-correction loops, Parameter Golf experiment (Fable 5 vs Opus 4.7, 6x improvement), memory as outer loop, Continual Learning Bench 1.0 results
- Cross-references: [[loops-x-conversation-june-2026]], [[goal-primitive]], [[harness-engineering]], [[karpathy-autoresearch]], [[agent-memory]], [[subagent-architecture]], [[centaur-principle]]
- Inventory update: 352 raw sources (pending daily synthesis pipeline)

## [2026-06-10] synthesis | 1 finding updated, lint: clean
- Ingest: 352 files scanned, 1 new, 0 changed
- New raw: 2026-06-10-designing-loops-with-fable-5.md (Lance Martin X article on Fable 5)
- Finding created: research/findings/fable-5-loops-and-memory.md
- Cross-references: goal-primitive, harness-engineering, karpathy-autoresearch, agent-memory, subagent-architecture, centaur-principle, feedback-loop-discipline, per-run-learning, synthesis-over-retrieval
- Lint: PASSED (0 errors, 16 warnings, 211 info)
- Commit: f4af2de — feat: fable-5 finding + index update (1 new raw, 1 finding, lint clean)
- INDEX.md updated: 321 findings, 352 raw sources

## [2026-06-11] no-op | Daily synthesis — no new/changed sources
- Ingest: 352 files scanned, 0 new, 0 changed, 22 orphan findings (known stem-mismatch false positives, incl. fable-5-loops-and-memory vs dated raw filename)
- No synthesis required. Exiting cleanly.

## [2026-06-11] ingest | missions-site deploy debugging findings (card trail provenance)
- Source: Kanban card t_340d7b29 comment trail + missions-site repo commits (8d3ae28, 1cdb213); AAR at missions/missions-site.aar.md in missions repo
- Raw file created: research/raw/2026-06-11-missions-site-deploy-debugging.md (evidence record: failure signature, both root causes, commits, version ids)
- Findings created:
  - research/findings/wrangler-3-vinext-handler-detection-failure.md — wrangler 3 uploads vinext 0.1.1 worker with handlers=[], deploy reports success, placeholder serves; fix is wrangler 4
  - research/findings/run-worker-first-asset-misroute-masking.md — run_worker_first:true misroutes /_next/static/* into SSR worker; rule-array fix needs >=1 positive rule; masking pattern (config change made while system is dead cannot be validated)
- Cross-references: cloudflare-first-agent-factory, deployment-governance, harness-engineering, browser-verification
- INDEX.md updated: 323 findings, 353 raw sources

## [2026-06-12] no-op | Daily synthesis — no new/changed sources
- Ingest: 353 files scanned, 0 new, 0 changed, 24 orphan findings (known stem-mismatch false positives; +2 from 2026-06-11 deploy-debugging findings whose stems differ from the dated raw filename)
- First digest run flagged 2026-06-11-missions-site-deploy-debugging.md as "new" but it was already fully ingested in commit ce76c36; hash state was simply behind. State refreshed, second run confirms clean.
- Lint: PASSED (0 errors, 16 warnings, 211 info)
- No synthesis required. Exiting cleanly.

## [2026-06-13] ingest | The Bayern Maneuver: Legal Theory of Autonomous-System Entities (1 raw)
- Source: Shawn Bayern, 19 Stan. Tech. L. Rev. 93 (2015), full primary PDF retrieved and read; plus Of Bitcoins/Zero-Member LLC (108 Nw. U. L. Rev. 1485), Autonomous Organizations (CUP 2021), LoPucki Algorithmic Entities (95 Wash. U. L. Rev. 887), Bryson et al. legal lacuna (25 AI and Law 273)
- Trigger: ClawBank/$CLAWBANK tweet (June 12, 2026) claiming first implementation of the "Bayern Maneuver" via Manfred LLC
- Raw file created: research/raw/bayern-maneuver-legal-theory.md (~18KB deep dive)
- Key content: zero-member LLC mechanism (RULLCA 701(a)(3)/110(c) waivability argument, NY LLC Law 701(a)(4)), entity cross-ownership fallback, process-agreement equivalence principle, grantable vs regulatory vs denialist personhood models, Scherer/LoPucki/Bryson counter-literature, ClawBank June 2026 context
- Inventory update: 354 raw sources (pending daily synthesis pipeline)
## [2026-06-14] synthesis | Bayern Maneuver finding (1 new raw, sync of pending)
- Raw source: research/raw/bayern-maneuver-legal-theory.md (ingested 2026-06-13, synthesized 2026-06-14)
- Finding created: research/findings/bayern-maneuver-legal-theory.md
  - Title: The Bayern Maneuver: Zero-Member LLCs as Legal Personhood for Autonomous Systems
  - Tags: agents, legal, governance, entity, autonomy, personhood
  - Cross-references: principal-agent-theory, workflow-as-contract, agent-identity, progressive-autonomy, protocol-as-coordination, constitutional-governance
- INDEX.md updated: 324 findings, 354 raw sources
- Lint: PASSED (0 errors, 16 warnings, 211 info)
## [2026-06-15] synthesis | Daily synthesis — 1 finding, lint: clean
- New raw source: myth-of-sisyphus-camus.md (355 raw files total, was ingested 2026-06-14)
- Finding created: research/findings/myth-of-sisyphus-camus.md
- Cross-references: process-without-substance, principal-agent-theory, kaizen, kanban-doctrine, process-philosophy
- Lint: 0 errors, 16 warnings (pre-existing), 211 info (pre-existing forward references in raw/)
- INDEX.md: updated counts (325 findings, 355 raw sources)
## [2026-06-16] no-op | Daily synthesis — no new/changed sources
- Ingest: 355 files scanned, 0 new, 0 changed, 24 orphan findings
- No synthesis required. Exiting cleanly.
## [2026-06-17] synthesis | Andreessen information diet (1 finding, lint: clean)
- New raw source: andreessen-information-diet.md (356 raw files total)
- Finding created: research/findings/andreessen-information-diet.md
- Cross-references: agent-memory, llm-wiki-pattern, intent-architecture, kanban-doctrine, principal-agent-theory, kaizen, agent-native-operations, tools-landscape, context-stack, workflow-as-contract
- Lint: 0 errors, 17 warnings (pre-existing), 211 info (pre-existing forward references in raw/)
- INDEX.md: updated counts (326 findings, 356 raw sources)

## [2026-06-21] no-op | Daily synthesis — no new/changed sources
- Ingest: 356 files scanned, 0 new, 0 changed, 0 SHA drift, HTML excluded: 0
- Lint: not run (no synthesis; lint is the gate for commits, none made)
- Orphan findings: 24 (unchanged from [2026-06-18])
  - Same set as prior no-op: mission/linguistics batch (12), NASA cluster (2), intent/business (4), other (6 including 2 known stem-mismatch false positives)
  - Assessment unchanged: 22 of 24 are genuine orphans needing back-links (connectivity campaign), not synthesis work
- No synthesis required. Exiting cleanly.
## [2026-06-26] ingest | Stanford STORM (NAACL 2024) peer-reviewed paper
- Source: arXiv 2402.14207v2, "Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models" (Shao et al., Stanford OVAL Lab)
- File created: research/raw/storm-naacl-2024.md (~9.5KB raw capture)
- Content: Full methodology (perspective discovery, multi-perspective conversation simulation with retrieval, outline curation), evaluation (FreshWiki dataset, 25% organization improvement, 10% coverage improvement over RAG baseline, 84.8% citation recall, 85.2% precision), known weaknesses (source bias transfer, over-association, no self-critique), system architecture, Python usage
- Trigger: operator directed prioritization of peer-reviewed originals over Nav Toor's viral distillation
- Cross-references: centaur principle, unknown unknowns, multi-perspective research methodology, Co-STORM

## [2026-06-26] ingest | Stanford Co-STORM (EMNLP 2024) peer-reviewed paper
- Source: arXiv 2408.15232v2, "Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations" (Jiang et al., Stanford OVAL Lab)
- File created: research/raw/costorm-emnlp-2024.md (~9.7KB raw capture)
- Content: Full methodology (collaborative human-AI discourse, agent-initiated questioning, dynamic mind map, comprehensive report), WildSeek dataset, human evaluation (70% prefer over search engine, 78% prefer over RAG chatbot), STORM vs Co-STORM comparison, centaur principle connection, Python usage
- Trigger: operator directed prioritization of peer-reviewed originals
- Cross-references: centaur principle, unknown unknowns, STORM paper, human-steered agent discourse
## [2026-06-27] ingest | Batch 20: agent-ops and research systems (7 findings)
- Sources (7 new raw files):
  - clawbank-shodai-ricardian-contract-research.md (renamed from clawbank_shodai_ricardian_contract_research.md — kebab-case fix)
  - costorm-emnlp-2024.md
  - cross-agent-reporting-patterns.md
  - integration-day-onboarding-frame.md
  - session-report-best-practices.md
  - sitrep-origin-and-doctrine.md
  - storm-naacl-2024.md
- Findings created (7):
  - ricardian-contract-agent-economy.md — ClawBank/Shodai first AI-agent-signed Ricardian contract
  - storm-naacl-2024.md — STORM multi-perspective question asking with retrieval
  - costorm-emnlp-2024.md — Co-STORM collaborative human-AI knowledge curation for unknown unknowns
  - cross-agent-reporting-patterns.md — Blackboard architecture for Hermes fleet coordination
  - integration-day-onboarding-frame.md — Concierge agent onboarding as systems integration
  - session-report-best-practices.md — Cross-domain synthesis for agent SITREPs
  - sitrep-origin-and-doctrine.md — SITREP military origins and canonical structure
- Lint: 0 ERRORs (linted on branch before commit), 23 WARNINGs (all pre-existing/exempt), 211 INFOs
- Raw file renamed: clawbank_shodai_ricardian_contract_research.md -> clawbank-shodai-ricardian-contract-research.md (kebab-case, via _lint.py --fix)
- Cross-references: crypto-as-agent-infrastructure, synthesis-over-retrieval, llm-wiki-pattern, centaur-principle, multi-agent-coordination-patterns, dark-factory, harness-engineering, chief-engineer-system, mission-command, kanban-doctrine, agent-native-operations, kaizen
- Orphan findings: 24 (unchanged from prior session; no new orphans introduced)

## [2026-06-27] synthesis | 7 findings updated, lint: clean
## [2026-06-29] ingest | Batch 21: IRL research cluster and May 2026 research dump (18 findings)
- Sources (22 new raw files):
  - IRL cluster (13): 2026-06-28-aima-irl-chapter.md, 2026-06-28-irl-landscape-2000-2010.md, 2026-06-28-ng-russell-2000-irl-summary.md, 2026-06-28-russell-human-compatible-storm-research.md, 2026-06-28-ziebart-maxent-irl-alignment-machine-conscience.md, 2026-06-29-active-interactive-irl.md, 2026-06-29-irl-theoretical-foundations.md, 2026-06-29-post-2018-irl-landscape.md, irl-mathematical-formalism.md, irl-moral-psychology-connection.md, ziebart-alignment-agent.md, ziebart-landscape-agent.md, ziebart-paper-agent.md
  - May 2026 research dump (9): agent-filesystems-infrastructure.md, agent-harness-architecture.md, ai-ethics-philosophy.md, anthropic-openclaw-ecosystem.md, fleet-of-agents-and-ibm-multi-agent-collaboration.md, great-instructors-report.md, protocols-coordination.md, research-dump-master-index-2026-05-20.md, youtube-videos.md
- Findings created (18):
  - IRL cluster (11): ng-russell-2000-irl-foundations, irl-landscape-2000-2010, irl-mathematical-formalism, ziebart-maxent-irl-alignment-conscience, russell-human-compatible-storm, irl-moral-psychology-connection, active-interactive-irl, irl-theoretical-foundations, post-2018-irl-landscape, aima-irl-chapter, ziebart-maxent-alignment-landscape-deep-dive
  - Research dump (7): agent-filesystems-infrastructure, agent-harness-architecture, ai-ethics-philosophy-dump, anthropic-openclaw-ecosystem-policy, fleet-of-agents-and-ibm-multi-agent-collaboration, great-instructors-report, protocols-coordination-institutional-design, research-dump-master-index, youtube-videos-research-dump
- Cross-references: IRL cluster cross-linked to conscience, principal-agent-theory, intent-architecture. Research dump cross-linked to agent-native-operations, multi-agent-coordination-patterns, kanban-doctrine, dark-factory, karpathy-autoresearch, goal-primitive, the-openclaw-lesson, centaur-principle
- Lint: PASSED (0 errors, 31 warnings pre-existing, 215 info)
- INDEX.md updated: 344 findings, 83 concepts, 385 raw sources
## [2026-06-30] ingest | Loops as orchestration primitive (1 finding)
- Source: 1 raw file — loops-x-conversation-june-2026.md (Steinberger/Cherny X conversation on loops: ReAct, AutoGPT, Ralph, /goal, continuous orchestration, Gas Town, cost inversion, hard stops, skills-not-prompts)
- Finding created (1):
  - loops-as-orchestration-primitive.md — Five-stage lineage from ReAct (2022) to continuous multi-agent orchestration (2026), three hard stops (iteration cap, no-progress detection, budget ceiling), cost inversion from tokens to loop management, skills as the durable unit inside the loop
- Cross-references: goal-primitive, goal-primitive-three-implementations, agent-orchestrator-pattern, agentic-architecture, harness-engineering, skills-as-portable-knowledge, automation-leverage, karpathy-autoresearch, progressive-autonomy, feedback-loop-discipline, myth-of-sisyphus-camus
- Previously ungested raw audit: 3 genuinely ungested files found. loops-x-conversation-june-2026.md synthesized (this batch). ziebart-alignment-agent.md and ziebart-landscape-agent.md confirmed as subagent outputs already consolidated into ziebart-maxent-alignment-landscape-deep-dive.md (composite finding cites ziebart-paper-agent.md as primary source but explicitly consolidates all three subagent docs)
- Coverage: 374/385 raw sources now have findings (97.1%), with the remaining 11 being composite-source raw files (NASA program docs, goal-command raw files, Ziebart subagent outputs) whose content is fully captured in existing findings
- Batch 21 unpushed commit: pushed to origin/main (ef8dd7d)
- INDEX.md updated: 378 findings, 91 concepts, 2 entities, 385 raw sources. Also corrected stale counts from prior session (344/83 -> 378/91)
- Lint: PASSED (0 errors, 31 warnings all pre-existing, 215 info)
## [2026-07-01] ingest | Isenberg AI-native organization thesis: the company as context layer
- Source: Greg Isenberg, X tweet, June 27, 2026 (3,490 likes, 376 RTs)
- Raw file: research/raw/isenberg-ai-native-orgs-context-layer.md (46KB, already committed)
- Finding created: research/findings/isenberg-ai-native-orgs-context-layer.md (~10KB)
- Content: Context-layer paradigm (Engelbart Collective IQ lineage), legibility as moat (James C. Scott inversion), Trust Economy (Zhao/Tang), SOPs as code not documentation, automation goldmine targeting, humans to strategy/taste/judgment (Autor, Brynjolfsson Turing Trap, Kasparov centaur chess), Klarna real architecture case study
- Cross-references: [[agent-native-operations]], [[centaur-principle]], [[automation-leverage]], [[institutional-ai-redesign]], [[harness-engineering]], [[synthesis-over-retrieval]], [[workflow-as-contract]], [[progressive-autonomy]], [[proof-of-work]], [[llm-wiki-pattern]], [[agent-memory]], [[principal-agent-theory]], [[context-stack]]
- Lint: 0 errors, 32 warnings (all raw fm-missing exemptions), 215 info. PASSED.
- INDEX updated: findings count 378 to 379, raw sources 385 to 386
## [2026-07-02] no-op | Daily synthesis — no new/changed sources
- Ingest: 386 files scanned, 0 new, 0 changed, 0 SHA drift, HTML excluded: 0
- Lint: PASSED (0 errors, 32 warnings all pre-existing raw fm-missing/fm-title-missing exemptions, 215 info)
- Orphan findings (_ingest.py stem-match): 40 (up from 24 on 2026-06-25)
  - Delta: +16 from recent batches whose findings have non-matching raw stems
    - IRL cluster (11): findings named e.g. `ng-russell-2000-irl-foundations` vs raw `2026-06-28-ng-russell-2000-irl-summary`; `irl-landscape-2000-2010`, `ziebart-maxent-irl-alignment-conscience`, `russell-human-compatible-storm`, `irl-moral-psychology-connection`, `active-interactive-irl`, `irl-theoretical-foundations`, `post-2018-irl-landscape`, `aima-irl-chapter`, `ziebart-maxent-alignment-landscape-deep-dive`
    - Research dump (7): `anthropic-openclaw-ecosystem-policy`, `fleet-of-agents-and-ibm-multi-agent-collaboration`, `ai-ethics-philosophy-dump`, `protocols-coordination-institutional-design`, `research-dump-master-index`, `youtube-videos-research-dump`, `great-instructors-report`
    - Other (3): `loops-as-orchestration-primitive` (raw: loops-x-conversation-june-2026), `ricardian-contract-agent-economy` (raw: clawbank-shodai-ricardian-contract-research), `isenberg-ai-native-orgs-context-layer` (raw source exists but stem differs — actually matches, see below)
  - Note: 38 of 40 are stem-mismatch false positives (finding `source:` frontmatter resolves to a differently-named raw file). `_lint.py` confirms only 2 genuine orphans: `nasa-mission-model`, `nasa-lifecycle-gates-and-decadal-survey` (known since 2026-06-18, raw sources are composite NASA program docs consolidated into existing findings)
  - Assessment: no connectivity-sense orphans introduced. The increase is mechanical (date-prefixed raw filenames). A connectivity campaign remains recommended for the 2 genuine NASA orphans but is not blocking.
- No synthesis required. Exiting cleanly.## [2026-06-30] ingest | Loops as orchestration primitive (1 finding)
- Source: 1 raw file — loops-x-conversation-june-2026.md (Steinberger/Cherny X conversation on loops: ReAct, AutoGPT, Ralph, /goal, continuous orchestration, Gas Town, cost inversion, hard stops, skills-not-prompts)
- Finding created (1):
  - loops-as-orchestration-primitive.md — Five-stage lineage from ReAct (2022) to continuous multi-agent orchestration (2026), three hard stops (iteration cap, no-progress detection, budget ceiling), cost inversion from tokens to loop management, skills as the durable unit inside the loop
- Cross-references: goal-primitive, goal-primitive-three-implementations, agent-orchestrator-pattern, agentic-architecture, harness-engineering, skills-as-portable-knowledge, automation-leverage, karpathy-autoresearch, progressive-autonomy, feedback-loop-discipline, myth-of-sisyphus-camus
- Previously ungested raw audit: 3 genuinely ungested files found. loops-x-conversation-june-2026.md synthesized (this batch). ziebart-alignment-agent.md and ziebart-landscape-agent.md confirmed as subagent outputs already consolidated into ziebart-maxent-alignment-landscape-deep-dive.md (composite finding cites ziebart-paper-agent.md as primary source but explicitly consolidates all three subagent docs)
- Coverage: 374/385 raw sources now have findings (97.1%), with the remaining 11 being composite-source raw files (NASA program docs, goal-command raw files, Ziebart subagent outputs) whose content is fully captured in existing findings
- Batch 21 unpushed commit: pushed to origin/main (ef8dd7d)
- INDEX.md updated: 378 findings, 91 concepts, 2 entities, 385 raw sources. Also corrected stale counts from prior session (344/83 -> 378/91)
- Lint: PASSED (0 errors, 31 warnings all pre-existing, 215 info)
## [2026-07-03] no-op | Daily synthesis — no new/changed sources
- Ingest: 386 files scanned, 0 new, 0 changed, 0 SHA drift, HTML excluded: 0
- Lint: not run (no synthesis; lint is the gate for commits, none made)
- Orphan findings: 40 (unchanged from 2026-07-02)
  - 38 stem-mismatch false positives (IRL cluster, research dump, loops, ricardian, isenberg)
  - 2 genuine (NASA cluster, known since 2026-06-18)
- No synthesis required. Exiting cleanly.
## [2026-07-07] ingest | continual-learning-for-agents-replit
- Source: Replit AI team article (Michele Catasta @pirroh), X article posted July 6, 2026 + expanded Replit blog post June 23-24, 2026
- File created: research/findings/continual-learning-for-agents-replit.md
- Content: Replit's continual learning model for agent systems. Core thesis: continual learning is the universal recipe for hill climbing with agents even when you do not own the model weights. The harness learns too. Three-layer measurement system (ViBench offline benchmark, A/B and production traces online, optimization loop). Telescope trace clustering (Clio-inspired, density-based clustering). Self-improvement loop where agents propose PRs from production telemetry, engineers gate launch. Four human gates: hypothesis selection, implementation architecture, eval curation, launch approval. Moat: proprietary corpus of real app failures.
- Cross-references: [[reference-free-evaluation]], [[harness-engineering]], [[feedback-loop-discipline]], [[per-run-learning]], [[proof-of-work]], [[agent-native-operations]]
- Trigger: new raw file detected by ingest digest cron (1 new, 0 changed, 386 unchanged)
- Lint: 0 errors on new finding; raw fm-missing warning is expected (raw files exempt per SCHEMA lint rule 5)
## [2026-07-08] no-op | Daily synthesis — no new/changed sources
- Ingest: 387 files scanned, 0 new, 0 changed, 0 SHA drift, HTML excluded: 0
- Lint: not run (no synthesis; lint is the gate for commits, none made)
- Orphan findings: 40 (unchanged from 2026-07-03)
  - 38 stem-mismatch false positives (IRL cluster, research dump, loops, ricardian, isenberg, NASA linguistics batch)
  - 2 genuine (NASA cluster: nasa-mission-model, nasa-lifecycle-gates-and-decadal-survey, known since 2026-06-18, raw sources composite)
- No synthesis required. Exiting cleanly.