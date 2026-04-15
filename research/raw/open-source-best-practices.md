# Open Source: History, Philosophy, and Best Practices for Repository Management

A research document for the Sivart project. Written to understand where open source came from, what makes it work, and what we should adopt as a small team building something that could grow.

**Related research:**
- [GitHub and Open Source Best Practices](github-practices/overview.md) (branching, commits, PRs, labels)
- [GitHub Project Management Best Practices](github-project-management/best-practices.md) (projects, milestones, workflow)
- [Issues Best Practices](github-project-management/issues-best-practices.md)

---

## Part 1: The History of Open Source

### Before the Name

The story begins before the term "open source" existed. In the 1960s and 1970s, software was shared freely among researchers. The notion of proprietary software would have seemed bizarre to the academics passing tapes between universities. Software was an appendage of hardware; you bought the machine, the code came with it, and you modified it to suit your needs.

That changed in the late 1970s and early 1980s. As the personal computer revolution made software independently valuable, companies began restricting access to source code. Bill Gates's 1976 "Open Letter to Hobbyists" is the canonical marker: software as intellectual property, copying as theft.

### The Free Software Movement

Richard Stallman watched this enclosure happen from inside MIT's AI Lab. When a printer driver went proprietary and he could no longer fix a paper jam in code, something crystallized. In 1983 he announced the GNU Project: a complete free operating system. In 1985 he founded the Free Software Foundation (FSF) and published the GNU Manifesto.

Stallman defined "free software" through four freedoms:

0. The freedom to run the program for any purpose.
1. The freedom to study and modify the source code.
2. The freedom to redistribute copies.
3. The freedom to distribute modified versions.

The GNU General Public License (GPL), first released in 1989, encoded these freedoms legally. Its copyleft mechanism was ingenious: you can do anything with the code, but derivatives must carry the same freedoms forward. The license weaponized copyright against itself.

By the early 1990s, GNU had most of an operating system: compiler (GCC), editor (Emacs), shell (Bash), utilities. Everything except the kernel.

### The Cypherpunk Thread

Running parallel to the free software movement was a less visible but equally radical current. In 1992, Eric Hughes, Tim May, and John Gilmore began gathering cryptographers, mathematicians, and hackers in the Bay Area. Judith Milhon named them "cypherpunks," a play on cyberpunk and cipher. Their mailing list became a crucible for ideas that would reshape the world.

Eric Hughes published "A Cypherpunk's Manifesto" in 1993: "Privacy is necessary for an open society in the electronic age." Tim May's "Crypto Anarchist Manifesto" (1992) went further, envisioning cryptographic tools as instruments of liberation from state power. Their motto was blunt: "Cypherpunks write code."

This was not armchair philosophy. The cypherpunks built anonymous remailers, created PGP distribution networks, and debated digital cash systems years before Bitcoin existed. The mailing list was unmoderated, chaotic, and generative. Ideas were tested by argument, then by implementation. The culture insisted that working code trumps elegant theory.

The line from cypherpunks to Bitcoin to Ethereum to the broader crypto ecosystem is direct and unbroken. Our project carries this DNA.

### Linux and the Cathedral Versus the Bazaar

In 1991, a Finnish student named Linus Torvalds posted a message to comp.os.minix: "I'm doing a (free) operating system (just a hobby, won't be big and professional like gnu)." Linux filled the kernel gap. GNU/Linux became the first complete free operating system, and it spread like fire through universities and then into server rooms.

What made Linux remarkable was not just the code but the development model. Eric Raymond captured this in his 1997 essay "The Cathedral and the Bazaar." The cathedral model: careful, centralized development behind closed doors, releasing polished versions (think GNU Hurd). The bazaar model: release early, release often, delegate everything, let a thousand contributors iterate in the open.

Raymond's key insight: "Given enough eyeballs, all bugs are shallow." He called it Linus's Law. The bazaar worked not despite its chaos but because of it. More eyes meant more perspectives, faster bug discovery, broader testing.

### The Term "Open Source"

By the late 1990s, free software had a perception problem. "Free" confused people (free as in freedom, not free as in beer). The philosophical intensity of Stallman's vision alienated pragmatic business interests. In February 1998, Christine Peterson coined the term "open source" at a strategy session in Palo Alto. The Open Source Initiative (OSI) was founded the same month, with Raymond and Bruce Perens leading the effort.

The rebranding was deliberate. "Open source" emphasized the practical development methodology over the moral philosophy. It was a pitch to business: this model produces better software. Stallman never accepted the rebrand, viewing it as a dilution of the ethical core. That tension between pragmatism and principle persists to this day.

### Inflection Points

**Apache (1995).** The Apache HTTP Server, born from patches to the NCSA httpd server ("a patchy server"), became the backbone of the early web. The Apache Software Foundation (ASF), incorporated in 1999, pioneered the foundation governance model. The Apache License was permissive rather than copyleft: use the code however you want, just give attribution. This became the template for corporate friendly open source.

**SourceForge and collaborative hosting (1999).** Before SourceForge, contributing to an open source project meant navigating mailing lists, FTP servers, and patch files. SourceForge provided centralized hosting, bug tracking, and download mirrors. It was the first platform to lower the barrier to participation at scale.

**Bitcoin (2008).** Satoshi Nakamoto published the Bitcoin whitepaper on the cypherpunks mailing list's spiritual successor, the cryptography mailing list. The first software was released January 2009. A pseudonymous founder, no company, no foundation, no venture capital. Just a whitepaper, working code, and an idea whose time had come. Bitcoin proved that open source could birth not just software but an entire monetary system. Satoshi's disappearance in 2010 was itself a governance act: by leaving, the founder ensured the project could never be captured by a single person.

**GitHub (2008).** GitHub did not invent Git (Linus Torvalds did, in 2005, for Linux kernel development). But GitHub turned distributed version control into a social network. The pull request model, forking, issue tracking, profile pages, contribution graphs: GitHub made open source participation visible and social. The "fork and pull" workflow became the universal pattern. By 2012, GitHub was the center of gravity for open source. Its acquisition by Microsoft in 2018 for $7.5 billion was both a vindication and an irony: the company once called open source "a cancer" now owned its primary platform.

**Ethereum (2015).** Vitalik Buterin, a teenager when he published the Ethereum whitepaper in late 2013, proposed a blockchain that could run arbitrary programs. A "world computer." The Ethereum Foundation provided early governance, but the project's real innovation was the EIP (Ethereum Improvement Proposal) process and the radical experiment of The DAO fork in 2016, where the community chose to rewrite history to undo a hack. That decision split the chain (Ethereum and Ethereum Classic) and proved that governance in decentralized systems is never purely technical; it is always political.

**Node.js and npm (2009 onwards).** Node.js demonstrated that open source could be an ecosystem, not just individual projects. npm, its package manager, created a dependency graph of hundreds of thousands of packages. This revealed both the power and fragility of open source: a single developer unpublishing a small package (the left-pad incident of 2016) could break thousands of projects downstream.

### The Evolution of Governance Models

Open source governance has evolved through several recognizable patterns.

**Benevolent Dictator for Life (BDFL).** The earliest model. One person makes final decisions. Linus Torvalds for Linux, Guido van Rossum for Python (until his retirement from the role in 2018). The BDFL model works when the dictator has good judgment and the community trusts them. It breaks when the dictator burns out, makes unpopular decisions, or simply becomes a bottleneck.

**Pseudonymous founder, then disappearance.** Bitcoin's unique contribution to governance theory. Satoshi created the system, guided its early development, then vanished. The project continued without a leader because the protocol itself encoded the rules. This model only works when the system's rules are sufficiently clear and self enforcing. It is governance by architecture rather than authority.

**Meritocracy.** Contributors earn authority through demonstrated competence. The Apache Software Foundation formalized this: contributor to committer to PMC member, each step requiring community recognition. In theory, the best ideas win regardless of who proposes them. In practice, meritocracy can reproduce existing power dynamics; those with more time, resources, and social capital advance faster.

**Foundation led governance.** The Linux Foundation, Apache Software Foundation, Ethereum Foundation, and Eclipse Foundation provide legal structure, trademark management, and governance frameworks. Foundations add legitimacy and longevity: projects outlive individual maintainers. They also add bureaucracy and can be influenced by their corporate sponsors.

**Rough consensus and running code.** The IETF's principle, adopted by many crypto projects. No formal voting. Discussion continues until disagreements narrow to a manageable set, then the chair (or in decentralized projects, the community) judges whether rough consensus exists. "We reject kings, presidents, and voting. We believe in rough consensus and running code." This ethos permeates Bitcoin Core development.

**Corporate backed open source.** A single company drives development, accepts contributions, and controls the roadmap. React (Meta), Angular (Google). This model produces well funded, well maintained software but creates dependency on the sponsoring company's strategic interests. License changes (the Redis and HashiCorp relicensing controversies of 2023 and 2024) revealed the tension: communities built around corporate open source discovered they had built on someone else's land.

### The Philosophical Underpinnings

Four philosophical currents run through this history.

**The ethical argument (Stallman).** Software freedom is a moral imperative. Users deserve to control the software they use. Proprietary software is an injustice regardless of its quality. The GPL exists to guarantee freedom, not to be convenient for businesses.

**The pragmatic argument (Raymond).** Open source is a superior development methodology. More eyeballs, faster iteration, better code. The license is a tool, not a statement of values. Choose whatever license gets the most people using and contributing to your software.

**The cypherpunk argument (Hughes, May, Finney).** Code is speech. Cryptography is a human right. Systems should be designed so that trust is minimized and individual sovereignty is maximized. You do not ask permission to deploy freedom; you build it and release it. The state will try to stop you. Build anyway.

**The commons argument (Ostrom and beyond).** Open source is a commons: a shared resource governed by community norms. Elinor Ostrom's principles for governing the commons (clear boundaries, collective choice arrangements, monitoring, conflict resolution) map surprisingly well onto successful open source governance. The tragedy of the commons (maintainer burnout, free rider corporate users) is the perpetual threat.

Our project sits at the intersection of the cypherpunk and commons traditions. We build in the open because it produces better work and because the street finds its own uses for things. "May all beings be free" is our version of the cypherpunk imperative, expanded beyond privacy to encompass all forms of liberation.

---

## Part 2: Best Practices for Repository Management

Our existing research in [GitHub Practices](github-practices/overview.md) and [GitHub Project Management](github-project-management/best-practices.md) covers branching, commits, PRs, labels, and project boards in depth. This section synthesizes those findings and expands into areas not yet covered.

### Community Standards Files

A well maintained repository communicates expectations before anyone reads a line of code. GitHub's Community Standards checklist identifies the essential files:

**README.md.** The front door. Should answer: what is this project, why does it exist, how do I use it, how do I contribute? A good README respects the reader's time. Lead with what the project does, not its history. Include installation instructions, a quick start example, and links to deeper documentation. The best READMEs carry the project's soul. Stallman's GNU Manifesto functioned as a README for the free software movement. Satoshi's whitepaper was Bitcoin's README before the repository existed. A README that only explains mechanics without conveying purpose is a missed opportunity.

**CONTRIBUTING.md.** The contributor's map. How to set up the development environment, how to submit changes, what standards to follow, what to expect from the review process. Our existing research covers this well. The key principle: reduce friction for first time contributors without sacrificing quality standards. Bitcoin Core's CONTRIBUTING.md is notably explicit: "there is no particular concept of 'Bitcoin Core developers' in the sense of privileged people." That sentence does more governance work than most GOVERNANCE.md files.

**CODE_OF_CONDUCT.md.** Sets behavioral expectations. The Contributor Covenant is the de facto standard, adopted by projects from Kubernetes to Rails. It signals that the project takes community health seriously. For a two person team, it might seem premature, but it establishes the culture before the culture needs enforcing.

**SECURITY.md.** How to report vulnerabilities. Should include: what to report, where to report it (never in public issues), expected response time, and the disclosure policy. GitHub supports a private vulnerability reporting feature that pairs well with this file. For crypto adjacent projects, security is existential, not optional.

**LICENSE.** Non negotiable. Without a license, the code is technically "all rights reserved" regardless of where it lives. Choose deliberately. MIT and Apache 2.0 for maximum adoption. GPL for copyleft protection. Our choice should reflect our values around freedom and reuse.

**SUPPORT.md.** Where to get help. Distinguishes between bug reports (issues), feature requests (issues or discussions), and general questions (discussions, community channels). Prevents issue trackers from becoming support forums.

**FUNDING.yml.** GitHub Sponsors integration. Even if not immediately relevant, it signals sustainability thinking.

### Issue and PR Templates

Templates enforce consistency without requiring memory. Our [GitHub Practices research](github-practices/overview.md) covers PR templates by type (docs, feature, fix, chore). For issues, the key templates are:

**Bug report.** Steps to reproduce, expected behavior, actual behavior, environment details. The more structured, the fewer rounds of clarification.

**Feature request.** Problem statement, proposed solution, alternatives considered. Forces the proposer to think before typing.

**Blank issue.** Always include an escape hatch. Not everything fits a template.

GitHub's issue forms (YAML based) provide dropdown fields, required sections, and validation. They are superior to markdown templates for structured input.

### Branch Protection and Review Processes

Branch protection on main is non negotiable. At minimum:

- Require pull request reviews before merging.
- Require status checks to pass.
- Require linear history (rebase or squash merging).
- Restrict who can push directly.

For a human plus AI team, review is where trust is built. Every PR gets eyes, whether the author is human or machine. The review is not just gatekeeping; it is knowledge transfer. The reviewer learns what the author did. The author learns what the reviewer values.

Our existing branch protection configuration and review process are documented in [GitHub Practices](github-practices/overview.md). The addition worth making: automated checks that catch what humans miss (linting, formatting, type checking, security scanning).

### CI/CD Integration

Continuous integration should be invisible until something breaks. The pipeline:

1. **On every PR:** Lint, format check, type check, tests.
2. **On merge to main:** Build, test, deploy (if applicable).
3. **On schedule:** Dependency updates (Dependabot or Renovate), security scanning.

The principle: fast feedback. A contributor should know within minutes whether their change is sound. Slow CI kills contribution velocity.

### Release Management and Versioning

Semantic Versioning (SemVer) is the standard. MAJOR.MINOR.PATCH. Our [GitHub Practices research](github-practices/overview.md) covers this in detail.

For changelog management: automated generation from conventional commits is the way. Tools like `release-please` or `standard-version` create changelogs and version bumps from commit history. The conventional commit format we already use makes this nearly free.

### Documentation Standards

Documentation lives as close to the code as possible. The hierarchy:

1. **Inline comments:** Why, not what. The code says what; comments explain decisions.
2. **README.md:** Quick orientation and getting started.
3. **docs/ directory:** Architecture decisions, guides, deep dives.
4. **External docs site:** When the project outgrows a directory. GitHub Pages or similar.

Our decision journal framework, guides directory, and research directory already embody this principle. The gap is a formal documentation style guide and a process for keeping docs current as the codebase evolves.

### Governance Documents

**GOVERNANCE.md.** How decisions are made. Who has what authority. How authority is earned. For a two person team, this might seem like overkill. It is not. Governance is not about bureaucracy; it is about transparency. Writing down how decisions are made prevents implicit assumptions from becoming invisible power structures.

For our scale, governance can be simple: decisions logged in the decision journal, major changes discussed before implementation, the human has final authority with the AI as a full partner in deliberation. As we grow, the governance document grows with us.

---

## Part 3: Case Studies

Three projects chosen for resonance with our identity. Each embodies values, not just process. Each changed the world with a small team or a radical idea. Each has something to teach us about how to run a repository that reflects what you believe.

### GNU: The Manifesto as Architecture

**What they are.** The GNU Project, launched by Richard Stallman in 1983, aimed to create a complete free operating system. It produced GCC, Emacs, Bash, and the GPL license. More than software, GNU was a political act. The GNU Manifesto (1985) was simultaneously a technical proposal and a moral argument. It declared that software should be free and that hoarding code was antisocial.

**Governance model.** BDFL in its purest form. Stallman led with moral authority, not corporate authority. He did not merely manage the project; he defined the philosophy that gave the project meaning. Every technical decision was filtered through an ethical lens: does this increase or decrease user freedom? The FSF provided institutional structure, but Stallman was the soul.

**What makes it remarkable.** GNU proved that a manifesto can be a founding document for a software project. The GNU Manifesto was not a README in the conventional sense, but it functioned as one for the movement. It told you what the project was, why it existed, and what it demanded of you. The four freedoms became a constitution. The GPL became enforceable law.

The project also demonstrated the limits of the BDFL model. Stallman's uncompromising stance produced the GPL (a gift to the world) and also produced interpersonal conflicts that eventually led to his departure from the FSF in 2019 and complicated return. The soul of a project and the personality of its leader are not the same thing, even when they appear inseparable for decades.

**What we can learn.** Write your values into your founding documents. Our SOUL.md already does this. The lesson is to let that document influence technical decisions, not just sit in the repo as decoration. When we face a choice between convenience and our values (freedom, sovereignty, transparency), the values should win. GNU also warns us: the leader's vision must be separable from the leader's person. Document the philosophy so it outlives any individual contributor.

### Bitcoin: Governance by Disappearance

**What it is.** Bitcoin is a peer to peer electronic cash system, described in a nine page whitepaper published by the pseudonymous Satoshi Nakamoto on October 31, 2008. The first software was released January 3, 2009. Satoshi participated in development for roughly two years, then vanished. No goodbye, no succession plan, no foundation (initially). Just silence.

The Bitcoin Core repository on GitHub is the reference implementation, maintained by a small group of maintainers with commit access. There is no CEO, no board, no formal hierarchy. The CONTRIBUTING.md states plainly: "there is no particular concept of 'Bitcoin Core developers' in the sense of privileged people."

**Governance model.** Bitcoin's governance operates on multiple layers simultaneously. At the protocol level, changes require near universal consensus because any controversial change risks a chain split (as demonstrated by the Bitcoin/Bitcoin Cash fork of 2017). The BIP (Bitcoin Improvement Proposal) process, modeled after Python's PEPs, provides structure for proposing changes. BIPs are submitted as pull requests to the bitcoin/bips repository. They go through Draft, Proposed, and Final stages, with community discussion happening on mailing lists, IRC, and GitHub.

At the repository level, a handful of maintainers (historically five to seven people) have merge access. But merge access is not authority in the traditional sense. Maintainers merge what has reached rough consensus; they do not decide what should be merged. The review process is deliberately slow. Changes to consensus code require extraordinary scrutiny. "Move fast and break things" is the antithesis of Bitcoin development culture, because the thing you might break is other people's money.

Satoshi's disappearance was the most important governance decision in the project's history. By leaving, the founder ensured that Bitcoin could never be "Satoshi's project." It became everyone's and no one's. The protocol's rules, encoded in software, became the authority. This is governance by architecture: the system's design constrains behavior more effectively than any human leader could.

**What we can learn.** First, the power of a whitepaper. Bitcoin's founding document is nine pages. It is clear, precise, and complete. It does not explain every implementation detail; it explains the idea. Our project should have an equivalent: a concise document that captures the core vision independent of any particular codebase.

Second, deliberate slowness in critical paths. Not every part of a project needs to move fast. Bitcoin distinguishes between consensus critical code (which changes glacially) and peripheral tooling (which can iterate freely). We should identify our own critical paths and protect them with proportional rigor.

Third, the value of explicit non hierarchy. Bitcoin Core's CONTRIBUTING.md demystifies the power structure by naming it plainly: maintainers exist for practical purposes, not as privileged people. Honesty about how decisions actually get made is better than pretending no hierarchy exists.

### Ethereum: The World Computer and the EIP Process

**What it is.** Ethereum extended Bitcoin's insight (trustless consensus) into a general purpose computation platform. Proposed by Vitalik Buterin in a whitepaper circulated in late 2013, launched in July 2015, Ethereum introduced smart contracts: programs that execute on a decentralized network with no single point of failure or control. The vision was a "world computer" that nobody owns and nobody can shut down.

**Governance model.** Ethereum's governance is offchain, meaning protocol changes are decided through social processes rather than onchain voting. The EIP (Ethereum Improvement Proposal) process is the formal mechanism. Anyone can submit an EIP as a pull request to the ethereum/EIPs repository. EIPs follow a lifecycle: Draft, Review, Last Call, Final. There are different types: Standards Track (protocol changes), Meta (process changes), and Informational.

The stakeholder landscape is deliberately broad. The ethereum.org governance page identifies seven groups: ETH holders, application users, application developers, node operators, EIP authors, validators, and protocol developers (also called "core developers"). No single group has veto power, but all must be considered. Core developers, who maintain the various client implementations (go-ethereum, Nethermind, Lighthouse, Prysm, and others), hold significant practical influence because they write the code that nodes run.

The All Core Developers (ACD) calls, held biweekly, are where protocol changes are discussed and coordinated. These calls are public, recorded, and summarized. The "Ethereum Cat Herders," a volunteer group of project managers, help coordinate upgrades and improve communication between teams.

**The DAO fork (2016)** is the defining governance event. A smart contract called The DAO raised $150 million in ETH, then was exploited through a reentrancy bug. The community faced a choice: accept the hack as the immutable consequence of "code is law," or rewrite history to return the funds. After heated debate, the community chose to fork. Ethereum (the forked chain) and Ethereum Classic (the original chain) went their separate ways. The fork proved that in decentralized systems, governance is ultimately social, not technical. The code does what the community decides the code should do.

Vitalik Buterin occupies an unusual role: not quite BDFL, not quite ordinary contributor. The Ethereum Foundation provides funding and coordination but explicitly avoids dictating protocol direction. Vitalik's influence is real but informal, exercised through blog posts, research papers, and participation in discussions rather than through any formal authority. The community sometimes calls this "rough consensus with Vitalik's gravity."

**What we can learn.** First, the EIP process is a masterclass in structured deliberation. Each proposal has a number, a type, a status, a champion, and a discussion thread. The lifecycle is explicit. This is what our decision journal could evolve toward: numbered proposals with clear statuses, not just records of decisions already made.

Second, public coordination calls. Even for a two person team, periodic recorded discussions about direction and priorities create accountability and a historical record. When the team grows, these recordings become onboarding material.

Third, the multi stakeholder model. Ethereum's governance explicitly names who has a voice and how different perspectives are weighed. As our project grows, we should think about who our stakeholders are and how their interests intersect. Users, contributors, the AI agent itself: each has a perspective worth formalizing.

Fourth, the courage to make hard governance decisions. The DAO fork was messy, controversial, and necessary. When our project faces a values conflict (and it will), having a governance framework that can absorb the shock is better than improvising in the moment.

---

## Part 4: Recommendations for Sivart

Based on this research, here is what we should adopt, mapped to our current state and ordered by impact.

### Immediate (This Week)

1. **Add a CODE_OF_CONDUCT.md.** Adopt the Contributor Covenant. Takes minutes, signals values, establishes culture before it needs enforcing.

2. **Add a SECURITY.md.** Define vulnerability reporting process. Even for a small project, this is table stakes. Enable GitHub's private vulnerability reporting.

3. **Add a LICENSE file.** If not already present, choose and commit. MIT aligns with our values around freedom and simplicity. Consider GPL if copyleft protection matters more.

4. **Create issue templates using YAML forms.** Bug report, feature request, and blank issue. Our existing markdown templates are good; YAML forms add validation and structure.

### Short Term (This Month)

5. **Set up automated CI checks.** Prettier (already used), linting, and any relevant type checking should run on every PR. Fast feedback loop.

6. **Add a GOVERNANCE.md.** Document our decision making process. Simple for now: decisions logged in the journal, major changes discussed first, the human has final authority with the AI as full partner in deliberation. This grows with us.

7. **Write a project vision document.** Following Bitcoin's whitepaper and Ethereum's founding documents, create a concise statement of what Sivart is, why it exists, and what it aims to become. Not a README. A founding document. SOUL.md is close but it describes the AI's identity; we need something that describes the project's identity.

8. **Implement automated changelog generation.** We already use conventional commits. Wire up `release-please` or similar to generate changelogs automatically.

### Medium Term (Next Quarter)

9. **Formalize a proposal process.** Inspired by BIPs and EIPs, create a lightweight proposal format for significant changes. Numbered, typed, with explicit statuses. Our decision journal is the seed; this is the flower.

10. **Add automated stale issue management.** GitHub Actions workflow to warn and close stale issues. Keeps the backlog honest.

11. **Document the human plus AI workflow.** Our collaboration model is novel. Document how it works: who does what, how decisions are made, how review works when one contributor is an AI. This could be valuable to the broader community and to our own clarity.

12. **Publish iteration plans.** Use GitHub issues or discussions to share what we are working on and why. Transparency scales trust.

### Principles to Carry Forward

**Automate the routine, humanize the exceptions.** Every repetitive task is a candidate for automation. Save human judgment for where it matters.

**Document decisions, not just outcomes.** The "why" is more valuable than the "what." Our decision journal is already strong here. Keep going.

**Values first, process second.** GNU, Bitcoin, and Ethereum all succeeded because their governance reflected their values, not just their operational needs. Our governance should do the same.

**Start simple, add complexity only when you feel the pain.** Every successful project we studied started with less process than they have now. They added structure in response to real problems, not anticipated ones.

**Governance is not bureaucracy.** It is transparency. Writing down how decisions are made is not overhead; it is the foundation of trust.

**The founder must be separable from the project.** This is the lesson of both GNU (where inseparability became a liability) and Bitcoin (where separation was a gift). Build the project so its values persist independent of any individual.

---

## Sources and Further Reading

- Stallman, R. "The GNU Manifesto." 1985.
- Hughes, E. "A Cypherpunk's Manifesto." 1993.
- May, T. "The Crypto Anarchist Manifesto." 1992.
- Raymond, E. "The Cathedral and the Bazaar." 1997.
- Perens, B. "The Open Source Definition." 1998.
- Nakamoto, S. "Bitcoin: A Peer to Peer Electronic Cash System." 2008.
- Buterin, V. "Ethereum Whitepaper." 2013.
- Ostrom, E. "Governing the Commons." 1990.
- Bitcoin Core CONTRIBUTING.md: https://github.com/bitcoin/bitcoin/blob/master/CONTRIBUTING.md
- Bitcoin Improvement Proposals: https://github.com/bitcoin/bips
- Ethereum Governance: https://ethereum.org/governance/
- Ethereum Improvement Proposals: https://eips.ethereum.org/
- GitHub Community Standards: https://docs.github.com/en/communities
- Contributor Covenant: https://www.contributor-covenant.org/
- Conventional Commits: https://www.conventionalcommits.org/
- Our GitHub Practices Research: [github-practices/overview.md](github-practices/overview.md)
- Our Project Management Research: [github-project-management/best-practices.md](github-project-management/best-practices.md)
