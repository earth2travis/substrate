---
title: "Autonomous Video Production Research"
tags: [finding, video, creative, automation, remotion, runway]
related: [[agent-native-operations]], [[skills-as-portable-knowledge]]
source: research/raw/autonomous-video-production.md
ingested: 2026-05-07
---

# Autonomous Video Production Research

Tool stack analysis for enabling Sivart to complete demo videos without human-in-the-loop.

## Key Points

**Full autonomy is achievable.** The recommended stack: Gemini 3 Pro (image generation, full API) + Runway ML (motion/animation, full API) + Remotion/FFmpeg (video editing, code-based/CLI).

**Runway ML API.** Full API available via `@runwayml/sdk` (Node.js). Capabilities: image-to-video, text-to-video, multiple models (gen4_turbo, veo3.1), variable duration (2-10 seconds), multiple aspect ratios. Per-second billing. Priority integration.

**Remotion (programmatic video).** React-based components for video. Programmatic timeline control, image sequences, audio sync, transitions, effects, server-side rendering. No GUI required, all logic in code, deterministic output. Free for individuals, $75-250/mo for teams/automation. Ideal for autonomous video assembly.

**FFmpeg (fallback).** CLI tool, fully scriptable. Image sequence to video, audio overlay, encoding. Free, open source. Reliable fallback when APIs fail.

**DaVinci Resolve and CapCut.** DaVinci Resolve has Lua/Python scripting but requires desktop. CapCut has no API and requires browser automation. Neither suitable for autonomous production.

**Recommended integration order.** 1. Runway ML for motion generation. 2. Remotion for assembly and editing. 3. FFmpeg for encoding and fallback. 4. Gemini for image generation inputs.

## Relevance

Video production is the next capability frontier after text/code. The Agent Factory should include video skills as part of the creative production pipeline.

## Related

- [[agent-native-operations]] -- Creative production as agent capability
- [[skills-as-portable-knowledge]] -- Video production as portable skill
