---
title: Autonomous Video Production Research
tags:
  - research
  - creative
related:
  - [[actual-occasions]]
  - [[ai-career-convergence]]
  - [[alfred-north-whitehead]]
  - [[api-first-interfaces]]
source: research/raw/autonomous-video-production.md
---

# Autonomous Video Production Research

Research findings for enabling [[Sivart]] to complete demo videos without human-in-the-loop.

## Executive Summary

**Key Finding:** Full autonomous video production is achievable with the right tool stack.

| Capability       | Tool            | API Available             | Autonomy Level          |
| ---------------- | --------------- | ------------------------- | ----------------------- |
| Image Generation | Gemini 3 Pro    | ✅ Yes                    | Full                    |
| Motion/Animation | Runway ML       | ✅ Yes                    | Full                    |
| Video Editing    | Remotion        | ✅ Yes (code-based)       | Full                    |
| Video Editing    | FFmpeg          | ✅ Yes (CLI)              | Full                    |
| Video Editing    | CapCut          | ❌ No API                 | Browser automation only |
| Video Editing    | DaVinci Resolve | ⚠️ Scripting (Lua/Python) | Requires desktop        |

**Recommended Stack:** Gemini + Runway ML API + Remotion/FFmpeg

---

## Tool Analysis

### 1. Runway ML API

**Status:** ✅ Full API available

**Documentation:** https://docs.dev.runwayml.com

**SDK:** `@runwayml/sdk` (Node.js)

**Capabilities:**

- Image-to-video generation
- Text-to-video generation
- Multiple models (gen4_turbo, veo3.1)
- Variable duration (2-10 seconds)
- Multiple aspect ratios

**API Example:**

```javascript
import RunwayML from "@runwayml/sdk";

const client = new RunwayML();

const task = await client.imageToVideo
  .create({
    model: "gen4_turbo",
    promptImage: "data:image/png;base64,...",
    promptText: "Subtle camera movement, flickering light",
    ratio: "1280:720",
    duration: 5,
  })
  .waitForTaskOutput();

// task.output contains the video URL
```

**Pricing:** Per-second billing, varies by model

**Access Requirements:**

- Developer account: https://dev.runwayml.com
- API key with billing enabled
- Store in 1Password: "Runway ML Developer"

**Verdict:** Fully automatable. Priority integration.

---

### 2. Remotion (Programmatic Video)

**Status:** ✅ Fully programmatic (React-based)

**Documentation:** https://remotion.dev/docs

**Package:** `remotion`

**Capabilities:**

- React components for video
- Programmatic timeline control
- Image sequences
- Audio sync
- Transitions and effects
- Server-side rendering

**Why It's Perfect for Agents:**

- No GUI required
- All logic in code
- Can be run headlessly
- Deterministic output

**Example:**

```jsx
import { Composition, Img, useCurrentFrame, interpolate } from "remotion";

const Panel = ({ src, startFrame, endFrame }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [startFrame, startFrame + 15], [0, 1]);

  return <Img src={src} style={{ opacity }} />;
};

export const DemoVideo = () => (
  <Composition
    id="Demo"
    component={VideoSequence}
    durationInFrames={30 * 180} // 3 minutes at 30fps
    fps={30}
    width={1920}
    height={1080}
  />
);
```

**Rendering:**

```bash
npx remotion render src/index.tsx Demo out/demo.mp4
```

**Pricing:**

- Free for individuals
- $75-250/mo for teams/automation

**Verdict:** Ideal for autonomous video assembly. Implement this.

---

### 3. FFmpeg (Fallback)

**Status:** ✅ CLI tool, fully scriptable

**Capabilities:**

- Image sequence to video
- Video concatenation
- Audio mixing
- Transitions (with filters)
- Format conversion

**Use Cases:**

- Simple image-to-video conversion
- Concatenating clips
- Adding audio tracks

**Example:**

```bash
# Convert image sequence to video
ffmpeg -framerate 30 -i panel-%02d.png -c:v libx264 -pix_fmt yuv420p output.mp4

# Concatenate videos
ffmpeg -f concat -i files.txt -c copy final.mp4

# Add audio
ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac output.mp4
```

**Verdict:** Good for simple assembly, use as fallback.

---

### 4. CapCut

**Status:** ❌ No public API

**Options:**

1. Browser automation (Playwright/Puppeteer)
2. Desktop automation (limited)

**Browser Automation Feasibility:**

- Web editor available at capcut.com
- Could automate with browser tool
- Fragile, UI changes break automation
- Not recommended for production

**Verdict:** Not suitable for autonomous workflow.

---

### 5. DaVinci Resolve

**Status:** ⚠️ Scripting available but complex

**Scripting Options:**

- Lua scripting
- Python API
- Requires desktop installation

**Limitations:**

- Must run on desktop (not server)
- Complex setup
- GUI interaction often required

**Documentation:** Available in Resolve installation

**Verdict:** Possible but high complexity. Use Remotion instead.

---

## Recommended Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    [[Sivart]] Autonomous Video Pipeline             │
└─────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│  Phase 1: Image Generation                                      │
│  Tool: Gemini 3 Pro Image Preview                               │
│  Input: panel-prompts.json + reference images                   │
│  Output: generated-panels/*.png                                  │
│  Status: ✅ IMPLEMENTED                                          │
└─────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│  Phase 2: Motion Addition                                       │
│  Tool: Runway ML API                                            │
│  Input: generated-panels/*.png + motion prompts                 │
│  Output: motion-clips/*.mp4                                     │
│  Status: 🔧 NEEDS IMPLEMENTATION                                 │
└─────────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│  Phase 3: Video Assembly                                        │
│  Tool: Remotion OR FFmpeg                                       │
│  Input: motion-clips/*.mp4 + screenshots + audio                │
│  Output: final-demo.mp4                                         │
│  Status: 🔧 NEEDS IMPLEMENTATION                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Implementation Plan

### Phase 1: Runway ML Integration (Priority)

**Issue:** Create new GitHub issue

**Tasks:**

1. Create Runway developer account
2. Generate API key
3. Store key in 1Password
4. Write `add-motion.js` script
5. Test with single panel
6. Scale to all panels

**Estimate:** 2-4 hours

### Phase 2: Remotion Video Assembly

**Issue:** Create new GitHub issue

**Tasks:**

1. Initialize Remotion project
2. Create video composition components
3. Implement timeline from script
4. Add transitions
5. Audio sync
6. Test render

**Estimate:** 4-8 hours

### Phase 3: End-to-End Pipeline

**Issue:** Create new GitHub issue

**Tasks:**

1. Orchestration script that runs all phases
2. Error handling and retry logic
3. Progress reporting
4. Quality validation
5. Documentation

**Estimate:** 2-4 hours

---

## Progressive Autonomy Plan

### Level 1: Instructions Only (Current)

- [[Sivart]] generates detailed instructions
- Human executes in GUI tools
- Human reviews output

### Level 2: API with Oversight

- [[Sivart]] calls Runway ML API directly
- [[Sivart]] uses Remotion for assembly
- Human reviews before final export
- **Target:** Implement this week

### Level 3: Full Autonomy with Gates

- [[Sivart]] runs entire pipeline
- Automated quality checks
- Human approves final output only
- **Target:** After successful Level 2

### Level 4: Continuous Production

- [[Sivart]] monitors for new requests
- Autonomous generation and delivery
- Exception handling to human
- **Target:** Future milestone

---

## Required Credentials

| Service          | Credential Type    | Storage Location         | Status       |
| ---------------- | ------------------ | ------------------------ | ------------ |
| Google AI Studio | API Key            | 1Password: "Nano Banana" | ✅ Have      |
| Runway ML        | API Key            | 1Password: "Runway ML"   | 🔧 Need      |
| Remotion         | License (optional) | N/A                      | Free tier OK |

---

## Cost Projections

### Per Demo Video (24 panels, 3 minutes)

| Phase            | Tool     | Calculation        | Cost       |
| ---------------- | -------- | ------------------ | ---------- |
| Image Generation | Gemini   | 24 × $0.134        | $3.22      |
| Motion Addition  | Runway   | 24 × 5s × ~$0.05/s | ~$6.00     |
| Video Assembly   | Remotion | Free tier          | $0.00      |
| **Total**        |          |                    | **~$9.22** |

### Monthly Projections

| Volume         | Monthly Cost |
| -------------- | ------------ |
| 1 demo/month   | ~$10         |
| 4 demos/month  | ~$40         |
| 10 demos/month | ~$100        |

---

## Next Steps

1. **Immediate:** Create Runway developer account and add API key
2. **This Week:** Implement `add-motion.js` with Runway ML SDK
3. **This Week:** Create proof-of-concept with 3 panels
4. **Next Week:** Implement Remotion assembly pipeline
5. **Ongoing:** Progressive autonomy testing

---

## Open Questions

1. **Runway API access:** Need to verify account type required for API
2. **Remotion rendering:** Server requirements for headless render
3. **Audio sync:** Best approach for voiceover timing
4. **Quality gates:** What automated checks can validate output?

---

_Last updated: February 8, 2026_
_Related Issues: #123, #124_
