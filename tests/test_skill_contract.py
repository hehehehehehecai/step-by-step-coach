from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
VERCEL = ROOT / "skills" / "step-by-step-vercel"
PARENT = ROOT / "skills" / "step-by-step-coach" / "SKILL.md"


class StepByStepVercelContractTests(unittest.TestCase):
    def test_required_skill_files_exist(self):
        expected = {
            VERCEL / "SKILL.md",
            VERCEL / "agents" / "openai.yaml",
            VERCEL / "references" / "deployment-scenarios.md",
            VERCEL / "references" / "environment-security.md",
            VERCEL / "references" / "domains-and-dns.md",
            VERCEL / "references" / "troubleshooting.md",
        }
        self.assertEqual([], sorted(str(path) for path in expected if not path.is_file()))

    def test_frontmatter_and_ui_metadata(self):
        skill = (VERCEL / "SKILL.md").read_text(encoding="utf-8")
        metadata = (VERCEL / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertRegex(skill, r"(?m)^name: step-by-step-vercel$")
        self.assertRegex(skill, r"(?m)^description: Use when ")
        self.assertIn("$step-by-step-vercel", metadata)

    def test_parent_routes_vercel_tasks(self):
        parent = PARENT.read_text(encoding="utf-8")
        self.assertIn("step-by-step-vercel", parent)
        self.assertRegex(parent, r"Vercel|部署|环境变量|域名")

    def test_child_preserves_one_action_contract(self):
        skill = (VERCEL / "SKILL.md").read_text(encoding="utf-8")
        for heading in ("当前目的：", "你现在只做：", "正常情况下：", "完成后请回复："):
            self.assertIn(heading, skill)
        self.assertIn("每轮最多一个", skill)
        self.assertIn("Dashboard", skill)
        self.assertIn("CLI", skill)

    def test_safety_contract_is_explicit(self):
        combined = "\n".join(path.read_text(encoding="utf-8") for path in VERCEL.rglob("*.md"))
        for phrase in (
            "不得要求用户发送真实",
            "Production",
            "Preview",
            "更安全的替代方案",
            "重新部署",
            "MX",
            "Hobby",
        ):
            self.assertIn(phrase, combined)
        self.assertIsNone(re.search(r"sk-[A-Za-z0-9]{20,}", combined))


if __name__ == "__main__":
    unittest.main()
