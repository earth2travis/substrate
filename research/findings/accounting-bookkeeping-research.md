---
title: "Accounting and Bookkeeping for AI-Native Operations"
tags: [operations, finance, tooling, agents]
related:
- 1password-integration
- 28-openclaw-mistakes
source: research/raw/accounting-bookkeeping-research.md
---
# Accounting and Bookkeeping for AI-Native Operations

## Summary

Research comparing bookkeeping tools for a human+AI partnership at small scale (~$50-100/mo expenses, US-based). The clear winner for AI-native workflows: plain text accounting (hledger or beancount). Traditional tools like Wave and QuickBooks are human-oriented and lack APIs practical for agent automation.

## Tool Comparison

| Tool | Cost | AI-Writable | Git-Friendly | Tax Mapping | Fit |
|------|------|-------------|--------------|-------------|-----|
| Wave Free | $0 | No | No | Basic | Poor |
| QB Solopreneur | $20/mo | Limited | No | Excellent | Okay |
| Google Sheets | $0 | Yes | No | Manual | Fair |
| hledger | $0 | Yes | Yes | Manual | Excellent |
| beancount | $0 | Yes | Yes | Manual | Excellent |

## Why Plain Text Accounting Wins

- **Files are the API**: No OAuth, no rate limits, no service dependencies
- **Git-versioned**: Full audit trail of every change
- **Scriptable**: CLI tools for querying, reporting, validation
- **Agent-native**: An AI agent reads and writes plain text natively

## The Tradeoff

Tax categorization is manual. You define your own chart of accounts mapped to Schedule C. For a micro operation, this is acceptable. For scale, QuickBooks' TurboTax integration becomes the killer feature.

## Recommendation

Start with hledger or beancount. Maintain the books as part of the agent's normal operations. If tax complexity justifies it later, migrate to QuickBooks with clean historical data.