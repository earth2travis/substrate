---
title: Origins and Evolution of Project Management and Issue Tracking
tags:
  - research
  - project-management
  - history
related:
  - [[2026-02-10-ai-career-convergence]]
  - [[5-whys]]
  - [[actual-occasions]]
  - [[alfred-north-whitehead]]
source: research/raw/origins-and-evolution.md
---

# Origins and Evolution of Project Management and Issue Tracking

_Research completed 2026-02-28. Related: issue #302. Capstone research for Foundation project._

## Part I: Project Management as a Discipline

### The Pre-Modern Era (Ancient Times to 1900s)

Project management is as old as civilization. The Great Pyramid of Giza (2560 BCE), the Roman aqueducts, the Great Wall of China: all required coordination of thousands of workers across years of effort. But these projects were managed through hierarchy, tradition, and direct observation. There was no methodology. There was a pharaoh, a master builder, and a very large stick.

The transition to modern project management begins with industrialization. Frederick Winslow Taylor published _The Principles of Scientific Management_ in 1911, arguing that work could be studied, measured, and optimized. Taylor was deeply flawed (his methods dehumanized workers, his data was sometimes fabricated), but his core insight survived: work is a system, and systems can be improved through observation and analysis. This is the same root that feeds PDCA, value stream mapping, and everything we have already studied.

### Henry Gantt and the Visual Revolution (1910s)

Henry Laurence Gantt, a mechanical engineer and management consultant who had worked with Taylor, created the Gantt chart around 1910 to 1915. The innovation was deceptively simple: a horizontal bar chart showing tasks plotted against time. For the first time, a project manager could see at a glance which tasks were in progress, which were complete, and how they related to the overall timeline.

The Gantt chart was first used extensively on the Hoover Dam project (started 1931) and in World War I planning. Its staying power is remarkable. Over a century later, virtually every project management tool offers Gantt chart views. The reason is fundamental: humans are visual thinkers, and a visual representation of work over time maps naturally to how we understand progress. This pattern, making the invisible visible, recurs throughout the entire history. It is the same principle that drives kanban boards, burndown charts, and value stream maps.

### PERT, CPM, and the Cold War Era (1950s to 1960s)

The 1950s produced the two techniques that most historians consider the birth of modern project management:

**Critical Path Method (CPM):** Developed in 1957 by Morgan Walker of DuPont and James Kelley of Remington Rand. CPM models a project as a network of tasks with dependencies and durations. The "critical path" is the longest sequence of dependent tasks, which determines the minimum project duration. Any delay on the critical path delays the entire project. This was revolutionary because it formalized something experienced project managers knew intuitively: not all tasks are equally important to the schedule.

**Program Evaluation and Review Technique (PERT):** Developed in 1958 by the U.S. Navy Special Projects Office for the Polaris submarine missile program. PERT added probabilistic estimation (optimistic, most likely, pessimistic durations) to network scheduling. Where CPM assumed deterministic durations, PERT acknowledged uncertainty. The Polaris project involved 3,000 contractors and 9,000 subcontractors. PERT helped coordinate this complexity.

Both techniques required significant computational effort. The first applications used mainframe computers, which limited adoption to large government and defense projects. This is a recurring pattern: new PM techniques emerge in large, high stakes contexts and then diffuse to smaller organizations as technology makes them accessible.

The Project Management Institute (PMI) was founded in 1969, formalizing project management as a profession. The International Project Management Association (IPMA) had been founded in Europe in 1965. Project management was no longer an ad hoc skill. It was becoming a discipline with its own body of knowledge, certifications, and career paths.

### Waterfall: The Misunderstood Model (1970)

Winston Royce published "Managing the Development of Large Software Systems" in 1970. The paper described a sequential development process: requirements, design, implementation, verification, maintenance. Ironically, Royce presented this sequential model as flawed. He advocated for iterative feedback loops. But the industry extracted the sequential diagram and named it "Waterfall," turning it into dogma for three decades.

The Waterfall model dominated software development from the 1970s through the 1990s. Its appeal was organizational: it mapped neatly onto existing bureaucratic structures. Requirements go up the chain, approvals come down, development proceeds in orderly phases. It worked tolerably well for projects with stable, well understood requirements (bridge construction, regulatory compliance systems). It failed catastrophically for projects with high uncertainty, which describes most software.

The lesson: a methodology's survival often depends more on organizational compatibility than on effectiveness. Waterfall persisted not because it worked well for software, but because it was legible to the management structures that funded software projects.

### The Toyota Production System and Lean (1940s to 1990s)

While Western project management was building ever more elaborate planning frameworks, Toyota was developing something fundamentally different.

Taiichi Ohno and Eiji Toyoda built the Toyota Production System (TPS) between the late 1940s and the 1970s. Its core principles:

1. **Eliminate waste (muda).** Any activity that does not add value from the customer's perspective is waste. Seven categories: overproduction, waiting, transportation, overprocessing, inventory, motion, defects.

2. **Just in time.** Produce only what is needed, when it is needed, in the amount needed. This inverts the Western batch and queue approach.

3. **Jidoka (automation with a human touch).** Build quality in at the source. Stop the line when a defect is detected. Do not pass problems downstream.

4. **Continuous improvement (kaizen).** Small, incremental improvements, every day, by everyone. Not periodic big bang transformations.

5. **Respect for people.** The workers closest to the work understand it best. Management's job is to create conditions for improvement, not to dictate solutions.

**Kanban** emerged from TPS in the late 1940s. Ohno was inspired by American supermarket shelving systems: items are pulled from shelves as needed, and restocking happens based on actual consumption, not forecasts. He translated this into a card (kanban means "visual signal" or "card" in Japanese) system for manufacturing. Each card authorized production of a specific quantity. Work was pulled through the system rather than pushed.

The intellectual lineage connects directly to our existing research:

- **PDCA** (see research/pdca-cycle.md) is the improvement engine within TPS
- **Value stream mapping** (see research/value-stream-mapping/) is the diagnostic tool
- **5 Whys** (see research/5-whys/) is the root cause analysis method
- **Fishbone diagrams** (see research/fishbone-diagrams.md) support systematic problem identification
- **A3 thinking** (see research/a3-thinking/) is the structured problem solving format

TPS was translated to Western audiences through several key texts:

- _The Machine That Changed the World_ (Womack, Jones, Roos, 1990): introduced "lean production" as a term
- _Lean Thinking_ (Womack and Jones, 1996): generalized lean principles beyond manufacturing
- _The Toyota Way_ (Liker, 2004): 14 management principles distilled from TPS

David Anderson adapted kanban for software development in the mid 2000s, publishing _Kanban: Successful Evolutionary Change for Your Technology Business_ in 2010. Software kanban differs from manufacturing kanban: the cards represent work items (features, bugs, tasks) rather than physical parts, and the board visualizes workflow stages rather than physical locations.

### The Agile Revolution (1990s to 2001)

The 1990s saw an explosion of "lightweight" methodologies, all reacting against Waterfall's rigidity:

- **Scrum** (1995): Jeff Sutherland and Ken Schwaber, inspired by a 1986 Harvard Business Review paper by Takeuchi and Nonaka that compared high performing product teams to rugby scrums. Fixed length sprints, daily standups, retrospectives.
- **Extreme Programming (XP)** (1996): Kent Beck. Pair programming, test driven development, continuous integration, short iterations.
- **Crystal** (1991): Alistair Cockburn. A family of methodologies scaled by project size and criticality.
- **Rapid Application Development (RAD)** (1991): James Martin. Prototyping and iterative development.
- **Feature Driven Development (FDD)** (1997): Jeff De Luca. Feature centric iterative development.

On February 11 to 13, 2001, seventeen software developers met at the Lodge at Snowbird ski resort in Utah. They represented different lightweight methodologies but shared common frustrations with heavyweight processes. They produced the Agile Manifesto:

> We are uncovering better ways of developing software by doing it and helping others do it. Through this work we have come to value:
>
> Individuals and interactions over processes and tools
> Working software over comprehensive documentation
> Customer collaboration over contract negotiation
> Responding to change over following a plan

The manifesto was intentionally brief and value oriented rather than prescriptive. It united disparate approaches under a shared philosophy. Agile is not a methodology. It is a set of values with twelve supporting principles.

What followed was both triumph and corruption. Agile became mainstream, then corporate, then commodified. "Agile transformations" became a consulting industry. Certifications proliferated. Many organizations adopted Agile vocabulary without Agile values, running "sprints" that were just two week waterfalls. The Agile Industrial Complex emerged, selling the thing that was supposed to be the alternative to buying things.

### Shape Up and Post-Agile (2010s to Present)

Basecamp (formerly 37signals) published _Shape Up_ in 2019, authored by Ryan Singer. It represented a reaction against Scrum's ritual density:

- **Six week cycles** instead of two week sprints. Long enough to build something meaningful, short enough to maintain urgency.
- **Shaping** before building: senior people define the rough boundaries and solution approach before handing off to a team.
- **Appetite, not estimates.** Instead of asking "how long will this take?" ask "how much time is this worth?"
- **No backlogs.** If something is important, it will come back. The backlog is a guilt pile that creates fake obligations.
- **Circuit breaker.** If work is not done at the end of a cycle, it does not automatically continue. The default is to stop and reassess.

Shape Up is notable for our context because it explicitly addresses the problem of scope creep and the false precision of estimation, both of which are magnified in a human plus AI workflow where the AI can generate work faster than the human can evaluate it.

Other modern approaches worth noting:

- **SAFe (Scaled Agile Framework):** Enterprise scaling of Agile. Widely adopted, widely criticized for reintroducing the bureaucracy Agile was designed to eliminate.
- **Basecamp's "Calm" philosophy:** Rejecting artificial urgency. Sustainable pace.
- **NoEstimates movement:** Questioning whether effort estimation provides value proportional to its cost.
- **Continuous delivery / DevOps:** Collapsing the boundary between development and operations. Ship small, ship often.

## Part II: The Evolution of Issue Tracking

### Physical Origins (1940s to 1970s)

Before digital issue tracking, there were:

- **Index cards and card files.** Physical cards organized in boxes or on boards. Each card represented a task or defect. The kanban board is a direct descendant.
- **Bug books.** Literal notebooks where testers logged defects. The term "bug" predates computers (Grace Hopper's famous moth was documented in 1947, but engineers used "bug" for technical problems as early as the 1870s).
- **Punch card systems.** IBM and others used punch cards for task tracking in large projects through the 1960s.
- **Paper forms and carbon copies.** Formal defect reports distributed through office mail.

The physical constraint was significant: a paper based system forces locality. The card is in one place. You have to physically go look at the board. This created natural work in progress limits (you can only pin so many cards) and made status radiators inherently visible.

### Early Digital Systems (1980s to 1990s)

- **GNATS (1992):** GNU's bug tracking system. Text based, email driven. Minimalist to the point of hostility.
- **SCCS, RCS, CVS:** Version control systems that included rudimentary change tracking, not full issue trackers but part of the ecosystem.
- **Bugzilla (1998):** Created by Terry Weissman for the Mozilla project after Netscape open sourced its codebase. Built on a MySQL backend with a web interface. Bugzilla introduced many concepts we now take for granted: severity and priority fields, component categorization, status workflows (NEW, ASSIGNED, RESOLVED, VERIFIED, CLOSED), CC lists, dependencies, and full text search. It was ugly, powerful, and free. Many open source projects still use it today.

### The Enterprise Era (2000s)

- **JIRA (2002):** Atlassian launched JIRA (named after Gojira, the Japanese name for Godzilla) as a bug tracker. It evolved into a comprehensive project management platform. JIRA's genius and curse was configurability: you could model any workflow, which meant every organization modeled a different workflow, which meant nobody could transfer their JIRA knowledge between jobs. JIRA became synonymous with enterprise Agile, for better and worse.
- **Trac (2003):** Integrated wiki and issue tracker for software projects. Lightweight, developer friendly.
- **Redmine (2006):** Open source, Rails based, inspired by Trac but more feature rich.
- **FogBugz (2000):** Joel Spolsky's Fog Creek Software. Notable for "Evidence Based Scheduling," which used historical data to improve estimates.

### The Modern Era (2010s to Present)

- **GitHub Issues (2009):** Launched as part of GitHub's platform. Radically simpler than JIRA. Issues are markdown documents with labels, milestones, and assignees. The key insight: put issue tracking where the code already lives. Developers do not context switch. The issue is next to the pull request is next to the code review. This integration advantage has been GitHub Issues' primary moat.
- **Trello (2011):** Kanban boards for everyone. Drag and drop simplicity. Acquired by Atlassian in 2017.
- **Asana (2008/2011):** Task management for teams. Founded by Facebook co-founder Dustin Moskovitz.
- **Linear (2019):** Built by former Uber engineers. Keyboard driven, fast, opinionated. Linear rejected JIRA's configurability in favor of strong defaults. Their thesis: the best tool is the one that works well out of the box, not the one that can be configured to work well.
- **GitHub Projects V2 (2022):** GitHub's response to the "GitHub Issues is too simple" criticism. Custom fields, multiple views (table, board, roadmap), automations, iterations. Closing the gap with JIRA while maintaining GitHub's integration advantage.

### The Sub-issues Evolution (2025)

In January 2025, GitHub released sub-issues in public preview, reaching GA in April 2025. This was a significant shift: GitHub Issues was historically flat. Every issue was a peer. Sub-issues introduced parent-child hierarchies, allowing work breakdown structures within the issue system. Combined with issue types (bug, task, initiative), this moved GitHub closer to a full project management platform.

## Part III: Patterns That Survived and Why

### Survivors

1. **Visual representation of work.** Gantt charts (1910s), kanban boards (1940s), burn charts (2000s), roadmap views (2020s). The medium changes. The need to see work does not.

2. **Iterative cycles.** PDCA (1920s/1950s), spiral model (1986), Scrum sprints (1995), Shape Up cycles (2019). Every successful methodology includes some form of plan, execute, reflect, adjust.

3. **Work breakdown.** WBS (1960s), user stories (1990s), sub-issues (2025). Breaking large work into smaller pieces is universal. The granularity and formalism vary, but the principle persists.

4. **Pull over push.** Kanban (1940s), just in time (1950s), pull requests (2008). Systems that let downstream demand trigger upstream work outperform systems that push work regardless of capacity.

5. **Retrospection.** After action reviews (military), retrospectives (Scrum), hansei (Toyota), postmortems (SRE). Looking back to improve is foundational.

6. **Making constraints visible.** Critical path (1957), WIP limits (kanban), circuit breakers (Shape Up). Explicitly identifying and managing constraints beats ignoring them.

### Discarded or Diminished

1. **Comprehensive upfront planning.** Waterfall's detailed requirements phase. Failed because it assumed stable requirements in unstable domains. Survived only in regulated industries where requirements genuinely are stable (construction, aerospace, pharma).

2. **Heavyweight process documentation.** CMMI level 5 process libraries. The cost of maintaining documentation exceeded its value. Replaced by lightweight conventions and automation.

3. **Deterministic scheduling.** PERT's probabilistic approach acknowledged uncertainty, but many implementations collapsed back to single point estimates. The NoEstimates movement is the latest pushback.

4. **Centralized command and control.** The project manager as omniscient planner. Replaced by self organizing teams, distributed decision making, and servant leadership.

5. **Phase gates and sign offs.** Sequential approval processes that create bottlenecks. Continuous delivery replaced them with automated quality gates.

## Part IV: What the Best Project Managers Know

### Tacit Knowledge of Expert PMs

Research from PMI on tacit knowledge in projects and from practitioners in the field reveals patterns that are not in any textbook:

1. **The plan is not the point. Planning is the point.** Eisenhower's formulation. The value of a plan is in the thinking it forces, not in the document it produces. Expert PMs know their plans will change. They plan anyway because the act reveals risks, dependencies, and assumptions.

2. **Most delays come from queues, not tasks.** A task might take two hours of work but sit in someone's queue for two weeks. Expert PMs obsess over wait times, handoffs, and context switches, not just execution speed. This connects directly to value stream mapping: the ratio of value added time to total lead time.

3. **Work in progress is the enemy.** Every open task is a commitment of attention. Too many open tasks means nothing gets finished. WIP limits are not about laziness. They are about throughput. Little's Law (L = λW) proves this mathematically: reducing work in progress reduces lead time.

4. **Communication is the actual work.** The PM's job is not to manage tasks. It is to manage information flow. Who needs to know what, when? What decisions are blocked on missing information? What assumptions are different people making?

5. **Scope is the only lever that matters.** You cannot add people to a late project (Brooks' Law). You cannot compress time without cutting scope or quality. Expert PMs negotiate scope constantly and explicitly, rather than letting it creep implicitly.

6. **The system produces the outcomes.** Individual heroism is a symptom of system failure. If you need heroics to ship, your process is broken. Deming taught this. Most organizations still have not learned it.

7. **Psychological safety enables velocity.** Teams that can admit mistakes, raise concerns, and challenge assumptions without fear move faster than teams that cannot. This is not soft. It is structural.

8. **Feedback loops must be short.** The longer the delay between action and feedback, the more waste accumulates. Daily standups, continuous integration, automated tests, short iterations: all reduce feedback delay.

### What Most AI Agents Miss

1. **Context that is not in the ticket.** The political dynamics behind a feature request. The technical debt that makes an estimate unreliable. The team member who is quietly overwhelmed. An AI PM that only reads issues misses the human substrate.

2. **When to not create an issue.** Not every thought deserves a ticket. Issue inflation creates noise that obscures signal. Expert PMs curate their backlog ruthlessly.

3. **The difference between busy and productive.** An AI can create, update, and close issues at inhuman speed. But activity is not progress. The question is always: did we ship something that mattered?

4. **When to break the process.** Processes exist to serve the work. When the process is impeding the work, an expert PM deviates. An AI trained on process compliance may struggle with this judgment.

5. **Emotional labor.** Managing a project is managing people. Frustration, motivation, burnout, excitement: these are real forces that affect velocity. An AI PM must at least recognize these forces exist, even if it cannot feel them.

## Connections to Our System

Our existing research forms a coherent body of knowledge rooted in the lean/TPS tradition:

| Our Research         | Historical Root                             | Function                   |
| -------------------- | ------------------------------------------- | -------------------------- |
| PDCA cycle           | Shewhart (1920s), Deming/Japan (1950s)      | Improvement engine         |
| Value stream mapping | Toyota TPS (1940s-70s), Rother/Shook (1999) | Diagnostic tool            |
| 5 Whys               | Sakichi Toyoda, TPS                         | Root cause analysis        |
| Fishbone diagrams    | Kaoru Ishikawa (1960s)                      | Problem decomposition      |
| A3 thinking          | Toyota, TPS                                 | Structured problem solving |
| GitHub PM guide      | Our synthesis                               | Implementation             |

This capstone research adds the historical context that connects these tools to the broader evolution of the discipline. We are not randomly selecting methodologies. We are working within a tradition that has been refined for over a century.

## Sources

- management.org, "The History of Project Management" (2025)
- PMI, "Early Literature of Modern Project Management"
- PMI, "Uncovering Tacit Knowledge in Projects"
- Agile Manifesto (agilemanifesto.org, 2001)
- InfoQ, "Evolving GitHub Issues" (2025)
- GitHub Blog, "Evolving GitHub Issues and Projects" (2025)
- GitHub Docs, "About Projects," "Best practices for Projects"
- Womack & Jones, _Lean Thinking_ (1996)
- Rother & Shook, _Learning to See_ (1999)
- Ryan Singer, _Shape Up_ (2019)
- Our existing research: pdca-cycle.md, value-stream-mapping/, 5-whys/, fishbone-diagrams.md, a3-thinking/
