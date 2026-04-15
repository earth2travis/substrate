---
title: "OpenClaw vs Hermes: Coding vs Research Analysis"
created: 2026-04-13
updated: 2026-04-13
type: comparison
tags: [model, comparison, evaluation]
sources:
  - raw/openclaw-vs-hermes-coding.md
---

# OpenClaw vs Hermes: Coding vs Research Analysis

## The Hypothesis

Tested claim: **OpenClaw = Better Coding Agent** while **Hermes = Better Research/Strategy Agent**.

## OpenClaw for Coding (Confirmed Strengths)

- **Massive coding skill ecosystem** -- 1200+ skills on ClawHub with entire "Coding Agents & IDEs" category
- **ACP protocol** -- Pioneered Agent Client Protocol for IDE-agent integration
- **Developer-first design** -- Strong terminal integration and coding workflows
- **Active developer community**

**What's overstated:** OpenClaw's coding skills were affected by ClawHavoc (341 malicious skills removed). The idea that it's the "undisputed" coding agent ignores Hermes' comparable terminal/file/code execution tools.

## Hermes for Research (Confirmed Strengths)

- **Genuine learning loop** -- Memory + autonomous skill creation + FTS5 session search = compound knowledge. Unique among agent platforms.
- **Deep research tooling** -- 40+ built-in tools including web search, document extraction, vision analysis
- **LLM Wiki integration** -- Karpathy-inspired wiki pattern for knowledge compounding
- **Structured knowledge management** -- Hierarchical wiki structure (raw → concepts → entities → comparisons)

**What's overstated:** Hermes isn't "only" good for research -- it has strong coding capabilities too. The learning loop doesn't automatically make Hermes better at all research tasks.

## Where the Hypothesis Falls Down

### Hermes is excellent at coding too
- `code_execution_tool.py` -- 53KB for programmatic code execution
- `file_tools.py` -- 39KB with fuzzy matching and patch
- 6 terminal backends (vs OpenClaw's more limited options)
- ACP adapter for IDE integration (VS Code, Zed, JetBrains)

### OpenClaw has grown strong research capabilities
- **Dreaming feature** -- Background memory consolidation for research synthesis
- **Academic research skills** -- OpenAlex API integration, paper search
- **Massive skill ecosystem** includes many research-focused skills
- **Enterprise features** -- Agent council, cost monitoring, audit trails

## The Real Differentiators

| Dimension | OpenClaw | Hermes |
|---|---|---|
| **Ecosystem approach** | Marketplace first (1200+ community skills) | Core functionality first (40+ built-in tools) |
| **Memory** | Dreaming (background consolidation, experimental) | Structured learning loop (memory, search, skill creation) |
| **Security** | Reactive (fixed 138 CVEs post-breach) | Proactive (designed secure from start) |
| **Philosophy** | "Let the community build it" | "Build the core, then let community extend" |

## Verdict

The real difference isn't "coding vs research" -- it's **ecosystem approach and memory architecture**. OpenClaw's marketplace model offers maximum customization through community skills. Hermes' core-first approach with genuine learning loop offers depth and compound growth. For [[harness-engineering]] workflows where security and reliability matter (agent-controlled infrastructure), Hermes' proactive security and structured memory are advantageous.

## See Also
- [[openclaw]] -- OpenClaw platform details
- [[hermes-agent]] -- Hermes platform details
- [[clawhavoc-security-crisis]] -- Security incident that differentiated the platforms
- [[nous-research]] -- Organization behind Hermes
