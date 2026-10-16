# Changelog

## [0.1.4] — owner decisions recorded; public distribution, 2026-10-16

- **Visibility decided by owner:** a dedicated **public** repository
  `Jhurling2024/common-sense-skill` carries the audited package (root layout);
  `marksman-capital-usa` stays private as the release-history origin
  (`docs/PUBLICATION-APPROVAL.md`, "Visibility").
- **Security finding F-03 approved as-is** by the owner: `docs/MONETIZATION.md`
  price points and candid IP-status disclosures are cleared for public viewing.
- `CITATION.cff` `repository-code` now points at the public repository; the README
  records both the release and the public distribution URL.
- No skill-body changes; evaluation results carry over unchanged.

## [0.1.3] — checkout-integrity fix, 2026-10-16

- Added `.gitattributes` (`* -text`) so line-endings can no longer be converted on
  checkout: `SHA256SUMS` now verifies identically on Windows (`core.autocrlf=true`),
  Linux and macOS. The defect was caught by clean-environment verification of the
  v0.1.2 tag: fresh Windows clone 0/20 hashes matched; LF-normalized hashes matched
  exactly, confirming CRLF conversion at checkout as the sole cause.
- No skill-body or behavioral changes; evaluation results carry over unchanged.
- Regenerated `SHA256SUMS` (21 entries, now includes `.gitattributes`).

## [0.1.2] — release preparation, 2026-10-16

- Expanded the behavioral evaluation suite from 16 to 31 scenarios: six categories (practical, complexity, evidence, risk, architecture, approval) with at least five scenarios each, including negative and adversarial cases.
- Added comparative with/without-skill evaluation results (`tests/evaluation-results.md`; full report: `docs/COMMON-SENSE-EVALUATION-REPORT.md`).
- Corrected the frontmatter compatibility claim: invocation verified in OpenCode; other runtimes previously named without verification now marked unverified.
- Extended package tests: 30-scenario minimum, category coverage, adversarial/negative coverage, SHA-256 manifest freshness, machine-specific-path guard.
- Recorded the owner publication approval (GitHub Issue #47, 2026-10-16) in `docs/PUBLICATION-APPROVAL.md`; target repository changed from the proposed standalone repo to `Jhurling2024/marksman-capital-usa`.
- Corrected `CITATION.cff` repository URL to the actual release repository; bumped version metadata to 0.1.2.
- Regenerated `SHA256SUMS` for the full package; added a CI workflow that runs the package tests on changes under `common-sense/`.

## [0.1.1] — ownership and attribution update, draft, 2026-10-14

- Designated Marksman Capital USA LLC as the project/commercial rights holder in license and documentation.
- Preserved prominent Justin Hurling credit as Founder, Originator and Project Creator.
- Added IP ownership/assignment due-diligence checklist and revised monetization contracting guidance.
- This designation is not itself a signed legal assignment or a copyright registration.

## [0.1.0] — draft, 2026-10-14

- Created portable Agent Skills instructions and OpenCode metadata.
- Introduced SENSE Loop, evidence taxonomy, approval classifications and existing-capability audit.
- Added generalized failure-pattern references, planning templates and behavioral evaluation scenarios.
- Added original MIT copyright notice and explicit Justin Hurling originator credit (rights holder designation revised in 0.1.1).
- Added optional sponsorship, consulting and support monetization plan.
- Not yet released or integrated into ATLAS PRIME.
