---
title: "Playwright Analysis"
tags: [research, playwright, testing, browser-automation, verification]
related: [browser-automation, claude-code-capabilities, skills-as-portable-knowledge, agent-native-operations, browser-verification]
source: "https://playwright.dev/docs/intro, research notes February 2026"
---


# Playwright Analysis

## Summary

End-to-end testing framework by Microsoft. Automates Chromium, Firefox, and WebKit browsers. Node.js based, free and open source. Best suited for verification skills: PR verification, blog validation, deployment checks, visual regression.

## Core Capabilities

- **Browser automation:** Navigate pages, click elements, fill forms, assert state
- **Auto-waiting:** Waits for elements to be actionable before interacting (no manual waits, no flakiness)
- **Test isolation:** Every test gets a fresh browser context (like incognito profile)
- **Parallel execution:** Tests run in parallel across browsers by default
- **Codegen:** Record browser interactions and auto-generate test code
- **Trace viewer:** Time-travel debugging with screenshots at every step
- **API testing:** Built-in `request` fixture for testing APIs without browser
- **GitHub Actions:** First-class CI integration with artifact upload for HTML reports

## API Surface

Locators: `page.getByRole()`, `page.getByLabel()`, `page.getByText()`. Assertions: `toHaveTitle()`, `toBeVisible()`, `toContainText()`.

Fixture system: tests declare needs as function parameters. Playwright provides isolated per-test fixtures: `page`, `context`, `browser`, `request`. Custom fixtures extend `test` for Page Object Model pattern.

## Why This Matters for Agent Factories

### 1. Product Verification Skills (Type 2 Gap)

Playwright is exactly the tool for building verification skills:
- **PR verification:** Navigate to GitHub PR page, verify CI status, check labels, verify linked issues
- **Blog verification:** Load transmissions.sivart.wtf, verify posts render, check links
- **Deployment verification:** After deploy, programmatically verify the site works

### 2. Intercom's Verification Pattern

"signup-flow-driver runs through signup, email verify, onboarding in a headless browser with hooks for asserting state at each step." This IS Playwright.

### 3. Data Collection for Skill Optimizer

The skill-optimizer scores skill outputs. Playwright verifies that skills producing web-facing artifacts actually work (e.g., does the blog post skill produce a page that renders correctly?).

### 4. Headless on VPS

Playwright runs headless on Linux. Hetzner VPS (Ubuntu 24.04, 2GB RAM) can run it. `--with-deps` flag installs system dependencies automatically.

## Potential Skills

| Skill | What Playwright Does | Value |
|-------|---------------------|-------|
| site-verifier | Load URL, check renders, assert content | Blog/deploy verification |
| pr-babysitter | Poll GitHub PR page, check CI badges, retry | Automated CI monitoring |
| visual-regression | Screenshot comparison across deploys | Catch UI breakage |
| link-checker | Crawl site, find broken links | Content quality |
| accessibility-audit | Run axe-core via Playwright | Compliance |

## Constraints

- **Not for API-only work:** GitHub interactions are better via `gh` CLI than browser automation
- **Memory:** Each browser context uses ~50-100MB RAM. Limit concurrent contexts on 2GB VPS
- **Token cost:** MCP browser tools burn 30-40K tokens per session. Playwright scripts are cheaper since they run as code, not model-driven interactions
- **Setup weight:** Browser binaries (~400MB for Chromium) add deployment complexity

## Recommendation

Install Playwright. Use it for verification skills (Type 2 gap). Start with a simple site-verifier that checks the blog after deploys. Build toward the pr-babysitter pattern. Don't use Playwright where `gh` CLI or `curl` suffice. Browser automation is for visual/interactive verification, not API calls.

## Related

- [[browser-automation]] — Browser automation options for AI agents
- [[claude-code-capabilities]] — Claude Code's browser integration and Chrome features
- [[skills-as-portable-knowledge]] — Agent behavior as versioned, composable instructions
- [[agent-native-operations]] — Tools designed for AI-human partnership