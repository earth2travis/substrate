---
title: "Browser Automation: Agent Control of the Web"
tags: [concept, agent, browser, automation, playwright, mcp]
related:
- browser-verification
- playwright-analysis
- claude-code-capabilities
- skills-as-portable-knowledge
- agent-native-operations
- the-openclaw-lesson
source: research/findings/browser-automation.md
---

# Browser Automation: Agent Control of the Web

## Thesis

Agents that cannot interact with JavaScript-heavy websites, fill forms, or take screenshots are agents with a missing sense. Browser automation is the prosthetic that lets agents perceive and act within the web as humans do. The gap between `web_search` and `web_interact` is the difference between a research tool and an operational one.

## Capabilities

- **Navigation**: Click, type, scroll, hover across dynamic DOMs
- **Observation**: Screenshots, DOM snapshots, ARIA accessibility trees
- **Interaction**: Form filling, authentication flows, JavaScript execution
- **Emulation**: Geolocation, timezone, device profiles, viewport sizing

## Implementation Landscape

- **Headless Chrome**: Full browser with `--no-sandbox` for VPS deployment
- **Playwright**: Cross-browser automation with element selectors
- **MCP Browser Tools**: Native browser capabilities via Model Context Protocol
- **Browser-as-a-Service**: Browserless, Hyperbrowser for resource-constrained environments

## The Security Tension

Browser automation dramatically expands agent capability and attack surface. A compromised agent with browser access can steal sessions, exfiltrate data, and execute arbitrary JavaScript. The OpenClaw lesson applies: capability without proportional security investment is liability.

## Related

- [[browser-verification]] — Playwright-based verification as quality gate
- [[playwright-analysis]] — Testing framework deep dive
- [[claude-code-capabilities]] — Agent platform with native browser support
- [[agent-native-operations]] — Tools designed for AI-human partnership
