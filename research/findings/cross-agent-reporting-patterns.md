---
title: "Cross-Agent Reporting Patterns: Blackboard Architecture for Hermes Fleet Coordination"
tags: [agents, multi-agent, architecture, coordination, hermes, blackboard, reporting]
related:
- agent-orchestrator-pattern
- multi-agent-coordination-patterns
- agent-native-operations
- kanban-doctrine
- mission-command
- context-stack
source: research/raw/cross-agent-reporting-patterns.md
---
# Cross-Agent Reporting Patterns: Blackboard Architecture for Hermes Fleet Coordination

## Summary

Research on design patterns for cross-system and cross-agent reporting in multi-agent architectures, identifying the best mechanism for circulating SITREPs from Hermes specialist profiles to the central coordinator. The recommendation: the blackboard pattern from Hearsay-II (1970s CMU speech understanding), applied to Hermes profile architecture via the shared filesystem.

## Multi-Agent Framework Communication Patterns

Four major frameworks converge on three mechanisms for inter-agent communication:

1. **Message passing** (AutoGen) — agents talk directly; conversation history IS the shared state. Limitation: context grows linearly; no persistent state across sessions.
2. **Shared state store** (CrewAI, LangGraph) — a common data structure all agents read/write. CrewAI's shared memory (short-term, long-term entity, crew-level) is the key innovation. LangGraph adds explicit typed state schema with checkpoints.
3. **Pipeline with context variables** (Semantic Kernel) — state flows through a sequence of functions via kernel memory.

The shared state store is the most generalizable pattern for fleet coordination.

## The Blackboard Pattern (Hearsay-II)

Originated at Carnegie Mellon (1971-1976). Core idea: a shared workspace holds partial solutions; multiple independent knowledge sources monitor it and contribute when they can; a control shell decides who acts next. Solutions emerge through collaborative, opportunistic contributions.

Applied to multi-agent: shared workspace = directory/database all agents read/write; knowledge sources = specialist agent profiles; control shell = coordinator agent.

Strengths: loose coupling (agents don't need to know about each other directly), opportunistic (any agent contributes to any partial solution), auditable (blackboard records all contributions). Weaknesses: concurrency control needed, unbounded growth without curation, requires shared schema.

## NASA Mission Control Shift Handoff

Structured protocol refined across Mercury, Gemini, Apollo, Shuttle, ISS programs. Components: verbal handover brief, console log (real-time written), console file (procedures/anomaly reports), shift change report (signed), read-back by incoming controller. Key principles: handoff takes as long as it takes; verbal plus written (neither alone sufficient); anomaly tracking central with numbered root-cause investigations.

## FAA Traffic Flow Management

Fan-in, fan-out pattern: central hub (ATCSCC) collects, synthesizes, and redistributes. Specialist facilities report upward; hub consolidates; consolidated picture shared back downward. Directly applicable to a profile fleet architecture.

## Hermes Profile Architecture

Each profile is a separate Hermes home directory (`~/.hermes/profiles/<name>/`) with its own config, memories, sessions, skills, cron. Profiles are isolated by `HERMES_HOME`. Critical fact: all profiles share the same OS user filesystem — `/home/sivart/substrate/` is accessible from every profile. There is no native cross-profile messaging, no shared mailbox, no inter-profile notification. Cron jobs are per-profile with delivery to origin/local/Telegram/etc. but no "deliver to default profile's chat."

## Recommendation: Shared Filesystem as Blackboard

Each specialist profile writes its SITREP to a shared directory (`~/.hermes/sitreps/<profile>/<date>-<session_id>.md`). The default profile (Sivart) runs a cron job scanning for new SITREPs, synthesizes a digest, and reports to the operator. Processed SITREPs are archived to prevent unbounded growth.

This is the Hearsay-II blackboard pattern applied to Hermes: shared directory is the blackboard, specialist profiles are knowledge sources, Sivart is the control shell. Low ceremony, loose coupling, auditable, extensible (new profiles just write to the directory), and compatible with existing Hermes architecture without requiring new features.

## Why This Matters for the Substrate

This research informs the distributed agent operations model. The blackboard pattern is already used implicitly in the Substrate itself — `research/raw/` and `research/findings/` are shared workspaces that multiple agents and cron jobs read and write. The SITREP circulation extends this to operational reporting across a fleet.

The fan-in, fan-out pattern connects to [[agent-orchestrator-pattern]] and [[multi-agent-coordination-patterns]]. The shift-handoff discipline (verbal plus written, read-back, anomaly tracking) connects to [[kanban-doctrine]] and [[mission-command]] — structured handoff is mission command's operationalization. The shared-filesystem-as-blackboard is the coordination substrate described in [[agent-native-operations]].

## Related

- [[agent-orchestrator-pattern]] — Patterns for multi-agent orchestration
- [[multi-agent-coordination-patterns]] — Coordination across independent agents
- [[kanban-doctrine]] — Auftragstaktik as agent operating system
- [[mission-command]] — Command by intent rather than instruction