# Runwork.ai Deep Dive: Product, Platform, and Value Proposition

Source: runwork.ai marketing site (homepage, features index, 11 feature pages, for-agents, pricing). Captured 2026-07-24 via direct curl (Firecrawl credits exhausted). Some secondary feature pages (apps, workflows, integrations, etc.) are JS-rendered and returned shell-only content; capabilities for those were reconstructed from the features index, homepage, pricing comparison table, and cross-references inside the pages that did render.

## What Runwork Is

Runwork is a shared AI workspace for teams. Its pitch: most companies bought AI tools (ChatGPT seats, Claude Code, Cursor) but none of it connects, nothing compounds, and nobody can see who is actually getting better at AI. Runwork sells the missing layer: shared capability. Setup, company context, skills, workflows, and adoption analytics live in one cloud workspace and sync into every AI tool every teammate uses.

Taglines: "Make your team actually good at AI." "Teach your AI once. Everyone's AI knows it." "Shared AI workspace for teams that want the work to compound." Secondary framing on feature pages: "The work cloud for AI agents" and "Operations platform for the AI-native era."

Supported agents: Claude Code, Claude Desktop (Cowork), Cursor, Codex (CLI + Desktop), Windsurf, Cline, Gemini CLI, Antigravity get "full support" (auto-detect and configure). ChatGPT is "light support" (MCP-only). Claims 60+ AI tools total.

## Capability Map

### 1. Onboarding and Setup (the Desktop App)
- Desktop app (Tauri, not Electron; macOS/Windows/Linux) runs a guided 14-scene onboarding journey, resumable if interrupted.
- Scans the machine, detects installed AI tools (Claude Code, Cursor, ChatGPT signed-in state, desktop apps like Slack/Notion/Drive), installs what is missing, configures each tool with the team's skills, MCP servers, and workspace settings. Adds team config alongside personal settings without overwriting.
- After onboarding: hub dashboard with tools, shared skills, integrations, active workflows, live activity feed. Tray icon with sync status (green/amber/red). Background continuous sync.
- Coaching system: guided tours, concept cards, quick-start guides per AI tool.
- CLI equivalent for engineers: `runwork setup --agent claude-code`, `runwork sync`, `runwork doctor`. One-line curl installer.
- Admin side: invite flow from the dashboard, onboarding funnel tracking (Invited / Desktop Installed / Setup Complete / Active), approved-tools policy (mark tools required), team instructions in markdown synced to every agent, per-agent instruction overrides.

### 2. Adoption and Training (the differentiator they lead with)
- "My Journey" personal dashboard: 0-100 score across four dimensions: Setup, Usage, Building, Knowledge. Compared against team average.
- Capability map: visual graph of capabilities (connect a tool, use a skill, connect an integration, create a skill, build a workflow, build an app, model data, expose an endpoint) marked mastered / ready-next / upcoming. Grounded explicitly in learning science: retention curves and zone of proximal development, not gamification.
- Skill decay: capabilities not exercised fade; nudges resurface them ("you connected an integration 2 months ago and haven't since").
- Next-best-step guidance: one concrete step beyond current reach, persona-aware (everyday, curious, engineer personas each have their own definition of "fully adopted"; an ops person can hit 100% without ever building an app).
- Weekly personalized training emails; admins see per-email reach/click performance.
- Team champions: surfaces who leads each capability area so help flows peer-to-peer.
- `runwork reflect`: weekly privacy-safe reflection analyzing the user's own messages, tool taxonomy, and skill usage; assistant output and tool results are dropped before analysis. Suggests saving repeated manual work as a skill or workflow, inside the user's own agent.
- Guidance surfaces everywhere: web app, desktop app, CLI, MCP, smart empty states, celebration moments.
- Three-level adoption ladder framing: Talk (chat with AI), Act (AI uses real tools and skills), Make (team builds workflows, apps, skills).

### 3. Team Dashboard (admin view)
- Four-dimension adoption scores per member (Setup/Usage/Building/Knowledge), engagement tiers (Power, Regular, Occasional, Dormant), recommended actions ("Jordan installed the CLI but hasn't completed setup. Send a nudge.").
- Nine tabs: Overview, Tools, Setup, Usage, Building, Knowledge, Training, Spend, Configuration.
- Agent fleet analytics: which AI tools are in use, combos, coverage gaps. 30-day usage trends, most-used skills. Building metrics (apps, workflows, schedules, agents created). Knowledge-sharing metrics (skills shared, components contributed).
- Training tab: 30-day adoption trend, per-member mastery heatmap, decay-risk view, training material reach.
- Spend tab: usage cost split across AI, integrations, sandbox runtime; budget tracking; top apps and users by cost.
- Telemetry is opt-in/out per member; privacy configurable by admin.

### 4. Skills
- Every app built on Runwork auto-generates a SKILL.md from its registered capabilities (entities, endpoints, workflows, schedules, integrations, components, agents, storage). Computed at runtime, always current.
- Users layer Domain Knowledge on top: best practices, recipes, guardrails, intent mappings. Editable; the auto-generated section is not.
- Slash commands in connected agents to browse/load skills; multiple skills load simultaneously for cross-app orchestration.
- Skills sync to every teammate's agent automatically.
- Portable: download SKILL.md (YAML frontmatter, capability descriptions, API refs with curl examples, MCP connection info) for use in Claude Code, Cursor, Codex outside Runwork.
- Import external skills by URL or file upload. External skills referencing APIs get a secure HTTP request tool with domain allowlisting.
- Skills Dashboard: All / App Skills / My Skills tabs, markdown editor with live preview, import/export.
- CLI: `runwork skills list`, `runwork skills push <file>`, `runwork sync`. During `runwork dev` the platform generates CLAUDE.md + AGENTS.md on the fly for framework context.

### 5. AI Agents and Agent Sandbox
- Build chat agents (persistent memory) and task agents (multi-step automation) via natural language; Runwork generates the agent code. No API keys or LLM infra to manage; BYOK or metered.
- Agents inherit workspace access: entities, integrations, workflows, custom tools (Zod schemas).
- Memory strategies: session / per-user / shared global knowledge base.
- Agents Dashboard: execution history with status, duration, cost, token usage; live execution streams; one-click retry.
- Agent Sandbox: agents delegate heavy work to Claude CLI running in an isolated compute environment with filesystem, web access, MCP tools, and workspace integrations. `delegate_task` tool auto-provided or `delegateTask()` in code.
- Cross-agent coordination through the filesystem (`/workspace/agents/`), session persistence by ID for multi-day work.
- Three-layer cost controls: platform credits ceiling, per-agent budgets/turn limits/timeouts, per-call overrides. 90% warning, 100% graceful stop.

### 6. MCP (two-way bridge)
- MCP Servers: every workspace exposes one MCP server aggregating everything; every app automatically gets its own per-app MCP server with full read/write (query entities, trigger workflows/schedules, call integrations, upload/download files, send channel messages). MCP resources (entity schemas, app manifests) and prompts (skills, channel instructions) served too. Streamable HTTP + SSE. API key auth, scopeable per app.
- MCP Servers Hub: four tabs (All, App MCPs, External, Integrations), live health checks with latency, Tool Explorer to browse and test any tool from the dashboard, quick-connect URLs with inline key creation.
- MCP Client: paste any external MCP server URL; auto-discovers tools/resources/prompts; external tools appear alongside native ones and auto-generate skill descriptions loadable via slash commands. Domain allowlisting + rate limiting.

### 7. Share and Resume (conversation handoff)
- From inside an agent: "share this conversation with alex@yourco.com" or "save this conversation."
- Tier 1 native byte-for-byte resume: captures the raw session file (Claude JSONL, Codex rollout) and places it in the recipient's own agent session store. Works Claude Code <-> Claude Desktop Cowork, Codex CLI <-> Codex Desktop.
- Universal fallback: verbatim Markdown transcript bundle; recipient in any MCP-speaking agent (Cursor, Windsurf, Gemini CLI, ChatGPT, etc.) pastes one prompt and continues with full context.
- Conversations inbox (sent / received / saved), auto-titles, metadata (source agent, work mode, topic tags, last user intent, suggested next step, open questions), email + desktop notifications, CLI (`runwork inbox`, `runwork resume <id>`).
- Audit log on every action, 7-day default expiry, soft-delete recoverable 7 days, external sharing gated by invite permission.

### 8. Workspace Platform (the "vibe-code" substrate)
- Apps: full-stack apps from natural language prompts, hosted and run by Runwork.
- Workflows: multi-step processes spanning hours/days, human-in-the-loop approvals, retries, full execution history.
- Schedules: durable cron-style background jobs. Automations: webhook-triggered pipelines.
- Data and Entities: shared structured data model across all apps (one source of truth for Contacts, Invoices, etc.).
- Integrations: 3,200+ services (HubSpot, Stripe, Slack, Gmail, Notion, Airtable, Jira, etc.), one connection usable by all apps and agents.
- Storage: object storage with presigned URLs, shared across apps.
- Public APIs: expose REST endpoints with API key auth, webhooks, rate limiting, request logging.
- Components: reusable UI blocks across apps.
- n8n Import: paste an n8n marketplace URL or upload workflow JSON; Runwork analyzes, adapts integrations, builds a full app with UI, automations, APIs. Claims 8,000+ importable workflow recipes.
- CLI: full terminal interface; every command supports `--json` for machine-readable output aimed at AI agents. `runwork init` -> `runwork dev` -> `runwork deploy`.
- Infra: git-based versioning with rollback, snapshot backups with point-in-time recovery, OAuth/email auth, RBAC (Owner/Admin/Editor/Viewer + user groups), audit logs (immutable, 30/90/365-day retention by tier), custom domains, global edge auto-scaling, marketplace for community apps, SOC 2 Type II "soon."

### 9. Community
- Browse/import skills from skills.sh and MCP servers from the MCP Registry. One-click import auto-syncs to the whole team. Popularity/install-count signals. Teams can publish their own skills back.

## Pricing (captured 2026-07-24)

- Startup: $79/mo, 3 seats, 10 GB data, 50 GB storage, $30/mo usage credits (~1,600 automations or 45 hrs agent work), 30-day audit retention, priority support.
- Growth (Most Popular): $379/mo, 15 seats, dedicated database, 50 GB data, 200 GB storage, $150 credits, 90-day retention.
- Scale: $979/mo, 50 seats, high-performance dedicated DB, 200 GB data, 1 TB storage, $400 credits, 1-year retention, 24/7 engineer support, custom domain.
- Enterprise: custom seats/usage/infra, region choice, SLA, SSO + SOC 2 (both "soon"), signed DPA, dedicated success manager.
- Additional seats $29/mo. 14-day Startup trial, no card. Post-trial workspace pauses read-only, nothing deleted.
- Usage credits meter integration calls and agent runtime. AI itself is BYOK by default (bills to your own keys, doesn't draw credits). Warnings at 75% and 90%, then pause, no surprise bills.
- Every plan includes the full platform: adoption/training, dashboard, desktop app, share-and-resume, unlimited skills/apps/workflows/schedules/APIs, MCP both directions, sandbox, community.

## Company and Positioning

- Runwork, Inc., 2026 copyright. Public presence: GitHub (runwork), Twitter (@runworkai), LinkedIn, Better Uptime status page. SOC 2 Type II in progress, runs on Cloudflare enterprise infrastructure, encryption at rest and in transit.
- Competitive frame: nobody else tracks team AI adoption; nobody else ships cross-user, cross-agent, cross-machine native conversation resume. They position against the "bought tools but no shared capability" gap rather than against any single vendor. Dedicated /compare/ and /for-agents/ pages. Use-case pages target founders, agencies, consultants, CTOs, and per-team pages (sales through legal, healthcare, SaaS).

## What Matters for Synthweave: Feature Candidates

Runwork is the closest existing product to Synthweave's concierge onboarding motion. Direct overlap and gaps:

1. Guided agent-led onboarding journey. Their 14-scene desktop flow with detection, resumability, and a "first useful AI moment" on day one is the benchmark. Synthweave's differentiator is doing it FOR the client (concierge) rather than shipping a self-serve installer; the journey structure, detection scan, and resumable checkpoints are worth adopting.
2. Team instructions + per-agent instructions as first-class synced artifacts. Markdown, pushed to every configured agent, editable centrally. This maps directly to how we should treat client context (CLAUDE.md/AGENTS.md/soul files) as managed, versioned, synced objects rather than one-time bootstrap files.
3. Skills as the compounding asset. Auto-generated-from-capabilities plus human-authored domain knowledge, synced to every agent, portable via SKILL.md, importable from registries. Our concierge deliverable should produce a skill library the client owns, not just a configured agent.
4. Adoption measurement as a product, not a report. Four-dimension scoring (Setup/Usage/Building/Knowledge), decay-aware mastery, persona-aware target paths, next-best-step nudges, weekly coaching emails. This is the retention engine that turns one-time onboarding into a subscription. Strong roadmap candidate.
5. `runwork reflect` pattern: privacy-safe digest (user messages + tool taxonomy only, assistant output dropped) that notices repeated manual work and suggests capturing it as a skill. Agent-led, in-surface, continuous onboarding after day one.
6. Share and Resume as knowledge transfer. Handing a working conversation to a teammate (native session file transplant or universal transcript bundle) is how good patterns spread. For client teams, this plus champion surfacing replaces train-the-trainer.
7. Onboarding funnel telemetry: Invited / Installed / Setup Complete / Active, with recommended actions per stuck member. Cheap to build, high demo value.
8. Approved-tools policy + remote detection/install. Client admin picks the sanctioned agent fleet; the system finds and configures whatever is actually on each machine.
9. MCP as the universal adapter, both directions. Per-app MCP servers auto-generated, external MCP servers importable with domain allowlisting. Everything we build for a client should be MCP-exposed by default.
10. Usage-credit economics with BYOK default. BYOK keeps AI cost off our ledger; credits meter only integration calls and agent runtime. Clean separation worth copying for Synthweave pricing.
11. n8n recipe import. Converts an existing automation ecosystem's content into platform workflows. A similar "import what you already have" motion (existing prompts, GPTs, zaps) could accelerate concierge onboarding.
12. Post-churn grace: workspace pauses read-only instead of deleting. Trust-building, cheap.

## Patterns for Agent-Led Onboarding (inspiration, applied to our concierge motion)

- The agent is the onboarding guide, not a form. Runwork's coaching system (concept cards, guided tours, quick-starts per tool) delivered inside the desktop app suggests our concierge agent should run the client's first session interactively: detect their tools, explain what it found, configure with consent, and end at a first useful moment tailored to their role.
- Onboarding never ends; it decays and renews. Skill-decay nudges and weekly next-best-step emails reframe onboarding as a continuous capability practice. Our post-onboarding engagement could be a scheduled agent that reviews usage, finds the frontier skill, and coaches one step per week.
- Day-one context preload. Their "first useful answer" promise (company context, team skills, approved tools already in place before the first prompt) is exactly what a concierge key should deliver: the client's agent wakes up already knowing the business.
- Persona paths. Everyday / curious / engineer as distinct completion definitions. Our onboarding plans should be persona-branched so non-technical staff are never pushed toward building.
- Reflection-driven capture. An agent that watches for repeated manual patterns and offers "save as skill" converts onboarding into a growing asset library, which is the compounding-value story we tell clients.
- Handoff as onboarding for late joiners. New hire resumes a saved conversation that shows how work actually gets done; the transcript IS the training material.
- Funnel visibility for the operator. Who is stuck where, with a named next action. For a concierge service this is our internal dashboard and also the client-facing proof of value.

## Open Questions / Unverified

- Secondary feature pages (apps, workflows, integrations, data, storage, APIs, CLI, components, workspaces, versioning, auth, audit, backups, marketplace, domains, scalable, compliance) are JS-rendered; details above for those come from index/pricing/for-agents cross-references, not the dedicated pages. A JS-capable fetch (browser tool) would fill gaps.
- /compare/, /about/, /changelog/, and use-case pages not yet captured.
- SOC 2 and SSO are both listed "Soon," which matters for enterprise client comparisons.
- No independent reviews captured; this is vendor self-description only.
