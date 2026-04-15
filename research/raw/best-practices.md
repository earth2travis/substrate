# Best Practices for Writing Effective UX Research Scenarios

## Synthesized from Authoritative Sources

---

## 1. What Makes a Scenario Effective

An effective scenario transforms a research session from an artificial test into something that approximates real behavior. The core mechanism is what Jakob Nielsen calls "suspension of disbelief": participants engage with scenarios deeply enough to behave as they would in their actual context, despite the artificial lab setting (Nielsen, NNG, "Authentic Behavior in User Testing").

**The three qualities every effective scenario must have** (from NNG's "Turn User Goals into Task Scenarios for Usability Testing"):

1. **Realistic**: Reflects activities the participant would actually perform in their own life or work
2. **Actionable**: Prompts the participant to DO something, not describe what they would do
3. **Non-leading**: Does not reveal how the interface should be used or give away the answer

These three principles are consensus across all major sources. They appear in NNG, Cooper's goal-directed design, Krug's "Rocket Surgery Made Easy," and Sauro's MeasuringU research.

---

## 2. Types of Scenarios

### Task Scenarios (NNG)
The most common type in usability testing. A short, situated prompt that gives context and asks the participant to accomplish a specific goal. Example: "You need to buy a pair of shoes for less than $40."

### Full-Scale Scenarios (Cooper / "About Face")
Alan Cooper distinguishes between task scenarios and what he calls "full-scale scenarios" in goal-directed design. These are narrative descriptions of a persona using a product across a complete workflow. They are not testing instruments; they are design tools used to envision the ideal experience before building it. Cooper's scenarios always begin with a persona and their goals, then describe how the product helps them achieve those goals.

Cooper identifies three types:
- **Context scenarios**: High-level, written early, describe the ideal experience without reference to technology
- **Key path scenarios**: More detailed, describe the main paths through the interface
- **Validation scenarios**: Edge cases and less common paths used to stress-test the design

### Elaborated Scenarios (Kim Goodwin / "Designing for the Digital Age")
Goodwin builds on Cooper's framework, adding detail about the environment, emotional state, and social context of the user. Elaborated scenarios include information about what is happening around the user, what they are thinking and feeling, and what constraints they face. These are primarily design artifacts, not research instruments.

### Scenario-Based Design Scenarios (John Carroll)
Carroll's foundational academic work at Penn State treats scenarios as the central representation in design. His framework (published in "Making Use: Scenario-Based Design of Human-Computer Interactions," MIT Press, 2000) positions scenarios as stories about people and their activities. Carroll argues that scenarios are deliberately rough and incomplete, which makes them useful for early exploration because they do not over-commit to implementation details.

Carroll identifies key properties of effective scenarios:
- They are concrete (specific people, specific situations)
- They are flexible (easy to revise and iterate)
- They are grounded in the world (not in the technology)
- They encourage reflection on tradeoffs

### Lean Scenarios (Leah Buley / "The User Experience Team of One")
Buley advocates for lightweight scenario creation that a solo practitioner can produce quickly. Her approach: start with a proto-persona, identify their top three goals, and write a brief narrative for each. These are less rigorous than Cooper's framework but pragmatic for resource-constrained teams.

---

## 3. How Scenarios Differ from Related Artifacts

| Artifact | Focus | Audience | Level of Detail |
|----------|-------|----------|-----------------|
| **Scenario** | User's goal in context | Research participants or design team | Situational, narrative |
| **User Story** | Business requirement | Development team | One sentence (As a... I want... So that...) |
| **Use Case** | System behavior | Developers, QA | Step-by-step system/actor interaction |
| **Test Script** | Exact procedure | QA/automation | Precise clicks, inputs, expected outputs |

The critical distinction: scenarios describe WHY someone is doing something and WHAT they want to achieve. Use cases and test scripts describe HOW the system responds. User stories capture the requirement but not the situated context.

NNG emphasizes this point repeatedly: "Rather than simply ordering test users to 'do X' with no explanation, it's better to situate the request within a short scenario that sets the stage for the action and provides a bit of explanation and context."

---

## 4. Writing Scenarios That Reveal Real Behavior

### Avoid Interface Vocabulary
NNG's "Write Better Qualitative Usability Tasks" (by Kathryn Whitenton) identifies using interface labels in task scenarios as the #1 mistake. If your interface has a button labeled "Find a Branch," do not write "Find a branch near you." Instead: "When is the bank location most convenient to you open tomorrow?"

This principle is grounded in the psychological concept of priming. Words from the interface in the scenario change what the participant looks for and how they scan the page.

### Avoid Describing Steps
Do not tell participants HOW to accomplish the task. "Go to the website, sign in, and tell me where you would click to get your transcript" is a bad scenario. "Look up the results of your midterm exams" is a good one.

### Provide Enough Context, But Not Too Much
Whitenton warns about both extremes:
- **Too vague**: "Make an appointment with your dentist" (participant will ask for more information)
- **Too elaborate**: A long backstory that the participant must remember while performing the task
- **Right balance**: "Make an appointment for next Tuesday at 10am with your dentist, Dr. Petersen"

The NNG guideline: provide all the information the participant needs to complete the task, without telling them where to click.

### Use Action Language, Not Hypotheticals
"How would you find a movie?" prompts verbal description. "Find a movie you'd be interested in seeing on Sunday afternoon" prompts actual behavior. NNG research shows self-reported behavior is significantly less accurate than observed behavior (Nielsen, "First Rule of Usability: Don't Listen to Users").

### Add Constraints to Induce Realistic Behavior
NNG's article on authentic behavior describes how adding budget constraints, time pressure, or accountability (e.g., "justify this choice to your boss") produces more realistic decision-making behavior. Without constraints, participants satisfice immediately, picking the first option they see.

---

## 5. Scenario Fidelity: When to Be Specific vs. Abstract

**Be specific when:**
- Testing a specific workflow (checkout, registration, search)
- You need participants to reach a particular part of the interface
- You need comparable data across participants (all doing the same task)
- Testing with paper prototypes or limited prototypes (you need to control the path)

**Be abstract when:**
- Exploring how users approach a problem space
- Testing information architecture (let them find their own path)
- Early-stage concept testing (you want to see what they gravitate toward)
- You want to discover tasks you had not anticipated

Cooper's context scenarios are intentionally abstract. His key path scenarios are intentionally specific. The fidelity matches the design stage.

---

## 6. Common Mistakes and Anti-Patterns

From NNG's "Write Better Qualitative Usability Tasks" (Whitenton), the 10 most common mistakes:

1. **Telling users where to go** (using interface labels as clues)
2. **Telling users what to do** (describing the steps, robbing you of discovery)
3. **Creating out-of-date tasks** (referencing past events, wrong seasons)
4. **Making tasks too simple** (testing navigation instead of comprehension)
5. **Creating an elaborate scenario** (unnecessary backstory that obscures the task)
6. **Writing an ad, not a task** (marketing language like "exciting new feature")
7. **Risking an emotional reaction** (mentioning family members who may have died)
8. **Trying to be funny** (jokes that distract or make participants uncomfortable)
9. **Offending the participant** (weight, politics, health, money, religion)
10. **Asking rather than telling** ("How would you..." instead of "Find...")

Additional anti-patterns from practitioner literature:

- **The compound task**: Combining multiple goals into one scenario so you cannot tell which part caused difficulty
- **The impossible task**: Asking participants to do something the system cannot actually support (unless that is deliberate)
- **The identity mismatch**: Asking a participant to pretend to be someone fundamentally different from themselves (a nurse pretending to be a doctor)
- **The leading scenario**: Embedding assumptions about what the participant values ("Since you care about privacy...")

---

## 7. How to Validate Scenarios Before Research

NNG's 7-step method (by Page Laubheimer) recommends pilot testing as the primary validation mechanism. Beyond that:

**Pre-study validation checklist:**
1. Read each scenario aloud. Does it sound natural?
2. Remove all words that appear in the interface
3. Confirm the task is actually completable with the current prototype/system
4. Check for timeliness (dates, seasons, current events)
5. Have someone outside the team read it and tell you what they think they are being asked to do
6. Verify the scenario matches your research questions (trace each scenario back to a research goal)
7. Check that you have not embedded emotional triggers, assumptions, or jargon

**The "tell me back" test** (from Krug's "Rocket Surgery Made Easy"): Hand the scenario to a colleague unfamiliar with the project. Ask them to paraphrase what they think they are supposed to do. If their interpretation differs from your intent, rewrite.

---

## 8. Adapting Scenarios for Different Research Methods

### Usability Testing
Most specific. The scenario gives a concrete goal and enough context to act. The participant uses the actual interface. Example: "You just moved to Austin. Find a dentist near your new address at 123 Main Street who accepts Blue Cross insurance and is taking new patients."

### Concept Testing
More open-ended. The scenario establishes a need or situation, then asks the participant to react to a concept. Example: "Imagine you are planning a dinner party for 8 people. You want to cook something impressive but you only have 2 hours. [Show concept.] How might this help you?"

### Contextual Inquiry
Scenarios may not be used at all, or are used as conversation starters. The researcher asks the participant to show them how they currently accomplish a task in their own environment. Example: "Can you walk me through the last time you needed to file an expense report?"

### Diary Studies
Scenarios define the trigger for when participants should make an entry. Example: "Whenever you feel frustrated trying to accomplish something on your phone, open the diary app and describe what happened."

### Surveys
Scenarios set context for rating scales or open-ended responses. They must be self-contained because there is no facilitator to clarify. Example: "Imagine you are shopping for a laptop online. You find one you like but it is $200 over your budget. How likely are you to..." Surveys require the most careful wording because there is no way to recover from ambiguity.

---

## 9. Scenario-Based Design (Carroll's Method)

John Carroll's work at Penn State (1990s through 2000s) established scenario-based design as a formal methodology in HCI. Key publications:

- "Making Use: Scenario-Based Design of Human-Computer Interactions" (MIT Press, 2000)
- "Scenario-Based Design: Envisioning Work and Technology in System Development" (Wiley, 1995)

Carroll's central argument: scenarios should be the fundamental unit of design work because they keep the focus on human activity rather than system functionality. His method involves:

1. **Problem scenarios**: Describe current practice and its breakdowns
2. **Activity design scenarios**: Describe new activities enabled by the envisioned system
3. **Information design scenarios**: Describe how information is structured and presented
4. **Interaction design scenarios**: Describe the specific mechanics of using the system

Each level adds detail. Each level can be evaluated by stakeholders and users because scenarios are readable by anyone, unlike technical specifications.

Carroll's work has been cited thousands of times and forms the theoretical backbone for most scenario-based approaches in UX, including Cooper's and Goodwin's.

---

## 10. The NNG 7-Step Method (from Research Goals to Scenarios)

Page Laubheimer's comprehensive method for generating scenarios from research goals:

1. **Determine the most important user tasks** (from analytics, surveys, stakeholder input)
2. **Discover which system aspects are of most concern** (stakeholder interviews, support logs, journey maps)
3. **Group and prioritize** (rank by importance to users AND organization)
4. **Create problem statements** for each top issue
5. **List research goals** for each problem statement
6. **List participant activities and behaviors** you need to observe for each goal
7. **Write scenarios** that will cause participants to exhibit those activities and behaviors

This method is particularly valuable because it creates traceability from business concerns all the way down to individual scenarios. It also generates stakeholder buy-in because they participate in steps 1 through 5.

---

## Source Summary

Each source referenced above is fully documented in `sources.md` with URLs, authors, and publication details.
