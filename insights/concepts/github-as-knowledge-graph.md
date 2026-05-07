---
title: "GitHub as Knowledge Graph"
tags: [github, knowledge-graph, institutional-memory, agent, operations]
related: [[github-as-memory]], [[github-knowledge-graph-second-brain]], [[github-issues-best-practices]], [[github-practices]], [[github-project-best-practices]], [[agent-native-operations]], [[harness-engineering]], [[kanban-doctrine]], [[deployment-governance]], [[living-project-graph]]
source: research/findings/github-as-memory.md
---

# GitHub as Knowledge Graph

## Thesis

GitHub Issues are not task trackers. They are nodes in an institutional knowledge graph. The commit log is a timeline. PRs narrate change. Comments preserve reasoning. When someone asks for the status of X, the answer must always be in GitHub, not in someone's head.

## The Memory Quality Problem

An audit of twenty recent issues scored an average memory quality of 2.96/5.0. Strong patterns: issue bodies explain context well, prefix conventions aid categorization, acceptance criteria create clear completion signals. Weak patterns: unlabeled issues, perfunctory closure comments, sparse cross-references, research issues rarely linking back to decisions they influenced.

## The GitHub Memory Protocol

Conventions for writing issues that serve as institutional memory:

1. **Issue Body: Write for Future Retrieval.** What, why, what did we learn, where does it connect.
2. **Mandatory Cross-References.** Parent goal, related decision, research file, artifact paths.
3. **Closure Protocol.** Outcome, artifacts, lessons, PR link.
4. **Label Hygiene.** Every issue gets labeled at creation.
5. **Knowledge Issues.** Decisions, learnings, patterns as reference issues.
6. **Search Optimization.** Write titles like search queries.

## The Mindset Shift

Organizations that use GitHub as memory share one trait: issues are written for the reader who arrives six months later, not for the person doing the work today. This is not a tooling problem. It is a discipline problem.

## Agent Implications

Agents that consume this graph downstream depend on the data quality created today. Loomrunner and similar systems need rich issue bodies to understand task requirements, find related context, learn from past decisions, and avoid repeating mistakes. Better issues improve downstream agent performance.

## Connection to Kanban

The Kanban doctrine's "Issue First" rule and closure discipline directly support knowledge graph quality. Every issue is a node; every closure is a synthesis. The board shows flow; the issues hold meaning.

## Related

- [[github-as-memory]] — The flagship document on GitHub as institutional memory
- [[github-knowledge-graph-second-brain]] — Synthesis of knowledge graph and second brain framing
- [[github-issues-best-practices]] — Anatomy, types, sizing, and lifecycle
- [[github-practices]] — Branching, commits, PRs, labels, CI/CD
- [[github-project-best-practices]] — Issues, labels, milestones, projects
- [[agent-native-operations]] — Tools designed for AI-human partnership
- [[harness-engineering]] — Agent-first development methodology
- [[kanban-doctrine]] — Auftragstaktik mapped to agent operations
