# Hetzner CPX21 Rescale: OOM Root Cause and Resolution

## Date
2026-06-28

## Summary

Rescaled the fleet VPS from Hetzner CPX11 (2 vCPU, 2 GB RAM, $4.99/mo) to CPX21 (3 vCPU, 4 GB RAM, $37.49/mo) after diagnosing the Linux OOM killer as the root cause of repeated Kanban worker crashes.

## Root Cause Analysis

Kanban workers were crashing simultaneously across all active tasks. The dispatcher recorded each as `outcome: "crashed"` with `error: "pid <N> not alive"`. Investigation revealed the workers were not failing in software but being killed by the kernel OOM killer.

### Evidence

1. **Journal logs confirm OOM kills:**
   - Jun 28 20:26:54: `hermes-gateway.service: A process of this unit has been killed by the OOM killer.` Killed PIDs 36308 (t_3fc0c992), 37184 (t_f0b7ac6d), 37185 (t_5553c2da) simultaneously with SIGKILL.
   - Jun 28 20:37:14: OOM killed PID 38939 (t_3fc0c992 retry, running solo) with SIGKILL.
   - Jun 26: all 3 workers on tasks t_52617407, t_f0b7ac6d, t_5553c2da died at identical epochs (1782583725 and 1782584226), confirming batch OOM kills, not independent failures.

2. **Memory state at time of crash:**
   - Total RAM: 1.9 GB, available: 65 MB
   - Swap: 1.0 GB, 99.9% full
   - The box was at its absolute memory ceiling.

3. **Survival cases confirm the diagnosis:**
   - Two lightweight review/audit workers (runs 144, 145) completed in 175 seconds each because they mostly read files and finished before memory pressure built enough to trigger OOM.
   - The heavy investigation worker (t_3fc0c992) crashed even running solo at 620 seconds because it accumulated more context, built a prototype, and ran tests until its memory footprint grew past the breaking point.

### Baseline Memory Consumption

Always-on services consume approximately 1.3 GB before any Kanban worker spawns:

| Service | RSS |
|---|---|
| Hermes gateway | 130 MB |
| Hermes dashboard | 180 MB |
| Interactive session (Sivart) | 220 MB |
| Cursor server | 200 MB |
| Headless Chrome x2 | 80 MB |
| signal-cli | 93 MB |
| tailscaled | 28 MB |
| **Baseline total** | **~1.3 GB** |

Each Hermes worker process runs approximately 200 MB RSS and grows as it accumulates context through a task. On a 2 GB box with 1.3 GB baseline, only 700 MB remains for workers. That supports roughly 3 lightweight workers briefly, but 3 heavy workers with context growth exceed the ceiling within minutes.

### Crash Threshold

3 concurrent workers on 2 GB RAM with 1.3 GB baseline. The three-role collaboration protocol (lead, reviewer, auditor) maxes at 3 concurrent by design. Auto-decompose caps at 3 new tasks per tick. The fleet's own design hits the OOM threshold reliably.

## Resolution

Rescaled from CPX11 to CPX21.

| Spec | CPX11 (old) | CPX21 (new) |
|---|---|---|
| vCPU | 2 | 3 |
| RAM | 2 GB | 4 GB |
| Disk | 40 GB | 40 GB |
| Traffic | 1 TB | 2 TB |
| Price | ~$4.99/mo | $37.49/mo |

### Headroom Analysis

At 4 GB: baseline 1.3 GB plus interactive session 0.2 GB leaves 2.5 GB for workers. That supports 3 concurrent heavy workers with full context growth headroom, or 5 to 6 lightweight ones. This covers the fleet's maximum concurrency (3 workers in the three-role protocol) with margin.

### Why Not Higher

CPX31 (8 GB, $73.49/mo) is comfortable but nearly double the cost for capacity the fleet will not use unless it grows significantly or starts running 6+ workers routinely. CPX41 (16 GB) and CPX51 (32 GB) are extreme overprovisioning for this workload.

## Defense in Depth

The kanban config has `max_in_progress_per_profile` set to None (unlimited). The OOM is cross-profile, not per-profile, so a worker cap would provide defense in depth against memory exhaustion even on the new box. Consider setting a per-profile concurrency limit as a secondary guard.

## Impact on Prior Research

Several prior research files referenced the CPX11 with 2 GB RAM as an infrastructure constraint. With the rescale to 4 GB, those constraints are relaxed. Key references that may need revisiting in future synthesis:

- `knowledge-graphs-as-agent-memory-substrate.md`: cited 2 GB RAM as a constraint for graph database selection. Kuzu recommendation still holds but the tightness argument is relaxed.
- `browser-automation.md`: noted 2 GB RAM as a limit for concurrent browser sessions. 4 GB provides more headroom.
- `composio-analysis.md`: cited 2 GB RAM as a reason Vault was too heavy. Still true that Vault is overkill, but the memory argument is less sharp.
- `connection-to-us.md`: framed 2 GB RAM as a constraint that forces honesty. The philosophy still applies but the specific constraint has changed.
- `nvidia-nemoguard-analysis.md`: identified the infrastructure as CPU-based Hetzner CPX11. Still CPU-based, now CPX21.