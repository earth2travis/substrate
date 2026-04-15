---
title: "Process Guide: Writing UX Research Scenarios"
tags:
  - ai-agents
  - knowledge-management
  - process-philosophy
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/process-guide.md
---

# Process Guide: Writing UX Research Scenarios

A practical, step-by-step guide for product designers and researchers.

---

## 1. When to Use Scenarios (and When Not To)

### Use scenarios when:
- **Usability testing**: You need participants to interact with an interface toward a goal
- **Concept testing**: You need to establish context before showing a concept
- **Scenario-based design**: You are envisioning future product behavior through narrative
- **Diary studies**: You need to define trigger conditions for participant entries
- **Surveys**: You need to ground abstract questions in concrete situations

### Do NOT use scenarios when:
- **Card sorting**: Participants organize items; no task context needed
- **A/B testing**: The system randomly assigns variants; no scenario framing required
- **Analytics review**: You are analyzing existing behavioral data, not generating new behavior
- **Stakeholder interviews**: You are gathering requirements, not testing behavior
- **Heuristic evaluation**: Expert review does not involve participants

### The decision test:
Ask yourself: "Do I need a participant to behave as if they have a real goal?" If yes, you need a scenario. If you are collecting data that does not depend on participant motivation, you do not.

---

## 2. Prerequisites: What You Need Before Writing

Before writing a single scenario, gather these inputs:

### Required
- **Research questions**: What are you trying to learn? (Not "is the design good?" but "Can users find the return policy within 60 seconds?")
- **User profile**: Who are your participants? What do they already know? What motivates them?
- **Interface or concept to test**: What will participants interact with?

### Strongly recommended
- **Personas or user archetypes**: Even lightweight ones help you write realistic context
- **Top task list**: What are the most important things users need to accomplish?
- **Stakeholder concerns**: What are the specific worries or questions the team has?
- **Problem statements**: What problems are you investigating?

### Helpful but optional
- **Journey maps**: Help you identify which moments to focus scenarios on
- **Support logs or FAQ data**: Reveal real pain points to build scenarios around
- **Analytics data**: Shows what users actually do (vs. what the team assumes)
- **Prior research findings**: Build on what you already know

---

## 3. Step-by-Step Process: From Research Question to Finished Scenario

### Step 1: List your research goals

For each research question, write one or more specific goals. Be precise.

**Research question**: "Is the checkout flow usable?"

**Research goals**:
- Discover where users get confused during checkout
- Learn whether users understand the shipping options
- Find out if users trust the payment form
- Determine whether users can apply a promo code

### Step 2: Identify the activities and behaviors you need to observe

For each goal, list what participants would need to DO for you to learn what you need.

**Goal**: "Learn whether users understand the shipping options"

**Activities to observe**:
- Participant reaches the shipping selection step
- Participant reads the shipping descriptions
- Participant selects a shipping option
- Participant explains why they chose that option

**Behavioral signals**:
- Hesitation or confusion at the shipping step
- Questions about what "standard" or "expedited" means
- Switching between options before deciding

### Step 3: Draft a scenario that causes those activities

Write a short narrative that gives the participant a reason to perform those activities WITHOUT telling them how to interact with the interface.

**Draft**: "Your friend's birthday is next Friday. You want to order a gift and make sure it arrives in time. Find something you think they'd like and complete the purchase."

### Step 4: Remove interface clues

Read your draft and circle any word that appears in the interface. Replace it.

- If the interface says "Add to Cart," do not write "add it to your cart"
- If the interface says "Checkout," write "complete the purchase" or "place your order"
- If the interface says "Express Shipping," do not mention "express"

### Step 5: Check for assumptions and leading language

Read the scenario as if you are the participant. Does it:
- Assume you know something you might not? Remove the assumption.
- Tell you how to feel about the product? Remove the emotional framing.
- Suggest which option is "correct"? Neutralize the language.
- Use jargon the participant might not know? Simplify.

### Step 6: Add necessary context, remove unnecessary context

**Necessary context**: Information the participant needs to act (budget, timeline, name/address for forms, specific need)

**Unnecessary context**: Backstory that does not affect behavior. If removing a sentence does not change what the participant does, remove it.

### Step 7: Pilot test

Read the scenario aloud to a colleague who is not on the project. Ask: "What do you think I'm asking you to do?" If their answer does not match your intent, rewrite.

Run at least one real pilot session. Watch for:
- Participant asking for clarification (scenario is ambiguous)
- Participant finishing in under a minute (scenario is too simple)
- Participant ignoring part of the scenario (too complex or too long)

---

## 4. Templates

### Template A: Usability Test Task Scenario

```
[Context: One sentence establishing who the participant is in this scenario]
[Motivation: One sentence explaining why they need to do this]
[Task: One sentence describing what they need to accomplish]

Optional: [Constraint: Budget, time, or other realistic limitation]
```

**Example**:
"You just started a new job and need to set up your benefits. You want to make sure you and your family are covered by health insurance. Enroll in a health plan that works for your situation."

### Template B: Concept Test Scenario

```
[Situation: Describe a realistic moment where this need arises]
[Show the concept]
[Open-ended prompt: How might this fit into what you just described?]
```

**Example**:
"Think about the last time you needed to cook dinner on a busy weeknight with very little time. What did that look like for you? [Participant describes.] Now I want to show you something. [Show concept.] How would this fit into a night like that?"

### Template C: Diary Study Trigger Scenario

```
[Trigger condition: Describe the specific moment when the participant should make an entry]
[What to capture: What information you need them to record]
```

**Example**:
"Each time you feel unsure about a financial decision this week, open the app and describe: what the decision was, what made you unsure, and what you did next."

### Template D: Survey Context Scenario

```
[Situation: Establish the context in 1 to 2 sentences]
[Question: Specific, answerable question grounded in that context]
```

**Example**:
"Imagine you are comparing two streaming services. One costs $8/month with ads and the other costs $15/month without ads. Which would you choose, and why?"

### Template E: Exploratory / Open Task Scenario

```
[Broad goal: Describe a general objective without specifying the path]
```

**Example**:
"You are thinking about taking a vacation sometime in the next few months. Use this site to explore your options and find something that interests you."

---

## 5. Review Checklist

Before using any scenario in research, verify each item:

### Language
- [ ] No words from the interface appear in the scenario
- [ ] No step-by-step instructions embedded in the scenario
- [ ] No marketing language or promotional tone
- [ ] No jargon the participant would not naturally use
- [ ] Action language ("Find...") not hypothetical ("How would you...")

### Realism
- [ ] A real person in this situation would actually do this
- [ ] Dates, events, and context are current and timely
- [ ] The task is completable with the current interface or prototype
- [ ] Constraints (budget, time) are realistic for the participant profile

### Neutrality
- [ ] Does not assume the participant's emotional state
- [ ] Does not assume the participant's values or preferences
- [ ] Does not suggest which option is "correct" or "best"
- [ ] Does not reference sensitive topics (health, weight, money, family, politics, religion) unnecessarily

### Clarity
- [ ] A person unfamiliar with the project can understand what to do after one read
- [ ] Contains all information needed to act (no need to ask the facilitator)
- [ ] Short enough to remember while performing the task (aim for 2 to 4 sentences)
- [ ] Not a compound task (tests one primary goal, not multiple goals bundled together)

### Traceability
- [ ] Maps to at least one research goal
- [ ] You can articulate what you will learn from observing this scenario
- [ ] The behaviors you need to observe will naturally occur during this scenario

---

## 6. Examples: Good vs. Bad, With Annotations

### Example 1: E-commerce

**Bad**: "Use the search feature to find Nike Air Max 90 shoes in size 10, add them to your cart, and proceed to checkout using the express shipping option."

**Why it's bad**: Tells the user which feature to use (search), which product to find (specific name), and which shipping to select. Tests reading comprehension, not usability. Uses interface labels ("cart," "checkout," "express shipping").

**Good**: "You need a new pair of running shoes. You'd like to spend under $150 and need them within a week. Find a pair you like and buy them."

**Why it's good**: Establishes a realistic goal. Provides constraints (budget, time) that force real decision-making. Does not prescribe the path. Will reveal whether participants can find products, evaluate options, and complete purchase within the interface.

---

### Example 2: Healthcare Portal

**Bad**: "You want to check your lab results. Click on the Health Records tab, then select Lab Results from the dropdown menu."

**Why it's bad**: This is a test script, not a scenario. It gives away the navigation path entirely. You will learn nothing about whether "Health Records" is a meaningful label.

**Good**: "Your doctor told you last week that your blood test results would be available online. Check whether they are ready."

**Why it's good**: Provides realistic motivation. Does not reveal where to look. Will reveal whether the participant can find lab results using whatever path they choose.

---

### Example 3: Internal Tool

**Bad**: "How would you submit a time-off request?"

**Why it's bad**: "How would you" prompts verbal description, not action. The participant will talk through what they would do instead of doing it.

**Good**: "You want to take the week of July 14th off for a family trip. Submit your request."

**Why it's good**: Provides specific dates (necessary context). Uses action language. The participant will actually interact with the system.

---

### Example 4: Concept Test

**Bad**: "What do you think of this exciting new meal planning feature?"

**Why it's bad**: "Exciting new" is marketing language that primes positive responses. "What do you think" is vague and leads to surface-level opinions.

**Good**: "Think about the last time you planned meals for the week. What was that like? [Participant describes.] Now take a look at this. [Show concept.] How does this compare to what you usually do?"

**Why it's good**: Grounds the participant in their real experience first. Shows the concept without framing it positively or negatively. Asks for comparison to their reality, which produces genuine assessment.

---

### Example 5: The Over-Elaborate Scenario

**Bad**: "You are a 35-year-old marketing manager named Alex. You live in Portland with your partner and two dogs. You commute 45 minutes each way. Last month, your company switched to a new project management tool and you have been struggling with it. Your boss asked you to set up a new project for the Q3 campaign. You need to add 6 team members, create 12 tasks, and set a deadline for August 1st."

**Why it's bad**: Too many irrelevant details. The participant must parse a paragraph of fiction to find the actual task. The identity details (name, age, location, pets) do not affect behavior. The specific numbers (6 members, 12 tasks) turn it into a procedural checklist.

**Good**: "Your team is starting a new project. Set it up in this tool and get it ready for your team to use."

**Why it's good**: Simple, clear, lets the participant's own mental model of "setting up a project" drive their behavior. You will observe what they think is important to configure, which is more valuable than watching them follow your checklist.

---

## 7. Adapting for Method

The same core need can be expressed differently depending on the research method:

### Core need: "Users need to find and compare health insurance plans"

**Usability test scenario**:
"Open enrollment starts next week. You need to choose a health plan for yourself and your spouse. Find a plan that covers both of you and fits your budget of $400/month. Be ready to explain why you chose it."

**Concept test scenario**:
"Tell me about the last time you had to choose a health insurance plan. What was that experience like? [Participant describes.] Now I want to show you a different way this could work. [Show concept.] Walk me through your reaction."

**Survey scenario**:
"Imagine you are choosing a new health insurance plan. You need to compare three options that differ in monthly cost, deductible, and network size. On a scale of 1 to 7, how confident are you that you could make the right choice using an online comparison tool?"

**Diary study trigger**:
"Over the next two weeks, whenever you look up health-related information online (costs, providers, coverage, prescriptions), make a diary entry describing what prompted it, what you searched for, and whether you found what you needed."

**Contextual inquiry prompt**:
"Can you show me how you last looked into your health insurance coverage? Walk me through what you did, where you went, and what happened."

### What changes across methods:

| Dimension | Usability Test | Concept Test | Survey | Diary Study | Contextual Inquiry |
|-----------|---------------|--------------|--------|-------------|-------------------|
| Specificity | High | Medium | Medium | Low (trigger-based) | Low (participant-led) |
| Action required | Yes, use the interface | React to concept | Answer questions | Self-report | Demonstrate |
| Facilitator present | Yes | Yes | No | No | Yes |
| Time of task | During session | During session | Participant's own time | Over days/weeks | In participant's context |
| Scenario length | 2 to 4 sentences | 1 to 2 sentences + discussion | 1 to 2 sentences | 1 to 2 sentences | 1 sentence or less |

---

## Quick Reference: The Five Rules

1. **Start with the user's goal, not the feature you want to test.** The scenario describes a situation where the user has a need. The feature is how they might fulfill it.

2. **Strip out every word that appears in the interface.** If you cannot write the scenario without interface vocabulary, your scenario is too tightly coupled to the implementation.

3. **Tell participants to DO, not to DESCRIBE.** "Find a flight" produces behavior. "How would you find a flight?" produces narration.

4. **Provide context, not instructions.** The participant should know WHY they are doing something and any relevant constraints. They should not know HOW to do it.

5. **Pilot test every time.** One dry run reveals more problems than ten rounds of editing.
