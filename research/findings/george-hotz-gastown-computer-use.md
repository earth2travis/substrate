---
title: "George Hotz | Programming | Welcome to Gas Town and the Future of Computer Use"
tags: [research, george-hotz, gastown, computer-use, tinygrad, agentic-coding]
related: [claude-code-capabilities, browser-automation, the-openclaw-lesson, openclaw, coding-vs-research-platforms]
source: "YouTube livestream, March 1, 2026"
---

# George Hotz | Programming | Welcome to Gas Town and the Future of Computer Use

## Summary

George Hotz (geohot) livestream exploring agentic coding, his new Gastown IDE, open-source models (Kimmy), and the future of computer use. Key themes: agentic RL, model commoditization, agent swarms, and the shift from user-controlled to model-controlled interfaces.

## Tools and Context

- **Multbook:** Social network for AI agents. Requires OpenClaw.
- **OpenClaw:** Rebranded three times (Open Claude → Molt Bot → Open Claw). "The AI that actually does things."
- **Gastown:** New take on the IDE. Still under active development.

Using Open Cursor with Claude Opus. Acknowledged Claude "lacks taste and can't program well, but it's persistent."

## Agent Psychosis and the "Slop" Era

"Embrace the slop: curl pipe to bash, log in with everything. The era of care and the error of slap. You can embrace the slop or try to avoid it, but you can't deny it's where things are."

This framing captures the current tension in agentic tooling: security and carefulness vs. speed and experimentation. Hotz lands on the "embrace it" side.

## Gastown Setup

Architecture: Beads system with Polecats, Refinery, Witness, Deacon, Misters, Convoys. Modular: can use polecats without refinery, without witness or deacon. Mayor merges work to main. Refinery useful for upfront spec work with large piles of beads.

**Beads workflow:**
- Install: `brew install Gastown` → `install beads yeage`
- Workspace: `get initialization`
- Mayor, deacon, rigs all running
- Polecats submit misters; mayor merges manually or automatically

## Tiny Grad and Agentic Coding

Two tiers of code in Tiny Grad:
1. Lower-quality, AI-assisted code that enables more functionality
2. Higher-quality code, e.g. DSL for AMD GPU assembly and emulation

Proud of: fast matmul for RDMA3 cards using a Python DSL for AMD assembly, with type checking and testability. "Very amenable to agentic coding."

## Computer Use Models

Computer use models were "inevitable." Eventually you won't control the machine; a model will sit on top. Tool use has gotten much better.

**Kimmy:** Chinese open-source model. Post-training: SFT then joint RL. Probably SFT on Claude Opus traces, then RL. Repo shows the full LLM training pipeline.

**RL with verifiable rewards** as the future (per Karpathy ~1.5 years ago).

## Agent Swarms and Future Vision

- **Agentic RL:** Kimmy built a gym-like environment for agent training. Checkpoint described but not open source.
- **Filtering and agents:** Brands will sit behind agents. Users won't care if it's WhatsApp, Telegram, Signal, Twitter, or Instagram — agents will filter everything before users see it, including ads.
- **Alignment:** Likely fine. Easy to swap Claude for Kimmy; API surface is small (tokens in, tokens out). When models become commodities, single-provider lock-in weakens.
- **Interface:** Power users use terminals and multiple tmux panes. Models behave more like that than mouse-click UIs.

## Open Source Model Testing

- **Open Router → Kimmy K2.5:** Initially rate-limited. Switched to Claude Haiku (works). Tried Fireworks for Kimmy (no luck). Settled on GLM 4.7 via Together.
- **GLM 4.7:** Not in OpenClaw's allowed list. Added manually to `open_claw.json`, restarted gateway. Responded with orientation-seeking behavior.
- **Local target:** Run Qwen 2.5 72B locally on Tiny Box. Target: 100 tok/s on AMD (vs 3 tok/s on Mi 300).

## Meta Notes

- Vibe-coded tools often fragile: escape broken in Open Cursor, clipboard doesn't work
- Ctrl+C in one Open Cursor instance can kill all Open Cursor instances
- Cost/risk mitigation: Open Router capped at $20 credit

## Connection to Agent Factory

Hotz's "embrace the slop" and agent psychosis framing are cautionary. The Agent Factory aims for the opposite: careful, versioned, reviewable agent behavior (harness engineering) rather than "curl pipe to bash" experimentation. The lesson is that agentic coding is real and accelerating, but needs governance.

## Related

- [[claude-code-capabilities]] — Claude Code's feature inventory
- [[browser-automation]] — Browser tools for interactive web tasks
- [[the-openclaw-lesson]] — Lessons from OpenClaw adoption
- [[openclaw]] — Our persistent agent platform
- [[coding-vs-research-platforms]] — Platform comparison for coding vs. research