# Scraped Primary Sources for Stitch Prompt Skill

## Source 1: Google AI Developers Forum — Official Stitch Prompt Guide
By Vincent_Nallatamby (Google), May 19, 2025. Pinned globally. 161K views, 462 likes.
URL: https://discuss.ai.google.dev/t/stitch-prompt-guide/83844

### 1. Starting Your Project
Choose broad or detailed. For complex apps, start high-level then drill down screen by screen.

- High-Level: "An app for marathon runners."
- Detailed: "An app for marathon runners to engage with a community, find partners, get training advice, and find races near them."

Set vibe with adjectives (influences colors, fonts, imagery):
- "A vibrant and encouraging fitness tracking app."
- "A minimalist and focused app for meditation."

### 2. Refining by iterating screen by screen
Focus on one screen/component, one or two adjustments per prompt.

- "On the homepage, add a search bar to the header."
- "Change the primary call-to-action button on the login screen to be larger and use the brand's primary blue color."
- Product detail page examples with specific style guidance

### 3. Controlling App Theme
Colors: specific or mood-based
- "Change primary color to forest green."
- "Update theme to a warm, inviting color palette."

Fonts & Borders:
- "Use a playful sans-serif font."
- "Make all buttons have fully rounded corners."
- Combined: "Book discovery app: serif font for text, light green brand color for accents."

### 4. Modifying images
Be specific. Use descriptive terms from app content.
- "Change background of [all] [product] images on [landing page] to light taupe."
- "On 'Team' page, image of 'Dr. Carter (Lead Dentist)': update her lab coat to black."

Coordinate with theme changes:
- "Update theme to light orange. Ensure all images and illustrative icons match this new color scheme."

### 5. Changing language
- "Switch all product copy and button text to Spanish."

### Pro Tips
- Be Clear & Concise
- Iterate & Experiment
- One Major Change at a Time
- Use UI/UX Keywords ("navigation bar," "call-to-action button," "card layout")
- Reference Elements Specifically
- Review & Refine

---

## Source 2: Google Blog — "Introducing 'vibe design' with Stitch" (March 18, 2026)
URL: https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/

Key features:
- AI-native infinite canvas
- Start from business objective, user feeling, or inspiration — not wireframes
- Design agent reasons across entire project evolution
- Agent manager for parallel ideas
- DESIGN.md: agent-friendly markdown for exporting/importing design rules across projects and tools
- Interactive prototypes: click "Play" to preview. Auto-generates logical next screens.
- Voice capabilities: speak to canvas for real-time critiques, design via interview, live updates
- MCP server and SDK for tool integration
- Export to Figma, AI Studio, Antigravity

---

## Source 3: dev.to/seifalmotaz — "Stop Generating AI Slop" Developer's Guide
URL: https://dev.to/seifalmotaz/stop-generating-ai-slop-the-developers-guide-to-google-stitch-jen

### Four-Layer Prompt Anatomy
1. Context: Who is this for? (fintech triggers different colors than children's game)
2. Structure: Layout topology (bento grid, sidebar nav)
3. Aesthetic: The "vibe" (vintage, brutalist)
4. Tech Stack: Execution medium (Tailwind CSS, dark mode)

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

### Technical Constraints
- Specify Tailwind, Material Design 3, or responsive behavior explicitly

### Copy-Paste Templates
Template A: High-End E-Commerce ("Cultured")
Template B: Crypto Dashboard ("Retro-Futurist")
Template C: Recipe Journal ("Vintage")
