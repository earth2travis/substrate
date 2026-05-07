---
title: "Prompt Injection Defenses"
tags: [security, agents, prompt-injection, llm]
related:
  - [[agent-security]]
  - [[agent-native-operations]]
  - [[agent-tool-permissions]]
source: research/raw/prompt-injection-defenses.md
---

# Prompt Injection Defenses

Research compiled from IBM, Invariant Labs, ETH Zurich, Google, Microsoft, and Simon Willison's ongoing work.

## Core Principle

**Once an LLM has ingested untrusted input, it must be constrained so it cannot trigger consequential actions based on that input.**

Any exposure to potentially malicious tokens taints the output. An attacker with token injection should be considered to have complete control over textual output, tool calls, and downstream agent behavior.

## Defense Patterns

### 1. Action-Selector Pattern
LLM triggers tools but cannot see or act on responses. An "LLM-modulated switch statement." Use when triggering actions without needing feedback (routing, categorization).

### 2. Plan-Then-Execute Pattern
Plan all tool calls before any exposure to untrusted content. Untrusted content can affect the content of actions but not the choice of actions.

Example: "Send today's schedule to John" → plan: `[calendar.read(), email.write(to=john@...)]`. Calendar content might corrupt email body but cannot change recipient.

### 3. LLM Map-Reduce Pattern
Sub-agents process untrusted content and return structured outputs (booleans, enums, numbers). Coordinator aggregates results without seeing raw content. Use when processing multiple untrusted items (emails, files, documents).

### 4. Dual LLM Pattern (Simon Willison, 2023)
Privileged LLM coordinates but never sees untrusted content. Quarantined LLM returns symbolic variables that privileged LLM can reference without exposure. Use when sophisticated coordination with untrusted data is needed.

### 5. Code-Then-Execute Pattern (CaMeL, Google DeepMind)
Privileged LLM generates code in a sandboxed DSL. The DSL enables full data flow analysis, tracking tainted data through the entire process. Use for complex workflows requiring data flow tracking.

### 6. Context-Minimization Pattern
Remove untrusted content from context after extracting structured data. Prevents injection attempts from surviving into subsequent interactions. Use in multi-turn conversations involving external data.

## Current Attack Surfaces

**Email Processing (HIGH RISK):** Malicious emails containing injection attempts. Classification is read-only but prompts see raw email content.

**Web Fetching (MEDIUM RISK):** Fetched web pages may contain injection attempts. OpenClaw wraps external content with security notices.

**Telegram Messages (LOW RISK):** Only Ξ2T has access to direct chat. Low risk for main session; higher for group chats.

**File Processing (MEDIUM RISK):** Files containing injection attempts. Low risk in trusted workspace; medium for external files.

## Already Protected

1. **OpenClaw external content wrapping:** Web fetch and search results wrapped with `<<<EXTERNAL_UNTRUSTED_CONTENT>>>` markers and security notices.
2. **System prompt safety:** AGENTS.md includes safety principles about not exfiltrating data or running destructive commands.
3. **Action confirmation:** Sensitive external actions require user confirmation.

## To Implement

1. **Email isolation:** Process emails in isolated context, return only structured data.
2. **Homograph detection:** Validate URLs before fetching.
3. **Consequential action audit:** Review all tools that can take external actions.

## References

- Simon Willison's prompt injection tag: https://simonwillison.net/tags/prompt-injection/
- OWASP LLM Top 10: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- Design Patterns for Securing LLM Agents (arXiv 2506.08837)
- CaMeL: Defeating Prompt Injections by Design (Google DeepMind, April 2025)
