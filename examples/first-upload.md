# Example: First Local Project Upload

The user has confirmed this context:

> I want to publish my local project for the first time. I am currently in PowerShell, but I do not know whether the directory is already a Git repository.

The coach does not dump the complete upload workflow. It starts with one read-only observation:

```text
当前目的：
确认当前目录是不是 Git 仓库，避免重复初始化或操作错误目录。

你现在只做：
git status

正常情况下：
Git 会显示当前分支和工作区状态；如果这里不是仓库，会返回明确报错。

完成后请回复：
请粘贴完整输出或报错原文。
```

If the user reports `fatal: not a git repository`, the coach does not assume that `git init` is correct. It first verifies the intended directory.

The flow continues one result at a time. Before files are staged for the first upload, the coach performs a separate secret and large-file check.
