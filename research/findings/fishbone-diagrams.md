---
title: "Fishbone Diagrams: Cause and Effect Made Visible"
tags: [fishbone, ishikawa, root-cause-analysis, quality, visualization, methodology]
related: [[5-whys]], [[kaizen-and-continuous-improvement]], [[the-five-whys-root-cause-analysis]]
source: research/raw/fishbone-diagrams.md
---

# Fishbone Diagrams: Cause and Effect Made Visible

Created by Kaoru Ishikawa in the 1960s at Kawasaki shipyards, the fishbone diagram maps potential causes of a problem across categories. It became one of the Seven Basic Tools of Quality — selected because they are visual, practical, and usable without advanced statistical training.

## Structure and Anatomy

**The Head:** the effect — the problem being investigated, stated specifically
**The Spine:** horizontal line representing the causal pathway
**The Ribs:** major diagonal lines representing cause categories
**Sub Branches:** specific causes within each category, 2-3 levels deep
**Annotations:** evidence markers, priority indicators, verification status

## Cause Categories

**The 5 Ms (Manufacturing):**
- Manpower/Mindpower: training, skill, motivation, cognitive load
- Machine: equipment, tools, technology, infrastructure
- Material: inputs, data, dependencies, specifications
- Method: processes, workflows, procedures
- Measurement: metrics, monitoring, testing, observability

**The 4 Ss (Service):**
- Surroundings: environment, physical space, digital interface
- Suppliers: vendors, partners, API providers
- Systems: procedures, processes, technologies
- Skill: knowledge, training, gaps

**For Software/AI:**
Code, Infrastructure, Data, Process, Monitoring, External Dependencies — or Model, Data, Pipeline, Compute, Monitoring, Human Oversight

## Construction Steps

1. Define the problem precisely (head)
2. Select categories (ribs)
3. Brainstorm causes without judgment
4. Drill into sub-causes (ask "what might be behind this?")
5. Analyze and prioritize (dot voting, data analysis)
6. Document and act (assign owners, set timelines)

## Relationship to Other Methods

- **5 Whys:** fishbone maps breadth (all potential causes); 5 Whys drills depth (single causal chain). Use fishbone first to identify branches, then 5 Whys to drill into them
- **PDCA:** fishbone lives in the "Check" phase
- **Fault tree analysis:** FTA uses Boolean logic for safety-critical systems; fishbone is less rigorous but more accessible
- **FMEA:** fishbone feeds into FMEA by identifying potential failure causes; FMEA adds quantitative risk assessment

## Strengths

- Visual clarity — immediate comprehension
- Breadth of investigation — forces consideration of overlooked categories
- Accessibility — no specialized training required
- Collaborative structure — shared visual space for different disciplines

## Limitations

- No causal logic — doesn't capture how causes interact
- Quality depends on the group — missing expertise means missing causes
- No built-in prioritization — requires additional methods
- Risk of false confidence — a completed diagram reflects assumptions, not necessarily reality
- Cultural prerequisites — requires blame-free environment
