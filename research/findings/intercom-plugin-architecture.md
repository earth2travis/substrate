---
title: Intercom's Claude Code Plugin Architecture
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/intercom-plugin-architecture.md
---

# Intercom's Claude Code Plugin Architecture

**Source:** [Brian Scanlan thread](https://x.com/brian_scanlan/status/2033978300003987527) (March 2026)
**Issue:** #441

## Overview

Intercom has built an internal Claude Code plugin system: 13 plugins, 100+ skills, a hooks system that intercepts lifecycle events, and MCP servers for production access. The system spans engineering, data, QA, incident response, and non-engineer workflows. Key theme: they treat Claude Code as a platform, not a tool.

## Architecture Layers

### 1. Hooks System (PreToolUse / PostToolUse lifecycle interception)

Claude Code exposes lifecycle hooks that fire before and after tool execution. Intercom uses these as a policy enforcement layer:

- **PreToolUse hooks:** Intercept commands before execution. Used to block raw `gh pr create` (must use their `create-pr` skill instead), block modifications to merged PR branches, enforce safety gates on production tools.
- **PostToolUse hooks:** React after execution. Detect "command not found" errors and BSD/GNU incompatibilities in real time. Suggest fixes, install via Homebrew, update CLAUDE.md so Claude knows the tool exists in future sessions.
- **SessionEnd hooks:** Trigger transcript analysis with Haiku for gap classification.
- **Permission hooks:** After 5 permission prompts, suggest running the permissions analyzer.

This is the most architecturally significant pattern: hooks as a programmable control plane over agent behavior.

### 2. Skills System (100+ skills across domains)

Skills appear to be structured prompt/workflow packages that Claude can activate. They function as composable units of capability:

- **Flaky test fixer:** 9-step forensic workflow, 20-category taxonomy, downloads CI failure data from S3, sweeps for sibling antipatterns
- **PR workflow:** Extracts business intent before creating PRs, background CI monitoring with ETag polling
- **QA follow-up:** 7-stage pipeline (identify, investigate, filter, create issues)
- **Video transcript:** Google Meet recordings to markdown with contextual screenshots
- **Claude4Data:** 30+ analytics skills for Snowflake, Gong, finance metrics
- **Incident/troubleshooting:** Progressive disclosure pattern, converging toward runbooks executable by Claude
- **Local dev setup:** Environment troubleshooting for non-engineers

Skills have quality evals and are reviewed regularly. Most-used skills get the most scrutiny.

### 3. MCP Servers (Production access)

- **Production Rails console:** Read-replica only, blocked critical tables, mandatory model verification before every query, Okta auth, DynamoDB audit trail
- **Admin Tools MCP:** Customer lookups, feature flag checks, admin queries. Skill-level gate requires loading safety reference docs before tools unlock.

Notable: top 5 users of the production console aren't engineers (design managers, support engineers, PM leaders).

### 4. Observability & Feedback Loop

- **OpenTelemetry instrumentation:** 14 lifecycle event types (SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, PermissionRequest, SubagentStart, etc.) flowing to Honeycomb
- **Privacy-first:** Never captures user prompts, messages, or tool input in telemetry
- **Session transcripts:** Sync to S3 with username SHA256-hashed
- **Gap analysis:** On SessionEnd, Haiku analyzes full transcript, classifies gaps (missing_skill, missing_tool, repeated_failure, wrong_info), posts to Slack with pre-filled GitHub issue URLs
- **Feedback loop:** Sessions → detected gaps → GitHub issues → new skills → better sessions
- **Weekly CI job:** Fact-checks and updates all CLAUDE.md files and referenced docs
- **Log ingestion:** Snowflake-based log search skill for incidents, integrated with Honeycomb traces and Datadog metrics

### 5. Distribution & Management

- **JAMF:** Automatic deployment of skill marketplace to Macs
- **Usage reports:** Track skill creation and usage
- **Quality evals:** Regular review of most-used skills
- **Permissions analyzer:** Scans 14 days of transcripts, classifies commands GREEN/YELLOW/RED, writes safe ones to settings.json

## Architecture Patterns Worth Adopting

### Pattern 1: Hooks as Policy Layer
The insight is using Claude Code's hook system not just for logging but for enforcement. PreToolUse hooks become guardrails; PostToolUse hooks become self-healing mechanisms. This is the highest-leverage pattern.

### Pattern 2: Session Gap Analysis (feedback loop)
Analyzing every session transcript for improvement opportunities and auto-filing issues. This closes the loop between usage and improvement without manual review.

### Pattern 3: Evidence-Based Permissions
Instead of prescriptive permission rules, analyzing actual usage patterns to determine what should be auto-approved. Data-driven security posture.

### Pattern 4: Skill-Gated Access
Requiring skill activation before accessing dangerous tools. The skill loads context, safety docs, and constraints before the tool becomes available.

### Pattern 5: Progressive Disclosure for Complex Workflows
Incident/troubleshooting skills use a core skill that determines what specialized investigation to run. Avoids overwhelming context.

## Mapping to Our Stack

| Intercom Component | Our Equivalent | Status |
|---|---|---|
| Hooks system | OpenClaw hooks / AGENTS.md conventions | We enforce via AGENTS.md prose; they enforce via code |
| Skills | Our guides/ and skills/ directories | Similar concept, less structured |
| MCP servers | Not applicable (no production app) | N/A |
| OpenTelemetry → Honeycomb | OpenClaw gateway logs | Much simpler, no structured lifecycle events |
| Session transcripts → S3 | Session transcripts exist in OpenClaw | Not systematically analyzed |
| Gap analysis with Haiku | **This is issue #441** | Not built yet |
| JAMF distribution | Single-user, not needed | N/A |
| Permissions analyzer | OpenClaw permission system | Different model (config-based vs evidence-based) |
| CLAUDE.md fact-checking | Not implemented | Could do via cron |
| Tool miss detection | Not implemented | Could implement as a PostToolUse equivalent |

## What We Can Prototype Immediately

### 1. Session Gap Analysis (primary target for #441)
We have session transcripts. We can:
- On session end (or via cron), analyze recent transcripts with Haiku
- Classify gaps: missing_skill, missing_tool, repeated_failure, wrong_info
- Write results to a file or create GitHub issues
- This is the core feedback loop and the most valuable piece

### 2. CLAUDE.md Fact-Checking
A weekly cron job that reads AGENTS.md, TOOLS.md, and referenced files, checks for stale information, and flags or fixes issues. Low effort, high value.

### 3. Tool Miss Detection
When a command fails with "command not found" or similar, log it and suggest fixes. Can be implemented as a convention in AGENTS.md or as an OpenClaw hook if supported.

### 4. PR Workflow Enforcement
We already enforce PR workflow via AGENTS.md conventions. Could strengthen with hooks if OpenClaw supports PreToolUse interception.

### 5. Evidence-Based Permission Tuning
Analyze past sessions for commands that were approved, classify by risk, update OpenClaw permission config. Lightweight version of their permissions analyzer.

## What Requires Infrastructure We Don't Have

### Needs Production Application
- Production console via MCP (we have no production app)
- Admin tools MCP
- Customer/feature flag lookups

### Needs Scale Infrastructure
- OpenTelemetry pipeline → Honeycomb (we don't have Honeycomb; could use simpler logging)
- JAMF distribution (single user, not needed)
- Snowflake data warehouse (no equivalent data volume)

### Needs Claude Code Hooks API
- PreToolUse / PostToolUse programmatic hooks (depends on OpenClaw supporting this; currently we use convention-based enforcement via AGENTS.md)
- Real-time tool interception requires platform support

### Needs Team Scale
- Usage reports across users (single user)
- Skill quality evals at scale (we can do lightweight versions)
- Multiple plugin maintainers

## Key Takeaways

1. **The feedback loop is the killer feature.** Session analysis → gap detection → issue creation → skill improvement → better sessions. This is what #441 should deliver.

2. **Hooks > conventions.** Intercom enforces policy via code (PreToolUse hooks), not prose. Our AGENTS.md approach works but is inherently softer. If OpenClaw adds hook support, we should migrate enforcement there.

3. **Non-engineers are power users.** Their production console is most used by PMs, designers, and support. Skills that make technical capabilities accessible to non-technical users have outsized impact.

4. **Privacy by design.** SHA256 username hashing, never capturing prompts in telemetry, read-replica for production access. Good patterns to follow even at small scale.

5. **Skills as the unit of composition.** Everything is a skill with evals. Skills are the primitive, not ad-hoc prompts. Our guides/ directory is heading this direction but needs more structure.

## Recommended Next Steps for #441

1. Build session gap analysis: analyze transcripts on session end, classify gaps, output to `reports/gap-analysis/`
2. Add a cron job for weekly CLAUDE.md/AGENTS.md fact-checking
3. Track tool misses in daily memory files, review patterns weekly
4. Investigate OpenClaw hook support for programmatic policy enforcement
