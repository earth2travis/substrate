---
title: Origins and Evolution of Project Management and Issue Tracking
tags:
- project-management
- history
- kanban
- agile
- lean
- waterfall
- github
related:
- kanban-doctrine
- toyota-production-system
- lean-doctrine
- pdca-cycle
- value-stream-mapping
- five-whys
- fishbone-diagrams
- a3-thinking
source: Capstone research, completed 2026-02-28
---




# Origins and Evolution of Project Management and Issue Tracking

## Part I: Project Management as a Discipline

### The Pre-Modern Era

Project management is as old as civilization. The Great Pyramid of Giza (2560 BCE), Roman aqueducts, the Great Wall of China: all required coordination of thousands of workers across years. But these projects were managed through hierarchy, tradition, and direct observation. There was no methodology. There was a pharaoh, a master builder, and a very large stick.

The transition to modern project management begins with industrialization. Frederick Winslow Taylor published "The Principles of Scientific Management" in 1911, arguing that work could be studied, measured, and optimized. Taylor was deeply flawed (his methods dehumanized workers, his data was sometimes fabricated), but his core insight survived: work is a system, and systems can be improved through observation and analysis.

### Henry Gantt and the Visual Revolution (1910s)

Henry Laurence Gantt created the Gantt chart around 1910 to 1915. The innovation: a horizontal bar chart showing tasks plotted against time. For the first time, a project manager could see at a glance which tasks were in progress, which were complete, and how they related to the overall timeline.

The Gantt chart was first used extensively on the Hoover Dam project (started 1931) and in World War I planning. Over a century later, virtually every project management tool offers Gantt chart views. The reason is fundamental: humans are visual thinkers, and a visual representation of work over time maps naturally to how we understand progress.

### PERT, CPM, and the Cold War Era (1950s to 1960s)

Critical Path Method (CPM): developed in 1957 by Morgan Walker of DuPont and James Kelley of Remington Rand. CPM models a project as a network of tasks with dependencies and durations. The "critical path" is the longest sequence of dependent tasks, determining minimum project duration.

Program Evaluation and Review Technique (PERT): developed in 1958 by the U.S. Navy Special Projects Office for the Polaris submarine missile program. PERT added probabilistic estimation (optimistic, most likely, pessimistic durations) to network scheduling.

Both techniques required significant computational effort. First applications used mainframe computers, limiting adoption to large government and defense projects. A recurring pattern: new PM techniques emerge in large, high-stakes contexts and diffuse to smaller organizations as technology makes them accessible.

The Project Management Institute (PMI) was founded in 1969, formalizing project management as a profession.

### Waterfall: The Misunderstood Model (1970)

Winston Royce published "Managing the Development of Large Software Systems" in 1970. The paper described a sequential development process. Ironically, Royce presented this sequential model as flawed and advocated for iterative feedback loops. But the industry extracted the sequential diagram and named it "Waterfall," turning it into dogma for three decades.

Waterfall dominated software development from the 1970s through the 1990s. Its appeal was organizational: it mapped neatly onto existing bureaucratic structures. It worked tolerably well for projects with stable, well-understood requirements. It failed catastrophically for projects with high uncertainty, which describes most software.

A methodology's survival often depends more on organizational compatibility than on effectiveness.

### The Toyota Production System and Lean (1940s to 1990s)

While Western project management built ever more elaborate planning frameworks, Toyota developed something fundamentally different.

Taiichi Ohno and Eiji Toyoda built the Toyota Production System between the late 1940s and the 1970s. Core principles: eliminate waste (muda), just in time (produce only what is needed when it is needed), jidoka (build quality in at the source, stop the line when defects detected), continuous improvement (kaizen), respect for people.

Kanban emerged from TPS in the late 1940s. Ohno was inspired by American supermarket shelving: items are pulled from shelves as needed, restocking happens based on actual consumption. He translated this into a card system for manufacturing. Work was pulled through the system rather than pushed.

The intellectual lineage connects directly: PDCA is the improvement engine within TPS. Value stream mapping is the diagnostic tool. 5 Whys is the root cause analysis method. Fishbone diagrams support systematic problem identification. A3 thinking is the structured problem solving format.

TPS was translated to Western audiences through "The Machine That Changed the World" (Womack, Jones, Roos, 1990), "Lean Thinking" (Womack and Jones, 1996), and "The Toyota Way" (Liker, 2004).

David Anderson adapted kanban for software development in the mid-2000s, publishing "Kanban: Successful Evolutionary Change for Your Technology Business" in 2010.

### The Agile Revolution (1990s to 2001)

The 1990s saw an explosion of lightweight methodologies reacting against Waterfall's rigidity: Scrum (1995, Jeff Sutherland and Ken Schwaber), Extreme Programming (1996, Kent Beck), Crystal (1991, Alistair Cockburn), Rapid Application Development (1991, James Martin), Feature Driven Development (1997, Jeff De Luca).

On February 11 to 13, 2001, seventeen software developers met at Snowbird, Utah. They produced the Agile Manifesto: individuals and interactions over processes and tools; working software over comprehensive documentation; customer collaboration over contract negotiation; responding to change over following a plan.

Agile is not a methodology. It is a set of values with twelve supporting principles.

What followed was both triumph and corruption. Agile became mainstream, then corporate, then commodified. "Agile transformations" became a consulting industry. Many organizations adopted Agile vocabulary without Agile values, running "sprints" that were just two-week waterfalls.

### Shape Up and Post-Agile (2010s to Present)

Basecamp published "Shape Up" in 2019 by Ryan Singer. Six week cycles instead of two week sprints. Shaping before building: senior people define rough boundaries before handing off to a team. Appetite, not estimates: instead of asking "how long will this take?" ask "how much time is this worth?" No backlogs: if something is important, it will come back. Circuit breaker: if work is not done at the end of a cycle, it does not automatically continue.

Other modern approaches: SAFe (Scaled Agile Framework), widely adopted and widely criticized for reintroducing bureaucracy; Basecamp's "Calm" philosophy rejecting artificial urgency; NoEstimates movement questioning whether effort estimation provides value proportional to cost; Continuous delivery and DevOps collapsing the boundary between development and operations.

## Part II: The Evolution of Issue Tracking

### Physical Origins (1940s to 1970s)

Before digital issue tracking: index cards and card files (physical cards organized in boxes, each representing a task or defect); bug books (literal notebooks where testers logged defects, the term "bug" predates computers, used since the 1870s); punch card systems; paper forms and carbon copies.

The physical constraint forced locality and natural WIP limits.

### Early Digital Systems (1980s to 1990s)

GNATS (1992): GNU's bug tracking system, text-based, email-driven, minimalist.

Bugzilla (1998): created by Terry Weissman for Mozilla. Built on MySQL with web interface. Introduced concepts now taken for granted: severity and priority fields, component categorization, status workflows, CC lists, dependencies, full-text search. Ugly, powerful, and free.

### The Enterprise Era (2000s)

JIRA (2002): Atlassian launched as a bug tracker, evolved into a comprehensive project management platform. JIRA's genius and curse was configurability: you could model any workflow, which meant every organization modeled a different workflow, which meant nobody could transfer JIRA knowledge between jobs.

Trac (2003): integrated wiki and issue tracker, lightweight, developer-friendly.

Redmine (2006): open source, Rails-based, inspired by Trac but more feature-rich.

FogBugz (2000): Joel Spolsky's Fog Creek Software. Notable for "Evidence Based Scheduling," using historical data to improve estimates.

### The Modern Era (2010s to Present)

GitHub Issues (2009): radically simpler than JIRA. Issues are markdown documents with labels, milestones, and assignees. Key insight: put issue tracking where the code already lives. Developers do not context switch.

Trello (2011): kanban boards for everyone, drag and drop simplicity. Acquired by Atlassian in 2017.

Asana (2008/2011): task management for teams, founded by Facebook co-founder Dustin Moskovitz.

Linear (2019): built by former Uber engineers. Keyboard-driven, fast, opinionated. Rejected JIRA's configurability in favor of strong defaults.

GitHub Projects V2 (2022): custom fields, multiple views (table, board, roadmap), automations, iterations. Closing the gap with JIRA while maintaining GitHub's integration advantage.

### The Sub-issues Evolution (2025)

In January 2025, GitHub released sub-issues in public preview, GA in April 2025. GitHub Issues was historically flat. Sub-issues introduced parent-child hierarchies, allowing work breakdown structures within the issue system. Combined with issue types, this moved GitHub closer to a full project management platform.

## Part III: Patterns That Survived and Why

### Survivors

1. Visual representation of work. Gantt charts (1910s), kanban boards (1940s), burn charts (2000s), roadmap views (2020s). The medium changes. The need to see work does not.
2. Iterative cycles. PDCA (1920s/1950s), spiral model (1986), Scrum sprints (1995), Shape Up cycles (2019). Every successful methodology includes plan, execute, reflect, adjust.
3. Work breakdown. WBS (1960s), user stories (1990s), sub-issues (2025). Breaking large work into smaller pieces is universal.
4. Pull over push. Kanban (1940s), just in time (1950s), pull requests (2008). Systems that let downstream demand trigger upstream work outperform systems that push work regardless of capacity.
5. Retrospection. After-action reviews (military), retrospectives (Scrum), hansei (Toyota), postmortems (SRE). Looking back to improve is foundational.
6. Making constraints visible. Critical path (1957), WIP limits (kanban), circuit breakers (Shape Up). Explicitly identifying and managing constraints beats ignoring them.

### Discarded or Diminished

1. Comprehensive upfront planning. Waterfall's detailed requirements phase. Failed because it assumed stable requirements in unstable domains.
2. Heavyweight process documentation. CMMI level 5 process libraries. Cost of maintaining documentation exceeded its value.
3. Deterministic scheduling. PERT's probabilistic approach acknowledged uncertainty, but many implementations collapsed back to single-point estimates.
4. Centralized command and control. The project manager as omniscient planner. Replaced by self-organizing teams and distributed decision making.
5. Phase gates and sign-offs. Sequential approval processes that create bottlenecks. Replaced by automated quality gates in continuous delivery.

## Part IV: What the Best Project Managers Know

### Tacit Knowledge of Expert PMs

1. The plan is not the point. Planning is the point. The value is in the thinking it forces, not in the document it produces.
2. Most delays come from queues, not tasks. A task might take two hours of work but sit in someone's queue for two weeks. Expert PMs obsess over wait times, handoffs, and context switches.
3. Work in progress is the enemy. Every open task is a commitment of attention. WIP limits are not about laziness; they are about throughput. Little's Law (L equals lambda W) proves this mathematically.
4. Communication is the actual work. The PM's job is not to manage tasks. It is to manage information flow.
5. Scope is the only lever that matters. You cannot add people to a late project (Brooks' Law). Expert PMs negotiate scope constantly and explicitly.
6. The system produces the outcomes. Individual heroism is a symptom of system failure. If you need heroics to ship, your process is broken.
7. Psychological safety enables velocity. Teams that can admit mistakes and raise concerns without fear move faster.
8. Feedback loops must be short. The longer the delay between action and feedback, the more waste accumulates.

### What Most AI Agents Miss

1. Context that is not in the ticket. Political dynamics, technical debt, team member overwhelm.
2. When to not create an issue. Not every thought deserves a ticket. Issue inflation creates noise that obscures signal.
3. The difference between busy and productive. An AI can create, update, and close issues at inhuman speed. But activity is not progress.
4. When to break the process. Processes exist to serve the work. When the process impedes the work, an expert PM deviates.
5. Emotional labor. Managing a project is managing people. Frustration, motivation, burnout, excitement: real forces that affect velocity.
