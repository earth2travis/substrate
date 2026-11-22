# "Agent platform 2027": John Suh's Blueprint for the Agent Operating System

Raw research file. Single-topic deep dive produced 2026-11-22 on a document circulated as four screenshots attached to a tweet by John Suh (@john_ssuh). Source material for later synthesis, not a finished essay.

Provenance note: the four screenshots were attached to the tweet below but did not reach this machine as attachments, so they were retrieved directly from the tweet's media CDN this session and transcribed from the images. The transcription in section 2 is therefore second-hand (an image transcription, not a published text). Two of the four images overlap by roughly four paragraphs, and the reconstruction below merges them once. Minor typos in the transcription may be transcription artifacts rather than the author's.

Status of the document itself, verified this session: it is UNPUBLISHED. No blog, Substack, company post, or archive copy exists. The author's personal site (suhjohn.com) has no writing index, and its /writing and /agent-platform-2027 paths both return 404. Screenshots 1 and 4 show an editor buffer rather than a rendered page (a live text caret, and a spell-check squiggle under "tldraw" on the last page). There is no date, byline, URL, or footer on any page. The document exists, as of capture, only as a working draft and as these four images. Every quotation in section 1 (the tweet) is exact, taken from the tweet's own JSON via two independent mirrors.

Related Substrate nodes: [[agent-platform-ecosystem]] (the Substrate's existing map of this layer; this document is a competing thesis for the same territory), [[runwork-ai-deep-dive]] (the nearest commercial instance of the thesis in the Substrate, a shared AI workspace for teams with skills, workflows, and apps synced into every AI tool; founder and CEO Oytun Tez, and no connection to this author was found), [[agent-tool-permissions]] (the permission model the blueprint's filesystem layer would need, and the crux of its riskiest claim), [[workflow-as-contract]] (the workflow-definition question the blueprint answers with "code, not drag-and-drop"), [[subagent-architecture]] (the swarm orchestration the blueprint assumes), [[agent-harness-architecture]] (the harness concept behind the blueprint's "self-improving harnesses"), [[hermes-agent-platform-analysis]] (the platform this session runs on, and one of the ADEs the blueprint is implicitly judging).

## 1. The tweet

FACT: Tweet by John Suh (@john_ssuh), posted 2026-11-22T02:56:14Z, blue-verified account, 4,419 likes at the time of capture. Four images attached, titled "Agent platform 2027". Text verbatim:

> Agent platform of 2027.
>
> This is the end game. This is the blueprint for the one and only application layer software that will exist. Every other software will effectively become databases for this layer, the everything agentic operating system for the million agent swarm to work on top of.
>
> This is obviously the end game vision for the application layer of ChatGPT and Claude. I have reasons to believe that an independent company will own this product layer. But most ADE, "enterprise agent platform", or vertical saas companies, are focused on the wrong things far too narrowly, not technically competent, and do not have the product / technical vision to see this inevitable future.
>
> The correct agent platform that wins will function like the base of a garden, from which customers will plant their unique "seeds" to grow their own plants and trees, managed and evolved by agents, humans, and signals from the sensors of the business. This presents a clearer picture than "factory of a factory" imo.

INTERPRETATION: The tweet is doing three rhetorical jobs at once. It names a category ("the application layer" as the only software that will exist), asserts a prediction ("an independent company will own this product layer," i.e. neither OpenAI nor Anthropic), and pre-emptively disqualifies the incumbent competition ("most ADE, enterprise agent platform, or vertical saas companies") on two grounds, focus and competence. The "factory of a factory" line is a direct jab at a competing framing in the same discourse.

## 2. The document, reconstructed

Title: **Agent platform 2027**. Eight sections, each closing with an italicized "Relevant:" footer naming products. Transcribed from the four images.

### 2.1 Agents as actors

> The status quo for most scalable agent workloads is to deploy agents using some form of Temporal. I think this will shift toward actors that allow each agent harness to have a fully independent runtime. The actor model provides runtime isolation, which is necessary for self-improving harnesses, where self-improving refers to an agent being able to write its own extensions or hooks on the fly. Actors help because they allow different implementations of the agent loop to run safely on the same platform backend, even within a single tenant.
>
> The platform should support a variety of agent configurations, separating the definition of an agent from its instances and sessions. Some users may want a mega-agent, but others may prefer bespoke agent definitions. Most notably, Anthropic argues for one mega-agent, but its revealed preference in Formalizing Fermat's Last Theorem suggests something different: each agent had access to only a shell and a file editor. It's unclear to me whether, even if Opus can distinguish the right tools, the researcher would have wanted agents loaded with Gmail, Google Drive, and internet search MCPs when commanding this swarm. Therefore, even within companies advocating for one mega-agent, my observation is that their revealed preference is closer to a code-defined "Grokbot" model.

Relevant: Cloudflare DO, Pi-Durable x Extensions, Vercel Eve, Rivet, DeepSeek Agent.

### 2.2 Environments and computers

> There are two types of computers the platform needs to support: clones of checkpointed sandboxes across a variety of providers, and people's local computers. N agents should be able to work with M computers (e.g., one agent spinning up five sandboxes to experiment with different configurations, one VM per coding agent with a full environment, or 1,000 agents using 100 VMs in parallel as a swarm). These environments should be configurable agentically.

Relevant: Claude Remote, Cursor Agent, Cua AI.

### 2.3 RBAC-ed filesystem

> Swarms of agents will operate on a shared POSIX filesystem in the cloud, with access controls attached to the filesystem separately from the computer. This layer acts part GitHub, where agent-generated code, extensions, and definitions live; part Google Drive, where uploaded, downloaded, and generated files and "apps" live; and more. Since it's effectively a remote shared filesystem, you could host .env files and have each directory use .git or jj for version control. There will be various configurations of RBAC that organizations will want, whether it's agents like humans, or permission granted based on who initiated the particular turn, or a mixture of both.

Relevant: Archil, S3 Filesystems, JuiceFS.

### 2.4 Separation of session and conversation

> The status quo for most coding agent applications is to expose the agent session, including its intermediate tool calls, directly to the user. I think this is wrong.
>
> What the user interacts with should be abstracted from the core agent session as a "conversation." Your app should natively have a concept of a conversation, at the same level of abstraction as a Slack channel, iMessage chat, WhatsApp conversation, or email thread. Content intended for the user should be posted through a tool call rather than by directly exposing the assistant messages from the underlying agent session.
>
> Direct access to agent sessions should be akin to reading the codebase: a way to inspect and debug the system, rather than the primary user interface.
>
> ADEs created in 2025-2026 that wrap coding agent sessions (e.g., T3) will face the same kind of dilemma Cursor faced in 2025-2026. I suspect most will not survive this transition because of the innovator's dilemma.

Relevant: Duet / Grokbot / Dots.

### 2.5 Inbox

> Rather than reading through conversations, users will increasingly interact with a focused inbox of approvals and questions. The inbox should also support tenant-specific apps for reviewing intermediate work relevant to the business that requires human action.

Relevant: MS Today by @nicbstme.

### 2.6 Listeners, monitors, single-tenant data

> Agents should be able to define streams of events from the external world to listen to on a per-tenant basis (WSS, Kafka streams, CDC, etc.) and translate those events, deterministically or agentially, into signals they can act on. These listeners should be buildable on the fly rather than requiring built-in support from the agent platform. This supports agents to define any form of integration to the outside world either as code or as agent. Anything from "I want my Capy Captain / Dots / Duet / main Grok Bot actually have a function for which every email comes in, have JEV filter over it, and trigger an agent run on that email" / "Nevermind, I actually want it to be batches of emails across all my accounts" / "Actually, I want emails from senders with acmecorp.com to be handled for the next week because we need to watch for specific emails from them but I need it to be time sensitive". Right now, the industry (Grok bot, Muse, Instinct, etc) really only supports hourly cron jobs that trigger an agent from a generalized platform perspective, and if not otherwise write bespoke webhook integration as plugins into these platforms. Listeners and monitors as a concept is a strict superset that supports tenants to flexibly configure the type of event-driven mechanism the actual core agent should reason over.

Relevant: Claude Code Monitor, Grokbot future feature.

NOTE: this section names "JEV" as a filtering component in an email-triggered agent pipeline. See section 5 for the connection question.

### 2.7 Workflows

> Agents should be able to define durable workflows on a per-tenant basis. Many business and enterprise workflows operate over long horizons and involve a mixture of agentic and deterministic steps.
>
> The paradigm of shoddily defined drag-and-drop workflow automation (n8n, the original Zapier) is inferior to writing custom code. Given that the agent platform centralizes data flows through APIs and MCPs, it should also be the place where workflows are defined. But these should be code-defined workflows rather than drag-and-drop automations.

Relevant: Zapier Zap, Rivet Workflows.

### 2.8 Apps (Aka Artifacts)

> The status quo is that people view Replit as one category, separate from Claude Artifacts, ChatGPT Apps, or embedded widgets in ChatGPT. I think this is wrong. These all converge on the same idea of an app.
>
> All interfaces should be apps in your filesystem that users can customize. For example, the entire /conversations page should be defined as an artifact. Each user would get a "clone" of the codebase in their filesystem that can be extended or modified as needed. This parallels how an OS ships with default applications.
>
> "Generative UI is going to come with default design components and be represented as JSON to be token-efficient!"
>
> "No, we're going to have a separate DSL that's an HTML hybrid to be more flexible."
>
> "No, we're going to have everything be a Rune App."
>
> I think the answer is that the platform will simply support all of these under the concept of an App, and the specific representation won't matter as much.
>
> The agent platform becomes the OS within which all these apps are built. At first glance, it's not obvious why we need an OS within an OS.
>
> The core reason, and the value to the user, comes down to the customizability and extensibility of the application layer built on top of the underlying OS.
>
> Consider how ten different accounting companies review tax forms. Every company within a vertical shares the same "noun" of "review XYZ," but the process by which each company evaluates and understands the information is bespoke. Ideally, these companies could fork Excel and create bespoke interfaces for their workloads.
>
> This is exactly the assumption behind vertical SaaS: that companies within a vertical share enough common workflows to justify common ways of representing them. But I think this idea is broken as a venture thesis, at least in its original form. The best vertical SaaS products eventually evolve into configurable platforms, with internal or external sales engineers, consultants, and deployment teams responsible for configuring the apps for each company. Which then begs the question, why do you want a shittier platform than a generalized one where the agent can fully operate on?
>
> My view is that this entire process will be done by agents on command, down to the most granular interface (whether you call it a single Claude Artifact or something else). Instead of relying on a vendor's implementation team to customize the software, users will be able to ask their agents to modify the applications directly. Creating these types of reverse-engineering artifacts is simply not friendly within the bounds of existing OS, but a separate application, whether on the browser or as a desktop application, has the full opportunity to support this.
>
> T3, Claude Cowork with customization, and installable Claude Artifacts all point in this direction.
>
> We will have different containers for apps (which themselves can also be apps):
> - Tmux-like interfaces. Already heavily explored by the better coding agent applications.
> - Apps embedded within messages. Already a default pattern, with apps in the sidebar also becoming standard in 2025-2026.
> - App-centered interfaces with chat in the sidebar. This inverts the relationship, making the app primary and chat secondary (e.g., Claude in Excel), similar to how agents are embedded in existing applications.
>
> These types of views will all continue to exist. But we'll also have:
> - Infinite canvases (tldraw). Useful for expressing things like ComfyUI workflows or designs in tools like Paper or Figma, where an interface could be represented as an infinite canvas with each component being an image-display App.
> - Fixed canvases with layered windows. The default OS experience.
> - Resizable panels with fixed widths and heights. Similar to Metabase.

Relevant: Rex, OpenCode Rune.

## 3. The argument in one pass

The document is a synthesis of mainstream late-2026 agent-infrastructure positions, assembled into a platform thesis. Its structure is: eight primitives, each asserted with a "Relevant" product list as evidence that the piece already exists somewhere. The eight claims and where each one actually sits:

**1. Agents as actors.** Claim: scalable agent workloads currently deploy with Temporal (a durable workflow engine) and should shift to the actor model, because actors give every agent harness a fully independent runtime, which is required for "self-improving harnesses" (an agent writing its own extensions or hooks on the fly), and which lets different agent-loop implementations share one backend. Prior art: actors are Hewitt (1973) with a production lineage in Erlang/OTP, Akka, and Orleans; the workflow lineage is Temporal, Restate, and DBOS. Battle lines: the claim fuses two orthogonal axes, runtime isolation (actors) and durable replay (workflows). Actors guarantee message-passing concurrency and per-actor isolation, not durability, which must be bolted on. Suh's strongest point is real: a self-modifying harness breaks deterministic replay, because replay requires the same code path on resume and an agent rewriting its hooks mid-run violates that. The strongest counter is equally real: agent workloads are long-horizon and stateful, with tool calls and multi-day waits, which is exactly the durable-execution sweet spot, and actors alone lose progress on restart.

**2. Environments and computers.** Claim: support both cloned checkpointed cloud sandboxes and users' local machines; N agents to M computers (1,000 agents on 100 VMs); environments configurable agentically. Grounding: sandbox checkpointing and forking is mature (E2B restores from a memory snapshot in about 150 ms; Modal's snapshot_filesystem yields a reusable image; isolation is tiered across Firecracker microVMs, gVisor, and plain containers). Battle lines: N-to-M is a real axis but the binding resource is token throughput and shared state, not VM count, and agent loops are I/O-wait dominated, so M much less than N is unremarkable. "Swarm" is a marketing frame; the honest axis is checkpoint granularity. The genuinely novel bit is agentically configured environments, and it collides with the reproducibility the first half of the claim depends on.

**3. RBAC-ed filesystem.** Claim: swarms share a remote POSIX filesystem with access control attached to the filesystem rather than the computer, "part GitHub, part Google Drive," hosting .env files, versioned per directory with git or jj. Prior art: POSIX-over-object-storage is established (JuiceFS, Archil, AWS EFS, Mountpoint for S3), and jj is a real VCS. Battle lines: this is the document's riskiest claim. A shared writable filesystem holding .env files, used by agents that write their own extensions, is a privilege-escalation and secret-exfiltration surface; one path-traversal or symlink bug reads every tenant's secrets. The partial defense is that per-directory version control adds audit and reversibility that per-host RBAC cannot, if the layer is rebuilt as a data plane guarded by short-lived capability tokens rather than ambient POSIX credentials. "Part GitHub, part Drive" waves at the hard part, which is reconciling per-directory git semantics with concurrent multi-writer swarms.

**4. Separation of session and conversation.** Claim: apps should not expose the raw agent session (tool calls, intermediate steps); the UI should be a "conversation" at the abstraction level of a Slack channel, and the session is for debugging, like reading the codebase. Battle lines: this is contrarian to the visible product trend. ChatGPT, Claude, and Cursor all surface traces, and the direction of travel is more transparency, because trace visibility buys trust, prompt-injection detection, debugging, and correction. Precedent for the split exists in CI/CD (build logs versus the PR view) and cloud consoles (activity feed versus raw logs), so the thesis is a product-design bet that trades observability for calm, not a law.

**5. Inbox.** Claim: users will interact with a focused inbox of approvals and questions rather than reading conversations, and the inbox should host tenant-specific apps for reviewing intermediate work. Prior art: GitHub PR review as an approval queue on diffs, Zapier's task history, and human-in-the-loop interrupts in LangGraph, the OpenAI Agents SDK, and Temporal signals. n8n's own guidance positions the approval checkpoint explicitly, distinguishing an AI that drafts for human approval from one that sends itself. Battle lines: approval UX is well-trodden and unsolved (batch versus real-time, SLA pressure, approval fatigue), and routing all interaction through approvals under-serves low-stakes exploratory work where reading is the point. Hosting review apps in the inbox re-derives the app-as-artifact thesis one layer up.

**6. Listeners, monitors, single-tenant data.** Claim: agents should define per-tenant event streams (WSS, Kafka, CDC) and translate them into signals, buildable on the fly without platform support, and this is a "strict superset" over the industry's hourly cron and bespoke webhook plugins. Prior art: Kafka, Debezium CDC, Postgres logical replication, and WebSockets are all long-established. Battle lines: "strict superset" holds for expressiveness (CDC observes every row change; a generic listener subsumes a specific webhook) and fails as stated for delivery semantics. Webhooks are push with at-least-once and signatures, cron is pull with idempotency, and a Kafka or WSS listener adds ordering and replay at the cost of offset management, dead-letter queues, and backpressure. The industry has supported CDC triggers for years, so "without platform support" is a tenancy-ergonomics claim, not a capability claim. Letting agents define their own event topology on the fly also invites topic sprawl and runaway cost.

**7. Workflows.** Claim: durable per-tenant workflows; drag-and-drop (n8n, the original Zapier) is inferior to code-defined workflows; the agent platform should be where workflows are defined because it centralizes data flow through APIs and MCPs. Grounding: n8n ships a built-in MCP server so an AI client can build and run workflows by description, and n8n's own decision framework routes deterministic recurring work to a workflow and judgment-heavy work to an agent. Battle lines: the n8n-versus-code debate has partly resolved to hybrid, which weakens the flat "inferior" framing, since the canvas wins on connector breadth and non-developer authorship while code wins on version control, testing, CI/CD, and observability. "Centralize data flow through MCP" is a real architectural bet, but MCP still lacks mature authorization, cost control, and durable execution, so it is an integration seam rather than a workflow substrate.

**8. Apps (Aka Artifacts).** Claim: Replit, Claude Artifacts, and ChatGPT Apps converge on one "app" concept; all interfaces should be apps in the user's filesystem, each user getting a modifiable clone of the codebase; the generative-UI representation debate runs JSON versus an HTML-hybrid DSL versus a "Rune App"; the platform is "an OS within an OS"; and vertical SaaS is a broken venture thesis because the commonality within a vertical is the noun ("review XYZ") rather than the process, so its best form is a configurable platform whose configuration work goes instead to agents on command. Grounding: the three products do converge on a generative-UI surface while diverging on deployment abstraction (a rendered component in a panel; an MCP server bound into the chat client; a deployed app at a URL). OpenUI's 2026 report splits generative UI into transport (AG-UI, MCP Apps) and format (OpenUI, A2UI, json-render, raw HTML), benchmarks OpenUI Lang at 4,800 tokens against YAML at 9,122 and json-render at 10,180, and notes that small models emit valid A2UI for only 3 percent (2B) and 62 percent (4B) of requests. Battle lines: artifacts-as-apps is converging in fact while the durable format stays unsettled, and the live argument is the tradeoff between declarative JSON (safe, terse, portable) and raw HTML (expressive, unsafe). The OS analogy is a rhetorical frame with a long lineage, useful for structuring a platform story and not falsifiable.

**On the vertical-SaaS half specifically.** This is the document's strongest and least original argument. Foundation Capital's services-as-software essays argue Suh's direction almost verbatim, including "the collapse of software primitives" and the claim that differentiation comes from implementation done by forward-deployed engineers. The strongest published reply is Euclid VC's "The Siren Song of Services," which argues that services-as-software risks low margins and low moats, that durable defensibility still rests on software and proprietary data, and that sizing TAM as all labor is inflated because automation has not replaced labor one-for-one historically.

**Where the document sits.** INTERPRETATION: it is a coherent synthesis, not a new theory. Durable execution as baseline, sandbox checkpoint and fork as mature, MCP as the integration seam, generative UI converging on a declarative-versus-open split, and services-as-software as the business frame are all mainstream 2026 positions that Suh has assembled well. Its three distinctive and contestable bets are the actor runtime over durable workflows (contested by the durable-execution camp), RBAC on a shared filesystem that holds tenant secrets (the riskiest), and the session/conversation split (contrarian to the visible product trend).

## 4. The named products, and what they actually are

The document's "Relevant" footers function as an implicit claim of research. Several names do not survive checking, which is worth knowing before treating the list as a market map.

**Runtimes and orchestration**

- **Cloudflare Durable Objects.** Per-key, single-threaded compute objects with attached transactional storage, part of Cloudflare Workers. FACT. Genuinely an actor-model primitive, the closest mainstream cloud analogue to a classic actor, and the only one here that is global by default and fully serverless. It is not a workflow engine and ships no scheduler.
- **Rivet.** Self-hostable runtime built around Rivet Actors (durable actors with per-actor SQLite state, WebSockets, hibernation), plus a workflow engine and sandbox integrations. FACT. The blueprint calls it both a workflow engine and an actor runtime, which is accurate but historically ordered: Rivet began as a game and real-time backend (rivet.gg), rewrote its own scheduler at its December 2024 relaunch as an in-house "actor-like workflow engine," and now markets actors first. Rivet Workflows shipped 2026-02-24.
- **Vercel Eve.** Open-source agent framework from Vercel where each agent is a directory of files (instructions.md plus tools, skills, subagents, channels folders), scaffolded with `npx eve@latest init`. FACT: real and shipping, contrary to the reasonable suspicion that it might not exist. It is a framework and deployment target, not a compute primitive.
- **Pi Durable x Extensions.** Not a single product. "Pi Durable" is an experimental durable agent-harness package from Earendil (npm @earendil-works/pi-durable) built on the minimal Pi harness; "Extensions" is its pluggable unit (a named bundle of prompt sections, tools, hooks, and tasks). FACT. The "x" is the blueprint's notation for a framework crossed with a host: Cloudflare ships a PiHarness binding to run it inside a Durable Object, and Rivet ships @rivet-dev/pi to run it inside a Rivet Actor. Beta, with the API warned to change between releases.
- **"DeepSeek Agent"** does not exist under that name. FACT: the matching real product is **DeepSeek Harness** (dsh), an MIT-licensed open-source agent runtime from DeepSeek built on the Cordis kernel, shipping as a developer preview since 2026-08-13, whose organizing rule is "everything is a plugin," model, tools, skills, sessions, sandboxes, filesystem, loop, and UI all swappable behind stable context keys.

**Environments and computers**

- **Cua.** Open-source infrastructure for computer-use agents from Cua AI, Inc. (trycua/cua): cross-OS sandboxes, drivers, SDK, CLI, and benchmarks, including a Cua Driver that lets agents drive real Mac, Windows, and Linux applications in the background while the user keeps working. FACT, MIT licensed, shipping. This is the hands-and-eyes layer; the others stop at shells and files.
- **"Claude Remote"** could not be verified as a product name. The real thing it most likely denotes is Anthropic's remote and cloud execution for Claude Code (managed sandboxes, web or mobile initiated sessions). FACT for Claude Code's remote execution existing in some form, UNVERIFIED for the name.
- **Cursor Agent.** Cursor's background and cloud agents: take a task, run in a Cursor-managed remote environment, return a branch or PR. BACKGROUND (not re-verified this session). The tightest loop between an IDE and a remote agent that opens a PR.

**Storage**

- **Archil** (archil.com). POSIX-compatible filesystem backed by object storage, aimed at AI agents: one disk mounted in many places at once, each file stored as an ordinary object any S3 tool can read, plus an agent-focused SDK and a mount CLI with conditional writes. FACT. Unusually, it targets agent workloads directly rather than general enterprise storage.
- **JuiceFS** (Juicedata). Open-source POSIX-compatible distributed filesystem keeping data in object storage and metadata in a separate database (Redis, TiKV, MySQL). BACKGROUND. The strongest fit of the three for a real multi-agent shared filesystem, because separating metadata from data is what yields correct POSIX semantics and concurrent multi-node access without the weak consistency of a bare S3 mount. JuiceFS now markets this use case directly.
- **"S3 Filesystems"** is a category, not a product. FACT. Real members are Mountpoint for Amazon S3, s3fs, and JuiceFS. The semantics gap matters: a plain S3 mount gives weak POSIX consistency and no multi-writer coordination, which is precisely the problem a multi-agent shared filesystem must solve.

**Agent front-ends** (the cluster the blueprint treats as competing)

- **Duet** is Claude Duet (Anthropic), a proactive agent app that flags what needs attention and drafts replies, shipping as an iOS and Android app and on claude.ai. FACT.
- **Grokbot** is Grok Bot (xAI), "your team of always-on agents," each with its own cloud computer working inside your applications. FACT. It is an xAI product, not a hobbyist project, which is worth stating because the name suggests otherwise.
- **Dots** is Dots (OpenAI), always-on agents. FACT, from an official OpenAI URL surfaced in search.
- **T3** is T3 Chat (Theo Browne, t3dotgg), a fast multi-model chat app. FACT. The blueprint's referent is the chat app, not the unrelated T3 stack.

**Inbox and eventing**

- **"MS Today by @nicbstme"** is Microsoft "Today," led by Nicolas Bustamante at Microsoft (previously founder of fintool, acquired by Microsoft, and of Doctrine, acquired by LexisNexis), a product shown across the Ignite conference. FACT. The "MS" prefix is the blueprint's disambiguator.
- **Claude Code Monitor** is the Monitor tool inside Claude Code (Anthropic): a built-in capability letting the agent watch a background process and react, framed against polling. FACT. A feature, not a standalone product.
- **"Grokbot future feature"** is a planned, unshipped capability. INTERPRETATION; xAI roadmaps are not public.

**Workflows and apps**

- **Zapier Zap** is a unit of automation (one trigger plus its actions). BACKGROUND.
- **Rex** is Rex, Superlogical's agent multiplexer ("an agent board and a real terminal"). FACT, with the referent inferred from cross-references (INTERPRETATION).
- **"OpenCode Rune" / "Rune App"** is Rune, Anomaly's pre-release Rust native UI framework for GPU-rendered interfaces across desktop and web, coupled to OpenCode (its component kit ports to match @opencode/ui, and the repository's opener is an OpenCode agent bot). FACT for the repository (MIT, created 2026-10-22); NOT shipping. "Rune App" is the framework's app format, not an established standard.
- **Claude Artifacts** is a self-contained runnable output rendered in a side panel. BACKGROUND. Its app abstraction is a rendered, shareable component, not a deployed service.
- **ChatGPT Apps** are built on the OpenAI Apps SDK, MCP-based, surfaced inside ChatGPT. BACKGROUND. Its app abstraction is an MCP server exposed as an interactive surface in the chat client.
- **Replit** is a browser IDE and hosting service that builds and deploys full apps from prompts. BACKGROUND. Its app abstraction is a deployed hosted application at a URL, the most "real software" of the three.
- **tldraw, ComfyUI, Figma, Metabase** are BACKGROUND, real, and used as exemplars of canvas and panel UI patterns rather than as agents.
- **Claude Cowork** (Anthropic's knowledge-work agent) and **Claude in Excel** (an add-in in the Claude for Microsoft 365 family) are FACT and shipping.
- **"Paper"** could not be verified. Candidates include paper.design, a canvas design tool, or a generative-UI format of that name. Treat as unidentified.

**Naming accuracy, summarized.** Two names are non-products ("DeepSeek Agent," "S3 Filesystems"), one is unverified ("Claude Remote"), one is notation rather than a name ("Pi-Durable x Extensions"), and one is unidentified ("Paper"). The remaining references check out, unusually for a crowded list, and Rivet's dual framing is more accurate than it first appears. The pattern suggests shorthand written from working knowledge rather than a researched market map.

## 5. The author, the JEV item, and reception

**Who he is.** FACT: John Suh is Sangwon "John" Suh, @john_ssuh, blue-verified, San Francisco. Per his own site (suhjohn.com, "John's scratchpad"): Princeton CS (started as a Philosophy major), backend engineer at Robinhood on Debit Card deposits and withdrawals, South Korean military service (Sergeant, intelligence, interpreter for Korean Special Forces in Abu Dhabi), co-founder of a consumer-AI-chatbot startup acquired by a long-term holding company, and currently "a Partner at a long-term holding company that buys services businesses and leverages AI to improve operations." The holding company is Long Lake, named in his X bio; the chatbot startup was Superdrop, acquired by Long Lake. His X bio reads "Building | prev: Founding team @ Long Lake." His X account joined 2025-10-31 and had 4,825 followers and 682 posts at capture.

INTERPRETATION, caution: aggregator pages also attach "Venture Partner at Spring Ventures" to a John Suh, and several well-known men share the name (Hyundai CRADLE's John Suh, the former LegalZoom CEO). Those are almost certainly person-conflation and should not be attributed to @john_ssuh without a primary source.

**Not Runwork.** FACT: nothing connects Suh to Runwork.ai, whose founder and CEO is Oytun Tez, despite the category overlap. The Substrate's [[runwork-ai-deep-dive]] remains the nearest commercial instance of the thesis, and this document sits beside it rather than overlapping it.

**The JEV item, which is the load-bearing detail for this Substrate.** FACT: the blueprint's event-listener passage says "have JEV filter over it, and trigger an agent run on that email." JEV resolves to **Jev, TypeSafe AI's first "System One Model"**, announced 2026-09-15 by founder Diogo Almeida (ex-OpenAI): unstructured state in, typed probabilistic decisions out, 70 to 500 ms responses, calibrated confidence on every answer, with claims that it cannot hallucinate or commit type errors. It is in early access, waitlist-based as of capture. INTERPRETATION: the blueprint uses Jev as a fast typed classifier and confidence-gated triage over inbound email, deciding whether a message should wake an agent. The Substrate has no node for Jev or System One models yet; this is the first place the concept appears in the knowledge graph, and it deserves its own file. Note for the operator: this is the same Jev you have been exploring, and this is the first third-party document in the graph that names it as a production pipeline component rather than a research curiosity.

The significance is not that the reference is obscure. It is that a blueprint pitching "the one and only application layer" reaches for a niche early-access classifier as its own argument's example. That tells you something about the author's proximity to the ecosystem and about how the demand side is starting to name primitives.

**Reception.** FACT (~14 hours after posting): 4,435 likes, 327 replies, 327 retweets, 204 quote-tweets, 13,140 bookmarks, 632,089 views. The bookmark-to-like ratio is unusually high for a text post, consistent with people saving the blueprint. Named responses found: Elvis Saravia (DAIR.AI) called it "a great recap of the key primitives of strong agent platforms"; John A. De Goes (Golem Cloud) quote-tweeted that "the agent platform of 2027 has a name. It's called @GolemCloud," a rival claiming the space; and several summarizer and riff accounts amplified it. No substantive technical critique and no response from a named frontier-lab figure surfaced in the indexed results.

**What he might be building.** FACT: he writes "I have reasons to believe that an independent company will own this product layer" and names no company. His bio says "Building" while his site says he is a Partner at a holding company. INTERPRETATION: the tweet reads as a stealth-founder pitch. It asserts that the layer will be owned by an independent company rather than by ChatGPT's or Claude's parent, that most ADE, enterprise-agent, and vertical-SaaS players are "not technically competent," and that the author has inside reasons to think the space is open. The most defensible reading is that he is founding or assembling something in or alongside Long Lake. UNVERIFIED: no company name, funding, or team confirmed.

## 6. Where the mapping breaks

- **It is an unpublished draft, so it should be read as a pitch, not a paper.** No date, no byline page, no archive, no version history. Reading a screenshot of a working document as a citable source is the first error to avoid, and this file's transcription is a second-hand image read, not a text.
- **The authority is argumentative, not positional.** The author's public trail is thin: a scratchpad page, a young X account, a LinkedIn. He is ex-Robinhood and ex-a-military-intelligence-interpreter with a Princeton CS degree and a chatbot acquisition behind him, which is a real record, and it is not a record of having shipped an agent platform. The blueprint's force has to come from its reasoning.
- **The reference list is looser than it looks.** A document that misnames products in the very list meant to demonstrate research ("DeepSeek Agent," "S3 Filesystems," "Claude Remote," "Pi-Durable x Extensions," "Paper") is either using working shorthand or has done less checking than the format implies. Either way, the "Relevant" footers should not be read as a vetted market map, and this file's section 4 is the correction.
- **The central claim is unfalsifiable as stated.** "The one and only application layer software that will exist" and "every other software will effectively become databases for this layer" are rhetorical frames, not predictions that could be tested and fail. The document is strongest exactly where it stops making total claims and starts naming mechanisms.
- **Its most interesting architectural bet is also its riskiest.** A shared writable filesystem holding .env files, operated by agents that write their own extensions, is a privilege-escalation surface by construction, and this risk gets one line of treatment in the original. The document's treatment of authorization is thinner than its treatment of durability, which is a strange ordering for a platform that would hold every tenant's secrets in one namespace.
- **The actor-versus-workflow bet is genuinely contested and the document does not present the other side.** Durable execution exists because long-horizon agents lose work on restart, and the durability camp has the clearer published case (Temporal's own docs, Martin Fowler's write-up on durable execution for exactly this workload). Suh's self-modifying-harness argument is a real objection to deterministic replay, and he does not engage with what replaces the guarantees he would give up.
- **The session/conversation split runs against the market.** Every major agent product is moving toward more trace visibility, for reasons of trust, debugging, and injection detection. The document's position is defensible as a design bet and is presented as settled. It is not.
- **"Not technically competent" is a competitive claim, and it is aimed at competitors.** The tweet disqualifies "most ADE, enterprise agent platform, or vertical saas companies" and asserts an independent company will win. That is a founder talking about his own market. The judgment may be right and it is not evidence.
- **The garden metaphor and the "factory of a factory" jab are positioning.** "Factory of a factory" is a recognizable formulation in the same discourse, and Suh explicitly drops it to a shrug ("imo"). The framing choice is rhetorical, and the two frames are not actually in tension: a platform that hosts agents which build software for other companies is a factory of factories by another name.
- **Reception is amplifying, not vetting.** 632,000 views and 13,140 bookmarks in fourteen hours means reach, not endorsement. The absence of technical critique in the indexed replies is an absence of critique, not a pass. One rival founder's "it has a name and it's mine" is the only adversarial response found, and it is not a technical argument.
- **The vertical-SaaS argument is the strongest part and the least original.** Foundation Capital has made this case in public for some time, and Euclid VC's reply is the strongest counter. Suh's contribution is the platform framing of it, and the framing is where the unfalsifiable language creeps back in.
- **For this Substrate specifically, the competitive read matters.** The category the document describes, an application layer where agents build and fork the interfaces, is the same territory as the operator's own agent-factory and agent-onboarding work. That is the reason to keep this file, not the document's own merit.

## 7. Compression points for synthesis

1. "Agent platform 2027" is an unpublished working draft by John Suh (@john_ssuh), circulated on 2026-11-22 as a four-image tweet that drew 632,000 views and 13,140 bookmarks in fourteen hours. It has eight sections, each closing with a "Relevant" product list.
2. Its thesis: one application layer absorbs everything else as databases, the interface must be agent-forkable rather than vendor-configured, and the win goes to whoever gets the primitives right. It claims an independent company, not OpenAI or Anthropic, will own this layer.
3. The primitives proposed are actor runtimes over durable workflows, N-agents-to-M-computers sandbox fleets, an RBAC-ed shared POSIX filesystem, a session/conversation split in the UI, an approval inbox, per-tenant event listeners, code-defined workflows, and apps-as-artifacts.
4. The strongest architectural claim is the actor model over Temporal-style durable execution, on the grounds that self-modifying harnesses break deterministic replay. The strongest counter is that long-horizon agent work is exactly the durable-execution case, since actors lose progress on restart.
5. The riskiest claim is the RBAC-ed shared filesystem holding .env files and used by self-extending agents, which is a privilege-escalation and secret-exfiltration surface by construction and gets one line of treatment in the original.
6. The most contrarian claim is the session/conversation split, which runs against the visible product trend toward more trace visibility across ChatGPT, Claude, and Cursor.
7. The vertical-SaaS critique is the document's strongest and least original argument: it matches Foundation Capital's services-as-software position closely, and Euclid VC's reply (low margins, low moats, inflated TAM) is the strongest published counter.
8. The product reference list is looser than it appears: "DeepSeek Agent," "S3 Filesystems," and "Claude Remote" are not products, while Vercel Eve and Rivet are real and more interesting than their one-line treatment. Rivet's dual actor-plus-workflow framing is accurate; the pivot from game backend to actor runtime is the substantive history.
9. The document names JEV, which resolves to Jev, TypeSafe AI's first System One Model (typed probabilistic decisions, calibrated confidence, 70 to 500 ms). This is the first appearance of Jev in the Substrate, and it is the clearest signal of the author's proximity to the live ecosystem. It deserves its own node.
10. Read it as competitive intelligence in the agent-platform category, not as a technical source: the argument is a competent synthesis of mainstream 2026 positions, the contested bets are the actor runtime and the filesystem permissions model, and the authority behind it is argumentative rather than positional.

## Sources

### Verified live this session

- The tweet: x.com/john_ssuh/status/2124336124172935336 (John Suh, 2026-11-22T02:56:14Z, 4 images, note tweet). Retrieved via https://api.fxtwitter.com/john_ssuh/status/2124336124172935336 and https://cdn.syndication.twimg.com/tweet-result?id=2124336124172935336 (both mirrors, agreeing).
- The four images (transcribed from the CDN copies this session): pbs.twimg.com/media/HXsjmKvaAAAMOdo.jpg, HXsjqh8bIAAUJ3-.jpg, HXsjuw-acAAJhec.jpg, HXsk6XWbIAAUiiO.png
- Author identity: https://api.fxtwitter.com/john_ssuh (profile JSON) and https://suhjohn.com/
- Unpublished status: suhjohn.com/writing and suhjohn.com/agent-platform-2027 both 404; no blog, Substack, or company post found.
- Reception: x.com/omarsar0/status/2124506354324840953 (Elvis Saravia), x.com/jdegoes/status/2124498906696618035 (John A. De Goes), x.com/AGTPinsights/status/2124450596421820905, x.com/0interestrates/status/2124376938903220555, x.com/olegakbarov/status/2124355361847320555 (handle as returned), x.com/0rdlibrary/status/2124521782136709583
- Infrastructure products: vercel.com/eve and github.com/vercel/eve; rivet-dev/rivet and rivet.dev/workflows plus rivet.dev/changelog/2026-02-24-introducing-rivet-workflows; github.com/anomalyco/rune (PLAN.md, crates/rune-kit); trycua/cua and cua.ai; archil.com; docs.capy.ai/captains
- Front-end products: claude.com/product/claude-duet; x.ai/news/introducing-grok-bot and docs.x.ai/grok-bot/overview; openai.com/index/introducing-dots; t3.chat; x.com/nicbstme; claude.com/product/cowork and claude.com/claude-for-microsoft-365; superlogical.com (via github.com/jeffarese/chompy and github.com/almonk/rexpad); JuiceFS blog "Giving AI Agents a Real File System"
- Jev: typesafe.ai/blog/introducing-system-one-models-and-jev, docs.typesafe.ai, github.com/typesafe-ai/system-one-adapter-python
- Theses grounding: Temporal "Durable AI" docs (docs.temporal.io/ai); Martin Fowler, "Long-horizon agents and durable execution"; DBOS comparison (docs.dbos.dev/explanations/comparing-temporal); E2B Firecracker memory-snapshot restore figure; Modal snapshot_filesystem docs; n8n MCP server docs; OpenUI "State of Generative UI 2026" (token benchmark and A2UI small-model validity rates); arXiv 2603.21334 and arXiv 2610.32129; Foundation Capital services-as-software essays; Euclid VC "The Siren Song of Services" and "Service-Level Disagreement"

### Established record cited but not re-verified (verify before direct quotation)

- The actor model (Hewitt, 1973); Erlang/OTP, Akka, Orleans as production lineages; Akka Persistence and Orleans event sourcing as the durability bolt-ons.
- Temporal, Restate, and DBOS as durable-execution engines; LangGraph interrupt, the OpenAI Agents SDK, and Temporal signals as human-in-the-loop mechanisms.
- Firecracker, gVisor, E2B, Daytona, and Modal as sandbox and isolation technologies; the fly.io and pinggy isolation-tier comparisons.
- JuiceFS, Archil, AWS EFS, s3fs, and Mountpoint for Amazon S3 as POSIX-over-object-storage options; Jujutsu (jj) as a version control system.
- Kafka, Debezium, and Postgres logical replication as event and CDC infrastructure.
- The a16z "AI is the new OS" lineage, tagged BACKGROUND; a primary a16z source was not verified this session.
- The claim that Anthropic's "Formalizing Fermat's Last Theorem" run used a shell and file editor per agent. Relevant to the Substrate: [[turing-computing-machinery-and-intelligence]] and the Fermat formalization work are both AI-math data points.
- "MS Today," Dots, and T3 as of the blueprint's usage: the identity mapping is an inference in the case of "MS Today" and Dots, though each rests on an official-domain page or post seen in search results.

### Open items for a later pass

- Jev and the System One models deserve a dedicated raw file; the Substrate currently has nothing on them.
- The full X reply and quote-tweet set for the blueprint was not crawlable without the X API. A fuller reception study is a later task.
- The document may later be published in full; if it is, this file's section 2 should be replaced with the original text and the provenance note retired.
