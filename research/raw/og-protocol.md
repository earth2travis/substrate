# Open Graph Protocol: Research Notes

_Consolidated from Feb 18 research session. Issues #230 and #231._

## Objective

Implement dynamic Open Graph metadata and per post OG images for the Transmissions blog (sivart-transmissions.orbiter.website).

## Key Resources

- **Protocol spec:** https://ogp.me/
- **Vercel OG image generation:** https://vercel.com/docs/og-image-generation
- **Slack unfurling docs:** https://docs.slack.dev/messaging/unfurling-links-in-messages/
- **Implementation guide:** https://www.opengraph.xyz/blog/how-to-implement-dynamic-open-graph-images

## Core Findings

1. **Dynamic generation preferred over static images.** Each blog post should have a unique, programmatically generated OG image rather than a shared default.
2. **Cross platform compatibility is essential.** OG tags render differently across Telegram, Twitter/X, Discord, Slack, and iMessage. Each has nuances.
3. **Performance and caching matter.** Real time generation adds latency; aggressive caching or pre generation mitigates this.
4. **Branding consistency.** Generated images should maintain visual identity across all posts.

## Technology Options

| Approach                  | Pros                              | Cons                       |
| ------------------------- | --------------------------------- | -------------------------- |
| **Satori (Vercel OG)**    | JSX to SVG, fast, well documented | Vercel ecosystem coupling  |
| **Cloudinary**            | CDN built in, transformation API  | External dependency, cost  |
| **Custom Playwright**     | Full control, any HTML/CSS        | Heavier, slower generation |
| **Hybrid pre generation** | Best performance, static output   | Build step complexity      |

## Implementation Strategies

- **Static pre generation with dynamic metadata:** Generate images at build time, embed metadata per post. Best for Astro/Orbiter stack.
- **On demand generation with caching:** Generate on first request, cache aggressively. Better for frequently updated content.
- **Hybrid:** Pre generate for published posts, on demand for previews/drafts.

## Platform Specific Notes

- **Telegram:** Caches OG images aggressively. Use unique URLs per revision.
- **Twitter/X:** Requires `twitter:card`, `twitter:image` meta tags in addition to OG.
- **Discord:** Respects standard OG tags. Embeds automatically.
- **Slack:** Uses OG tags for unfurling. See their docs for edge cases.
- **iMessage:** Renders OG previews in link bubbles.

## Next Steps

- [ ] Evaluate Satori for Astro integration (likely best fit)
- [ ] Design OG image template matching Transmissions branding
- [ ] Implement OG meta tags in Astro layout
- [ ] Test across all target platforms
- [ ] Set up caching strategy

## Related

- Issue #230: Research Open Graph protocol best practices
- Issue #231: Implement OG metadata and images for blog
- Decision doc: `decisions/2026-02-18-og-research.md`
