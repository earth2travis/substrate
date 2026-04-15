# AI Native PM Operating System Walkthrough with Mike Ball

> **Source:** YouTube video transcript
> **Date:** February 7, 2026
> **Guest:** Mike Ball, Head of Product at David's Bridal
> **Host:** Akash
> **Link:** [The AI-Native PM Operating System [Live Demo]](https://www.youtube.com/watch?v=1C0daBcDBig&t=14s)

---

## Introduction

**Akash:** Mike Ball is leading product at David's Bridal, which is undergoing a massive digital transformation. He's been testing out all the AI tools. We've put our heads together in this episode to create the AI native PM operating system.

---

## What Makes an AI Native PM?

**Mike:** I think "thinking in prompts" is the fundamental thing. When you start integrating tools day to day, that's how you end up working. What do I need to get done? What's the best way to do it? If you're thinking about AI as an extension of yourself, you're asking: what are the instructions? What are the steps?

AI native PMs are working from "what do I need to do" to "what are the steps" to "what are the best tools to get me there." They're pushing themselves beyond that mental block of "that's too technical" or "that sounds too hard."

---

## The Operating System Concept

**Mike:** It's not necessarily a set of strict tools. Logging into 20 different tools for a bunch of different tasks throughout the day is a bunch of time wasting. What I see more and more people doing is centralizing around tools like Claude Desktop or Cursor, and connecting those to everything else — either bringing context and data into it, or having it interact with other tools like Jira or GitHub.

For example, I might be working on a PRD and I'm not sure if something got completed or shipped. Instead of opening a tab and checking Jira, I can say, "Can you check if this issue was completed?" I don't have to leave the tool I'm in. I can stay in my flow state without changing the UI.

---

## Demo: Connecting Tools via MCP in Cursor

**Mike:** If you're not familiar with Cursor, there are three areas: the agent panel on the right, the file editor in the middle, and the terminal at the bottom where I interact with Claude Code. I don't really use the IDE like most developers would — I'm using Cursor to connect tools via MCP to the agent or terminal.

For example, I had wedding planning content stuck in a spreadsheet and wanted to move it into Sanity, our content management system. I have the MCP connected already. The MCP has an API key that proves I can access the information and its own map to the API, so it can find what I'm asking for.

**Akash:** For people who don't know, CMS is a content management system — often the backend for a blog. And MCP is Model Context Protocol, which lets you connect apps and tools like Claude Code or Cursor to other tools without having to do most of the coding and integration yourself.

**Mike:** So instead of me having to go into Sanity, spin up the studio locally, and manually add a new task, it just does that for me. I say "add a task for car rentals for the honeymoon" and it creates the document and pushes it into the tool.

I've done this with Supabase for structuring database schema or doing migrations on the fly. I've done it with Render's MCP to host apps — I didn't have to know anything about DevOps to get it up and running.

---

## Claude Desktop: The Same Power, Different Interface

**Mike:** You can do the same thing in Claude Desktop. You can go into settings, then Connectors, and connect all these different tools they support out of the box. You can also configure your own with a simple text file.

**Akash:** I noticed you had some custom instructions in your Claude. What are your favorite project instructions?

**Mike:** At the project level, I try to frame the context of the specific project rather than everything in the entire application. For example, this project is the wedding planning app, this one is advertising and partnerships across e-comm. I set context for ones that need to be differentiated.

I also use the Memory MCP so it picks up relationships between ideas over time. Sometimes I'll say, "I need you to look across project knowledge" or "pull information from these two different projects."

---

## Why Claude Over ChatGPT?

**Mike:** Anthropic created the MCP framework and supported it best. Claude Desktop had it out of the gate. OpenAI has MCP support via API and maybe they're rolling it out in the chat app now, but I think the last two GPT model releases got more lazy and less useful. I just feel like Claude is more reliable for me.

**Akash:** Claude is also just a better writer, and PMs do a lot of writing. But if you have ChatGPT at work, they're starting to roll this out, so you can do a similar stack with ChatGPT at the center.

**Mike:** There are also desktop apps and open-source projects that act as a gateway — they let you connect MCPs and then connect to whichever models you want. I have one called Five (starts with a 5) that lets you jump between them. It's a project to set up, but if you don't have the tools you want, you can hotwire MCPs in an interesting way.

---

## Design Concepts: Figma Make and AI Studio

**Mike:** I took an image we generated in Canva — the problem is it's flat, just an image you can't edit without a lot of prompting. So I dropped it into Figma. If you right-click a frame, there's a "Send to Figma Make" option. It picks up layers and makes them editable.

I don't really trust Figma Make to write production-quality code, but it has a unique advantage: if you're working on product files structured in your design system, it's easy to move things in and visualize a specific flow or variation. You can then bring it back to the designer with a conceptual starting point.

The cool thing is when you copy it back to Figma, it's fully layered — designers can take the pieces they want and add them to the design.

**Akash:** So Figma Make is the most designer-friendly AI prototyping tool?

**Mike:** I don't even use it for prototyping. I use it mostly for design variation. If I need to see an edge case, error handling, or a specific state, and the designer is already working on the next thing, I'll take the existing design, throw it into Make, and generate variations for the developers.

### Google AI Studio for Prototyping

**Mike:** The last three months I've been blown away by Google AI Studio. It's Google DeepMind's developer-focused play space, but they've done a good job of not alienating non-developers. This is where you can test the newest models and get a free API key quickly.

In terms of how they manage chat context and memory, AI Studio is infinitely better than the Gemini app. The developer team just built a better experience.

You can one-shot apps in there. My team asked me to create marketing images with Halloween costume concepts for dresses on sale. I built a working app in literally 10 minutes.

**Akash:** How does AI Studio fit into the overall operating system?

**Mike:** I build rough concepts in AI Studio. Once I get to a good point, I'll either push to GitHub or deploy to Cloud Run. Then I switch to Cursor, open it up, and start editing in my normal workflow — check the browser, see the app running locally, go back and give feedback. It has to be at a certain level of quality before I pull it into my main operating system.

---

## Research and Context Gathering with Manus

**Mike:** When I say research, I mean context gathering. I used to use Perplexity more, but Manus is fantastic at this. With Agent Mode on GPT or even Research in Claude, it tends to max out quickly and burn through usage. Manus just runs independently, lets you know when it's done, and gives you the entire trace of everything it did.

For example, I tested it with a paranormal sightings app — sounds silly, but functionally it had community posting, governance workflows, map plotting, and time-based filtering. Great for stress-testing vibe coding tools.

Manus gave me a sample CSV, a data sources report in markdown, a quick start guide, and a human summary. I can access every piece independently and use them elsewhere. I pulled that raw information into Claude and asked for product requirements, user research, personas, and a technical strategy.

**Akash:** When do you use Manus vs. Claude regular?

**Mike:** My frustration with Claude is chat length limits and usage limits. If you turn on research mode, it just runs and doesn't do a great job showing its work like Manus does. I've used Claude's research mode maybe twice in the last two weeks.

The other reason is intentional context management. If Manus gets something wrong, I can pick and choose what I bring into my core operating system. LLMs tend to anchor themselves to whatever's in memory and create "common beliefs." If you're not careful about what you feed them, you end up with the equivalent of a conspiracy theorist LLM partner running with random ideas.

---

## Knowledge Reference: Confluence + Figma Gap Analysis

**Mike:** I asked Claude, "What do my Confluence docs say about the vision board?" It uses the Atlassian MCP with Rovo AI Search to go through Confluence, find my requirements documents, and give me a summary.

Then I grabbed a Figma link and asked it to compare the requirements against the MVP designs. The Figma MCP grabs a screenshot of the specific frame.

**Akash:** This is seriously connected workflows.

**Mike:** It gave me a pretty good gap analysis — catching specific discrepancies like "the wedding style from onboarding doesn't display on the vision board" and "documents show bridesmaid only instead of wedding party." Normally you're pulling up the PRD and looking at the design side by side, or you just miss this altogether.

I trust this as much as I trust myself going through a massive list comparing every module manually. Something might get missed either way. It's nice to have a second brain to gut check yourself.

---

## MCP Permissions and Security

**Mike:** Depending on what MCPs you set up, you can configure them to ask permission every time they do something, or only ask before they edit or push changes while allowing reads without permission. That's how I have it set up for the most part.

---

## Communications: Gmail, Calendar, and Connectors

**Mike:** There are MCPs for Gmail, Slack, and calendar. Claude has native connectors for these now — you can connect your calendar and ask what's coming up this week, or connect Gmail and search for emails. They used to only work on desktop but now they're in the browser version too.

They're calling them "connectors" because MCP is probably intimidating for less technical people.

**Akash:** I've never used this and I consider myself a Claude super user. I'm having so many epiphanies in this episode.

**Mike:** A lot of people think automation tools like n8n or Zapier are the answer, but I have a hard time thinking of something I do often enough to justify configuring an automation. This is more fluid.

---

## Cursor MCP Ecosystem

**Mike:** There's a long list of MCPs you can connect in Cursor: Notion, Figma, ClickUp, Chrome DevTools, FireCrawl, Amplitude, and many more.

Chrome DevTools is great — especially now that Cursor has browser use. It can pull DevTools reports and test functionality in your local instance. Not that I trust it blindly for testing, but it's a nice step beyond copying console errors and pasting them back in.

If you have product data in Amplitude, you can pull that in. Sometimes even in a coding space, I'll think about what the data says and switch Claude Code to plan mode.

---

## The Composable Stack

**Mike:** Conceptually, if you hear the word "composable" in technical architecture — you can pick and choose how it's configured to meet your needs at any given time. These are all different use cases throughout your week or month.

Sometimes a specific project has unique requirements. I was working on domain applications for new TLD strings. The evaluation criteria involved patent searches, cultural sensitivity, geographic considerations, and language conflicts. The patent database API was a one-time need — I just gave the API key to Claude Code and it handled it.

The right set of tools isn't constrained to ones you can log in to. There are free APIs and generous free tiers that can make you more effective.

---

## Recommended Tool Licenses and Budget

**Akash:** This is a lot of AI tool licenses. What should product leaders be getting for their teams?

**Mike:** For the core tools, start with read access for AI tools versus write if you're conservative. A lot of this is free — AI Studio is free, many APIs have generous free tiers.

Our internal approach is: start with a $20/month plan, show you're getting value from it, and we'll bump it up. If you start hitting limits, you're actually using it, and we bump it up again. You're not giving everybody a blanket $200/month plan that adds up if they're not using it.

### The Minimum Viable AI Native PM Stack

- **Claude:** $20/month (starting tier)
- **Manus:** $20/month
- **Google AI Studio / Gemini:** $20/month (or free with API key usage-based billing)

**Mike:** I'd even argue you can do a lot in AI Studio for free. Your IT team could spin up a project with an API key for usage-based billing and you get wholesale rates. Nano Banana is 4 cents an image — I could go crazy for a week and spend $20, then not use it for three weeks without paying a subscription for nothing.

---

## Making the Case for AI Tools in Your Organization

**Akash:** What if you're stuck where you don't have access to these tools? How do you make the case to leadership?

**Mike:** I work at David's Bridal — a 75-year-old wedding dress retailer with a lot of old beliefs and processes. When I talk to leadership, I say: here's what my team has done at this velocity, and our team is one quarter the size of most others working on this.

I took shipping and logistics data and said, "Here are three ideas that might be causing excessive overhead." They said, "We hadn't thought about problem B." That took me 10 minutes. Imagine what a team could do just asking smart questions.

I would be fairly concerned about any organization pushing back on people trying to use AI to be more productive.

**Akash:** A lot of PMs I talk to are in that world — automotive, finance, healthcare, living five years in the past. But you can chip away one tool at a time. Start with Claude, show the personal productivity gains, then move up.

**Mike:** Show that you're getting value from the technology first. Get organizational buy-in on the value. Show that it accelerates you, helps tackle hard problems, and unlocks talent. Then build the case: here's what I can do with this tool, here's where I'm hitting a wall, here's what I could do with the next tool. It's the same muscle memory as pitching a feature — just applied to your own tooling.

---

## AI Throughout the PM Lifecycle

**Akash:** When should PMs be using these tools in the lifecycle?

**Mike:** My default is the entire lifecycle.

**Upfront research and validation:** What about this consumer segment vs. that one? What competitors are in the space? Based on their recent marketing and releases, who's on a trajectory to compete with us? And then — red team it. Tear this thing apart. Tell me what I'm missing. Give me every possible angle so I'm prepared to defend it.

**During development:** Am I checking my design against requirements? Am I using it to shape tickets in Jira or Linear to make sure they're clear and specific? Did I reference the GitHub repo to make sure the ticket doesn't conflict with the current codebase?

**Prototyping and beyond:** I don't see a place where AI actually hurts — unless you don't know what you're doing with it.

---

## Biggest Mistakes PMs Make with AI

**Mike:** Garbage in, garbage out still resonates.

**Over-prompting:** Really deep, structured prompts meant to be reused systematically without understanding the subtleties each time. Unless it's a truly repetitive task, you don't need rigid prompt structures because it depends on what you're starting with and where you are in your thinking.

**Laziness with AI:** You put a prompt into Manus, download the files, upload them to Gemini without reading them, and prototype something. You'll get something along the lines of what you're thinking, but not very intentional. You're proving that that level of product management isn't valuable anymore.

**Taste and intuition matter:** Being able to look at something and say "I did this for X reason" is 10x more valuable than "I put this together." Junior PMs tend to say, "I used AI and put this doc together," but it doesn't make sense because they didn't use the actual customer interviews or existing information.

You have to be skeptical with all of it.

---

## Key Takeaways

1. **Build an operating system, not a tool stack** — centralize around Claude Desktop or Cursor and connect everything else via MCP
2. **Be intentional about context** — curate what goes into your AI tools to avoid creating "conspiracy theorist" AI partners
3. **Start small, show value, then expand** — begin with a $20/month plan and build the case for more investment
4. **Use AI throughout the entire PM lifecycle** — from research and validation through development and testing
5. **Maintain taste and skepticism** — AI accelerates your work, but product judgment and intentionality still matter most
