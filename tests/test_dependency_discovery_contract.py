from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
PARENT = SKILLS / "step-by-step-coach" / "SKILL.md"


class DependencyDiscoveryContractTests(unittest.TestCase):
    def test_both_children_explicitly_allow_implicit_invocation(self):
        for child in ("step-by-step-git", "step-by-step-vercel"):
            metadata = (SKILLS / child / "agents" / "openai.yaml").read_text(
                encoding="utf-8"
            )
            self.assertRegex(
                metadata,
                r"(?ms)^policy:\s*\n\s+allow_implicit_invocation:\s*true\s*$",
                child,
            )

    def test_parent_has_all_dependency_preflight_states(self):
        parent = PARENT.read_text(encoding="utf-8")
        self.assertIn("## 子 Skill 可用性预检", parent)
        for phrase in (
            "当前任务可发现",
            "标准安装位置存在",
            "仓库副本或知识库备份",
            "所有位置均不存在",
        ):
            self.assertIn(phrase, parent)

    def test_dependency_repair_is_not_a_teaching_step_or_path_request(self):
        parent = PARENT.read_text(encoding="utf-8")
        self.assertIn("## 子 Skill 可用性预检", parent)
        preflight = parent.split("## 子 Skill 可用性预检", 1)[1].split(
            "## 领域路由", 1
        )[0]
        for phrase in (
            "Codex 基础设施动作",
            "四标题教学卡之外",
            "不得要求用户提供子 Skill 路径",
            "不计入 Git 或 Vercel 教学步骤",
        ):
            self.assertIn(phrase, preflight)
        self.assertNotRegex(preflight, r"请提供.*(?:Skill|skill).*路径")

    def test_readmes_explain_implicit_routing_and_stale_catalog(self):
        expectations = {
            "README.md": (
                "implicit routing",
                "all three complete Skill directories",
                "restart Codex",
                "catalog",
            ),
            "README.zh-CN.md": (
                "隐式路由",
                "三个完整的 Skill 目录",
                "重启 Codex",
                "目录",
            ),
        }
        for filename, phrases in expectations.items():
            readme = (ROOT / filename).read_text(encoding="utf-8")
            for phrase in phrases:
                self.assertIn(phrase, readme, f"{filename}: {phrase}")

    def test_parent_routes_only_after_confirmed_domain(self):
        parent = PARENT.read_text(encoding="utf-8")
        self.assertRegex(parent, r"用户明确确认.*Git")
        self.assertRegex(parent, r"用户明确确认.*Vercel")
        self.assertIn("普通概念问答", parent)


if __name__ == "__main__":
    unittest.main()
