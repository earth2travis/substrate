---
title: "Skill Design Foundations"
tags: [research, skills, design, agents]
related: [skills-as-portable-knowledge, agent-native-operations, codex, kanban-doctrine]
source: "Research notes from February 14, 2026"
---

# Skill Design Foundations

## Summary

Research on skill design principles from the skill-creator ecosystem and agents.md community. Skills are for agents, not humans. The context window is a public good: only add what models don't already know.

## Key Concepts

**Three Core Principles:**
1. Concise is Key: challenge each piece with "Does this justify its token cost?"
2. Degrees of Freedom: match specificity to fragility (high freedom for text, medium for pseudocode, low for scripts)
3. Progressive Disclosure: metadata (~100 words) always loaded, body (<5k words) when triggered, bundled resources as needed

**Skill Anatomy:**
```
skill-name/
├── SKILL.md (required: YAML frontmatter + Markdown instructions)
└── Bundled Resources (optional)
    ├── scripts/      # Deterministic code
    ├── references/   # Docs loaded as needed
    └── assets/       # Files used in output
```

**Frontmatter is Critical:**
The `description` field is the primary trigger. Must include what the skill does AND when to use it. All "when to use" info belongs in description because the body loads AFTER triggering.

**What NOT to Include:**
README.md, INSTALLATION_GUIDE.md, CHANGELOG.md. Skills are for agents.

**Good Skill Candidates (3+ criteria met):**
- Repeated use (High)
- Domain expertise not in base model (High)
- Fragile operations (Medium)
- Script-able (Medium)
- Shareable (Low)

**Emerging Patterns:**
- Directory as Context: `.agent/` directory with spec/, wiki/, links/
- Domain-specific organization: references/ sorted by domain (finance.md, sales.md, product.md)

## Applications

Skills give agents specialized knowledge that couldn't previously be codified beyond design systems or code. The unopinionated platform access + opinionated community skills on top maps to Context Stack architecture (operations + intelligence layers). [[skills-as-portable-knowledge]] [[agent-native-operations]] [[codex]]
