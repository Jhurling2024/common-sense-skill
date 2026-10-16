# Owner release checklist — APPROVED 2026-10-16

**Owner authorization:** GitHub Issue #47 (`Jhurling2024/marksman-capital-usa`,
2026-10-16) — explicit approval to publish/release the Common Sense agent skill,
executed as directive ATLAS-CS-RELEASE-20261016-001. This approval covers publication
of this skill only; it does not authorize Gate E activation, autonomous production
execution, unrelated projects, or purchases.

**Release repositories:** `Jhurling2024/marksman-capital-usa` (private; package under
`common-sense/`; origin of the release history) and `Jhurling2024/common-sense-skill`
(**public**; package at repository root; owner decision 2026-10-16 — see "Visibility"
below). Issue #47 designated the existing repository for the release itself; the
standalone public repository proposed earlier was created at the visibility decision.

## Before publication — evidence

- [x] Owner reviewed and approved publication, including AI-assisted portions — Issue #47, 2026-10-16.
- [x] Rights holder designated: Marksman Capital USA LLC; Justin Hurling credited as Founder, Originator and Project Creator (`AUTHORS.md`, `docs/IP-OWNERSHIP.md`).
- [ ] **Executed assignment / documented ownership basis** for protectable human-authored content remains not executed. Documented caveat: originator and designated rights holder stem from the same owner; Issue #47 is the owner's explicit release authorization; no third-party material was found (security review 2026-10-16). Status: CONDITIONAL — REQUIRES LEGAL REVIEW for full chain-of-title certainty; not treated as a blocker for MIT publication.
- [x] Repository name decided — Issue #47 designates `Jhurling2024/marksman-capital-usa`.
- [x] Personal information, secrets, internal IDs, confidential client data, hidden metadata and machine-specific paths — full-file review of all 20 package files: PASS on every public-release criterion (`docs/COMMON-SENSE-SECURITY-REPORT.md`, 2026-10-16); enforced continuously by `tests/test_skill_package.py` (secret sentinels, machine-path guard) and by CI in both layouts (origin repository: root workflow on `common-sense/**`; public repository: the in-package workflow on every push/PR).
- [x] Packaging/static tests and independent behavioral evaluation, with evidence — 9/9 package tests (SHA-256 manifest freshness, frontmatter, version consistency, category coverage, sentinel and path guards); blind-graded comparative evaluation, 31 scenarios: baseline 27/31, skilled 30/31, zero regressions (`tests/evaluation-results.md`; full report `docs/COMMON-SENSE-EVALUATION-REPORT.md` in the origin repository).
- [x] MIT license verified (`LICENSE`, frontmatter, `CITATION.cff`, security review item 9); the owner's directive acknowledges competitors can freely use/fork/sell derived versions.
- [x] Explicit owner approval to publish source files — Issue #47, 2026-10-16.
- [ ] **Trademark:** no USPTO/name screening performed for "common-sense-skill" (status UNKNOWN). Required before selling branded services or claiming exclusivity; not required for MIT code publication.
- [ ] GitHub Sponsors / paid consulting: banking, 2FA, tax and marketplace policies unconfirmed. Not required for this release; required before monetization (see `docs/MONETIZATION.md`).
- [x] Minimal package published — only the files listed in `SHA256SUMS` plus this checklist.

## Security review finding F-03 — RESOLVED 2026-10-16

Owner sign-off **approved as-is** (owner decision recorded in Issue #47): the price
points and candid unsigned-IP/trademark status notes in `docs/MONETIZATION.md` are
cleared for public viewing in the dedicated public repository.

## Visibility — DECIDED 2026-10-16 (owner)

- **Dedicated public repository** `Jhurling2024/common-sense-skill` carries the audited
  package only (root layout). The application code in `marksman-capital-usa` remains
  private and was never part of this publication scope (it was not security-audited).
- The `marksman-capital-usa` release stays as the private integration copy and origin
  of the release history (tags, PRs, evidence docs).
- **Mirror policy:** re-import the `common-sense/` contents into the public repository
  whenever a new release tag is cut here, and verify `SHA256SUMS` + package tests in
  both places after every import.

## Publish steps (executed 2026-10-16)

1. Release branch `release/common-sense-skill` carrying the package under `common-sense/`.
2. Focused pull request with this checklist, the source inventory, security report,
   evaluation report, `SHA256SUMS` and CI evidence.
3. CI workflow `common-sense-package-tests` runs the package tests on the PR.
4. Merge through the repository's normal (owner-controlled) process; tag `v0.1.3`
   and publish a GitHub Release from the tag (`v0.1.2` superseded the same day —
   checkout-integrity fix, see `CHANGELOG.md`).
5. Third-party installation: copy or clone the `common-sense/` directory into an
   agent's skills directory and verify files against `SHA256SUMS`. Do not use zipball
   uploads that bypass `.gitignore` (bytecode exclusions; security review F-01).
6. Public distribution (2026-10-16, owner decision): create
   `Jhurling2024/common-sense-skill` (public), import the released package as the
   initial commit, tag `v0.1.4`, publish a GitHub Release, and verify `SHA256SUMS` +
   package tests from a fresh clone.
7. Public in-place verification fix (2026-10-16, v0.1.5): fresh-clone verification of
   the public `v0.1.4` import showed `SHA256SUMS` 21/21 correct but the package tests
   failing when the package **is** the repository root — the coverage check enumerated
   `.git/**`. Fixed the test to exclude VCS internals, added the in-package CI
   workflow, re-imported as `v0.1.5`, and verified `SHA256SUMS` (22 entries) + 9/9
   tests from a fresh clone of the public tag; public `v0.1.4` marked superseded.

**Approval record:** approved by repository owner Justin Hurling via Issue #47 on
2026-10-16; release executed under directive ATLAS-CS-RELEASE-20261016-001.
