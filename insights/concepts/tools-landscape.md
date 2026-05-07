---
title: "Tools Landscape: The MCP Ecosystem"
tags: [concept, tools, mcp, function-calling, agent-tools, protocols]
related:
- skills-as-portable-knowledge
- agent-tool-permissions
- agent-platform-ecosystem
- agent-native-operations
- protocol-as-coordination
- the-openclaw-lesson
source: research/findings/tools-landscape.md
---

# Tools Landscape: The MCP Ecosystem

## Thesis

MCP (Model Context Protocol) has become the industry standard for connecting LLMs to external tools and data. Anthropic created it, then donated it to the Agent AI Foundation. It solves the N×M integration problem: instead of every framework implementing every tool, each tool implements one protocol and every framework speaks it.

## Architecture

Three roles:
- **Hosts**: LLM applications (Claude Desktop, Hermes Agent, etc.)
- **Clients**: Connectors that manage protocol state
- **Servers**: Context and capability providers (file systems, databases, APIs)

Protocol: JSON-RPC 2.0 over stateful connections (moving to stateless in June 2026). Servers describe every tool with names, argument schemas, descriptions, and result formats.

## The Universal Loop

All frameworks converge on the same pattern:
1. Model receives messages + tool definitions
2. Model outputs tool call
3. Runtime executes tool
4. Result feeds back to model
5. Repeat until task complete

## The Permission Problem

The weakest area across the entire landscape is permission models. Current frameworks provide assignment-level permissions, not enforcement. What's needed: per-tool policies (read vs write vs execute), scope-based access, audit trails, and budget enforcement. This is where OpenClaw failed and where the next generation must succeed.

## Related

- [[skills-as-portable-knowledge]] — Skills as the instruction set for agent systems
- [[agent-tool-permissions]] — Permission models as the weakest link
- [[agent-platform-ecosystem]] — Platform comparison and architecture
- [[protocol-as-coordination]] — Protocols as coordination mechanisms
