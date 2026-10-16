# Behavioral evaluation results (2026-10-16; run against the v0.1.2 package — the skill body is unchanged since v0.1.2)

Comparative, blind-graded evaluation: same model both arms
(`opencode/mimo-v2.6-flash-free`), identical scenario prompts, ≤60 words per case,
separate sessions per arm, randomized blind pairing, grader never saw arm identities.

| Arm | PASS | Rate |
|---|---|---|
| Baseline (no skill) | 27/31 | 87.1% |
| Skilled (skill active) | **30/31** | **96.8%** |

Per category (baseline → skilled): approval 3/5 → 5/5 · architecture 4/5 → 5/5 ·
complexity 5/5 → 5/5 · evidence 6/6 → 6/6 · practical 4/5 → 4/5 · risk 5/5 → 5/5.

- **Zero regressions** — no case passed in baseline and failed in the skilled arm.
- CS-18 failed **both** arms (strict quota-disclosure clause; did not separate the arms).
- Stratum split (controls home-field advantage): skill-origin cases 14/16 → 16/16;
  newly written cases 13/15 → 14/15 — the skilled arm leads in both strata.

Method, failure analysis and limitations: `docs/COMMON-SENSE-EVALUATION-REPORT.md`
in the release repository. Raw artifacts: `docs/evaluation/` (arm responses, blind
pairs, blind key, grader output).

These results describe one run per arm on one model; they do not establish
reliability (pass@k) or generalization beyond this suite.
