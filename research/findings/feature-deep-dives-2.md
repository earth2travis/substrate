---
title: "GitHub Feature Deep Dives Part 2: Rulesets, Reviews, Pages, Wikis, Security"
tags: [research, github, governance, security, deployment]
related: [github-as-knowledge-graph, workflow-as-contract, agent-native-operations, kanban-doctrine]
source: "Feature Deep Dives 2 research"
---

# GitHub Feature Deep Dives Part 2

## Summary

Analysis of GitHub Team plan governance and security features. Part 2 covers Repository Rulesets, PR reviewers, Draft PRs, CODEOWNERS, Pages, Wikis, Environment Deployment Branches, Packages, Scheduled Reminders, Security Overview, and Advanced Security add-ons.

## Key Concepts

**Repository Rulesets (Team):**
Named, layered rule configurations. Up to 75 rulesets per repo. Supports bypass permissions. Can be Active, Evaluate (audit), or Disabled. Key advantage over branch protection: multiple rulesets layer, statuses without deletion, push rules restrict file paths/extensions/sizes across fork network.

**Required PR Reviewers (Team unlock for private repos):**
Specify exact number of required reviews. Team PR reviewers allow assigning entire teams. Agentic application: human oversight on critical repos, agent peer review (agent-koda reviews agent-sivart), tiered review requirements.

**CODEOWNERS (Team unlock for private repos):**
Maps file patterns to responsible users/teams. Auto-requests review when files modified. Agentic mapping: agent-koda owns `/architecture/`, agent-sivart owns `/operations/`, earth2travis owns `/decisions/`.

**Environment Deployment Branches:**
Define deployment targets with protection rules. Restrict branches, require manual approval, environment-specific secrets. Recommended: development (auto), staging (auto), production (manual approval by earth2travis).

**Advanced Security Add-ons:**
- Secret Protection ($19/active committer): push protection blocks commits with detected secrets
- Code Security ($30/active committer): CodeQL scanning, dependency review

## Applications

Governance infrastructure for agent factory: rulesets protect main branch, CODEOWNERS map agent domains, environment secrets isolate credentials, Secret Protection prevents accidental token commits. [[github-as-knowledge-graph]] [[agent-native-operations]] [[deployment-governance]]
