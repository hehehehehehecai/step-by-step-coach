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

    def test_environment_reference_covers_secret_lifecycle(self):
        reference = (VERCEL / "references" / "environment-security.md").read_text(encoding="utf-8")
        for phrase in (
            "Development",
            "Preview",
            "Production",
            "NEXT_PUBLIC_",
            "VITE_",
            "Sensitive Environment Variables",
            "不得要求用户发送真实",
            "重新部署",
            "撤销或轮换",
            "不回显",
        ):
            self.assertIn(phrase, reference)

    def test_deployment_reference_covers_full_lifecycle(self):
        reference = (VERCEL / "references" / "deployment-scenarios.md").read_text(encoding="utf-8")
        for phrase in (
            "GitHub",
            "GitLab",
            "Bitbucket",
            "Framework Preset",
            "Root Directory",
            "Preview",
            "Production",
            "Promote",
            "Rollback",
            "Hobby",
            "Functions",
        ):
            self.assertIn(phrase, reference)

    def test_deployment_reference_separates_promoted_and_current_states(self):
        reference = (VERCEL / "references" / "deployment-scenarios.md").read_text(encoding="utf-8")
        self.assertRegex(reference, r"(?m)^\| Promoted \|")
        self.assertRegex(reference, r"(?m)^\| Current \|")

    def test_domain_reference_uses_live_targets_and_protects_mail(self):
        reference = (VERCEL / "references" / "domains-and-dns.md").read_text(encoding="utf-8")
        for phrase in ("A", "CNAME", "TXT", "NS", "MX", "CAA", "SSL", "TTL", "传播"):
            self.assertIn(phrase, reference)
        self.assertIn("Dashboard 当前显示", reference)
        self.assertIn("不得清空", reference)
        self.assertNotIn("76.76.21.21", reference)
        self.assertIn("_acme-challenge 子域委派不同于整域 Nameserver 切换", reference)
        self.assertIn("从项目移除或删除域名", reference)

    def test_troubleshooting_reference_is_evidence_driven(self):
        reference = (VERCEL / "references" / "troubleshooting.md").read_text(encoding="utf-8")
        for phrase in (
            "Git 集成",
            "构建",
            "运行时",
            "环境变量",
            "Functions",
            "域名",
            "网络",
            "权限",
            "套餐",
            "完整报错",
            "一次只检查一个",
        ):
            self.assertIn(phrase, reference)

    def test_readmes_document_vercel_installation(self):
        for name in ("README.md", "README.zh-CN.md"):
            readme = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn("step-by-step-vercel", readme)
            self.assertIn("environment", readme.lower())
            self.assertIn("Vercel", readme)

    def test_production_risk_card_covers_requested_change_set(self):
        skill = (VERCEL / "SKILL.md").read_text(encoding="utf-8")
        risk_section = skill.split("## 风险确认契约", 1)[1].split("## 完成标准", 1)[0]
        for phrase in (
            "不得索要或回显",
            "Hobby",
            "Dashboard 当前显示",
            "实时 DNS",
            "MX",
            "重新部署",
        ):
            self.assertIn(phrase, risk_section)

    def test_high_risk_actions_use_one_confirmation_per_imminent_action(self):
        skill = (VERCEL / "SKILL.md").read_text(encoding="utf-8")
        risk_section = skill.split("## 风险确认契约", 1)[1].split("## 完成标准", 1)[0]
        for phrase in (
            "删除项目",
            "删除部署",
            "删除域名",
            "发布或提升到 Production",
            "Production 重新部署",
            "Rollback",
            "修改或删除 DNS",
            "删除或覆盖任何环境的变量",
            "改变环境变量作用域",
            "Production Branch",
            "Root Directory",
            "Build Command",
            "Output Directory",
            "访问保护",
            "成员或项目权限",
            "每次确认只授权一个紧接着要执行的高风险动作",
            "其余高风险动作仍为待处理，尚未获得授权",
        ):
            self.assertIn(phrase, risk_section)
        self.assertIn("Dashboard 当前显示的 Custom Environment", skill)

    def test_environment_reference_covers_custom_environments_and_access_controls(self):
        reference = (VERCEL / "references" / "environment-security.md").read_text(encoding="utf-8")
        for phrase in (
            "Custom Environments",
            "Pro/Enterprise",
            "不得推断变量继承或隔离关系",
            "分支专用变量",
            "单独项目",
            "不等同于隔离",
            "Deployment Protection",
            "Standard Protection",
            "最小权限",
            "不得索要 Cookie、绕过密钥、会话数据或凭据",
        ):
            self.assertIn(phrase, reference)

    def test_deployment_reference_marks_all_production_configuration_changes_high_risk(self):
        reference = (VERCEL / "references" / "deployment-scenarios.md").read_text(encoding="utf-8")
        for phrase in (
            "Production Branch",
            "Root Directory",
            "Build Command",
            "Output Directory",
            "删除部署",
            "每次确认只授权一个紧接着要执行的高风险动作",
        ):
            self.assertIn(phrase, reference)


if __name__ == "__main__":
    unittest.main()
