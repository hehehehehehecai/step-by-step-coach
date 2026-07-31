# 一步一教（Step-by-Step Coach）

[English](README.md) | 简体中文

> 一个面向 Git 与 GitHub 操作的 Codex 教练：每轮只教一个动作，等待真实结果后再继续。

很多人第一次接触 Vibe Coding，刚刚让 AI 把想法变成代码，就被 Git、分支、提交和 PR 挡在了下一关。问 AI 怎么办，它常常非常热心地一次甩来十几个步骤——每个字都认识，连在一起却不知道先做什么，更担心输错一条命令把项目弄乱。无论你是完全没有计算机基础，还是只是偶尔使用 Git、总记不住操作流程，“一步一教”都不会催你赶进度：一次只做一件事，确认没问题后再继续。

“一步一教”采用以下协作方式：

- 每轮只提供一个命令或一个 GitHub 网页操作；
- 等待用户反馈真实结果后再继续；
- 根据实际输出、报错或页面状态决定下一步；
- 在强制推送、历史重写、破坏性重置、删除分支、合并 PR 或可能泄露敏感文件前暂停；
- 可以先读取用户指定的 Codex 来源任务，确认上下文后再开始教学。

## Skill 架构

本仓库包含两个互相配合、但彼此独立的 Codex Skill：

```text
skills/
├─ step-by-step-coach/
│  ├─ SKILL.md
│  └─ agents/
│     └─ openai.yaml
└─ step-by-step-git/
   ├─ SKILL.md
   ├─ agents/
   │  └─ openai.yaml
   └─ references/
      └─ scenarios.md
```

### `step-by-step-coach`

父 Skill，负责：

- 通用的单步教学协议；
- 来源任务选择与只读接续；
- 上下文确认；
- 等待用户反馈；
- 高风险操作门禁；
- 根据任务领域调用对应的子 Skill。

### `step-by-step-git`

Git 子 Skill，负责：

- 判断当前 Git 与 GitHub 状态；
- 选择当前唯一需要执行的动作；
- 解释命令输出与报错；
- 处理常见 Git/GitHub 场景；
- 在危险操作前执行安全检查。

两个 Skill 必须作为 Codex Skills 根目录下的同级目录安装。不要把 `step-by-step-git` 放进 `step-by-step-coach` 目录内部。

## 安装

克隆本仓库，然后把两个 Skill 目录复制到个人 Codex Skills 目录。

### Windows PowerShell

```powershell
Copy-Item -Recurse -LiteralPath ".\skills\step-by-step-coach" -Destination "$env:USERPROFILE\.codex\skills"
Copy-Item -Recurse -LiteralPath ".\skills\step-by-step-git" -Destination "$env:USERPROFILE\.codex\skills"
```

### macOS 或 Linux

```bash
cp -R ./skills/step-by-step-coach ~/.codex/skills/
cp -R ./skills/step-by-step-git ~/.codex/skills/
```

安装完成后重启 Codex。

## 使用方式

新建一个 Codex 任务，然后显式调用：

```text
$step-by-step-coach
```

### 接续另一个 Codex 任务

如果当前 Codex 环境提供 `list_threads` 和 `read_thread`，父 Skill 可以：

1. 显示最近的 Codex 任务；
2. 让用户选择需要接续的来源任务；
3. 只读提取任务背景；
4. 生成上下文确认卡；
5. 得到用户确认后再开始 Git 教学。

父 Skill 不会向来源任务发送消息，也不会重命名、归档或改变来源任务的其他状态。

如果旧任务在另一台电脑上不可见，可以改为提供：

- 任务摘要；
- 上下文交接文件；
- 项目记录或知识库笔记。

Skill 会把这些信息整理为相同的上下文确认卡。

## 单步教学格式

确认上下文后，每个普通教学轮次固定使用以下格式：

```text
当前目的：
[说明当前动作解决什么问题]

你现在只做：
[一个命令，或一个 GitHub 网页操作]

正常情况下：
[描述完成后应该看到的结果]

完成后请回复：
[要求粘贴完整输出、报错原文或页面截图]
```

强制规则：

- 每轮最多一个操作；
- 不使用 `&&`、`;`、管道或脚本串联多个动作；
- 不提前展示后续步骤；
- 不一次性给出完整操作清单；
- 不猜测路径、分支名、远端地址或仓库名称；
- 用户没有反馈前不得继续；
- Codex 只负责指导，不代替用户执行 Git 或 GitHub 操作。

## 当前覆盖的 Git 与 GitHub 场景

- 第一次把本地项目上传到 GitHub；
- 查看仓库状态；
- 暂存与提交修改；
- 推送当前分支；
- 创建和切换分支；
- 创建 Pull Request；
- 更新已有 Pull Request；
- 拉取远端更新；
- 合并 Pull Request；
- 处理 non-fast-forward；
- 处理未提交修改；
- 处理合并冲突；
- 处理认证、权限、远端地址和分支名错误。

第一版暂不覆盖：

- 服务器部署；
- 网站发布；
- Docker 操作；
- npm 或其他软件包发布。

这些领域可以在后续通过增加新的子 Skill 扩展。

## 安全机制

以下操作必须在给出具体命令或网页操作前单独暂停：

- force push；
- 重写提交历史；
- 删除本地或远端分支；
- 丢弃未提交修改；
- hard reset 或回退到旧提交；
- 覆盖远端状态；
- 合并或关闭 Pull Request；
- 上传 `.env`、Token、SSH 私钥、凭据、数据库或异常大文件。

高风险确认轮必须说明：

- 准备执行的动作；
- 影响的对象；
- 可能造成的后果；
- 更安全的替代方案；
- 需要用户明确确认的内容。

用户确认前不得提供可直接执行的破坏性命令。

## 这个 Skill 适合谁

它不是另一份 Git 命令大全，也不是为了替代所有自动化操作。

它更适合：

- 刚开始尝试 Vibe Coding、没有计算机基础的用户；
- 刚开始使用 Git 和 GitHub 的用户；
- 只会基本 `commit`、`push`，遇到异常就不知道如何继续的人；
- 很久才操作一次、记不住流程顺序的人；
- 需要接触仓库的产品经理、设计师、运营或独立创作者；
- 希望理解每一步，而不是完全把仓库交给 AI 操作的人；
- 对删除、覆盖和历史重写等操作比较谨慎的人；
- 容易被长步骤和大量信息压垮的人。

它解决的主要问题不是“缺少 Git 命令”，而是：

> 降低操作过程中的认知负担和焦虑，让每一步都能被理解、执行和验证。

## 示例

- [第一次上传本地项目](examples/first-upload.md)
- [Force Push 风险确认](examples/force-push-safety.md)

## 已知边界

- `list_threads` 和 `read_thread` 是 Codex 环境提供的系统工具，不包含在本仓库中；
- 不同 Codex 环境能够看到的历史任务可能不同；
- 来源任务不可见时需要人工提供任务摘要或交接材料；
- Skill 不保存 GitHub Token、密码、SSH 私钥或其他凭据；
- Skill 不会替用户执行真实的 Git 命令或 GitHub 页面操作。

## 贡献

欢迎提交 Issue 或 Pull Request，例如：

- 补充新的 Git/GitHub 场景；
- 改进新手提示和错误解释；
- 增加新的领域子 Skill；
- 提供真实使用案例；
- 修复可能绕过单步协议或风险门禁的情况。

提交贡献时，请勿包含真实 Token、密码、私钥、个人绝对路径或其他敏感信息。

## License

本项目使用 [MIT License](LICENSE)。
