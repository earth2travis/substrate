---
title: "Figma x Claude Code Live: Roundtrip Workflows with Figma MCP"
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/figma-x-claude-code-livestream.md
---

# Figma x Claude Code Live: Roundtrip Workflows with Figma MCP

**Source:** https://www.youtube.com/watch?v=R9mBpeiCMM0
**Speakers:** Brett (Designer Advocate, Figma), Tarek (Claude Code team, Anthropic)
**Date:** Late March / Early April 2026
**Extracted:** 2026-04-02

## Key Takeaways

### The Workflow Shift

The product development process is compressing. Roles are blending (designer, developer, PM). The cost from inspiration to prototype is collapsing, meaning ideas can start from anywhere, not just the design canvas.

Figma positions itself as the space for **divergent thinking and collaboration**. Brett uses the metaphor of "spotlight vs lantern mode": coding is spotlight (focused on the problem), design canvas is lantern (shining light in all dark corners to find inspiration).

### Source of Truth is Shifting

Not shifting to code. Shifting to **the system**: design, research, content, all inputs together. The system IS the context. MCP is the mechanism for delivering design context to agents.

### MCP as Round-Trip Pipeline

Pre-MCP: clear handoffs, describing changes, manually sending screenshots.
Post-MCP: agents traverse surfaces (code, canvas) while keeping context intact.

Core concept: **a single idea, manipulated on multiple surfaces.** Code and UI are both materials. MCP provides lossless translation between them. Claude understands at an abstract level ("what is the app you're trying to build?") then translates into different "languages" (React code, Figma structures).

### Figma MCP Capabilities

**Read capabilities** (existed earlier):
- Extract design context from Figma files
- Pull component structures, properties, variants

**Write capabilities** (newer, in beta):
- `generate_figma_design`: Initial tool. Gets layers from code onto Figma canvas. Limited.
- `use_figma`: New beta tool. Uses Figma's Plugin API directly to manipulate objects. Creates files, organizes frames/pages, manages variables. Also supports FigJam.
- Image generation/upload via MCP: **not yet available, in the works.**

### Installation (One Command)

```bash
claude plugin install figma
```

This initiates the MCP connection and installs foundational skills in one shot. Then authenticate via `/figma/mcp` in the Claude session.

### Skills Architecture

Skills give agents specialized knowledge that couldn't previously be codified beyond design systems or code.

**Foundational skill:** `figma-use` teaches agents how to interact with the Plugin API generally. Figma provides this as unopinionated platform access.

**Community skills build on top.** Example: `cc-figma-tokens` skill dramatically improved variable generation. Without it, Claude created one collection per JSON file. With it, Claude properly generated modes (dark/light) within collections.

**Key insight from Brett:** Skills are a new artifact type for the community. Like plugins, they're composable, shareable, and extensible.

**Skill creation approach (from Tarek):**
- Ask Claude to interview you about your design system using `ask_user_question` tool
- Claude builds the skill from your answers
- Add "gotcha" sections for consistent model mistakes

**Skill composition:** Can be small and composable (combined by Claude as needed) or larger monolithic ones. No prescriptive answer. Try both.

**Skill invocation:** Claude will try to infer when to use skills, but explicit invocation is more reliable. "The less Claude needs to infer from your intent, the better."

### Live Demo: Component Round-Trip

1. Tarek started Claude Code in his recipe box repo
2. Prompted: "Create the card component in Figma using the Figma MCP" with a link to shared Figma file
3. Claude created the component with variants, boolean toggles, all properties from the codebase
4. Brett made manual tweaks in Figma (hug height, rating adjustments)
5. Prompted Claude: "I've modified the card component in Figma. Can you update it in code to match?"
6. Claude read the Figma changes and updated the codebase

**Notable:** The component was architecturally correct with proper variant structure. Visual tweaks needed (badges too round, no images), but the structure was sound.

### Live Demo: Marketing Poster

Tarek prompted Claude to create a marketing poster for the app in Figma. Result was a usable first pass, editable and tweakable. Not just UI: graphic design, marketing assets, anything visual.

Key value: **solves the blank canvas problem.** Gives cross-functional partners something concrete to discuss and iterate on.

### Live Demo: State Explosion

Brett asked Claude to generate frames for each state of a login flow. Claude analyzed the code logic and generated all screens. Valuable for **legacy apps without Figma documentation** that need design iteration.

Claude self-annotated the output:
- Fidelity notes on canvas
- Which components it linked to from the library
- What it had to manually rebuild (no matching component)
- Known issues requiring manual cleanup

**Why didn't it fix the issues itself?** Tarek: Claude tries to balance initiative vs asking for approval. It's deliberately collaborative. You can adjust with prompting ("just run with it" vs "interview me").

### Live Demo: Design QA / Diff Comparison

Brett asked Claude to compare a Figma frame against the actual login screen and annotate differences. Claude:
- Generated an "as built" frame from code
- Annotated discrepancies with severity (high/medium/low)
- Flagged component overrides
- Dropped comments on the Figma frame (via REST API, not MCP, requiring a personal access token)

**Key moment:** Claude knew the comment API required a different auth method and prompted Brett to provide it. Agent as collaborator, knowing what it needs.

### Live Demo: Variable Generation from JSON

First attempt (no skill): Created one collection per JSON file. Incorrect structure.
Second attempt (with `cc-figma-tokens` skill): Properly generated collections with dark/light modes. Clear demonstration of skill value.

### Prompting Guidance

- Be specific. Ambiguity is the enemy.
- "Interview me" is a powerful prompt when you don't know what you want.
- "Implement this eight different ways" leverages cheap exploration.
- One or two words can completely change output.
- Each model generation behaves differently. Stay curious, keep experimenting.
- Giving more constraints sometimes backfires. Balance specificity with letting the model reason.

### Figma Canvas as Cheap Exploration

Brett's insight on token economics: Figma's canvas is cheap exploration (option-drag, duplicate, iterate) without spending tokens. When you associate cost to something, it becomes precious and harder to throw away. Knowing when to use agentic workflows vs traditional workflows is a critical skill.

### Collaboration Model

Claude Code is a "single player experience." Figma MCP makes it collaborative. Both people can edit the same Figma file while Claude operates on it.

For engineers: the bar for visual output rises. Marketing assets, prototypes, things that previously needed a designer for simple versions.

For designers: delegate tooling work (syncing, organizing, auditing, linting) to agents. Focus on deep creative work.

**Cross-functional advice:** Designers and engineers should collaborate on skill creation. A designer creating a skill that helps a PM land work in design language creates a flywheel.

### Practical Next Steps (from the speakers)

1. Install Figma MCP: `claude plugin install figma`
2. If you're a designer, work with an engineer who knows Claude Code
3. Explore community skills at Figma's community skill repository
4. Try hackathons / greenfield exploration time
5. Be curious, be efficient with token spend

## Relevance to Our Work

This directly validates the Figma MCP research we already have (`research/figma-claude-code/analysis.md`). New information:

- **`use_figma` tool confirmed as beta:** The Plugin API access we identified is live and being demoed publicly.
- **Skills are the differentiation layer:** The unopinionated platform access + opinionated skills on top maps exactly to our Context Stack architecture (Operations layer + Intelligence layer).
- **Variable/token generation is a real workflow:** The `cc-figma-tokens` skill example is directly relevant to Synthweave's design system bootstrap plan.
- **Design QA via agent is production-ready:** Comparing Figma to code implementation and annotating differences. This is a Synthweave product feature.
- **FigJam connectivity exists:** Opens whiteboarding/planning workflows.
- **Image support coming:** Current gap, but actively being worked on.

The "single idea, multiple surfaces" framing is exactly what Loom should enable. MCP as the lossless translation layer between surfaces. This livestream is a public proof point for the architecture we're building toward.
