---
title: "Scraped Primary Sources for Stitch Prompt Skill"
tags: [design, agents, stitch, design-systems, prompts, google]
related:
  - [[design-system-as-code]]
  - [[roundtrip-workflow]]
  - [[skills-as-portable-knowledge]]
  - [[creative-partnership]]
source: research/raw/scraped-sources.md
---

# Scraped Primary Sources for Stitch Prompt Skill

Three sources on Google Stitch prompting, compiled as reference for skill development.

## Source 1: Google AI Developers Forum — Official Stitch Prompt Guide

**Author:** Vincent_Nallatamby (Google), May 19, 2025. 161K views.

### Starting Your Project

Choose broad or detailed. For complex apps, start high-level then drill down screen by screen.

Set vibe with adjectives (influences colors, fonts, imagery): "A vibrant and encouraging fitness tracking app."

### Refining by Iterating Screen by Screen

Focus on one screen/component, one or two adjustments per prompt.

- "On the homepage, add a search bar to the header."
- "Change the primary call-to-action button on the login screen to be larger and use the brand's primary blue color."

### Controlling App Theme

**Colors:** specific or mood-based. "Change primary color to forest green." "Update theme to a warm, inviting color palette."

**Fonts & Borders:** "Use a playful sans-serif font." "Make all buttons have fully rounded corners."

### Modifying Images

Be specific. Use descriptive terms from app content. "Change background of [all] [product] images on [landing page] to light taupe."

Coordinate with theme changes: "Update theme to light orange. Ensure all images and illustrative icons match this new color scheme."

### Pro Tips

- Be Clear & Concise
- Iterate & Experiment
- One Major Change at a Time
- Use UI/UX Keywords
- Reference Elements Specifically
- Review & Refine

---

## Source 2: Google Blog — "Introducing 'vibe design' with Stitch" (March 18, 2026)

Key features:
- AI-native infinite canvas
- Start from business objective, user feeling, or inspiration — not wireframes
- Design agent reasons across entire project evolution
- Agent manager for parallel ideas
- DESIGN.md: agent-friendly markdown for exporting/importing design rules
- Interactive prototypes: click "Play" to preview. Auto-generates logical next screens
- Voice capabilities: speak to canvas for real-time critiques, design via interview, live updates
- MCP server and SDK for tool integration
- Export to Figma, AI Studio, Antigravity

---

## Source 3: dev.to/seifalmotaz — "Stop Generating AI Slop" Developer's Guide

### Four-Layer Prompt Anatomy

1. **Context:** Who is this for? (fintech triggers different colors than children's game)
2. **Structure:** Layout topology (bento grid, sidebar nav)
3. **Aesthetic:** The "vibe" (vintage, brutalist)
4. **Tech Stack:** Execution medium (Tailwind CSS, dark mode)

### Naive vs Expressive

- Aesthetic: "Make it look cool" → "Apply a retro-futurist aesthetic with neon accents, CRT scanline textures, and cyberpunk typography"
- Layout: "Show some photos" → "Arrange images in a bento box grid with varying aspect ratios, rounded corners, and hover-state scaling"
- Color: "Use blue" → "Utilize a monochromatic indigo palette with electric blue highlights and matte black backgrounds"
- Tech: "Make a website" → "Generate a responsive landing page using Tailwind CSS utility classes and glassmorphism card effects"

### Aesthetic Semantics

- Vintage = authenticity, age, texture (paper grain, ink bleed)
- Retro = modern homage (80s synthwave, pixel art)
- "Cultured/Editorial" = high-end, Awwwards-style (maximize whitespace, restrict palette)
- Brutalism/Neubrutalism = ignore conventions (clashing colors, thick borders, hard shadows)

### Layout Semantics

- Bento Box Grid (Apple/Linear style)
- Masonry Layout (Pinterest style)
- Split-screen hero

### Lighting & Materiality

- Glassmorphism: frosted glass, backdrop-filter blur
- Neumorphism: extruded soft plastic
- Cinematic Lighting: dramatic depth

### Copy-Paste Templates

Template A: High-End E-Commerce ("Cultured")
Template B: Crypto Dashboard ("Retro-Futurist")
Template C: Recipe Journal ("Vintage")
