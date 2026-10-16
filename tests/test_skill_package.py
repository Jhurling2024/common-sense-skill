"""Static packaging tests; do NOT mistake these for LLM behavior verification."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


class SkillPackageTests(unittest.TestCase):
    def test_required_files(self):
        for name in ["SKILL.md", "LICENSE", "README.md", "CITATION.cff", "AUTHORS.md"]:
            self.assertTrue((ROOT / name).is_file(), name)

    def test_frontmatter(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        block = text.split("---\n", 2)[1]
        self.assertRegex(block, r"(?m)^name: common-sense-skill$")
        self.assertRegex(block, r"(?m)^description: .{10,1024}$")
        self.assertRegex(block, r"(?m)^license: MIT$")
        self.assertRegex(block, r'(?m)^  opencode/slash: "true"$')
        self.assertTrue(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", "common-sense-skill"))
        self.assertLess(len(text.splitlines()), 500)

    def test_referenced_relative_files(self):
        body = SKILL.read_text(encoding="utf-8")
        for rel in re.findall(r"`((?:references|templates|tests)/[^`]+)`", body):
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_author_credited(self):
        self.assertIn("Copyright (c) 2026 Marksman Capital USA LLC", (ROOT / "LICENSE").read_text())
        self.assertIn("Founder, Originator and Project Creator", (ROOT / "README.md").read_text())
        self.assertIn("Justin Hurling", (ROOT / "README.md").read_text())
        self.assertIn("Hurling", (ROOT / "CITATION.cff").read_text())

    def test_evals_present_and_unique(self):
        ev = json.loads((ROOT / "tests/evaluation-cases.json").read_text())
        # Release directive ATLAS-CS-RELEASE-20261016-001 section 7:
        # at least 30 scenarios, six categories with >= 5 each,
        # plus negative and adversarial coverage.
        self.assertGreaterEqual(len(ev), 30)
        self.assertEqual(len({e["id"] for e in ev}), len(ev))
        for e in ev:
            self.assertTrue(all(e.get(k) for k in ("id", "scenario", "must", "must_not")))
        categories = {
            "practical", "complexity", "evidence",
            "risk", "architecture", "approval",
        }
        counts = {}
        for e in ev:
            cat = e.get("cat")
            self.assertIn(cat, categories, f"{e['id']}: missing/unknown cat")
            counts[cat] = counts.get(cat, 0) + 1
        self.assertEqual(set(counts), categories)
        for cat, n in counts.items():
            self.assertGreaterEqual(n, 5, f"category {cat} has only {n} scenarios")
        types = {}
        for e in ev:
            t = e.get("type", "positive")
            self.assertIn(t, ("positive", "negative", "adversarial"), e["id"])
            types[t] = types.get(t, 0) + 1
        self.assertGreaterEqual(types.get("adversarial", 0), 2)
        self.assertGreaterEqual(types.get("negative", 0), 2)

    def test_no_embedded_private_secrets(self):
        # A sentinel check, not a credential scanner or security certification.
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts:
                continue
            if path.suffix not in (".md", ".json", ".cff", ""):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            self.assertNotIn("ghp_", text, str(path))
            self.assertNotIn("sk-proj-", text, str(path))

    def test_sha256_manifest_current(self):
        # Reproducible packaging: every manifest hash must match its file, and
        # the manifest must cover exactly the package files.
        import hashlib
        entries = []
        for line in (ROOT / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
            if line.strip():
                digest, rel = line.split("  ", 1)
                entries.append((digest, rel))
        self.assertTrue(entries, "manifest must not be empty")
        listed = set()
        for digest, rel in entries:
            f = ROOT / rel
            self.assertTrue(f.is_file(), f"manifest lists missing file {rel}")
            actual = hashlib.sha256(f.read_bytes()).hexdigest()
            self.assertEqual(actual, digest, f"stale manifest hash for {rel}")
            listed.add(rel)
        on_disk = set()
        for p in ROOT.rglob("*"):
            if not p.is_file():
                continue
            rel = p.relative_to(ROOT).as_posix()
            if rel == "SHA256SUMS" or "__pycache__" in rel.split("/"):
                continue
            on_disk.add(rel)
        self.assertEqual(listed, on_disk, "manifest must cover exactly the package files")

    def test_no_machine_specific_paths(self):
        # Release rule (Issue #47): public artifacts carry no machine-specific paths.
        needles = ["C:" + "\\Users", "C:/Users", "/home/", "OneDrive"]
        for path in ROOT.rglob("*"):
            if not path.is_file() or path.name == Path(__file__).name:
                continue
            if path.suffix not in (".md", ".json", ".cff", "", ".example"):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for needle in needles:
                self.assertNotIn(needle, text, f"{path.name}: {needle}")

    def test_version_consistency(self):
        # Metadata validation: one version across SKILL.md, CHANGELOG, CITATION, README.
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        m = re.search(r'(?m)^  version: "([0-9]+\.[0-9]+\.[0-9]+)"$', skill)
        self.assertTrue(m, "frontmatter metadata.version missing")
        version = m.group(1)
        self.assertIn(
            f"## [{version}]",
            (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"),
            f"CHANGELOG has no entry for {version}",
        )
        self.assertIn(
            f'version: "{version}"',
            (ROOT / "CITATION.cff").read_text(encoding="utf-8"),
            f"CITATION version differs from {version}",
        )
        self.assertIn(version, (ROOT / "README.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
