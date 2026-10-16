# ATLAS PRIME integration proposal (not authorization)

**Existing authority:** Human owner → ATLAS PRIME (one master coordinator) → currently authorized engineers → OpenCode execution environment.

Common Sense Skill is a **cross-cutting review skill**, never a new master coordinator and never an autonomous background watcher.

## Recommended limited deployment

1. Inventory existing installed skills and their canonical names/versions before doing anything. If an equivalent accepted skill already exists, augment it instead of duplicating.
2. Review the v0.1.0 sources and MIT license under read-only access; scan for untrusted prompt-injection, conflicts and resource use.
3. Register the skill only in an isolated **test project** after a separate owner approval; never auto-edit live skill registries or OpenCode configuration.
4. Check detection and actual loading via OpenCode's `available_skills`/`skill` mechanism, not by file existence alone.
5. Evaluate against the `tests/evaluation-cases.json` corpus using at least one build-focused and one adversarial/auditor model; compare with a baseline **without** the skill.
6. Measure missed-native-option rate, unsupported "done" claims, permission violations, unnecessary paid-tool suggestions, extra agent/process creation and user-visible acceptance-test accuracy. Require no increase in unsafe actions.
7. Owner and independent reviewer decide whether to allow particular engineer roles to load it. Shared/global activation remains a separate gate.
8. Gather improvement suggestions as reviewed diffs, with provenance and regression evidence. Never self-upgrade code or permissions.

## Current project-specific hold

At the time of draft creation, project reports still describe the authenticated local OpenCode execution backend as unverified/unavailable and the production activation gate as NO-GO. Installing a SKILL.md file would neither fix the backend nor authorize a production launch. This note is contextual and must be reassessed against *fresh* bridge evidence.

## Integration conflict rules

- Preserve governance ADRs, project isolation, existing skill priority and author permissions.
- Read-only GitHub message intake is not an authority escalation mechanism.
- Skills cannot silently grant agents write rights, approval rights or subscription spending authority.
- Do not expose internal documents or personal discussions in the public skill repository.
