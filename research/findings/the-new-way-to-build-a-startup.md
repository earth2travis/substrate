---
title: The New Way To Build A Startup
tags:
  - ai-agents
  - knowledge-management
  - systems-thinking
related:
  - [[1password-integration]]
  - [[28-openclaw-mistakes-kloss]]
  - [[5-whys]]
  - [[a3-thinking]]
source: research/raw/the-new-way-to-build-a-startup.md
---

# The New Way To Build A Startup

**Source:** [The New Way To Build A Startup](https://youtu.be/rWUWfj_PqmM?si=pUa1Wt_WV7eTPSuJ)  
**Date:** Mar 5

---

## Granola Summary

### 20x Companies Concept

- Companies using AI automation across all internal functions to compete against much larger incumbents
- Evolution of Parker Conrad’s “compound startup” theory applied to internal automation
- Term coined by Giga ML founders who beat 100x larger competitors to win DoorDash

### AI FTE Teammates Approach

- Giga ML’s Atlas agent handles all product tasks
  - Uses browsers, edits policies, writes code
  - Doubles/triples engineer scope by eliminating boilerplate work
  - Single human FTE services Fortune 500 clients with 500k-1M daily calls
- Atlas works alongside human to focus on customer relationships and feature requests

### AI Integrated Source-of-Truth Systems

- Legion Health’s custom care operations interface
  - Pulls patient history, scheduling, insurance codes instantly
  - Prevents communications from getting lost across departments
- Scaled 4x revenue with flat ops headcount
  - Thousands of patients monthly with 1 clinical lead, 1 patient support, 1 billing person
  - Traditional healthcare companies need entire departments for same functions

### Document Manual Tasks and Build Custom Agents

- Phase Shift’s approach: 12-person team competing against companies with hundreds of employees
- Process:
  1. Employees document daily manual tasks
  2. Build quick AI agents for each workflow
  3. Customize agents per employee preferences
- Results: Avoided hiring design person by using Magic Patterns for all frontend designs
- Culture of relentless automation enables delayed hiring across entire functions

---

Chat with meeting transcript: [https://notes.granola.ai/t/6909d26b-eecd-4251-9d0b-12c0305f0f32-00demib2](https://notes.granola.ai/t/6909d26b-eecd-4251-9d0b-12c0305f0f32-00demib2)

## Full Transcript

### Opening: Claude and the shift to internal automation

**Them:** If you haven't tried Claude Code in the last month, it's time to give it another shot. And if you have, you know what I'm talking about. It feels like AGI is here.

One of Anthropic's own engineers writes Claude, wrote Claude. Cowork: us humans meet in person to discuss foundational architecture and product decisions. But all of us devs manage anywhere between three and eight Claude instances, implementing features, fixing bugs, or researching potential solutions. Think about what that means. The team developing one of the most sophisticated AI products in the world, something many of you probably use every day, is using this AI internally to improve their product.

I think this points to a fundamental shift in how startups operate. Right now, the best teams aren't automating one or two internal functions, they're automating all of them. Often they're tiny teams, able to beat huge incumbents thanks to internal automation. Their leanness is their superpower. I've been calling these startups **20x companies**.

### 20x companies and the compound startup idea

Several years ago, my friend Parker Conrad, founder of Rippling and Zenefits, coined the term **compound startup** to describe companies that build multiple integrated products in parallel rather than focusing narrowly on one thing. The theory of the compound software business is that there's this island of product market fit that's kind of over the edge of the horizon line, that's sort of harder to get to, but if you can build multiple parallel applications at once, you can get there, and it actually ends up being a much more powerful type of product market fit that's much harder to displace at that point.

The 20x company could be an evolution of Parker's idea, but applied to internal automation. Instead of just narrowly automating a few things like writing code or handling customer support, 20x companies build automations across all internal functions: code, support, marketing, sales, hiring, QA, and more. This makes each of their employees orders of magnitude more powerful than they would be otherwise. It also allows them to postpone hiring additional sales and ops staff for much longer, keeping payroll down and culture from drifting.

### Giga ML and Atlas: AI teammate as superpower

The phrase "20x company" was actually coined by the founders of Giga ML, which builds voice based customer service agents for enterprise, to describe how they managed to close DoorDash as a customer going up against incumbents that were literally 20x as large. When we got DoorDash as a customer, we were approximately four to five engineers going against players who had like 100x engineers. So we kind of coined the term: hey, we are a 20x company because we are able to beat these much bigger players by having a better product and better numbers.

Giga was able to close DoorDash and several other Fortune 500 companies as customers because of a powerful internal agent they call **Atlas**. Atlas can basically do anything within the product that you want to do. It can use browsers, it can edit the policies, it can write code, it can do anything within the product. Atlas dramatically expands the range of what each engineer can take on. Before Atlas, every engineer can probably work on four to five problems at once because they're bottlenecked by all the boilerplate stuff they have to do for the customers: customer integrations, they would have to probably work on that. Now with AI taking care of all the boilerplate stuff, each engineer's scope is basically doubled or tripled because they don't need to work on the boilerplate code.

But Atlas doesn't just accelerate Giga's engineers. It also acts as a full time AI employee that works in tandem with a human FTE to service dozens of accounts. Right now we have only a single human FTE within the company. As hard as it is to believe, we have companies like DoorDash using us. We're in pilots with multiple Fortune 500, ten Fortune 500s, where each of these companies probably have volumes over 500,000 or a million calls a day. It's only been possible because we have Atlas and this person can primarily focus on just the customer relationships, the asks by the customers, taking customer requests and turning them into feature requests and everything.

Building an AI teammate is one approach. Another is to build an AI integrated source of truth that gives employees instant context across your entire system.

**Me:** I know.

### Legion Health: single source of truth

**Them:** Legion Health, which is building an AI native psychiatry network, is one example of how to do this. Legion built a custom internal interface for their care operations team that lets them pull patient history, scheduling availability, insurance codes, and a lot more. What we're showing you right now is an interface that a vast majority of our care operations team uses in their day to day work for anything that actually has not been yet automated. And this includes everything from digging into a particular patient or many patients' backgrounds, trying to understand where they're at in their journey, if they need a new appointment to be rescheduled, if they're having a prescription issue, if they've sent us a message that in traditional healthcare might have otherwise gotten lost in the sea of different communications that go back and forth between so many different people. All of that is at fingertips' reach for every single member of our care ops.

This single source of truth interface has let Legion keep its ops headcount flat even as it's dramatically scaled revenue. We've grown 4x in the past year, but we haven't hired a single net new person. We've been able to 4x the number of patients. We're seeing thousands of patients a month. We have dozens of providers, but we have one clinical lead, we have one patient support person, and we have one billing person. And in a typical healthcare company, those are all departments. Those are call centers. Those are groups of people sitting around desks doing a ton of things manually.

### Phase Shift: custom agents per employee

A third approach is to build custom agents for each employee depending on their workflow and preferences. **Phase Shift**, which is building agents to automate accounts receivable, took this approach. Phase Shift right now is a 12 person team and we're going up against companies that have been around since 2006 that have hundreds of employees. The key to us as a 12 person team moving so fast is we bring AI into every process that is manual and try to automate as much as possible with AI agents.

One way Phase Shift does this is by literally asking its employees to document the manual tasks they do and then building custom agents for them. So what we do is essentially say, what do you spend your time doing throughout the day? And we make them document that and then we build quick AI agents. And this culture of relentless automation has let Phase Shift delay hiring for entire functions. We've actually avoided hiring a design person at the company so far. To date we're about a 12 person company. By just leveraging Magic Patterns that our engineering team uses to build all front end designs.

### Closing

These approaches aren't mutually exclusive. You can build AI teammates, a unified source of truth, and custom agents for each member of your team. The companies that do this are staying lean and setting record high growth rates. This is the new way to build, and the startups that figure it out first are going to win.
