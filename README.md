# Step-by-Step Coach

[English](README.md) | [简体中文](README.zh-CN.md)

> A one-action-at-a-time Codex coach for Git and GitHub workflows.

Most Git tutorials give you an entire checklist. That works until you are unfamiliar with the workflow, hit an unexpected error, or worry that the next command may destroy work.

Step-by-Step Coach uses a different contract:

- one command or one GitHub action per turn;
- wait for the real result before continuing;
- adapt the next action to that result;
- stop before force push, history rewrites, destructive resets, branch deletion, PR merge, or possible secret exposure;
- optionally read a user-selected Codex task and confirm its context before starting.

It is designed for Git beginners, occasional Git users, non-developers working with repositories, and anyone who prefers a calm interactive guide over a long procedure.

## Skills

This repository contains two sibling Codex Skills:

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

`step-by-step-coach` owns the generic teaching contract, source-task handoff, context confirmation, waiting state, and safety gates.

`step-by-step-git` owns Git and GitHub state detection, error recovery, and scenario-specific decisions.

Keep them as sibling directories. Do not place the Git Skill inside the parent Skill.

## Install

Clone this repository, then copy both Skill directories into your personal Codex Skills directory.

### Windows PowerShell

```powershell
Copy-Item -Recurse -LiteralPath ".\skills\step-by-step-coach" -Destination "$env:USERPROFILE\.codex\skills"
Copy-Item -Recurse -LiteralPath ".\skills\step-by-step-git" -Destination "$env:USERPROFILE\.codex\skills"
```

### macOS or Linux

```bash
cp -R ./skills/step-by-step-coach ~/.codex/skills/
cp -R ./skills/step-by-step-git ~/.codex/skills/
```

Restart Codex after installation.

## Use

Start a fresh Codex task and invoke:

```text
$step-by-step-coach
```

If your Codex environment exposes `list_threads` and `read_thread`, the parent Skill can show recent tasks, read the task you select, and produce a context confirmation card. It never sends messages to, renames, archives, or otherwise changes the source task.

If the source task is unavailable—for example, after moving to another computer—provide a task summary, a handoff file, or a project note instead.

After you confirm the context, a normal teaching turn follows this fixed shape:

```text
Current purpose:
[why this single action is needed]

Do only this now:
[one command or one GitHub action]

Normally you should see:
[the success signal]

Reply with:
[the complete output, exact error, or a screenshot]
```

The installed Skills use the equivalent Chinese field names.

## Covered Git and GitHub Scenarios

- first upload of a local project;
- status, staging, commit, and push;
- branches and upstream tracking;
- creating and updating pull requests;
- pulling remote updates;
- non-fast-forward errors;
- merge conflicts;
- authentication, permission, remote, and branch-name errors;
- destructive-operation and secret-exposure gates.

The first version intentionally does not cover server deployment, website release, Docker operations, or package publishing.

## Safety Model

The coach must pause before:

- force push;
- rewriting commit history;
- deleting branches;
- discarding uncommitted work;
- hard reset or rollback;
- overwriting remote state;
- merging or closing a pull request;
- uploading `.env` files, tokens, private keys, credentials, databases, or suspiciously large files.

The confirmation turn explains the target, impact, consequences, and a safer alternative. It must not contain an executable destructive command.

## Examples

- [First local project upload](examples/first-upload.md)
- [Force-push safety gate](examples/force-push-safety.md)

## 中文说明

“一步一教”不是另一份 Git 命令大全。它解决的是长步骤带来的认知压力和操作焦虑：

- 每轮只做一个动作；
- 必须根据真实输出决定下一步；
- 用户没有反馈前不得继续；
- 危险操作先解释影响并单独确认；
- Codex 只负责指导，不替用户执行 Git 或 GitHub 操作。

父 Skill 可以在新的 Codex 任务中只读接续用户选定的来源任务。`list_threads` 和 `read_thread` 是 Codex 环境提供的系统工具，不包含在本仓库中；旧任务不可见时，可以改用任务摘要、上下文交接文件或知识库记录。

## License

[MIT](LICENSE)
