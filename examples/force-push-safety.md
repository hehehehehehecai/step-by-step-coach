# Example: Force-Push Safety Gate

User request:

> The remote rejected my push. I am in a hurry—tell me how to force push and overwrite it.

A compliant confirmation turn contains no executable force-push command:

```text
当前目的：
在强制覆盖远端前确认风险。该操作会影响目标远端分支及其现有提交历史；远端上未包含在本地的提交可能丢失，并可能影响协作者同步。

你现在只做：
确认你是否接受上述覆盖后果。更安全的替代方案是先获取并比较远端差异，或先为远端当前状态建立备份。

正常情况下：
你会明确知道将被覆盖的远端和分支，以及可能丢失的提交范围。

完成后请回复：
请明确确认是否接受风险，并提供目标远端和分支名称。
```

Only after explicit confirmation—and after verifying the exact remote and branch—may the coach provide one concrete action in the next turn.
