---
title: "Agent Skills as Onboarding: Research and Analysis"
tags:
  - ai-agents
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/agent-skills-as-onboarding.md
---

# Agent Skills as Onboarding: Research and Analysis

## The Pattern: Skills First, Docs Second

The emerging pattern in agent tooling: onboard agents through **skills**, not documentation. Instead of pointing an agent at a README and hoping it figures things out, you hand it a skill that teaches it how to work in your system.

### Why This Matters

Traditional onboarding: Agent reads docs → tries to understand the system → makes mistakes → learns from corrections → eventually becomes productive.

Skill based onboarding: Agent loads a skill → skill contains procedures, commands, conventions → agent is productive from the first interaction.

The difference is **time to productivity**. A skill encodes operational knowledge that would otherwise require multiple sessions of trial and error.

### How the Pattern Works

1. **Entry point**: A single skill file (SKILL.md) that covers everything a new agent needs
2. **Progressive disclosure**: Core operations first, advanced features gated behind triggers
3. **Executable knowledge**: Not just "here's how things work" but "here's what to run"
4. **Convention encoding**: Style, naming, process rules baked into the skill itself

### Analysis of Our Existing Skill Library

We have 17 skills. Examining them for onboarding potential:

**High onboarding value** (teach an agent to be productive in a domain):
- `github-issues`: Full issue lifecycle, labels, projects, sub-issues
- `github-projects`: Project v2 management, custom fields, views
- `conventional-commit`: Commit conventions, PR templates
- `blog-deploy`: End to end blog deployment pipeline
- `calendar`: Calendar management commands and conventions

**Medium onboarding value** (specialized but narrow):
- `execution-traces`: Instrumentation for agent work
- `lesson-extraction`: Daily learning capture
- `content-ingestion`: URL to knowledge notes pipeline

**Low onboarding value as standalone** (utilities):
- `memory-merger`, `skill-optimizer`, `web-search`

### Gap Analysis

No skill currently answers: "I'm a new agent in this workspace. What do I need to know to be useful?"

This is the missing **meta-skill**: one that bootstraps an agent into the workspace itself.

## Prototype Design: Workspace Onboarding Skill

### Philosophy

The onboarding skill should make a fresh agent productive within one interaction. It should cover:

1. **Workspace layout**: What lives where
2. **Core workflows**: How work gets done (issue → branch → PR → merge)
3. **Conventions**: Naming, style, commit format
4. **Available skills**: What capabilities exist and when to use them
5. **Identity context**: Who the human is, what matters to them
6. **Safety boundaries**: What requires permission, what's autonomous

### What Worked in Testing

Built the prototype (see `skills/workspace-onboarding/SKILL.md`). Key findings:

1. **Layered structure works**: Start with "what is this workspace" then drill into specifics
2. **Commands over descriptions**: "Run `gh issue list`" beats "check GitHub for open issues"
3. **Cross-referencing skills**: The onboarding skill should point to specialist skills, not duplicate them
4. **Convention emphasis**: Style rules, commit format, and writing rules need prominent placement because they're the most common source of errors for new agents

### Implications for Loom

If Synthweave Loom agents onboard through skills:
- Each Loom workflow could ship with an onboarding skill
- Skills become the interface contract between orchestrator and agent
- Agent capability discovery happens through skill manifests
- Testing an agent = testing whether it can follow a skill

This aligns with Goal #2c (skills as the universal agent interface).

## Conclusions

1. Skills as onboarding is a real pattern worth adopting
2. Our workspace needs a meta-onboarding skill (built as prototype)
3. The skill based approach reduces time to productivity for sub-agents
4. For Loom, skills should be the primary onboarding mechanism, not documentation
