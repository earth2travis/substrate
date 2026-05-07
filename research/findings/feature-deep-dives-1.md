---
title: "GitHub Feature Deep Dives Part 1: Discussions, Projects, Actions, Codespaces"
tags: [research, github, project-management, automation]
related: [github-as-knowledge-graph, workflow-as-contract, kanban-doctrine, agent-native-operations]
source: ".github/CODEOWNERS for the-agent-factory research"
---


# GitHub Feature Deep Dives Part 1

## Summary

Analysis of GitHub Free vs Team plan features for agent factory operations. Part 1 covers Discussions, Projects, Actions, and Codespaces.

## Key Concepts

**GitHub Discussions (Free + Team):**
Threaded forum-style conversations with categories, labels, pinning, polls. API-accessible via `gh api` or GraphQL. Recommended categories: Announcements, Decisions, Architecture, Agent Reports, General, Q&A. Agents can post daily/weekly reports as Discussion threads.

**GitHub Projects v2 (Free + Team):**
Kanban boards and table views with custom fields and automations. Cross-repo tracking. Recommended custom fields: Agent (single select), Priority, Domain, Estimated Hours. Built-in automations: auto-add issues from repos, auto-set status on PR merge.

**GitHub Actions (2,000 Free → 3,000 Team minutes):**
CI/CD backbone. Linux 1x, Windows 2x, macOS 10x multiplier. Self-hosted runners: free, no minute consumption. Triggers: push, PR, schedule, workflow_dispatch, repository_dispatch, discussion events.

**GitHub Codespaces (Team unlock):**
Cloud dev environments. Limited direct value for CLI agents. Potential uses: human onboarding, standardized environments, ephemeral workspaces. Free gives 120 core-hours/month personal quota. Team allows org-paid usage.

## Applications

Discussions as primary agent communication channel. Projects as central task management with per-agent filtered views. Actions for agent workflows, automated reviews, cross-repo orchestration. Codespaces for human contributor onboarding. [[github-as-knowledge-graph]] [[workflow-as-contract]]
