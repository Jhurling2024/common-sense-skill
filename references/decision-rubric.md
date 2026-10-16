# Decision rubric and evidence ledger

## Choose paths by fitness, not popularity

Compare **native**, **existing/installed**, **audited open-source**, **small custom build** and (only if authorized) **paid** routes. Reject any option that violates a hard requirement before scoring.

Score the remaining routes 0–2 per dimension (2 = strongest):

| Dimension | Ask | Weight |
| --- | --- | ---: |
| Outcome | Does it meet the actual acceptance test? | 3 |
| Reuse | Does it use supported, already-owned/installed functionality? | 2 |
| Safety | Does it preserve security, licensing, privacy and gates? | 3 |
| Verification | Can we prove it in the target environment? | 3 |
| Reversibility | Is testing/rollback practical? | 2 |
| Cost | No new spend, known quota and low operational burden? | 2 |
| Simplicity | Few moving parts and low maintenance overhead? | 2 |

Hard failure on legal/authority/security constraints means **disqualify**, regardless of total score. Do not fabricate numeric scores. Where no measurements exist, mark unknown.

## Evidence ledger template

| Claim | Label | Exact source/time | Acceptance link tested? | Next probe |
| --- | --- | --- | --- | --- |
| Listener received comment | Observed | Journal event with ID | No | Coordinator correlated read |
| Coordinator read request | Observed | Session/GitHub reply | No | Backend authenticated request |
| Task executed | Unknown | Not yet available | No | Session result and artifact |
| User sees corrected release | Unknown | Local ZIP only | No | Cloud preview on target devices |

## Impact classes

- **C0: read-only / reversible discussion:** research and status checks within existing permissions. No extra approval ordinarily needed.
- **C1: isolated local experiment:** contained scratch writes and temporary processes, permitted only if specifically authorized by the applicable project policy.
- **C2: shared configuration or permissions:** installs, credentials, schedules, network configuration, new agents, persistent services; obtain owner approval and rollback.
- **C3: external or irreversible action:** public releases, account role changes, payments, mass communications, destructive changes and production deployment; require explicit authorization and verified preconditions.

These are **recommended classifications**, not a documented OpenCode permission syntax. Existing project governance and tool-side permissions always override this reference.

## Reports should answer

**What is known?** Provide evidence. **What is inferred?** Label it. **What remains blocked?** Name the minimal test and approval. **What simpler route was evaluated?** State it. **What can the user actually do next?** One unambiguous action.
