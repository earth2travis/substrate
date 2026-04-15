---
title: "Figma Dev Mode + MCP Official Presentation"
date: 2026-04-01
source: https://www.youtube.com/watch?v=A4mqzgFbmjI
presenter: Jake (Developer Advocate, Figma)
type: research
tags: [figma, mcp, code-connect, dev-mode, design-systems]
---

# Figma Dev Mode + MCP: Official Presentation Notes

Official Figma presentation by Jake (Developer Advocate). Demonstrates the full design-to-code workflow using Dev Mode, Code Connect, and the Figma MCP server.

## Design System Abstractions in Figma

Figma organizes design intent through named abstractions:

**In Figma directly:**
- **Variables**: Design tokens that change between themes (colors, sizes, text values)
- **Components**: Reusable elements with component properties, existing in both Figma and code
- **Styles**: Composite tokens described by one idea (box shadow, text style)

**Implied in code, referenced in Figma:**
- Layout patterns (grid systems, flexbox, absolute positioning)
- Usage guidelines and naming conventions
- Content, state, and data schema

## Dev Mode

Dedicated space in Figma with developer perspective. Key features:

- **Inspect panel**: Code preview in CSS, React, etc. with selection colors categorized by application
- **Export options**: PNG, SVG, PDF, JPEG at configurable resolutions
- **Plugin ecosystem**: Jira integration, Tailwind codegen, others render directly in inspect panel
- **"Ready for Dev" workflow**: Designers mark sections as ready. Creates a timeline view for developers showing only handoff-ready work.
- **Figma AI layer audit**: When marking ready for dev, AI detects improvement opportunities (unnamed layers get auto-named). Ensures metadata quality before handoff.
- **Focus view**: Developers see only the section marked for dev, scoped and focused. Can toggle themes (e.g., dark mode preview).

## Code Connect (Two Versions)

### 1. Code Connect Snippets (Deep Integration)

Dynamic snippets showing the production code form of designed components inside Dev Mode.

**How it works:**
- Template files sit in the codebase alongside components
- Maps Figma component properties to code output
- Published via `npx figma connect publish`
- Renders recursively for nested components
- Links to GitHub source for each component
- Changes dynamically based on which component is selected

**Example structure:**
```
components/
  button/
    Button.tsx          # React component
    Button.css          # Styles
    Button.figma.tsx    # Code Connect template
```

The template maps Figma information to code output. Selecting a pricing card shows the flat component API. Selecting a nested text list or button shows their individual implementations.

### 2. Code Connect UI (NEW: Shallow but Wide)

Lower-lift alternative for connecting entire libraries quickly.

- Connect components to code from within Figma UI
- Authenticates with GitHub for searching code files
- Maps each component to its code definition
- Pulls in definition code for preview
- Auto-connects icon libraries
- **Key for agentic workflows**: establishes the component-to-file relationship that LLMs need

## Variable Code Syntax

Per-platform code syntax for variables:

- Supply different code representations for web, iOS, and Android
- Developers see exact code form when inspecting (e.g., `color-background-default-secondary-hover` instead of Figma's sentence-case name)
- This metadata flows to LLMs through the MCP server
- Handles aliasing and mode switching (light/dark) with inheritance visualization

## Figma MCP Server: The Five Tools

The MCP server (still in beta) provides these tools to LLMs:

| Tool | What it returns |
|---|---|
| **Get metadata** | High-level info for current selection: frames, instances, structure |
| **Get screenshot** | Visual image of the selection |
| **Get code connect map** | All relevant Code Connect snippets for the selection |
| **Get variable definitions** | Relevant variables in their code syntax form |
| **Get code** | React + Tailwind representation with variables and Code Connect embedded |

Token count estimation is shown in the MCP server section of Dev Mode, helping developers understand message size before sending to LLMs.

## The Full Workflow (Demonstrated Live)

Using VS Code + GitHub Copilot with Claude Sonnet 4:

1. Designer marks section as "Ready for Dev" (Figma AI audits layer names)
2. Developer selects section in Figma
3. Opens coding tool, prompts: "Implement my figma selection in demo.tsx"
4. Agent calls MCP tools in sequence:
   - Get metadata → understands structure
   - Get screenshot → sees visual design
   - Get code connect map → gets production component snippets
   - Get variable definitions → gets design tokens in code syntax
   - Get code → gets React/Tailwind representation
5. Agent implements using correct components, proper tokens, connected to data layer
6. Result: Production-grade UI matching the design system

**Key detail:** The presenter configured Copilot with specific instructions (like cursor rules) to follow this exact tool sequence whenever implementing from Figma. Workspace-level agent instructions are critical.

## Figma Make

Interactive prototyping within Figma:

- Paste designs and bring them to life
- Test states, interactions, toggles
- Uncover implied complexity (toggle behavior, current plan states, button text changes)
- Developers can access Make prototypes via MCP
- Workflow: design → explore in Make → simplify with annotations → hand off

## Annotations as Machine-Readable Design Intent

Annotations are the bridge between design intent and LLM understanding:

- **Content annotations**: "This FAQ content is stored in the CMS"
- **Property callouts**: Fill color, auto-layout direction, gaps, component variants
- **Rich text**: Bold, italic, headlines for structured context
- **Custom context**: Asset locations ("this image is in our brand-approved drive")

**Purpose:** Call out things that might get lost in design context, or provide information not otherwise visible. Annotations are machine-readable, making them critical for LLM-powered workflows.

## Best Practices (Official Figma Guidance)

1. **Design patterns are machine-readable.** Document and adopt patterns with modern dev tools in mind. More consistency = better LLM outcomes.

2. **Use MCP beyond UI generation.** Project planning ("help me plan implementing these screens"), auditing design tokens, checking component usage against codebase. The MCP server is an analysis tool, not just a code generator.

3. **Instruct your agents.** Provide workspace-level context (copilot instructions, cursor rules) about implementation details. Tell agents how to interpret Figma output. Don't set and forget.

4. **Annotate design intent.** Describe sequences and user experience, not just visuals. Annotations are the designer's contribution to LLM context quality.

## Resources

- **Simple Design System (SDS)**: [github.com/figma/sds](https://github.com/figma/sds). React + Figma library with Code Connect, Storybook, REST API examples for variable syncing. Stencil/web components/Vue/Angular versions by One North agency.
- **Figma Developers**: [figma.com/developers](https://figma.com/developers). MCP server docs, Code Connect setup, plugin APIs, REST APIs.

## Comparison: Figma MCP vs Stitch

| Aspect | Figma MCP | Google Stitch |
|---|---|---|
| **Purpose** | Translate human-designed Figma files to code | AI-generated design from prompts |
| **Input** | Existing Figma designs with design systems | Text prompts, screenshots, wireframes |
| **Output** | Production code using team's actual components | HTML/design that needs conversion |
| **Design system** | Uses your existing system via Code Connect | Creates its own via design.md |
| **Best for** | Production design-to-code with team consistency | Rapid prototyping, ideation, exploration |
| **Code quality** | High (uses actual codebase components) | Needs post-processing (React Component skill, shadcn skill) |

**They serve different stages:** Stitch for rapid ideation and exploration. Figma MCP for production handoff with full design system fidelity. Both are valuable. Neither replaces the other.
