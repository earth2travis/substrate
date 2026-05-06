---
title: "Skills as Portable Knowledge"
tags: [concept, skills, mcp, agent-tools, progressive-disclosure, composability]
related: [[skills-landscape]], [[tools-landscape]], [[workflows-landscape]], [[our-skills-audit]], [[mak-prompt-engineering-skills]], [[gstack-analysis]], [[paperclip-patterns-worth-adopting-for-synthweave]], [[agent-native-operations]], [[harness-engineering]], [[the-openclaw-lesson]], [[context-stack]], [[agent-memory]]
source: insights/concepts/skills-as-portable-knowledge.md
---

# Skills as Portable Knowledge

## Thesis

Skills are becoming the instruction set for agent systems. Anthropic formalized them in October 2025, OpenAI adopted the same format for Codex by December, and the Agent AI Foundation now lists Skills alongside MCP and agents.md as founding sibling projects. The skill is the unit of portable, versionable, composable procedural knowledge.

## The Progressive Disclosure Pattern

The reference implementation uses three loading levels: YAML frontmatter (always in context, under 1024 chars), SKILL.md body (loaded when relevant), and linked files (discovered as needed). This is genuinely good engineering: most skills are invisible most of the time. Only the trigger description occupies permanent context space.

This maps directly to the principle of writing for the reader six months from now. The frontmatter is the index entry, the body is the full text, the references are the appendices. A well-designed skill is a well-designed knowledge node.

## Three Categories

1. **Document and Asset Creation**: Style guides, templates, quality checklists. No external tools needed.
2. **Workflow Automation**: Multi-step processes with validation gates and iterative refinement.
3. **MCP Enhancement**: Orchestrates multiple MCP tool calls with domain expertise and error handling.

Category 3 is where Skills and MCP intersect. The skill provides the workflow logic (do A, check B, if C then D), and MCP provides the tool execution (here is how to actually do A). This is the pattern that matters for Synthweave.

## Composability Over Monoliths

Mak's prompt engineering skills demonstrate the canonical pipeline: Create → Test → Fix → Re-test → Benchmark → Ship. Each skill does one thing. Their outputs are each other's inputs. prompt-creator doesn't test. prompt-tester doesn't create. model-benchmarker doesn't modify. Together they form a self-improving loop.

The implication: design skills with explicit input/output contracts. A skill's output should be directly usable as another skill's input. This is the same principle that makes Unix pipes powerful.

## What Is Still Missing

No formal registry or marketplace exists. Discovery is manual (zip files, folder drops). No runtime verification: skills are instructions, not contracts. The model might not follow them perfectly. Trigger precision requires careful prompt engineering. No inter-skill coordination exists beyond coexistence.

The next evolution will add runtime contracts: required tools, preconditions, postconditions, token budget estimates. Skills will become more like functions and less like documentation.

## Connection to Our Stack

Skills are the bridge between tools and workflows in our three-layer architecture: MCP servers provide capabilities, Skills encode how to orchestrate those capabilities, and Workflow orchestration manages when skills get activated. This cleanly separates concerns and lets each layer evolve independently.

The context-stack and agent-memory systems enable skills to persist their learning across sessions. A skill that improves itself session-over-session is practicing kaizen.
