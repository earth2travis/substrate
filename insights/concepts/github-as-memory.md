---
title: "GitHub as Memory: Institutional Knowledge Graph"
tags: [concept, github, memory, knowledge-graph, process, operations]
related:
- github-as-knowledge-graph
- workflow-as-contract
- agent-native-operations
- custom-tooling-opportunities
- protocol-as-coordination
- llm-wiki-pattern
source: research/findings/github-as-memory.md
---

# GitHub as Memory: Institutional Knowledge Graph

## Thesis

GitHub Issues are not a task tracker. They are nodes in an institutional knowledge graph. Every issue captures a decision, a context, a piece of understanding. The commit log is a timeline. PRs narrate how and why things changed. Comments preserve the reasoning that shaped direction. The quality of this memory determines how well future agents and humans can understand the system.

## The Memory Quality Audit

Twenty recent issues scored on five dimensions:
- Context richness: 3.4/5.0
- Cross-references: 2.8/5.0
- Searchability: 3.1/5.0
- Closure quality: 2.5/5.0
- Knowledge density: 3.0/5.0
- **Overall: 2.96/5.0** — passing, significant room for improvement

## The GitHub Memory Protocol

1. **Issue Body**: Write for future retrieval (what, why, what did we learn, where does it connect)
2. **Mandatory Cross-References**: Parent goal, related decision, research file, artifact paths
3. **Closure Protocol**: Outcome, artifacts, lessons, PR link
4. **Label Hygiene**: Every issue gets labeled at creation
5. **Knowledge Issues**: Decisions, learnings, patterns as reference issues
6. **Search Optimization**: Write titles like search queries

## The Mindset Shift

Organizations that use GitHub as memory share one trait: issues are written for the reader who arrives six months later, not for the person doing the work today. The same discipline applies to Substrate: every page written for the reader six months from now.

## Related

- [[github-as-knowledge-graph]] — The promoted insight on GitHub as knowledge graph
- [[workflow-as-contract]] — Agent behavior versioned in-repo
- [[agent-native-operations]] — Tools designed for AI-human partnership
- [[llm-wiki-pattern]] — Structured markdown as knowledge substrate
