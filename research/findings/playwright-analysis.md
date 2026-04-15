---
title: Playwright Research
tags:
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/playwright-analysis.md
---

# Playwright Research

Source: https://playwright.dev/docs/intro

## What It Is

End-to-end testing framework by Microsoft. Automates Chromium, Firefox, and WebKit browsers. Node.js based. Free, open source.

## Core Capabilities

- **Browser automation**: Navigate pages, click elements, fill forms, assert state
- **Auto-waiting**: Waits for elements to be actionable before interacting (no manual waits, no flakiness)
- **Test isolation**: Every test gets a fresh browser context (like an incognito profile)
- **Parallel execution**: Tests run in parallel across browsers by default
- **Codegen**: Record browser interactions and auto-generate test code
- **Trace viewer**: Time-travel debugging with screenshots at every step
- **API testing**: Built-in `request` fixture for testing APIs without a browser
- **GitHub Actions**: First-class CI integration with artifact upload for HTML reports

## API Surface (Key Patterns)

```javascript
const { chromium } = require('playwright');

const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('https://example.com');

// Locators (find elements)
await page.getByRole('link', { name: 'Get started' }).click();
await page.getByLabel('Username').fill('admin');

// Assertions (verify state)
await expect(page).toHaveTitle(/Expected/);
await expect(page.getByRole('heading')).toBeVisible();
await expect(page.getByText('Success')).toContainText('done');

await browser.close();
```

## Fixture System

Tests declare what they need as function parameters. Playwright provides it, isolated per test:
- `page`: Isolated browser page
- `context`: Isolated browser context
- `browser`: Shared browser instance
- `request`: Isolated API request context

Custom fixtures extend `test` to provide domain objects (Page Object Model pattern).

## Why This Matters for Us

### 1. Product Verification Skills (Thariq Type 2)
Our biggest skill gap. Playwright is exactly the tool for building verification skills:
- **PR verification**: Navigate to GitHub PR page, verify CI status, check labels, verify linked issues
- **Blog verification**: Load transmissions.sivart.wtf, verify posts render, check links
- **Deployment verification**: After deploy, programmatically verify the site works

### 2. Intercom's Verification Pattern
From our Intercom research (#441): "signup-flow-driver runs through signup, email verify, onboarding in a headless browser with hooks for asserting state at each step." This IS Playwright.

### 3. Data Collection for Skill Optimizer
The skill-optimizer (#453) scores skill outputs. Playwright could verify that skills producing web-facing artifacts actually work (e.g., does the blog post skill produce a page that renders correctly?).

### 4. Headless on Our VPS
Playwright runs headless on Linux. Our Hetzner VPS (Ubuntu 24.04, 2GB RAM) can run it. The `--with-deps` flag installs system dependencies automatically.

### 5. GitHub Actions Integration
We already have CI. Adding Playwright tests to our workflow is a YAML addition. Test reports upload as artifacts automatically.

## Installation on Our Stack

```bash
npm init playwright@latest  # Interactive setup
npx playwright install --with-deps  # Download browsers + system deps
```

**Concern:** Browser binaries are large (~400MB for Chromium alone). On our 40GB NVMe with 37% used, this is fine. On RAM-constrained VPS (2GB), headless mode is essential.

## What We Could Build

| Skill | What Playwright Does | Value |
|-------|---------------------|-------|
| site-verifier | Load URL, check renders, assert content | Blog/deploy verification |
| pr-babysitter | Poll GitHub PR page, check CI badges, retry | Automated CI monitoring |
| visual-regression | Screenshot comparison across deploys | Catch UI breakage |
| link-checker | Crawl site, find broken links | Content quality |
| accessibility-audit | Run axe-core via Playwright | Compliance |

## Constraints

- **Not for API-only work**: Our GitHub interactions are better via `gh` CLI than browser automation
- **Memory**: Each browser context uses ~50-100MB RAM. Limit concurrent contexts on 2GB VPS
- **Token cost**: Thariq warned that MCP browser tools burn 30-40K tokens per session. Playwright scripts are cheaper since they run as code, not as model-driven browser interactions
- **Setup weight**: Installing browser binaries is a one-time cost but adds deployment complexity

## Recommendation

Install Playwright. Use it for verification skills (Type 2 gap). Start with a simple site-verifier that checks our blog after deploys. Build toward the pr-babysitter pattern from Thariq's taxonomy.

Don't use Playwright where `gh` CLI or `curl` suffice. Browser automation is for visual/interactive verification, not API calls.
