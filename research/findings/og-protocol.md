---
title: Open Graph Protocol Implementation Research
source: research/raw/og-protocol.md
tags:
- open-graph
- meta-tags
- social-sharing
- web
related:
- design-system-as-code
- roundtrip-workflow
---



# Open Graph Protocol Implementation Research

Research on implementing dynamic Open Graph metadata and per-post OG images for the Transmissions blog.

## Core Findings

1. **Dynamic generation preferred over static images.** Each post should have a unique, programmatically generated OG image rather than a shared default.
2. **Cross-platform compatibility is essential.** OG tags render differently across Telegram, Twitter/X, Discord, Slack, and iMessage.
3. **Performance and caching matter.** Real-time generation adds latency; aggressive caching or pre-generation mitigates this.
4. **Branding consistency.** Generated images should maintain visual identity across all posts.

## Technology Options

| Approach | Pros | Cons |
|----------|------|------|
| Satori (Vercel OG) | JSX to SVG, fast, well documented | Vercel ecosystem coupling |
| Cloudinary | CDN built-in, transformation API | External dependency, cost |
| Custom Playwright | Full control, any HTML/CSS | Heavier, slower generation |
| Hybrid pre-generation | Best performance, static output | Build step complexity |

## Platform Notes

- **Telegram**: Caches OG images aggressively. Use unique URLs per revision.
- **Twitter/X**: Requires `twitter:card`, `twitter:image` meta tags in addition to OG.
- **Discord**: Respects standard OG tags. Embeds automatically.
- **Slack**: Uses OG tags for unfurling.
- **iMessage**: Renders OG previews in link bubbles.

## Recommended Strategy

Static pre-generation with dynamic metadata: generate images at build time, embed metadata per post. Best fit for Astro/Orbiter stack.
