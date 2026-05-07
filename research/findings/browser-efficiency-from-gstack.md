---
title: "Browser Efficiency Patterns from gstack"
tags: [browser, efficiency, gstack, claude-code, performance]
related:
- gstack-analysis
- tools-landscape
- agent-native-operations
- cloudflare-first-agent-factory
source: research/raw/browser-efficiency-from-gstack.md
---
# Browser Efficiency Patterns from gstack

## Summary

gstack's browse skill uses a persistent headless Chromium daemon via compiled Playwright binary. First call starts the server (~3s). Every subsequent call: ~100-200ms. Browser stays running between commands with cookies, tabs, and localStorage carrying over. Auto-shutdown after 30 min idle.

This is dramatically faster than MCP browser tools or Chrome extension relay. In a 20-command browser session, MCP tools burn 30,000-40,000 tokens on protocol framing alone. gstack burns zero. The key patterns: navigate once then query many times, use snapshot -i for ref-based interaction instead of CSS selector hunting, use js for precision queries, use chain for multi-step flows in a single CLI invocation, and use responsive for layout checks across breakpoints.

For Synthweave's browser automation needs (checking deployments, reading docs), the actionable improvements are: batch browser operations by planning full sequences upfront, always snapshot before interacting using refs, systematically screenshot + Read for visual verification, and check console/network after navigation. The compiled binary approach is interesting for Loom but would require custom build effort.
