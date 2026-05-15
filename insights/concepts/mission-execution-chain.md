---
title: "Mission → Objectives → Projects → Tasks → Execution: The Five-Domain Chain"
tags: [concept, mission, intent, cascade, handoff, objectives, OKR, MBO, BHAG, agent-native, synthesis, execution, delegation]
related:
  - mission-arc
  - mission-command
  - management-by-objectives
  - objectives-and-key-results
  - intent-architecture
  - principal-agent-theory
  - kanban-doctrine
  - opord-mission-command-synthesis
  - nasa-mission-model
  - diplomatic-mission
  - mission-in-business
  - progressive-autonomy
  - workflow-as-contract
  - centaur-principle
  - protocol-as-coordination
source: research/findings/mission-in-business.md, research/findings/nasa-mission-model.md, research/findings/opord-mission-command-synthesis.md, research/findings/grove-okrs-intent-architecture.md, research/findings/drucker-management-by-objectives-deep-dive.md, research/findings/bhag-sinek-synthesis.md
ingested: 2026-05-15
---

# Mission → Objectives → Projects → Tasks → Execution: The Five-Domain Chain

## The Claim

The concept of mission is not a metaphor. It is a structural pattern that recurs across every domain where purpose is delegated from one actor to another. This concept page maps the full chain: how intent travels from its origin (the Why) through organizational layers to the point of execution, and where it is most likely to be lost.

The five domains are not analogies. They are empirical experiments in solving the same problem: how to align action with intent when the actor is distant, numerous, and better informed about local conditions.

## The Chain: A Cross-Domain Map

| Layer | Religious | Military | NASA | Diplomacy | Business | Agent-Native |
|---|---|---|---|---|---|---|
| **Why** | Missio Dei | National Interest | Decadal Survey | National Interest | Mission Statement / Core Ideology | Context Stack Purpose |
| **Strategic Goal** | Evangelize the world | Defeat the enemy | Put a man on the moon | Secure alliance | BHAG ($125B by 2000) | Platform BHAG |
| **Mission** | Great Commission | Seize the bridge | Discovery Program mission | Embassy mandate | Business unit mission | GitHub Issue |
| **Objectives** | Per-region targets | OPORD Paragraph 2 | KDP commitments | Diplomatic objectives | OKRs / MBO | Key Results |
| **Projects** | Monastery, school | Battalion operation | Project (spacecraft build) | Negotiation round | Product roadmap | Plan of action |
| **Tasks** | Sermon, translation | Squad movement | Engineering task | Note verbale | Engineering ticket | Tool invocation |
| **Execution** | The act of preaching | The engagement | Launch and ops | The meeting | The shipped code | The tool output |

## The Handoff Points: Where Intent Lives or Dies

The chain has six transitions. Each is a potential failure point.

### Handoff 1: Why → Strategic Goal

**The question:** Does the strategic goal serve the Why, or has it already been corrupted?

- **Religious:** The Great Commission serves Missio Dei, but institutionalization (Stage 2) often subordinates divine purpose to organizational survival.
- **Military:** National interest is interpreted by politicians. The commander receives a mission that may or may not serve the true national interest.
- **NASA:** The Decadal Survey is peer-reviewed science, but Congress may fund programs that serve political constituencies rather than scientific priorities.
- **Business:** BHAGs often drift from product/innovation to financial targets. Boeing replaced "build the jet age" with "maximize shareholder value."
- **Agent:** The context stack's "purpose" field must be written by the human operator. If the operator writes a financial target instead of a user-centered purpose, the agent will optimize for the wrong thing.

**Preservation mechanism:** Intent restatement. The strategic goal must be written in fresh words that connect back to the Why, not copy-pasted.

### Handoff 2: Strategic Goal → Mission

**The question:** Is the mission a bounded expression of the strategic goal, or has it become disconnected?

- **Religious:** The missionary is sent to a specific region. The mandate must be specific enough to act on but broad enough to serve the global goal.
- **Military:** The OPORD Paragraph 2 must specify what must be achieved without prescribing how. "Seize the bridge to prevent reinforcement" serves the strategic goal. "Move along Route 34 at 0600" does not.
- **NASA:** The Program (Discovery) is the strategic goal; the Project (a specific spacecraft) is the mission. The PI must understand how their spacecraft serves the Decadal Survey.
- **Business:** The business unit mission must connect to the corporate BHAG. Without this connection, business units compete rather than collaborate.
- **Agent:** The GitHub Issue must carry the "Why" in its body. The `purpose` field is not optional.

**Preservation mechanism:** The Paragraph 2 Test. If the agent achieves the mission but misses the strategic goal, the mission was written wrong.

### Handoff 3: Mission → Objectives

**The question:** Do the objectives constrain outcome, or have they become task lists?

- **Religious:** Objectives like "establish 10 churches" are measurable but may not serve the mission of spiritual transformation.
- **Military:** KRs like "capture 500 prisoners" are measurable but may not serve the mission of degrading enemy capability.
- **NASA:** KDP commitments (cost, schedule, technical performance) are the OKRs. But they must be subordinate to scientific return.
- **Business:** OKRs like "reduce cart abandonment 20%" are good KRs. But they are not the mission. The mission is "make shopping effortless."
- **Agent:** The evaluation criteria must measure outcome, not activity. "Run the test suite" is an activity; "zero critical bugs in production" is an outcome.

**Preservation mechanism:** Outcome orientation. Every objective must be phrased as a result, not an activity. The verb matters.

### Handoff 4: Objectives → Projects

**The question:** Does the project design serve the objectives, or has the project become its own purpose?

- **Religious:** Building a cathedral is a project. But the project can become about the building rather than the worship.
- **Military:** The operation plan is the project. But plans are not for execution; they are for creating shared understanding.
- **NASA:** The spacecraft design is the project. But the PI must remember that the spacecraft is a means, not an end.
- **Business:** The product roadmap is the project. But product teams often fall in love with features rather than outcomes.
- **Agent:** The plan of action is the project. But the agent must be able to abandon the plan when the situation changes. This is disciplined initiative.

**Preservation mechanism:** Backbrief. Before execution, the subordinate presents their plan and explains how it serves the objective.

### Handoff 5: Projects → Tasks

**The question:** Do the tasks carry the intent of the project, or are they disconnected actions?

- **Religious:** Translating a scripture is a task. But the translator must understand the theological intent.
- **Military:** Moving a squad is a task. But the squad leader must understand how the movement serves the mission.
- **NASA:** Fabricating a component is a task. But the engineer must understand how the component serves the spacecraft's scientific purpose.
- **Business:** Writing code is a task. But the engineer must understand the user outcome.
- **Agent:** Invoking a tool is a task. But the agent must understand how the tool output serves the objective.

**Preservation mechanism:** Intent metadata. Every task must carry a link to the objective it serves. In Substrate, this is the `related:` field in the task description.

### Handoff 6: Tasks → Execution

**The question:** Does the execution preserve intent, or has it become rote?

- **Religious:** The sermon is delivered. But delivery without understanding is noise.
- **Military:** The engagement happens. But engagement without purpose is slaughter.
- **NASA:** The spacecraft launches. But launch without scientific return is an expensive fireworks display.
- **Business:** The code ships. But shipped code that does not serve the user is technical debt.
- **Agent:** The tool executes. But execution without understanding the objective is a wasted API call.

**Preservation mechanism:** Verification. The backbrief, the eval, the benchmark, the review. Was the intent achieved, or merely the task?

## The Cascade Problem: Entropy at Every Handoff

The cascade problem is not a failure of any single layer. It is the cumulative effect of entropy across all six handoffs. At each transition, some signal is lost. By the time execution occurs, the original intent may be entirely absent.

The cascade is silent. It does not announce itself. The individual contributor is not aware that their task once served a grand purpose. The agent is not aware that its tool invocation serves a human goal. The entropy is structural, not personal.

The military solution is the backbrief: the subordinate restates the mission in their own words before executing. The NASA solution is the KDP review: formal gates where intent is re-verified. The business solution is the OKR review: quarterly re-alignment. The religious solution is the retreat: periodic return to first principles.

For agent-native operations, the solution must be built into the infrastructure:
1. **Intent metadata in every task.** The `purpose` field in the Kanban task is not optional.
2. **Automatic backbrief.** The agent must summarize its plan and how it serves the objective before executing.
3. **Cascading intent restatement.** Every sub-task must restate the higher objective in fresh words.
4. **Stop-the-line authority.** The agent must be able to block when intent is unclear (`kanban_block`).
5. **Shared mental models.** The Substrate itself is the General Staff: every agent reads the same knowledge base.

## The Five-Domain Synthesis

| Domain | Primary Mechanism | Key Handoff Risk | Preservation Tool |
|---|---|---|---|
| Religious | Divine mandate → institutional mission | Institutionalization subordinates purpose to survival | Retreat, renewal, Missio Dei theology |
| Military | Commander's intent → OPORD → engagement | Cascade through echelons degrades intent | Backbrief, Paragraph 2 Test, shared training |
| NASA | Decadal Survey → Program → Project → Mission | Political interference in scientific priorities | Peer review, KDP gates, PI autonomy |
| Diplomacy | Mandate → embassy → negotiation | Secrecy isolates negotiators from national interest | Reporting, recall, institutional memory |
| Business | Mission → BHAG → OKR → task → execution | Financial targets replace product/innovation intent | Quarterly review, culture, leadership |
| Agent | Purpose → objective → plan → tool → output | Orchestrator compresses intent in decomposition | Context stack, backbrief, shared substrate |

## The Structural Insight

The same pattern recurs because it is the optimal response to the same structural condition: the principal cannot specify the optimal method because the principal does not know the local conditions. The agent knows more but needs alignment. The solution is an incomplete contract (mission, objective, task) plus a cultural and technical substrate that fills the gaps.

This is why the concept is not metaphorical. It is not that business "borrows" from military mission or that NASA "adapts" religious sending. It is that all five domains face the same problem: how to delegate purpose without destroying initiative. The solution converges because the problem is invariant.

For Substrate, the implication is direct: the agent-native operating system must implement all six handoffs explicitly. Not as optional metadata, but as required fields. The `purpose` field is the Why. The objective is the BHAG. The task is the mission. The tool is the execution. And the backbrief is the verification that intent has survived.

The chain is not a theory. It is a checklist. Every task must carry the full chain, or the chain will break.
