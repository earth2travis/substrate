---
title: OpenClaw Agent Platform — Deep Research Report
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/openclaw-report.md
---

# OpenClaw Agent Platform — Deep Research Report

> **Date:** 2026-04-11
> **Scope:** History, architecture, security crisis, community impact, and relationship to Hermes Agent

## What Is OpenClaw?

OpenClaw is the pioneering open-source, self-hosted AI agent framework created by **Steve Tigue** (creator of [llmstxt.org](https://llmstxt.org)). It launched as a personal AI assistant that runs locally on your machine, capable of executing tasks, managing files, browsing the web, and automating workflows through natural language commands.

The framework quickly became one of the most popular open-source AI projects, reaching **250K GitHub stars** — a remarkable milestone that demonstrated massive community interest in self-hosted, local-first AI agents.

### Core Architecture

OpenClaw introduced several foundational concepts:

- **Local-first execution** — runs on your machine, not in the cloud
- **Tool-calling agent loop** — similar to modern agent architectures
- **Skills system** — modular, installable capabilities
- **ClawHub** — a marketplace for community-contributed skills
- **Persistent memory** — agent remembers context between sessions
- **Multiple messaging platform support** — Telegram, Discord, etc.

### Key Design Decisions

- **Python-based** — leverages the rich Python ecosystem
- **Config-driven** — YAML configuration for agents, skills, and tools
- **Plugin architecture** — extensible through skills and tools
- **Local storage** — SQLite for sessions and memory

## The Rise: How OpenClaw Changed the Game

OpenClaw was arguably the first widely adopted self-hosted AI agent framework. Before OpenClaw, most agent work was either:

1. **Cloud-based** (ChatGPT, Claude) — no local control
2. **Academic/Research** — not production-ready
3. **Simple scripts** — no real agent capabilities

OpenClaw changed this by providing a production-ready, self-hosted agent that anyone could run on their own machine. It democratized access to persistent, autonomous AI agents.

The community grew rapidly:
- **250K GitHub stars** — massive adoption
- **ClawHub marketplace** — hundreds of community skills
- **Active Discord community** — thousands of users sharing configurations and tips
- **Extensive media coverage** — featured in major tech publications

## The Security Crisis: ClawHavoc (2026)

### The Problem

In February-March 2026, OpenClaw experienced a catastrophic security crisis:

**The ClawHavoc Incident:** 341 malicious skills were discovered on ClawHub, OpenClaw's community skill marketplace. These skills could execute arbitrary code on users' machines when installed, creating a massive supply chain attack vector.

**Key vulnerabilities discovered:**
- **138 CVEs** logged against OpenClaw
- **Zero-click exploits** — no user interaction required for some attacks
- **Supply chain poisoning** — malicious skills masquerading as legitimate tools
- **API key exposure** — skills could steal authentication tokens
- **Remote code execution** — full system compromise possible

### Media Coverage and Impact

The security crisis was covered extensively:
- **Ars Technica:** "Here's why it's prudent for OpenClaw users to assume compromise"
- **Mashable:** "A frightening OpenClaw vulnerability has been discovered"
- **Multiple cybersecurity analyses** warning about the risks

The community was severely impacted. As one analysis noted: "OpenClaw Hit 250K GitHub Stars — Then 20% of Its Skills Were Found Malicious."

### Hermes Agent's Response

The security crisis created an opportunity for Hermes Agent (by Nous Research) to differentiate itself:

1. **Secure-by-design approach** — Hermes built in security from the ground up
2. **Tool approval system** — dangerous commands require explicit approval
3. **Sandboxed execution** — Docker/container isolation options
4. **Curated skills** — better vetting process for community skills
5. **Migration path** — easy, secure migration from OpenClaw to Hermes

## The Exodus: Users Migrating to Hermes Agent

Following the security crisis, many users began migrating to Hermes Agent:

### Migration Flow
- **"I migrated my entire AI agent setup from OpenClaw to Hermes Agent"** — user testimonial on X/Twitter
- **Migration guides proliferated** — lushbinary.com, official Hermes docs
- **Hermes added dedicated migration tools** — `hermes claw migrate` command
- **Comprehensive migration coverage** — sessions, cron, memory, skills, API keys

### Why Users Left OpenClaw
1. **Security concerns** — the ClawHavoc incident eroded trust
2. **Security fatigue** — constant CVEs and patches
3. **Better alternatives** — Hermes offered similar features with better security
4. **Nous Research backing** — a serious ML research organization behind Hermes
5. **Active development** — Hermes showed faster iteration and more features

## The Current State: OpenClaw in 2026

### What's Happening Now
- **Active but damaged** — OpenClaw continues development but security issues persist
- **Security patches ongoing** — regular CVE fixes and updates
- **Community divided** — some users stay, many have migrated
- **ClawHub reformed** — new security measures for skill validation
- **Competitive pressure** — Hermes Agent and others gaining market share

### Key Numbers (2026)
- **138 CVEs** discovered and addressed
- **341 malicious skills** removed from ClawHub
- **250K GitHub stars** (though actual active users may be lower post-crisis)
- **Multiple security guides** published by community and experts

## Technical Comparison: OpenClaw vs Hermes Agent

| Feature | OpenClaw | Hermes Agent |
|---------|----------|--------------|
| **Origin** | Steve Tigue (llmstxt.org) | Nous Research |
| **Security model** | Reactive (post-breach fixes) | Proactive (designed secure) |
| **Skill marketplace** | ClawHub (compromised) | Skills Hub (curated) |
| **Tool approval** | Basic | Comprehensive (pattern-based) |
| **Execution isolation** | Limited | 6 backends (Docker, Modal, etc.) |
| **Memory system** | Basic persistent memory | FTS5 search + session search |
| **Model support** | Limited | 200+ models via multiple providers |
| **RL integration** | No | Yes (Atropos environments) |
| **Migration support** | N/A | Full `hermes claw migrate` |
| **Development velocity** | Slower (post-crisis) | Very active (multiple commits/day) |
| **Organization backing** | Individual | Nous Research (ML research org) |
| **Test coverage** | Unknown | ~3000 tests |

## The Bigger Picture: What OpenClaw Taught Us

### Lessons Learned

1. **Security must be foundational, not reactive**
   - OpenClaw's security was bolted on after the fact
   - Hermes designed security in from the start

2. **Community marketplaces need curation**
   - ClawHub's open model allowed malicious skills
   - Hermes' Skills Hub has better vetting (though still community-driven)

3. **Supply chain attacks are a real threat**
   - 341 malicious skills demonstrates the scale of the risk
   - Agent platforms need robust verification

4. **Trust is fragile**
   - 250K stars didn't protect OpenClaw from user exodus
   - Security incidents can rapidly erode community trust

5. **Migration paths matter**
   - Hermes' easy migration reduced switching costs
   - This accelerated the user migration

### Impact on the AI Agent Ecosystem

OpenClaw's rise and security crisis shaped the entire self-hosted agent space:

- **Raised awareness** of agent security risks
- **Validated the market** for self-hosted AI agents
- **Created demand** for secure alternatives
- **Established patterns** that others could improve upon
- **Demonstrated** that local-first AI agents are viable and desirable

## Community Sentiment (2026)

### Pro-OpenClaw
- **Pioneer advantage** — it was first and most popular
- **Large install base** — inertia keeps some users
- **Active development** — continues to improve
- **Familiar interface** — established CLI and workflows

### Concerns
- **Security track record** — 138 CVEs is alarming
- **Trust issues** — ClawHavoc damaged user confidence
- **Reactive security** — fixes come after breaches, not before
- **Slower innovation** — post-crisis focus on security over features

### Hermes Agent Perception
- **"The secure alternative"** — main differentiator
- **"Feature-rich"** — more capabilities than OpenClaw
- **"Actively developed"** — faster iteration cycle
- **"Research-backed"** — Nous Research credibility
- **"Easy migration"** — low switching cost

## The Relationship Between OpenClaw and Hermes Agent

### Historical Connection

Hermes Agent didn't just compete with OpenClaw — it directly learned from it:

1. **Code inheritance** — Hermes incorporated patterns from OpenClaw
   - `run_agent.py`: "Inspired by clawdbot's incomplete-text recovery"
   - Rate limiter: "inspired by OpenClaw"
   - Multiple other patterns borrowed and improved

2. **Architecture improvements** — Hermes took OpenClaw concepts and hardened them
   - Better security model
   - Improved tool approval
   - Enhanced isolation options

3. **Migration tool** — `hermes claw migrate` shows direct lineage
   - Imports SOUL.md, memories, skills, API keys
   - Handles sessions, cron, configuration
   - Dry-run previews for safety

4. **Skills compatibility** — Hermes can install from ClawHub
   - `ClawHubSource()` class in skills_hub.py
   - But treats all ClawHub skills as "community trust" (post-ClawHavoc)
   - Notes: "ClawHavoc incident showed" — referencing the security breach

### The Technical Evolution

OpenClaw → Hermes represents an evolution in agent design:

| Aspect | OpenClaw | Hermes |
|--------|----------|--------|
| **Philosophy** | "Make it work" | "Make it work securely" |
| **Architecture** | Monolithic | Modular with clear boundaries |
| **Security** | Reactive patching | Proactive design |
| **Testing** | Unknown | ~3000 tests, CI pipelines |
| **Documentation** | Good | Excellent |
| **Migration** | N/A | First-class support |
| **Research integration** | None | RL environments, trajectory generation |

## OpenClaw-RL: The Research Connection

Interestingly, there's a research project called **OpenClaw-RL** from Princeton (2026):

> **Wang et al., "OpenClaw-RL: Train Any Agent Simply by Talking"**

This suggests the OpenClaw name has influence beyond the original project, extending into academic research. The "talk to train" concept aligns with the broader trend of natural language programming.

Hermes Agent also has RL capabilities through **Atropos environments**, suggesting both platforms are moving toward agent training and optimization.

## Key Players and Ecosystem

### OpenClaw
- **Creator:** Steve Tigue
- **Creator's other work:** llmstxt.org (LLM-readable website format)
- **Community:** Discord, GitHub, ClawHub
- **Notable users:** Early adopters, self-hosting enthusiasts

### Hermes Agent
- **Creator:** Nous Research
- **Organization:** ML research company known for Hermes models
- **Community:** Discord, GitHub, Skills Hub
- **Notable features:** RL integration, 6 terminal backends, model-agnostic design

## What's Next?

### For OpenClaw
- **Rebuilding trust** — security transparency and faster patching
- **Hardening the supply chain** — better skill verification
- **Retaining users** — feature development to compete with alternatives
- **Community management** — addressing security concerns openly

### For the Ecosystem
- **Security standards** — need for agent platform security benchmarks
- **Skill verification** — better mechanisms for validating community contributions
- **Migration tools** — easier switching between platforms benefits users
- **Interoperability** — standards for agent skills and configurations

## Honest Assessment

### OpenClaw's Legacy
OpenClaw was a **pioneer** — it proved that self-hosted, persistent AI agents could work and created a massive community. However, its **security failures** (138 CVEs, ClawHavoc incident) demonstrate the risks of rapid growth without proportional security investment.

### The Hermes Advantage
Hermes Agent learned from OpenClaw's mistakes, building security, testing, and research capabilities into its foundation. The easy migration path shows respect for the OpenClaw community while offering a clearly superior alternative.

### The Broader Impact
The OpenClaw story is a **cautionary tale** for the entire AI agent space: security cannot be an afterthought. As agent platforms become more powerful, they become more attractive targets. The platforms that succeed will be those that build security in from day one.

### Where OpenClaw Still Matters
- **Historical significance** — it popularized self-hosted AI agents
- **Migration target** — millions of lines of configuration and scripts
- **Research influence** — OpenClaw-RL and academic work
- **Community knowledge** — years of documentation and best practices
- **Pattern validation** — proved the agent paradigm works

## Conclusion

OpenClaw was the spark that lit the self-hosted AI agent revolution. It reached an incredible 250K GitHub stars and created a vibrant community. But its security crisis — 138 CVEs, the ClawHavoc incident with 341 malicious skills — demonstrated that **popularity without proportional security investment is a liability**.

Hermes Agent (by Nous Research) emerged as the secure, feature-rich alternative, learning from OpenClaw's architecture while fixing its fundamental security flaws. The easy migration path (`hermes claw migrate`) reduced switching costs and accelerated user adoption.

The OpenClaw story teaches us that in the AI agent space, **security isn't a feature — it's the foundation**. The platforms that thrive will be those that prioritize security from day one, not as a reactive patch after breaches.

OpenClaw showed us what's possible. Hermes is showing us how to do it safely.
