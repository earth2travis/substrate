---
title: "Wrangler 3 Silently Fails to Detect vinext's Re-Exported Fetch Handler"
tags: [finding, cloudflare, wrangler, vinext, deployment, debugging, tooling]
related:
- cloudflare-first-agent-factory
- deployment-governance
- harness-engineering
source: research/raw/2026-06-11-missions-site-deploy-debugging.md
ingested: 2026-06-11
---

# Wrangler 3 Silently Fails to Detect vinext's Re-Exported Fetch Handler

## Core Claim

Wrangler 3.x cannot statically detect a Worker's default fetch handler when it
is exposed through a minified ESM re-export chain, the shape vinext 0.1.1's
server bundle produces (`export{...,xD as default,...}`). The deploy succeeds
by every visible signal — assets upload, "Deployed" prints, a version id is
issued — but the script is uploaded with `handlers: []`, Cloudflare never
activates a fetch-handling deployment, and workers.dev serves its "There is
nothing here yet" placeholder on every path. Upgrading to wrangler 4 (4.99.0)
fixed it with zero config changes.

## Failure Signature

Recognize this exact case by the conjunction:

- Every route 404, and the 404 page is **Cloudflare's placeholder**, not the
  worker's own error page. Whose 404 you are looking at is the single most
  diagnostic bit.
- API: deployed version reports `handlers: []`; script metadata shows
  `deployment_id: ""` even though the deployments list shows a version at 100%.
- Forcing a deployment via API POST succeeds and changes nothing; toggling the
  workers.dev subdomain changes nothing.
- Reproduces identically via `npx vinext deploy` and via an entry file with a
  literal `export default { fetch }` — because the same local wrangler 3 does
  the upload in every path. Three "different" deploy strategies failing
  identically was itself the clue that the fault sat below all of them.

## Why It Matters

This is a tool-rot failure with a deceptive surface: the toolchain reports
success while shipping a dead artifact. Three hypothesis cycles and ~8 hours
went to ruling out config, entry-point shape, and vinext's own deploy path
before the version pin surfaced. The lesson generalizes past wrangler:
**"the deploy tool said success" is evidence about the tool, not the edge.**
Liveness criteria must be verified from outside the deploy toolchain, and a
worker that cannot run its verification must block, not complete. The repo
carried `wrangler: ^3.0.0` from scaffold time; vinext is young software whose
bundle shape evolved past what wrangler 3's static analysis could see — the
version-skew trap described in [[harness-engineering]]: capability assumptions
encoded in pinned tooling decay silently.

## Operational Rule

When a Workers deploy "succeeds" but the placeholder serves: check whose 404
it is, then check `handlers` on the deployed version via API, then check the
wrangler major version — before touching config. Fix order: upgrade wrangler
first, rediagnose second. Per [[deployment-governance]], deploy gates should
require an out-of-band HTTP 200 as the completion artifact, never the deploy
tool's exit status.
