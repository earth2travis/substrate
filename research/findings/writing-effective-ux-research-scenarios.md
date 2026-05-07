---
title: Best Practices for Writing Effective UX Research Scenarios
tags:
- ux
- research
- scenarios
- usability
- testing
- design
related:
- design-system-as-code
- creative-partnership
source: research/raw/writing-effective-ux-research-scenarios.md
---




# Best Practices for Writing Effective UX Research Scenarios

Synthesized from NNG, Cooper's goal-directed design, Krug's "Rocket Surgery Made Easy," Sauro's MeasuringU, Carroll's scenario-based design, and practitioner literature.

## What Makes a Scenario Effective

An effective scenario transforms a research session from an artificial test into something that approximates real behavior. The core mechanism is what Jakob Nielsen calls "suspension of disbelief": participants engage deeply enough to behave as they would in their actual context.

**The three qualities every effective scenario must have:**

1. **Realistic:** Reflects activities the participant would actually perform
2. **Actionable:** Prompts the participant to DO something, not describe what they would do
3. **Non-leading:** Does not reveal how the interface should be used or give away the answer

## Types of Scenarios

### Task Scenarios (NNG)
The most common type in usability testing. A short, situated prompt that gives context and asks the participant to accomplish a specific goal. Example: "You need to buy a pair of shoes for less than $40."

### Full-Scale Scenarios (Cooper / "About Face")
Narrative descriptions of a persona using a product across a complete workflow. Design tools, not testing instruments. Three types: context scenarios (high-level, ideal experience), key path scenarios (main paths through interface), validation scenarios (edge cases).

### Elaborated Scenarios (Kim Goodwin)
Add detail about environment, emotional state, and social context. Include what is happening around the user, what they are thinking and feeling, what constraints they face.

### Scenario-Based Design Scenarios (John Carroll)
Carroll's foundational work treats scenarios as the central representation in design. Key properties: concrete, flexible, grounded in the world, encourage reflection on tradeoffs.

### Lean Scenarios (Leah Buley)
Lightweight scenario creation for solo practitioners. Start with a proto-persona, identify top three goals, write a brief narrative for each.

## How Scenarios Differ from Related Artifacts

| Artifact | Focus | Audience | Level of Detail |
|----------|-------|----------|-----------------|
| **Scenario** | User's goal in context | Research participants or design team | Situational, narrative |
| **User Story** | Business requirement | Development team | One sentence |
| **Use Case** | System behavior | Developers, QA | Step-by-step interaction |
| **Test Script** | Exact procedure | QA/automation | Precise clicks, inputs, expected outputs |

The critical distinction: scenarios describe WHY and WHAT. Use cases and test scripts describe HOW. User stories capture the requirement but not the situated context.

## Writing Scenarios That Reveal Real Behavior

### Avoid Interface Vocabulary
NNG's #1 mistake: using interface labels in task scenarios. If your interface has a button labeled "Find a Branch," do not write "Find a branch near you." Instead: "When is the bank location most convenient to you open tomorrow?"

This is grounded in the psychological concept of priming. Words from the interface change what the participant looks for.

### Avoid Describing Steps
Do not tell participants HOW to accomplish the task. "Go to the website, sign in, and tell me where you would click" is a bad scenario. "Look up the results of your midterm exams" is a good one.

### Provide Enough Context, But Not Too Much
- **Too vague:** "Make an appointment with your dentist" (participant will ask for more information)
- **Too elaborate:** A long backstory that must be remembered while performing the task
- **Right balance:** "Make an appointment for next Tuesday at 10am with your dentist, Dr. Petersen"

### Use Action Language, Not Hypotheticals
"How would you find a movie?" prompts verbal description. "Find a movie you'd be interested in seeing on Sunday afternoon" prompts actual behavior. Self-reported behavior is significantly less accurate than observed behavior.

### Add Constraints to Induce Realistic Behavior
Budget constraints, time pressure, or accountability ("justify this choice to your boss") produce more realistic decision-making. Without constraints, participants satisfice immediately, picking the first option they see.

## Scenario Fidelity: When to Be Specific vs. Abstract

**Be specific when:**
- Testing a specific workflow (checkout, registration, search)
- You need participants to reach a particular part of the interface
- You need comparable data across participants

**Be abstract when:**
- Exploring how users approach a problem space
- Testing information architecture (let them find their own path)
- Early-stage concept testing
- You want to discover tasks you had not anticipated

## Common Mistakes and Anti-Patterns

From NNG's "Write Better Qualitative Usability Tasks" (Whitenton):

1. **Telling users where to go** (using interface labels as clues)
2. **Telling users what to do** (describing the steps)
3. **Creating out-of-date tasks** (referencing past events, wrong seasons)
4. **Making tasks too simple** (testing navigation instead of comprehension)
5. **Creating an elaborate scenario** (unnecessary backstory)
6. **Writing an ad, not a task** (marketing language)
7. **Risking an emotional reaction** (mentioning family members who may have died)
8. **Trying to be funny** (jokes that distract)
9. **Offending the participant** (weight, politics, health, money, religion)
10. **Asking rather than telling** ("How would you..." instead of "Find...")

Additional anti-patterns:
- **The compound task:** Multiple goals in one scenario
- **The impossible task:** Something the system cannot support
- **The identity mismatch:** Asking a participant to pretend to be someone fundamentally different
- **The leading scenario:** Embedding assumptions about what the participant values

## How to Validate Scenarios Before Research

NNG's 7-step method:

1. Read each scenario aloud. Does it sound natural?
2. Remove all words that appear in the interface
3. Confirm the task is actually completable with the current prototype/system
4. Check for timeliness (dates, seasons, current events)
5. Have someone outside the team read it and paraphrase what they think they are being asked to do
6. Verify the scenario matches your research questions
7. Check that you have not embedded emotional triggers, assumptions, or jargon

**The "tell me back" test** (from Krug): Hand the scenario to a colleague unfamiliar with the project. Ask them to paraphrase what they think they are supposed to do. If their interpretation differs from your intent, rewrite.

## Adapting Scenarios for Different Research Methods

- **Usability Testing:** Most specific. Concrete goal, enough context to act.
- **Concept Testing:** More open-ended. Establishes a need or situation, asks participant to react.
- **Contextual Inquiry:** Scenarios may not be used, or used as conversation starters.
- **Diary Studies:** Scenarios define the trigger for when participants should make an entry.
- **Surveys:** Scenarios set context for rating scales. Must be self-contained because there is no facilitator to clarify.

## Scenario-Based Design (Carroll's Method)

Carroll's central argument: scenarios should be the fundamental unit of design work because they keep the focus on human activity rather than system functionality. His method involves four levels:

1. **Problem scenarios:** Describe current practice and its breakdowns
2. **Activity design scenarios:** Describe new activities enabled by the envisioned system
3. **Information design scenarios:** Describe how information is structured and presented
4. **Interaction design scenarios:** Describe the specific mechanics of using the system

Each level adds detail. Each level can be evaluated by stakeholders and users because scenarios are readable by anyone, unlike technical specifications.

## The NNG 7-Step Method (from Research Goals to Scenarios)

Page Laubheimer's method for generating scenarios from research goals:

1. Determine the most important user tasks
2. Discover which system aspects are of most concern
3. Group and prioritize
4. Create problem statements for each top issue
5. List research goals for each problem statement
6. List participant activities and behaviors you need to observe
7. Write scenarios that will cause participants to exhibit those activities and behaviors

This creates traceability from business concerns all the way down to individual scenarios. It also generates stakeholder buy-in because they participate in steps 1 through 5.
