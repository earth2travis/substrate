# Recursive Self-Improvement of AI: Anthropic and OpenAI Positions

**Compiled:** July 20, 2026
**Sources:** Anthropic Institute article (July 2026), OpenAI Alignment Blog (December 2025), OpenAI Preparedness Framework v2 (April 2025), OpenAI Deep Research announcement (February 2025), arXiv papers, public statements by Sam Altman and Anthropic leadership

---

## Part 1: Anthropic -- "When AI Builds Itself" (July 2026)

Source: https://www.anthropic.com/institute/recursive-self-improvement
Authors: Marina Favaro and Jack Clark, Anthropic Institute

### The Core Claim

Anthropic is already delegating a growing share of AI development to AI systems. The trend points toward a system capable of fully autonomously designing and developing its own successor. That is recursive self-improvement (RSI). They are not there yet, but they believe it could come sooner than most institutions are prepared for.

The key internal data point: Anthropic engineers ship 8x as much code per quarter as they did from 2021-2025.

### The Evolution of the AI Development Loop

| Era | Stage | Description |
|-----|-------|-------------|
| 2021-2023 | Building the first Claude | People writing code and docs on laptops |
| 2023-2025 | Chatbots | People used early chatbots for short code snippets, copying output into editors |
| 2025-2026 | Coding agents | Agents write and edit code on their own, sometimes entire files |
| Today | Autonomous agents | Agents run code themselves and delegate hours of work to other agents |
| Future | Closing the loop | Agents could become capable enough to build and train models themselves |

### External Evidence

- Task completion horizons doubling roughly every 4 months (up from every 7 months previously)
- March 2024: Claude Opus 3 could complete 4-minute tasks
- March 2025: Claude Sonnet 3.7 managed 1.5-hour tasks
- March 2026: Claude Opus 4.6 managed 12-hour tasks
- METR found Claude Mythos Preview could work for "at least" 16 hours
- SWE-bench saturated in 2 years (low single digits to near 100%)
- CORE-Bench (reproducing existing research) saturated in 15 months (20% to near 100%)

### Internal Evidence from Anthropic

**Engineering:**
- More than 80% of code merged into Anthropic's codebase was authored by Claude as of May 2026 (up from low single digits before Claude Code launched in Feb 2025)
- Claude Code launched in research preview February 2025
- Lines of code merged per engineer per day stayed constant 2021-2024, then climbed in 2025, steepened in 2026
- Two inflection points: (1) Claude began to run code rather than just suggesting it, (2) models began to work autonomously over longer time horizons
- Q2 2026: typical engineer merging 8x as much code per day as in 2024
- Caveat: lines of code measures quantity over quality, true productivity gain is lower
- March 2026 internal poll of 130 research employees: median estimated 4x output with Mythos Preview vs. without any AI
- Claude shipped 800+ fixes reducing a class of API errors by 1000x; estimated a human would have taken 4 years
- Claude's success rate on most open-ended tasks: 76% in May 2026, up 50 percentage points in 6 months
- Example: Claude isolated an obscure debugging flag causing crashes in tens of thousands of training jobs, in 2 hours (would normally take 2-3 days)

**Code Quality:**
- Claude-written code was worse than human-written in late 2025, roughly at parity today, expected to be strictly better within the year
- Automated Claude reviewer catches bugs, security flaws, defects before merge
- Retrospective analysis: automated Claude review would have caught roughly 1/3 of bugs behind past claude.ai incidents

**Research:**
- Claude Opus 4 (May 2025) averaged ~3x speedup on training code optimization tasks; Claude Mythos Preview (April 2026) achieved ~52x
- A skilled human researcher needs 4-8 hours to reach 4x on the same task
- April 2026: first demonstration of Claude running open-ended research project end-to-end (can a weaker model reliably supervise a stronger one?)
- Two human researchers recovered 23% of the gap over a week; agents recovered 97% over 800 cumulative hours, using ~$18,000 in compute
- Caveats: didn't transfer cleanly to production-scale models; humans still chose the problem and created the scoring rubric
- Claude's research judgment (next-step decisions in real sessions): Opus 4.5 (Nov 2025) beat human choice 51% of the time; Mythos Preview (April 2026) beat human choice 64% of the time
- Check on judge bias: on moments where human's next move was already strong, models were judged better only ~20% of the time

**The human role narrowing:**
- Humans supply goals but no longer need to supply methods
- Large performance gaps persist in choosing goals (research taste and judgment)
- Once code quality reaches parity, humans stop writing code and shift to reviewing it
- But if humans can't review code as fast as Claude generates it, review becomes the bottleneck
- Amdahl's law applies to organizations: as one part speeds up, the bottleneck shifts elsewhere

### Three Future Scenarios

**Scenario 1: The trend stalls.**
- S-curves rather than exponentials. Diminishing returns to scale.
- Binding constraint could be supply chain (energy, chips, interconnect), not model capability
- Even frozen at today's level, major changes expected: Project Glasswing found 10,000+ high/critical severity vulnerabilities
- 100-person companies could do the work of 1,000-person ones
- They don't believe this scenario is likely: every measurable capability follows the same curve, and the curve hasn't bent

**Scenario 2: Compounding efficiency gains.**
- AI development substantially automated, humans set research directions and judge results
- 100-person companies doing the work of 10,000 or 100,000
- Revolutionizes knowledge work and government services, but also authoritarian surveillance and influence operations
- Amdahl's law already showing: human code review has become a bottleneck
- Explosion of new ideas, initiatives, tools, simulations beyond capacity to pursue

**Scenario 3: Full recursive self-improvement.**
- AI systems design and refine themselves
- Pace of progress determined entirely by compute availability
- Humans move to oversight, validation, verification of an expanding "virtual lab"
- Alignment is the least certain factor: models could be aligned enough to discover novel solutions, or misalignment could compound as models build successors
- Recursive intelligence alone doesn't change industrial production, social organization, or markets immediately
- Embodied intelligence (robotics) might quickly follow recursive intelligence

### Anthropic's Position on What to Do

- A slowdown or pause would be good, but only if coordinated and verifiable
- Unilateral pause by one lab is achievable immediately but accomplishes much less
- Need multiple well-resourced labs in multiple countries agreeing to stop under the same conditions, with mutual verification
- AI systems are far easier to conceal than missile silos; inputs are general-purpose; incentive to defect quietly is enormous
- Anthropic Institute will organize conversations with policymakers, researchers, civil society, and other AI companies
- They will build verification systems that a credible slowdown or pause would require

---

## Part 2: OpenAI -- RSI Positions and Publications

### 2.1 OpenAI Alignment Blog: "Hello World" (December 2025)

Source: https://alignment.openai.com/hello-world/

OpenAI explicitly researches safe development and deployment of AI "capable of recursive self-improvement (RSI)." Goals:
- Systems that consistently follow human intent in complex, real-world scenarios and adversarial conditions
- Avoid catastrophic behavior
- Remain controllable, auditable, and aligned with human values

The blog is framed as a "lab notebook" for sharing early safety/alignment work. Key statement: "no one should deploy superintelligent systems without being able to robustly align and control them." They believe empirical study of safety and alignment can help global decisions on development pace "as we get closer to systems capable of recursive self-improvement."

### 2.2 OpenAI Preparedness Framework v2 (April 2025)

Source: https://openai.com/index/updating-our-preparedness-framework/
PDF: https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf

AI Self-improvement is one of three core Tracked Categories (alongside biological/chemical and cybersecurity). Defined as "the ability of an AI system to accelerate AI research, including to increase the system's own capability," which "could also create new challenges for human control of AI systems."

**Thresholds:**

- **High:** Model's impact is equivalent to giving every OpenAI researcher a highly performant mid-career research engineer assistant (relative to 2024 baseline). At this level: "AI self-improvement may be beginning to accelerate." Require security controls meeting High standard.

- **Critical:** The model is capable of recursively self-improving (i.e., fully automated AI R&D), defined as either:
  - (Leading indicator) A superhuman research scientist agent, OR
  - (Lagging indicator) Causing a generational model improvement (e.g., o1 to o3) in 1/5th the wall-clock time of equivalent 2024 progress (e.g., sped up to just 4 weeks) sustainably for several months

At Critical level: "A major acceleration in the rate of AI R&D could rapidly increase the rate at which new capabilities and risks emerge, to the point where our current oversight practices are insufficient to identify and mitigate new risks, including risks to maintaining human control of the AI system itself." Action: halt further development until Critical-standard safeguards are specified.

### 2.3 OpenAI Deep Research (February 2025)

Source: https://openai.com/index/introducing-deep-research/

Agentic capability in ChatGPT powered by an o3-optimized model. Independently conducts multi-step web research, analyzes and synthesizes hundreds of sources (text, images, PDFs), produces comprehensive cited reports. Accomplishes in tens of minutes what takes humans many hours.

Key statement: "a significant step toward our broader goal of developing AGI, which we have long envisioned as capable of producing novel scientific research."

Deep research systems represent a step toward AI self-improvement by creating the research loop infrastructure: gather, analyze, synthesize, report.

### 2.4 OpenAI o3 and o4-mini System Card (April 2025)

Source: https://openai.com/index/introducing-o3-and-o4-mini/

o3/o4-mini show improved performance on software engineering and AI research tasks "relevant to AI self-improvement risks" (e.g., SWE-Bench). However, they remain below the Preparedness Framework's "High" threshold in the AI self-improvement category after rigorous safety evaluations. They demonstrate agentic tool use but lack capabilities for fully autonomous/open-ended real-world research assistant work.

### 2.5 RSI Safety Researcher Job Posting (2026)

Source: https://openai.com/careers/researcher-recursive-self-improvement-safety-san-francisco/

OpenAI's Preparedness team hiring for technical roles focused on "preparations for recursive self-improvement." Scope includes:
- Mitigations for "loss of control risk"
- Better pre-deployment risk-assessment
- Control measures
- "RSI-relevant training interventions"
- Turning technical work into established institutional practices
- Maintaining and strengthening RSI safety cases
- Addressing blind spots in mitigation areas

### 2.6 Sam Altman's RSI Statements (June 2026)

Via Reuters, The Information, and CryptoBriefing reporting on internal Slack messages:

- Altman indicated OpenAI could be "less than six months away from Recursive Self Improvement"
- He noted rapid RSI progress "could weaken the push for a quick IPO" (planned optionality within the next year, potentially September 2026)
- Direct quote: "The faster the potential RSI takeoff looks like it could be, the more it could be advantageous to delay an IPO," because "the technology and the world may change in surprising ways, and there might be good reasons to be a private company during that time"
- Internal milestones referenced: automated intern-level functionality by ~September 2026, "automated AI researcher" by ~March 2028

### 2.7 ResearcherBench: Evaluating Deep AI Research Systems (July 2025)

Source: arXiv:2507.16280
Authors: Tianze Xu, Pengrui Lu, Lyumanshan Ye, Xiangkun Hu, Pengfei Liu (Shanghai Jiao Tong University, SII, GAIR)

First benchmark evaluating Deep AI Research Systems (DARS) on frontier scientific questions. 65 research questions across 35 AI subjects, categorized as technical details, literature review, and open consulting.

Key findings: OpenAI Deep Research and Gemini Deep Research significantly outperform other systems, with particular strength in open-ended consulting questions. The paper explicitly frames this as "a meaningful step toward AI self-improvement, aligning with the vision of ASI for AI."

The benchmark represents a paradigm shift from assessing "whether deep research systems can retrieve and summarize information" to evaluating "whether DARS can understand complex, frontier research questions and provide meaningful insights."

---

## Part 3: Comparative Analysis

### Where Anthropic and OpenAI Align

Both labs agree that:
1. RSI is coming. The question is when, not if.
2. AI is already accelerating AI development internally. Both see significant productivity gains from AI-assisted coding and research.
3. The transition from human-driven to AI-driven development is a spectrum, not a binary switch. Current systems are on the spectrum.
4. Safety and alignment are the critical unsolved problems. Both labs invest in safety research as a prerequisite for RSI.
5. Coordination between labs is necessary. Unilateral action is insufficient.

### Where They Diverge

**Transparency about internal progress:**
- Anthropic shares extensive internal data (code authorship rates, productivity metrics, task completion success rates, research judgment benchmarks)
- OpenAI is more guarded: shares threshold definitions and evaluation results against those thresholds, but less internal productivity data

**Timeline estimates:**
- Anthropic avoids specific timelines but implies the transition could happen within years
- Altman states OpenAI could be "less than six months away" from RSI (June 2026)
- OpenAI's internal milestones: automated intern-level by September 2026, automated AI researcher by March 2028

**Framing of the risk:**
- Anthropic frames RSI as a spectrum with three scenarios, emphasizes the alignment problem as the least certain factor
- OpenAI frames RSI through their Preparedness Framework: a capability threshold to be evaluated and gated, with concrete actions at each level

**Safety approach:**
- Anthropic: verification systems for coordinated slowdown, "race to the top" on safety via ASL levels
- OpenAI: Preparedness Framework with Tracked Categories, halt development at Critical threshold until safeguards specified, RSI safety researcher hiring

### The Convergence

The most striking convergence is that both labs, independently, are building the same thing: agents that do AI research. Anthropic's Claude Mythos Preview runs open-ended research projects end-to-end. OpenAI's Deep Research produces comprehensive cited reports from hundreds of sources. Both are steps toward the same capability: AI systems that can conduct the research necessary to improve themselves.

The difference is that Anthropic is measuring and publicizing the internal acceleration (8x code output, 52x speedup on training optimization, 97% gap recovery on research tasks), while OpenAI is defining the thresholds at which they would halt development and hiring people to figure out how to not cross them unprepared.

### Key Open Questions

1. Can research taste be learned? Anthropic's data shows improving research judgment (51% to 64% in six months). But choosing which problems matter remains the human advantage.

2. Will the trend be an S-curve or an exponential? Anthropic says the curve hasn't bent. Altman says less than six months. Both could be right if the curve bends soon after the inflection point.

3. Is verification possible? Anthropic is building verification systems for coordinated slowdown. OpenAI's Preparedness Framework requires verifiable evaluations. Both face the problem that AI development is harder to monitor than nuclear weapons.

4. What happens to the economy? Anthropic's Scenario 3 describes a world where human labor stops being competitive. Neither lab has a good answer for what that means for most people.

5. Who decides? Anthropic wants multi-stakeholder conversations. OpenAI wants to remain private long enough to make the call internally. Both want to be the ones making the decision.

---

## Part 4: Key Data Points for Quick Reference

| Metric | Anthropic (2026) | OpenAI (2025-2026) |
|--------|------------------|---------------------|
| Code authored by AI | >80% of merged code (May 2026) | Not disclosed |
| Engineer productivity | 8x code per day (Q2 2026) | Not disclosed |
| Research speedup | 52x on training optimization (Mythos) | Not disclosed |
| Task horizon | 16+ hours (Mythos Preview) | Not disclosed |
| Research gap recovery | 97% (vs 23% human baseline) | Not disclosed |
| Research judgment | 64% better than human (April 2026) | Not disclosed |
| RSI timeline | Years (implied) | <6 months (Altman, June 2026) |
| Safety framework | ASL levels + verification for coordinated slowdown | Preparedness Framework v2 with Tracked Categories |
| Halt condition | Not specified explicitly | Critical threshold: halt until Critical-standard safeguards specified |
