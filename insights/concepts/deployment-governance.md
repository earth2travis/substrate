---
title: "Deployment Governance"
tags: [concept, governance, deployment, github]
related: [github-as-knowledge-graph, workflow-as-contract, agent-native-operations, agent-factory-production-system, kanban-doctrine]
---

# Deployment Governance

## Definition

The layered set of rules, approvals, and environmental controls that govern how code, configuration, and agent behavior move from development to production.

## Core Idea

In an agent factory, deployment is not just shipping code. It is releasing capability. Deployment governance ensures that agent behavior changes are reviewed, tested, and reversible before they reach production. The goal is not to slow down agents but to make their autonomy auditable and safe.

## Key Components

**Repository Rulesets**
Named, layered rule configurations that stack. Most restrictive wins. Multiple rulesets can coexist: main branch protection, push safety (file extension/size restrictions), and agent workspace rules (lighter checks for agent branches). Rulesets can be Active, Evaluate (audit mode), or Disabled.

**CODEOWNERS**
Maps file patterns to responsible parties. In an agent factory, this maps agent domains: one agent owns architecture, another owns operations, human founder owns governance. Automatic review assignment ensures the right reviewer sees every change.

**Environment Deployment Branches**
Restrict which branches can deploy to which environments. Require manual approval for production. Store environment-specific secrets separately from repo secrets. Agents auto-deploy to staging; production requires human approval.

**Required PR Reviews**
Tiered review requirements: critical repos need two reviewers (ensuring at least one human or senior agent), agent workspaces need one (peer review). Draft PRs signal work-in-progress and prevent premature merges.

**Secret Protection**
Push protection blocks commits containing detected secrets. Custom patterns for org-specific credentials. Critical when agents handle API tokens and might accidentally embed them in code.

## Applications

**Agent Workspace Isolation**
Each agent gets its own repo or branch space with lighter rulesets. The main factory repo maintains strict protection. This balances autonomy with safety.

**Governance as Code**
Rulesets and CODEOWNERS are version-controlled, reviewable, and auditable. Changes to governance flow through the same PR process as code changes.

**Audit Trail**
Every deployment, approval, and flag change leaves a trace. When an agent makes a mistake, the governance layer shows what was approved, by whom, and when.

## Related

- [[github-as-knowledge-graph]]: GitHub as the institutional memory layer
- [[workflow-as-contract]]: executable process definitions
- [[agent-native-operations]]: agents as first-class operators
- [[agent-factory-production-system]]: Toyota-inspired model for agent operations
- [[kanban-doctrine]]: visualizing and limiting work in progress
