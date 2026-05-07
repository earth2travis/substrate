---
title: 'Solving Memory: ClawVault and the Obsidian Insight for Agent Continuity'
tags:
- agent-memory
- clawvault
- obsidian
- markdown
- memory-systems
related:
- knowledge-graphs-as-agent-memory-substrate
- memory-systems
- the-context-stack-spec
- clawhavoc-security-crisis
- openclaw
source: research/raw/solving-memory.md
---




# Solving Memory: ClawVault and the Obsidian Insight for Agent Continuity

## Summary

ClawVault is an open-source memory architecture that gives AI agents continuity by treating memory as markdown files with YAML frontmatter in a folder hierarchy, exactly like Obsidian. The key insight from benchmarking: plain markdown files organized in folders, with grep and search, outperformed purpose-built memory infrastructure (74.0% vs. 68.5% on LoCoMo). Why? Because LLMs already know how to work with files. Fighting that instinct with specialized APIs is swimming upstream. ClawVault enforces a memory taxonomy (decision, preference, relationship, commitment, lesson) and uses wiki-links for associative navigation. The architecture makes zero network calls, stores everything on the filesystem, and produces a vault that is simultaneously a ClawVault document, an Obsidian note, and a plain text file. One format, zero lock-in, complete interoperability.

## Key Claims

1. **The agent memory problem is a design problem, not a technology problem.** The tools already exist: markdown files, YAML frontmatter, folder hierarchies, wiki-links. Obsidian proved this works for humans. ClawVault proves it works for agents.

2. **Memory types matter.** Every memory is typed because "show me all decisions from last month" only works if you stored them as decisions. Dumping everything into a single notes file is the agent equivalent of writing on your hand.

3. **The vault index pattern.** A single file listing every note with a one-line description. The agent scans the index first before deciding what to read. Dramatically more efficient than embedding search for most queries.

4. **Budget-aware context injection.** Observational memory compresses conversations into priority-tagged observations: critical (decisions, commitments, blockers), notable (insights, preferences), background (routine updates). The agent loads critical observations first, then fills remaining context budget with notable, then background.

5. **Zero cloud, full sovereignty.** Agent memories contain the most sensitive operational data in an organization. That data should never leave the infrastructure unless explicitly chosen. ClawVault makes zero network calls.

## Implications

Human knowledge management and agent memory management are the same problem. Both need typed structured storage, associative linking, priority-based retrieval under budget constraints, compression that preserves signal, and zero lock-in. When the agent's memory vault IS an Obsidian vault, the agent's memory becomes inspectable, auditable, and editable by humans. That is not a feature. That is the whole point.

## Related

- [[knowledge-graphs-as-agent-memory-substrate]] — Graph-based memory as a complementary layer
- [[memory-systems]] — Memory architectures supporting agent continuity
- [[the-context-stack-spec]] — The Context Stack as the portable identity layer
- [[clawhavoc-security-crisis]] — The security crisis that ClawVault emerged from
- [[openclaw]] — The OpenClaw platform and its memory architecture
