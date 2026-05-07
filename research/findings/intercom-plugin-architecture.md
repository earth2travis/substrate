---
title: "Intercom's Claude Code Plugin Architecture"
tags: [plugin-architecture, agent-platform, hooks, skills, observability, feedback-loop]
related:
  - [[agent-platform-ecosystem]]
  - [[skills-as-portable-knowledge]]
  - [[feedback-loop-discipline]]
  - [[agent-native-operations]]
  - [[context-persistence]]
source: "[Brian Scanlan thread](https://x.com/brian_scanlan/status/2033978300003987527) March 2026"
---

# Intercom's Claude Code Plugin Architecture

Intercom built an internal Claude Code plugin system: 13 plugins, 100-plus skills, a hooks system that intercepts lifecycle events, and MCP servers for production access. The system spans engineering, data, QA, incident response, and non-engineer workflows. Key theme: they treat Claude Code as a platform, not a tool.

## Architecture Layers

### 1. Hooks System (PreToolUse / PostToolUse lifecycle interception)

Claude Code exposes lifecycle hooks that fire before and after tool execution. Intercom uses these as a policy enforcement layer:

- PreToolUse hooks: intercept commands before execution. Block raw gh pr create (must use their create-pr skill instead), block modifications to merged PR branches, enforce safety gates on production tools.
- PostToolUse hooks: react after execution. Detect "command not found" errors and BSD versus GNU incompatibilities in real time. Suggest fixes, install via Homebrew, update CLAUDE.md so Claude knows the tool exists in future sessions.
- SessionEnd hooks: trigger transcript analysis with Haiku for gap classification.
- Permission hooks: after 5 permission prompts, suggest running the permissions analyzer.

This is the most architecturally significant pattern: hooks as a programmable control plane over agent behavior.

### 2. Skills System (100-plus skills across domains)

Skills are structured prompt or workflow packages that activate automatically:

- Flaky test fixer: 9-step forensic workflow, 20-category taxonomy, downloads CI failure data from S3, sweeps for sibling antipatterns.
- PR workflow: extracts business intent before creating PRs, background CI monitoring with ETag polling.
- QA follow-up: 7-stage pipeline (identify, investigate, filter, create issues).
- Video transcript: Google Meet recordings to markdown with contextual screenshots.
- Claude4Data: 30-plus analytics skills for Snowflake, Gong, finance metrics.
- Incident and troubleshooting: progressive disclosure pattern, converging toward runbooks executable by Claude.
- Local dev setup: environment troubleshooting for non-engineers.

Skills have quality evals and are reviewed regularly. Most-used skills get the most scrutiny.

### 3. MCP Servers (Production access)

- Production Rails console: read-replica only, blocked critical tables, mandatory model verification before every query, Okta auth, DynamoDB audit trail.
- Admin Tools MCP: customer lookups, feature flag checks, admin queries. Skill-level gate requires loading safety reference docs before tools unlock.

Notable: top 5 users of the production console are not engineers (design managers, support engineers, PM leaders).

### 4. Observability and Feedback Loop

- OpenTelemetry instrumentation: 14 lifecycle event types (SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, PermissionRequest, SubagentStart, etc.) flowing to Honeycomb.
- Privacy-first: never captures user prompts, messages, or tool input in telemetry.
- Session transcripts: sync to S3 with username SHA256-hashed.
- Gap analysis: on SessionEnd, Haiku analyzes full transcript, classifies gaps (missing_skill, missing_tool, repeated_failure, wrong_info), posts to Slack with pre-filled GitHub issue URLs.
- Feedback loop: sessions to detected gaps to GitHub issues to new skills to better sessions.
- Weekly CI job: fact-checks and updates all CLAUDE.md files and referenced docs.
- Log ingestion: Snowflake-based log search skill for incidents, integrated with Honeycomb traces and Datadog metrics.

### 5. Distribution and Management

- JAMF: automatic deployment of skill marketplace to Macs.
- Usage reports: track skill creation and usage.
- Quality evals: regular review of most-used skills.
- Permissions analyzer: scans 14 days of transcripts, classifies commands GREEN, YELLOW, RED, writes safe ones to settings.json.

## Architecture Patterns Worth Adopting

Pattern 1: Hooks as policy layer. Using Claude Code's hook system not just for logging but for enforcement. PreToolUse hooks become guardrails; PostToolUse hooks become self-healing mechanisms.

Pattern 2: Session gap analysis (feedback loop). Analyzing every session transcript for improvement opportunities and auto-filing issues. This closes the loop between usage and improvement without manual review.

Pattern 3: Evidence-based permissions. Instead of prescriptive permission rules, analyzing actual usage patterns to determine what should be auto-approved. Data-driven security posture.

Pattern 4: Skill-gated access. Requiring skill activation before accessing dangerous tools. The skill loads context, safety docs, and constraints before the tool becomes available.

Pattern 5: Progressive disclosure for complex workflows. Incident and troubleshooting skills use a core skill that determines what specialized investigation to run. Avoids overwhelming context.

## Key Takeaways

1. The feedback loop is the killer feature. Session analysis to gap detection to issue creation to skill improvement to better sessions.
2. Hooks are greater than conventions. Intercom enforces policy via code (PreToolUse hooks), not prose.
3. Non-engineers are power users. Their production console is most used by PMs, designers, and support. Skills that make technical capabilities accessible to non-technical users have outsized impact.
4. Privacy by design. SHA256 username hashing, never capturing prompts in telemetry, read-replica for production access.
5. Skills as the unit of composition. Everything is a skill with evals. Skills are the primitive, not ad-hoc prompts.
