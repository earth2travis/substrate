# Browser Efficiency Patterns (from gstack)

**Source:** [github.com/garrytan/gstack](https://github.com/garrytan/gstack)
**Filed:** 2026-03-11

## Architecture

Persistent headless Chromium daemon via compiled Playwright binary. First call starts the server (~3s). Every subsequent call: ~100-200ms. Browser stays running between commands. Cookies, tabs, localStorage carry over. Auto-shutdown after 30 min idle.

This is dramatically faster than MCP browser tools or Chrome extension relay.

## Speed Rules (directly applicable)

1. **Navigate once, query many times.** `goto` loads the page, then `text`, `js`, `css`, `screenshot` all run against the loaded page instantly. Don't reload for each query.

2. **Use `snapshot -i` for interaction.** Gets refs for all interactive elements, then click/fill by ref. No CSS selector guessing.

3. **Use `js` for precision.** `js "document.querySelector('.price').textContent"` is faster than parsing full page text.

4. **Use `links` to survey.** Faster than `text` when you just need navigation structure.

5. **Use `chain` for multi-step flows.** JSON array of commands, single CLI invocation. Avoids per-command overhead.

6. **Use `responsive` for layout checks.** One command = screenshots at mobile/tablet/desktop.

## Command Patterns Worth Adopting

### QA Flow
```
goto URL → snapshot -i → fill @ref "value" → click @ref → screenshot → Read screenshot
```
22 tool calls, ~60 seconds for full signup/navigation/verification flow.

### Debugging
```
goto URL → console (check errors) → network (check requests) → screenshot
```

### Form Interaction
```
snapshot -i → fill @e2 "email" → fill @e3 "password" → click @e5 → screenshot
```
Ref-based interaction is faster and more reliable than CSS selector hunting.

### Page Comparison
```
diff url1 url2
```
Text diff between two pages in one command.

## What This Means for Us

### Current State
We use OpenClaw's browser tool, which works but:
- Each action is a separate tool call with overhead
- No persistent session between calls
- No compiled binary, runs through the OpenClaw abstraction layer
- No `chain` equivalent for batching commands

### Applicable Improvements

1. **Batch browser operations.** When doing QA or page checking, plan the full sequence upfront instead of one action at a time. Our browser tool supports `act` which can be used for multi-step flows.

2. **Snapshot-first interaction.** Always snapshot before interacting. Use refs instead of guessing selectors. We already have this via OpenClaw's snapshot with `refs="aria"`.

3. **Screenshot + Read for visual verification.** The pattern of taking a screenshot and then reading it (via image analysis) is how the agent "sees" the UI. We should do this more systematically when checking deployments or verifying changes.

4. **Console/network inspection.** After navigation, check console for errors. We have `browser(action="console")` available but rarely use it.

5. **The compiled binary approach.** For Synthweave's Loom orchestration, having a fast persistent browser daemon (like gstack's) could be a building block. ~100ms per command vs current tool-call overhead would be a significant speedup for any agent that needs to interact with web UIs.

## Not Directly Applicable

- gstack is built for Claude Code (local CLI), not OpenClaw (remote gateway). The compiled binary approach doesn't directly translate.
- Our browser automation needs are different: we're checking deployments and reading docs, not doing full QA flows on our own apps.
- The Playwright daemon architecture is interesting for Loom but would be a custom build.
