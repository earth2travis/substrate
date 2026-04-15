# Tools Landscape for Agentic Systems (March 2026)

## MCP: The Protocol That Won

Model Context Protocol (MCP) is now the standard for connecting LLMs to external tools and data. Anthropic created it, then donated it to the Agent AI Foundation (with OpenAI, Block, and dozens of others contributing $100k+/year each). This is no longer Anthropic's protocol. It's the industry's.

### Architecture

MCP uses JSON-RPC 2.0 over stateful connections (though moving to stateless in June 2026 spec).

**Three roles:**
- **Hosts**: LLM applications that initiate connections (Claude, ChatGPT, IDEs)
- **Clients**: Connectors within the host application
- **Servers**: Services that provide context and capabilities

**Server capabilities (what servers offer to clients):**
- **Resources**: Context and data (files, database records, API responses)
- **Prompts**: Templated messages and workflows
- **Tools**: Functions for the AI model to execute

**Client capabilities (what clients offer to servers):**
- **Sampling**: Server-initiated LLM calls (bidirectional; now supports tool calling as of Nov 2025 spec)
- **Roots**: Server queries about filesystem/URI boundaries
- **Elicitation**: Server requests for additional user input

### What's Coming

**Stateless MCP (June 2026 target):** The steering committee is moving to remove the initialize handshake. Metadata moves to per-request headers. This simplifies hosting dramatically: "we'll host your MCP server" becomes much closer to standard REST. Adoption will trail through end of 2026.

**MCP Apps:** Standardizing a pattern where MCP servers are full applications (not just tool providers). Already adopted by Goose, Postman before formal spec.

**OAuth 2.1 auth:** The Nov 2025 spec added proper authorization via Protected Resource Metadata discovery and OpenID Connect. Remote servers over HTTPS now have standardized auth.

### MCP's Real Value

MCP solves the N×M integration problem. Without it, every LLM application needs custom integrations for every service. With it, a service implements one MCP server and every MCP-compatible host can use it.

The killer feature is **tool discovery at runtime**. MCP servers describe every tool with names, argument schemas, descriptions, and result formats. The client loads this metadata into context so the model knows what's available without hardcoding.

### MCP's Limitations

- **Context window cost**: Every tool description eats tokens. With many MCP servers connected, tool descriptions alone can consume significant context
- **Security surface**: Tools represent arbitrary code execution. The protocol provides guidelines but can't enforce safety at the protocol level
- **Stateful complexity** (being addressed): Current stateful connections are harder to scale than stateless APIs
- **No built-in tool composition**: MCP tools are individual functions. Composing them into workflows requires external orchestration (which is where Skills come in)

## Function Calling Across Frameworks

### The Universal Pattern

Every framework converges on the same basic loop:

1. Model receives messages + tool definitions (JSON Schema)
2. Model outputs a tool call (function name + arguments)
3. Runtime executes the function
4. Result feeds back to model
5. Repeat until model produces a final response

The differences are in how tool definitions are provisioned and how execution is managed.

### Framework-Specific Approaches

**OpenAI (Assistants/Swarm):**
- Tools defined as JSON Schema in assistant configuration
- Built-in tools: code_interpreter, file_search, function
- Parallel function calling supported
- Tool choice: auto, required, none, or specific function
- Limitation: tools tied to OpenAI's ecosystem

**Anthropic (Claude):**
- Tools via API `tools` parameter with JSON Schema
- MCP for dynamic tool provisioning
- Skills for workflow-level tool orchestration
- Computer use (screen interaction) as a tool type
- Cache-friendly: tool definitions can use prompt caching

**LangGraph:**
- Tools are Python functions with type annotations
- `@tool` decorator converts functions to LangChain tools
- Tool nodes handle execution, can be customized
- Tools can be dynamically added/removed from agent state
- MCP integration via langchain-mcp adapters

**CrewAI:**
- Tools defined as classes with `_run` methods
- Built-in tools for web scraping, file operations, search
- Custom tools via `@tool` decorator
- Tools assigned per-agent (permission model by assignment)
- Less flexible than LangGraph but simpler

**AutoGen:**
- Tools registered on agents via `register_for_llm` / `register_for_execution`
- Separation of "who can call" vs "who executes" (useful for sandboxing)
- Docker execution environments for code tools

### What Actually Matters

The tool definition format (JSON Schema) is converging. The real differentiators are:

1. **Dynamic discovery** (MCP wins): Runtime tool availability vs compile-time definitions
2. **Execution isolation** (AutoGen leads): Sandboxed execution environments
3. **Permission models** (everyone is weak): Who can call what, with what limits

## Tool Composition

No framework handles tool composition well. The patterns that exist:

**Sequential chaining:** Output of tool A feeds into tool B. Every framework supports this implicitly through the conversation loop. Not explicit composition.

**Workflow tools:** A "tool" that internally calls other tools in sequence. CrewAI tasks and LangGraph subgraphs approximate this. Skills formalize it.

**MCP Sampling:** An MCP server can request LLM calls from the client, enabling server-side orchestration of multi-step tool workflows. This is the most promising primitive for tool composition, but it's new and underexplored.

**The gap:** There's no standard way to say "tool C = tool A then tool B with these transformations." Skills are the closest thing, but they operate at the instruction level (telling the model how to compose tools) rather than the runtime level (actually composing function calls).

## Permission Models

This is the weakest area across the entire landscape.

**Current state:**
- MCP: "Hosts MUST obtain explicit user consent before invoking any tool." Guidelines, not enforcement.
- OpenAI: Tool-level permissions in Assistants. Blanket approval patterns in practice.
- LangGraph: Human-in-the-loop interrupt nodes before tool execution. Most granular control available.
- CrewAI: Tools assigned to agents. No finer-grained permissions.
- AutoGen: Separation of call authorization vs execution. Closest to a real permission model.

**What's needed:**
1. **Per-tool permission policies**: Read vs write vs execute. Rate limits. Cost caps.
2. **Scope-based access**: Agent A can use tools X, Y but not Z. Current frameworks do assignment but not enforcement.
3. **Audit trails**: What was called, with what arguments, by which agent, with what result. LangSmith provides this for LangGraph. Others are ad hoc.
4. **Budget enforcement**: "This agent can spend at most $5 in tool calls." Nobody implements this well.

## What Synthweave/Loom Should Use

### MCP as the tool layer

MCP is the obvious choice for tool provisioning. It's the standard. It has momentum. It handles discovery, schema, and execution. Build MCP servers for our capabilities.

### Skills for tool orchestration

MCP gives you individual tools. Skills tell the agent how to use them together. This is the right separation: MCP for "what can I do," Skills for "how should I do it."

### Permission model from scratch

Nobody has solved this. We should build:
- Tool-level policies (read/write/execute permissions per agent)
- Budget caps (token and dollar limits per agent per task)
- Audit logging (every tool call recorded with full context)
- Scope inheritance (sub-agents inherit parent's permissions minus any restrictions)

### Stateless MCP preparation

The June 2026 stateless spec is the future. Design our MCP integrations to be stateless-ready. Don't depend on connection state.

### Skip framework-specific tool abstractions

Don't use LangChain's `@tool` decorator or CrewAI's tool classes. Use MCP servers directly. The framework abstractions add indirection without value when MCP already provides discovery and schema.
