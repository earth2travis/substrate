# Browser Automation for AI Agents: Research Overview

_Research for Issue #81. Last updated: 2026-02-03._

---

## Executive Summary

[[Sivart]] needs browser automation for interactive web tasks (signups, JS-heavy sites, form filling). The current gap: `web_search` and `web_fetch` work, but anything requiring JavaScript execution or user interaction fails.

**Recommendation:** Start with Clawdbot's built-in browser support (headless Chrome on the server). Fall back to Browserless if resource constraints prove too tight. The infrastructure already exists; we just need to enable it.

---

## 1. Current Constraints

### Server Resources (Hetzner CPX11)

| Resource | Total  | Available |
| -------- | ------ | --------- |
| RAM      | 2 GB   | ~1.1 GB   |
| CPU      | 2 vCPU | Shared    |
| Disk     | 40 GB  | 31 GB     |

Headless Chrome typically uses 300-500 MB per instance with proper flags. Tight but workable.

### Current Tooling

Clawdbot has a full browser tool already. Current status: `No supported browser found` because Chrome is not installed on the server.

---

## 2. Clawdbot's Built-in Browser Support

The platform has comprehensive browser automation built in. Key capabilities:

### Modes

1. **clawd (managed):** Dedicated, isolated Chrome profile controlled by the agent
2. **chrome (extension relay):** Uses existing Chrome tabs via browser extension
3. **remote CDP:** Connect to Browserless or any CDP endpoint

### Features

When Playwright is installed:

- Tab control (open, focus, close, navigate)
- Snapshots (AI or ARIA format) with element refs
- Actions (click, type, drag, select, hover)
- Screenshots and PDFs
- Cookie and storage management
- Geolocation, timezone, device emulation

### Linux Setup (Our Path)

From the docs, the recommended approach for Ubuntu:

```bash
# Install Chrome (not snap)
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install -y

# Config (~/.clawdbot/clawdbot.json)
{
  "browser": {
    "enabled": true,
    "executablePath": "/usr/bin/google-chrome-stable",
    "headless": true,
    "noSandbox": true
  }
}
```

Key flags for low-memory VPS:

- `--headless`: No GUI, saves memory
- `--no-sandbox`: Required for some Linux setups
- `--disable-dev-shm-usage`: Uses /tmp instead of /dev/shm
- `--disable-gpu`: No GPU needed for headless
- `--disable-extensions`: Fewer processes

---

## 3. Browser-as-a-Service Alternatives

If local Chrome proves too resource-hungry, remote options exist.

### Browserless

The most established option. Clawdbot has native support.

| Plan        | Price   | Units/mo | Concurrency | Notes            |
| ----------- | ------- | -------- | ----------- | ---------------- |
| Free        | $0      | 1k       | 1           | Good for testing |
| Prototyping | $25/mo  | 20k      | 3           | Development      |
| Starter     | $140/mo | 180k     | 20          | Production       |

A "unit" is 30 seconds of browser time. Residential proxy costs 6 units/MB.

Config example:

```json5
{
  browser: {
    enabled: true,
    defaultProfile: "browserless",
    profiles: {
      browserless: {
        cdpUrl: "https://production-sfo.browserless.io?token=<TOKEN>",
      },
    },
  },
}
```

### Hyperbrowser

Newer entrant, AI-first design. Includes "HyperAgent" for natural language browser control. Has MCP integration. Faster connection times in benchmarks, but Browserless faster for page navigation.

### Browserbase

Modern session handling, good developer experience. Powers Stagehand (open source web agent framework).

### Trade-offs

| Option       | Pros                            | Cons                         |
| ------------ | ------------------------------- | ---------------------------- |
| Local Chrome | Free, low latency, full control | Uses server RAM              |
| Browserless  | Established, Clawdbot native    | Costs money, network latency |
| Hyperbrowser | AI-first, HyperAgent            | Newer, less proven           |

---

## 4. AI Agent Browser Patterns

### Playwright MCP (Model Context Protocol)

Microsoft's protocol letting AI models interact with browser accessibility trees. Clawdbot's browser tool uses this pattern internally.

Key concepts:

- **Snapshots:** Text representation of page state with element refs
- **Actions:** Click, type, etc. using snapshot refs (not CSS selectors)
- **Refs are ephemeral:** Re-snapshot after navigation

### Browser-Use (Open Source)

Python library by Magnus Müller and Gregor Žunić. Wraps Playwright in an LLM control loop. Open source, free to use.

Use case: If we needed a Python-based browser agent separate from Clawdbot.

### Best Practices from Research

1. **Prompt the agent with focused tools.** Don't overwhelm with every capability.
2. **Use snapshots, not screenshots, for decisions.** Text is cheaper than vision.
3. **Re-snapshot after navigation.** Refs are not stable across page changes.
4. **Manual login for sensitive sites.** Automated login triggers anti-bot.
5. **Headless + stealth flags** for avoiding detection.

---

## 5. Security Considerations

### Credential Handling

- **Never give the model credentials directly.** Manual login in the clawd browser profile.
- Store tokens in 1Password, inject via environment variables.
- For X/Twitter and strict sites, use host browser with manual login.

### Sandboxing

Clawdbot supports sandboxed browser sessions. Trade-off: more likely to trigger bot detection. For sensitive sites, use host browser with `allowHostControl: true`.

### CDP Security

- Keep control URLs loopback-only (127.0.0.1)
- For remote CDP, use token auth and/or Tailscale
- Never expose CDP to public internet

### Profile Isolation

The `clawd` profile is separate from any personal browser. Treat it as sensitive (may contain logged-in sessions).

---

## 6. Resource Optimization

### Memory-Efficient Chrome Flags

```bash
google-chrome-stable \
  --headless \
  --no-sandbox \
  --disable-gpu \
  --disable-dev-shm-usage \
  --disable-extensions \
  --disable-background-networking \
  --disable-sync \
  --disable-translate \
  --no-first-run \
  --single-process \
  --memory-pressure-off
```

### Monitoring

```bash
# Check Chrome memory usage
ps aux | grep chrome | awk '{sum+=$6} END {print sum/1024 " MB"}'

# Kill if needed
pkill -f chrome
```

### Limits

Can use systemd-run or ulimit to cap memory:

```bash
systemd-run --scope -p MemoryLimit=512M google-chrome-stable ...
```

---

## 7. Recommended Implementation Path

### Phase 1: Local Chrome (Low Cost)

1. Install Google Chrome on the server
2. Configure Clawdbot with headless + noSandbox
3. Test with simple automation tasks
4. Monitor memory usage

### Phase 2: Resource Assessment

After Phase 1:

- If memory is stable (<800 MB with Chrome), stay local
- If memory pressure or OOM issues, move to Browserless free tier

### Phase 3: Production (if needed)

If usage grows:

- Upgrade to Browserless Prototyping ($25/mo) or Starter ($140/mo)
- Or upgrade server (2GB → 4GB is ~$4/mo more on Hetzner)

---

## 8. ClawdHub Skills

Several browser-related skills exist on ClawdHub:

- `agent-browser-clawdbot`: Appears to be Clawdbot-specific browser skill
- `agent-browser`: Generic browser automation
- `browsh`: Text-based browser (lightweight alternative)

Worth exploring if we need specific patterns beyond built-in support.

---

## 9. Open Questions

1. **Memory reality check:** Does headless Chrome actually fit in ~1GB available RAM?
2. **Playwright installation:** Does the Clawdbot package include Playwright, or separate install needed?
3. **Browserless free tier:** Is 1k units/month enough for our use cases?
4. **X/Twitter access:** Should we prioritize the `bird` CLI skill over browser automation for social?

---

## 10. Next Steps

- [ ] Install Google Chrome on server
- [ ] Enable browser in Clawdbot config
- [ ] Verify Playwright availability
- [ ] Test basic automation (snapshot, navigate, click)
- [ ] Monitor resource usage
- [ ] Document results

---

## References

- Clawdbot Browser Docs: `/home/clawd/.npm-global/lib/node_modules/clawdbot/docs/tools/browser.md`
- Linux Troubleshooting: `/home/clawd/.npm-global/lib/node_modules/clawdbot/docs/tools/browser-linux-troubleshooting.md`
- Browser Login Guide: `/home/clawd/.npm-global/lib/node_modules/clawdbot/docs/tools/browser-login.md`
- Browserless: https://browserless.io
- Hyperbrowser: https://hyperbrowser.ai
- Browser-Use: https://github.com/browser-use/browser-use
- Playwright MCP: https://developer.microsoft.com/blog/the-complete-playwright-end-to-end-story-tools-ai-and-real-world-workflows
