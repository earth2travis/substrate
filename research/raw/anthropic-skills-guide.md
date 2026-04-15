# The Complete Guide to Building Skills for Claude
## Source: Anthropic (resources.anthropic.com)
## Extracted: 2025-07-17

## Key Concepts

### What is a Skill?
A folder containing:
- **SKILL.md** (required): Instructions in Markdown with YAML frontmatter
- **scripts/** (optional): Executable code (Python, Bash, etc.)
- **references/** (optional): Documentation loaded as needed
- **assets/** (optional): Templates, fonts, icons used in output

### Core Design Principles

#### Progressive Disclosure (Three Levels)
1. **YAML frontmatter**: Always loaded in system prompt. Tells Claude when to use the skill.
2. **SKILL.md body**: Loaded when Claude thinks skill is relevant. Full instructions.
3. **Linked files**: Additional files Claude discovers only as needed.

#### Composability
Skills work alongside other skills. Don't assume exclusivity.

#### Portability
Works across Claude.ai, Claude Code, and API without modification.

### Skill Use Case Categories

#### Category 1: Document & Asset Creation
Creating consistent, high-quality output (documents, code, designs).
- Embedded style guides and brand standards
- Template structures for consistent output
- Quality checklists before finalizing
- No external tools required

#### Category 2: Workflow Automation
Multi-step processes with consistent methodology.
- Step-by-step workflow with validation gates
- Templates for common structures
- Built-in review and improvement suggestions
- Iterative refinement loops

#### Category 3: MCP Enhancement
Workflow guidance on top of MCP tool access.
- Coordinates multiple MCP calls in sequence
- Embeds domain expertise
- Provides context users would otherwise need to specify
- Error handling for common MCP issues

### Technical Requirements

#### File Structure
```
your-skill-name/
├── SKILL.md          # Required
├── scripts/          # Optional
├── references/       # Optional
└── assets/           # Optional
```

#### Critical Rules
- SKILL.md must be exactly `SKILL.md` (case-sensitive)
- Folder naming: kebab-case only (no spaces, underscores, capitals)
- No README.md inside skill folder

#### YAML Frontmatter
```yaml
---
name: your-skill-name
description: What it does. Use when user asks to [specific phrases].
---
```

**name** (required): kebab-case, should match folder name
**description** (required): Must include BOTH what it does AND when to use it (trigger conditions). Under 1024 chars. No XML tags. Include specific task phrases users might say.

Optional fields: license, compatibility, metadata (author, version, mcp-server)

**Security**: No XML angle brackets in frontmatter. No "claude" or "anthropic" in name.

### Writing Effective Instructions

#### Recommended SKILL.md Structure
```markdown
---
name: your-skill
description: [...]
---

# Your Skill Name

## Instructions

### Step 1: [First Major Step]
Clear explanation of what happens.

```bash
python scripts/fetch_data.py --project-id PROJECT_ID
Expected output: [describe what success looks like]
```

## Examples

Example 1: [common scenario]
User says: "Set up a new marketing campaign"
Actions:
1. Fetch existing campaigns via MCP
2. Create new campaign with provided parameters
Result: Campaign created with confirmation link

## Troubleshooting

Error: [Common error message]
Cause: [Why it happens]
Solution: [How to fix]
```

#### Best Practices
- Be specific and actionable (not vague)
- Reference bundled resources clearly
- Use progressive disclosure (core in SKILL.md, details in references/)
- Include error handling

### Testing

#### Three Testing Areas

1. **Triggering tests**: Does the skill load at the right times?
   - Should trigger on obvious tasks
   - Should trigger on paraphrased requests
   - Should NOT trigger on unrelated topics

2. **Functional tests**: Does it produce correct outputs?
   - Valid outputs generated
   - API calls succeed
   - Error handling works
   - Edge cases covered

3. **Performance comparison**: Is it better than baseline?
   - Compare token usage, message count, error rate with/without skill

#### Iteration Signals
- **Undertriggering**: Add more detail to description, include keywords
- **Overtriggering**: Add negative triggers, be more specific
- **Execution issues**: Improve instructions, add error handling

### Distribution

#### Current Model
- Download folder → zip → upload to Claude.ai Settings > Capabilities > Skills
- Or place in Claude Code skills directory
- Organization admins can deploy workspace-wide

#### API
- `/v1/skills` endpoint for managing skills
- Add to Messages API via `container.skills` parameter

### Success Metrics (Aspirational)
- Skill triggers on 90% of relevant queries
- Completes workflow in X tool calls
- 0 failed API calls per workflow
- Users don't need to prompt about next steps
- Workflows complete without user correction
- Consistent results across sessions
