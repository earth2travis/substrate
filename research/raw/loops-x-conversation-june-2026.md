---
source_url: https://x.com/mvanhorn/status/2063865685558903149
ingested: 2026-06-08
sha256: 7729625ee3e3bde6a2961e7f3531861500b1b4e16910ddb68a70c683408b2c67
---

# WTF Is a Loop? Peter Steinberger vs. Boris Cherny

> Compiled from Matt Van Horn's X article (June 8, 2026), subagent research, and lab paper references. This is a raw source; synthesis belongs in the wiki proper.

## The Tweet That Has the Timeline in a Chokehold

On June 7, 2026, Peter Steinberger (@steipete) posted a tweet that cleared 2.2 million views:

> "Here's your monthly reminder that you shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents."

The replies turned into a brawl over what it actually meant. Varadh Jain asked the only question that mattered: what does this look like in practice? Matthew Berman (@MatthewBerman) replied:

> "nobody knows but him and boris."

That is the real story. Not that loops are the future, but that a six-word phrase hit two million views while the people boosting it argued in the replies about what it meant.

## What a Loop Actually Is

Boris Cherny (creator of Claude Code, Anthropic) gave the cleanest definition on stage at the Acquired Unplugged event hosted by WorkOS on June 2, 2026:

> "Now it's actually leveled up, I think, again, to the next wave of abstraction where I don't prompt Claude anymore. I have loops that are running. They're the ones that are prompting Claude and figuring out what to do. My job is to write loops."

A loop is a small program you write that prompts the coding agent for you, reads what it produced, decides whether it is done, and if not, prompts it again. You stop being the thing inside the loop typing prompts. You become the author of the loop. The model becomes a subroutine.

Boris describes three stages:
1. A year ago: wrote code by hand with autocomplete
2. Then: ran 5-10 Claude sessions in parallel and prompted each one
3. Now: writes loops that prompt Claude; hundreds of agents read his GitHub, Slack, and Twitter and decide what to build next

He deleted his IDE in November and has not opened it since. In the last 30 days, 100% of his contributions to Claude Code were written by Claude Code. He landed 259 PRs.

The nuance the prompt-engineering-is-dead crowd skips: he is not saying engineers are obsolete. Someone still has to decide what to build, talk to customers, and coordinate teams. The job did not vanish. It moved up an altitude, from writing the code to writing the thing that writes the code.

## The Spectrum: From ReAct to Orchestration

The replies were a mess because "loop" hides at least five different things. Here is the ladder, oldest to newest:

### Stage One: Academic While-Loop (ReAct, 2022)
The 2022 ReAct paper formalized it: the model reasons, calls a tool, reads the result, repeats until done. One model, one loop, a human watching.

**Paper:** Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models" (arXiv:2210.03629, October 2022). Authors: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao.

### Stage Two: AutoGPT (2023)
Gave the agent a goal and let it prompt itself. Became famous for spinning forever doing nothing. That failure seeded years of "agents are a toy."

### Stage Three: The Ralph Loop (July 2025)
Published by Geoffrey Huntley. Almost insultingly simple: a bash one-liner that pipes the same prompt file into the agent over and over.

```bash
while :; do cat PROMPT.md | claude-code ; done
```

Its real innovation was discipline: every iteration resets the context to a fixed set of anchor files instead of letting the conversation grow. Huntley built an entire programming language with it for about $297.

Key repos:
- `mikeyobrien/ralph-orchestrator` (2.9k stars)
- `acazau/ralph-orchestrator-ts` (TypeScript/Bun port)
- `syuya2036/ralph-loop` (32 stars)
- `alfredolopez80/multi-agent-ralph-loop` (138 stars, multi-agent extension with MemPalace memory)

### Stage Four: Productized Ralph (/goal, Spring 2026)
Both Codex and Claude Code shipped a /goal command that runs the Ralph loop until a small validator model confirms the task is done.

### Stage Five: Continuous Orchestration Loop (Now)
What Boris and Steinberger actually mean. Four things changed:
1. The loop became the unit of work, not the task
2. Loops started supervising other loops, concurrently and on a schedule
3. Scheduling replaced the human kickoff (runs on infrastructure time)
4. Durability became explicit, with git-backed state and crash recovery

The single-agent Ralph loop is old hat; multi-agent supervision is the new layer.

## It's Just a Cron Job with a Hat On

The best skeptic line: "Cronjobs have funny re-branding rn."

This is half right. Yes, the scheduling layer is cron. Boris literally runs his on cron. The /loop command in Claude Code uses cron under the hood.

What cron never had is the part in the middle. A cron job runs a fixed script. A loop runs a model that looks at the current state, decides what to do next, does it, checks whether it worked, and decides whether to keep going. The decision is the agent's, not yours.

Stack those, let one loop dispatch and supervise others, give them durable shared state, and you have something cron cannot express. The honest framing: loops are cron plus a decision-maker in the body.

## What It Looks Like When You Actually Build One

Claude Code shipped `/loop`. Boris's canonical starter:

```
/loop babysit all my PRs. Auto-fix build issues, and when comments come in, use a worktree agent to fix them.
```

Boris posted five tips for running Opus autonomously:
1. Use auto mode for permissions so Claude doesn't ask for approval
2. Use dynamic workflows to have Claude orchestrate hundreds or thousands of agents
3. Use `/goal` or `/loop` to nudge Claude to keep going until it's done
4. Use Claude Code in the cloud so you can close your laptop
5. Make sure Claude has a way to self-verify its work end to end

Tip five is the one practitioners obsess over: a loop is only as trustworthy as its ability to check its own work.

## The Deep End: Gas Town

Steve Yegge's Gas Town, launched in January 2026: 20-30 Claude Code instances coordinated by a Mayor agent, with patrol agents that run continuous loops and state stored in git so work survives a crash. That is the continuous orchestration loop Trash Panda was reaching for, shipped and open source.

Repo: `gastownhall/gastown`

## The Plot Twist: The Loop Is Now the Expensive Part

Every AI agent shipped is a for-loop, an LLM call, and a try/catch. The only thing agentic about it is the Anthropic bill at the end of the month.

Uber capped its engineers at $1,500 per person per tool per month for Claude Code and Cursor after burning its annual AI budget in four months. Once the model writes the code for almost nothing, the cost moves to the loop running it.

The failure mode everyone in production is scared of: the loop that does not stop.

Every serious 2026 write-up on loops converges on three hard stops:
1. Maximum iteration count
2. No-progress detection
3. Token or dollar budget ceiling

Gartner puts agentic AI at the peak of inflated expectations, with only about 17% of organizations actually deploying agents.

## It's Not Loops. It's Skills.

The durable half of Steinberger's point: if you do something more than once, turn it into an automated skill. A loop with no reusable skills inside it is just a while-true around a stranger. A loop that calls a library of sharp, tested, named skills is a system that compounds.

## Key Patterns from the Research

1. A loop is cron plus a decision-maker in the body: the model picks the next action each tick.
2. The lineage is real: ReAct (2022) → AutoGPT (2023) → ralph (2025) → /goal (Spring 2026) → orchestration loops now.
3. The loop is only as good as its feedback. Continuous review and validation gates are what make a loop trustworthy.
4. The expensive resource shifted from tokens to loop management. Cap iterations, detect no-progress, set a dollar budget.
5. The reusable unit inside the loop is a skill, not a prompt.

## Anthropic's Formal Framework (Dec 2024)

Anthropic's "Building Effective Agents" (Dec 19, 2024) formalizes the distinction:
- **Workflows**: predefined, predictable. Prompt chaining, routing, parallelization, orchestrator-workers.
- **Agents**: flexible, model-driven decision-making. The model dynamically directs its own process and tool usage.

The article recommends starting with LLM APIs directly, not frameworks. Frameworks add abstraction that obscures prompts and responses.

## Relevant Papers and Sources

| Paper/Source | Authors | Date | URL |
|---|---|---|---|
| ReAct: Synergizing Reasoning and Acting in Language Models | Yao et al. | Oct 2022 | https://arxiv.org/abs/2210.03629 |
| Building Effective Agents (Anthropic blog) | Anthropic Engineering | Dec 2024 | https://anthropic.com/engineering/building-effective-agents |
| Focused ReAct: Improving ReAct through Reiterate and Early Stop | Li et al. | Oct 2024 | https://arxiv.org/abs/2410.10779 |
| Co-ReAct: Rubrics as Step-Level Collaborators | Kang et al. | May 2026 | https://arxiv.org/abs/2605.23590 |
| Agentic Very Much! Adoption of Coding Agent in New GitHub Projects | Robbes et al. | Jun 2026 | https://arxiv.org/abs/2606.07448 |
| Socratic-SWE: Self-Evolving Coding Agents via Trace-Derived Agent Skills | Xiao et al. | Jun 2026 | https://arxiv.org/abs/2606.07412 |
| How AI Agents Reshape Knowledge Work | Yang et al. (Perplexity) | Jun 2026 | https://arxiv.org/abs/2606.07489 |
| OpenClaw (Steinberger's project) | Peter Steinberger | 2025 | https://github.com/openclawhq |
| Ralph Orchestrator | mikeyobrien | 2025 | https://github.com/mikeyobrien/ralph-orchestrator |
| Gas Town | Steve Yegge | Jan 2026 | https://github.com/gastownhall/gastown |
| Karpathy Autoresearch | Andrej Karpathy | 2025 | https://karpathy.ai/blog/autoresearch |

## Voices in the Conversation

**Top voices identified:**
- Peter Steinberger (@steipete) — OpenAI, OpenClaw. Bio: "Polyagentmorous ClawFather."
- Boris Cherny (@bcherny) — Anthropic, creator of Claude Code
- Matt Van Horn (@mvanhorn) — Author of the article, runs /last30days research
- Geoffrey Huntley (@ghuntley) — Creator of the Ralph loop
- Matthew Berman (@MatthewBerman) — AI commentator
- Steve Yegge — Creator of Gas Town
- Andrej Karpathy — Autoresearch loop pioneer

**Earlier Steinberger tweet (July 5, 2025):**
> "Telling the agent to keep track of the work in a markdown is so effective, especially once you automated the loop that it can work for hours."

**Reddit practitioner (r/ChatGPTCoding, June 2026):**
> "A lot of people are rolling their eyes on Twitter, but my ears are perked up."

**Working engineer (@rohit_jsfreaky, June 2026):**
> "Every ai agent i shipped this year is a for-loop, an llm call, and a try/catch around the json parsing. The only thing agentic about it is the anthropic bill at the end of the month."

**On cost (@runes_leo, June 2026):**
> "The costliest thing in AI coding is no longer writing code, it's managing the agent loop."

**On guardrails (@cv_usk, June 2026):**
> "Without guardrails, you get infinite loops and billing surprises orders of magnitude over budget."

**On verification (@DanKornas, June 2026):**
> "Your coding agent can move fast, but bad commits compound fast too."

## Gartner Context

Agentic AI sits at the peak of inflated expectations on the Gartner Hype Cycle. Only ~17% of organizations have actually deployed agents. The gap between the timeline and the receipts is the real state of play.

## Research Methodology Note

This raw source was compiled via:
1. Direct browser extraction of Matt Van Horn's X article (the browser rendered the full article text)
2. Subagent research on X conversation, GitHub repos, and technical lineage
3. arXiv API searches for relevant papers (ReAct lineage, agent loops, multi-agent orchestration)
4. Direct navigation to Anthropic's "Building Effective Agents" blog post

X/Twitter's login wall prevented direct search access to threaded conversations. The article text itself is the primary source for the X discourse. Technical lineage was reconstructed from GitHub repos, Hacker News, and blog posts.
