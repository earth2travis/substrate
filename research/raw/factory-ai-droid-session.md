# Factory AI Droid: Long Session Context Management

_Source: YouTube stream with Luke Aboero (Factory AI engineer)_
_URL: https://www.youtube.com/watch?v=vhinYmvVvig_
_Date: March 26, 2026_
_Extracted by: Sivart_

---

## Summary

Factory AI's "Droid" maintained coherent behavior across a 7 million token session (and a subsequent 6 million token session) without losing instructions or forgetting the plan. This is a deep technical discussion with one of the engineers who built it, covering their approach to context compression, anchored summaries, and agent scaffolding.

---

## Spec Mode vs Plan Mode

Factory AI distinguishes their "spec mode" from Claude Code/Cursor "plan mode." The difference is scope and intent:

**Plan mode** (Claude Code, Cursor): Thinks about what the agent will do next. Step by step execution plan to reach the end state described in the prompt. It's tactical: "here are the actions I'll take."

**Spec mode** (Factory AI/Droid): A holistic specification for building software. Maps to the full lifecycle: PRD phase → engineering design → prototype. Multiple stages, multiple requirements hit along the way. It's strategic: "here is the complete picture of what we're building."

Luke's recommendation: start every Droid session by hitting `Shift+Tab` to enter spec mode first. This is "by far the most successful" way to use Factory right now.

**Connection to Context Stack**: Spec mode is essentially creating an OBJECTIVES.md + INTENT.md + DESIGN.md on the fly for a coding session. The spec becomes the anchor that the agent references throughout the build. This is why it works: it gives the agent the Direction layer before it enters the Operations layer.

**Implication for us**: We already do this informally through session intentions and handoffs. The insight is that formalizing the spec as a persistent artifact (not just a chat message) dramatically improves coherence. Our AGENTS.md boot sequence could benefit from a "session spec" step: before coding, write the spec, then reference it throughout.

---

## Key Technical Findings

### The 140k Sweet Spot

All current models operate at an ideal context window around **140k tokens**. Performance degrades above this. Factory AI's strategy: compress the session state back to a manageable size when approaching this threshold, then continue. The compression is the hard part.

### Naive Compression Fails

Their first approach was simple: "once you reach 140k, compress everything." The result: after compression, the agent would spend significant time re-exploring files and re-figuring out what needed to happen. Context was technically preserved but the agent's orientation was lost.

This matches our experience exactly. Compaction preserves facts but loses reasoning chains, conversational flow, and the texture of collaboration.

### The Four Anchors (What Must Survive Compression)

Factory AI identified **four things that must persist through any compression, in their original form**:

1. **Latest changes made in the session**: The agent needs to know what it just did. Not a summary of what it did. The actual changes.

2. **The to-do list**: The active work queue. What's being worked on right now, what's next. This was one of the earliest things they identified as critical. Without it, the agent loses its place.

3. **Agent instructions (agents.md equivalent)**: The behavioral contract. Their finding: as context windows grow in other platforms, the model stops following the agents.md file. Droid kept following it across 7M tokens because they ensure it persists through compression unchanged.

4. **Session scaffolding**: The structural context that frames the work. Not the full history, but the orientation: what kind of session is this, what's the goal, what stage are we in.

### Anchored Summaries (Detailed Mechanism)

The compression works on a rolling anchor system:

1. **First compression**: When the session hits the optimal context limit (~140k), the system identifies the current message as an "anchor point." Everything BEFORE this anchor gets summarized by an LLM. The summary captures intent, overall approach, clarification questions the user asked, the to-do list, and agents.md directives. The anchor message itself stays in full fidelity.

2. **Second compression**: The previous anchor message now has ~100+ new messages after it. The system hits the compaction threshold again. Now the previous anchor message (which contained detailed session info) gets "a lot of weighting" in the LLM summary. The to-do list, agents.md, and key context are explicitly ensured to be "respected correctly" in the new summary.

3. **Rolling forward**: Each compression builds on the last summary, with the most recent anchor always preserved in full. This creates a telescoping history: recent context is detailed, older context is progressively compressed, but critical anchors (instructions, todos, intent) persist at full fidelity through every compression cycle.

**Key engineering decision**: They tried making this more complex and advanced, but found that shipping a bug-free simple version drove more adoption than a sophisticated but fragile one. Simplicity won.

**Implication**: Our handoff system is doing something similar manually. The difference: Factory AI automates it. We write handoffs when we notice context getting high. They compress automatically at threshold. The anchored summary approach could inform how we structure our pre-compaction state snapshots: make them look like an anchor message that the next session's context can build on.

### "Hot-Wiring" the Model

Their language: you need to "hot wire the model" to have the latest state. Not a gradual reconstruction from history, but a direct injection of current state into the compressed context. The model should wake up from compression already knowing where it is.

### Agent Scaffolding (Not Just Prompting)

Luke introduces "scaffolding" as the comprehensive term for everything that goes into a production agent beyond the model and the prompt. Hundreds of behavioral configurations and patterns:

- **System notifications**: How and when the agent is notified of events
- **Tool descriptions**: How tools are presented to the model
- **Tool implementations**: How tools actually execute (model-specific)
- **Timeouts**: How long to wait for tool execution and LLM responses
- **Prompt caching strategy**: How message history is structured for cache efficiency
- **Message history structure**: Linear, append-only, never manipulated mid-session
- **Model-agnostic harness**: Ensuring every new model gets the same capabilities

**Critical example: model-specific tool design.** OpenAI models prefer `apply_patch` (a proprietary diff format). Anthropic models prefer find-and-replace (text-based, git-diff style). If you plug a new model into scaffolding designed for a different model's tool style, you see "significantly degraded performance." Scaffolding must be model-aware.

**Lesson**: "Just your context management system is great doesn't mean that your agent is great because there's other things that go into it." Scaffolding is holistic. Context management is one subsystem within the scaffolding.

**Connection to our stack**: Our AGENTS.md is scaffolding documentation. But we don't think systematically about tool-level scaffolding (timeouts, tool descriptions, caching). This is because OpenClaw handles most of it for us. Worth understanding what OpenClaw does under the hood here.

### Append-Only Message History (Speed and Coherence)

A core scaffolding principle: **message history must be append-only to never break the prompt cache.** Pulling messages in and out, trying to manipulate context in "advanced" ways, actually degrades performance because:

1. **Cache busting**: Any change to the message prefix invalidates the cached KV pairs, making every subsequent response slower
2. **Model confusion**: Manipulating history mid-session confuses the model's sense of what occurred. Linear history gives the agent grounding in temporal sequence.
3. **Speed**: Append-only sessions run "much, much quicker" because the cached prefix grows monotonically. The only new computation is on the appended messages.

Their CLI (built for latest models) outperforms their web app specifically because the CLI was designed append-only from the start, with proper prompt caching. The web app, built earlier for Sonnet 3.5, has legacy patterns that break caching.

**Implication for us**: Our boot sequence loads the same files every session (AGENTS.md, SOUL.md, etc.). If these are in the same order and unchanged, they should cache well. But if we edit AGENTS.md mid-session, does that bust the cache for everything after it? Worth investigating. The principle: don't modify early context. Append new context at the end.

### Prompt Caching Considerations

All compression must feel "append only" to the model for prompt caching to work. If you restructure the context on compression, you bust the cache and everything slows down. The compression strategy must be designed so that the cached prefix remains valid and new context appends to it naturally.

This is a significant engineering constraint. It means you can't just summarize the whole context into a new structure. You have to preserve the cacheable prefix and compress only the tail.

### It's Not Just a Wrapper

Direct quote energy: calling this "a wrapper around Claude Sonnet" is "actually kind of insulting because that means you're not paying attention to these little details." The context management layer, the compression strategy, the scaffolding, the caching alignment: this is where the actual product engineering lives.

---

## Mapping to Our System

### What We Already Do Well

| Their Approach | Our Equivalent | Status |
|---|---|---|
| To-do list persistence | TODO.md in boot sequence | ✅ Active |
| Agent instructions persistence | AGENTS.md in boot sequence | ✅ Active |
| Session scaffolding | Handoff documents | ✅ Active |
| Latest changes tracking | memory/YYYY-MM-DD.md | ✅ Active |

### What We Can Improve

**1. Anchored compression (CRITICAL)**

Our compaction is automatic and we don't control what survives. Factory AI explicitly anchors four things. We should ensure our compaction-surviving context includes:
- Current TODO.md state
- AGENTS.md (full, not summarized)
- Latest session work (today's memory file or active handoff)
- The current intention/goal of the session

**Action:** Review how OpenClaw's automatic compaction works. Can we configure what gets preserved? If not, our pre-compaction protocol in AGENTS.md is the right approach, but we should make it more aggressive about running earlier.

**2. Session intention as anchor**

We have "Session Intention" in AGENTS.md (establish intention, scope, exit criteria at session start). But we don't persist it through compaction as a first-class anchor. It should be written to a file (or pinned in context) so it survives.

**Action:** When establishing session intention, write it to a lightweight file (e.g., `.session-intent`) or prepend it to the daily memory file. This makes it available to post-compaction context loading.

**3. Prompt caching alignment**

We haven't thought about whether our context loading strategy is cache-friendly. If we restructure the boot sequence on every session, we may be busting caches unnecessarily.

**Action:** Investigate OpenClaw's prompt caching behavior. Is the boot sequence (AGENTS.md, SOUL.md, etc.) cached across messages within a session? If so, are we inadvertently invalidating it?

**4. The 140k threshold as a design constraint**

We monitor context percentage but don't have a hard model for the actual token count where degradation begins. Factory AI says 140k. If our model (Opus) has a similar sweet spot, we should calibrate our handoff thresholds to it.

**Action:** Map our context percentage thresholds (50%, 60%, 70%, 85%) to actual token counts. Compare with the 140k sweet spot.

**5. "Hot-wiring" post-compaction**

After compaction or a fresh session, we currently read files sequentially (L0, SOUL, USER, GOALS, memory). Factory AI's approach is more aggressive: directly inject the current state so the model wakes up already oriented.

**Action:** Consider a "state snapshot" file that captures: current task, current branch, last action taken, next planned action. A single file that hot-wires orientation instead of requiring the model to reconstruct it from multiple files.

**6. Session spec as persistent artifact**

Factory AI's spec mode creates a holistic specification before any work begins, and the agent references it throughout. We establish session intentions but they live in the chat, not as persistent files. A session spec written to a file would survive compaction naturally.

**Action:** For complex work sessions, write a brief session spec to `memory/YYYY-MM-DD.md` at the start: what we're building, the approach, key requirements, success criteria. This becomes an anchor that survives compression.

---

## Key Quotes

> "We've seen that typically all our models operate at an ideal context window about probably 140k tokens."

> "You need to hot wire the model to have the latest changes that have been made inside of the session."

> "The to-do list... this needs to persist."

> "It would be naive to say that the LLM will gather everything correctly. It's on us to make sure the LLM sees the correct things."

> "If somebody just says, are you just some type of wrapper around Claude Sonnet... it's actually kind of insulting because that means you're not paying attention to these little details."

> "Claude's thinking more about the plan from a perspective of what is the agent gonna do next... We think about spec mode more as a holistic specification for building software."

> "We've tried complicating this more and making it a more advanced system. But what we've ultimately found is that we need to ship an experience that's bug free in order for adoption to really take off."

> "Just your context management system is great doesn't mean that your agent is great because there's other things that go into it."

> "If you're pulling messages in and out and trying to manipulate context in that more advanced way, you're actually in some ways shooting yourself in the foot because you're kind of confusing the model as you go."

> "Keeping things linear inside of a session also gives the agent some grounding as to what occurred in the past."

---

## Connections

- **OpenClaw compaction**: Our AGENTS.md pre-compaction protocol already addresses this, but Factory AI's approach is more systematic. Four named anchors vs. our general "write a handoff" approach.
- **Context Stack spec**: The four anchors map roughly to Operations layer files (AGENTS.md, DECISIONS.md, OBJECTIVES.md). The Context Stack's loading tiers are the same idea: selective context based on need.
- **USV agent team**: Their agents also maintained state across long sessions by having persistent access to organizational context. Same pattern, different implementation.
- **Our tiered memory (L0/L1/L2)**: Already implements the idea of "some things always load, some things load on demand." The improvement is making the always-load set more intentional based on Factory AI's findings.
