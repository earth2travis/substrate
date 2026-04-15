---
title: Lessons from Building Claude Code Skills (Thariq Shihipar, March 2026)
tags:
  - ai-agents
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/thariq-skills-lessons.md
---

# Lessons from Building Claude Code Skills (Thariq Shihipar, March 2026)

Source: https://x.com/trq212/status/2033949937936085378

Thariq leads Claude Code at Anthropic. This is from hundreds of skills in active use internally.

## The 9 Skill Types

### 1. Library & API Reference
How to use a lib/CLI correctly. Code snippets + gotchas folder.
**Our skills:** web-search, evm-wallet (partial).
**Gap:** None of ours bundle reference code snippets in a folder.

### 2. Product Verification
Test/verify code works. Scripts, headless browser, assertions, video recording.
**Our skills:** None.
**Gap:** Biggest missing category. PR verification, issue closure verification, skill test runner all belong here.

### 3. Data Fetching & Analysis
Connect to data stacks. Dashboard IDs, common queries, credential helpers.
**Our skills:** calendar (partial), gmail-processor (script, not skill).
**Gap:** Could formalize gmail and calendar as proper skills with data access patterns.

### 4. Business Process & Team Automation
Encode team workflows. Log previous results for consistency.
**Our skills:** conventional-commit, github-issues (WIP), github-projects (WIP).
**Key tip:** Save previous results in log files so the model stays consistent across runs.

### 5. Code Scaffolding & Templates
Generate boilerplate. Especially useful when scaffolding has natural language requirements.
**Our skills:** agent-soul-design (creates SOUL.md from scratch).
**Gap:** Could build new-skill, new-agent, new-experiment scaffolders.

### 6. Code Quality & Review
Enforce code quality. Deterministic scripts for robustness. Run via hooks or GitHub Actions.
**Our skills:** conventional-commit covers commit quality. Skill-optimizer is meta quality.
**Key pattern:** "adversarial-review: spawns a fresh-eyes subagent to critique, implements fixes, iterates until findings degrade to nitpicks."

### 7. CI/CD & Deployment
Fetch, push, deploy. May reference other skills.
**Our skills:** None as formal skills (we do this ad hoc).
**Key pattern:** "babysit-pr: monitors PR, retries flaky CI, resolves merge conflicts, enables auto-merge." We need this.

### 8. Runbooks
Symptom in, structured report out. Multi-tool investigation.
**Our skills:** None as formal skills (ops agent does this informally).
**Key pattern:** "oncall-runner: fetches alert, checks usual suspects, formats finding." Maps to our ops agent's daily check.

### 9. Infrastructure Operations
Routine maintenance with guardrails for destructive actions.
**Our skills:** openclaw-stability, healthcheck (bundled).
**Gap:** dependency-management, cost-investigation patterns.

## Tips That Change How We Build

### 1. Don't State the Obvious
Focus on information that pushes the model out of its normal thinking. The gotchas are the highest signal content.

**Action for us:** Every skill should have a prominent Gotchas section built from real failures. The skill-optimizer changelog IS this: it captures what doesn't work.

### 2. Use the File System as Progressive Disclosure
A skill is a folder, not a file. Tell the model what files exist and it reads them when needed.

**Action for us:** Restructure skills to use:
- `references/` for API docs, code snippets
- `assets/` for templates to copy
- `examples/` for worked examples
- `scripts/` for executable tools

We already do scripts/ in skill-optimizer. Extend this pattern everywhere.

### 3. Avoid Railroading
Be too specific and the skill becomes brittle. Give information, not step-by-step scripts.

**Action for us:** Review our skills for over-prescription. The conventional-commit skill might be too rigid.

### 4. Setup via config.json
Skills that need user context should store it in a config.json. If missing, ask the user.

**Action for us:** The skill-optimizer already does this with its config files. Formalize this pattern for all skills that need per-user setup.

### 5. The Description Field Is for the Model
It's not a summary. It's "when should I trigger this skill?" Write it as a trigger condition.

**Action for us:** Audit all our skill descriptions. Are they trigger conditions or summaries?

### 6. Memory via Log Files
Store data within skills (append-only logs, JSON, even SQLite). Next run, the model reads its own history. Use stable folder for persistence across upgrades.

**Action for us:** The standup-post pattern (standups.log) is directly applicable. Our session gap analyzer should keep a running log. Skill-optimizer already saves changelogs. Generalize this.

### 7. Store Scripts, Generate Code
Give the model helper functions. It spends turns on composition, not reconstruction.

**Action for us:** Bundle helper scripts in skills. The web-search skill already has search.py. The skill-optimizer has its runner. Every skill that involves computation should ship a script.

### 8. On-Demand Hooks
Skills can register hooks that activate only when the skill is called. Like `/careful` blocking destructive commands, or `/freeze` restricting edits to one directory.

**Not directly applicable** (OpenClaw doesn't have Claude Code's hook system), but the PATTERN is applicable: skills that change the agent's behavior temporarily. We could implement this via AGENTS.md cognitive modes (#448).

### 9. Distribution: Marketplace Pattern
Sandbox folder → traction → PR to marketplace. Curation before release.

**Maps to our plan:** `~/.openclaw/skills/` (shared) → ClawHub for registry (#427). The "sandbox → traction → promoted" flow is exactly what we should do.

### 10. Measuring Skills
PreToolUse hook logs skill usage. Find popular and undertriggering skills.

**Action for us:** Track which skills are actually loaded in sessions. The session gap analyzer could add a "skills_used" field.

### 11. Composing Skills
Reference other skills by name. Model invokes them if installed.

**Already doing this:** skill-optimizer references conventional-commit by name in its test configs.

## Top 5 Actions for Us (Priority Order)

1. **Add Gotchas sections** to every existing skill, built from real failures
2. **Restructure skill folders** with references/, assets/, scripts/ subdirs
3. **Build a PR babysitter skill** (type 7): monitor CI, retry flakes, auto-merge
4. **Add memory/logging** to skills that run repeatedly (gap analyzer, optimizer)
5. **Audit skill descriptions** as model trigger conditions, not summaries

## Skills We Should Build Next (by type gap)

| Priority | Skill | Type | Why |
|----------|-------|------|-----|
| HIGH | pr-babysitter | CI/CD | We manually check CI after every PR |
| HIGH | issue-verifier | Verification | #3 process failure (incomplete closure) |
| MEDIUM | oncall-runner | Runbook | Formalize ops agent's daily check |
| MEDIUM | new-skill-scaffold | Scaffolding | Make skill creation consistent |
| LOW | cost-investigator | Infra Ops | Monthly cost review automation |
