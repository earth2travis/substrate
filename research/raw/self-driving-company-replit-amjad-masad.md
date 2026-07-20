# Self-Driving Company - Replit / Amjad Masad

Source: https://x.com/amasad/status/2077802290304684404
Linked article: https://replit.com/blog/self-driving-company
Author: Amjad Masad (Founder & CEO, Replit)
Date: Thu, Jul 16, 2026 (post and article)

## Key Excerpts and Facts

"We are beginning to see what happens when a company learns to operate itself."

"In the past six months, engineers at Replit have nearly tripled code output. Review times held steady. Reversions and product incidents have stayed flat. Quality metrics improved, and releases have accelerated. All the typical trade-offs you might expect have not occurred."

"Agents now investigate production incidents, review pull requests, answer questions, analyze business data, triage support tickets, research sales accounts, and improve the systems that power Replit Agent itself."

"It feels like a single master intelligence threaded through every employee, even though it is not. It is an expanding system of agents operating across the company: taking goals from people, gathering context, performing work, checking the results, and escalating when human judgment is needed."

"We think this represents the beginning of a new kind of organization: the self-driving company."

"A self-driving company is not one without people. People still choose the destination. They decide which problems matter, make difficult tradeoffs, exercise taste, and take responsibility for the outcome. But increasingly, they do not perform every step required to get there."

"The shift began late last year. Like many people working in AI, we returned from the Christmas break feeling that something fundamental had changed. Models could sustain work over much longer horizons. Tasks that had repeatedly failed, like alert triage and root-cause investigation, began working. AI started solving some of our most stubborn bugs. So we stopped treating agents as tools that lived inside an editor or chat window. We wove them, carefully, into the fabric of the company itself."

"Once engineering proved the value, adoption took on a life of its own. Team after team started offloading their most tedious work, reclaiming time for the strategic and creative thinking that actually moves the business. People don't feel like they've been automated. They feel like they've been promoted."

### Engineering Metrics

"From early January to late June, there was a 5.8X increase in the lines of code contributed."

"Keeping a consistent cohort of authors, we see 2.9x as much code as before. Traditionally, it’s considered excellent if you keep output per engineer flat as you scale a team. We just tripled per engineer rate while doubling the team."

"code review latency is flat, largely because we put our agent to work in reviewing code. It’s now able to assess risk levels and only call in a second human reviewer when necessary. That means 30% (and growing) of human PR review time has been saved."

"PR reversion rates and incidents opened, trends are flat. This means we’re actually improving on a relative basis."

"Human code reviews have the benefit of an agentic co-reviewer, so more bugs get caught. Incident investigations (meaningful bugs or actual incidents) are assisted by an agent that attempts to find the root cause, so mean time to mitigation (MTTM) is going down."

"the rate of project completion is sharply up along with our coding volume."

"A self-driving engineering team can ship more, while raising quality at the same time."

### Agent of Agents and Loops

"When engineers find ways to generate loops, sending a fleet of agents off to complete a verifiable task, we see the most dramatic change. Every employee gets access to a manager agent that can spawn multiple agents, enabling orchestration of agents working in loops on your behalf."

"Loops resulted in some very unique looking PR graphs..."

"One Engineer completed a long stalled migration of our CSS system... Another engineer automated a migration that enabled us to localize the product. Yet another automated flaky test maintenance. Our CTO finally cracked one of our hardest networking bugs related to PSC and fd shutdown with a swarm of agents."

"The most exciting self-driving example comes from our AI team. They built a [system] that analyzes user feedback, proposes improvements, and uses a combination of benchmarks and A/B tests to validate the wins. Replit Agent is self improving!"

### Build vs Buy

"Our internal agent now outperforms products we test that are seen as market leading. We just churned a seven-figure SaaS solution because our internal app, built entirely in Replit, was superior and employees had migrated over."

"A tool to help engineers triage alerts and root cause incidents came back with similar quality but at 10x the cost of running it on our agent. A tool that runs automated penetration testing found fewer vulnerabilities than our internal version at 10x higher cost."

### Beyond Engineering

"Usage spread quickly out of Engineering, mostly because of a Slack interface."

"data team... gave the agent a semantic layer over our data warehouse... Now anyone at Replit can ask business intelligence questions and get a reliable answer. They can build charts and presentations from live data (including every chart in this post). The data team spends its time going deeper on the hardest problems, instead of fielding requests."

"Sales... uses the agent to find and enrich product qualified leads... Account executives use it to prepare for customer conversations... This is all then packaged up into branded slides customized to the account."

"marketing team can use the agent to draft product specs from scratch with a single prompt, based on conversations and documents products across engineering and product."

"support team gave the agent skills to investigate issues and follow standard playbooks... A self-driving support team closes the hardest tickets (those escalated to humans) 60% faster."

"In every example, the human didn't get automated out. They got promoted. Self-driving turns doers into directors, and the people thriving are the ones who think in outcomes and set direction. That is the most valuable work there is now."

### Context from X Post

The X post by @amasad (Amjad Masad) links directly to the article with the text: "https://t.co/9ujCmLs3lQ" (shortened link to the blog post). Posted around 5:07 PM · Jul 16, 2026, with 1.2M Views and 98 replies noted in the snapshot.

Replit context: Replit is the world's leading online programming environment and community. Amjad Masad is Jordanian American entrepreneur and engineer, previously at Facebook (JavaScript infrastructure) and founding engineer at Codecademy.

## Related Concepts Noted (Raw Sources)

- Self-driving company: Organizational model where AI agents handle execution loops, humans set direction and exercise judgment.
- Agent swarms / fleets / loops: Orchestration of multiple agents for verifiable tasks, "agent of agents".
- Loop engineering: Generating closed-loop agent workflows for migrations, testing, bug fixing, self-improvement.
- Internal agent harness: Custom system using microVMs, remote filesystem, access policies, token proxies, audit logging, ZeroTrust.
- Cross-functional adoption: From engineering to data (semantic layer, BI self-serve), sales (lead enrichment, account prep), marketing (spec drafting), support (triage/playbooks).
- Productivity without tradeoffs: Code output up, review latency flat, quality stable/improved, project completion up.
- Build vs buy shift: Internal agents outperforming commercial tools at lower cost.
- Self-improving systems: AI team agents validating improvements via benchmarks/A/B tests.
- Democratization intent: Planning to extend to users with policy, permissions, security, cost controls.

No additional external articles or discussions synthesized here. Sources limited to the primary Replit blog post and associated X/LinkedIn references.