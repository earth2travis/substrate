# Nex AI Brainstorm: Team Agent on OpenClaw

_February 19, 2026. Synthweave team session._

## Context

Synthweave attended an OpenClaw hackathon, then spent a week hacking on "Nex," a team PM agent running OpenClaw on Render (Docker). This session brought the full team together to brainstorm capabilities.

## Attendees

Le, Alexey, Mak, Andrei, Micah Parker, Emiliano Villarreal, Travis

## The Core Problem

OpenClaw is deeply single player. Built for one human, one agent. Synthweave is hacking around this by treating the company as the "single user" and team members as "employees." Works well enough to be mind blowing, but it's a hack that breaks in predictable ways:

- Memory is per user, not per team member
- MCP access goes through one user's permissions (Travis's), causing access issues
- Can't read DMs between team members
- No per person notification preferences
- Heartbeat is global, not per individual

## Infrastructure (Current State)

- Running on Render in Docker (not ideal, OpenClaw wasn't designed for Docker)
- Homebrew installed in persistent storage for tool access
- Connected to Synthweave (via MCP) and GitHub (own user: Synthweave Next)
- Heartbeat runs every 30 minutes
- If container rebuilds, requires manual script to rewire folders

## What Each Person Wants

### Mak: Standup assistance
- Ask 1 to 5 minute questions about daily work
- Connect with channel messages for context
- Generate weekly team reports on blockers and milestones
- Reminder to update when he forgets (works late nights)

### Travis: Celebration and visibility
- Share completed work so he can recognize and celebrate people
- Not surveillance. Recognition.

### Andrei: Product feedback tracking
- Track user needs, improvement suggestions, ideas from conversations
- DM notifications 30 min morning/afternoon, leave day free
- Capture ideas when trigger phrases appear ("we should," "wouldn't it be cool if")

### Emiliano: Project progress tracking
- Show progress on objectives (36 tasks, 17 done, next priorities)
- Weekly congratulations on completed work
- Milestone tracking against goals

### Alexey: Enhanced PR notifications
- Real time notifications when assigned as reviewer (not when PR opens)
- Sync PRs with GitHub issues automatically
- Custom notification subscriptions per issue/PR
- Short summaries with links (click for details, don't read everything)

### Le: Memory and personalization
- Individual agent per team member with custom instructions
- Persistent memory using files or memory services
- Teach Nex to behave differently per person
- Use Synthweave snips as memory/knowledge store

### Micah: Automated ticket management
- Auto move tickets to "done" when merging dev to main
- Multiplayer coding in Slack threads with PR generation
- Reduce ticket management overhead

## Key Technical Decisions

1. **Daily check in format:** Shift to be more PR focused
2. **PR hooks:** Implement reviewer notification hooks
3. **Storage:** Use Synthweave bases instead of local files for Nex's knowledge
4. **"Nex OS" base:** Create a Synthweave base as the interface/command center
5. **Heartbeat source:** Pull heartbeat checklist from Synthweave base
6. **Notification model:** Test heartbeat polling (30 min) vs real time hooks

## Three Big Insights

### 1. OpenClaw is not multiplayer
The fundamental architecture assumes one human. Everything from memory to permissions to notification preferences needs rethinking for teams. This is the gap MultiClaw could fill.

### 2. Synthweave snips as agent memory
Instead of local markdown files, use Synthweave bases as the knowledge layer. This gives team visibility, collaborative editing, and a path toward "git for context files" (versioning, merge controls on important agent instructions).

### 3. Multi agent dashboard as hosted service
Think about Nex not as a personal assistant but as a hosted service. Each team member could have their own agent. The business is the brain; agents are the hands. Synthweave becomes the substrate that connects them.

## Unsolved Problems

- How to give per person preferences in a single player system
- TipTap to markdown conversion (could be a blocker for Synthweave as file store)
- Permission model: MCP access through one user's credentials
- Balancing push vs pull notifications (maker mode, attention aperture)
- Git version control for important context files

## Next Steps (from meeting)

- [ ] Format daily summaries to focus on PRs and engineering board
- [ ] Set up PR notification hooks for reviewer assignments
- [ ] Create Synthweave base structure for Nex's file storage
- [ ] Test notification preferences and automation features
- [ ] Implement ticket sync between PRs and GitHub issues
- [ ] Explore "Nex OS" base as heartbeat instruction source

## Quotable

Emiliano: "Our build velocity is starting to get really fast and really impressive... but visibility and alignment around priorities and backlog states, that stuff is falling behind."

Micah: "OpenClaw is deeply single player. It was built to service one person."

Le: "We may just want to have one single agent per team member and each team member has their own instruction."

Emiliano: "If we're trying to make this a team player tool, then we need it to be the business brain, the source of truth that is going off and passing instructions to other agents."
