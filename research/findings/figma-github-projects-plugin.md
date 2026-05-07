---
title: "Figma + GitHub Projects v2 Plugin: Research Findings"
tags: [figma, github, plugin, dev-mode, integration]
related: [github-as-memory, project-board-configuration, github-capabilities-audit]
source: research/raw/figma-github-projects-plugin.md
---

# Figma + GitHub Projects v2 Plugin: Research Findings

## Summary

Research into building a Figma plugin that bridges design and GitHub Projects v2, covering Figma's dual-thread architecture, Dev Mode inspect panel capabilities, GitHub's GraphQL API constraints, and competitive analysis against Jira/Linear/Asana plugins.

## Key Insights

### Figma Plugin Architecture

Plugins run in a dual environment: a minimal sandbox (ES2020+, no browser APIs) and a UI iframe (full browser environment). Communication happens via postMessage. Dev Mode plugins can take over the inspect panel, showing contextual data when a developer selects a frame.

### Dev Mode Integration

Dev Mode plugins are read-only on the document but CAN write pluginData metadata to nodes. This enables linking Figma frames to GitHub issues by storing issue IDs as node metadata. Selectionchange events allow reactive updates.

### GitHub Projects v2 API

Exclusively GraphQL. Supports custom fields (text, number, date, single select, iteration). Key mutations: addProjectV2ItemById, updateProjectV2ItemFieldValue. Rate limit: 5,000 points/hour.

### Critical CORS Constraint

GitHub's GraphQL API does NOT set Access-Control-Allow-Origin: *. Direct calls from a Figma plugin iframe (null origin) fail. A backend proxy is mandatory. Recommended architecture: Cloudflare Worker (stateless, low cost) for v1, migrating to GitHub App for v2.

### Competitive Landscape

Jira plugin is the gold standard with inspect panel integration, bidirectional linking, and status updates. Linear and Asana plugins exist but are simpler. No well-maintained GitHub Projects v2 plugin exists. This is a clear market gap.

### Auth Recommendation

GitHub App with user authorization flow. Fine-grained permissions, short-lived tokens, ability to request only project:read and project:write scopes. Alternative: OAuth App or PAT for individual use.

## Architecture Options

| Option | Backend | Pros | Cons |
|--------|---------|------|------|
| A | Managed SaaS | Best UX, webhooks | Hosting cost, privacy |
| B | Self-hosted | Data sovereignty | High friction |
| C | Cloudflare Worker | Low cost, minimal attack surface | Limited server features |
| D | GitHub App | Best security model | Complex setup |

**Recommended:** Option C for v1, migrate to D for v2.

## Synthesis

A Figma plugin for GitHub Projects v2 is technically feasible and addresses a clear gap. The CORS requirement makes a backend proxy non-negotiable. Starting with a stateless Cloudflare Worker minimizes operational burden while proving the value of design-to-issue linking.
