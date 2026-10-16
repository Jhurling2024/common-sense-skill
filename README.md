# Common Sense Skill

> **Think ahead. Reuse what works. Verify before claiming success.**

**Founder, Originator and Project Creator: Justin Hurling** · [GitHub: @Jhurling2024](https://github.com/Jhurling2024)  
**Copyright notice: © 2026 Marksman Capital USA LLC** · **License: MIT** · v0.1.4

Common Sense Skill is a portable Agent Skill that prompts coding and automation agents to exercise practical judgment *before* creating complexity. It is intended for OpenCode and other tools compatible with the [Agent Skills format](https://agentskills.io/specification).

It does **not** claim that AI acquires human common sense. It implements repeatable checks: *outcome → existing capability → simpler alternative → evidence → cost & authority → real-world verification → learning*.

## Why it exists

Many failures are not programming errors. An agent may build a bridge when a desktop workflow should have been evaluated, suggest a metered automation product despite a zero-cost requirement, treat a listener acknowledgment as production readiness, or generate a "fixed" ZIP without testing the cloud preview. This skill turns those classes of oversight into preflight questions and acceptance checks.

It is **not** a replacement for a security engineer, legal professional, code tester or the user's own decisions.

## What it does

| Without the check | With Common Sense Skill |
| --- | --- |
| Starts adding tools immediately | Checks existing native and installed capabilities first |
| Claims "fixed" because a file builds | Requires user-visible/environment-specific verification |
| Confuses delivery, ACK and execution | Reports each proven layer independently |
| Suggests paid tools without warning | Screens for actual billing, quotas and free/local options |
| Asks questions already answered in context | Reuses constraints and asks only blocking questions |
| Repeats the same mistake | Captures a regression scenario and proposes reviewed improvement |
| Installs more autonomous agents | Defers to existing coordinator and approval hierarchy |

## Get started

OpenCode scans `.opencode/skills/<name>/SKILL.md` within the project (and global skill paths). Place this **entire directory** at:

```text
YOUR_PROJECT/.opencode/skills/common-sense-skill/
```

For a project-local copy, keep `SKILL.md`, `references/` and `templates/` together. On Windows, use file management or your existing approved agent installer. **Inspect for an existing skill named `common-sense-skill` first**; do not overwrite conflicts.

The OpenCode-specific `metadata.opencode/slash: "true"` advertises a potential `/common-sense-skill` command. Its normal description supports on-demand discovery. Behavior must be verified in the installed OpenCode version and its permission policy. This repository **does not** change `opencode.json`, execute commands, request unrestricted permissions, or grant itself approval.

For ATLAS PRIME: review `references/agent-governance.md` before proposing integration. Treat the skill as a planning/verification behavior for authorized existing engineers, **not** as a new coordinator. Activation in a governed production system requires a separate approval and regression test.

## Example use cases

- **"Build a continuous YouTube publishing system"** → check installed tools, local hardware, API permissions, credit limits and existing scheduling before buying anything.
- **"The preview is correct, production is wrong"** → compare live HTML/CSS/cache, reproduce at relevant screen sizes, and avoid claiming a ZIP is deployed.
- **"The bridge says ACK"** → distinguish GitHub delivery, listener acceptance, coordinator processing, backend authentication, real task output.
- **"Why didn't you suggest the desktop app?"** → record the missed native option and add an evaluation case, without assuming that the app has computer-control access.

## Validation

Runs without dependencies:

```bash
python -m unittest discover -s tests -v
```

The included tests validate **packaging and static safety properties only**, not the quality of an agent's real decisions. Behavioral evaluation ships as `tests/evaluation-cases.json` (31 scenarios across six categories, including negative and adversarial cases) with comparative with/without-skill results in `tests/evaluation-results.md`; the full release report is `docs/COMMON-SENSE-EVALUATION-REPORT.md` in this repository.

## Credit and reuse

**Marksman Capital USA LLC** is the designated project and commercial rights holder; **Justin Hurling** is credited as **Founder, Originator and Project Creator**. Original concept, problem definition and governing principles were provided by Justin Hurling. An AI assistant helped organize and draft the initial text; final human authorship, editorial revisions and publication approval are the project owner's responsibility. Contributors are recognized in `AUTHORS.md` and `CITATION.cff`.

The MIT license permits personal and commercial reuse with retention of the copyright and license notice. It does **not** require a marketing credit on a website, prevent commercial forks, or confer trademark rights.

See [`docs/MONETIZATION.md`](docs/MONETIZATION.md) for ethical paid services and sponsored maintenance models.

## Project status

**v0.1.4 — released through [`Jhurling2024/marksman-capital-usa`](https://github.com/Jhurling2024/marksman-capital-usa) under owner authorization (Issue #47, 2026-10-16). Public distribution: [`Jhurling2024/common-sense-skill`](https://github.com/Jhurling2024/common-sense-skill).** Installation and activation are separate from publication: the owner's local machine runs v0.1.1 (hash-verified 2026-10-14), and activation across other local agents requires its own approval. Content was generated from a thematic review of accessible user conversations and project history; not an exhaustive audit of every archived message. Public materials deliberately contain no internal account identifiers, credentials, unpublished source code, private conversation transcripts or machine-specific paths.

## Sources

- [Agent Skills specification](https://agentskills.io/specification)
- [OpenCode official Agent Skills documentation](https://docs.opencode.ai/docs/skills/)
- [MIT license reference](https://choosealicense.com/licenses/mit/)
