# 子 Skill 发现与恢复行为记录

## RED：真实失败基线

- 日期：2026-08-04
- 输入背景：用户已明确要求“一步一教”处理 Git 问题；仓库、本机安装和 Obsidian 备份中的 `step-by-step-git` 均包含完整的 `SKILL.md`、`agents/openai.yaml` 和 `references/scenarios.md`。
- 文件验证：三处逐文件 SHA-256 一致，安装副本通过 `quick_validate.py`。
- 实际失败：父 Skill 回复“当前环境缺少必需的 `step-by-step-git` 子 Skill”，并要求用户“请提供 `step-by-step-git` 的路径，或回复‘帮我查找并安装’”。
- 根因证据：`step-by-step-git/agents/openai.yaml` 设置 `allow_implicit_invocation: false`，使子 Skill 不进入默认可发现上下文。
- 判定：失败。已安装依赖被误判为缺失，基础设施恢复又被包装成四标题教学步骤。
- 合同测试：2026-08-04 运行一次，共 5 项；4 项失败、1 项因预检章节不存在而报错。失败点分别覆盖子 Skill 元数据、父级预检、确认后路由和 README 说明，未发现与设计无关的失败。

## GREEN：四个独立行为检查

实现完成后只记录以下四次 fresh-context 检查，不增加重复样本：

1. Git 父级路由：待执行。
2. Vercel 父级路由：待执行。
3. 普通概念问答非触发：待执行。
4. 子 Skill 不可发现边界：待执行。
