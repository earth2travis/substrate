---
title: "Research Dump: Agent Harness Architecture & Primitives"
date: 2026-05-20
source_type: web_research
status: raw
---

# Agent Harness Architecture & Primitives

A collection of sources from open tabs, processed May 2026. These are raw captures. Synthesis and cross-referencing to follow.

---

## 1. The /goal Primitive

**Source:** X post by @Saboo_Shubham_ (2026-05-14)
**URL:** https://x.com/Saboo_Shubham_/status/2054988166541770782

Core claim: /goal is not a feature. It is a primitive, like HTTP or JSON. Codex CLI added it. Claude Code added it. Hermes Agent has had it.

What /goal actually is:
- A regular prompt asks an agent for the next response. You steer every turn.
- /goal flips that. You write down what "done" looks like, submit it once, and the agent works toward it until it gets there.
- The goal stays active until achieved, paused, blocked, cleared, or budget runs out.
- Shift from prompting (you driving) to assigning (the agent driving toward a target).

Example:
/goal Build the app described in SPEC.md. Done means tests pass, build passes, README is accurate, and git status only shows relevant project files.

Three tools that speak /goal:
1. Codex (OpenAI's coding CLI)
2. Claude Code (Anthropic's coding CLI)
3. Hermes Agent (orchestrator)

What /goal needs next:
- A common schema
- A shared registry of verified goal types
- A protocol for handing off goals between tools

**Sivart note:** This directly validates the Mission Contract philosophy. The "common schema" and "handoff protocol" are exactly what we are building. The convergence of /goal across Codex, Claude Code, and Hermes is signal.

---

## 2. What Is an Agent Harness

**Source:** X post by @aparnadhinak (2026-04-25)
**URL:** https://x.com/aparnadhinak/status/2046980769747533830

A harness is NOT a framework. LangChain and LangGraph are frameworks for humans to build agents. A harness is born bottom-up from coding agents solving real problems.

Products that are harnesses: Cursor, Claude Code, Windsurf, Codex. They independently converged on similar architectures while solving the same problem: make an LLM write and edit real code across real repositories.

Harness Architecture (1.0):
1. Outer Iteration Loop — the while loop. Model decides what tools to call. Iterates until done.
2. Context Management & Compression — what to pull into context, how to simplify large data.
3. Skills/Tools Management — tool registry, composition, data passing.
4. SubAgent Management — spawning child agents when tasks get too big.
5. Built-in pre-packaged skills.
6. Session Persistence and Recovery.
7. System Prompt Assembly / Project Context Injection.
8. Life Cycle Hooks.
9. Permission & Safety Layer.

Key distinction: A harness works out of the box. It ships as a working agent with fixed architecture. No assembly step. It is designed for the agent to accomplish almost any task, not for humans to configure agents.

**Sivart note:** Best taxonomy I've seen. These nine components should be a checklist for any agent system we evaluate or build.

---

## 3. The Harness Is the Backend

**Source:** X post by @mfpiccolo (2026-04-27)
**URL:** https://x.com/mfpiccolo/status/2049139067359568032

Core thesis: The most important architectural question is not which model to use, but how much infrastructure is required to build something useful with it.

The spectrum of harness thickness:
- Anthropic: thin harness. Elegant loop: assemble prompt, call model, execute tools, repeat. Model decides everything.
- OpenAI: more structure. Instruction stacks, orchestration modes, explicit handoffs.
- CrewAI: multi-pronged. Deterministic Flows for routing, autonomous agents for the rest.
- LangGraph: biggest harness. Every decision is a node, every transition an edge.

Spectrum: strongly trust the model, weakly encode logic <-> weakly trust model, strongly encode logic.

Hidden assumption: the harness is extrinsic to the traditional backend. This is temporary. A backend has three elements: workers that orchestrate work, triggers that invoke services, and functions that do the work. The harness and backend will merge.

**Sivart note:** The "thin vs thick harness" spectrum is a useful eval frame. Mike Piccolo's company ii is building the unified layer. Worth tracking.

---

## 4. Agentic Harness Engineering

**Source:** X post by @omarsar0 (2026-04-29), paper arxiv.org/abs/2604.25850
**URL:** https://x.com/omarsar0/status/2049492169887748365

A framework that makes harness evolution observable. Three layers:
1. Components as revertible files
2. Experience as condensed evidence from millions of trajectory tokens
3. Decisions as falsifiable predictions checked against task outcomes

Results:
- pass@1 Terminal-Bench 2: 69.7% -> 77.0% in ten iterations
- Beats human-designed Codex-CLI (71.9%) and self-evolving baselines (ACE, TF-GRPO)
- Transfers across model families: +5.1 to +10.1 point gains
- Uses 12% fewer tokens than seed on SWE-bench-verified

Key insight: harness work is the biggest hidden cost in most agent systems. This is the first credible recipe for letting the harness improve itself without drifting into noise.

**Sivart note:** Scientific rigor applied to harness optimization. The "falsifiable predictions" layer is a quality gate mechanism. Could inform Mission Contract validation logic.

---

## 5. Grok Build — xAI's Agentic CLI

**Source:** X post by @xAI (2026-05-14)
**URL:** https://x.com/xai/status/2054993285152989373

An early beta of Grok Build, an agentic CLI for coding, building apps, and automating workflows. Available for SuperGrok Heavy subscribers.

Directly competitive with Claude Code, Codex CLI, and Windsurf. Confirms every major model provider is building a harness.

**Sivart note:** Market validation. The fact that xAI (which started as a "truth-seeking" model company) is now building a coding harness proves the harness is the product, not the model.

---

## 6. Symphony — OpenAI's Agent Orchestrator

**Source:** X post by @OpenAIDevs (2026-04-27)
**URL:** https://x.com/OpenAIDevs/status/2048825010371039648

Symphony: open-source agent orchestrator for Codex. Turns task trackers into always-on systems for agentic work. Humans focus on review and direction.

Tagline: "What if every open issue had a Codex agent?"

**Sivart note:** OpenAI's entry into orchestration. Integrates with issue trackers. Signals the shift from chat to assignment-and-review.

---

## 7. Claude Managed Agents

**Source:** Claude blog post (2026)
**URL:** https://claude.com/blog/new-in-claude-managed-agents

New features: dreaming, outcomes, and multiagent orchestration.
- Dreaming: agents that learn
- Outcomes: meeting a quality bar
- Multiagent orchestration: parallel agent work

**Sivart note:** "Dreaming" sounds like offline learning / skill accumulation. "Outcomes" is goal specification with quality gates. Both align with Mission Contract concepts.

---

## 8. Autobrowse — Browser Agent Memory

**Source:** X post by @kylejeong (2026-05-06)
**URL:** https://x.com/kylejeong/status/2052103973377867913

Problem: Browser agents re-discover every site from scratch on every run. The cost graph is a straight line going up.

Solution: Autobrowse. An agent iterates on a real task until it converges, then graduates the winning approach into a durable, reusable skill (markdown + deterministic glue).

Core loop: Objective -> Run -> Study -> Strategy -> Iterate -> Converge -> Graduate.

Inspired by Karpathy's autoresearch harness. First run is expensive on purpose. It pays for everything after.

Output: a small, readable SKILL.md any future agent can load and execute.

**Sivart note:** This is exactly how we think about skills. The "graduate to SKILL.md" pattern is identical to our skill system. Industry convergence.

---

## 9. Printing Press — CLI Factory

**Source:** X post by @mvanhorn (2026-05-07), website printingpress.dev
**URL:** https://x.com/mvanhorn/status/2052422567181611010
**URL:** https://printingpress.dev/

Thesis: Most APIs, MCPs, and official CLIs suck for agents. They waste tokens and time.

Solution: One command prints a token-efficient Go CLI, a Claude Code skill, an OpenClaw skill, and an MCP server from any API spec, HAR, or URL.

Built by Peter Steinberger (@steipete). Philosophy: a local SQLite mirror beats a remote API call, compound commands beat ten round trips, an agent-native CLI beats raw HTTP.

**Sivart note:** Tool factory for agents. Relevant to our tooling stack. The "local SQLite mirror" pattern is a performance optimization worth understanding.

---

## 10. Coding Agents for Product Management

**Source:** X post by @danshipper (2026-05-01)
**URL:** https://x.com/danshipper/status/2050235671466606665

Marcus (from @every) went from product manager to shipping product like a madman with coding agents. Wrote the definitive guide.

**Sivart note:** Signals coding agents are now being used for end-to-end product management and shipping, not just code generation. The practice is maturing.

---

## Raw HTML Captures

The following raw HTML files are preserved in this directory:
- `claude_managed_agents.html` — Full blog post
- `champion_kit.html` — Claude Code Champion Kit docs
- `printingpress.html` — Printing Press website
- `x_posts_raw.json` — Structured JSON of all X posts
