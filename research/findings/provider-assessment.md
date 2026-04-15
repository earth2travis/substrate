---
title: Venice AI Provider Assessment
tags:
  - ai-agents
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/provider-assessment.md
---

# Venice AI Provider Assessment

**Date:** 2026-03-09
**Status:** Actionable today for OpenClaw path. Blocked for Claude Code path.

## 1. Venice API Compatibility

**Base URL:** `https://api.venice.ai/api/v1`
**Auth:** Bearer token (`vapi_xxxxxxxxxxxx`)
**Protocol:** OpenAI-compatible `/v1/chat/completions`

| Feature | Support |
|---------|---------|
| Streaming | ✅ All models |
| Function/tool calling | ✅ Most models (check `supportsFunctionCalling`) |
| Vision | ✅ Select models |
| JSON mode | ✅ via `response_format` |
| Prompt caching | ✅ Select models (automatic for system prompts) |

**Claude models available via Venice (anonymized proxy):**

| Model | Venice ID | Input/MTok | Output/MTok | Cache Read | Context |
|-------|-----------|-----------|-------------|------------|---------|
| Claude Opus 4.5 | `claude-opus-4-5` | $6.00 | $30.00 | $0.60 | 198K |
| Claude Opus 4.6 (Beta) | `claude-opus-4-6` | $6.00 | $30.00 | $0.60 | 1000K |
| Claude Sonnet 4.5 | `claude-sonnet-4-5` | $3.75 | $18.75 | $0.38 | 198K |
| Claude Sonnet 4.6 (Beta) | `claude-sonnet-4-6` | $3.60 | $18.00 | $0.36 | 1000K |

**Venice-specific features:** Web search, web scraping, uncensored system prompts, character personas. Can disable Venice system prompt via `venice_parameters.include_venice_system_prompt: false`.

**Privacy:** Claude models are "anonymized" (metadata stripped, proxied through Venice). Open-source models are "private" (no logging at all).

## 2. OpenClaw Provider Configuration

**OpenClaw has first-class Venice support.** There's a dedicated provider doc at `docs/providers/venice.md`.

### Setup (can do today):

```bash
# Option A: Environment variable + onboard
export VENICE_API_KEY="vapi_xxxxxxxxxxxx"
openclaw onboard --auth-choice venice-api-key

# Option B: Non-interactive
openclaw onboard --non-interactive \
  --auth-choice venice-api-key \
  --venice-api-key "vapi_xxxxxxxxxxxx"

# Set model
openclaw models set venice/claude-opus-45
```

### Config file example:

```json5
{
  env: { VENICE_API_KEY: "vapi_..." },
  agents: { defaults: { model: { primary: "venice/claude-opus-45" } } },
  models: {
    mode: "merge",
    providers: {
      venice: {
        baseUrl: "https://api.venice.ai/api/v1",
        apiKey: "${VENICE_API_KEY}",
        api: "openai-completions"
      }
    }
  }
}
```

OpenClaw auto-discovers Venice models when `VENICE_API_KEY` is set. Falls back to static catalog if API unreachable.

## 3. Claude Code CLI with Custom Providers

**Blocked.** Claude Code (`claude` CLI) does **not** support custom API base URLs or third-party providers.

- `claude auth` only supports `login`/`logout`/`status` with Anthropic accounts
- No `--base-url`, `--api-base`, or `ANTHROPIC_BASE_URL` option
- The `--model` flag accepts model aliases (`sonnet`, `opus`) or full Anthropic model names only
- No provider configuration in `~/.claude/settings.json`

Venice wraps Claude behind an OpenAI-compatible API, but Claude Code speaks the Anthropic API natively (not OpenAI-compatible). Even if there were a base URL override, the protocol mismatch would block it.

**Verdict:** Cannot use Venice as a backend for Claude Code CLI.

## 4. Paperclip Adapter Implications

### Path A: OpenClaw Gateway → Venice (✅ Works today)

The `openclaw_gateway` adapter in Paperclip routes through OpenClaw, which can route through Venice. This path:
- Uses OpenAI-compatible protocol throughout
- Supports streaming, tool calling, vision
- Venice provider is first-class in OpenClaw
- Model name would be `venice/claude-opus-45` or `venice/claude-opus-4-6`

**Limitation:** The current OpenClaw setup uses `anthropic/claude-opus-4-6` directly. Switching to Venice would mean routing Claude requests through Venice's anonymized proxy instead of direct Anthropic API. This adds ~10-50ms latency per Venice docs.

### Path B: Claude Code (`claude_local`) → Venice (❌ Blocked)

Cannot use Venice as a backend for Claude Code CLI. The `claude_local` adapter would continue to use Anthropic directly (via Claude Max subscription or API key).

### Recommendation

These are independent paths. The `openclaw_gateway` adapter could use Venice for specific models while `claude_local` continues using Anthropic directly. No either/or needed.

## 5. Pricing Comparison

### Claude Opus 4.5/4.6

| | Input/MTok | Output/MTok | Cache Read/MTok |
|---|-----------|-------------|-----------------|
| **Anthropic direct** | $15.00 | $75.00 | $1.50 |
| **Venice** | $6.00 | $30.00 | $0.60 |
| **Difference** | -60% | -60% | -60% |

Venice is **60% cheaper** than Anthropic direct pricing for Opus 4.5/4.6.

### Claude Sonnet 4.5/4.6

| | Input/MTok | Output/MTok | Cache Read/MTok |
|---|-----------|-------------|-----------------|
| **Anthropic direct** | $3.00 | $15.00 | $0.30 |
| **Venice (4.5)** | $3.75 | $18.75 | $0.38 |
| **Venice (4.6)** | $3.60 | $18.00 | $0.36 |
| **Difference (4.6)** | +20% | +20% | +20% |

Venice is **20% more expensive** for Sonnet.

### Note on our current setup

We currently use Claude Max ($200/mo flat rate via subscription) through `claude_local`, which is effectively unlimited for our usage. The Venice pricing comparison matters for the `openclaw_gateway` path or if we ever need API-based Claude access.

## Summary

| Question | Answer |
|----------|--------|
| Can Venice work as OpenClaw provider? | **Yes, first-class support. Configurable today.** |
| Can Venice work with Claude Code CLI? | **No. Protocol mismatch + no base URL override.** |
| Is Venice cheaper for Opus? | **Yes, 60% cheaper than Anthropic direct.** |
| Is Venice cheaper for Sonnet? | **No, 20% more expensive.** |
| Tool calling supported? | **Yes, on most models.** |
| Streaming supported? | **Yes, all models.** |
| Privacy trade-off? | Claude via Venice is "anonymized" not "private" |
| Latency impact? | +10-50ms per request (proxy overhead) |

## Action Items

1. **If we want Venice for OpenClaw:** Run `openclaw onboard --auth-choice venice-api-key` with a Venice API key
2. **Best use case:** Use Venice for Opus-class tasks through OpenClaw when Claude Max quota is a concern, or for privacy reasons
3. **Not useful for:** Replacing Claude Code CLI backend (blocked by design)
