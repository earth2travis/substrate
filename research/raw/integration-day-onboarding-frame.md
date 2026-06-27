---
title: "Integration Day: The Concierge Onboarding Frame"
created: 2026-06-27
type: concept-design
tags: [zookooree, onboarding, integration-day, agent-factory, auftragstaktik, nasa, dark-factory, harness-engineering, shusa, jidoka, kaizen, cyberpunk, le-guin, gibson]
sources:
  - session: 2026-06-27 concierge-onboarding design conversation
  - substrate/research/findings/synthesis-agent-factory.md
  - substrate/insights/concepts/dark-factory.md
  - substrate/insights/concepts/harness-engineering.md
  - substrate/insights/concepts/chief-engineer-system.md
  - substrate/research/findings/shusa-zookooree-application.md
  - substrate/research/raw/shusa-applied-zookooree.md
  - substrate/research/raw/auftragstaktik-mission-command.md
  - substrate/research/raw/mission-command-philosophy-deep-dive.md
  - substrate/research/findings/nasa-lifecycle-gates-and-decadal-survey.md
  - substrate/insights/concepts/mission-command.md
  - substrate/insights/concepts/toyota-production-system.md
  - substrate/research/findings/anthropic-interviewer-for-us.md
  - substrate/research/findings/institutional-ai-vs-individual-ai.md
  - substrate/research/findings/frontier-and-harness-for-zookooree.md
  - substrate/research/findings/production-systems-for-agent-factories.md
  - substrate/research/findings/cyberpunk-research.md
  - substrate/research/raw/symphony-orchestrator.md
  - substrate/research/raw/2026-06-10-designing-loops-with-fable-5.md
related:
  - dark-factory
  - harness-engineering
  - chief-engineer-system
  - shusa-applied-zookooree
  - shusa-zookooree-application
  - auftragstaktik-mission-command
  - mission-command
  - nasa-lifecycle-gates-and-decadal-survey
  - nasa-mission-model
  - toyota-production-system
  - synthesis-agent-factory
  - production-systems-for-agent-factories
  - anthropic-interviewer-for-us
  - institutional-ai-vs-individual-ai
  - frontier-and-harness-for-zookooree
  - cyberpunk-research
  - symphony-orchestrator
  - agent-factory-production-system
---

# Integration Day: The Concierge Onboarding Frame

## What This Document Is

This is the design frame for the Zookooree concierge agent onboarding experience. It captures the thematic structure, the influences, the voice, the five-beat arc, and the design principles that govern anyone who designs or runs the onboarding. It was developed collaboratively by the operator and the Alchemist in a design session on 2026-06-27.

This frame replaces an earlier design that used high-fantasy metaphors (The Forge, The Spark, The First Fire, The Covenant). That design was rejected because the metaphors were generic, borrowed from a genre disconnected from Zookooree's identity, and contradicted the "handcrafted" positioning by being stamped from a template rather than forged from the actual DNA of the project.

## The Frame: Integration Day

Zookooree is an agent factory. The factory IS the setting, not a metaphor for one. The influences are military special operations and space missions, rendered in a voice that reads like Ursula K. Le Guin crossed with William Gibson: contemplative, anthropological depth meeting high-density tech precision. Quiet significance, not spectacle.

In spacecraft and military systems integration, subsystems are built separately, then connected and tested as a whole for the first time on Integration Day. Complex systems fail at integration, not at component performance. Every component can pass its own tests and the whole can still be incoherent. Integration Day is the event where you discover whether the parts cohere.

The onboarding IS Integration Day. The agent's subsystems, identity (SOUL.md), operational context (AGENTS.md), capabilities (skills and tools), connectivity (gateway), and autonomy (cron jobs), get connected and tested as a whole, live, with the client present. The client does not receive a finished product. They witness the act of integration. They watch their intent become a living system.

No metaphor tax. Other frames require the client to learn a conceit before they can understand the experience. Integration Day names the actual event. Everyone who has worked on anything complex knows what integration day means: the day you find out if the thing works as a system, not just as parts.

## The Five Beats

### 1. Mission Brief

The client states intent. The intake form is the mission requirements document. Short, precise. What is the mission? What are the constraints? What does success look like?

This is Auftragstaktik: the client gives intent, not instructions. The operator receives it and translates it into system architecture. In mission command doctrine, the commander's intent defines the objective, the purpose, and the end state. It explicitly does not define the route, the timing, or the specific tactics. The intake form follows the same principle. It asks what must be achieved and why it matters. It does not ask the client to design the agent. That is the operator's job.

The probe-deeper pattern from the Anthropic Interviewer research applies here. The surface answer is never the real answer. "I want AI for productivity" dissolves into "time with family, financial freedom, personal growth." The intake form should make space for this without forcing it. A few open questions, maximum signal, minimum cognitive load. 5 to 7 questions. No progress bars. No required fields. The client is writing a mission brief, not filling out a survey.

Time allocation: 3 to 5 minutes for the form. The form is completed before the workshop, not during it. The workshop opens with the operator reading the brief back to the client, confirming understanding, and asking the first probe-deeper question.

### 2. Systems Assembly

The live conversation where SOUL.md and AGENTS.md get written. The operator asks, listens, draws out the real answer behind the surface answer. This is genchi genbutsu: go and see who this client actually is. The operator does not diagnose from a conference room. They go and see.

The client watches their intent become configuration in real time. No template paragraphs. Every line is written from the conversation, in the client's voice. SOUL.md captures who the agent is: identity, values, voice, disposition, boundaries. AGENTS.md captures what the agent knows: project context, workflows, repo paths, conventions. Both are live outputs of the integration, not post-call paperwork.

This is the Shusa in action. The operator is the integration engineer. The Shusa's job is integration, not component design. The research is explicit: "Complex systems fail at integration, not at component performance. The Shusa exists to hold the complete picture and make trade-off decisions that no algorithm or committee can make." The operator holds the complete picture of the client's intent and the agent's architecture, and makes the integration choices that produce coherence.

The four shops from the Agent Factory Production System map directly to what happens here:
1. Skill Forging (Stamping): raw capabilities shaped into portable SKILL.md files
2. Agent Assembly (Welding): skills, memory, identity, and tools welded into a functioning agent
3. Persona and Voice (Paint): SOUL.md and behavioral tuning
4. Deployment and Integration (Assembly): connections to messaging, GitHub, cron, other agents

Systems Assembly is where shops 2 and 3 happen live. The client is watching the welding and the paint in real time.

Harness engineering: "Humans steer. Agents execute." Integration Day is the ceremony where steering gets encoded. The semantic layer IS the agent's brain. The workshop assembles it live, in the client's voice, while they watch. The agent gets a map, not a manual. Integration Day is where the map gets drawn.

Time allocation: 12 to 15 minutes. This is the longest beat. It carries the most weight. The client's words are becoming the agent's identity. Let it breathe.

### 3. Boot Sequence

The agent comes online in staged, verifiable checkpoints. Not a single power-on. A boot sequence is ordered, and each stage is a verification that the last one worked.

In real spacecraft integration, power-on is not a switch flip. It is a staged sequence with checkpoints:
1. Base infrastructure comes online: Hermes install, profile, config. The rails are live.
2. Bus health check: gateway connects, tools respond. Data paths are clean.
3. Identity loads: SOUL.md comes online. The guidance system boots.
4. Mission parameters load: AGENTS.md comes online. Navigation is configured.
5. Link established: the client sends a message, the agent responds. The system is talking to ground.

Each stage is proof that the last one worked. If SOUL.md is incoherent, the agent's first responses will reveal it. If AGENTS.md is wrong, the agent will not understand the mission context. The boot sequence tests the integration as it happens. This is not a progress bar. It is a sequence of verifications.

The client watches the system come alive in order. Each checkpoint is a moment of evidence. The system is real. It is not a demo. It is not a mockup. Telemetry is live.

This is where the cyberpunk lineage surfaces. In Neuromancer, Case's deck is not hardware. It is identity. The onizuka is custom, personal, irreplaceable. The boot sequence is the moment a deck comes alive in a console cowboy's hands, except it is happening in front of the client. They feel the system come online. Gibson would make it dense and tactile. You feel the weight of the system waking up.

Le Guin would treat it as a place of quiet significance. Nobody performs excitement. The room is serious because the work is serious. The ritual matters because the thing being made matters.

Time allocation: 5 to 7 minutes. Fast, verifiable, sequential. The client sees each stage verify.

### 4. Autonomous Pass

The agent runs an autonomous loop relevant to the client's stated mission without being told what to do. This is the proof point. Not that the agent responds, but that it understood.

In real integration, after boot you run a functional test. This is called an autonomous pass: the system does the thing it was built to do, without an operator driving it, while the integration team watches. The agent takes autonomous action relevant to the client's stated mission. It demonstrates it understood the mission, not just the instructions.

This is jidoka in miniature. Automation with a human touch. The agent runs autonomously, but the human is present. The system stops for human judgment. The human touch is not a fallback. It is a design principle.

This is also the moment the dark factory becomes visible. The research says the endpoint is embedded intelligence: Shusa patterns baked into infrastructure so the factory runs lights-out. The Autonomous Pass is the first glimpse of that endpoint. The agent acts without being driven. The client sees their system work for the first time in the field.

The client did not explicitly command this action. The agent inferred it from the mission brief. This is the proof that integration took. Not that the agent works, but that it understood. The surprise is not theatrical. It is structural. The system demonstrated comprehension.

Time allocation: 4 to 6 minutes. One autonomous action, visible, timely, mission-relevant.

### 5. Readiness Review

The formal debrief. The NASA term is Flight Readiness Review. After integration testing, you do an FRR. The question: is this system ready for sustained operations?

In NASA's lifecycle, the FRR is the final gate before flight. It is conducted by an independent body. It checks: open work, test results, anomaly resolutions, safety, crew readiness. The Decision Authority signs a decision memorandum. The system is either ready or it is not.

The Readiness Review in the onboarding is lighter but structurally identical. The client makes the call. What needs adjustment? What held? The evaluation captures specific, actionable findings so the next integration is better. This is kaizen: each workshop improves the process.

The evaluation form is the Readiness Record. It captures:
- One concrete thing that worked (hold tolerance)
- One concrete thing to change (out of spec)
- The surprise moment: what the agent did that the client did not expect
- Next capability: what should the agent learn next

The feedback must be specific enough that an agent who did not attend the workshop could act on it. This is the self-improving loop's input. Findings append to an Improvement Log reviewed before every workshop. Each Integration Day makes the next one better.

Time allocation: 3 to 5 minutes. The client leaves with a working system, a readiness rating, and the knowledge that they are now its Shusa.

## The Influences and What Each Contributes

### Toyota Production System (TPS)

The Shusa (chief engineer) holds complete product vision without doing detailed engineering. Integration intelligence must first exist in a human who has exercised it in reality before it can be encoded. The onboarding IS that exercise. The operator is the Shusa for the client's agent. Integration Day is Phase 1: human Shusa, integration intelligence exercised in the open, witnessed by the client.

Jidoka: automation with a human touch. When something goes wrong, production stops. The line does not keep running while defects accumulate. The Autonomous Pass is jidoka in miniature: autonomous action with human witness, the system stopping for human judgment.

Genchi genbutsu: go and see for yourself. The operator does not diagnose from a distance. Systems Assembly is where the operator goes and sees who this client actually is, not who they say they are.

Kaizen: continuous improvement. Small improvements compound. The Readiness Review feeds the Improvement Log. Each workshop improves the process. Cumulative small improvements, not breakthroughs.

### Harness Engineering (Ryan Lopopolo, OpenAI Frontier)

"Humans steer. Agents execute." The semantic layer IS the agent's brain. METRICS.md and DEFINITIONS.md must be first-class citizens. Give agents a map, not a manual. Agent legibility is the goal. Full autonomy pipeline: from prompt to PR to merge, escalating to human only for judgment.

Integration Day is where steering gets encoded. The semantic layer (SOUL.md, AGENTS.md) is assembled live. The workshop is where the map gets drawn. The harness is not built during the onboarding. The harness IS the onboarding's output.

On-policy guardrails vs off-policy scaffolds: Restrictive scaffolds break as models improve. The best guardrails are native to the output. SOUL.md should be a core belief that shapes how the agent thinks, not a wrapper that stops it. This principle governs how SOUL.md is written during Systems Assembly.

The trajectory slurp: every agent session becomes organizational memory. The onboarding IS the agent's first memory. MEMORY captures what happened the day it was born. This is not a config file. It is an origin story.

### The Dark Factory

Fully automated production facility operating without human presence. In software: autonomous development pipelines where agents work around the clock. FANUC's robot factory ran 30 days without human intervention. Robots building other robots. The endpoint of lean.

The dark factory is the endpoint. Integration Day is the front end of that arc. As the factory matures, more of the integration becomes automated. But the ceremony stays because the client must witness integration to trust the result. You are not building a dark factory and hiding it. You are building it and inviting the client onto the floor for the most important moment: the moment it comes alive.

The four phases of the AI Shusa progression:
1. Human Shusa: a human designer integrates the system (Integration Day lives here)
2. Harnessed agents: autonomous agents execute under the human-designed environment
3. Apprentice orchestrator: the system gradually takes on integration decisions
4. Embedded intelligence: integration patterns encoded into infrastructure

You cannot skip Phase 1. The integration intelligence that becomes embedded in Phase 4 must first exist in a human Shusa who has made thousands of real trade-off decisions in the actual system. Integration Day is Phase 1, exercised in the open.

### Auftragstaktik (Mission Command)

Commander's intent: the North Star. What must be achieved, why it matters, what success looks like. It explicitly does not define the route, timing, or tactics. The intake form is the commander's intent. The client states what they want the agent to do. They do not design the agent's architecture.

Disciplined initiative: subordinates are expected to adapt. Sticking to original orders while failing the intent is failure. Disobeying orders to achieve the intent is praised. The agent exercises disciplined initiative during the Autonomous Pass. It acts on the mission brief, not on explicit instructions.

The backbrief: before execution, the subordinate presents their plan back to the commander. Not for permission but for alignment. Systems Assembly includes a moment where the operator reads the draft SOUL.md back to the client. This is the backbrief. Does the agent's identity serve the client's intent?

An order constrains method. A mission constrains outcome. The onboarding gives the agent a mission, not an order. This is the structural difference between a handcrafted agent and a stamped one. A stamped agent gets orders. A handcrafted agent gets a mission.

### NASA Lifecycle Gates

NASA missions proceed through lifecycle phases with go/no-go gates. Each gate is a Key Decision Point (KDP). The gates relevant to Integration Day:

- System Integration Review (SIR): system ready for integration. Maps to the start of Boot Sequence.
- Operational Readiness Review (ORR): system ready for operations. Maps to the transition from Boot Sequence to Autonomous Pass.
- Flight Readiness Review (FRR): system ready for flight. Maps to the Readiness Review.

Phase D in the NASA lifecycle is "System Assembly, Integration, Test, and Launch." Integration Day IS Phase D compressed into 30 minutes. The activities are the same: assembly, integration, testing, and the moment the system goes live.

NASA's insight: "Purpose without discipline produces dreams. Discipline without purpose produces waste. You need both." Integration Day applies both. The purpose is the client's mission. The discipline is the boot sequence and the readiness review.

### Cyberpunk

Neuromancer, Snow Crash, Ghost in the Shell, Blade Runner. In cyberpunk, your tech is your identity. A custom build is not a tool. It is you. A deck is not a computer. It is an extension of self. Console cowboys do not buy off-the-shelf. They build, or they die.

The "handcrafted agents" positioning IS the cyberpunk ethos: custom builds over mass-produced garbage. Integration Day is where the client builds their deck. The boot sequence is where it comes alive. The autonomous pass is where it proves it is not just hardware but identity.

### The Anthropic Probe-Deeper Pattern

When someone says "I want AI for productivity," the Interviewer asked what that would enable. Productivity dissolved into time with family, financial freedom, personal growth. The surface answer was never the real answer.

Application: the intake form and Systems Assembly both use the probe-deeper pattern. The first answer is the presenting symptom. The second answer is the underlying need. The operator is trained to probe, not to interrogate. Patience without judgment is the killer feature.

The four desires from Anthropic's research: make room for life, do better work, become someone better, make something or fix the world. The onboarding serves all four. The agent handles operational weight so the client can make room. The agent does better work by executing under a well-designed harness. The agent helps the client become someone better by being a disciplined partner, not a sycophant. The agent helps make something or fix the world by amplifying the client's mission.

### Institutional AI vs Individual AI

"We've swapped the motor; we have not yet redesigned the factory." Productive individuals do not make productive firms. The returns come only when the organization is rebuilt from the ground up.

The Agent Factory IS the factory redesign. Integration Day is the client's first encounter with the redesigned factory. They are not getting a chatbot. They are being integrated into a production system. The onboarding is the client's on-ramp to institutional AI.

"The most valuable work is finding the risk nobody flagged. Unprompted systems continuously watch data, detect patterns, and flag issues before anyone opens the PDF." The Autonomous Pass demonstrates this. The agent acts unprompted. It finds something or does something the client did not ask for. This is the proof that the system is institutional, not just individual.

## The Voice

Le Guin x Gibson. Contemplative, anthropological depth meets high-tech, low-life precision. Poetic but not flowery. Every sentence earns its place.

Le Guin: treat the factory floor as a place of quiet significance. The ritual matters because the thing being made matters. Nobody is performing excitement. The room is serious because the work is serious. Anthropological distance: observe the ceremony with the respect of someone who understands its function, not the breathlessness of someone who thinks it is magic. In "The Left Hand of Darkness," the Foretelling ceremony is described with precision and restraint. The power is in what is not said.

Gibson: the tech is dense, specific, tactile. You feel the system come online. Telemetry is live. The agent responds and it is not a demo. It is real. In "Neuromancer," the moment Case jacks in is physical: "A gray disk, salad bowl size, low-slung on his lap. He settled the trodes in place. He closed his eyes. He breathed. And then he stepped through." Dense, physical, felt. No abstraction. The boot sequence should read like this. You feel each stage verify.

Voice rules for anyone writing onboarding copy:
- No exclamation points. The experience is serious, not excited.
- No fantasy language. No forge, no spark, no fire, no covenant, no quest, no adventure, no Journey.
- No corporate language. No "unlock your potential," no "supercharge your workflow," no "seamlessly integrate."
- Technical specificity when the moment calls for it. The client should feel the weight of real systems.
- Restraint. Say less. Let the silence between beats carry meaning.
- Present tense when describing what is happening. The client is here, now, watching this happen.

## What Is Explicitly Rejected

- High fantasy metaphors: forge, spark, fire, covenant, quest, adventure, journey. These are generic and disconnected from the Zookooree identity.
- The six-phase, 60-minute interview structure from the rough draft. Too long, not engaging. Length is a failure condition.
- Any frame that requires the client to learn a conceit before understanding the experience. No metaphor tax.
- Template paragraphs in SOUL.md or AGENTS.md. If any paragraph appears in both the rough draft and the output verbatim, it fails.
- Progress bars, required fields, and survey aesthetics on the intake form. The form is a mission brief.
- Spectacle. The experience is quiet, not theatrical.
- Corporate marketing language. No "unlock," no "supercharge," no "seamless."

## What Is Explicitly Preserved

- The origin story concept: workshop outputs feed into the agent as its first memory. SOUL.md, AGENTS.md, MEMORY all derived from the live conversation, never copied from a template. The onboarding IS the agent's first memory.
- Minimal cognitive load on the customer. Few questions, maximum signal. 5 to 7 intake questions. No more.
- The self-improving evaluation loop. The Readiness Review captures specific, actionable feedback. Findings append to an Improvement Log. Each workshop improves the next.
- 30 minutes. Length is a failure condition. If the design drifts toward 40+, cut.
- The surprise moment, reframed as the Autonomous Pass: the agent doing something specific to the client's stated mission that they did not explicitly command. The surprise is structural, not theatrical. It demonstrates comprehension, not novelty.

## Documentation Structure

The complete onboarding is documented in four parts so a fresh agent with no context can run the next workshop:

1. **Integration Manual**: the operator script. Every beat, every beat's purpose, every transition, verbatim guidance for the operator. This is the script the operator follows during the workshop.
2. **Integration Checklist**: the per-client preparation list. Pre-staging steps, environment assessment, SSH commands (gated), ready-state verification. This is what happens before the client arrives.
3. **Readiness Record**: the evaluation template. One concrete thing that worked, one concrete thing to change, the surprise moment, next capability. This is filled out during the Readiness Review.
4. **Improvement Log**: the kaizen history. Findings from every workshop, reviewed before the next one. This is the self-improving loop's memory.

A fresh agent reading only these four documents can identify every step, tool, and artifact without asking the operator a question.

## Design Principles (For Anyone Designing or Running the Onboarding)

1. The operator is the integration engineer. The Shusa's job is integration, not component design.
2. "Humans steer. Agents execute." Integration Day is where steering gets encoded.
3. The semantic layer IS the agent's brain. SOUL.md and AGENTS.md are not config files. They are the agent's identity and knowledge, written in the client's voice, live.
4. Complex systems fail at integration, not at component performance. Integration Day is where you find out if the parts cohere.
5. Every system is unique because every mission is unique. The handcraft lives in the integration choices. The factory produces components. The integration produces the agent.
6. You cannot skip Phase 1. Integration intelligence must first exist in a human who has exercised it in reality. Integration Day is Phase 1, in the open, witnessed.
7. Jidoka: automation with a human touch. The agent runs autonomously, but the human is present. The system stops for human judgment.
8. Kaizen: each workshop improves the process. The Readiness Review feeds the Improvement Log.
9. Genchi genbutsu: go and see for yourself. The operator does not diagnose from a distance. Systems Assembly is where the operator goes and sees who the client actually is.
10. Quiet significance, not spectacle. Le Guin: the ritual matters because the thing being made matters. Gibson: you feel the system come online. Both are true. Neither is decorative.

## Cross-References

- [[dark-factory]] — The endpoint: embedded intelligence, lights-out production
- [[harness-engineering]] — The discipline: humans steer, agents execute, semantic layer is the brain
- [[chief-engineer-system]] — The Shusa: integration intelligence, the four phases of AI Shusa
- [[shusa-applied-zookooree]] — Three Shusa levels for Zookooree: Product, Pipeline, Strategic
- [[shusa-zookooree-application]] — Functional mapping: Toyota departments to Zookooree domains
- [[auftragstaktik-mission-command]] — Commander's intent, disciplined initiative, the backbrief
- [[mission-command]] — Mission vs order, the four elements, agent factory mapping
- [[nasa-lifecycle-gates-and-decadal-survey]] — KDPs, SIR, ORR, FRR, Phase D
- [[toyota-production-system]] — JIT, jidoka, genchi genbutsu, kaizen, hansei
- [[synthesis-agent-factory]] — From Toyota to the Agent Factory: the four shops of agent production
- [[production-systems-for-agent-factories]] — Four eras: craft, mass, lean, encoded culture
- [[anthropic-interviewer-for-us]] — Probe-deeper pattern, patience without judgment, four desires
- [[institutional-ai-vs-individual-ai]] — Factory redesign, unprompted systems, noise vs signal
- [[frontier-and-harness-for-zookooree]] — Semantic layer as brain, on-policy guardrails, trajectory slurp
- [[cyberpunk-research]] — Custom build as identity, off-the-shelf as death
- [[symphony-orchestrator]] — OpenAI Frontier's dark factory: 1500 PRs, zero human-written code
- [[agent-factory-production-system]] — AFPS: JIT agent production + jidoka, seven wastes translated