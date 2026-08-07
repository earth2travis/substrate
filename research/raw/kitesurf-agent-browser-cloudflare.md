# Kitesurf: Cloudflare's Agent-First Browser on Workers

**Compiled:** July 20, 2026
**Primary Source:** Cloudflare Blog, "Introducing Kitesurf" (August 6, 2026)
**Author:** Celso Martinho (Cloudflare)
**Additional Sources:** Cloudflare Browser Run developer documentation (pricing, limits, CDP integration, MCP clients, Quick Actions)

---

## What Kitesurf Is

Kitesurf is a new browser engine built from scratch by Cloudflare, designed specifically for AI agents rather than human users. It runs entirely on Cloudflare Workers in V8 isolates, using Rust compiled to WebAssembly. It is available for free while in beta as part of the Browser Run product.

The core insight: Chromium was built for humans. It supports tabs, themes, extensions, sync, 60fps scrolling, pixel-perfect rendering. None of that matters to an AI agent. What matters is token count, context windows, scalability, performance, and cost. Kitesurf strips away everything an agent does not need and keeps only what it does.

## Why This Matters for Agent Fleets

Current browser automation for agents relies on headless Chromium (Puppeteer, Playwright, Browserbase, etc.). Chromium is heavy: 271 MiB memory for a screenshot, 877ms CPU for HTML extraction. This makes it expensive to give every agent its own browser instance, which restricts web access to well-funded operations.

Kitesurf is 3-7x cheaper on CPU and memory:
- Screenshot: 380ms CPU (vs 1,173ms Chromium), 57.8 MiB (vs 271 MiB)
- HTML extraction: 229ms CPU (vs 877ms Chromium), 39.4 MiB (vs 273.7 MiB)
- Wall time: 1.7-1.8x slower than Chromium (cold software renderer vs JIT-warmed Chromium), but this gap is narrowing

The cost savings mean more agents can have browser access, more sessions can run concurrently, and the per-request cost drops enough to make web-browsing a default capability rather than a premium one.

## How It Works

### Architecture: Three Components

**1. The Engine** (public-facing)
- Handles Chrome DevTools Protocol (CDP) WebSocket and HTTP REST APIs
- Serves a landing page for internal testing
- Stores session state (the only stateful component)
- Compatible with Puppeteer, Playwright, chrome-remote-interface, and Chrome DevTools

**2. PageScript** (per-page isolate)
- Uses Dynamic Workers to spin up a long-lived V8 isolate per page
- Populates a clean globalThis with the DOM document
- Parses HTML using Blitz (Rust rendering engine) and CSS using Stylo (Firefox's CSS parser)
- Executes JavaScript and WebAssembly in the same isolate
- Uses Boa JS (Rust ECMAScript engine) for eval() calls since Workers do not support native eval
- Fetches all page assets through the SandboxOutbound worker

**3. PageRenderer** (stateless, disposable)
- Generates actual pixel output from the computed page objects
- Works in a loop with the Engine Worker via Workers RPC
- Fetches fonts and images from Static Assets
- Uses blitz-paint (Rust) for rasterization, Parley for text shaping
- Returns JPEG/PNG/PDF buffers
- Fully stateless: kill it, start another, replay the request

### Network Isolation: SandboxOutbound

All network requests from all components go through a single SandboxOutbound worker. Nothing else touches the network directly. It enforces CORS, injects browser-shaped headers, filters responses, and maintains per-page cookie jars. Any request that fails policy gets a 403.

### Design Principles

1. **Tests first.** Web Platform Tests (WPT) give AI agents clear goalposts for feature conformance. Integration and visual regression testing against real websites using Puppeteer. 215,000+ WPT tests passing and growing.

2. **Rust everywhere possible.** Native Rust compiled to WebAssembly via wasm-bindgen. No Emscripten emulation layers. Runs as close to the metal as Workers allows.

3. **Exception handling.** Any failure degrades to a blank frame or missing element, never a dead session. Catch faults at every boundary, default to safe and empty, log enough to diagnose.

4. **Isolation.** Every page load is untrusted input. Every session starts fresh. Each component has access only to resources strictly necessary for its function.

5. **Stateless when possible.** Stateless components are disposable, parallel, and cheap. Kill on stall, run thousands at once, size to demand.

## Integration Methods

### Quick Actions (stateless, one-shot)

REST API endpoints for common tasks. No code deployment needed.

- `/content` - Fetch HTML
- `/screenshot` - Capture screenshot
- `/pdf` - Render PDF
- `/markdown` - Extract Markdown from a webpage
- `/snapshot` - Capture multiple page formats
- `/scrape` - Scrape HTML elements
- `/json` - Capture structured data using AI
- `/links` - Retrieve links from a webpage
- `/crawl` - Crawl web content (async, up to 100 pages on free plan)

Example (Markdown extraction):
```
curl -X POST 'https://api.cloudflare.com/client/v4/accounts/<accountId>/browser-rendering/markdown' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <apiToken>' \
  -d '{"url": "https://example.com"}'
```

### Browser Sessions (persistent, full control)

CDP over WebSocket for complex automation:
- Puppeteer: `@cloudflare/puppeteer`
- Playwright: `@cloudflare/playwright`
- Direct CDP: WebSocket to `/devtools/browser`
- chrome-remote-interface

### MCP Integration

The `chrome-devtools-mcp` package provides an MCP server for AI agents:

```json
{
  "mcp": {
    "kitesurf": {
      "type": "local",
      "command": [
        "npx", "-y", "chrome-devtools-mcp@latest",
        "--wsEndpoint=wss://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/browser-render/devtools/browser?browser=kitesurf",
        "--wsHeaders={\"Authorization\":\"Bearer <API_TOKEN>\"}"
      ],
      "enabled": true
    }
  }
}
```

Works with Claude Desktop, Claude Code, Cursor, OpenCode, and any MCP-compatible client.

## Kitesurf-Specific Configuration

To use Kitesurf instead of Chromium, add `?browser=kitesurf` to any Browser Run endpoint:
- CDP WebSocket: `wss://api.cloudflare.com/client/v4/accounts/<ID>/browser-render/devtools/browser?browser=kitesurf`
- Quick Actions: `POST .../browser-rendering/screenshot?browser=kitesurf`

## Pricing and Limits

**Workers Free:**
- 10 minutes of browser time per day
- 3 concurrent browsers
- 1 new browser instance every 20 seconds
- 60-second browser timeout
- 1 Quick Actions request every 10 seconds
- 5 crawl jobs per day (100 pages each)

**Workers Paid:**
- 10 hours per month included, then $0.09/hour
- 10 concurrent browsers (monthly average), then $2.00/browser
- 120 concurrent browsers max
- 1 new browser instance per second
- 10 Quick Actions requests per second

**Kitesurf beta:** Free while in beta.

**Key billing detail:** Failed requests (waitForTimeout errors) are NOT charged. The `X-Browser-Ms-Used` response header reports browser time per request.

## Current Limitations

- No video playback
- No WebGL rendering
- No bot-challenge handshake negotiation with real TLS fingerprints
- No long-lived authenticated sessions (max 10 minutes with keep_alive)
- 1.7x slower than Chromium on wall time (rasterization and encoding overhead)
- Subset of CDP protocol (sufficient for most agent tasks but not complete)
- Not yet open source (planned)

## What Works Today

TodoMVC (vanilla, React, Vue, Angular, Preact), Wikipedia, Hacker News, Cloudflare Blog, Cloudflare dashboard. 215,000+ WPT tests passing. Strong coverage in CSS, DOM, HTML, selection, SVG, XHR -- the areas that matter most for agents.

## Hermes Integration Assessment

### Current Pain Points Kitesurf Could Solve

1. **Browserbase cost and contention.** Hermes currently uses Browserbase (Chromium-based) for browser_navigate. Sessions are heavy, expensive, and sometimes contend for resources. Kitesurf's Quick Actions could handle the most common use case (read a URL, extract text/markdown) at a fraction of the cost.

2. **Firecrawl credit exhaustion.** When Firecrawl credits run out, web_extract and web_search fail. Kitesurf's /markdown endpoint could serve as a fallback for URL-to-text conversion.

3. **X/Twitter access.** The comms_officer currently relies on Grok's x_search for X content because OAuth credits are depleted and X blocks headless Chromium. Kitesurf might not fully solve X's bot detection (it explicitly notes it cannot negotiate bot-challenge handshakes), but for reading public X profiles and posts without login walls, it could work if X serves static content to non-authenticated browsers.

4. **Session startup time.** Browserbase sessions take several seconds to spin up. Kitesurf Quick Actions are stateless and instant for one-shot tasks.

### Integration Path

The simplest integration: use Kitesurf's Quick Actions REST API as a web extraction backend, replacing or supplementing Firecrawl.

**What we would need:**
1. A Cloudflare account with a Browser Run API token (`Browser Rendering - Edit` permission)
2. The Cloudflare account ID
3. A lightweight Python function that wraps the Quick Actions REST API as a drop-in replacement for web_extract

**Potential Hermes integration points:**
- New tool: `browser_quick` for one-shot URL-to-markdown/screenshot/PDF
- Fallback for web_extract when Firecrawl is down
- Content extraction pipeline for comms_officer's research workflow

**What Kitesurf would NOT replace:**
- Interactive browsing (multi-step navigation, form filling, clicking)
- Session persistence across pages (login flows, authenticated content)
- Complex JavaScript-heavy SPAs that need full Chromium
- Bot-detection circumvention (it explicitly cannot do this)

### Comparison with Current Stack

| Feature | Browserbase (current) | Kitesurf (proposed) |
|---------|----------------------|---------------------|
| Engine | Chromium | Custom (Rust/Wasm) |
| Memory per session | ~270 MiB | ~40-58 MiB |
| CPU per request | ~900-1200 ms | ~230-380 ms |
| Cold start | Several seconds | Near-instant |
| Session persistence | Yes | Quick Actions: no; CDP: up to 10 min |
| Interactive browsing | Full support | CDP subset, growing |
| Bot detection bypass | Yes (stealth features) | No |
| MCP integration | Via Browserbase | Via chrome-devtools-mcp |
| Cost (free tier) | Limited | 10 min/day free, beta: free |
| Cost (paid) | Per-session pricing | $0.09/hour, $2/concurrent browser |

## What I Need to Get It Set Up

1. **Cloudflare account.** A Cloudflare account on the Workers Paid plan (or Free for initial testing at 10 min/day). The account ID from the dashboard.

2. **API token.** A custom API token with `Browser Rendering - Edit` permission, created at https://dash.cloudflare.com/profile/api-tokens

3. **Credential storage.** The API token and account ID stored in 1Password Operations vault under a new item (e.g., "cloudflare-kitesurf")

4. **Configuration decision.** Whether to use Kitesurf as: (a) a fallback for web_extract, (b) the primary extraction method for one-shot reads, or (c) a new dedicated tool callable by any agent.

5. **Testing.** Point it at a few URLs we commonly access (X posts, blog articles, documentation pages) and compare results with Firecrawl and Browserbase to validate quality.
