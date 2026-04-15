# Paperclip is an OS for autonomous agent companies

**Source:** research/paperclip/analysis.md
**Date:** 2026-03-09

Paperclip is a control plane for AI agent companies. It does not build agents, run agents, or provide an agent framework. It provides the organizational infrastructure layer that sits above individual agents: structure, accountability, and coordination.

**Core value proposition:** If you have multiple AI agents (OpenClaw instances, Claude Code sessions, Codex, Cursor, custom bots), Paperclip gives them an org chart, task management, budget enforcement, goal alignment, and governance.

**The metaphor:** "If OpenClaw is an employee, Paperclip is the company."

**Problem it solves:** People running 10+ simultaneous agent sessions lose track of what each agent is doing, spend money uncontrollably, have no audit trail, and manually coordinate context between agents.

**What it is NOT:** Not an agent framework. Not a workflow builder. Not a chatbot. Not a prompt manager. Not a single agent tool.

**Tech stack:** Node.js + Express, React + Vite, PostgreSQL via Drizzle ORM, embedded PGlite for zero config local dev. MIT licensed. `npx paperclipai onboard --yes` gets you running.

See also:
- [[paperclip-atomic-task-checkout-prevents-agent-collisions]]
- [[paperclip-patterns-worth-adopting-for-synthweave]]
- [[zero-human-company-framing-oversells-autonomy]]
