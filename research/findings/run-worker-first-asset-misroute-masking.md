---
title: "run_worker_first Misroutes Static Assets and Can Hide Behind Other Failures"
tags: [finding, cloudflare, wrangler, workers, assets, routing, deployment, debugging]
related:
- wrangler-3-vinext-handler-detection-failure
- cloudflare-first-agent-factory
- deployment-governance
source: research/raw/2026-06-11-missions-site-deploy-debugging.md
ingested: 2026-06-11
---

# run_worker_first Misroutes Static Assets and Can Hide Behind Other Failures

## Core Claim

In a Cloudflare Workers config with static assets, `run_worker_first: true`
routes **every** request — including `/_next/static/*` hashed assets — into
the worker script instead of the asset layer. An SSR worker with no asset
routes returns text/plain 404 for every stylesheet and JS chunk while HTML
routes serve normally: a styled-less site that "works." The fix is the rule
array form, which keeps worker-first routing for pages while exempting assets:

```json
"assets": {
  "run_worker_first": ["/*", "!/_next/static/*", "!/favicon.svg"]
}
```

Pitfall inside the fix: wrangler rejects an array containing only negative
rules ("must provide at least 1 non-negative rule"). The positive `"/*"` is
mandatory, exemptions are carved out of it.

## The Masking Pattern

The misconfiguration was introduced as a debugging hypothesis while a
*different* failure (wrangler 3 uploading the worker with no detected handler,
see [[wrangler-3-vinext-handler-detection-failure]]) made the worker entirely
inert. While nothing was being served, the misroute was invisible — it
produced no distinct symptom on top of total failure. The moment the deeper
failure was fixed, the misroute surfaced as a fresh regression: stylesheet
404, favicon flipping from 200 to 404.

This is the general shape worth keeping: **a config change made while the
system is dead cannot be validated by the system staying dead.** Hypotheses
applied during an outage and not reverted become landmines that detonate when
the outage ends. Two corollaries: revert unproven hypotheses before stacking
the next one, and after any layered fix, re-verify the *full* artifact graph
(every href/src with content-types), not just the routes that were failing.

## Diagnostic Shortcut

`wrangler dev` against the same config reproduced the asset 404 on localhost,
eliminating every deployment-side explanation (caching, propagation, account
state) in one step. When a deployed Worker misbehaves, reproducing against
local `wrangler dev` is the cheapest bisection between config and platform —
the same boundary-finding move as [[browser-verification]]: verify at the
layer below before theorizing about the layer above.
