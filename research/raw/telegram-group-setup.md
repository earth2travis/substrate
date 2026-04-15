# Telegram Group Setup with OpenClaw

**Date:** 2026-03-02
**Issue:** #310
**Sources:** OpenClaw docs, Dan Malone's multi-agent guide, Macaron setup guide, OpenClaw Discord

## Goal

Move from flat DM chat to a Telegram forum group with topic-based channels for project threading. Eventually support multi-agent routing.

## How Telegram Forums Work

Telegram "forum mode" (Topics) turns a supergroup into a threaded workspace. Each topic is an independent thread with its own message history. OpenClaw has first-class support:

- Each topic gets an isolated session: `agent:main:telegram:group:<chatId>:topic:<threadId>`
- Topics inherit group settings unless overridden
- Per-topic config: `channels.telegram.groups.<chatId>.topics.<threadId>`
- Per-topic overrides: `requireMention`, `allowFrom`, `skills`, `systemPrompt`, `enabled`

## Architecture Decision: One Bot vs Multiple Bots

Dan Malone's guide compares two approaches:

### One Bot, Multiple Topics (simpler, recommended for us now)
- Single bot token, one identity in the group
- Each topic is an isolated session
- Can set per-topic systemPrompt to specialize behavior
- All topics share the same agent workspace and tools
- Lower config overhead

### Multiple Bots, Multiple Topics (multi-agent future)
- Each bot gets its own workspace, tools, memory, SOUL.md
- True isolation between agents
- `sessions_send` for cross-agent communication
- Requires separate BotFather token per bot
- More config, more infra

**Recommendation:** Start with one bot + topics. When we spin up additional agents, add more bots. The group and topic structure carries forward.

## Proposed Topic Structure

| Topic | Purpose | Notes |
|---|---|---|
| General | Default, catch-all conversation | Like our current DM |
| Operations | Infra, server, OpenClaw, tooling | Cron alerts could route here |
| Research | Deep dives, reading, analysis | HyperStack, prompt caching, etc |
| Framing | Project work, issues, PRs | Active development |
| Writing | Transmissions, essays, creative | Blog and creative work |
| Comms | Farcaster, social, external | Social presence |

Topics can be added/removed anytime. Start lean, expand as needed.

## Setup Steps

### 1. Create the Telegram Group

1. Create a new group in Telegram (just you + the bot)
2. Convert to supergroup (happens automatically when you enable Topics)
3. Enable Topics (Forum mode) in group settings
4. Add the Sivart bot to the group
5. Make the bot a group admin (ensures it sees all messages)
6. Note the group chat ID from `openclaw logs --follow`

### 2. Create Topics

Create topics manually in Telegram: General, Operations, Research, Framing, Writing, Comms.

Note each topic's `threadId` from the logs when you first message in each topic.

### 3. Update OpenClaw Config

```json
{
  "channels": {
    "telegram": {
      "enabled": true,
      "dmPolicy": "pairing",
      "groupPolicy": "allowlist",
      "groups": {
        "<GROUP_CHAT_ID>": {
          "groupPolicy": "open",
          "requireMention": false,
          "topics": {
            "<GENERAL_THREAD_ID>": {
              "enabled": true
            },
            "<OPERATIONS_THREAD_ID>": {
              "enabled": true
            },
            "<RESEARCH_THREAD_ID>": {
              "enabled": true
            },
            "<FRAMING_THREAD_ID>": {
              "enabled": true
            },
            "<WRITING_THREAD_ID>": {
              "enabled": true
            },
            "<COMMS_THREAD_ID>": {
              "enabled": true
            }
          }
        }
      }
    }
  }
}
```

### 4. BotFather Settings

- `/setprivacy` → OFF (bot sees all group messages)
- Remove and re-add bot after changing privacy mode

### 5. Routing Cron Outputs

Cron jobs can target specific topics by setting the `channel` and potentially `threadId` in delivery config. This means:
- Email triage results → Operations topic
- Calendar alerts → General topic
- Project audit results → Framing topic
- Release monitor → Operations topic

This needs testing. The cron `delivery.mode: "announce"` currently routes to the last active session. We may need to configure `delivery.channel` and topic targeting.

## Important Notes

### Session Isolation
Each topic is a separate session. Conversation in Research won't be visible in Framing. This is the whole point: context stays focused.

### DM Still Works
The DM channel continues to work alongside the group. You can use DM for private/sensitive stuff and the group for project work.

### requireMention
Set to `false` for the group so the bot responds to every message. In a private group with just us, there's no need for @mention gating.

### Heartbeat Target
Currently heartbeat targets "telegram" (the DM). May want to route heartbeat alerts to the Operations topic instead. Test this.

### createForumTopic Tool
OpenClaw has a `createForumTopic` action, meaning I can programmatically create new topics when new projects spin up. No need to do it manually every time.

## Future: Multi-Agent in the Group

When we add more agents (per #304 HyperStack research, autonomous organization direction):

1. Create a new bot via BotFather for each agent
2. Add each bot to the group
3. Configure per-bot routing to different agents via `channels.telegram.accounts`
4. Each agent owns specific topics
5. Cross-agent communication via `sessions_send`

Dan Malone's setup runs 4 agents this way successfully. The pattern is proven.

## References

- OpenClaw Telegram docs: https://docs.openclaw.ai/channels/telegram
- Dan Malone multi-agent guide: https://www.dan-malone.com/blog/building-a-multi-agent-ai-team-in-a-telegram-forum
- Macaron setup guide: https://macaron.im/blog/openclaw-telegram-bot-setup
- OpenClaw feature request for per-topic agent routing: https://github.com/openclaw/openclaw/issues/1615
