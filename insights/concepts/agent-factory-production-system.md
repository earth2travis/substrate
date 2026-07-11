---
title: "Agent Factory Production System"
related:
- alternative-organizational-structures
- alternative-organizational-structures-insights
- institutional-ai-vs-individual-ai
---

---
title: "Agent Factory Production System"
tags: [concept, agent-factory, lean, production-system, afps, toyota]
related:
- toyota-production-system
- lean-doctrine
- dark-factory
- production-paradigms
- heijunka
- kaizen
- skills-as-portable-knowledge
- centaur-principle
- institutional-ai-redesign
- multi-agent-coordination-patterns
source: research/findings/synthesis-agent-factory.md
---

# Agent Factory Production System

## Definition

The Agent Factory Production System (AFPS) is a production framework modeled on the Toyota Production System, adapted for autonomous agent operations. It treats the factory as the product and agents as outputs. The core thesis: build the system that builds agents, then make the system better every day.

## The Two Pillars

**Just-in-Time Agent Production:** Build agents when needed, with the skills they need, deployed where they are needed. No speculative agent creation. No bloated general-purpose agents. Purpose-built, composed from modular skills.

**Jidoka (Autonomy with Oversight):** Agents operate autonomously but detect their own problems and escalate. No silent failures. No unchecked drift. The system stops and signals when something is wrong.

## The Seven Wastes, Translated

| Toyota Waste | Agent Factory Equivalent |
|---|---|
| Overproduction | Building agents nobody asked for |
| Waiting | Agents blocked on missing skills, credentials, or approvals |
| Transport | Unnecessary data movement between systems |
| Overprocessing | Agents doing work that does not change the output |
| Inventory | Accumulated unread research, unprocessed memory, stale context |
| Motion | Context switching, redundant tool calls, re-reading already loaded files |
| Defects | Wrong outputs, hallucinations, process violations, missed issues |

## The Six Phases

Mapped from Toyota's 40-year factory planning arc:

1. **Strategic decision:** Select runtime, knowledge stores, and coordination layers that can scale without rebuild
2. **Factory design:** Four shops: Skill Forging, Agent Assembly, Persona and Voice, Deployment and Integration
3. **Construction:** Scope expansion is the norm. Get one production line (one agent type) running end-to-end before adding others
4. **Trial production:** Pilot team builds agents by hand, documents processes, mocks up workflows before implementation
5. **Start of production:** Kill switches, dashboards, pull-based demand queues, and continuous improvement loops activated
6. **Continuous evolution:** Agents run their own lesson extractors, optimize skills, identify gaps, and monitor health

## Key Practices

- **Skill Library as Parts Inventory:** modular, tested, version-controlled skills that any agent can load just-in-time
- **SOUL.md as Quality Standard:** explicit values, voice, and boundaries that prevent behavioral defects
- **Standardized Agent Assembly:** repeatable process from requirements to deployed agent using templates and checklists
- **Pull-Based Task Assignment:** agents pull work from queues rather than being pushed tasks
- **Kaizen Loop:** lesson extraction → skill optimization → process updates → better agents, running continuously

## The Fourth Era

Manufacturing history progressed through Craft → Mass → Lean → Industry 4.0. Agent production is replaying this arc in compressed time. AFPS aims to be a fourth-era system: lean's quality and flexibility, mass's scale, craft's care, with culture encoded into infrastructure (SOUL.md, AGENTS.md, CONTRACT.md) rather than dependent on sustained human commitment.

## External Validation

Chamath Palihapitiya's 8090 Labs ($135M Series A) independently validates AFPS with the "five tests of a real software factory": business intent input, finished goods with guaranteed quality, end-to-end accountability, coherence under continuous change, and independence from individuals. 8090 reverse-engineered 18M lines of COBOL/Assembly into ~300k plain-English rules in 40 days using this approach. The "who takes the call" accountability test maps directly to AFPS's Jidoka pillar and Context Stack infrastructure. See [[chamath-software-factory-thesis]] for the full mapping.

## Related

- [[toyota-production-system]] -- Historical origin of the production system
- [[lean-doctrine]] -- JIT, Jidoka, and waste elimination
- [[dark-factory]] -- Autonomous production endpoint
- [[production-paradigms]] -- The four eras of manufacturing
- [[heijunka]] -- Production leveling for agent orchestration
- [[kaizen]] -- Continuous improvement culture
- [[skills-as-portable-knowledge]] -- Modular capability system
- [[chamath-software-factory-thesis]] -- External commercial validation of the factory thesis

- [[factory-ai-droid-session]]
- [[openclaw-vs-hermes-coding]]
- [[paperclip-patterns-worth-adopting-for-synthweave]]
- [[ai-sdk-research]]
- [[production-systems-compared]]
- [[price-minus-for-the-agent-factory]]
- [[synthweave-mcp-analysis]]
- [[harness-engineering]]
- [[openai-frontier-and-harness-engineering]]
- [[multi-agent-coordination]]
- [[agentic-maximization]]

- [[accounting-bookkeeping-research]]
- [[price-minus-vs-cost-plus]]
- [[deployment-guide]]
- [[gateway-integration]]
- [[paperclip-is-an-os-for-autonomous-agent-companies]]
- [[paperclip-atomic-task-checkout-prevents-agent-collisions]]

- [[production-systems-for-agent-factories]]
- [[synthesis-agent-factory]]

- [[adapter-system]]
- [[tool-provisioning-contract]]
