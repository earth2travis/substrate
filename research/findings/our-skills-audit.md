---
title: Skills Audit Against Anthropic Guide
tags:
  - ai-agents
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/our-skills-audit.md
---

# Skills Audit Against Anthropic Guide
## Date: 2025-07-17

### Scoring: ✅ Good | ⚠️ Needs Work | ❌ Missing

| Skill | Frontmatter | Triggers | Structure | Progressive Disclosure | Score |
|-------|------------|----------|-----------|----------------------|-------|
| agent-soul-design | ✅ | ✅ Good triggers | ✅ Has references/, assets/ | ⚠️ Could split more to refs | 8/10 |
| calendar | ❌ Was missing! Fixed. | ⚠️ Added but needs real-world phrases | ✅ Has script | ⚠️ All in SKILL.md | 5/10 |
| evm-wallet | ✅ | ✅ Specific triggers | ✅ Has scripts/ | ⚠️ Unknown depth | 7/10 |
| openclaw-stability | ✅ | ✅ Good triggers | ✅ Has scripts/ | ⚠️ Unknown depth | 7/10 |
| web-search | ✅ | ⚠️ Too generic, starts with "This skill should be used" | ✅ Has scripts/ | ⚠️ Unknown depth | 6/10 |

### Key Findings

1. **calendar had no YAML frontmatter at all** — Claude couldn't auto-trigger it. Fixed.
2. **web-search description is weak** — "This skill should be used when..." is passive. Should be direct: "Search the web for information using DuckDuckGo. Use when..."
3. **No skill has testing** — Zero triggering tests, functional tests, or performance comparisons exist for any skill.
4. **No MCP Enhancement skills (Category 3)** — All our skills are Category 1 or 2. The Synthweave play is Category 3.

### Actions Taken
- [x] Fixed calendar SKILL.md — added proper YAML frontmatter
- [ ] Improve web-search description
- [ ] Add testing framework for skills
- [ ] Build first Category 3 skill (Synthweave MCP enhancement)
