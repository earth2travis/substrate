---
title: "Browser Verification"
tags: [concept, verification, browser-automation, testing, skills, agents]
related: [[playwright-analysis]], [[browser-automation]], [[skills-as-portable-knowledge]], [[agent-native-operations]], [[claude-code-capabilities]]
source: insights/concepts/browser-verification.md
---

# Browser Verification

## Thesis

Agent factories produce web-facing artifacts (blog posts, UIs, deployments), but verifying those artifacts actually work is a persistent gap. Browser automation — Playwright, headless Chrome, MCP browser patterns — provides the infrastructure for Type 2 verification skills: programmatically confirming that agent outputs render correctly, function as intended, and don't break across deploys.

## The Verification Gap

Current agent tooling has strong creation capabilities (file operations, code generation, git workflows) but weak verification. `web_search` and `web_fetch` work for static content, but anything requiring JavaScript execution, form interaction, or visual confirmation fails.

The Intercom pattern ("signup-flow-driver runs through signup, email verify, onboarding in a headless browser with hooks for asserting state at each step") is the canonical example of what's missing in most agent stacks.

## The Browser Verification Stack

### 1. Playwright as Verification Engine

End-to-end testing framework by Microsoft. Automates Chromium, Firefox, WebKit. Key features for agent verification:
- **Auto-waiting:** No manual sleeps, no flakiness
- **Test isolation:** Fresh browser context per test
- **Trace viewer:** Time-travel debugging with screenshots
- **Codegen:** Record interactions and auto-generate test code

Playwright scripts run as code, not as model-driven browser interactions. This is 30-40x cheaper in tokens than MCP browser tools.

### 2. Headless Chrome on the Server

Clawdbot's built-in browser support provides three modes:
- **clawd (managed):** Dedicated, isolated Chrome profile controlled by the agent
- **chrome (extension relay):** Uses existing Chrome tabs via browser extension
- **remote CDP:** Connect to Browserless or any CDP endpoint

On a 2GB VPS, headless Chrome uses 300-500MB per instance with proper flags (`--headless`, `--no-sandbox`, `--disable-dev-shm-usage`, `--single-process`).

### 3. MCP Browser Patterns

Microsoft's Model Context Protocol for browser interaction:
- **Snapshots:** Text representation of page state with element refs
- **Actions:** Click, type, etc. using snapshot refs (not CSS selectors)
- **Ephemeral refs:** Re-snapshot after navigation

Best practices: prompt agents with focused tools, use snapshots not screenshots, manual login for sensitive sites, headless + stealth flags for detection avoidance.

## Verification Skill Patterns

| Skill | What It Does | Value |
|-------|-------------|-------|
| site-verifier | Load URL, check renders, assert content | Blog/deploy verification |
| pr-babysitter | Poll GitHub PR page, check CI badges | Automated CI monitoring |
| visual-regression | Screenshot comparison across deploys | Catch UI breakage |
| link-checker | Crawl site, find broken links | Content quality |
| accessibility-audit | Run axe-core via Playwright | Compliance |

## Implementation Path

**Phase 1: Local Chrome**
1. Install Google Chrome on the server
2. Configure Clawdbot with headless + noSandbox
3. Test with simple automation tasks
4. Monitor memory usage

**Phase 2: Resource Assessment**
- If memory stable (<800 MB with Chrome), stay local
- If memory pressure, move to Browserless free tier (1k units/month)

**Phase 3: Production**
- Upgrade to Browserless Prototyping ($25/mo) or Starter ($140/mo)
- Or upgrade server (2GB → 4GB is ~$4/mo more on Hetzner)

## Security Considerations

- **Credentials:** Never give the model credentials directly. Manual login in clawd browser profile. Store tokens in 1Password, inject via environment variables.
- **Sandboxing:** Clawdbot supports sandboxed browser sessions. Trade-off: more likely to trigger bot detection.
- **CDP Security:** Keep control URLs loopback-only (127.0.0.1). Never expose CDP to public internet.
- **Profile isolation:** The `clawd` profile is separate from personal browser. Treat as sensitive.

## Connection to Agent Factory

Browser verification is the infrastructure layer that makes "first-time-right" delivery possible. Without it, agents can generate code that passes static checks but fails in the browser. With it, agents can verify their own outputs before claiming completion.

The pattern from Rowboat (background agents that update the graph automatically) and Intercom (signup-flow-driver) both point to the same need: agents must be able to verify what they build.

## Related

- [[playwright-analysis]] — End-to-end testing framework capabilities
- [[browser-automation]] — Browser automation options for AI agents
- [[skills-as-portable-knowledge]] — Agent behavior as versioned, composable instructions
- [[agent-native-operations]] — Tools designed for AI-human partnership
- [[claude-code-capabilities]] — Claude Code's browser integration and Chrome features