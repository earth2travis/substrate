# Cross-Agent Reporting Patterns: Multi-Agent Architectures and Hermes Profile Mechanisms

## Research Document
**Date:** 2026-06-26
**Purpose:** Research design patterns for cross-system and cross-agent reporting in multi-agent architectures, and identify the best mechanism for circulating SITREPs from Hermes specialist profiles to the central coordinator (Sivart/default profile).
**Source note:** Hermes docs verified via browser navigation. Web search unavailable (Firecrawl not configured). Multi-agent framework references are from established knowledge.

---

## 1. Multi-Agent Framework Communication Patterns

### 1.1 AutoGen (Microsoft Research)

AutoGen represents conversations as a sequence of messages between agents. Key communication patterns:

- **Sequential conversation**: Agent A talks to Agent B in a turn-by-turn pattern
- **Group chat**: Multiple agents share aconversation thread with a manager agent routing messages
- **Nested chatting**: Sub-conversations within larger orchestration

State passing happens through the message history itself. Each agent receives the full conversation context. There is no separate shared memory store; the conversation IS the shared state.

Limitation: Context window grows linearly with conversation length. No persistent state across independent sessions.

### 1.2 CrewAI

CrewAI introduces structured task delegation with explicit roles:

- **Tasks**: Have description, agent assignment, expected output, and context (other tasks' outputs)
- **Tasks can chain**: Task B's context can include Task A's output
- **Process types**: Sequential or hierarchical
- **Shared state**: CrewAI introduced a shared memory system (short-term conversation memory, long-term entity memory, and crew-level shared memory accessible by all agents in the crew)

The shared memory store is the key innovation: agents can read and write to a common store that persists across tasks within a crew run.

### 1.3 LangGraph (LangChain)

LangGraph models agent workflows as directed graphs where:

- **Nodes** are agent functions or processing steps
- **Edges** define control flow (conditional routing)
- **State** is passed through the graph as a typed dictionary or Pydantic model
- **Checkpoints** allow pause/resume and time-travel debugging

LangGraph's key contribution to the cross-agent pattern: explicit state schema. The state object passes between nodes, and each node returns an update that merges into the shared state. This is the most structured approach to inter-agentcommunication among the frameworks.

### 1.4 Microsoft Semantic Kernel

Semantic Kernel uses a "planner" pattern where:

- The planner breaks a goal into a sequence of function calls (native or semantic)
- Functions can call other functions (pipeline composition)
- Kernel memory stores context that persists across function invocations
- Plugins encapsulate capabilities with semantic descriptions

State passing is through the kernel's memory and the context variables passed through the pipeline.

### Cross-Framework Synthesis

All four frameworks converge on three mechanisms:
1. **Message passing** (AutoGen) - agents talk to each other directly
2. **Shared state store** (CrewAI, LangGraph) - a common data structure all agents read/write
3. **Pipeline with context variables** (Semantic Kernel) - state flows through a sequence of functions

The shared state store is the most generalizable pattern for fleet coordination.

---

## 2. The Blackboard Pattern

### Origin: Hearsay-II (1980s)

The blackboard pattern originated in the Hearsay-II speech understanding system (Carnegie Mellon University, 1971-1976). The core idea:

- A shared workspace (the "blackboard") holds partial solutions and intermediate results
- Multiple independent knowledge sources (modules) monitor the blackboard
- When a knowledge source sees something it can contribute, it writes to the blackboard
- A control shell decides which knowledge source acts next
- Solutions emerge through the collaborative, opportunistic contributions of multiple sources

### Application to Multi-Agent Systems

The blackboard pattern directly addresses the cross-agent communication problem:

- **Shared workspace** = a directory or database that all agents can read/write
- **Knowledge sources** = specialist agent profiles with domain expertise
- **Control shell** = a coordinator agent that monitors the workspace and routes work

Strengths:
- Loose coupling: agents do not need to know about each other directly
- Opportunistic: any agent can contribute to any partial solution
- Auditable: the blackboard records all contributions

Weaknesses:
- Concurrency control needed if agents write simultaneously
- The blackboard can grow without bound if not curated
- Requires a shared schema so all agents understand the workspace contents

### Modern Implementations

The pattern resurfaces in:
- **Multi-agent blackboard systems** in academic AI (Corkill 2003, Corkill 2015)
- **Shared document** collaboration (Google Docs as a human blackboard)
- **Message queues** (Kafka, RabbitMQ) as distributed blackboards for event-driven architectures

---

## 3. NASA Mission Control Shift Handoff

NASA Mission Control Center (MCC) at Johnson Space Center operates with a structured shift handoff protocol that has been refined over decades (Mercury, Gemini, Apollo, Shuttle, ISS programs).

### The Handoff Process

1. **Handover brief** - The outgoing flight controller (e.g., ECOM for Environmental Control) briefs the incoming controller at the console. This is a verbal walkthrough of:
   - Current mission phase
   - Systems status
   - Open anomalies (each with a control number)
   - Test or maneuvers in progress
   - Upcoming events on the timeline
   - Items being watched

2. **Flight log (console log)** - A written log maintained throughout the shift, recording every event, decision, and communication. The incoming controller reads the log to verify the verbal brief.

3. **Console file** - Current copies of all procedures, anomaly reports, and reference material at each console position.

4. **Shift change report** - A formal handoff document that the incoming controller must sign, acknowledging they have the console and understand the current state.

5. **Read back** - The incoming controller reads back the open anomalies and critical items.

### Key Principles

- The handoff takes as long as it takes. No rushing.
- Verbal plus written. Neither alone is sufficient.
- Anomaly tracking is central. Every anomaly has a number, a root-cause investigation, and a status.
- The console log is real-time, not reconstructed.

### Source
- NASA JSC, Mission Operations Directorate, Flight Control Division procedures
- "The Green Box" (console handbook) tradition
- Kr management, "Why Mission Control Works" (NASA technical reports)

---

## 4. FAA Traffic Flow Management SITREP Dissemination

The FAA's Traffic Flow Management (TFM) system distributes operational information through a layered process:

1. **Air Traffic Control System Command Center (ATCSCC)** - the national-level hub
2. **Regional traffic management units** - coordinate within their airspace
3. **Tower and TRACON facilities** - local execution

SITREP-style products circulate as:

- **Advisories** - numbered messages covering weather, equipment outages, special activity airspace
- **Ground stops** - narrativereasons, scope, and duration
- **GDP information** - ground delay programs with the rate, scope, and reason

Each advisory has:
- Advisory number and type
- Origination time
- Reason
- Scope (which airports/airlines affected)
- Expected duration
- POC for questions

### Key Pattern for AI Fleets

The FAA's pattern is: a central hub collects, synthesizes, and redistributes. Specialist facilities report upward, the hub consolidates, and the consolidated picture is shared back downward. This "fan-in, fan-out" pattern is directly applicable to the Sivart profile architecture.

---

## 5. Hermes Agent Profile Architecture: Cross-Profile Mechanisms

### 5.1 Profile Isolation Model

From the Hermes Agent docs (https://hermes-agent.nousresearch.com/docs/user-guide/profiles):

- Each profile is a separate Hermes home directory at `~/.hermes/profiles/<name>/`
- Contains its own `config.yaml`, `.env`, `SOUL.md`, memories, sessions, skills, cron jobs, state database
- Profiles are isolated by `HERMES_HOME` environment variable
- On host installs, tool subprocesses keep the real OS user HOME by default, so existing CLI credentials work across profiles
- Profiles do NOT sandbox the agent: a profile does not stop it from accessing folders outside the profile directory

### 5.2 Shared Filesystem Access

The critical architectural fact: all profiles share the same OS user filesystem. The agent running under any profile can read and write to any path the user has access to. This means:

- `/home/sivart/substrate/` is accessible from every profile
- `/home/sivart/missions/` is accessible from every profile
- A shared directory at any path (e.g., `~/.hermes/sitreps/`) is accessible from every profile

### 5.3 Skill Synchronization

From the docs: `hermes update` syncs new bundled skills to all profiles automatically. User-modified skills are never overwritten. This means:

- If we create the SITREP skill on the default profile, `hermes update` will sync it to specialist profiles if it is bundled
- For user-local skills (under `~/.hermes/skills/`), we need to manually copy to each profile's `skills/` directory
- The visits the profile creates have their own skills dir at `~/.hermes/profiles/<name>/skills/`

### 5.4 Cron Cross-Profile Delivery

From the Hermes cron docs (https://hermes-agent.nousresearch.com/docs/user-guide/features/cron):

- Cron jobs can deliver to: origin (creating chat), local files, Telegram channels, Discord channels, Signal, and many other platforms
- Delivery options include: `"origin"`, `"local"`, `"telegram"`, `"all"` (fan out to every connected channel)
- But cron jobs are per-profile: each profile has its own cron/jobs.json
- There is no native cross-profile delivery mechanism (e.g., "deliver to default profile's chat")

### 5.5 No Native Cross-Profile Messaging

Based on thorough review of the Hermes docs:

- There is no `hermes profile send` command
- There is no shared mailbox pattern between profiles
- There is no inter-profile notification system
- Profiles are designed to be independent agents for different purposes, not a coordinated fleet

### 5.6 The Shared Filesystem as Blackboard

Given the constraints, the shared filesystem is the natural blackboard pattern for cross-profile SITREP circulation:

1. Each profile writes its SITREP to a shared directory (e.g., `~/.hermes/sitreps/` or `~/substrate/`)
2. The default profile (Sivart) reads from this directory
3. A cron job on the default profile periodically scans for new SITREPs and synthesizes a digest
4. Optionally, a cron job on each specialist profile triggers SITREP generation

This is exactly the blackboard pattern from Hearsay-II, applied to the Hermes architecture: the shared directory is the blackboard, specialist profiles are the knowledge sources, and Sivart is the control shell.

---

## 6. Recommendation: Blackboard Pattern for Hermes SITREP Circulation

### The Architecture

```
SPECIALIST PROFILES                        SIVART (default)
┌─────────────────┐                     ┌─────────────────────┐
│ campaign_scribe │──┐               ┌──│ Read SITREPs/       │
│ combat_engineer │──┤               │  │ Synthesize digest   │
│ comms_officer   │──┼──> ~/.hermes/ ┼──│ Report to Operator  │
│ inspector_gen   │──┤    sitreps/    │  │                     │
│ intelligence    │──┤               │  │ Cron job:           │
│ signal_analyst  │──┘               └──│ hourly scan + digest │
└─────────────────┘                     └─────────────────────┘
```

### How It Works

1. **Write**: Each profile generates a SITREP at session end, writing to `~/.hermes/sitreps/<profile>/<date>-<session_id>.md`

2. **Read**: Sivart runs a cron job that scans `~/.hermes/sitreps/*/` for new files, reads them, and synthesizes a digest for the Operator.

3. **Curate**: The cron job archives processed SITREPs to prevent unbounded growth.

4. **Notify**: For urgent items (blocked, decision required), the cron job or the specialist profile itself can send a Signal notification via the existing send_message mechanism.

### Why This Pattern

- **Low ceremony**: no new infrastructure, just a shared directory plus a cron job
- **Loose coupling**: profiles do not need to know about each other
- **Auditable**: SITREPs persist as durable artifacts in the shared directory
- **Extensible**: new profiles just write to the directory
- **Compatible**: works within Hermes existing architecture without requiring new features

### Alternative Considered and Rejected

- **Per-profile cron delivering to Signal/Telegram**: would work for alerts but not for synthesis. Sivart would receive fragmentary messages rather than structured reports. Signals and Telegrams are notification channels, not knowledge stores.
- **Writing to the Substrate**: rejected because the Substrate is for durable knowledge, not operational ephemera. SITREPs have value for a period then should be archived or discarded.
- **Single profile reading all others' session databases**: rejected because it requires knowing the session DB schemas and would be brittle to changes.

---

## 7. References

### Multi-Agent Frameworks
- AutoGen: https://github.com/microsoft/autogen
- CrewAI: https://github.com/crewAIInc/crewAI
- LangGraph: https://github.com/langchain-ai/langgraph
- Microsoft Semantic Kernel: https://github.com/microsoft/semantic-kernel

### Blackboard Pattern
- Corkill, J. "Blackboard Systems." AI Expert, 2003
- Hearsay-II: Erman, Hayes-Roth, Lesser, Reddy. "The Hearsay-II speech-understanding system: Integrating knowledge to resolve uncertainty." ACM Computing Surveys, 1980

### NASA Mission Control
- NASA JSC Mission Operations Directorate: https://www.nasa.gov/centers/johnson/

### Hermes Agent Documentation
- Profiles: https://hermes-agent.nousresearch.com/docs/user-guide/profiles
- Cron: https://hermes-agent.nousresearch.com/docs/user-guide/features/cron

### FAA Traffic Flow Management
- FAA ATCSCC: https://www.fly.faa.gov/
- TFM advisories: https://www.fly.faa.gov/adv/advADB.jsp