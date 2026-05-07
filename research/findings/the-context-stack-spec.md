---
title: 'The Context Stack: A Universal Specification for Agent Identity'
tags:
- context-engineering
- agent-identity
- knowledge-architecture
- agentic-architecture
- specification
related:
- interchangeable-context
- context-stack-as-conscience
- context-stack-observations
- memory-systems
- agent-identity
source: research/raw/the-context-stack-spec.md
---




# The Context Stack: A Universal Specification for Agent Identity

## Summary

The Context Stack is a four-layer, markdown-based specification for representing individuals and organizations as machine-readable context. It answers the agent blindness problem: every AI agent starts with no knowledge of who it serves, what they value, where they're headed, or how they operate. The four layers are Identity (who), Direction (where), Operations (how), and Intelligence (what). The specification is designed to be human-writable, machine-readable, framework-agnostic, and selectively loadable based on task requirements. It is the foundational architecture that makes agent identity portable, auditable, and composable.

## Key Claims

1. **Markdown as the interchange format.** No proprietary formats, no databases, no APIs required. Portability is non-negotiable.

2. **Layered loading, not monolithic.** An agent doing a quick task reads one or two files. An agent making strategic decisions reads the full stack. Loading tiers range from Tier 0 (Identity only) to Tier 3 (targeted depth).

3. **The stack is the precondition for conscience.** The files provide moral knowledge (VALUES.md, CONTRACT.md), self-awareness (SOUL.md, EXPERIENCE.md), and stop criteria (CONTRACT.md hard boundaries). What the stack does not provide is the comparison engine and signal mechanism: the runtime process that evaluates output against values. That loop is the missing piece.

4. **Agent-to-agent communication via stack exchange.** When two entities interact, they exchange curated subsets of their stacks. The handshake is "read our stack" rather than "let me tell you about us."

5. **Context loading is the new boot process.** The loading strategy is the nervous system. Semantic routing selects which files are relevant to a given decision. Progressive disclosure loads summaries before full content.

## Implications

The Context Stack reframes agent deployment as an assembly problem rather than a craft problem. When context is standardized, agent deployment cost collapses from days of skilled prompt engineering to minutes of file loading. The Context Stack is to agent production what interchangeable parts were to manufacturing: it moves skill from deployment to authorship.

## Related

- [[interchangeable-context]] — Ford's revolution as structural parallel for standardized context
- [[context-stack-as-conscience]] — The five conscience components mapped to Context Stack files
- [[context-stack-observations]] — Living log of insights and test results during spec development
- [[memory-systems]] — Memory architectures that complement or extend the Context Stack
- [[agent-identity]] — Identity as the foundation of agent behavior and trust
