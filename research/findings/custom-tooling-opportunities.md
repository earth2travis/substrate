---
title: "Custom Tooling Opportunities: Agent-Native Project Management"
tags: [agent, tooling, project-management, process, automation, github]
related:
- github-as-memory
- project-board-configuration
- kanban-doctrine
- lean-software-delivery
- harness-engineering
- agent-native-operations
source: research/raw/custom-tooling-opportunities.md
---
# Custom Tooling Opportunities: Agent-Native Project Management

## Summary

Research on where existing tools fall short for an AI-human partnership and what custom tooling would close the gaps. The workflow is unusual: the project manager is an AI agent (Sivart) working with a human (Ξ2T). This creates specific friction points that no off-the-shelf tool addresses.

## Five Friction Points

**Friction Point 1: Context Loss Between Sessions.** Sivart wakes up fresh each session. Minutes are spent reconstructing context. Opportunity: Session context generator that produces a structured briefing (open issues by priority, recent closures, PRs awaiting review, calendar events, last daily notes summarized).

**Friction Point 2: Issue Lifecycle Gaps.** Process requires issue first, add to project, do work, commit with reference, close with summary. But nothing enforces this. Opportunity: Process compliance checker that audits commits without issue references, open issues with no recent activity, closed issues with no linked commits, issues not assigned to projects, PRs without linked issues.

**Friction Point 3: Work Capacity Blindness.** No clear picture of WIP, queue depth, or sustainable pace. No WIP limits, velocity tracking, or cycle time metrics. Opportunity: Capacity dashboard calculating current WIP, queue depth by priority, velocity (issues closed per week), size distribution, and cycle time.

**Friction Point 4: Research Discoverability.** Rich research directory (40+ files) but no index, no search. Sivart must ls and cat files to check what exists. Opportunity: Research index generator scanning research/ and generating an index with title, date, tags, related files, and one-line summary.

**Friction Point 5: Decision Tracking Fragmentation.** Decisions scattered across issue comments, commit messages, daily notes, and decisions/ directory. Opportunity: Decision log with backlinks ensuring every decision references the issue that prompted it.

## Agent-Native Project Management: What Changes

**What an AI PM does better:** Perfect process compliance (when configured), exhaustive search, consistent triage, documentation as natural output, 24/7 availability, multi-source synthesis.

**What an AI PM does worse:** No persistent state (wakes up reading files), no social sensing (cannot read frustration or detect burnout), difficulty with "when to break the rules," no independent motivation (no background processing between sessions), context window as WIP limit.

## Six Design Principles

1. **Write everything down.** If it is not in a file, it does not exist for the next session.
2. **Automate the ceremony, preserve the judgment.** Moving cards is ceremony. Deciding what to work on is judgment.
3. **Build session affordances.** Every tool interaction should assume fresh context.
4. **Externalize memory to structured data.** JSON for metrics, YAML for metadata, project fields for state.
5. **Short feedback loops by default.** Check process compliance after every commit, not once a week.
6. **Human-in-the-loop for irreversible actions.** Propose; human approves. Act autonomously on reversible actions.

## Six Concrete Proposals

1. **Session Briefing Script** (`scripts/session-briefing.js`) — High priority, 1 day effort
2. **Process Audit Script** (`scripts/process-audit.js`) — High priority, 1 day effort
3. **Capacity Report Script** (`scripts/capacity-report.js`) — Medium priority, 1.5 days
4. **Research Index Generator** (`scripts/research-index.js`) — Medium priority, 0.5 day
5. **Issue Form Templates** (`.github/ISSUE_TEMPLATE/`) — Medium priority, 0.5 day
6. **GitHub Actions Pipeline** (`.github/workflows/`) — Medium priority, 1 day

Total effort: approximately 5.5 days of focused work. Each is independent and can be a separate issue.

## Related

- [[github-as-memory]] — Issues as institutional knowledge graph
- [[project-board-configuration]] — GitHub Projects configuration
- [[kanban-doctrine]] — Auftragstaktik as agent operating system
- [[harness-engineering]] — Agent-first development methodology
- [[lean-software-delivery]] — Continuous improvement and measurement
- [[telegram-group-setup]] — Workspace for agent-human collaboration
