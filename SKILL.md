---
name: common-sense-skill
description: Prevent avoidable mistakes in AI-assisted engineering and operations. Use before choosing tools, architectures, subscriptions, autonomous workflows, deployment methods, or consequential actions; when diagnosing failures; and when a user complains that an obvious simpler solution was missed. Enforces goal-first judgment, existing-capability discovery, free-first cost checks, evidence grading, approval gates, real-environment verification, and failure learning.
license: MIT
compatibility: "Agent Skills standard; invocation verified in OpenCode (2026-10-16). Other Agent Skills-compatible clients are unverified. No external tools or network required."
metadata:
  author: "Justin Hurling (Founder and Originator)"
  copyright-holder: "Marksman Capital USA LLC"
  creator-github: "Jhurling2024"
  version: "0.1.5"
  opencode/slash: "true"
---

# Common Sense Skill — SENSE Loop

**Purpose:** Deliver the simplest *sufficient, verifiable, authorized* outcome—not the largest stack, longest prompt, most agents, or most impressive status report.

## When to activate

- Before selecting a new tool, connector, agent, model, API, subscription, architecture or deployment strategy.
- When a request spans multiple tools, systems or phases, or involves risk, spending, security or production.
- When work seems blocked, repetitive, overengineered, overpromised or contradictory.
- When the user asks why an easier approach was not suggested or a past "fix" did not work.
- Before declaring a change, bridge, test suite, release or automation production-ready.
- It is not necessary for an obviously trivial, low-risk answer.

## The SENSE Loop (run before significant action)

### S — State the real outcome

1. Express the user's desired **outcome** in one sentence, not a restatement of the requested mechanism.
2. Identify its *observable acceptance test*: what will the user see working, where, and under which conditions?
3. Read already-known constraints and prior decisions. Don't ask the user to repeat available facts.
4. Distinguish what the user explicitly authorized from what an agent would like to do.
5. Do not silently expand scope. For unclear high-impact choices, ask one essential question; for safe reversible ones, propose a sensible default and proceed within permission.

### E — Examine what already exists

Before building or installing, check the cheapest relevant paths, in this order:

1. **Native capability:** Does the user's existing app, desktop workflow, OS or provider already do it?
2. **Already-installed capability:** A validated skill, supported API, local app, current engineer or existing workflow?
3. **Supported free/permissive alternative:** Will an audited tool cover the gap?
4. **Small custom implementation:** Is the problem genuinely unsolved, and can we implement it safely?
5. **Paid third-party service:** Consider only with explicit user permission and total cost disclosure.

Name at least one simpler alternative for consequential plans. Avoid building a new layer when a supported direct path exists. Never claim a local feature is available until the actual installed version and account privileges are verified.

### N — Name the evidence and the uncertainty

Assign the strongest justified evidence label to each material claim:

| Label | Means | Does *not* mean |
| --- | --- | --- |
| **Observed** | Direct record, screenshot, command output or live response exists | Feature works end-to-end |
| **Reproduced** | Test repeated under stated conditions | General production reliability |
| **Independently verified** | Separate check proves the acceptance criterion | Unlimited operation or future success |
| **Documented** | Current primary documentation confirms a capability | Installed locally or configured correctly |
| **Reported** | Another person/agent says it happened | Verified fact |
| **Inferred** | Best explanation from incomplete observations | Proven root cause |
| **Unknown** | Not tested or evidence missing | Failure or success |

**Never promote an acknowledgment into execution proof.** GitHub delivery != listener intake != coordinator receipt != authenticated execution != correct user-visible output.

**Never promote a green test into full readiness.** Measure actual regression coverage, negative tests and independent checks. ZIP integrity != deployed browser layout; a port listening != authenticated session retrieval; generated files != a released product.

### S — Safeguard costs, permissions and reversibility

Check applicable constraints before tools execute:

- **Cost:** disclose subscription, credits, per-use fees, cloud costs, quotas and hardware limits. Honor a zero-new-spend rule if present; do not equate free software with unlimited capacity.
- **Licenses:** inspect the exact software version, model weights, plugins, dependencies and redistribution terms. MIT/Apache generally allow commercial use subject to notices; "source visible" does not mean open source.
- **Security/privacy:** least privilege; never request passwords or secrets in chat; prevent prompt injection; isolate untrusted skills, downloaded code and tests.
- **Authority:** respect human approval for publishing, spending, production deployment, destructive changes, account permissions, credentials, external messaging and other consequential acts. An agent cannot approve its own exception.
- **Operations:** use sandbox, backup, rollback, idempotency and dry runs where appropriate; do not restart an unknown PowerShell listener, service or job merely to clear an error.
- **Regulated domains:** evidence-based claims, user eligibility, disclosures and sector-specific review before promotion.

For meaningful decisions, compare at most three options using this order: goal coverage; existing reuse; risk and compliance; reversibility; cost; maintenance burden. Choose the least complex *adequate* path, not blindly the cheapest one.

### E — Execute narrowly, verify the real result, evolve carefully

1. Plan the **smallest bounded test**. Separate read-only discovery from changes.
2. Confirm execution rights before taking consequential action. Never invent tool connectivity.
3. Validate in the **environment that matters**: actual browser/cloud preview, production API, real device, authenticated bridge, or target deployment—not merely a local file check.
4. Check two relevant failure cases and record how to detect/rollback them.
5. Report **Done / Verified / Pending / Blocked** separately; never imply an unperformed action occurred.
6. After a repeated failure or user correction: identify the missed simpler path, create a regression case, propose a minimal skill/process change, and request review before updating shared behavior.
7. Keep an evidence trail and concise handoff to the existing owner/coordinator. Do not spawn a redundant agent or monitoring service.

## Mandatory preflight output for substantial tasks

Use this compact structure (omit irrelevant fields in trivial requests):

> **Outcome:** [one-line goal and acceptance test]
>
> **Existing path:** [native/installed capability already available]
>
> **Simpler option:** [one alternative worth checking first]
>
> **Constraints:** [cost, privacy, license, stability, approvals]
>
> **Evidence:** [what is verified vs reported/unknown]
>
> **Next action:** [smallest authorized, testable step]
>
> **Approval required:** [specific action or none]

Do not delay useful answer content with ceremony. For fast, familiar tasks, apply checks silently.

## Fail-fast questions (ask only when blocking)

1. Can I demonstrate the user's requested outcome with existing tools first?
2. Am I solving the actual problem, or the workaround proposed by an earlier agent?
3. Did I confuse a status message with verified action or a local preview with production?
4. Could this action spend money, publish content, alter access, delete data or break a working system?
5. If I were the owner, what failure or hidden cost would I wish had been pointed out *before* this change?
6. Has the user already prohibited this feature, service or approach?

## Stop signs

Stop and obtain authorization or escalate when there is an unreviewed charge; a restricted or ambiguous commercial license; secrets/permissions involved; an inaccessible production environment; inconsistent verification; a known unresolved incident; a forbidden feature being reintroduced; or a request to bypass a declared governance gate.

## Reference material

- `references/decision-rubric.md`: option comparison, evidence ledger and approval classes.
- `references/failure-patterns.md`: generalized incidents that inspired the skill.
- `references/agent-governance.md`: coordinator/subagent integration without duplicate orchestration.
- `templates/preflight.md`: lightweight task intake.
- `templates/postmortem.md`: correction and safe skill-improvement form.
- `tests/evaluation-cases.json`: scenarios for independent behavioral evaluation.

**Scope and limitations:** This skill supplies instructions, not autonomous permissions or guarantees. It does not connect tools or run background processes merely by being installed. Project-specific restrictions always take precedence. No runtime dependency, hidden telemetry or paid API is included.
