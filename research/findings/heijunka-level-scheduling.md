---
title: "Heijunka: Production Leveling"
tags:
  - ai-agents
  - knowledge-management
  - lean-manufacturing
  - systems-thinking
related:
  - [[1password-integration]]
  - [[2026-02-14-foundations]]
  - [[2026-02-19-nex-brainstorm]]
  - [[2026-02-20-composable-primitives]]
source: research/raw/heijunka-level-scheduling.md
---

# Heijunka: Production Leveling

**Researched:** 2026-04-12
**Topic:** Heijunka, Toyota Production System, Level Scheduling

---

## I. Overview
**Heijunka** (平準化) is a Japanese term meaning "leveling." In the Toyota Production System, it refers to the practice of smoothing out production to reduce the "Mura" (unevenness) that leads to "Muri" (overburden) and "Muda" (waste). Instead of producing in large batches based on sporadic orders, Heijunka averages the volume and variety of production over a fixed period.

## II. The Heijunka Box
The primary visual tool for this practice is the **Heijunka Box**. It is a grid-based scheduling board:
*   **Rows:** Represent different product types or "families."
*   **Columns:** Represent fixed time intervals (e.g., hours or shifts).
*   **Kanban Cards:** Placed in the slots to signal exactly what should be produced and when.

**The Shift:** Instead of "All Chairs on Monday, All Tables on Tuesday," Heijunka dictates a mix: "Chair, Table, Chair, Chair, Table..." This **interleaving** ensures that the production line is always ready for any product, reducing setup times and keeping the workflow steady.

## III. Leveling by Volume vs. Product Type
1.  **Volume Leveling:** Distributing the *total* number of orders evenly across days to prevent "stop-and-start" cycles.
2.  **Product Leveling:** Distributing *different* product types evenly to minimize the "changeover" pain. At Toyota, they aim for changeovers of under three minutes.

## IV. Benefits of Heijunka
*   **Reduced Inventory:** By producing to a leveled schedule (Just-in-Time), you don't need massive warehouses for large batches.
*   **Predictability:** Upstream processes and suppliers know exactly what is coming, allowing them to level their own work.
*   **Workforce Satisfaction:** It prevents the "crunch time" burnout followed by "idle time" boredom.
*   **Flexibility:** The system can absorb small changes in demand without collapsing the entire schedule.

## V. Relevance to the Agent Factory
Heijunka is the perfect model for **Agent Orchestration**.
*   **The Problem:** Currently, agents likely "batch" their work. Sivart does a month of research, then Koda does a month of coding. This leads to **Mura** (unevenness) and **Muri** (overburden) for our shared memory and your human attention.
*   **The Heijunka Solution:** We should **interleave** our work. instead of "Research Month," we should have a **Heijunka Schedule**: "Strategic Insight, Code Refactor, Strategic Insight, Infrastructure Update."
*   **The Brain-Two Heijunka Box:** Our `brain-two` repo should be the "Box." It should have a leveled schedule of "Strategy" and "Execution" cards, ensuring that our factory is always balanced and never overburdened by a single type of cognitive load.

---

## VI. Sources
- Toyota Motor Corporation: "The Toyota Production System."
- Lean.org: "Heijunka - Production Leveling."
- DuraLabel: "The Heijunka Box: A Visual Scheduling Tool."