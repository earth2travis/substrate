# Paperclip Agent Adapter System: Deep Research

Source: https://github.com/paperclipai/paperclip (cloned and read 2026-03-09)

---

## 1. Architecture Overview

Paperclip uses a **three-consumer adapter model**: each adapter package provides implementations for the server, UI, and CLI. Adapters live in `packages/adapters/<name>/` with four package exports: `.` (shared metadata), `./server`, `./ui`, `./cli`.

Current adapters: `claude-local`, `codex-local`, `cursor-local`, `opencode-local`, `pi-local`, `openclaw-gateway`, plus generic `process` and `http` adapters in `server/src/adapters/`.

Three registries consume adapter modules:
- **Server**: `server/src/adapters/registry.ts` — maps type string to `ServerAdapterModule`
- **UI**: `ui/src/adapters/registry.ts` — maps type string to `UIAdapterModule`
- **CLI**: `cli/src/adapters/registry.ts` — maps type string to `CLIAdapterModule`

---

## 2. Adapter Interface / Contract

All types live in `packages/adapter-utils/src/types.ts`.

### ServerAdapterModule (the core contract)

```typescript
interface ServerAdapterModule {
  type: string;
  execute(ctx: AdapterExecutionContext): Promise<AdapterExecutionResult>;
  testEnvironment(ctx: AdapterEnvironmentTestContext): Promise<AdapterEnvironmentTestResult>;
  sessionCodec?: AdapterSessionCodec;
  supportsLocalAgentJwt?: boolean;
  models?: AdapterModel[];
  listModels?: () => Promise<AdapterModel[]>;
  agentConfigurationDoc?: string;
  onHireApproved?: (payload: HireApprovedPayload, adapterConfig: Record<string, unknown>) => Promise<HireApprovedHookResult>;
}
```

**Required methods:**
- `execute(ctx)` — runs the agent. Receives `AdapterExecutionContext`, returns `AdapterExecutionResult`
- `testEnvironment(ctx)` — preflight diagnostics for the "Test environment" UI button

**Optional:**
- `sessionCodec` — serialize/deserialize session state between runs
- `supportsLocalAgentJwt` — whether to inject a short-lived JWT as `PAPERCLIP_API_KEY`
- `onHireApproved` — lifecycle hook when agent is approved/hired

### AdapterExecutionContext (input to execute)

```typescript
interface AdapterExecutionContext {
  runId: string;
  agent: AdapterAgent;          // { id, companyId, name, adapterType, adapterConfig }
  runtime: AdapterRuntime;      // { sessionId, sessionParams, sessionDisplayId, taskKey }
  config: Record<string, unknown>;  // The agent's adapterConfig
  context: Record<string, unknown>; // Runtime context (taskId, wakeReason, approvalId, etc.)
  onLog: (stream: "stdout" | "stderr", chunk: string) => Promise<void>;
  onMeta?: (meta: AdapterInvocationMeta) => Promise<void>;
  authToken?: string;
}
```

### AdapterExecutionResult (output from execute)

```typescript
interface AdapterExecutionResult {
  exitCode: number | null;
  signal: string | null;
  timedOut: boolean;
  errorMessage?: string | null;
  errorCode?: string | null;
  usage?: UsageSummary;
  sessionId?: string | null;
  sessionParams?: Record<string, unknown> | null;
  sessionDisplayId?: string | null;
  provider?: string | null;
  model?: string | null;
  billingType?: AdapterBillingType | null;
  costUsd?: number | null;
  resultJson?: Record<string, unknown> | null;
  summary?: string | null;
  clearSession?: boolean;
}
```

### UIAdapterModule

```typescript
interface UIAdapterModule {
  type: string;
  label: string;
  parseStdoutLine: (line: string, ts: string) => TranscriptEntry[];
  ConfigFields: ComponentType<AdapterConfigFieldsProps>;
  buildAdapterConfig: (values: CreateConfigValues) => Record<string, unknown>;
}
```

### CLIAdapterModule

```typescript
interface CLIAdapterModule {
  type: string;
  formatStdoutEvent: (line: string, debug: boolean) => void;
}
```

---

## 3. The OpenClaw Gateway Adapter

**Location:** `packages/adapters/openclaw-gateway/`
**Type string:** `"openclaw_gateway"`
**Registration:** `server/src/adapters/registry.ts` — `supportsLocalAgentJwt: false`

### How It Connects

The adapter connects via **WebSocket** to an OpenClaw gateway. The protocol is versioned (currently `PROTOCOL_VERSION = 3`).

**Connection flow:**

1. Opens WebSocket to configured `url` (ws:// or wss://)
2. Waits for `connect.challenge` event containing a `nonce`
3. Sends `connect` request with:
   - Protocol version bounds (`minProtocol: 3, maxProtocol: 3`)
   - Client identity (`id`, `version`, `platform`, `mode`)
   - Role (default `"operator"`)
   - Scopes (default `["operator.admin"]`)
   - Auth credentials (token, password, and/or deviceToken)
   - **Device auth** (Ed25519 signed payload if enabled): signs `v3|deviceId|clientId|clientMode|role|scopes|signedAtMs|token|nonce|platform|deviceFamily`

**Device identity:** Uses Ed25519 key pairs. If `devicePrivateKeyPem` is in config, derives the device ID from the public key SHA-256. Otherwise generates an ephemeral key pair per connection.

**Auto-pairing:** If connection fails with "pairing required" and `autoPairOnFirstConnect` is true (default), the adapter opens a *second* WebSocket connection using shared auth to call `device.pair.list` and `device.pair.approve`, then retries the original connection.

### What API Calls It Makes (Gateway WebSocket Methods)

1. **`connect`** — initial handshake with auth + device signature
2. **`agent`** — primary request, sends the wake payload:
   - `message`: constructed wake text with full Paperclip API workflow instructions
   - `sessionKey`: based on strategy (issue-based by default: `paperclip:issue:{issueId}`)
   - `idempotencyKey`: the run ID
   - `timeout`: wait timeout
   - Plus any fields from `payloadTemplate` config
3. **`agent.wait`** — if the `agent` response status is not immediately `"ok"`, waits for completion
4. **`device.pair.list`** / **`device.pair.approve`** — only during auto-pairing flow

### Wake Text Construction

The adapter builds a detailed instruction text (`buildWakeText`) that is injected as the `message` field. This text contains:

- All `PAPERCLIP_*` environment variables for the run
- Reference to `~/.openclaw/workspace/paperclip-claimed-api-key.json` for API key
- Complete HTTP workflow instructions:
  1. `GET /api/agents/me`
  2. Determine issueId from env vars
  3. If issueId exists: checkout, get issue, get comments, execute, update status
  4. If no issueId: list assigned issues, pick one, execute
- API conventions (Authorization header, X-Paperclip-Run-Id header)
- Explicit warnings against guessing undocumented endpoints

### Event Handling

Listens for gateway events on the WebSocket:
- **`agent` events**: tracked by `runId`, captures `assistant` stream deltas for summary, `error`/`lifecycle` streams for error detection
- **`shutdown` events**: logged

### Result Extraction

After completion:
- Extracts summary from assistant event chunks or result payload
- Parses usage (tokens), provider, model, cost from nested `result.meta.agentMeta` or `meta`
- Maps to `AdapterExecutionResult`

### Configuration Fields

From `agentConfigurationDoc` in `src/index.ts`:

| Field | Type | Default | Purpose |
|-------|------|---------|---------|
| `url` | string | required | Gateway WebSocket URL |
| `headers` | object | {} | Handshake headers |
| `authToken` | string | - | Shared gateway token |
| `password` | string | - | Gateway shared password |
| `clientId` | string | "gateway-client" | Gateway client ID |
| `clientMode` | string | "backend" | Client mode |
| `role` | string | "operator" | Gateway role |
| `scopes` | string[] | ["operator.admin"] | Gateway scopes |
| `disableDeviceAuth` | boolean | false | Skip device auth |
| `payloadTemplate` | object | {} | Extra fields for agent params |
| `timeoutSec` | number | 120 | Adapter timeout |
| `waitTimeoutMs` | number | timeoutSec*1000 | agent.wait timeout |
| `autoPairOnFirstConnect` | boolean | true | Auto-approve device pairing |
| `sessionKeyStrategy` | string | "issue" | issue/fixed/run |
| `sessionKey` | string | "paperclip" | Fixed session key |
| `paperclipApiUrl` | string | - | Override API URL in wake text |

### Key Differences from Local Adapters

- **No sessionCodec** — the openclaw_gateway adapter has no session codec (sessions are managed gateway-side via `sessionKey`)
- **`supportsLocalAgentJwt: false`** — no JWT injection (the gateway handles its own auth)
- **No process spawning** — communicates entirely over WebSocket
- **Wake text injection** — instead of env vars + CLI flags, the entire workflow is injected as a text message to the gateway

---

## 4. Heartbeat Dispatch Through Adapters

The heartbeat system lives in `server/src/services/heartbeat.ts` (~2300 lines). Here's the flow:

### Wakeup Enqueue → Run Execution

1. **`enqueueWakeup(agentId, opts)`** — entry point for all agent invocations
   - Sources: `timer`, `assignment`, `on_demand`, `automation`
   - Checks agent status (not paused/terminated/pending_approval)
   - Checks heartbeat policy (enabled, wakeOnDemand)
   - Handles issue execution locking (prevents concurrent work on same issue)
   - Creates a `heartbeatRuns` record with status `"queued"`
   - Creates an `agentWakeupRequests` record
   - Calls `startNextQueuedRunForAgent()`

2. **`startNextQueuedRunForAgent(agentId)`** — concurrency-controlled queue drain
   - Uses per-agent start lock to prevent races
   - Checks `maxConcurrentRuns` (default 1, max 10)
   - Claims queued runs → status `"running"`
   - Calls `executeRun()` for each claimed run

3. **`executeRun(runId)`** — the main execution flow
   - Loads agent, runtime state, context
   - **Resolves workspace** (`resolveWorkspaceForRun`): project workspace → task session → agent home fallback
   - **Resolves session**: codec-based deserialization, cwd-aware resume, task session lookup
   - **Session reset logic**: resets on `issue_assigned`, timer wakes, manual invokes
   - Sets agent status to `"running"`
   - **Resolves secrets**: `secretsSvc.resolveAdapterConfigForRuntime()` — replaces secret references with values
   - **Gets adapter**: `getServerAdapter(agent.adapterType)` from registry
   - **Creates auth token**: `createLocalAgentJwt()` if `supportsLocalAgentJwt`
   - **Calls `adapter.execute(ctx)`** with full context
   - **Post-execution**: resolves next session state, updates runtime state, persists task sessions, records cost events, finalizes agent status

### Context Enrichment

The `enrichWakeContextSnapshot()` function builds the context object passed to adapters:

```typescript
contextSnapshot = {
  wakeReason,        // "issue_assigned", "issue_comment_mentioned", etc.
  issueId,           // from payload or context
  taskId,            // same as issueId typically
  taskKey,           // derived from taskId/issueId
  commentId,         // triggering comment
  wakeCommentId,     // same
  wakeSource,        // "timer", "assignment", "on_demand", "automation"
  wakeTriggerDetail, // "manual", "ping", "callback", "system"
  paperclipWorkspace, // { cwd, source, projectId, workspaceId, repoUrl, repoRef }
  paperclipWorkspaces, // array of workspace hints
  projectId,
  approvalId,
  approvalStatus,
  issueIds,          // linked issue IDs
}
```

### Concurrency & Locking

- Per-agent start locks prevent race conditions
- Issue execution locks prevent multiple agents working on the same issue simultaneously
- Deferred wakes queue up when an issue is locked by another agent's run
- Promotion: when a run completes and releases an issue lock, deferred wakes are promoted to queued runs

---

## 5. Agent Context: Tasks, Goals, Org Position

Context is injected differently depending on adapter type:

### For Local Adapters (claude-local, codex-local, etc.)

Context flows through **environment variables** and **prompt templates**:

**Environment variables** (from `buildPaperclipEnv` + execute logic):
- `PAPERCLIP_AGENT_ID`, `PAPERCLIP_COMPANY_ID` — identity
- `PAPERCLIP_API_URL` — server URL for API calls
- `PAPERCLIP_RUN_ID` — current run ID
- `PAPERCLIP_API_KEY` — short-lived JWT (local adapters only)
- `PAPERCLIP_TASK_ID` — current issue/task ID
- `PAPERCLIP_WAKE_REASON` — why this run was triggered
- `PAPERCLIP_WAKE_COMMENT_ID` — specific triggering comment
- `PAPERCLIP_APPROVAL_ID`, `PAPERCLIP_APPROVAL_STATUS` — approval context
- `PAPERCLIP_LINKED_ISSUE_IDS` — comma-separated linked issues

**Prompt templates** use `renderTemplate()` with variables: `agentId`, `companyId`, `runId`, `company`, `agent`, `run`, `context`.

The agent then uses the **Paperclip skill** to call APIs (`GET /api/agents/me`, issue checkout, etc.) to discover its org position, goals, chain of command, and task details at runtime.

### For OpenClaw Gateway Adapter

Context flows through the **wake text message** — a structured instruction text injected as the `message` field of the `agent` gateway request. This text contains:
- All PAPERCLIP_* env var values inline
- A complete step-by-step workflow (checkout, read issue, execute, update)
- API endpoint references

The agent reads the wake text and follows the procedure, calling Paperclip APIs to discover its full context.

### Org Position & Goals Discovery

These are **not** pre-injected into the context. Instead, the agent discovers them at runtime:
- `GET /api/agents/me` returns: id, companyId, role, chainOfCommand, budget
- Issue objects include: project, ancestors (parent chain), goal references
- The Paperclip skill (`skills/paperclip/SKILL.md`) documents the full procedure

---

## 6. Skill Injection System

Skills live in the repo's top-level `skills/` directory. Each skill has a `SKILL.md` with YAML frontmatter (name, description) and detailed instructions.

### Current Skills

| Skill | Purpose |
|-------|---------|
| `paperclip` | Interact with Paperclip control plane API (heartbeat procedure, issue management, API reference) |
| `paperclip-create-agent` | Create new agents workflow |
| `create-agent-adapter` | Guide for building new adapter packages |
| `release` | Release workflow |
| `release-changelog` | Changelog generation |
| `para-memory-files` | Memory file management |

### Injection Mechanisms (per adapter)

**claude-local**: Creates a tmpdir with `.claude/skills/` containing symlinks to repo skills, passes `--add-dir <tmpdir>` to Claude Code. Claude Code discovers skills as registered skills. Cleaned up in `finally` block.

```typescript
async function buildSkillsDir(): Promise<string> {
  const tmp = await fs.mkdtemp(path.join(os.tmpdir(), "paperclip-skills-"));
  const target = path.join(tmp, ".claude", "skills");
  await fs.mkdir(target, { recursive: true });
  // symlink each skill directory
  return tmp;
}
// Used as: args.push("--add-dir", skillsDir);
```

**codex-local**: Symlinks skills into Codex's global config directory (`$CODEX_HOME/skills` or `~/.codex/skills`). Skips existing entries to avoid overwriting user skills.

**openclaw-gateway**: Skills are **not injected** by the adapter. The wake text contains inline instructions equivalent to the `paperclip` skill's heartbeat procedure. The OpenClaw agent is expected to have its own skill/instruction system.

### Skill Design Philosophy

- Skills are **on-demand procedures**: the agent sees metadata (name + description) in context but only loads full SKILL.md content when it decides to invoke
- Descriptions act as routing logic (when to load the full skill)
- Keeps base prompt small
- For mandatory procedures, use explicit prompt instructions ("Use the paperclip skill to report your progress")

### .claude/skills/ (Repo-level)

The repo also has `.claude/skills/design-guide/SKILL.md` which is a Paperclip-internal skill for the design system, not injected into agents.

---

## 7. Key Observations for OpenClaw Integration

1. **The openclaw_gateway adapter treats OpenClaw as a black box**: it sends a message over WebSocket and waits for a result. All Paperclip-specific behavior is encoded in the wake text.

2. **Session management is gateway-side**: session keys follow the pattern `paperclip:issue:{issueId}` or `paperclip:run:{runId}`, sent as part of the agent request. The gateway is expected to manage session persistence.

3. **No local JWT for gateway adapter**: `supportsLocalAgentJwt: false`. The agent must have its own `PAPERCLIP_API_KEY` stored at `~/.openclaw/workspace/paperclip-claimed-api-key.json`.

4. **The wake text is essentially the entire Paperclip skill inlined**: it contains the full checkout/execute/update workflow, API rules, and env var values. This is because the gateway adapter can't inject skills via filesystem.

5. **Device auth is Ed25519-based**: uses challenge-response with signed payloads. Supports configured persistent keys or ephemeral per-connection keys.

6. **Auto-pairing is built in**: on first "pairing required" error, the adapter automatically opens a second connection to approve the device, then retries.

7. **The adapter protocol is frame-based**: request/response frames with UUIDs, event frames for streaming. Three frame types: `req`, `res`, `event`.
