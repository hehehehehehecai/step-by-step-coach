# 一步一教子 Skill 发现与恢复设计

## 背景与已确认根因

真实失败表现为：父 Skill 已进入 Git 教学路由，但声称缺少 `step-by-step-git`，并把“请提供路径或安装子 Skill”作为四标题教学卡中的下一步。

只读检查确认仓库、本机安装和 Obsidian 备份中的 `step-by-step-git` 均完整、结构校验通过且逐文件 SHA-256 一致。根因是其 `agents/openai.yaml` 设置了 `policy.allow_implicit_invocation: false`；Codex 规范说明该值为 `false` 时 Skill 不会默认注入模型上下文，只能由用户显式 `$step-by-step-git` 调用。Vercel 子 Skill 当前进入了可用 Skill 列表，但尚未经过父级真实路由验证。

## 目标

让 `step-by-step-coach` 能稳定路由 Git 和 Vercel 子 Skill，并在依赖未加载或确实缺失时进入基础设施恢复，而不是把安装依赖冒充为用户的一步一教操作。

## 名称与触发边界

- 保持 `step-by-step-coach`、`step-by-step-git` 和 `step-by-step-vercel` 名称不变。
- 用户明确要求“一步一教”并确认 Git/GitHub 背景后，父 Skill 隐式加载 Git 子 Skill。
- 用户确认 Vercel 背景后，父 Skill隐式加载 Vercel 子 Skill。
- 用户仍可通过 `$step-by-step-git` 或 `$step-by-step-vercel` 显式调用子 Skill。
- 普通 Git/Vercel 概念问答不因本次修改自动进入一步一教。

## 文件与职责

### Git 子 Skill 元数据

将 `skills/step-by-step-git/agents/openai.yaml` 的 `allow_implicit_invocation` 改为 `true`。

### Vercel 子 Skill 元数据

在 `skills/step-by-step-vercel/agents/openai.yaml` 显式写入 `allow_implicit_invocation: true`，避免依赖默认值造成迁移歧义。Vercel 的 `SKILL.md` 与四份参考文件不变。

### 父 Skill

在领域路由前加入统一的子 Skill 可用性预检：

1. 当前任务可发现目标子 Skill时，完整读取并进入教学。
2. 当前任务不可发现，但 `<CODEX_HOME>/skills/<child>/SKILL.md` 存在时，退出教学状态，说明安装已存在但当前任务目录未刷新，需要重启 Codex；不得索要路径。
3. 本机文件不存在时，退出教学状态，只读寻找仓库副本或知识库备份。
4. 找到完整副本时进入恢复流程；安装写入需要权限时再申请。
5. 没有完整副本时明确报告依赖缺失，不临时复制子 Skill 规则到父 Skill。

依赖检查是 Codex 基础设施动作，不使用四标题教学卡，也不算作用户的 Git/Vercel 操作。

### README

保留三个同级 Skill 的安装说明，并补充：

- Git、Vercel 都允许父 Skill 隐式路由；
- 安装或更新后必须重启 Codex；
- 子 Skill 文件存在但当前任务不可见时，不要让用户提供路径，应重启刷新；
- 三个 Skill 目录必须完整复制。

## 风险与错误处理

- 不在依赖检查中执行 Git、GitHub 或 Vercel 操作。
- 不静默覆盖不一致的本机或知识库版本。
- 不删除目标树中的额外文件；检测到版本冲突时停止并请求选择基准。
- 当前任务的 Skill 目录不会因文件写入动态刷新；重启前只报告文件和配置已更新，不宣称运行时目录已刷新。

## 验收

### RED

使用用户提供的真实截图作为行为失败证据，并用静态合同证明 Git 的隐式调用开关为 `false`、父 Skill 缺少依赖预检。

### GREEN

只执行以下四个互不重复的 fresh-context 行为检查：

1. Git 父级路由；
2. Vercel 父级路由；
3. 普通概念问答非触发；
4. 子 Skill 不可发现时的依赖边界。

同时验证三个 Skill 的结构、元数据、README、引用和凭据扫描。

### 安装与迁移

- 仓库、本机、知识库三处完整同步三个 Skill；实际内容未变的文件不重复覆盖。
- 更新能力卡、最新《Codex 个人 Skill 迁移说明》和更新日志 `N+1`。
- 只从知识库备份恢复到临时目录，验证三个 Skill 的相对路径、文件数量和 SHA-256。
- 最终要求用户重启 Codex；重启后的可用 Skill 目录必须同时出现 Git 与 Vercel 子 Skill，才能完成运行时验收。

