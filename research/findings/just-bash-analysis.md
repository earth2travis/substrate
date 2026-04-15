---
title: "just-bash: Virtual Shell Analysis for Agent Execution"
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/just-bash-analysis.md
---

# just-bash: Virtual Shell Analysis for Agent Execution

**Source:** [github.com/vercel-labs/just-bash](https://github.com/vercel-labs/just-bash)
**Status:** Beta (Apache-2.0)
**Filed:** 2026-03-17
**Issue:** #406

## 1. Overview and Architecture

just-bash is a TypeScript implementation of a bash interpreter with an in-memory virtual filesystem. It parses bash scripts into an AST and interprets them entirely in JavaScript/TypeScript, never spawning real child processes. The execution pipeline:

```
Input → Parser (Lexer → Tokens → AST) → Interpreter → Output
```

### Core Design

Each `Bash` instance encapsulates:
- A virtual filesystem (pluggable: InMemoryFs, OverlayFs, ReadWriteFs, MountableFs)
- A command registry (~79 built-in commands reimplemented in TypeScript)
- Interpreter state (env vars via `Map<string, string>`, cwd, functions, shell options)
- Execution limits (loop iterations, call depth, command count, string length)
- Optional defense-in-depth (monkey-patching dangerous JS globals during execution)

Each `exec()` call gets an **isolated shell state**: env vars, functions, and cwd reset between calls. The **filesystem is shared** across calls, so files written in one `exec()` are visible in the next. This is the key design decision: state isolation per call, persistence via filesystem.

```typescript
import { Bash } from "just-bash";

const bash = new Bash({
  files: { "/data/file.txt": "content" },
  env: { MY_VAR: "value" },
  cwd: "/app",
  executionLimits: { maxCommandCount: 10000 },
});

const result = await bash.exec('echo "Hello" > greeting.txt');
// result: { stdout: "", stderr: "", exitCode: 0, env: {...} }
```

### Command Implementation

All ~79 commands are reimplemented in TypeScript: `cat`, `grep`, `sed`, `awk`, `jq`, `find`, `curl`, `sqlite3`, `python3`, `js-exec`, etc. Each command receives a `CommandContext` with access to `fs`, `cwd`, `env`, `stdin`, `exec` (for subcommands), and `fetch` (for network). Commands are registered lazily and can be restricted:

```typescript
const bash = new Bash({
  commands: ["cat", "grep", "echo", "ls"], // Only these commands available
});
```

### Filesystem Architecture

Four filesystem implementations, all conforming to `IFileSystem`:

| Implementation | Reads From | Writes To | Use Case |
|---|---|---|---|
| **InMemoryFs** (default) | Memory | Memory | Pure sandbox, no disk access |
| **OverlayFs** | Real disk (read-only) | Memory (copy-on-write) | Explore real codebases safely |
| **ReadWriteFs** | Real disk | Real disk | Agent needs real file access |
| **MountableFs** | Mixed (per mount) | Mixed (per mount) | Compose read-only + read-write zones |

InMemoryFs supports lazy file loading, including async providers:

```typescript
const bash = new Bash({
  files: {
    "/data/config.json": '{"key": "value"}',
    "/data/large.csv": () => "col1,col2\na,b\n",           // lazy, sync
    "/data/remote.txt": async () => (await fetch(url)).text(), // lazy, async
  },
});
```

### Browser Support

The core (parser, interpreter, InMemoryFs, all built-in commands) runs in browsers. Node-only features: `python3`, `sqlite3`, `js-exec`, OverlayFs, ReadWriteFs.

### Package Details

Published as `just-bash` on npm. Companion package `bash-tool` wraps it as an AI SDK tool. Also provides a `Sandbox` class that's API-compatible with `@vercel/sandbox` (Vercel's real VM sandbox) for development/testing.

## 2. Security Model

### Trust Boundaries

The threat model is thorough and well-documented in `THREAT_MODEL.md`. The primary threat actor is an **untrusted script author** (AI agent or user) with ZERO trust. The model explicitly trusts:
- The host application (fs, fetch, customCommands, plugins)
- Node.js runtime and OS
- npm dependencies (supply chain is out of scope for runtime)

### Defense Layers

**Primary defenses (high bypass difficulty):**
- **Architecture**: No `child_process` import anywhere. No code path from bash interpretation to JS code execution.
- **Filesystem**: Path normalization + root containment via `isPathWithinRoot()`. Symlinks default-denied.
- **Network**: Disabled by default. URL prefix allow-list with per-redirect validation. Header transforms for credential injection (secrets never enter the sandbox).
- **Command registry**: Only registered TypeScript implementations run. No arbitrary binary execution.
- **Execution limits**: Enforced at every loop, call, expansion, glob, string operation.
- **Prototype pollution guards**: `Map<string, string>` for env, `Object.create(null)` for data objects, `DANGEROUS_KEYS` set for JQ.
- **Parser limits**: Token count (100K), depth (200), input size (1MB), iteration count (1M).
- **re2js regex engine**: Linear-time guarantee, no catastrophic backtracking.

**Secondary defenses (defense-in-depth, medium bypass difficulty):**
- Monkey-patching of `Function`, `eval`, `setTimeout`, `process.*`, `WebAssembly`, `Proxy`, etc. via `AsyncLocalStorage` context-aware proxies.
- ESM loader hooks block `data:` and `blob:` URL imports (Node.js 20.6+).
- Error sanitization strips host paths from all error messages.
- Virtual process info (PID=1, UID=1000) instead of real values.

### Key Security Properties

1. **No network by default.** `curl` command doesn't even register without `network` config.
2. **No Python/JS by default.** Both are opt-in due to additional attack surface.
3. **No real process spawning.** Everything is interpreted in-process.
4. **No real filesystem access by default.** InMemoryFs touches nothing on disk.
5. **Configurable execution limits** prevent infinite loops, memory exhaustion, regex DoS.

### Known Gaps (Honest Assessment)

- **No VM isolation.** Runs in the same V8 context as the host. Defense-in-depth is secondary.
- **Python (when enabled) has MEDIUM risk.** CPython WASM with isolation by construction (no JS bridge), but still arbitrary Python execution.
- **No total memory ceiling.** Per-object limits exist (10MB strings, 100K array elements) but no aggregate memory tracking per `exec()`.
- **Signal/job control** not fully tested.

### Verdict on Security

For AI agent use cases where the agent is generating bash scripts: this is a well-thought-out security model. It's not a full VM sandbox (they explicitly recommend Vercel Sandbox for that), but the layered defenses are comprehensive. The threat model is unusually thorough for an open-source project.

## 3. Agent Usage Patterns

### From agent-examples/

The test suite in `src/agent-examples/` demonstrates canonical agent workflows:

1. **Codebase Exploration**: Agent creates a Bash instance with a pre-loaded project filesystem, then runs `ls`, `cat`, `grep -r`, `find` to understand structure.
2. **Feature Implementation**: Agent reads existing code, identifies TODOs, modifies files, runs verification commands.
3. **Security Audit**: Agent searches for vulnerability patterns using `grep`.
4. **Code Review / Refactoring / Migration**: Multi-file operations using `sed`, `awk`, `find | xargs`.
5. **Log Analysis / Text Processing**: Data pipeline workflows using pipes.
6. **Dependency Analysis**: Parsing `package.json` with `jq`.
7. **Bug Investigation / Debugging**: Exploring logs and code to find issues.

### From examples/bash-agent/

A complete working example of an AI agent using just-bash with the AI SDK:

```typescript
// Creates an OverlayFs over a real directory (read-only)
const overlayFs = new OverlayFs({
  root: projectRoot,
  mountPoint: "/workspace",
  readOnly: true,
});

const bash = new Bash({ fs: overlayFs, cwd: "/workspace" });

// Wraps as AI SDK tool
const toolkit = await createBashTool({
  sandbox: bash,
  destination: "/workspace",
  extraInstructions: `Use bash commands to explore...`,
});

// Used in streamText with Claude
const result = streamText({
  model: "anthropic/claude-haiku-4.5",
  tools: { bash: toolkit.bash },
  messages: history,
});
```

### Key Pattern: Custom Commands as Agent Tools

The most architecturally significant pattern: custom commands become the bridge between the sandbox and the outside world.

```typescript
const searchWeb = defineCommand("search-web", async (args, ctx) => {
  const query = args.join(" ");
  const results = await externalSearchAPI(query); // Host-controlled
  return { stdout: JSON.stringify(results), stderr: "", exitCode: 0 };
});

const bash = new Bash({ customCommands: [searchWeb] });
await bash.exec('search-web "typescript best practices" | jq .results[]');
```

Custom commands:
- Receive full `CommandContext` (fs, cwd, env, stdin, exec for subcommands)
- Work with pipes, redirections, and all shell features
- Are marked `trusted: true` by default (run inside `DefenseInDepthBox.runTrustedAsync()`)
- Can be lazy-loaded for code splitting
- Take precedence over built-ins with the same name

## 4. Custom Command System Deep Dive

The custom command API is the most important feature for our use case. Here's how it works internally:

### Definition

```typescript
export function defineCommand(
  name: string,
  execute: (args: string[], ctx: CommandContext) => Promise<ExecResult>,
): Command {
  return { name, trusted: true, execute };
}
```

### CommandContext Interface

```typescript
interface CommandContext {
  fs: IFileSystem;           // Virtual filesystem
  cwd: string;               // Current working directory
  env: Map<string, string>;  // Environment variables (Map for prototype safety)
  stdin: string;             // Standard input content
  limits?: Required<ExecutionLimits>;
  exec?: (command: string, options: CommandExecOptions) => Promise<ExecResult>;
  fetch?: SecureFetch;       // Only if network configured
  signal?: AbortSignal;      // Cooperative cancellation
  // ... more fields
}
```

### Registration

Custom commands register after built-ins, so they can override. Registration creates stubs in `/bin` and `/usr/bin` for PATH resolution:

```typescript
registerCommand(command: Command): void {
  this.commands.set(command.name, command);
  fs.writeFileSync(`/bin/${command.name}`, stub);
  fs.writeFileSync(`/usr/bin/${command.name}`, stub);
}
```

### Trusted vs Untrusted

Commands marked `trusted: true` run inside `DefenseInDepthBox.runTrustedAsync()`, meaning they can access Node.js globals that are normally blocked. This is intentional: custom commands are host-provided and trusted, while the bash script calling them is untrusted.

### Lazy Loading

```typescript
const heavy = { name: "heavy", load: () => import("./heavy-cmd.js") };
const bash = new Bash({ customCommands: [heavy] }); // Only loaded on first use
```

### Integration with Shell Features

Custom commands participate fully in the shell:

```bash
# Pipes work
echo "input data" | my-command | grep pattern

# Redirections work
my-command > output.txt 2> errors.txt

# Command substitution works
result=$(my-command --flag)

# Conditionals work
if my-command; then echo "success"; fi

# xargs/find integration works
find . -name "*.ts" | xargs my-command
```

## 5. Loom Integration Analysis

### Could just-bash Be the Execution Sandbox for Loom Agents?

**Short answer: No for the primary Loom use case, but yes for a complementary role.**

Loom agents need to:
1. Run `git clone`, `git push`, `npm install`, `npm test` (real OS operations)
2. Execute `gh pr create` (real CLI tool)
3. Write real files to disk (for PRs)
4. Run arbitrary test suites

just-bash cannot do any of these. It's a virtual environment. The commands are TypeScript reimplementations, not real binaries. `git` doesn't exist. `npm` doesn't exist. Test runners don't exist.

**However**, just-bash could serve as a **sandboxed pre-execution environment** for:
- Script validation before running on real OS
- Data processing tasks within agent workflows
- Isolated code analysis (grep, awk, jq on codebase snapshots)
- Tool mediation layer (custom commands as controlled interfaces)

### Custom Command API → Loom Tool Provisioning Contract

The Loom spec's `tools` section (§10) defines declarative tool provisioning. just-bash's custom command system maps cleanly:

| Loom Concept | just-bash Equivalent |
|---|---|
| Tool declaration in WORKFLOW.md | `customCommands` array in `BashOptions` |
| MCP server connection | Custom command wrapping MCP client |
| CLI tool availability check | Command present in registry |
| File injection | `files` option in `BashOptions` |
| Least privilege | `commands` option restricts available built-ins |

**Specific mapping for MCP tools:**

```typescript
// Each Synthweave MCP tool becomes a custom command
const snipSearch = defineCommand("snip-search", async (args, ctx) => {
  const query = args.join(" ");
  const results = await synthweaveMcpClient.call("snip_search", { query });
  return { stdout: JSON.stringify(results, null, 2), stderr: "", exitCode: 0 };
});

const reportProgress = defineCommand("report-progress", async (args, ctx) => {
  const [status, ...rest] = args;
  await synthweaveMcpClient.call("report_progress", {
    issue_id: ctx.env.get("ISSUE_ID"),
    status,
    summary: rest.join(" "),
  });
  return { stdout: "Progress reported.\n", stderr: "", exitCode: 0 };
});
```

### Per-Agent Scoped Instances

Each agent in a Loom orchestration could get its own just-bash instance with scoped commands. This maps to the "least privilege" principle in §10.1:

```typescript
// Security auditor agent: only gets read + analysis commands
const auditorBash = new Bash({
  commands: ["cat", "grep", "find", "awk", "jq", "diff"],
  customCommands: [snipSearch, createSnip],
  fs: new OverlayFs({ root: workspacePath, readOnly: true }),
});

// Implementation agent: gets write access + more tools
const implBash = new Bash({
  customCommands: [snipSearch, createSnip, reportProgress, ghPrCreate],
  fs: new ReadWriteFs({ root: workspacePath }),
  network: { allowedUrlPrefixes: ["https://api.github.com"] },
});
```

### Recommended Loom Spec Changes

1. **Add `sandbox` option to `agent` config** (§5.3.5):
   ```yaml
   agent:
     sandbox:
       engine: just-bash | native | vercel-sandbox
       commands: [cat, grep, find, jq]  # built-in restriction
       network:
         allowed_prefixes: [...]
   ```
   This would allow Loom to optionally run agents in a virtual environment instead of (or alongside) real OS access.

2. **Extend `tools.mcp` with `expose_as` field** (§5.3.7):
   ```yaml
   tools:
     mcp:
       - name: synthweave
         url: $SYNTHWEAVE_MCP_URL
         expose_as: shell_commands  # Expose MCP tools as shell commands
   ```
   This enables the custom command bridge pattern.

3. **Add `tools.sandbox_commands` section** for custom command definitions:
   ```yaml
   tools:
     sandbox_commands:
       - name: validate-schema
         module: ./tools/validate-schema.ts
         trusted: true
   ```

4. **Consider a hybrid execution model** where data processing runs in just-bash and system operations (git, npm, test runners) run on the real OS. The `MountableFs` composability makes this viable:
   ```typescript
   const fs = new MountableFs({ base: new InMemoryFs() });
   fs.mount("/workspace", new OverlayFs({ root: realWorkspace }));
   fs.mount("/scratch", new InMemoryFs()); // Agent temp space
   ```

## 6. Agent Factory Connection

### just-bash as Provisioning Primitive

The institutional-ai-vs-individual-ai analysis identifies a key insight: "organizations need help encoding their processes in agents." just-bash's architecture maps directly to this:

**Agent Instance = Bash Instance.** Each agent gets a sandboxed environment with:
- A specific filesystem view (what it can see)
- A specific command set (what it can do)
- Specific network access (what it can reach)
- Specific custom commands (what tools it has)

This is exactly the "tool injection per agent role" pattern:

```typescript
// The Factory produces role-specific agents
function createAgent(role: "auditor" | "implementer" | "reviewer") {
  const commands = ROLE_COMMANDS[role];       // Role-specific built-ins
  const custom = ROLE_CUSTOM_COMMANDS[role];  // Role-specific tools
  const fsConfig = ROLE_FS[role];             // Role-specific filesystem view
  const netConfig = ROLE_NETWORK[role];       // Role-specific network access
  
  return new Bash({
    commands,
    customCommands: custom,
    fs: fsConfig,
    network: netConfig,
  });
}
```

### Institutional Intelligence Layer Connection

The article's "Coordination vs Chaos" differentiator maps to just-bash + Loom:

| Individual AI (Chaos) | Institutional AI (Coordination) |
|---|---|
| Each agent gets full OS access | Each agent gets scoped just-bash instance |
| Agents share nothing | Agents share filesystem via MountableFs |
| No visibility into agent actions | Custom commands log all tool invocations |
| Agents can do anything | Agents can only use provisioned commands |

The "Deterministic vs Nondeterministic" differentiator also applies: just-bash's execution limits and sandboxing make agent behavior more predictable. An agent can't accidentally `rm -rf /`, install rogue packages, or exfiltrate data through unexpected channels.

### Custom Commands as Process Engineering

The article's insight about "process engineering" as the most important near-term technology: custom commands ARE process engineering. They encode organizational processes:

```typescript
// Encodes: "Every PR must pass schema validation"
const validateSchema = defineCommand("validate-schema", async (args, ctx) => {
  const schema = await ctx.fs.readFile("/schemas/" + args[0]);
  const data = ctx.stdin;
  // ... validation logic ...
});

// Encodes: "Decisions must be documented in Synthweave"
const documentDecision = defineCommand("document-decision", async (args, ctx) => {
  const [type, ...description] = args;
  await synthweave.createSnip({
    title: `Decision: ${description.join(" ")}`,
    tags: ["decision", type],
    content: ctx.stdin || description.join(" "),
  });
  return { stdout: "Decision documented.\n", stderr: "", exitCode: 0 };
});
```

## 7. Current Approach Comparison

### What We Have Now (OpenClaw exec)

- Real OS shell access via `exec` tool
- Full access to `git`, `gh`, `npm`, `node`, `python`, all system tools
- Real filesystem, real network, real processes
- Safety via OpenClaw's permission model (deny/allowlist/full)
- No isolation between exec calls (shared OS state)

### What just-bash Gives Us That We Don't Have

| Capability | OpenClaw exec | just-bash |
|---|---|---|
| **Per-agent isolation** | Shared OS | Isolated per-instance |
| **Filesystem sandboxing** | Real FS (dangerous) | Virtual FS (safe by default) |
| **Command restriction** | Allowlist at OpenClaw level | Per-instance command registry |
| **Tool injection** | N/A | Custom commands with full context |
| **Browser execution** | Not possible | Core works in browsers |
| **Execution limits** | Process-level timeouts | Granular (loops, depth, strings, output) |
| **Deterministic replay** | No (real OS state) | Yes (InMemoryFs is reproducible) |
| **Prototype pollution safety** | N/A | Built-in (Maps, null-prototype objects) |
| **Network control** | System-level firewall | Per-instance URL allow-list with header transforms |
| **Credential injection** | Environment variables | Header transforms (secrets never enter sandbox) |

### What We Lose

| Capability | Notes |
|---|---|
| **Real binary execution** | No git, npm, make, cargo, docker, etc. |
| **Real process management** | No background processes, signals, job control |
| **Performance** | TypeScript reimplementations are slower than native |
| **Full bash compatibility** | Many edge cases missing; beta software |
| **System interaction** | No systemctl, network interfaces, hardware access |
| **Large file handling** | 10MB string limit, all in memory |
| **Real test execution** | Can't run pytest, jest, cargo test, etc. |

### The Honest Assessment

For Sivart's current use case (a single personal AI agent with full OS trust), just-bash adds complexity without clear benefit. OpenClaw's exec with allowlist permissions is sufficient.

For Loom (multi-agent orchestration with varying trust levels), just-bash becomes compelling as a **tool mediation layer**, not a replacement for OS access. The hybrid model (just-bash for sandboxed analysis + real exec for system operations) is the practical path.

## 8. Limitations and Risks

### Technical Limitations

1. **Beta software.** The README says "Use at your own risk." Command implementations may have bugs or missing features.
2. **Not real bash.** Edge cases in bash behavior (trap handling, process groups, terminal control, etc.) are not fully modeled.
3. **Memory-bound.** Everything runs in the Node.js heap. Large codebases via OverlayFs may hit memory limits.
4. **No real concurrency.** Each `exec()` is a single-threaded interpreter run. No background processes, no parallel pipelines (pipes are sequential).
5. **Python/JS sandboxing is WASM-based.** Adds significant overhead and has its own attack surface.

### Architectural Risks

1. **Vendor coupling to Vercel ecosystem.** The `bash-tool` wrapper targets the AI SDK. The `Sandbox` API targets `@vercel/sandbox`. Switching ecosystems requires extracting just-bash from the Vercel stack.
2. **Maintenance burden.** 79 commands reimplemented in TypeScript is a large surface area. Each needs to match bash behavior (or document deviations).
3. **Security is best-effort, not guaranteed.** The threat model is excellent but explicitly states: no VM isolation. In a hostile environment, a determined attacker may find escape vectors.
4. **AST transform API is powerful but risky.** Transform plugins can modify the AST before execution, which is great for instrumentation but adds complexity.

### Process Risks

1. **Dependency on a single project.** If Vercel deprioritizes just-bash, we'd need to fork or find alternatives.
2. **Early adopter risk.** Beta status means API changes, breaking updates, and incomplete documentation.

## 9. Verdict and Next Steps

### Verdict

just-bash is an impressive piece of engineering with a clear security-first design. It solves a real problem (giving AI agents a safe execution environment) in an elegant way (virtual bash with pluggable filesystems and custom commands).

**For Sivart/current operations:** Not needed. OpenClaw's exec is fine for a trusted single-agent setup.

**For Loom/multi-agent orchestration:** Worth integrating as a **tool mediation layer**. The custom command system is the key value: it provides a clean, shell-native interface for injecting controlled tools into agent environments. The filesystem composability (MountableFs with OverlayFs mounts) enables sophisticated read/write isolation patterns.

**For Agent Factory concept:** Strong fit. Each agent role gets a purpose-built Bash instance with exactly the tools it needs. Custom commands encode organizational processes. This is the "process engineering" the institutional AI thesis calls for.

### Recommended Next Steps

1. **Prototype a custom command bridge.** Write 3-5 custom commands wrapping Synthweave MCP tools. Test that they work with pipes, redirections, and shell features. (~1 day)

2. **Prototype hybrid execution.** Create a Loom agent runner that uses just-bash for data analysis tasks and real exec for git/gh operations. Test the handoff pattern. (~2 days)

3. **Evaluate MountableFs for Loom workspaces.** Mount a real workspace as OverlayFs (read-only view for analysis agents) and ReadWriteFs (for implementation agents). Measure memory overhead. (~1 day)

4. **Draft Loom spec amendments.** Based on prototype results, formalize the `sandbox` config option and `expose_as` MCP bridge described in §5 above. (~0.5 day)

5. **Monitor the project.** Watch the repo for stability improvements, breaking changes, and the path to 1.0. File issues if we find bugs during prototyping.

6. **Do NOT adopt for production until 1.0.** Beta software with this much security surface should be used for prototyping and evaluation only.
