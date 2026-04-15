---
title: "Figma + GitHub Projects v2 Plugin: Research Findings"
tags:
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/research.md
---

# Figma + GitHub Projects v2 Plugin: Research Findings

## 1. Figma Plugin API Capabilities

### Architecture

Figma plugins run in a dual environment:

- **Main thread (sandbox):** Minimal JavaScript environment (ES2020+) with access to the Figma document tree via the `figma` global object. No browser APIs (no fetch, no DOM, no setTimeout).
- **UI iframe:** Full browser environment with HTML/CSS/JS, browser APIs, fetch, DOM. Cannot access the Figma document directly.
- **Communication:** Message passing between sandbox and iframe via `postMessage`/`onmessage`.

The plugin main thread accesses the Figma scene graph (nodes, properties, selection). The iframe handles UI rendering and network requests. Figma also provides a `fetch` API directly in the sandbox for simpler network calls without needing an iframe.

### Plugin Types and Modes

Plugins can target multiple editor types via `manifest.json`:

- `"figma"`: Design mode (full read/write access)
- `"dev"`: Dev Mode (read only, with special inspect panel integration)
- `"figjam"`: FigJam
- `"slides"`: Figma Slides
- `"buzz"`: Figma Buzz

**Critical for this project:** A plugin can target both `"figma"` and `"dev"` editor types, allowing it to work in both design and development contexts.

### Dev Mode Integration (Key Feature)

Dev Mode plugins have unique capabilities that make them ideal for project management integration:

- **Inspect panel takeover:** When a Dev Mode plugin opens an iframe, it takes up the full height and width of the Inspect panel. This is exactly how Jira's plugin works.
- **Capabilities:** The manifest supports `"inspect"` capability for inspection plugins and `"codegen"` for code generation plugins.
- **VS Code support:** Dev Mode plugins can run in Figma for VS Code by adding `"vscode"` to capabilities.
- **Read only:** Dev Mode plugins cannot modify the document, but CAN write `pluginData` and `relaunchData` metadata to nodes.
- **Selection events:** Plugins can listen to `selectionchange` events to react when users select different layers.

This means the plugin can show GitHub issue context in the inspect panel when a developer selects a frame, exactly mirroring the Jira plugin pattern.

### UI Capabilities

- **Modal iframe:** Standard plugin UI, floating modal window
- **Inspect panel iframe:** In Dev Mode, fills the entire inspect panel
- **Relaunch buttons:** Buttons that appear in the Properties panel (design mode) or Inspect panel (Dev Mode) on specific nodes. Configured via `setRelaunchData()` and `manifest.json` `relaunchButtons`.
- **Plugin parameters:** Accept input via the quick actions menu without needing custom UI
- **No background execution:** Plugins must be actively invoked; they cannot run in the background

### Network and Auth

- Plugins can make network requests via the Figma Fetch API or from the iframe
- CORS applies: iframe has null origin, so APIs must allow `Access-Control-Allow-Origin: *` or the plugin must use a backend proxy
- `networkAccess` in manifest controls allowed domains (displayed on Community page)
- No built in OAuth support; plugins must implement their own auth flow (typically: open external URL via `figma.openExternal()`, user authenticates, callback delivers token)
- Plugin data can be stored per node (`setPluginData`), per file (`setPluginData` on root), or client side (`figma.clientStorage`)

### Plugin Data Storage

- **`pluginData`:** Key/value string storage on any node. Persists with the file. Scoped to the plugin.
- **`sharedPluginData`:** Like pluginData but accessible across plugins (with a namespace).
- **`clientStorage`:** Local storage on the user's machine. Good for auth tokens.
- **No server side storage:** Plugins must bring their own backend if persistent server side state is needed.

### Publishing Process

- Register plugin via Figma's "Create new plugin" feature
- Submit for review with support contact
- After initial approval, updates publish immediately without review
- No analytics from Figma; must instrument your own
- Version history visible to users

## 2. GitHub Projects v2 API

### GraphQL API Structure

GitHub Projects v2 is exclusively managed through the GraphQL API. Key objects:

- **ProjectV2:** The project itself (title, description, fields, items, views, workflows)
- **ProjectV2Item:** An item in the project (can be an Issue, PR, or DraftIssue)
- **ProjectV2Field / ProjectV2FieldConfiguration:** Field definitions
- **ProjectV2ItemFieldValue:** The value of a field for a specific item

### Field Types

Projects v2 supports these custom field types:

- **Text:** Free form text
- **Number:** Numeric values
- **Date:** Date picker
- **Single select:** Dropdown with color coded options (used for Status)
- **Iteration:** Sprint/cycle planning with date ranges
- **Issue fields:** Organization level fields (priority, effort, dates) available in Projects
- **Parent issue / Sub issue progress:** Hierarchy tracking
- **Pull request fields:** Linked PRs and reviewers
- **Issue type field:** Categorization

### Key Mutations

- `addProjectV2ItemById`: Add existing issue/PR to a project
- `updateProjectV2ItemFieldValue`: Update a field value on a project item
- `createProjectV2`: Create a new project (requires org/user context)
- `deleteProjectV2Item`: Remove item from project
- `createIssue`: Create a new issue (separate mutation, then add to project)

### Authentication Options

For a third party Figma plugin connecting to GitHub:

1. **OAuth App (Web Application Flow):**
   - User redirected to `github.com/login/oauth/authorize`
   - Callback delivers authorization code
   - Exchange code for access token via backend
   - Scopes needed: `repo` (for private repos), `project` (for Projects v2 access), `read:org` (for org projects)
   - Long lived tokens (no expiry unless revoked)

2. **GitHub App (recommended by GitHub):**
   - Fine grained permissions instead of broad scopes
   - Short lived tokens (more secure)
   - Can act on behalf of user or as installation
   - More complex setup but better security model

3. **Personal Access Token (PAT):**
   - Simplest for individual use
   - User generates token and pastes into plugin
   - Fine grained PATs available with specific permissions
   - Not ideal for a published community plugin

**Recommendation:** GitHub App with user authorization flow. Fine grained permissions, short lived tokens, and the ability to request only `project:read` and `project:write` scopes.

### Rate Limits

- 5,000 points per hour per user (standard)
- 10,000 points per hour for GitHub Enterprise Cloud
- Each query costs points based on complexity
- Pagination via cursors (standard GraphQL relay pattern)

### CORS Consideration

The GitHub GraphQL API (`api.github.com/graphql`) does NOT set `Access-Control-Allow-Origin: *`. This means:

- **Direct calls from a Figma plugin iframe (null origin) will fail due to CORS**
- **A backend proxy is required** to relay API calls from the plugin to GitHub
- This is a fundamental architectural constraint that shapes the entire system design

## 3. Competitive Analysis

### Jira Plugin for Figma (Gold Standard Reference)

The Atlassian Jira plugin is the benchmark for project management integration in Figma:

- **Inspect panel integration:** Shows issue details when a frame is selected in Dev Mode
- **Issue linking:** Designers can link Figma frames to Jira issues
- **Status updates:** Can change issue status directly from Figma
- **Issue creation:** Can create new Jira issues from within Figma
- **Bidirectional:** Jira also shows Figma design links on the issue page
- **Architecture:** Uses Atlassian's backend (Atlassian Connect), so the plugin calls Atlassian servers which call the Jira API. No direct browser to Jira calls.

### Linear Plugin

- Exists in the Figma community
- Links designs to Linear issues
- Shows issue status and assignments
- Simpler than Jira plugin but demonstrates the pattern works

### Asana Plugin

- Official Asana plugin for Figma
- Create tasks from designs
- Link designs to existing tasks
- View task status and assignments

### GitHub Plugins (Current State)

Current GitHub related Figma plugins are minimal:

- A few community plugins for viewing GitHub repos or managing code
- No official or well maintained plugin for GitHub Projects v2
- No inspect panel integration for GitHub issues
- **This is a clear gap in the market**

### Common Patterns Across Successful Plugins

1. **Auth flow:** External browser window for OAuth, token stored in `clientStorage`
2. **Backend service:** All successful plugins use a backend to proxy API calls (CORS) and handle OAuth token exchange
3. **Selection awareness:** React to `selectionchange` to show contextual information
4. **Node metadata:** Store linking data as `pluginData` on nodes
5. **Dual mode:** Work in both design mode (for designers) and Dev Mode (for developers)
6. **Relaunch buttons:** Add quick access buttons to linked nodes

## 4. Technical Constraints and Opportunities

### Constraints

1. **CORS requires a backend:** GitHub's API doesn't support null origin requests. A lightweight proxy service is mandatory.
2. **No background execution:** Plugin cannot sync data in the background; all operations happen when the user actively runs the plugin.
3. **Read only in Dev Mode:** Cannot modify the document from Dev Mode, but CAN write pluginData (which is how linking works).
4. **Single action at a time:** Only one plugin can run at once.
5. **No webhooks to plugin:** GitHub cannot push updates to the plugin. Data is always pulled on demand.

### Opportunities

1. **Inspect panel is prime real estate:** Dev Mode inspect panel integration puts GitHub context exactly where developers look.
2. **Relaunch buttons:** Persistent buttons on linked nodes make the plugin discoverable.
3. **VS Code integration:** Dev Mode plugins can work in Figma for VS Code, bringing GitHub context into the IDE.
4. **pluginData for linking:** Storing issue IDs as plugin data on frames creates a durable, file level link between designs and issues.
5. **Figma REST API complement:** The Figma REST API (separate from plugin API) could enable a GitHub Action or webhook that reads design metadata, enabling bidirectional linking.
6. **Open source advantage:** No existing open source solution exists. Synthweave can own this space.

### Architecture Options

**Option A: Plugin + Managed Backend (SaaS style)**
- Figma plugin communicates with a Synthweave hosted backend
- Backend handles OAuth, proxies GitHub API calls, caches project data
- Pros: Best UX, handles CORS, can add features like webhooks
- Cons: Requires hosting, operational cost, privacy concerns (tokens pass through backend)

**Option B: Plugin + Self Hosted Backend**
- Same architecture but users deploy their own backend
- Pros: Full data sovereignty
- Cons: High friction for adoption, not viable for a community plugin

**Option C: Plugin + Cloudflare Worker (Lightweight Proxy)**
- Minimal proxy that handles OAuth token exchange and relays API calls
- No persistent storage; tokens stay in Figma `clientStorage`
- Pros: Low cost (Cloudflare free tier), minimal attack surface, stateless
- Cons: Limited ability to add server side features later

**Option D: Plugin + GitHub App Backend**
- GitHub App installation handles auth
- Backend is a GitHub App server that manages installation tokens
- Pros: Best security model, fine grained permissions
- Cons: More complex setup, users must install a GitHub App

**Recommended: Option C for v1, migrate to Option D for v2.** Start with a stateless Cloudflare Worker that handles OAuth and proxies requests. This minimizes operational burden while solving the CORS problem. As the plugin matures, add a GitHub App for better auth and server side features.
