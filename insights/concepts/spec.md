---
title: The Context Stack
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/spec.md
---

# The Context Stack

_A universal specification for representing individuals and organizations as machine-readable context._

_Version 0.1 | March 2026_

---

## The Problem

Every AI agent starts blind. It has no idea who it's working for, what they care about, where they're headed, how they operate, or what they know. The current solution is ad hoc: a system prompt here, a README there, tribal knowledge nowhere.

The result is agents that are technically capable but contextually stupid. They produce correct outputs that are strategically wrong, tonally off, or organizationally ignorant. The human spends more time correcting context than doing work.

The Context Stack is a structured set of markdown files that gives any agent complete context about an entity, whether that entity is a person, a team, a company, or another agent. Read the stack, understand the entity. Act on its behalf without constant correction.

---

## Design Principles

**Markdown only.** No proprietary formats, no databases, no APIs required. Any agent, any framework, any editor can read these files. Portability is non-negotiable.

**Human-writable, machine-readable.** Every file should make sense to a person reading it in a text editor. Agents parse the same content. No separate human and machine versions.

**Layered, not monolithic.** Context is organized into four layers. An agent doing a quick task reads one or two files. An agent making strategic decisions reads the full stack. The layers enable selective loading based on what the task requires.

**Opinionated structure, flexible content.** The file names and layer organization are fixed. What goes inside each file is up to the entity. A startup's VISION.md looks nothing like an individual's. Same structure, different substance.

**Living documents.** These files change. Some change daily (DECISIONS.md), some change yearly (SOUL.md), some grow continuously (knowledge/). The stack is not a snapshot. It is the entity's evolving self-representation.

---

## The Four Layers

### Identity (who)

The most stable layer. Changes slowly, sometimes over years. This is the foundation everything else builds on. An agent that understands identity can make judgment calls even without explicit direction.

### Direction (where)

The strategic layer. Changes quarterly or when priorities shift. Tells an agent what the entity is trying to accomplish right now, why, and through what specific efforts. Without direction, an agent optimizes for nothing.

### Operations (how)

The execution layer. Changes frequently as processes evolve, decisions accumulate, and roles shift. Tells an agent how work gets done, who does what, what's already been decided, and what constraints are absolute.

### Intelligence (what)

The knowledge layer. Grows continuously, rarely shrinks. Four directories representing different states of knowing: established knowledge, active research, applied capability, and relational understanding.

---

## File Specifications

### Identity Layer

#### SOUL.md

The innermost file. Who the entity is at its core. For a person: personality, voice, values in practice, what they care about and why, how they think. For an organization: culture, founding story, the thing that makes them them. For an agent: its designed identity and behavioral compass.

This is the hardest file to write and the most important to get right. Everything downstream inherits from it. An agent that reads only SOUL.md should be able to approximate the entity's judgment on novel questions.

**Changes:** Rarely. When it does change, it matters.

**Example signals:**
- "We value speed over polish in early stages"
- "I think in systems, not features"
- "Honesty costs comfort. I will not tell you what you want to hear."

#### VISION.md

What the entity believes the world should look like. Not a mission statement written for investors. The actual belief about what's broken, what could be better, and what the entity exists to change.

For an individual, this might be a personal philosophy of work or life. For a company, it's the future they're building toward. For an agent, it's the purpose it serves beyond individual tasks.

**Changes:** Rarely. Evolves as understanding deepens.

#### VALUES.md

What the entity optimizes for when things conflict. Values are only meaningful under tension. "We value quality" means nothing until quality conflicts with speed, and this file says which wins.

Distinct from SOUL.md: the soul is holistic identity, values are the explicit priority stack used for tradeoff decisions. An organization might have soul-level culture that's hard to articulate, but values that are concrete and rankable.

**Changes:** Slowly. Usually after a hard lesson about what actually matters.

**Example signals:**
- "Transparency over comfort, always"
- "Ship over perfect, except for security"
- "User privacy beats feature velocity"

#### EXPERIENCE.md

What the entity has done. Track record, credentials, past work, domain expertise earned through practice. This is the file that gives weight to everything else. An agent reading SOUL.md knows what you believe. An agent reading EXPERIENCE.md knows why anyone should listen.

For an individual: career history, projects shipped, domains mastered, failures learned from. For an organization: products launched, markets entered, customers served, pivots survived. For an agent: tasks completed, accuracy records, domains it has operated in.

**Changes:** Grows over time. Append-heavy.

#### TASTE.md

The file that can't be taught. Adjacent to VALUES.md but distinct: values are principles you can rank, taste is instinct you can only recognize. What makes someone choose this font over that one, this word over that one, this partner over that one, before they can explain why.

For an individual: aesthetic preferences, design sensibilities, what they're drawn to and repelled by, the ineffable quality that makes their choices theirs. For an organization: what "good" looks like to them, the pattern that separates a yes from a no when the spreadsheet says both are equal. For an agent: the stylistic and qualitative preferences it should internalize, the difference between technically correct and actually right.

Taste operates below the threshold of explanation. It is the hardest file to write because it requires articulating what you normally just feel. But once written, it is the file that prevents an agent's output from being generic. An agent without access to TASTE.md produces correct work. An agent with it produces work that feels like yours.

**Changes:** Slowly. Taste evolves through exposure, not decision.

---

### Direction Layer

#### OBJECTIVES.md

What the entity is trying to achieve right now. Concrete, measurable where possible, time-bound. These are the current targets, not the eternal mission.

The difference between VISION.md and OBJECTIVES.md: vision is the destination on the horizon, objectives are the mile markers for this quarter. An agent choosing between two tasks checks OBJECTIVES.md to decide which moves the needle.

**Changes:** Quarterly or when priorities shift.

**Example signals:**
- "Ship the beta by April 15"
- "Reduce open issues to under 20"
- "Close the seed round"

#### MISSIONS.md

The specific campaigns underway to hit objectives. If objectives are the targets, missions are the operations launched to reach them. Each mission has a scope, a team or agent responsible, a timeline, and success criteria.

Missions can run in parallel. They can be abandoned or completed. They are the active work streams, not the aspirations.

**Changes:** Weekly or as work streams start and finish.

#### INTENT.md

The why behind current direction. This is the file most organizations are missing entirely, which is why new hires and new agents make moves that are technically correct but strategically wrong.

Intent explains the reasoning behind objectives and missions. Why this priority order? Why this approach instead of the obvious alternative? What context shaped these decisions? An agent that reads INTENT.md can extrapolate to novel situations because it understands the logic, not just the instructions.

**Changes:** When direction changes. Updated alongside OBJECTIVES.md.

**Example signals:**
- "We're prioritizing developer experience over features because retention is the bottleneck"
- "The partnership with X matters more than the revenue it generates because it validates our approach in the market"
- "I'm saying no to consulting work this quarter to protect deep work time on the core product"

#### TODO.md

The working surface. What's next, right now, today. If OBJECTIVES.md is the quarterly horizon and MISSIONS.md is the active campaigns, TODO.md is the immediate queue: the short list that an agent checks to decide what to do next.

This is one of Factory AI's four compaction anchors: the to-do list must survive every context compression unchanged. It is the single most important orientation file for an agent mid-session. Without it, the agent loses its place.

TODO.md is not a backlog. It is not a project tracker. It is the curated, prioritized, current list of work. Items move on and off quickly. Stale items are a signal that the list needs maintenance.

**Changes:** Daily. The most frequently updated file in the Direction layer.

---

### Operations Layer

#### AGENTS.md

How work gets done. Processes, conventions, operating model, tooling, communication patterns. For a human entity, this is their personal productivity system. For an organization, it's the operating manual. For an agent, it's the behavioral contract.

This file answers: "I know what you want to achieve. How do you want me to achieve it?"

**Changes:** Frequently. Processes evolve through practice.

#### ROLES.md

Who does what. Human and agent responsibilities, authority boundaries, escalation paths. In a team with multiple agents, ROLES.md prevents duplication and dropped balls.

Each role entry: who (person or agent), what they own, what they can decide autonomously, what requires approval, and who they report to or coordinate with.

**Changes:** When team composition or responsibilities shift.

#### DECISIONS.md

The decision log. What was decided, when, by whom, why, and what alternatives were rejected. This is institutional memory in its most actionable form.

An agent about to make a decision checks DECISIONS.md first. If a similar question was already resolved, it follows precedent or explicitly notes why it's deviating. This prevents the organization from relitigating settled questions.

**Changes:** Continuously. Every significant decision gets logged.

#### DESIGN.md

How things look, feel, and behave. The visual and interaction contract. For software entities, this is the design system: colors, typography, spacing, component patterns. For non-software entities, this might be brand guidelines, communication style, or aesthetic preferences.

Any agent generating user-facing output reads DESIGN.md to ensure consistency. This is the file that prevents every screen, document, or communication from looking like it came from a different entity.

**Changes:** Moderate. Evolves as the design language matures.

#### CONTRACT.md

The enforcement layer. Every other file is descriptive or directional. CONTRACT.md is the one with teeth.

Non-negotiable constraints. What an agent must never do. What requires human approval. SLAs with external parties. Legal boundaries. API rate limits. Spending caps. Privacy rules. Compliance requirements.

Values are weighted. Contracts are binary. You either comply or you breach. An agent can read VALUES.md and make a reasonable tradeoff. An agent that violates CONTRACT.md has failed, full stop.

This file bridges internal context and external commitments. SOUL.md is who you are to yourself. CONTRACT.md is who you are to others, enforceable.

**Changes:** When agreements change, regulations shift, or hard boundaries are discovered through incident.

---

### Intelligence Layer

#### skills/

What the entity can do. Each skill is a directory containing a SKILL.md (instructions) and optional scripts, templates, or supporting files. Skills are executable knowledge: an agent reads the skill and gains a new capability.

Skills are portable. They can be shared between entities, installed from external sources, and versioned independently. They are the composable unit of capability.

#### research/

What the entity is actively learning. Ongoing investigations, experiments, literature reviews, competitive analysis. Research is intelligence in motion, not yet settled.

Research may graduate to knowledge/ when validated, inform updates to other files (a research finding might change OBJECTIVES.md), or be abandoned when the question becomes irrelevant.

#### knowledge/

What the entity knows to be true. Established facts, validated findings, reference material, domain expertise. This is the settled body of intelligence that skills and decisions draw from.

The difference between research/ and knowledge/ is confidence. Research is "we think." Knowledge is "we know." The bar for moving something from research to knowledge should be high.

#### relationships/

Who matters to the entity and why. Not a contact list. A map of the relationships that shape decisions, open doors, require care, or carry history. Each relationship gets its own file within the directory: `relationships/boilerhaus.md`, `relationships/investors.md`, `relationships/community.md`. The depth of the file matches the depth of the relationship.

For an individual: collaborators, mentors, communities, the people whose opinions carry weight. For an organization: partners, investors, customers, competitors, community. For an agent: the humans it serves, peer agents it coordinates with, external services it depends on.

Each relationship file should include: who they are, the nature of the relationship, its current state, and what matters to them. An agent drafting communication to someone described here should know whether to be formal or casual, direct or careful, warm or professional.

Relationships are not identity. They are intelligence you've gathered about the world outside yourself. You learned these people. You studied these dynamics. You maintain this understanding. That's knowledge, not self.

**Changes:** Moderate. New relationships form, old ones evolve. Individual files updated as dynamics shift.

---

## Context Loading

Not every task needs the full stack. Loading all nineteen items for a simple formatting request wastes tokens and attention. The stack is designed for selective loading based on task requirements.

### Loading Tiers

**Tier 0: Identity only.** SOUL.md. Enough for basic judgment calls, tone, and voice. Load this always.

**Tier 1: Identity + Direction.** Add OBJECTIVES.md and INTENT.md. Enough for prioritization decisions and strategic work.

**Tier 2: Full context.** All four layers. For complex decisions, cross-functional work, or onboarding a new agent.

**Tier 3: Targeted depth.** Full stack headers plus deep loading of specific files relevant to the task. A design task loads DESIGN.md fully but only headers from DECISIONS.md.

### Semantic Routing

The speculation that matters: an intelligent context loader that reads the incoming prompt and determines which files (and which sections within files) are relevant.

A prompt about "draft an email to the BoilerHAUS team" triggers:
- SOUL.md (voice and tone)
- relationships/ (BoilerHAUS entry specifically)
- INTENT.md (why we're engaging with them)
- CONTRACT.md (any communication constraints)

A prompt about "should we build feature X" triggers:
- VISION.md (does it align?)
- OBJECTIVES.md (does it advance current goals?)
- VALUES.md (does it conflict with priorities?)
- DECISIONS.md (have we decided this before?)
- INTENT.md (why are we even asking?)
- research/ (what do we know about this space?)

A prompt about "write the deployment script" triggers:
- AGENTS.md (how we do things)
- DESIGN.md (if it's user-facing)
- CONTRACT.md (any deployment constraints)
- skills/ (relevant deployment skills)

The loader doesn't need to be perfect. It needs to be better than "load everything" and better than "load nothing." Even a rough relevance score per file dramatically reduces noise.

### Progressive Disclosure

Files themselves can be structured for progressive loading. The first paragraph of each file is the abstract: enough context to decide whether to read deeper. Headers provide scannable structure. An agent can read the outline of DECISIONS.md and only load the full entry for relevant decisions.

This means every file benefits from a consistent internal structure:
1. **First line:** One-sentence description of what this file contains.
2. **Summary section:** The essential context in under 200 words.
3. **Full content:** Everything else.

An agent at Tier 1 reads the summaries. An agent at Tier 2 reads the full content. The information architecture supports both without requiring separate files.

---

## What Becomes Possible

### For Individuals

A person with a complete Context Stack has a persistent digital identity that any agent can read. Switch from Claude to GPT to Gemini to a local model: same context, same continuity. Your AI assistant understands you on day one because you hand it the stack, not because it learned you over months of conversation.

Career transitions carry forward. Everything you know, everyone you've worked with, every decision you've made and why, all portable. The stack is your professional memory, externalized.

### For Organizations

Onboarding drops from weeks to hours. A new employee or agent reads the stack and understands: who we are, where we're going, how we work, what we know, what we must never do. The tacit knowledge problem that kills organizations as they scale becomes a solved problem, if the stack is maintained.

Multiple agents operating on behalf of the same organization produce coherent output because they're reading the same context. No more "this email sounds nothing like us" or "this agent doesn't know we already decided that."

### For Agent Teams

A team of specialized agents with shared access to the stack can coordinate without a central orchestrator. Each agent reads ROLES.md to know its responsibilities, OBJECTIVES.md to prioritize, DECISIONS.md to avoid contradictions, and CONTRACT.md to know the walls.

The stack becomes the shared state that replaces constant human mediation. Agents don't need to ask "should I do this?" if the answer is derivable from the stack.

### For Agent-to-Agent Communication

When two entities interact, they can exchange stacks (or curated subsets). An agent representing Entity A reads Entity B's SOUL.md, VALUES.md, and relationships/ before drafting a proposal. It understands not just what to propose but how to frame it, what matters to the other party, and what to avoid.

Negotiation, collaboration, and partnership become more efficient because both sides have legible context. The handshake is not "let me tell you about us" but "read our stack."

### For Context-Aware Routing

The endgame: a routing layer that sits between the prompt and the stack, selecting the optimal slice of context for each interaction. Not a fixed boot sequence that loads the same files every time, but a dynamic system that understands the task and assembles the relevant context.

This routing layer learns over time. It observes which context files were loaded for tasks that succeeded versus tasks that required correction. It discovers that email drafting rarely needs DESIGN.md but always needs relationships/. It learns that technical decisions need DECISIONS.md but creative exploration doesn't.

The human or agent never thinks about context loading. They state their intent, and the router assembles the right context. The stack is the library. The router is the librarian.

---

## Adoption Path

### Starting Point

You don't need all nineteen items on day one. Start with three:

1. **SOUL.md**: Who you are.
2. **OBJECTIVES.md**: What you're doing.
3. **AGENTS.md**: How you work.

That's enough to make any agent meaningfully more effective. Add files as the gaps become apparent. "This agent doesn't know our constraints" → write CONTRACT.md. "This agent keeps relitigating settled decisions" → start DECISIONS.md.

### Maintenance

The stack is only valuable if it's current. Stale context is worse than no context because it creates false confidence. Each file should have an implicit or explicit freshness expectation:

- **Daily:** TODO.md, DECISIONS.md, research/
- **Weekly:** OBJECTIVES.md, MISSIONS.md, knowledge/
- **Monthly:** ROLES.md, AGENTS.md, relationships/, skills/
- **Quarterly:** VALUES.md, INTENT.md, CONTRACT.md, DESIGN.md
- **Yearly:** SOUL.md, VISION.md, TASTE.md, EXPERIENCE.md

Agents themselves can flag staleness: "OBJECTIVES.md was last updated 47 days ago. Still accurate?"

---

## Relationship to Existing Patterns

The Context Stack does not invent new ideas. It names and organizes patterns that are already converging independently:

- **claude.md / AGENTS.md**: Anthropic's recommended project configuration
- **design.md**: Google Stitch's portable design system
- **SOUL.md**: Emerging pattern for agent identity (OpenClaw, Synthweave)
- **ADRs (Architecture Decision Records)**: DECISIONS.md is the generalization
- **OKRs**: OBJECTIVES.md is the context-aware version
- **Skills-as-markdown**: Cloudflare vinext, OpenClaw, BoilerHAUS
- **README.md**: The original context file. The stack is README.md, evolved.

The insight is not any individual file. It is the complete set, organized into layers, with a loading strategy that makes selective access practical.

---

_The Context Stack is an open specification. Use it, modify it, extend it. The only requirement is that it remains markdown, human-writable, and machine-readable._
