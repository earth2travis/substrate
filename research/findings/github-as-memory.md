---
title: "GitHub as Memory: Institutional Knowledge Graph"
tags: [github, memory, knowledge-graph, process, agent, operations]
related: [[llm-wiki-pattern]], [[harness-engineering]], [[dark-factory]], [[lean-software-delivery]], [[custom-tooling-opportunities]], [[agent-native-operations]], [[protocol-as-coordination]]
source: research/raw/github-as-memory.md
---

# GitHub as Memory: Institutional Knowledge Graph

## Summary

GitHub Issues are not a task tracker. They are nodes in an institutional knowledge graph. Every issue captures a decision, a context, a piece of understanding. The commit log is a timeline. PRs narrate how and why things changed. Comments preserve the reasoning that shaped direction. The research audited 20 recent issues and found an average memory quality score of 2.96/5.0: passing but significant room for improvement.

## Key Claims

**The memory quality audit.** Twenty recent issues (#446 through #550) scored on five dimensions: Context richness (3.4), Cross-references (2.8), Searchability (3.1), Closure quality (2.5), Knowledge density (3.0). Overall: 2.96/5.0.

**Strong patterns:** Issue bodies generally explain context well (research issues especially). Prefix convention (feat:, chore:, research:) aids categorization. Acceptance criteria create clear completion signals.

**Weak patterns:** 5 of 20 issues have zero labels. Closure comments are often perfunctory ("done") or missing entirely. Cross-references are sparse. Research issues rarely link back to which decisions they influenced. No convention for linking issues to file artifacts.

**The GitHub Memory Protocol.** Conventions for writing issues that serve as institutional memory:
1. Issue Body: Write for Future Retrieval (what, why, what did we learn, where does it connect)
2. Mandatory Cross-References (parent goal, related decision, research file, artifact paths)
3. Closure Protocol (outcome, artifacts, lessons, PR link)
4. Label Hygiene (every issue gets labeled at creation)
5. Knowledge Issues (decisions, learnings, patterns as reference issues)
6. Search Optimization (write titles like search queries)

**The mindset shift.** Organizations that use GitHub as memory share one trait: issues are written for the reader who arrives six months later, not for the person doing the work today.

## Research: How Others Use GitHub as Memory

**Agent Systems:** SWE-agent uses issue bodies as task specs but rarely as knowledge stores. BoilerHAUS stores knowledge as markdown in repos, uses issues for meta-discussion. Cursor/Windsurf treat codebase as memory, issues as work queue.

**Human Organizations:** GitLab's handbook-first approach: everything documented in repo, issues lead to handbook changes. Oxide Computer: dense issue culture, RFDs as primary decision mechanism. Astral (uv/ruff): high-quality triage but issues are still tasks, not knowledge.

## Five Concrete Improvements

1. **Label the unlabeled** (immediate): Issues #546-550 need labels
2. **Create a closure template** (this week): Outcome, artifacts, lessons, PR link
3. **Add "Related" sections retroactively** (ongoing): When touching an issue, add cross-references
4. **Monthly memory health check** (cron): Flag issues with no labels, no closing comment, PRs with no linked issue
5. **Enable Discussions for architectural conversations** (decision needed): Open-ended conversations that don't fit issue format

## Connection to Loomrunner

Loomrunner (the-agent-factory #37) needs to understand project context from GitHub. The quality of our issues directly determines how well Loomrunner can understand task requirements, find related context, learn from past decisions, and avoid repeating mistakes. The GitHub Memory Protocol is a data quality standard for the knowledge graph that Loomrunner will consume.

## Related

- [[llm-wiki-pattern]] — Structured markdown as knowledge substrate
- [[harness-engineering]] — Agent-first development methodology
- [[dark-factory]] — Lights-out operation requiring institutional memory
- [[lean-software-delivery]] — Continuous improvement and documentation
- [[github-as-knowledge-graph]] — The promoted insight on GitHub as knowledge graph
- [[github-knowledge-graph-second-brain]] — Synthesis of knowledge graph and second brain framing
- [[github-issues-best-practices]] — Anatomy, types, sizing, and lifecycle
- [[github-practices]] — Branching, commits, PRs, labels, CI/CD
- [[custom-tooling-opportunities]] — Agent-native tooling for process compliance
- [[project-board-configuration]] — GitHub Projects configuration for visibility
