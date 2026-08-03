# 一步一教（Step-by-Step Coach）

[English](README.md) | 简体中文

> 面向 Git/GitHub 与 Vercel 的 Codex 单步操作教练：一次只教一个动作，等真实结果回来再继续。

很多教程会一次性给出完整清单。“一步一教”换了一种方式：先只做一件事，等你提供真实页面、输出或报错，再根据证据决定下一步。它适合 Git 新手、偶尔操作的人、需要接触仓库的非开发者，以及刚开始 Vibe Coding、希望先弄懂再动手的用户。

## Skill 架构

本仓库包含三个互相配合、彼此独立的 Codex Skill。安装或复制时必须保留每个目录及其全部子目录。

```text
skills/
├─ step-by-step-coach/
│  ├─ SKILL.md
│  └─ agents/
│     └─ openai.yaml
├─ step-by-step-git/
│  ├─ SKILL.md
│  ├─ agents/
│  │  └─ openai.yaml
│  └─ references/
│     └─ scenarios.md
└─ step-by-step-vercel/
   ├─ SKILL.md
   ├─ agents/
   │  └─ openai.yaml
   └─ references/
      ├─ deployment-scenarios.md
      ├─ environment-security.md
      ├─ domains-and-dns.md
      └─ troubleshooting.md
```

- `step-by-step-coach`：负责上下文确认、固定单步回复格式、等待和风险门禁。
- `step-by-step-git`：负责 Git/GitHub 状态判断、报错处理和安全仓库操作。
- `step-by-step-vercel`：在父 Skill 确认背景后，负责 Vercel 部署与配置判断。

## 安装

克隆本仓库后，将三个完整的 Skill 目录复制到个人 Codex Skills 目录。

### Windows PowerShell

```powershell
Copy-Item -Recurse -LiteralPath ".\skills\step-by-step-coach" -Destination "$env:USERPROFILE\.codex\skills"
Copy-Item -Recurse -LiteralPath ".\skills\step-by-step-git" -Destination "$env:USERPROFILE\.codex\skills"
Copy-Item -Recurse -LiteralPath ".\skills\step-by-step-vercel" -Destination "$env:USERPROFILE\.codex\skills"
```

### macOS 或 Linux

```bash
cp -R ./skills/step-by-step-coach ~/.codex/skills/
cp -R ./skills/step-by-step-git ~/.codex/skills/
cp -R ./skills/step-by-step-vercel ~/.codex/skills/
```

安装后重启 Codex。

## 使用方式

新建一个 Codex 任务，然后调用：

```text
$step-by-step-coach
```

如果环境提供 `list_threads` 和 `read_thread`，父 Skill 会只读你选定的来源任务，并要求你先确认上下文，再路由到 Git/GitHub 或 Vercel。旧任务不可见时，可以提供任务摘要、交接文件或项目笔记。

每个普通教学回复都使用“当前目的、你现在只做、正常情况下、完成后请回复”四个字段；在你反馈本轮结果前，不会给下一步。

## Vercel 覆盖范围

Vercel 子 Skill 只处理既有代码周边的部署与配置：从 GitHub、GitLab 或 Bitbucket 导入仓库，构建设置，Preview 与 Production，提升或回滚部署，环境变量与密钥，Functions，域名、DNS 与 SSL，日志、排错和访问保护。

它默认 Dashboard-first：优先给一个 Vercel Dashboard 网页操作；只有 Dashboard 无法完成、你明确偏好 CLI，或确实需要可复现的本地诊断时，才会给一个 CLI 命令。

它默认 Hobby-first：涉及保留、回滚、访问保护、团队控制等可能受套餐影响的能力时，先确认项目是否为 Hobby 以及 Dashboard 实际显示的能力；有免费替代方案时会先说明，不会臆测套餐能力。

## 安全机制

以下操作必须先得到明确确认：force push、重写历史、破坏性重置、删除分支、合并 PR、发布或提升到 Production、回滚、覆盖或删除环境变量、可能影响用户的重新部署、DNS 修改以及访问控制修改。确认轮会说明准备做什么、影响对象、可能不可逆后果和更安全的替代方案，但不会包含可直接执行的生产操作。

处理 environment 配置时，Skill 不会索要、保存或回显真实密钥、Token、Cookie、完整环境变量值或未遮盖截图；会先确认唯一目标环境或分支，区分 `NEXT_PUBLIC_`、`VITE_` 等客户端公开前缀与密钥，并提醒环境变量修改后需要重新部署才会生效。

处理域名和 DNS 时，Skill 会以 Vercel Dashboard 当前显示的实时记录目标为准，不会写死 DNS 值；会先询问既有邮箱依赖，绝不删除、覆盖或清空 MX 记录。DNS、Nameserver 和证书委派都必须单独经过风险确认。

## 已知边界

这些 Skill 只负责一次一个动作的安全教学：不编写业务代码，不代替你执行被教学的 Git 或 Vercel 操作，不保存凭据，也不能保证第三方服务一定接受某项配置。当前暂不覆盖 Docker 和软件包发布。没有配置对应子 Skill 的领域，父 Skill 会明确说明，而不是假装提供完整教学流程。

## 示例

- [第一次上传本地项目](examples/first-upload.md)
- [Force Push 风险确认](examples/force-push-safety.md)

## License

[MIT License](LICENSE)
