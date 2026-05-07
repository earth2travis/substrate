---
title: "Browser Automation for AI Agents: Research Overview"
tags: [research, browser-automation, headless-chrome, playwright, mcp, clawdbot]
related: [playwright-analysis, claude-code-capabilities, skills-as-portable-knowledge, agent-native-operations, the-openclaw-lesson]
source: "Research for Issue #81, last updated February 3, 2026"
---

# Browser Automation for AI Agents: Research Overview

## Summary

Sivart needs browser automation for interactive web tasks (signups, JS-heavy sites, form filling). Current gap: `web_search` and `web_fetch` work, but anything requiring JavaScript execution or user interaction fails. Recommendation: start with Clawdbot's built-in browser support (headless Chrome), fall back to Browserless if resource constraints prove too tight.

## Current Constraints

**Server Resources (Hetzner CPX11):**
- RAM: 2 GB total, ~1.1 GB available
- CPU: 2 vCPU shared
- Disk: 40 GB total, 31 GB available

Headless Chrome typically uses 300-500 MB per instance with proper flags. Tight but workable.

**Current Tooling:** Clawdbot has a full browser tool already. Status: `No supported browser found` because Chrome is not installed on the server.

## Clawdbot Built-in Browser Support

### Modes

1. **clawd (managed):** Dedicated, isolated Chrome profile controlled by the agent
2. **chrome (extension relay):** Uses existing Chrome tabs via browser extension
3. **remote CDP:** Connect to Browserless or any CDP endpoint

### Features (when Playwright installed)

- Tab control (open, focus, close, navigate)
- Snapshots (AI or ARIA format) with element refs
- Actions (click, type, drag, select, hover)
- Screenshots and PDFs
- Cookie and storage management
- Geolocation, timezone, device emulation

### Linux Setup

```bash
# Install Chrome (not snap)
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install -y
```

Config (`~/.clawdbot/clawdbot.json`):
```json
{
  "browser": {
    "enabled": true,
    "executablePath": "/usr/bin/google-chrome-stable",
    "headless": true,
    "noSandbox": true
  }
}
```

Key flags for low-memory VPS: `--headless`, `--no-sandbox`, `--disable-dev-shm-usage`, `--disable-gpu`, `--disable-extensions`, `--single-process`, `--memory-pressure-off`.

## Browser-as-a-Service Alternatives

### Browserless

Most established option. Clawdbot has native support.

| Plan | Price | Units/mo | Concurrency |
|------|-------|----------|-------------|
| Free | $0 | 1k | 1 |
| Prototyping | $25/mo | 20k | 3 |
| Starter | $140/mo | 180k | 20 |

A "unit" is 30 seconds of browser time. Residential proxy costs 6 units/MB.

### Hyperbrowser

Newer entrant, AI-first design. Includes "HyperAgent" for natural language browser control. MCP integration. Faster connection times in benchmarks.

### Browserbase

Modern session handling, good developer experience. Powers Stagehand (open source web agent framework).

## AI Agent Browser Patterns

### Playwright MCP

Microsoft's protocol letting AI models interact with browser accessibility trees. Key concepts: snapshots (text representation of page state with element refs), actions (click, type using snapshot refs), ephemeral refs (re-snapshot after navigation).

### Browser-Use (Open Source)

Python library by Magnus Müller and Gregor Žunić. Wraps Playwright in an LLM control loop. Open source, free to use.

### Best Practices

1. Prompt the agent with focused tools — don't overwhelm with every capability
2. Use snapshots, not screenshots, for decisions — text is cheaper than vision
3. Re-snapshot after navigation — refs are not stable across page changes
4. Manual login for sensitive sites — automated login triggers anti-bot
5. Headless + stealth flags for avoiding detection

## Security Considerations

- **Credential handling:** Never give the model credentials directly. Manual login in clawd browser profile. Store tokens in 1Password, inject via environment variables.
- **Sandboxing:** Clawdbot supports sandboxed browser sessions. Trade-off: more likely to trigger bot detection. For sensitive sites, use host browser with `allowHostControl: true`.
- **CDP Security:** Keep control URLs loopback-only (127.0.0.1). For remote CDP, use token auth and/or Tailscale. Never expose CDP to public internet.
- **Profile isolation:** The `clawd` profile is separate from personal browser. Treat as sensitive (may contain logged-in sessions).

## Recommended Implementation Path

**Phase 1: Local Chrome (Low Cost)**
1. Install Google Chrome on the server
2. Configure Clawdbot with headless + noSandbox
3. Test with simple automation tasks
4. Monitor memory usage

**Phase 2: Resource Assessment**
- If memory stable (<800 MB with Chrome), stay local
- If memory pressure or OOM issues, move to Browserless free tier

**Phase 3: Production (if needed)**
- Upgrade to Browserless Prototyping ($25/mo) or Starter ($140/mo)
- Or upgrade server (2GB → 4GB is ~$4/mo more on Hetzner)

## Connection to Agent Factory

Browser automation is the missing piece for Type 2 verification skills. The agent factory needs to verify that web-facing outputs actually work. Playwright and headless Chrome provide the infrastructure. The pattern from Intercom (signup-flow-driver) is the canonical example.

## Related

- [[playwright-analysis]] — End-to-end testing framework capabilities
- [[claude-code-capabilities]] — Claude Code's browser integration and Chrome features
- [[skills-as-portable-knowledge]] — Agent behavior as versioned, composable instructions
- [[agent-native-operations]] — Tools designed for AI-human partnership
- [[the-openclaw-lesson]] — Lessons from OpenClaw adoption