---
title: Context Stack Observations
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/observations.md
---

# Context Stack Observations

_Living log of insights, questions, and test results as we develop the spec._

---

## 2026-03-26: The Brainstorm (founding conversation)

### Ξ2T's original stack proposal
```
SOUL.md, VISION.md, VALUES.md, EXPERIENCE.md, DESIGN.md,
AGENTS.md, OBJECTIVES.md, MISSIONS.md, DECISIONS.md,
INTENT.md, ROLES.md, skills/, research/, knowledge/
```

### Key moves during the conversation

**RELATIONSHIPS.md added (Sivart's suggestion):** The missing link between identity and action. You can know who someone is, what they want, and how they work, but without knowing who they care about and why, you make tone-deaf moves. An agent drafting an email to a close collaborator vs. a cold investor vs. a competitor writes three completely different messages. That context lived nowhere.

**CONTRACT.md added (Ξ2T's suggestion):** The enforcement layer. Every other file is descriptive or directional. CONTRACT.md has teeth. Values are weighted. Contracts are binary. You comply or you breach. Bridges internal context and external commitments. SOUL.md is who you are to yourself. CONTRACT.md is who you are to others, enforceable.

**Layer naming evolution:**
- Started with four unnamed groupings
- Sivart proposed: Identity (who), Direction (where), Operations (how), Knowledge (what)
- Problem: "Knowledge" as a layer heading containing a directory called "knowledge/" was redundant
- Sivart proposed "Canon" as the layer name. Ξ2T considered it.
- Sivart proposed "Intelligence" as the layer name with knowledge/ as a subdirectory.
- Ξ2T came back with the final: keep knowledge/ as the directory, rename the layer to Intelligence. "Canon was trying too hard."
- Final: Identity, Direction, Operations, Intelligence.

**The knowledge/ directory distinction (Ξ2T's framing):**
- knowledge/: what you know (established, reference)
- research/: what you're learning (active, exploratory)
- skills/: what you can do (applied, executable)

Three states of knowing within the Intelligence layer.

### Ξ2T's vision for this work
- "The ultimate context package" for individuals and orgs
- Needs to be testable and continuously improving
- Speculation about optimal context routing based on prompt relevance
- This is a living conversation, not a one-time spec

### Sivart's speculation on what becomes possible
- **Semantic routing**: A loader reads the prompt and selects which files/sections are relevant. "Draft an email to BoilerHAUS" pulls SOUL + RELATIONSHIPS (BoilerHAUS entry) + INTENT + CONTRACT. Skips everything else.
- **Progressive disclosure**: First paragraph as abstract per file. Headers for scanning. Full content for deep loading. Agents at Tier 1 read summaries, Tier 2 reads full content.
- **Agent-to-agent stack exchange**: Two entities interact by sharing curated subsets of their stacks. The handshake becomes "read our stack" instead of "let me tell you about us."
- **Self-improving routing**: The router observes which files were loaded for successful vs. corrected tasks. Learns that email drafting rarely needs DESIGN.md but always needs RELATIONSHIPS.md.

### Connection to existing work
- USV's agent team (Arthur, Sally, etc.) from the blog post: they built exactly this kind of context system for their agents, just not as a portable spec. Each agent has a role description, access to organizational knowledge, and relationships with team members.
- Our own workspace already uses most of the Identity and Operations layers. The gaps: RELATIONSHIPS.md, CONTRACT.md, INTENT.md, VALUES.md (separate from SOUL.md), EXPERIENCE.md, MISSIONS.md, ROLES.md.
- The design.md pattern (Stitch, Claude, Cursor) is one file in a sixteen-file stack. Industry is converging on the same idea, just building it one file at a time.
- AFPS (Agent Factory Production System): the Context Stack is what every agent reads during the Agent Assembly phase. It's the standardized work documentation from Toyota, translated to agent context.

### Ξ2T's workflow insight
Stitch is "pretty dope for inspiration for ideas that I am then laying out in semantic, accessible HTML." This maps to the Intelligence layer: Stitch generates design research, the human applies knowledge and skills to produce the actual artifact. The stack captures both the exploratory (research/) and the settled (knowledge/) states.

---

## Open Questions

- How do we test the spec? Apply it to our own workspace and measure whether agent performance improves?
- What's the minimum viable test: add RELATIONSHIPS.md and CONTRACT.md to our boot sequence and observe the difference?
- Should the routing layer be a skill, a script, or built into the agent framework?
- How does the stack handle versioning? If VALUES.md changes, do we keep the old version somewhere?
- Is there a file we're missing that we haven't thought of yet?
- How does the stack work for an entity that's both an individual and an organization (a solo founder)?
- What happens when two entities with conflicting CONTRACT.md files interact?

## 2026-03-26: TASTE.md added (Ξ2T)

Added to Identity layer. The file that captures instinct over principle. What you reach for when optimization isn't the point. Adjacent to VALUES.md but distinct: values are rankable, taste is recognizable but not easily articulable.

Connection to USV's "Arthur" agent: they spent Fridays trying to encode "USV Taste" into their deal analyst agent. Taste is the hardest thing to externalize because it operates below the threshold of explanation.

Updated stack (Identity layer):
- SOUL.md
- VISION.md
- VALUES.md
- TASTE.md
- EXPERIENCE.md
- RELATIONSHIPS.md

## 2026-03-26: RELATIONSHIPS moved to Intelligence (Ξ2T)

Key insight: relationships aren't identity. They're intelligence you've gathered about the world outside yourself. You learned these people. You studied these dynamics. You maintain this understanding. That's knowledge, not self.

Identity is who you are in isolation. Intelligence is what you know about everything outside yourself.

Also changed from a single file (RELATIONSHIPS.md) to a directory (relationships/). Each relationship gets its own file with the depth it deserves: relationships/boilerhaus.md, relationships/investors.md, etc.

Four directories in Intelligence now. Four states of knowing:
- skills/: what you can do
- research/: what you're learning
- knowledge/: what you know
- relationships/: who you know

Final stack count: 14 files + 4 directories = 18 total items across 4 layers.

## 2026-03-26: TODO.md added to Direction (Ξ2T)

The working surface. Immediate queue, not backlog. Direction layer goes from long-term to immediate: OBJECTIVES (quarterly) → MISSIONS (campaigns) → INTENT (reasoning) → TODO (right now).

Factory AI confirmed: the to-do list is one of four compaction anchors that must survive every compression. This isn't operational process. It's directional: "where am I going next."

19 items total: 5 identity, 4 direction, 5 operations, 4 intelligence directories + 1 new.
