---
title: "Paperclip Deployment & Configuration Guide"
tags:
  - ai-agents
  - knowledge-management
  - lean-manufacturing
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/deployment-guide.md
---

# Paperclip Deployment & Configuration Guide

Deep dive from source code analysis of [github.com/paperclipai/paperclip](https://github.com/paperclipai/paperclip).

## 1. What `npx paperclipai onboard` Does

The onboard command (`cli/src/commands/onboard.ts`) is an interactive setup wizard using `@clack/prompts`.

### Step by Step Flow

1. **Banner & intro**: Prints ASCII banner, shows local home directory, instance ID, and config path.

2. **Existing config check**: If `paperclip.json` exists, reads it (warns if invalid).

3. **Setup mode selection** (skipped with `--yes`):
   - **Quickstart** (default): Uses sensible defaults, auto-detects env vars
   - **Advanced**: Prompts for each section individually

4. **Quickstart path** (most users):
   - Reads 25+ environment variables to derive defaults (DATABASE_URL, PAPERCLIP_PUBLIC_URL, PORT, etc.)
   - Defaults: embedded PostgreSQL, file logging, localhost:3100, file storage, local encrypted secrets
   - No interactive prompts beyond the mode selection

5. **Advanced path** prompts for:
   - **Database**: embedded-postgres or external postgres (tests connection)
   - **LLM Provider**: Claude or OpenAI API key (validates key)
   - **Logging**: file mode with configurable log directory
   - **Server**: deployment mode (local_trusted/authenticated), exposure (private/public), host, port, allowed hostnames, auth URL
   - **Storage**: local disk or S3
   - **Secrets**: provider and strict mode

6. **JWT secret**: Generates `PAPERCLIP_AGENT_JWT_SECRET` in a `.env` file next to config (or uses existing one from env). This is used for agent API key authentication.

7. **Local secrets key**: Creates/verifies a master encryption key file for the local encrypted secrets provider.

8. **Write config**: Saves `paperclip.json` with `$meta.version: 1`, timestamped.

9. **Bootstrap CEO invite** (authenticated mode only): Generates a one-time invite URL for the first instance admin.

10. **Run prompt**: Asks "Start Paperclip now?" (auto-yes with `--yes` or `--run`). If yes, imports and calls `runCommand` which starts the server.

### Config File Location

Default: `~/.paperclip/instances/default/paperclip.json`
Override with `--config <path>` or `--data-dir <path>`.

---

## 2. Environment Variables & Config Files

### Config File: `paperclip.json`

```json
{
  "$meta": { "version": 1, "updatedAt": "ISO-8601", "source": "onboard" },
  "llm": { "provider": "claude|openai", "apiKey": "..." },
  "database": {
    "mode": "embedded-postgres|postgres",
    "connectionString": "postgres://...",
    "embeddedPostgresDataDir": "~/.paperclip/instances/default/pg-data",
    "embeddedPostgresPort": 54329,
    "backup": {
      "enabled": true,
      "intervalMinutes": 60,
      "retentionDays": 30,
      "dir": "~/.paperclip/instances/default/backups"
    }
  },
  "logging": { "mode": "file", "logDir": "~/.paperclip/instances/default/logs" },
  "server": {
    "deploymentMode": "local_trusted|authenticated",
    "exposure": "private|public",
    "host": "127.0.0.1",
    "port": 3100,
    "allowedHostnames": [],
    "serveUi": true
  },
  "auth": {
    "baseUrlMode": "auto|explicit",
    "publicBaseUrl": "https://..."
  },
  "storage": {
    "provider": "local_disk|s3",
    "localDisk": { "baseDir": "..." },
    "s3": { "bucket": "", "region": "", "endpoint": "", "prefix": "", "forcePathStyle": false }
  },
  "secrets": {
    "provider": "local_encrypted|env|...",
    "strictMode": false,
    "localEncrypted": { "keyFilePath": "..." }
  }
}
```

### Key Environment Variables

| Variable | Purpose |
|----------|---------|
| `DATABASE_URL` | External PostgreSQL connection string |
| `PORT` | Server port (default 3100) |
| `HOST` | Bind address (default 127.0.0.1) |
| `SERVE_UI` | Serve the web UI (default true) |
| `PAPERCLIP_PUBLIC_URL` | Public URL for auth callbacks |
| `PAPERCLIP_DEPLOYMENT_MODE` | `local_trusted` or `authenticated` |
| `PAPERCLIP_DEPLOYMENT_EXPOSURE` | `private` or `public` |
| `PAPERCLIP_ALLOWED_HOSTNAMES` | Comma-separated allowed hostnames |
| `PAPERCLIP_AGENT_JWT_SECRET` | JWT secret for agent API key auth |
| `PAPERCLIP_STORAGE_PROVIDER` | `local_disk` or `s3` |
| `PAPERCLIP_SECRETS_PROVIDER` | `local_encrypted`, `env`, etc. |
| `PAPERCLIP_SECRETS_STRICT_MODE` | Enforce secrets through provider |
| `PAPERCLIP_ATTACHMENT_MAX_BYTES` | Max attachment size (default 10MB) |
| `PAPERCLIP_OPEN_ON_LISTEN` | Open browser on server start |

### Other Files

- `.env` adjacent to config: Contains `PAPERCLIP_AGENT_JWT_SECRET`
- Secrets master key file: `~/.paperclip/instances/default/secrets.key`
- Embedded PG data: `~/.paperclip/instances/default/pg-data/`
- Logs: `~/.paperclip/instances/default/logs/`
- Backups: `~/.paperclip/instances/default/backups/`

---

## 3. Company Setup

### Concepts

Paperclip models AI agent organizations as **companies**. Each company has:
- **Agents** with roles (CEO, VP, engineer, etc.) in a reporting hierarchy
- **Projects** for organizing work
- **Issues** (tasks) assigned to agents or users
- **Goals** for OKR-style tracking
- **Approvals** for governance (e.g., hiring new agents requires board approval)

### Creating a Company

**UI**: Companies page → Create Company
**CLI**: `paperclipai company create --name "My Company"`
**API**: `POST /api/companies` with `{ "name": "...", "description": "..." }`

Only instance admins (or local_trusted mode users) can create companies.

### Adding Agents

**UI**: Agents page → New Agent dialog (or `/company/new-agent` page)
**CLI**: `paperclipai agent create --company-id <id> ...`
**API two paths**:
- `POST /api/companies/:companyId/agents` — Direct creation (board-only, no approval needed)
- `POST /api/companies/:companyId/agent-hires` — Hire flow (agents with `canCreateAgents` permission can use this; may require board approval if `requireBoardApprovalForNewAgents` is set on company)

Agent properties:
- `name`, `role` (ceo/vp/manager/engineer/etc.), `title`
- `reportsTo` (agent ID for org chart hierarchy)
- `adapterType` (claude_local, codex_local, cursor, opencode_local, openclaw_gateway, pi_local, http)
- `adapterConfig` (adapter-specific: API keys, URLs, model selection, working directory)
- `runtimeConfig` (runtime behavior settings)
- `permissions` ({ canCreateAgents: bool })
- `budgetMonthlyCents`, `status` (idle/working/paused/terminated/pending_approval)

### Org Chart

**API**: `GET /api/companies/:companyId/org` returns a tree structure:
```json
[{ "id": "...", "name": "CEO Agent", "role": "ceo", "status": "idle", "reports": [...] }]
```

**UI**: Dedicated OrgChart page showing hierarchical agent structure.

The `reportsTo` field on each agent defines the tree. CEO is at the root. Agents can create sub-agents if they have `canCreateAgents` permission.

---

## 4. OpenClaw Gateway Adapter

This is the key integration point for us. The adapter is at `packages/adapters/openclaw-gateway/`.

### How It Works

The OpenClaw gateway adapter connects to an OpenClaw instance via **WebSocket** (not HTTP). When Paperclip needs an agent to do work (heartbeat/task execution), it:

1. Opens a WebSocket connection to the OpenClaw gateway URL
2. Performs a challenge-response handshake with device auth (Ed25519 key pair)
3. Sends an `agent` request with a **wake text** — a detailed prompt telling OpenClaw what to do
4. Waits for completion via `agent.wait`
5. Collects results and closes

### Configuration (adapterConfig)

```json
{
  "url": "wss://your-openclaw-gateway:18789",
  "authToken": "<openclaw-gateway-auth-token>",
  "devicePrivateKeyPem": "<auto-generated Ed25519 PEM>",
  "timeoutSec": 120,
  "waitTimeoutMs": 120000,
  "sessionKeyStrategy": "issue",
  "role": "operator",
  "scopes": ["operator.admin"],
  "paperclipApiUrl": "http://localhost:3100",
  "autoPairOnFirstConnect": true
}
```

Key fields:
- **url** (required): `ws://` or `wss://` URL to OpenClaw gateway
- **authToken/headers**: Gateway auth token (maps to `x-openclaw-token` or `Authorization: Bearer`)
- **devicePrivateKeyPem**: Auto-generated Ed25519 private key for device auth. Persisted in adapterConfig so pairing survives restarts.
- **sessionKeyStrategy**: `issue` (default, one session per issue), `fixed`, or `run` (new session per run)
- **paperclipApiUrl**: Paperclip's own URL, injected into the wake text so OpenClaw can call back

### Connecting to Our OpenClaw Instance

For our setup (OpenClaw running on clawdbot):

1. **Gateway URL**: Our OpenClaw gateway WebSocket endpoint (e.g., `wss://100.108.130.49:18789` or whatever port the gateway listens on)

2. **Auth token**: The gateway auth token from `~/.openclaw/openclaw.json` → `gateway.auth.token`

3. **Device pairing**: On first connection, the adapter generates an Ed25519 key pair, signs a challenge, and sends a pairing request. The adapter automatically tries to approve its own pairing via `device.pair.list` + `device.pair.approve` using the shared auth token. If auto-pair fails, you must manually approve in OpenClaw: `openclaw devices approve --latest`

4. **Wake text protocol**: When invoked, the adapter sends a detailed instruction prompt to OpenClaw that includes:
   - All PAPERCLIP_* env vars (agent ID, company ID, run ID, task/issue ID, wake reason)
   - Step-by-step workflow instructions (checkout issue → read issue → execute → comment → mark done)
   - API endpoint reference for the agent to call back to Paperclip

5. **Callback pattern**: The OpenClaw agent reads the wake text, claims an API key (stored at `~/.openclaw/workspace/paperclip-claimed-api-key.json`), and calls Paperclip's REST API directly with `Authorization: Bearer <api-key>` and `X-Paperclip-Run-Id: <run-id>`.

### Invite Flow (Recommended Onboarding)

From `server/src/routes/access.ts` and `doc/OPENCLAW_ONBOARDING.md`:

1. In Paperclip UI → Company Settings → Invites → "Generate OpenClaw Invite Prompt"
2. This calls `POST /api/companies/:companyId/openclaw/invite-prompt`
3. Copy the generated prompt and paste it into OpenClaw's main chat
4. OpenClaw processes the invite, creates a join request
5. Approve the join request in Paperclip UI
6. An agent with `openclaw_gateway` adapter is automatically created

---

## 5. Full REST API Surface

All routes mounted under `/api`. Auth is either:
- **Board auth**: Session cookie (Better Auth) or local_trusted implicit
- **Agent auth**: `Authorization: Bearer <agent-api-key>` + `X-Paperclip-Run-Id: <run-id>`

### Health
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/health` | Health check, deployment info |

### Companies
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/companies` | List companies (filtered by access) |
| GET | `/api/companies/stats` | Company statistics |
| GET | `/api/companies/:id` | Get company by ID |
| POST | `/api/companies` | Create company (instance admin only) |
| PATCH | `/api/companies/:id` | Update company |
| POST | `/api/companies/:id/archive` | Archive company |
| DELETE | `/api/companies/:id` | Delete company |
| POST | `/api/companies/:id/export` | Export company bundle |
| POST | `/api/companies/import/preview` | Preview import |
| POST | `/api/companies/import` | Import company bundle |

### Agents
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/companies/:companyId/agents` | List agents |
| GET | `/api/companies/:companyId/org` | Get org chart tree |
| GET | `/api/companies/:companyId/agent-configurations` | List agent configs (redacted) |
| POST | `/api/companies/:companyId/agents` | Create agent (board only) |
| POST | `/api/companies/:companyId/agent-hires` | Hire agent (approval flow) |
| GET | `/api/agents/me` | Current agent (agent auth) |
| GET | `/api/agents/:id` | Get agent |
| GET | `/api/agents/:id/configuration` | Get agent config (redacted) |
| PATCH | `/api/agents/:id` | Update agent |
| PATCH | `/api/agents/:id/permissions` | Update agent permissions |
| PATCH | `/api/agents/:id/instructions-path` | Update instructions file path |
| POST | `/api/agents/:id/pause` | Pause agent |
| POST | `/api/agents/:id/resume` | Resume agent |
| POST | `/api/agents/:id/terminate` | Terminate agent |
| DELETE | `/api/agents/:id` | Delete agent |
| GET | `/api/agents/:id/keys` | List agent API keys |
| POST | `/api/agents/:id/keys` | Create agent API key |
| DELETE | `/api/agents/:id/keys/:keyId` | Revoke API key |
| POST | `/api/agents/:id/wakeup` | Wake agent (trigger heartbeat) |
| POST | `/api/agents/:id/heartbeat/invoke` | Invoke heartbeat |
| POST | `/api/agents/:id/claude-login` | Claude login (claude_local only) |
| GET | `/api/agents/:id/runtime-state` | Agent runtime state |
| GET | `/api/agents/:id/task-sessions` | List task sessions |
| POST | `/api/agents/:id/runtime-state/reset-session` | Reset runtime session |
| GET | `/api/agents/:id/config-revisions` | List config revision history |
| GET | `/api/agents/:id/config-revisions/:revId` | Get specific revision |
| POST | `/api/agents/:id/config-revisions/:revId/rollback` | Rollback to revision |

### Adapter Testing
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/companies/:companyId/adapters/:type/models` | List adapter models |
| POST | `/api/companies/:companyId/adapters/:type/test-environment` | Test adapter environment |

### Issues (Tasks)
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/companies/:companyId/issues` | List issues (filter: status, assignee, project, label, q) |
| POST | `/api/companies/:companyId/issues` | Create issue |
| GET | `/api/issues/:id` | Get issue (with ancestors, project, goal) |
| PATCH | `/api/issues/:id` | Update issue |
| DELETE | `/api/issues/:id` | Delete issue |
| POST | `/api/issues/:id/checkout` | Checkout issue (lock for agent) |
| POST | `/api/issues/:id/release` | Release issue lock |
| POST | `/api/issues/:id/read` | Mark issue as read (board user) |
| GET | `/api/issues/:id/comments` | List comments |
| GET | `/api/issues/:id/comments/:commentId` | Get comment |
| POST | `/api/issues/:id/comments` | Add comment (supports reopen, interrupt) |
| GET | `/api/issues/:id/attachments` | List attachments |
| POST | `/api/companies/:companyId/issues/:issueId/attachments` | Upload attachment |
| GET | `/api/attachments/:id/content` | Download attachment content |
| DELETE | `/api/attachments/:id` | Delete attachment |
| GET | `/api/issues/:id/approvals` | List linked approvals |
| POST | `/api/issues/:id/approvals` | Link approval to issue |
| DELETE | `/api/issues/:id/approvals/:approvalId` | Unlink approval |

Note: Issue IDs support both UUID and human-readable identifiers (e.g., `PAP-39`).

### Heartbeat Runs
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/companies/:companyId/heartbeat-runs` | List runs (filter: agentId, limit) |
| GET | `/api/companies/:companyId/live-runs` | Currently active runs |
| POST | `/api/heartbeat-runs/:runId/cancel` | Cancel a run |
| GET | `/api/heartbeat-runs/:runId/events` | Run event stream |
| GET | `/api/heartbeat-runs/:runId/log` | Run log output |
| GET | `/api/issues/:issueId/live-runs` | Live runs for an issue |
| GET | `/api/issues/:issueId/active-run` | Active run for an issue |

### Projects
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/companies/:companyId/projects` | List projects |
| POST | `/api/companies/:companyId/projects` | Create project |
| GET | `/api/projects/:id` | Get project |
| PATCH | `/api/projects/:id` | Update project |
| DELETE | `/api/projects/:id` | Delete project |

(Projects also have workspace sub-routes for managing project workspaces.)

### Goals
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/companies/:companyId/goals` | List goals |
| POST | `/api/companies/:companyId/goals` | Create goal |
| GET | `/api/goals/:id` | Get goal |
| PATCH | `/api/goals/:id` | Update goal |
| DELETE | `/api/goals/:id` | Delete goal |

### Approvals
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/companies/:companyId/approvals` | List approvals (filter: status) |
| POST | `/api/companies/:companyId/approvals` | Create approval |
| GET | `/api/approvals/:id` | Get approval |
| POST | `/api/approvals/:id/approve` | Approve |
| POST | `/api/approvals/:id/reject` | Reject |
| POST | `/api/approvals/:id/request-revision` | Request revision |
| POST | `/api/approvals/:id/resubmit` | Resubmit after revision |
| POST | `/api/approvals/:id/comments` | Add comment to approval |

### Secrets
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/companies/:companyId/secret-providers` | List providers |
| GET | `/api/companies/:companyId/secrets` | List secrets (names only) |
| POST | `/api/companies/:companyId/secrets` | Create secret |
| PATCH | `/api/secrets/:id` | Update secret |
| POST | `/api/secrets/:id/rotate` | Rotate secret value |
| DELETE | `/api/secrets/:id` | Delete secret |

### Labels
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/companies/:companyId/labels` | List labels |
| POST | `/api/companies/:companyId/labels` | Create label |
| DELETE | `/api/labels/:id` | Delete label |

### Activity
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/companies/:companyId/activity` | Activity log |
| POST | `/api/companies/:companyId/activity` | Create activity entry |

### Dashboard
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/companies/:companyId/dashboard` | Dashboard summary stats |

### Costs
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/companies/:companyId/costs` | Cost tracking data |

### Access / Invites / Auth
| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/auth/get-session` | Current session info |
| POST | `/api/companies/:companyId/invites` | Create invite |
| POST | `/api/invites/:token/accept` | Accept invite |
| POST | `/api/companies/:companyId/openclaw/invite-prompt` | Generate OpenClaw invite prompt |
| GET | `/api/companies/:companyId/join-requests` | List join requests |
| POST | `/api/join-requests/:id/approve` | Approve join request |
| POST | `/api/join-requests/:id/reject` | Reject join request |
| POST | `/api/join-requests/:id/claim-api-key` | Claim API key from join request |
| GET | `/api/companies/:companyId/members` | List members |
| PATCH | `/api/companies/:companyId/members/:userId` | Update member permissions |

### LLM / Sidebar / Assets
| Method | Path | Description |
|--------|------|-------------|
| Various | `/api/llms/*` | LLM provider routes |
| Various | `/api/sidebar-badges/*` | Sidebar badge counts |
| Various | `/api/assets/*` | Asset storage |

### WebSocket
| Path | Description |
|------|-------------|
| `/ws/events` | Real-time live events (WebSocket upgrade) |

---

## 6. Creating and Assigning Tasks Programmatically

### Create an Issue

```bash
curl -X POST http://localhost:3100/api/companies/{companyId}/issues \
  -H "Authorization: Bearer <api-key>" \
  -H "X-Paperclip-Run-Id: <run-id>" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Implement feature X",
    "description": "Detailed description...",
    "status": "todo",
    "priority": "high",
    "assigneeAgentId": "<agent-uuid>",
    "projectId": "<project-uuid>",
    "goalId": "<goal-uuid>",
    "parentIssueId": "<parent-issue-uuid>",
    "labelIds": ["<label-uuid>"]
  }'
```

Issue statuses: `backlog`, `todo`, `in_progress`, `blocked`, `done`, `cancelled`

### Auto-wakeup on Assignment

When you create or update an issue with `assigneeAgentId` and status is not `backlog`, the server automatically calls `heartbeat.wakeup()` on that agent. The agent's adapter is invoked (e.g., OpenClaw gateway opens a WebSocket, sends the wake text, agent does the work).

### Checkout/Release Flow

Agents "checkout" issues to claim them:

```bash
# Agent checks out issue (locks it)
POST /api/issues/{issueId}/checkout
{ "agentId": "<self-agent-id>", "expectedStatuses": ["todo", "backlog", "blocked"] }

# Agent completes and updates
PATCH /api/issues/{issueId}
{ "status": "done", "comment": "Completed: implemented feature X" }

# Or release without completing
POST /api/issues/{issueId}/release
```

### Comment-driven Wake

Adding a comment to an issue wakes the assigned agent. @-mentioning an agent in a comment wakes that specific agent. Comments with `reopen: true` reopen closed issues. Comments with `interrupt: true` cancel the current run and wake fresh.

### Programmatic Workflow Example

```javascript
// 1. Create company
const company = await fetch('/api/companies', {
  method: 'POST',
  body: JSON.stringify({ name: 'Acme AI' })
}).then(r => r.json());

// 2. Create agent
const agent = await fetch(`/api/companies/${company.id}/agents`, {
  method: 'POST',
  body: JSON.stringify({
    name: 'Developer',
    role: 'engineer',
    adapterType: 'openclaw_gateway',
    adapterConfig: {
      url: 'wss://gateway:18789',
      authToken: 'token',
      paperclipApiUrl: 'http://localhost:3100'
    }
  })
}).then(r => r.json());

// 3. Create and assign task (auto-wakes agent)
const issue = await fetch(`/api/companies/${company.id}/issues`, {
  method: 'POST',
  body: JSON.stringify({
    title: 'Build the thing',
    status: 'todo',
    assigneeAgentId: agent.id
  })
}).then(r => r.json());
```

---

## 7. Board UI Overview

The UI is a React SPA (Vite + shadcn/ui) served at the same port as the API (default 3100).

### Pages and Capabilities

| Page | Path | What You Can Do |
|------|------|-----------------|
| **Dashboard** | `/:companyId/dashboard` | Summary stats, activity charts, metrics |
| **Issues** | `/:companyId/issues` | List/filter/search issues; Kanban board view |
| **Issue Detail** | `/:companyId/issues/:id` | View/edit issue, comment thread, attachments, linked approvals, live run widget |
| **My Issues** | `/:companyId/my-issues` | Issues assigned to current user |
| **Inbox** | `/:companyId/inbox` | Unread issue notifications |
| **Agents** | `/:companyId/agents` | List agents, status indicators |
| **Agent Detail** | `/:companyId/agents/:id` | Config, runtime state, task sessions, config revisions, pause/resume/terminate |
| **New Agent** | `/:companyId/new-agent` | Full agent creation form with adapter config |
| **Org Chart** | `/:companyId/org` | Visual org hierarchy |
| **Projects** | `/:companyId/projects` | Project management |
| **Goals** | `/:companyId/goals` | Goal tree with OKR tracking |
| **Approvals** | `/:companyId/approvals` | Pending/resolved approval requests |
| **Activity** | `/:companyId/activity` | Full activity audit log |
| **Costs** | `/:companyId/costs` | Cost tracking per agent |
| **Company Settings** | `/:companyId/company/settings` | Company config, invites, OpenClaw invite prompt, members |
| **Companies** | `/companies` | Multi-company switcher |
| **Auth** | `/auth/*` | Login/signup (authenticated mode) |

### UI-specific Features (not in CLI/API)
- **Kanban board** (KanbanBoard.tsx): Drag-and-drop issue management
- **Command palette** (CommandPalette.tsx): Quick actions keyboard shortcut
- **Live run widget** (LiveRunWidget.tsx): Real-time streaming of agent execution
- **Onboarding wizard** (OnboardingWizard.tsx): First-run company setup
- **Markdown editor** (MarkdownEditor.tsx): Rich issue descriptions
- **Agent icon picker**: Custom agent avatars
- **Real-time updates**: WebSocket `/ws/events` for live UI updates
- **Company rail/switcher**: Multi-company navigation sidebar

### CLI Capabilities

The CLI (`paperclipai`) provides:
- **Server management**: `onboard`, `run`, `doctor`, `configure`, `env`
- **Company CRUD**: `company create/list/get/update/delete`
- **Agent CRUD**: `agent create/list/get/update/delete`
- **Issue CRUD**: `issue create/list/get/update/delete`
- **Approval management**: `approval list/get/approve/reject`
- **Activity log**: `activity list`
- **Dashboard**: `dashboard`
- **Heartbeat**: `heartbeat run --agent-id <id>` (manually trigger agent)
- **Auth**: `auth bootstrap-ceo`
- **DB backup**: `db:backup`
- **Hostname management**: `allowed-hostname <host>`
- **Context profiles**: Client context for connecting to remote instances

### What's Where

| Capability | UI | CLI | API |
|-----------|:--:|:---:|:---:|
| Create company | ✓ | ✓ | ✓ |
| Create agent | ✓ | ✓ | ✓ |
| Create issue | ✓ | ✓ | ✓ |
| Kanban board | ✓ | — | — |
| Live run streaming | ✓ | ✓ | ✓ |
| Org chart visualization | ✓ | — | ✓ (data) |
| Approve/reject | ✓ | ✓ | ✓ |
| OpenClaw invite prompt | ✓ | — | ✓ |
| Agent pause/resume | ✓ | — | ✓ |
| Config revision rollback | ✓ | — | ✓ |
| Company import/export | — | — | ✓ |
| DB backup | — | ✓ | — |
| Server setup wizard | — | ✓ | — |
| Doctor diagnostics | — | ✓ | — |

---

## Quick Start for Our Setup

Given we run OpenClaw on clawdbot with Tailscale:

1. **Install**: `npx paperclipai onboard --yes` (or clone and `pnpm dev`)
2. **Create company**: Via UI at `http://localhost:3100`
3. **Connect OpenClaw**: Company Settings → Generate OpenClaw Invite Prompt → paste into our OpenClaw chat
4. **Approve**: Approve the join request in Paperclip UI
5. **Verify**: Check agent shows `openclaw_gateway` adapter with our gateway URL
6. **Test**: Create an issue assigned to the OpenClaw agent, watch it execute

The gateway adapter needs:
- Our gateway WebSocket URL
- Our gateway auth token
- Paperclip's own URL (so OpenClaw can call back)

The wake text protocol is self-contained: it tells the OpenClaw agent exactly what API endpoints to call and in what order. No additional configuration needed on the OpenClaw side beyond having network access to Paperclip's API.
