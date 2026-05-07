---
title: "Tools Landscape: MCP and Function Calling Across Frameworks"
tags: [tools, mcp, function-calling, agent-tools, protocols]
related: [[skills-landscape]], [[workflows-landscape]], [[cloudflare-first-agent-factory]], [[agent-native-operations]], [[the-openclaw-lesson]], [[agent-tool-permissions]]
source: research/raw/tools-landscape.md
---

# Tools Landscape: MCP and Function Calling Across Frameworks

## Summary

MCP is now the industry standard for connecting LLMs to external tools and data. Anthropic created it, then donated it to the Agent AI Foundation. It uses JSON-RPC 2.0 over stateful connections, moving to stateless in June 2026. Three roles: Hosts (LLM applications), Clients (connectors), Servers (context/capability providers).

MCP's real value is solving the N×M integration problem and enabling tool discovery at runtime. Servers describe every tool with names, argument schemas, descriptions, and result formats. The client loads this metadata into context so the model knows what is available without hardcoding.

Limitations: context window cost from tool descriptions, security surface from arbitrary code execution, stateful complexity (being addressed), and no built-in tool composition. Frameworks converge on the same universal loop (model receives messages + tool definitions → outputs tool call → runtime executes → result feeds back → repeat).

The weakest area across the entire landscape is permission models. Current frameworks only provide assignment-level permissions, not enforcement. What's needed: per-tool policies (read vs write vs execute), scope-based access, audit trails, and budget enforcement.
