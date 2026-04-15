---
title: "Google Stitch: Premium Results Strategy"
date: 2026-04-01
source: https://x.com/stitchbygoogle/status/2039025289653846256
presenter: David East (Google)
type: research
tags: [stitch, design, prompt-engineering, design-systems]
---

# Google Stitch: Premium Results Strategy

Official Stitch guidance from David East on consistently getting premium results. The core thesis: Stitch is a design tool, not a replacement for the design process. You get the best results when you act as Creative Director.

## The Creative Director Mindset

"Coding agents are really good at writing code, and they can be even more effective if you play the role of their tech lead. Stitch is really good at designing, and it can be even more effective when you act as the creative director."

Without direction, Stitch produces generic results. With direction, it produces designs that feel intentional.

## Strategy 1: Start with Empathy, Not Aesthetics

The first thing to think about is NOT color, typography, or layout. It's empathy.

- Who is this for?
- What do you want them to feel?

**Common mistake:** Describing ideas with abstract words like "make it look good" or "high end." There's not enough direction.

**Better approach:** Describe what the thing actually looks, feels, and reminds you of.

**Example:** For a Washington DC site:
- ❌ "patriotic" or "monumental" (generic)
- ✅ "neoclassical, marble columns, wide open plazas, the feeling of standing in the Jefferson Memorial"

## Strategy 2: Use Design Language, Not Abstract Words

Stitch builds from concrete aesthetic descriptions, not vague adjectives.

**The technique:** Ask Gemini (or any LLM) to help translate your feeling into design language.

Example prompt to Gemini: "Help me write a prompt using design concepts and aesthetic descriptions to establish a creative direction. I'm thinking about the prestige of the Boston Marathon, colors that are historic in running, like the clay of an old track."

Gemini returns language like:
- "architectural limestone"
- "ink on paper"
- "high-end stationery"

These are words you wouldn't know to use on your own, but they're exactly what Stitch can build from.

**New feature: Prompt Enhancer** (under the '+' menu). Does this translation for you. Teaches design language and swaps abstract words for tangible aesthetic descriptions.

## Strategy 3: Color as Hierarchy, Not Palette

Don't think of the four design system colors as a matching palette. Think of them as a hierarchy where each color has a job based on visual weight.

| Role | Coverage | Job | Example |
|---|---|---|---|
| **Neutral** | 80-90% of screen | The canvas | Warm architectural limestone (nudge hue toward orange) |
| **Primary** | Core content | The ink: headings, body text | Dark asphalt (good contrast against warm canvas) |
| **Secondary** | Supporting | More subdued so primary keeps focus | Muted complement |
| **Tertiary** | Accent (least used) | The call to action, the loudest but used least | Clay red, earthy track color |

"Third in volume, but first in visual pull."

**Practical tip:** Modify colors manually in the design system. Nudge the hue wheel, don't just accept defaults. For warmth, push toward orange. For asphalt, drop to dark neutral.

## Strategy 4: Typography with Intent

Font hierarchy: Headline, Body, Label.

**David's approach for the marathon site:**
- **Headline + Body:** Public Sans. Feels official but round and friendly. Gives "prestigious journal, but approachable."
- **Label:** Space Grotesk. "Looks like a timestamp, very official." Great for labels, code, timestamps. Keep it out of headlines.

**David's editorial opinion:** Space Grotesk is fantastic in labels. It is not great for headlines. Stitch will sometimes generate headlines with it. You can't stop it. Just know this and adjust.

**Corner radius decision:** This is a "you gotta decide" moment. Round = approachable/friendly. Sharp = stationery/formal. For the marathon site, David leaned toward slight rounding for approachability.

## Strategy 5: Layout as Physical Object

When stuck on layout, think about the physical application: "If my website was a book, what kind of book would it be?"

**Marathon site → Coffee table book:**
- Full page imagery
- Dense information
- Editorial headings
- On the web, this maps to a **lookbook layout**

**Using variants for layout exploration:**
- **Refine:** Just a little change
- **Explore:** Sweet spot for meaningful variations
- **Reimagine:** "Buckle up. It goes places."

Example variant prompt: "Explore an editorial lookbook layout. I want big editorial headings over images, like a luxury travel magazine."

## Strategy 6: Imagery with Specificity

Generic imagery kills good design. Be specific about what you want.

Example variant prompt for imagery: "Focus on major marathon cities. Use major marathon city images that convey scale and grandeur. Use minimalist cinematic photography of road race courses. Avoid cliche runners on the road images."

## Strategy 7: Real Copy Changes Everything

Even with perfect aesthetics, generic AI copy makes a site feel like a template.

**The approach:** Use a copywriting agent skill.

1. Install the copywriting skill from skills.sh (by Corey Haynes)
2. Provide app context + design.md as input
3. LLM generates copy in the right voice
4. Review and edit (the agent provides a reviewable document)
5. Paste final copy into a Stitch variant prompt

"Target layout, images, and text content only" and paste in the real copy. The site stops feeling like a template.

**Alternative for non-developers:** Copy the skill's markdown content and paste it into Gemini with your context. Similar results without CLI tools.

## Strategy 8: design.md as Portable Creative Direction

The design.md contains all established direction. You can:

1. **Copy it to a new Stitch project** to start with the same aesthetic
2. **Send it to Gemini** with a new app idea to generate a new design.md in the same style
3. **Share it** as a creative brief that works for both humans and agents

David shared his polished design.md as a reference template. It can be used as a base for other projects.

## The Complete Process

1. **Empathy**: Who is the site for? How should they feel?
2. **Creative Direction**: Translate feelings into design language (use Prompt Enhancer or Gemini)
3. **Color Hierarchy**: Neutral (canvas) → Primary (ink) → Secondary (subdued) → Tertiary (accent)
4. **Typography**: Choose fonts that match the emotional intent
5. **Layout**: Think physical objects. Use variants to explore.
6. **Imagery**: Be specific about cities, moods, photography styles
7. **Copy**: Use real copywriting, not AI defaults. Agent skills or Gemini.
8. **Iterate**: Use design.md to carry direction into new projects

"Stitch does not replace the design process. It's a design tool and the best designs come from thought, understanding your content, and setting a creative direction."

## New Features Mentioned

- **Prompt Enhancer** (under '+' menu): Translates abstract words into Stitch-optimized design language
- **Variants**: Refine/Explore/Reimagine creativity levels with custom prompts
- **Design system manual editing**: Full control over colors, fonts, corner radius
- **"Update to latest design system"**: Right-click to apply design system changes to existing screens
- **Preview mode** (Shift+P): Responsive viewer for scrolling through designs
- **Copy-targeted variants**: Paste real copy into variant prompts to replace generic text

## Next Video Preview

David will cover exporting screens as code, the design-to-development handoff.
