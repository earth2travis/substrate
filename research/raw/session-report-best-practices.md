# Session-End Reporting and Handoff Best Practices: Cross-Domain Research

## Research Document
**Date:** 2026-06-26
**Purpose:** Research best practices for session-end reporting, handoff documentation, and shift-change communication across five high-stakes domains, to inform the design of a SITREP pattern for AI agent sessions.
**Source note:** Compiled from established domain knowledge. Web search unavailable (Firecrawl not configured). URLs are canonical, stable references for each domain.

---

## 1. Military Shift-Change Briefings and Watch-Stander Turnover

### Overview

Military watch-standing (naval, command center, operations center) has centuries of institutional experience passing context from one operator to another. The core principle is that the relief must be able to assume the watch with no loss of situational awareness, potentially under combat or emergency conditions.

### Core Format Fields

Standard U.S. Navy / DoD watch turnover includes:

1. **Watch Purpose and Scope** - What this watch is responsible for
2. **Current Situation / Big Picture** - What is happening right now in the area of responsibility
3. **Active Contacts / Threats** - Items being tracked, their status, and threat assessment
4. **Ongoing Operations / Tasking** - Missions in progress, where they stand
5. **Equipment Status** - What is up, what is down, what is degraded
6. **Standing Orders / Commander's Intent** - What the commanding officer has directed, constraints
7. **Pending Actions / Timelines** - Time-critical tasks due during the watch
8. **Unusual Conditions / Exceptions** - Anything abnormal the relief needs to know
9. **Open Communications** - Who is on the net, pending calls, messages not yet acted on
10. **Read-Back / Confirmation** - The relief reads back critical items to confirm understanding

The turnover is typically conducted from a written watch log / deck log updated throughout the watch. The verbal turnover is backed by this log.

### Good vs. Bad

**Good turnover:**
- Written log maintained in real-time, not reconstructed at end of watch
- Verbal brief covers only deltas from routine, does not re-explain everything from scratch
- Relief asks questions; presenter does not assume understanding
- Read-back required for critical items (active threats, time-sensitive orders)
- Relief formally relieves only after confirming: "I have the watch"

**Bad turnover:**
- "Nothing happened, you'll be fine" with no structured handoff
- Verbal-only with no written backing
- Log filled out five minutes before turnover with reconstruction errors
- No read-back / no confirmation step
- Relief takes the watch without understanding standing orders because "it's quiet"

### Common Failure Modes

- The "quiet watch" assumption: nothing happened, so nothing to report, then a surprise event occurs
- Log drift: written log does not match what actually happened due to delayed entry
- Assumed knowledge: presenter assumes relief knows things they do not (especially during cross-training)
- Premature relief: outgoing watch-stander mentally checks out before formally being relieved
- Information overload: presenter dumps everything including trivia, relief cannot triage

### Sources
- U.S. Navy OPNAVINST 3120.32C (Standard Organization and Regulations of the U.S. Navy)
- U.S. Naval Institute, The Naval Officer's Guide, watch turnover procedures
- Army regulation watchstanding: https://armypubs.army.mil/ (AR 220-15 family)

---

## 2. Medical Shift Changes: SBAR and I-PASS

### Overview

Patient handoffs are a well-studied patient safety problem. The Joint Commission found communication failures during handoffs contribute to a significant majority of sentinel events. Multiple structured protocols have been developed and validated in research studies.

### 2a. SBAR (Situation, Background, Assessment, Recommendation)

Developed originally at Kaiser Permanente, adapted from Navy nuclear submarine communication protocols.

**Core fields:**
1. **S, Situation**: What is happening right now? (Patient, problem, urgency) One or two sentences.
2. **B, Background**: Relevant history, clinical context, meds, recent events leading to now.
3. **A, Assessment**: What do you think is going on? Differential diagnosis, stability, trend.
4. **R, Recommendation**: What should be done? Specific actions, timeline, who needs to be notified.

SBAR is primarily designed for urgent clinical communication (e.g., nurse calling physician) but is widely adapted for shift handoff.

**Good vs. Bad SBAR:**
- Good: Situation is one clear sentence. Bad: Wander through full history before stating the problem.
- Good: Assessment includes a clinical judgment. Bad: Only recites data with no interpretation.
- Good: Recommendation is concrete. Bad: "Call me if you need anything."

### 2b. I-PASS (Illness Severity, Patient Summary, Action List, Situation Awareness, Synthesis by Receiver)

Developed by a multi-institution research collaborative and validated in a landmark NEJM study (Starmer et al., 2014) that showed a 23% reduction in medical errors and 30% reduction in preventable adverse events in pediatric hospitals.

**Core fields:**
1. **I, Illness Severity**: One-word/short-phrase stability rating ("stable", "watcher", "unstable") so the receiver instantly knows triage priority.
2. **P, Patient Summary**: Brief summary statement, admitting diagnosis, key events during shift, current condition.
3. **A, Action List**: What needs to be done, by whom, timeline. To-do list with specific items.
4. **S, Situation Awareness and Contingency Planning**: "If X happens, then Y" anticipated events and what to do about them.
5. **S, Synthesis by Receiver**: The receiving physician restates key points and action items (read-back).

I-PASS is specifically a shift-change protocol (unlike SBAR which is per-clinical-event).

### Good vs. Bad (Medical Handoffs)

**Good:**
- Structured: follows the mnemonic every time, even for "boring" patients
- Illness severity stated upfront for triage
- Contingency plans stated explicitly ("If BP drops, give fluid bolus and call me")
- Receiver performs synthesis/read-back: active confirmation, not passive listening
- Written handoff document backs up verbal handoff
- Quiet patients still get reported: "stable, admitted for X, plan: [plan]"

**Bad:**
- Verbal-only handoff with no written backup
- "Stable patient, doing fine" with no illness severity or action list
- No contingency planning: "we'll see" is not a plan
- No read-back: receiver may miss critical items
- Handoff interrupted by pages/calls, done in 30 seconds
- Information dump with no prioritization (all patients equally detailed)

### Common Failure Modes

- Distortion / loss: each handoff is a game of telephone, details degrade
- Omission of the normal: people report problems but skip "all clear" patients who later reveal surprises
- Drop-out under time pressure: rushing skips structure entirely
- Failure to read back: critical orders misunderstood but never caught
- No contingency thinking: the unexpected happens and the incoming team was not warned
- Frequency decay: as teams tire, the structure erodes

### Sources
- Starmer AJ, et al. "Changes in Medical Errors after Implementation of a Handoff Program." New England Journal of Medicine, 2014; 371:1803-1812. https://www.nejm.org/doi/full/10.1056/NEJMsa1405556
- AAP I-PASS Handoff Program: https://www.aap.org/en/practice-management/patient-safety/i-pass-patient-handoff-program/
- The Joint Commission Sentinel Event data: https://www.jointcommission.org/sentinel-events
- Haig K, Sutton S, Whittington J. "SBAR: a shared mental model for improving communication between clinicians." Joint Commission Journal on Quality and Patient Safety, 2006; 32(3):167-175.

---

## 3. Software Engineering: End-of-Session Documentation and PR Descriptions

### Overview

Software engineering has the loosest formalization of the five domains, but strong informal norms. The two main artifacts are PR (Pull Request) descriptions and end-of-session notes. The PR description is the closest thing to a formal SITREP in software: it explains "what I did, why, what's still open."

### Core Format: Good PR Description

A well-structured PR description includes:

1. **Title** - Single-line summary
2. **Problem / Motivation** - What problem exists in the world? Why are we changing this?
3. **Solution / Approach** - What this PR does to address the problem. The diff tells you "how"; the description tells you "why."
4. **Testing Done** - How was this verified? (Unit tests run, manual testing steps, perf benchmarks)
5. **Scope** - What is and is not in this PR. Explicit "not addressed here: X, tracked in #5678."
6. **Risk / Breaking Changes** - Anything the reviewer needs to watch for
7. **Outstanding Items / Follow-ups** - What is still TODO, what is deferred
8. **Backout / Reversion Plan** - How to roll back if this breaks production
9. **Screenshots / Output Samples** - If visual or console output
10. **Checklist** - Lint passing, tests passing, docs updated, CHANGELOG entry

### Core Format: End-of-Session Notes

Common structure (drawn from GitLab check-ins, Basecamp, and Linux LKML reporting tradition):

1. **What I was doing** - One-line theme of the session
2. **What I completed** - Concrete ships / merges
3. **What I'm mid-way through** - In-flight work with state ("branch foo has the schema migration drafted but not tested")
4. **What's blocked / pending** - Dependencies, waiting on review, waiting on infra
5. **What's next** - Top items for the next session
6. **Anything weird** - Surprises, debug notes, "I spent 3 hours on Y because Z"

### Common Failure Modes

- Bystander effect: "code review will catch it" then no self-review, no problem statement
- Commit hygiene erosion: PRs accumulate unrelated changes, no squashing, no description
- "Will write the docs after merge" and the PR description never gets backfilled
- The mid-day memory: things you knew at noon you have forgotten by 5pm
- Disappearing debug knowledge: hours of debugging become a single "fix" commit
- No "stopping point" rationale: next agent does not know what placeholder you left or why

### Sources
- Conventional Commits: https://www.conventionalcommits.org/
- Angular contributing guide PR template: https://github.com/angular/angular/blob/main/CONTRIBUTING.md
- Linux Kernel submitting-patches: https://www.kernel.org/doc/html/latest/process/submitting-patches.html
- GitLab async communication: https://about.gitlab.com/handbook/communication/
- Basecamp Shape Up: https://basecamp.com/shapeup

---

## 4. Incident Response Post-Mortems and SRE Handoffs

### Overview

Modern SRE practice has two distinct but related artifacts:

- **Mid-incident IC handoff** - transferring incident command across personnel/time during long-running incidents
- **Post-incident post-mortem** - written retrospective capturing the timeline, root cause analysis, and action items

### 4a. Mid-Incident IC Handoff Fields

1. **Incident status / severity** - Severity level, current state of impact, customer impact ongoing?
2. **Customer impact** - What is being affected, how many, what surfaces
3. **What we've tried** - All remediations attempted and outcomes (critical, often neglected)
4. **What we're currently trying** - In-flight action items, who owns each, ETA
5. **Hypotheses / leading theories** - What we think the cause might be and ranking
6. **Decisions made** - Especially around trade-offs
7. **Open questions** - Things still being investigated
8. **Chain of command and contacts** - Who is on call, who has been escalated to
9. **Timeline / log** - Pointer to the incident timeline doc / chat transcript
10. **Action items outstanding** - Things decided but not yet executed
11. **Read-back / confirmation** - relief IC repeats back the active frame

### 4b. Post-Incident Post-Mortem Fields

1. **Title and Incident ID** - Date range, severity, owning service
2. **Author and Reviewers**
3. **Executive Summary** - Two or three sentences: what happened, impact, root cause
4. **Impact** - Severity, customer impact (counts, % of users, downtime), SLA violation, revenue
5. **Root Cause** - Single paragraph factual explanation
6. **Timeline** - Chronological event-by-event log
7. **What Went Well** - Actions that contributed positively
8. **What Went Wrong** - Specific failures, delays, confusions (blameless language)
9. **Where We Got Lucky** - Aspect that worked despite not having been designed to
10. **Action Items** - Each with: owner, due date, tracking issue
11. **Appendices** - Charts, logs, references

The post-mortem is BLAMELESS. Focus on systems and processes, not individuals. "Why did this action make sense to the person who took it at the time?"

### Good vs. Bad

**Good IC handoff (mid-incident):**
- Documents failed mitigation attempts explicitly
- States the current working hypothesis and alternatives
- Identifies action items that were decided but did not get executed
- Captures "what would be different if we knew X"
- Read-back by relief IC

**Bad IC handoff:**
- "Status is improving, I'll brief you on what you need" but does not
- Relief reads Slack scrollback instead of being briefed verbally
- Forgets to mention the experimental mitigation that did not work
- No decision log

### Common Failure Modes

- IC hand-off creates context loss: relief IC's mental model is different from outgoing's
- "We'll write the post-mortem later" then incident forgets key details in 24 hours
- Action items pile up, never tracked, drift away
- Post-mortem blames individuals, people hide mistakes next time
- Post-mortem focuses chronologically but skips why the system failed to defend against a single error
- Handoff fails to mention proposed mitigations that were rejected

### Sources
- Google SRE Book, Postmortem Culture chapter: https://sre.google/sre-book/postmortem-culture/
- Google SRE Workbook, postmortems: https://sre.google/workbook/postmortems/
- Atlassian Incident Postmortem: https://www.atlassian.com/incident-management/postmortem
- AWS Builder's Library: https://aws.amazon.com/builders-library/
- PagerDuty Postmortem Runbook: https://response.pagerduty.com/before/post_mortem/

---

## 5. Aviation CRM (Crew Resource Management) Debriefs

### Overview

CRM emerged after NTSB investigations identified crew communication failures (not technical flying failures) as the root cause of multiple fatal airline accidents in the 1970s and 1980s (notably United 173 and Tenerife). FAA mandates CRM training for Part 121 carriers. The post-flight debrief is where the crew reviews their joint performance in a structured way.

### CRM Debrief Core Fields

1. **Objectives** - What were we trying to accomplish on this flight/leg?
2. **What went well** - Specific named behaviors, not "we did good"
3. **What went wrong / Errors and threats** - Every error, however minor; threats encountered (weather, ATC, system anomalies, crew fatigue)
4. **Countermeasures deployed** - What did we do to manage errors/threats?
5. **What would we do differently** - Specific identifiable change items
6. **Open conversations** - Anything that came up that crew should talk about
7. **Hands on** - Brief duration, open initially, ends with "anything else?"

Structure guided by the LOSA (Line Operations Safety Audit) framework and the Threat and Error Management (TEM) model developed at UT Austin.

### Threat and Error Management (TEM) Model

- **Threats** - environmental or operational conditions that increase complexity
- **Errors** - crew actions or inactions that introduce undesired state
- **Undesired States** - conditions that reduce safety margin
- **Countermeasures** - what the crew did to mitigate

For each threat/error: Was it detected? Was it managed? Did countermeasures work? What did we learn?

### Common Failure Modes

- Authoritarian captain who does not invite F/O input, defeats the purpose
- Post-flight debrief becomes rubber-stamp ("great flight team") as the clock runs out
- Errors are reported only when they produce a visible bad outcome, close calls never get discussed
- Skip the debrief after "normal" flights (this is the exact trip where CRM matters most, because complacency is highest)
- Tempting to joke/tease or deflect because mistakes produce feelings

### Sources
- FAA AC 120-51E (CRM Training): https://www.faa.gov/regulations_policies/advisory_circulars/
- ICAO Doc 9806, Threat and Error Management
- Helmreich RL, Foushee HC. 1993. "Why Crew Resource Management?" In: Weiner, Kanki, Helmreich eds. Cockpit Resource Management. Academic Press
- NTSB accident report UA173 (Portland, 1978): https://www.ntsb.gov/investigations/

---

## Cross-Domain Synthesis: Universal Patterns

### What All Five Domains Have in Common

1. **Verbal + Written Combination** - Every domain pairs a synchronous verbal handoff (read-back required) with a written artifact. The verbal focuses on deltas; the written is the durable record. Neither alone is sufficient.

2. **Structured/templated format** - Every domain uses a fixed template. SBAR has four letters; I-PASS has five; military has numbered paragraphs; post-mortems have standard sections; good PRs follow a predictable structure. The template prevents omission and speeds production under pressure.

3. **Closing-loop / Read-back** - Every domain requires active confirmation by the receiver. I-PASS calls it "Synthesis by Receiver"; military requires read-back; IC handoff has the relief restate the active frame; CRM debrief asks each crew member to confirm. Read-back is not formality, it is the critical error-catching mechanism.

4. **Situation before Solution** - Good reports start with the problem and why before the what. SBAR starts with Situation. I-PASS starts with illness severity (the triage frame). Good PRs start with problem framing. Post-mortem executive summary covers what-happened before timeline.

5. **Severity/Priority Up Front** - I-PASS forces one-word severity first. Post-incident has severity-state at the top. Military puts active threats first. The good handoff gives the receiver a triage frame.

6. **Failed attempts / rejected options logged** - Post-mortems include "what we tried." IC handoffs document what mitigations were rejected. Medical I-PASS has contingency planning. This prevents the next person from re-running the same dead-end.

7. **What's Next, Concretely** - All domains close with the next action set. I-PASS Action List; post-mortem Action Items; PR Follow-ups; CRM "what would we do differently"; military Pending Actions.

8. **Blameless / Systems Framing** - SRE post-mortems explicitly blameless. CRM debrief normalizes error. Medical handoffs focus on errors in process not persons. Good handoffs preserve psychological safety.

9. **Contingency / "If-X-Then-Y"** - I-PASS explicitly includes this. IC handoff includes "what would we do if hypothesis is wrong." Good PRs include rollback plan. Military turnover includes contingency orders.

10. **Active Verification, Not Passive Sign-off** - Receiver reads back, IC repeats active frame, CRM asks each crewmember to contribute. "Any questions?" is not verification, it is a formality.

### Minimal Universal Structure for a Session Report (SITREP)

1. **Headline / Situation Summary** (1-3 sentences) - the elevator pitch
2. **Severity / Status** (one phrase or color) - green/yellow/red, done cleanly/partial/blocked/failed
3. **What was attempted** (list, concrete) - initiatives attempted, hypotheses tested, actions taken
4. **What succeeded / completed** (list) - concrete verifiable wins
5. **What failed / didn't work** (list) - includes the why if known, and rejected approaches
6. **What's blocked / pending** (list) - external dependencies, awaiting input, technical blockers
7. **Active state / In-flight work** (state dump) - "where I left off in the middle of X"
8. **Next actions** (sorted list) - who does what when for the next session
9. **Open questions / contingencies** - "If X then Y," unknowns, decision points
10. **References / State snapshots** - pointers to logs, commits, files, IDs, related issues, prior SITREPs

Close: read-back (when synchronous) - the receiver restates the situation summary and top three action items.

### Cross-Domain Pattern Matrix

| Pattern | Military Turnover | SBAR/I-PASS | PR Description | SRE Post-mortem | CRM Debrief |
|---|---|---|---|---|---|
| Situation summary | "Current situation" | S-Situation | Title+Problem | Exec Summary | Mission Objectives |
| Status/severity | Active threats listed | I-Illness Severity | Scope/Risk | Severity+Impact | Trip outcome |
| What attempted | Ongoing ops | N/A | Approach | What we tried | Errors declared |
| What completed | Watch actions done | P-Summary | Testing done | What went well | What went well |
| What failed | Equipment down | Contingencies used | Issues found | What went wrong | Threats/Errors |
| What's blocked | Pending comms/actions | A-Action list | Followups | Action items outstanding | Action items outstanding |
| Active state | "Next action due" | A-Action items | "Not in this PR" | Current mitigation state | TEM state |
| Next actions | Pending orders | A-Action items | Followups | Action items (next) | What we'd do differently |
| Contingencies | Standing orders | S-Contingency | Risk section | Where we got lucky | Countermeasures |
| References | Deck log | Written handoff doc | Commit IDs, linked PRs | Incident doc, timeline | Training record |
| Read-back | Verbal read-back | S-Synthesis by Receiver | Reviewer response | IC readback | Each crew confirms |

### Two Universal Anti-Patterns

1. **The "Nothing Happened" Dismissal** - "Quiet watch, stable patient, great flight, no notes." This hides the active frame precisely when it is most likely to be lost. The protocol must mandate the report especially when nothing visible happened.

2. **The "I'll Write It Later" Assumption** - End-of-watch rush, post-flight rushing, "we'll do postmortem next week," "PR description after merge." Each is the moment memory decays fastest and reconstruction error creeps in. The protocol must require capture close to the event.

### One Sentence

A session report is a context transfer artifact. It must be structured, templated, closed-loop confirmed, and capture failed attempts alongside successful ones, written as close to the event as possible, not as a courtesy at the end.