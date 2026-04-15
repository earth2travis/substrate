---
title: "George Hotz | Programming | Welcome to Gas Town and the future of Computer Use"
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/2026-03-01-george-hotz-gastown-computer-use.md
---

# George Hotz | Programming | Welcome to Gas Town and the future of Computer Use

**Source:** [YouTube – Agentic AI Part 1](https://www.youtube.com/watch?v=awOxxHnsiv0)  
**Meeting:** Agentic AI exploration and open source model testing  
**Date:** Mar 1

---

## Introduction

New setup, first time streaming from a non‑Mac. Living in Hong Kong; South Dakota resident in the US. Moved out of California. Tiny Corp has a subsidiary in Hong Kong. Opening an office for Tiny Grad with 90 amps of 220V power. Using Omarc Hyprland.

Train metaphor (from Japan): if there’s a train leaving, you gotta get on it. There might not be another one for two hours. Get on the train.

---

## Tools and Context

**Multbook** – Social network for AI agents. Need Open Claw to use it.

**Open Claw** – Rebranded three times: Open Claude (Anthropic threatened to sue), Molt Bot, now Open Claw. The AI that actually does things.

**Gastown** – New take on the IDE. Still under active development.

Using Open Cursor with Claude Opus. It lacks taste and can’t program well, but it’s persistent. Same pressure everyone feels: adapt now or get left behind. Not sure that’s true, but worth understanding what’s going on.

**Agent psychosis** – There’s a post about it. Leaning into it. Embrace the slop: curl pipe to bash, log in with everything. The era of care and the error of slap. You can embrace the slop or try to avoid it, but you can’t deny it’s where things are.

---

## Gastown Setup

- `brew install Gastown` (needed Go first)
- Identified missing dependency: beads
- `install beads yeage` – quick install script
- Workspace: `get initialization`
- Mayor, deacon, rigs all running
- AI tooling feels like maximalist software, similar to hyper pop

**Beads architecture:** Polecats, refinery, witness, Deacon, misters, convoys. You can use polecats without the refinery, even without the witness or Deacon. Tell the mayor to shut down the rig and sling work to the polecats with the message to merge to main directly. Polecats can submit misters; mayor merges manually. Refinery is useful if you’ve done upfront spec work and have huge piles of beads to churn through with convoys.

---

## Tiny Grad and Agentic Coding

Tiny Grad leans heavily on agentic coding. Two tiers:

1. Lower‑quality, AI‑assisted code that enables more functionality
2. Higher‑quality code, e.g. DSL for AMD GPU assembly and emulation

Proud of: fast matmul for RDMA3 cards using a Python DSL for AMD assembly, with type checking and testability. Very amenable to agentic coding.

---

## Computer Use Models

Computer use models were inevitable. Eventually you won’t control the machine; a model will sit on top. Had something similar in Tiny Grad (Python calls), but tool use has gotten much better.

Claude Code quality is impressive, likely from long‑context RL in similar environments.

**Kimmy** – Chinese open‑source model. Post‑training: SFT then joint RL. Probably SFT on many Claude Opus traces, then RL. Repo shows the full LLM training pipeline.

RL with verifiable rewards as the future (per Karpathy ~1.5 years ago).

---

## Agent Swarms and Future Vision

Agentic RL: Kimmy built a gym‑like environment. Checkpoint described but not open source.

Society: this is about more than coding; it affects sleep, habits, workflows. Permissions everywhere; security assumptions are shifting.

**Filtering and agents:** Brands will sit behind agents. You won’t care if it’s WhatsApp, Telegram, Signal, Twitter, or Instagram; your agent will filter everything before you see it. That includes ads.

**Alignment:** Likely fine. Easy to swap Claude for Kimmy; API surface is small (tokens in, tokens out). When models become commodities, single‑provider lock‑in weakens.

**Interface:** Power users use terminals and multiple tmux panes. These models behave more like that than like mouse‑click UIs.

Open‑source models are available (e.g. on Open Router). Kimmy K2.5 ran at 3 tok/s on Mi 300 Xbox. Commoditization helps avoid worst‑case lock‑in.

**AI slop vs wokeism:** This isn’t like wokeism. Wokeism makes shit art; everything it touches becomes cringy. But with this software, unclear whether it’s a phase or the future. Different outcome possible.

---

## Open Claw Configuration and Troubleshooting

- Model: Open Router → Kimmy K2.5
- Gateway service initialized
- Initial run: no output (possible streaming bug)
- Web UI vs TUI: gateway token via dashboard

**Kimmy rate limiting:** Open Router returned “temporarily rate limited” for Kimmy. Switched to Claude Haiku (works). Tried Fireworks for Kimmy (no luck). Settled on GLM 4.7 via Together as provider.

**GLM 4.7:** Not in Open Claw’s allowed list. Added to `open_claw.json`, fixed JSON syntax, restarted gateway. Model responded: “Hey, I just. Let me get oriented first, okay? What model is this? How do you know that? I love AI. It’s in the runtime. Information that was provided to me. Very cool. Plus I saw a system notification you demand.”

Conclusion: Kimmy broken on Open Router; GLM 4.7 works. Possible next step: run Qwen 2.5 72B locally on Tiny Box. Which Tiny Boxes: Mac Studios, AMD boxes (non‑Nvidia). Target: 100 tok/s on AMD (vs 3 tok/s on Mi 300); Kimmy on two Mac Studios would be ~3 tok/s.

---

## Conversation: Open Claw and Browser

> **Them:** Can you access the George Hot Twitch stream?

> **Me:** When. I.

> **Them:** The browser control isn’t running yet.

> **Me:** Love. Me.

> **Them:** I can try fetching the page content. Twitch is heavily JavaScript. Let’s browser. Help me. What do you mean, help me? I just want you to do it.

---

## Gastown Rig Setup

- Beads installed and in path
- `gt rig add` for project tinygrad
- Rig created
- Creating crew workspace
- Mayor: “Tell the mayor what I want to build” – needs API keys again
- Desire: run Kimmy locally on AMD boxes, target ~100 tok/s
- Timeout waiting for mayor; no agents running
- Attempted to start mayor; may require starting processes manually

**Blocker:** Gastown appears to need Claude Code runtime. Only Open Cursor installed. Claude Code unavailable. Mayor logs show deprecation warnings. Anthropic blocks in Hong Kong (Tailscale) may affect stream/connectivity.

> **Me:** To. Be. By. My side. Now. I need you. Tell. Me. The truth.

---

## Meta Notes

- Vibe‑coded tools often fragile: escape broken in Open Cursor, clipboard doesn’t work
- Ctrl+C in one Open Cursor can kill all Open Cursor instances (“Oh, it killed all the open codes. All the open codes died”)
- Cost/risk mitigation: Open Router capped at $20 credit
