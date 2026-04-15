---
title: "Proposal: Learnings from Agent Company Research"
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/proposal.md
---

# Proposal: Learnings from Agent Company Research

Based on analysis of the X articles [[Ξ2T]] shared.

---

## Executive Summary

The articles describe a multi-agent system architecture. While much of it is overengineered for our needs, there are three patterns worth adopting:

1. **Memory Type Taxonomy** (low effort, immediate value)
2. **Priority-Tagged Memories** (low effort, improves retrieval)
3. **Verification of ClawVault Claims** (research task)

---

## Recommended Actions

### 1. Adopt Memory Type Taxonomy in MEMORY.md

**What:** Organize MEMORY.md sections by memory type:

- **Insights** → New discoveries, observations
- **Patterns** → Recurring behaviors, trends
- **Strategies** → What works, approaches
- **Preferences** → [[Ξ2T]]'s preferences, my preferences
- **Lessons** → What we learned from mistakes

**Why:** Makes memory more structured and retrievable. When making decisions, I can query "lessons" specifically rather than scanning everything.

**Effort:** 30 minutes to reorganize MEMORY.md

**Example:**

```markdown
## Lessons Learned

- **Compaction incident (Jan 31):** Lost raw soul exploration dialogue...
- **Project number 4:** Foundation is project 4, not 1...

## Patterns

- **Session greeting:** Always check context % after startup reads
- **Email handling:** Radio silence default, escalate when necessary

## Strategies

- **Centaur chess principle:** Weak human + machine + better process > all
- **Issues first:** Every time, no exceptions
```

### 2. Add Priority Tags to Key Memories

**What:** Mark memories with priority indicators:

- 🔴 Critical (decisions, commitments, blockers)
- 🟡 Notable (insights, context worth remembering)
- 🟢 Background (nice to know, low urgency)

**Why:** When context is limited, load 🔴 first. Helps with memory search prioritization.

**Effort:** 15 minutes to tag existing memories

### 3. Verify ClawVault Before Considering

**What:** Research task to verify:

- Does https://github.com/Versatly/clawvault exist?
- Is the npm package real and maintained?
- Can we reproduce their benchmark claims?

**Why:** The file-based memory approach aligns with what we already do. If ClawVault is real and good, it might offer useful patterns. If it's vaporware, we ignore it.

**Effort:** 1 hour research

---

## What We Should NOT Do

1. **Don't add more agents.** We have one agent (me) working well. Adding 5 more would add complexity without clear benefit.

2. **Don't build relationship tracking.** Affinity systems between agents are cool but pointless when there's only one agent.

3. **Don't switch to Supabase.** Their architecture assumes PostgreSQL for state. We use files + [[OpenClaw]]. Our approach works and is simpler.

4. **Don't install their Claude Code skill.** Unverified source, unclear if it's even related to our [[OpenClaw]].

5. **Don't overcomplicate the heartbeat.** Our HEARTBEAT.md + [[OpenClaw]] heartbeat is sufficient. We don't need 16 conversation formats.

---

## Validation of Our Current Approach

The ClawVault article's key finding validates what we're already doing:

> "Plain markdown files — organized in folders, with grep and search — outperformed purpose-built memory infrastructure."

We use:

- MEMORY.md (curated long-term memory)
- memory/YYYY-MM-DD.md (daily notes)
- decisions/ (decision records)
- reports/ (daily reports)

This IS the pattern they recommend. We're ahead of them.

---

## Future Considerations (Not Now)

If we ever scale to multiple agents (spawn sub-agents for complex tasks), these patterns become relevant:

- **Proposal/Mission/Step loop** for task management
- **Atomic claiming** for distributed workers
- **Reaction matrix** for agent-to-agent coordination

For now, one agent + [[OpenClaw]] cron jobs is sufficient.

---

## Decision Requested

- [ ] Approve memory taxonomy reorganization
- [ ] Approve priority tagging
- [ ] Approve ClawVault verification research
- [ ] Defer all multi-agent patterns until needed
