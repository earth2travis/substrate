# Insights: The Five Whys for Agentic Intelligence

**Source:** `research/management/the-five-whys-root-cause-analysis.md`
**Extracted:** 2026-04-12

---

## Insight 1: The "Blameless" Agent
The Five Whys teaches us that **human error is always a process error**. For our agents, this means: if Sivart gives a bad answer, it's not because she's "dumb." It's because her **Context Stack** was incomplete or her **Prompt** was misaligned. By focusing on the "Why" of the process, we can build a system that gets smarter without getting "defensive."

## Insight 2: From "What" to "Why"
Most agents focus on the **"What"** (the output). The Five Whys forces a focus on the **"Why"** (the rationale). 
*   **Sivart's Upgrade:** Instead of just providing a summary, she should provide the **Five Whys** of her strategic recommendation. Why this path? Why now? Why these risks?
*   **Koda's Upgrade:** Instead of just fixing a bug, she should document the **Five Whys** of the failure in the PR description. This turns every bug fix into a lesson for the whole factory.

## Insight 3: The "Why-Tree" for Complex Systems
Software failures are rarely linear. They are **trees**. 
*   **Why did the site go down?** (Database overload AND Load Balancer failure).
*   **Why the overload?** (Bad query). **Why the LB failure?** (Config drift).
*   **Strategy:** For complex Agent Factory failures, we must use a **Why-Tree** approach, mapping out multiple causal chains until we find the "common ancestor" root cause.

## Insight 4: The Five Whys as a "Learning Loop" Trigger
Every time we complete a Five Whys analysis, it should **trigger a learning event**:
1.  Update `CONTRACT.md` (if a rule was broken).
2.  Update `TOOLS.md` (if a tool was misused).
3.  Add a new "Skill" to Koda's repertoire (if a new fix was found).
4.  Update Sivart's "Strategic Memory" in `brain-two` (if a strategic gap was found).

---

## Conclusion
The Five Whys is the difference between **fixing a bug** and **fixing the factory**. By embedding this practice into our agents, we ensure that every failure is an investment in future success. We don't just "work through" problems; we **learn through** them.