---
title: missions-site deploy debugging card trail
source: kanban://t_340d7b29 (board ~/.hermes/kanban.db), repo github.com/earth2travis/missions-site
ingested: 2026-06-11
tags: [cloudflare, wrangler, vinext, deployment, debugging, missions]
related: [[cloudflare-first-agent-factory]], [[deployment-governance]]
---

# missions-site deploy debugging card trail

> Evidence record extracted from Kanban card t_340d7b29 (mission missions-site),
> its comment trail, and the missions-site repo commit history, 2026-06-11.
> Captured for Substrate because two of its findings have shelf life beyond the
> mission. The AAR lives at missions/missions-site.aar.md in the missions repo.

## Context

Mission: deploy a vinext 0.1.1 (Cloudflare's Vite plugin reimplementing the
Next.js API surface) site to Cloudflare Workers. The deploy card completed
claiming the site live; the site was in fact serving Cloudflare's "There is
nothing here yet" placeholder on every path. Roughly 8 hours of
operator-authorized direct-fix debugging followed, in three hypothesis cycles.

## Evidence trail

### Failure signature (card comment, 07:29 UTC)

- All routes 404; live page is Cloudflare's placeholder, NOT the worker's own 404.
- Cloudflare API: deployed version shows `handlers: []` (no fetch handler
  detected on the main module).
- Script metadata: `deployment_id: ""` empty, despite the deployments list
  showing a version at 100%.
- Forced deployment POST via API accepted (id c18cd9ce) — changed nothing.
- workers.dev subdomain enabled, toggled off/on — no effect.
- Reproduced even when deploying via `npx vinext deploy` (vinext's own path,
  version d6ec5478) and with vinext's generated `worker/index.ts` entry that
  contains a literal `export default { fetch }`.

### Root cause 1 (card comment, 13:54 UTC; commit 8d3ae28)

The repo was pinned to wrangler 3.114.17. Wrangler 3 cannot statically detect
the default fetch handler in vinext 0.1.1's server bundle, which exposes it
through a minified re-export chain (`export{...,xD as default,...}`). It
uploads the script with `handlers: []`; Cloudflare never recognizes an active
fetch-handling deployment and workers.dev serves its placeholder for ALL paths.
Fix: `npm install -D wrangler@4` (4.99.0), redeploy identical config
(`main: dist/server/index.js`). Version f420c4c1: all nine routes 200.

### Root cause 2, unmasked by fixing root cause 1 (card comment, 14:19 UTC; commit 1cdb213)

`run_worker_first: true` had been added to the wrangler config's assets block
during an earlier hypothesis. While wrangler 3 was failing silently, this
misroute was invisible — nothing was being served at all. Once wrangler 4
activated the worker, every request including `/_next/static/*` was routed
into the SSR worker, which has no asset routes and returned text/plain 404
for every hashed asset (stylesheet, JS chunks). The favicon survived only
because the server bundle carried its own copy.

Fix: `run_worker_first` as a rule array:

```json
"run_worker_first": ["/*", "!/_next/static/*", "!/favicon.svg"]
```

Pitfall found en route: wrangler rejects an array of only negative rules with
"Only negative `run_worker_first` rules were provided; must provide at least
1 non-negative rule." At least one positive rule is mandatory.

Verified (version 1665b52b): full asset graph 200 with correct content-types,
nine routes 200, unknown paths return the worker's SSR 404 page.

### Diagnostic method note

The decisive disproof of the initial "build drift" hypothesis was running
`wrangler dev` against the same config locally: the asset 404 reproduced on
localhost, eliminating every deployment-side explanation in one step.
