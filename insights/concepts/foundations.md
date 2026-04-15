---
title: Skill Design Foundations
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/foundations.md
---

# Skill Design Foundations

_Research notes from February 14, 2026_

---

## Core Principles (from skill-creator)

### 1. Concise is Key

The context window is a public good. Only add what models don't already know.

**Challenge each piece:** "Does this justify its token cost?"

### 2. Degrees of Freedom

Match specificity to fragility:

- **High freedom** (text): Multiple valid approaches
- **Medium freedom** (pseudocode): Preferred patterns exist
- **Low freedom** (scripts): Fragile, consistency critical

### 3. Progressive Disclosure

Three-level loading:

1. **Metadata** (~100 words): Always loaded, triggers skill
2. **SKILL.md body** (<5k words): Loaded when triggered
3. **Bundled resources** (unlimited): Loaded as needed

---

## Anatomy of a Skill

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/      # Deterministic code
    ├── references/   # Docs loaded as needed
    └── assets/       # Files used in output
```

### Frontmatter is Critical

The `description` field is the primary trigger. Include:

- What the skill does
- When to use it (specific triggers)
- All "when to use" info (body is loaded AFTER triggering)

---

## What NOT to Include

- README.md
- INSTALLATION_GUIDE.md
- CHANGELOG.md
- Any auxiliary documentation

Skills are for agents, not humans.

---

## Emerging Patterns

### Directory as Context (agents.md #71)

Proposal for `.agent/` directory standard:

```
.agent/
├── spec/       # Requirements, design, tasks
├── wiki/       # Architecture, domain knowledge
└── links/      # External resource URIs
```

Interesting for project-level context, not individual skills.

### Domain-Specific Organization

For skills with multiple domains, organize by domain:

```
bigquery-skill/
└── references/
    ├── finance.md
    ├── sales.md
    └── product.md
```

Load only relevant domain when needed.

---

## Identifying Good Skill Candidates

| Criterion                            | Weight |
| ------------------------------------ | ------ |
| Repeated use                         | High   |
| Domain expertise (not in base model) | High   |
| Fragile operations                   | Medium |
| Script-able                          | Medium |
| Shareable                            | Low    |

If 3+ criteria are met, likely a good skill.

---

## Sources

- [[OpenClaw]] skill-creator SKILL.md
- agents.md issue #71 (Directory as Context)
- Medium: "Organizing Files for Agentic AI Systems"

---

## Next Research

- [ ] Study ClawHub top skills for patterns
- [ ] agents.md community discussions
- [ ] Multi-agent skill coordination
