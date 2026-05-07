---
title: "Lessons from Building Claude Code Skills (Thariq Shihipar)"
tags: [agents, skills, claude-code, best-practices, anthropic]
related:
  - [[skills-as-portable-knowledge]]
  - [[harness-engineering]]
  - [[agent-native-operations]]
  - [[the-openclaw-lesson]]
source: research/raw/thariq-skills-lessons.md
---

# Lessons from Building Claude Code Skills (Thariq Shihipar)

**Source:** https://x.com/trq212/status/2033949937936085378, March 2026
**Author:** Thariq Shihipar, leads Claude Code at Anthropic

## The 9 Skill Types

1. **Library & API Reference:** How to use a lib/CLI correctly. Code snippets + gotchas.
2. **Product Verification:** Test/verify code works. Scripts, headless browser, assertions.
3. **Data Fetching & Analysis:** Connect to data stacks. Dashboard IDs, common queries.
4. **Business Process & Team Automation:** Encode team workflows. Log previous results for consistency.
5. **Code Scaffolding & Templates:** Generate boilerplate. Useful when scaffolding has natural language requirements.
6. **Code Quality & Review:** Enforce code quality. Deterministic scripts for robustness.
7. **CI/CD & Deployment:** Fetch, push, deploy. May reference other skills.
8. **Runbooks:** Symptom in, structured report out. Multi-tool investigation.
9. **Infrastructure Operations:** Routine maintenance with guardrails for destructive actions.

## Tips That Change How to Build Skills

1. **Don't state the obvious.** Focus on information that pushes the model out of normal thinking. Gotchas are highest signal.
2. **Use the file system as progressive disclosure.** A skill is a folder, not a file. Tell the model what files exist and it reads them when needed.
3. **Avoid railroading.** Be too specific and the skill becomes brittle. Give information, not step-by-step scripts.
4. **Setup via config.json.** Skills that need user context should store it in config.json.
5. **The description field is for the model.** It's not a summary. It's "when should I trigger this skill?"
6. **Memory via log files.** Store data within skills (append-only logs, JSON, SQLite). Next run, the model reads its own history.
7. **Store scripts, generate code.** Give the model helper functions. It spends turns on composition, not reconstruction.
8. **On-demand hooks.** Skills can register hooks that activate only when called.
9. **Distribution: Marketplace pattern.** Sandbox folder → traction → PR to marketplace.
10. **Measuring skills.** PreToolUse hook logs skill usage. Find popular and undertriggering skills.
11. **Composing skills.** Reference other skills by name. Model invokes them if installed.

## Top 5 Actions

1. Add Gotchas sections to every existing skill, built from real failures
2. Restructure skill folders with references/, assets/, scripts/ subdirs
3. Build a PR babysitter skill: monitor CI, retry flakes, auto-merge
4. Add memory/logging to skills that run repeatedly
5. Audit skill descriptions as model trigger conditions, not summaries
