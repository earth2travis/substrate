# Synthweave Technical Summary

## 1. MCP Server

### Protocol: StreamableHTTP (Stateless)

**Location:** `apps/server/src/mcp/routes.ts`

```typescript
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";

mcpRouter.post("/", async (req: McpAuthenticatedRequest, res) => {
  const transport = new StreamableHTTPServerTransport({
    sessionIdGenerator: undefined, // Stateless mode
    enableJsonResponse: true,
  });
  const server = createMcpServer();
  await server.connect(transport);
  await transport.handleRequest(req, res, req.body);
});
```

- **Endpoint:** `POST /mcp`
- **Health check:** `GET /mcp/health`
- **Transport:** HTTP-based, per-request transport instances

### Auth Model: API Key with Bcrypt Verification

**Location:** `apps/server/src/mcp/middleware/apiKeyAuth.ts`

```typescript
// Format: Authorization: Bearer sw_<prefix>_<secret>
const apiKey = authHeader.substring(7); // Remove 'Bearer '

// Lookup by prefix, verify with bcrypt
const result = await pool.query(
  `SELECT ak.id, ak.user_id, ak.name, ak.key_hash, ak.scopes, ak.is_active, ak.organization_id
   FROM api_keys ak
   LEFT JOIN agents a ON ak.user_id = a.agent_id
   WHERE ak.key_prefix = $1 AND ak.is_active = true`,
  [prefix]
);
const isValid = await bcrypt.compare(apiKey, keyRecord.key_hash);
```

### Tool Definitions (22 Tools)

| Category | Tool | Description |
|----------|------|-------------|
| **Navigation** | `ls` | List workspace contents (bases, projects, folders, snips) |
| **Search** | `snip_search` | Hybrid search (semantic + full-text) with filters |
| **Snip Management** | `snip_reader` | Read snip with content, links, comments |
| | `create-snip` | Create snip with title, content, tags, project associations |
| | `snip_commenter` | Add comments to snips |
| | `get-comments` | Retrieve all comments for a snip |
| | `snip_rewrite` | Replace entire snip content |
| | `checkpoint` | Manage version history (list/read/create) |
| | `manage_snip` | Create, move, or update snip metadata |
| | `manage_reference_links` | CRUD for snip-to-snip links |
| **Project Management** | `create_project` | Create new project in a base |
| | `task_creator` | Create task (new snip or link existing) |
| | `task_updater` | Update task status, assignee, due date |
| | `manage_folder` | Create, rename, move, delete folders |
| | `manage_project` | Create, update, delete projects |
| **User Management** | `user_search` | Search users by email/username |

**Example Tool Schema** (`snip_search`):
```typescript
{
  query: z.string().describe("The search query text"),
  limit: z.number().optional(),
  offset: z.number().optional(),
  searchMode: z.enum(["hybrid", "semantic", "fulltext"]).optional(),
  filters: z.object({
    contentType: z.string().optional(),
    tags: z.array(z.string()).optional(),
    projectIds: z.array(z.string()).optional(),
    templatesOnly: z.boolean().optional(),
  }).optional()
}
```

---

## 2. Data Model

### Core Entities & Relationships

```
Organization
├── Bases (workspaces)
│   ├── BaseMemberships (user roles: viewer/editor/admin)
│   ├── BaseFolders (hierarchical)
│   ├── Projects
│   │   ├── Tasks (todo/doing/done)
│   │   ├── Milestones
│   │   ├── Collaborators
│   │   ├── ProjectFolders
│   │   └── ProjectSnips (many-to-many)
│   └── Snips (TipTap JSON content)
│       ├── SnipLinks (manual + @mention)
│       ├── Comments (threaded)
│       ├── Versions (checkpoint history)
│       └── Gists (AI summaries)
├── Groups (user groupings)
├── Invitations
└── Permissions (resource-level RBAC)
```

### Key Database Tables

**From `hasura/migrations/`:**

```sql
-- Snips (Rich Content)
CREATE TABLE snips (
  id UUID PRIMARY KEY,
  title TEXT NOT NULL,
  content JSONB,  -- TipTap JSON
  content_type content_type_enum DEFAULT 'tiptap',
  owner_id TEXT NOT NULL REFERENCES users(id),
  organization_id UUID REFERENCES organizations(id),
  base_id UUID REFERENCES bases(id),
  tags TEXT[],
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Projects
CREATE TABLE projects (
  id UUID PRIMARY KEY,
  title TEXT NOT NULL,
  goal TEXT,
  description TEXT,
  owner_id TEXT NOT NULL REFERENCES users(id),
  base_id UUID REFERENCES bases(id),
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tasks
CREATE TABLE tasks (
  id UUID PRIMARY KEY,
  project_id UUID NOT NULL REFERENCES projects(id),
  description TEXT NOT NULL,
  status task_status DEFAULT 'todo',
  assigned_user_id TEXT REFERENCES users(id),
  due_date TIMESTAMPTZ
);

-- Vector Search
CREATE TABLE content_embeddings (
  id UUID PRIMARY KEY,
  content_id UUID NOT NULL,
  embedding vector(1536),  -- OpenAI embedding dimension
  search_vector tsvector GENERATED ALWAYS AS (
    setweight(to_tsvector('english', title), 'A') ||
    setweight(to_tsvector('english', content_text), 'B')
  ) STORED
);
```

### Domain Models (TypeScript)

**Location:** `apps/*/src/bounded-contexts/*/domain/models/`

```typescript
// SnipManagement
export interface Snip {
  readonly id: SnipId;
  readonly title: SnipTitle;
  readonly content: SnipContent;  // TipTap JSON
  readonly ownerId: string;
  readonly tags: readonly string[];
  readonly projectIds: readonly string[];
}

// Collaboration
export interface Conversation {
  id: string;
  state: ConversationState;  // queued|running|waiting_for_user|completed|failed|cancelled
  messages: UIMessage[];
  totalInputTokens: number;
  totalOutputTokens: number;
}
```

---

## 3. Current API Surface

### Hasura GraphQL (Auto-generated CRUD)

**Endpoint:** `http://localhost:8080/v1/graphql`

- Auto-generated queries/mutations/subscriptions from PostgreSQL schema
- Real-time subscriptions via WebSocket
- Role-based permissions at field level (configured in `hasura/metadata/`)

### REST Endpoints (Express.js)

**Location:** `apps/server/src/` (80+ endpoints)

| Path | Purpose |
|------|---------|
| `/api/search/hybrid-search` | Semantic + full-text search |
| `/api/ai-assistant/chat` | AI chat streaming (Vercel AI SDK) |
| `/api/agents/:id/chat` | Agent conversation handling |
| `/api/organizations/*` | Org CRUD operations |
| `/api/snips/:id/images/*` | Image upload/serve |
| `/api/auth/setup` | User + org initialization |

### Webhooks (Hasura Event Triggers)

**33 tables with event triggers** for INSERT/UPDATE/DELETE:

| Table | Webhook | Purpose |
|-------|---------|---------|
| `snips` | `/webhooks/activity/snips` | Activity tracking |
| `projects` | `/webhooks/activity/projects` | Activity tracking |
| `tasks` | `/webhooks/triggers/evaluate` | Agent trigger evaluation |
| `comments` | `/webhooks/activity/comments` | Notification triggers |
| `versions` | `/webhooks/gist/checkpoint` | Gist generation |

### Hasura Actions (Custom Mutations)

```yaml
# hasura/metadata/actions.yaml
- name: bulkReindex
  handler: {{WEBHOOK_HOST_URL}}/webhooks/search/events/bulk-reindex

- name: moveProject
  handler: {{WEBHOOK_HOST_URL}}/webhooks/projects/move-project
```

---

## 4. Workflow Engine

**Status: Event-Driven Trigger System (not traditional DAG workflow)**

### Trigger Types

**Location:** `apps/server/src/bounded-contexts/Agents/domain/models/AgentConfigVersion.ts`

```typescript
export type TriggerCondition =
  | { type: "event"; entity: string; action: string }  // e.g., "snip.created"
  | { type: "mention"; location: "comment" | "chat" }  // @mention triggers
  | ScheduleTrigger;  // cron, interval, once

export type AgentScheduleConfig =
  | { kind: "cron"; expr: string; timezone?: string }
  | { kind: "interval"; everyMs: number }
  | { kind: "once"; at: string };
```

### Execution Flow

```
Database Event → Hasura Event Trigger → /webhooks/triggers/evaluate
                                              ↓
                              TriggerEvaluatorService.evaluateEvent()
                                              ↓
                              Match event → Create Conversation (queued)
                                              ↓
                              BullMQ enqueue → AgentWorker processes
                                              ↓
                              AgentRunner.runStreaming() → Completion hooks
```

### Job Queue (BullMQ + Redis/Valkey)

**Location:** `apps/server/src/bounded-contexts/Agents/infrastructure/queue/`

```typescript
// Two queues
agent-invocations  // Event & mention triggers (concurrency: 5)
agent-schedules    // Schedule triggers (concurrency: 3)

// Retry policy
const DEFAULT_JOB_OPTIONS = {
  attempts: 3,
  backoff: { type: "exponential", delay: 5000 },
  removeOnComplete: { age: 24 * 3600, count: 1000 },
};
```

### State Machine

```
queued → running → completed
              ↘ failed
              ↘ waiting_for_user → running (resumed)
              ↘ cancelled
```

---

## 5. Integration Points

### External Services

| Service | Purpose | Auth |
|---------|---------|------|
| **Auth0** | User authentication | OIDC/JWT |
| **OpenAI** | Embeddings, LLM | API key |
| **Anthropic** | LLM (Claude) | API key |
| **Google AI** | LLM (Gemini) | API key |
| **GitHub** | Project integration | OAuth + App |
| **Slack** | Team messaging | OAuth + Webhooks |
| **Google Calendar** | Meeting transcription | OAuth |
| **Fireflies AI** | Transcription | API key |
| **AWS S3** | File storage | IAM credentials |
| **AWS SES** | Email | IAM credentials |
| **Serper** | Web search | API key |
| **LlamaCloud** | Document parsing | API key |

### Credential Management

**Encryption:** AES-256-GCM for OAuth tokens and API keys

```typescript
// Format: [version][IV][authTag][ciphertext]
// IV: 12 bytes, authTag: 16 bytes
const cipher = crypto.createCipheriv("aes-256-gcm", key, iv);
```

**Environment Variables** (from `apps/server/src/config/env.ts`):
```
HASURA_GRAPHQL_ADMIN_SECRET
AUTH0_DOMAIN / AUTH0_AUDIENCE
OPENAI_API_KEY / ANTHROPIC_API_KEY / GOOGLE_GENERATIVE_AI_API_KEY
GITHUB_TOKEN_ENCRYPTION_KEY / SLACK_TOKEN_ENCRYPTION_KEY
S3_BUCKET_NAME / AWS_ACCESS_KEY_ID / AWS_SECRET_ACCESS_KEY
```

---

## 6. Architecture

### Monorepo Structure

```
synthweave/
├── apps/
│   ├── ui/                  # React 19 + Vite 7 frontend
│   │   └── src/bounded-contexts/
│   │       ├── SnipManagement/
│   │       ├── ProjectManagement/
│   │       ├── Collaboration/
│   │       ├── AIAssistant/
│   │       ├── AgentManagement/
│   │       ├── Bases/
│   │       ├── Search/
│   │       └── ... (18 total)
│   ├── server/              # Express.js backend
│   │   └── src/
│   │       ├── bounded-contexts/
│   │       ├── mcp/         # MCP server
│   │       ├── webhooks/    # Event handlers
│   │       └── shared/      # Cross-cutting concerns
│   └── storybook/           # Component library
├── packages/
│   └── snip-edit-core/      # Shared TipTap editor
└── hasura/
    ├── migrations/          # PostgreSQL migrations
    ├── metadata/            # Hasura config (permissions, relationships)
    └── seeds/               # Test data
```

### Tech Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | React 19, Vite 7, TailwindCSS 4, URQL, TipTap |
| **Backend** | Express 5, TypeScript, BullMQ |
| **Database** | PostgreSQL 16 + pgvector |
| **Cache** | Valkey (Redis-compatible) |
| **Real-time** | Yjs + WebSocket, GraphQL subscriptions |
| **Auth** | Auth0 + Hasura JWT |
| **Build** | Turbo monorepo, tsup |

### Deployment

**Docker Compose** (`docker-compose.yml`):
```yaml
services:
  postgres:
    image: pgvector/pgvector:pg16
    ports: ["5432:5432"]
  valkey:
    image: valkey/valkey:7-alpine
    ports: ["6379:6379"]
  graphql-engine:
    image: hasura/graphql-engine:v2.40.0
    ports: ["8080:8080"]
```

### DDD Pattern (per Bounded Context)

```
domain/
├── models/      # Aggregates, Entities, Value Objects (pure TS)
├── services/    # Stateless domain services
└── ports/       # Repository interfaces
application/
├── events/      # Use cases, orchestration
└── dtos/        # Request/response shapes
infrastructure/
├── persistence/ # GraphQL repositories (URQL)
├── graphql/     # Custom operations
└── clients/     # External service adapters
ui/
├── components/
├── hooks/
└── services/
```

---

## Summary

| Component | Status |
|-----------|--------|
| **MCP Server** | 22 tools via StreamableHTTP, API key auth |
| **Data Model** | PostgreSQL + Hasura, DDD-structured |
| **API Surface** | GraphQL + 80+ REST endpoints + webhooks |
| **Workflow Engine** | Event-driven triggers (not full DAG workflow) |
| **Integrations** | Auth0, GitHub, Slack, AI providers, S3 |
| **Architecture** | Turbo monorepo, 18 bounded contexts, DDD |
