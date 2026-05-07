---
title: "OpenClaw Community Audit Practices"
tags: [openclaw, audit, agents, community, governance, security]
related:
- openclaw
- clawhavoc-security-crisis
- harness-engineering
- dark-factory
source: research/raw/openclaw-community.md
---
# OpenClaw Community Audit Practices

## Summary

OpenClaw's built-in infrastructure provides a foundation for agent auditing: AGENTS.md as constitution, memory system for audit trails, heartbeat for periodic checks, and sub-agent isolation for independent verification. However, no standardized audit framework exists in the community.

## Key Claims

1. **Built-in Infrastructure:** AGENTS.md acts as repository constitution; memory/ directory + MEMORY.md for persistent state; heartbeat system for background work; compaction for context management; `openclaw doctor` for health checks.
2. **Agent Workspace Pattern:** Identity files (SOUL.md, IDENTITY.md, USER.md), operational files (AGENTS.md, TOOLS.md, HEARTBEAT.md), memory files (memory/YYYY-MM-DD.md), bootstrap flow.
3. **File-Based Self-Monitoring:** Write procedures to files, read every session, follow them. Memory files serve as audit trail. Daily notes as raw journal, MEMORY.md as curated wisdom.
4. **Missing Standardization:** No community-wide audit framework exists. Each operator builds their own approach. Opportunity for reusable patterns.

## Implications

OpenClaw's file-based architecture is inherently audit-friendly: everything is version-controlled and reviewable. The gap is not tooling but standardization. A shared audit practice could become a community standard.

## Related

- [[openclaw]] — Platform architecture
- [[clawhavoc-security-crisis]] — Security incident motivating audit practices
- [[harness-engineering]] — Agent environment design
- [[dark-factory]] — Lights-out operation requiring self-monitoring
