# Step-by-Step Coach Dependency Discovery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the parent Skill reliably discover Git and Vercel children and route dependency failures outside the teaching protocol.

**Architecture:** Keep all three Skills as sibling directories. Fix child discovery through explicit metadata, add a parent-side preflight state machine, then synchronize repository, local installation, Obsidian backups, migration documentation, and recovery evidence.

**Tech Stack:** Codex Skills Markdown/YAML, Python `unittest`, `quick_validate.py`, PowerShell SHA-256 verification, Git worktree.

## Global Constraints

- Do not copy Git or Vercel domain rules into the parent Skill.
- Do not treat dependency installation as a four-heading teaching action.
- Do not ask the user to provide a child Skill path when the standard installation path can be checked.
- Run exactly four non-repeated behavior checks: Git route, Vercel route, non-trigger, missing-child boundary.
- Do not claim the current task catalog refreshed before Codex restarts.
- Knowledge-base writes require latest-read, deduplication, `N+1`, and post-write verification.

---

### Task 1: Capture RED and add dependency contracts

**Files:**
- Create: `tests/test_dependency_discovery_contract.py`
- Create: `tests/skill-evals/dependency-discovery-results.md`

**Interfaces:**
- Consumes: the approved design and the user's real screenshot failure.
- Produces: executable contracts and an honest baseline record.

- [ ] **Step 1: Record the real RED**

Record that the current parent response asked for a `step-by-step-git` path despite complete matching source/install/backup trees. Do not invent another behavioral failure.

- [ ] **Step 2: Write focused failing contracts**

Add tests that parse both `agents/openai.yaml` files and require explicit `allow_implicit_invocation: true`; verify the parent contains observable branches for “available”, “installed but catalog stale”, “missing but recoverable”, and “missing everywhere”; verify the recovery branch is outside four-heading teaching and does not ask the user to provide a path; verify both READMEs document three sibling installs and restart.

- [ ] **Step 3: Run RED once**

Run:

```powershell
python -m unittest tests.test_dependency_discovery_contract -v
```

Expected: FAIL because Git is explicitly false and the parent preflight is absent.

- [ ] **Step 4: Commit RED evidence**

```powershell
git add tests/test_dependency_discovery_contract.py tests/skill-evals/dependency-discovery-results.md
git commit -m "test: capture child discovery failure"
```

---

### Task 2: Implement explicit discovery and preflight

**Files:**
- Modify: `skills/step-by-step-git/agents/openai.yaml`
- Modify: `skills/step-by-step-vercel/agents/openai.yaml`
- Modify: `skills/step-by-step-coach/SKILL.md`
- Modify: `README.md`
- Modify: `README.zh-CN.md`

**Interfaces:**
- Consumes: Task 1 contracts.
- Produces: discoverable child metadata and a dependency state machine.

- [ ] **Step 1: Enable both child Skills explicitly**

Set `policy.allow_implicit_invocation: true` for both child metadata files without changing their interface text.

- [ ] **Step 2: Add the parent preflight**

Before domain routing, add the four observable branches from the design. State positively that dependency repair uses a short infrastructure notice outside teaching format; it never asks the user for a path and never counts installation as a Git/Vercel action.

- [ ] **Step 3: Align the READMEs**

Document implicit routing, complete sibling installation, restart requirements, and the catalog-stale recovery message in semantically aligned English and Chinese.

- [ ] **Step 4: Run focused GREEN and metadata validation**

```powershell
python -m unittest tests.test_dependency_discovery_contract -v
python -X utf8 "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" skills\step-by-step-coach
python -X utf8 "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" skills\step-by-step-git
python -X utf8 "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" skills\step-by-step-vercel
```

Expected: focused tests and all three validations pass.

- [ ] **Step 5: Commit implementation**

```powershell
git add skills README.md README.zh-CN.md tests
git commit -m "fix: make step-by-step children discoverable"
```

---

### Task 3: Run the four behavior checks

**Files:**
- Modify: `tests/skill-evals/dependency-discovery-results.md`

**Interfaces:**
- Consumes: final repository Skill tree.
- Produces: four raw, independent, non-repeated behavior records.

- [ ] **Step 1: Run Git route once**

In a fresh context, explicitly load the parent and child artifacts and ask to continue a confirmed Git scanning task. Verify the response routes into Git teaching without requesting a Skill path.

- [ ] **Step 2: Run Vercel route once**

In a separate fresh context, explicitly load the parent and child artifacts and ask to continue a confirmed Vercel environment-variable task. Verify Vercel routing and one-action teaching.

- [ ] **Step 3: Run one non-trigger check**

Ask an ordinary conceptual Git question without requesting one-step teaching. Verify it does not use the four-heading teaching contract.

- [ ] **Step 4: Run one missing-child boundary check**

Use a fresh context where the required child is declared unavailable. Verify the response is a short infrastructure blocker outside the teaching contract, does not ask the user to provide a path, and does not invent domain guidance.

- [ ] **Step 5: Record raw outputs and commit**

Record every raw response and judgment once. Do not run additional samples for statistics.

```powershell
git add tests/skill-evals/dependency-discovery-results.md
git commit -m "test: verify child dependency routing"
```

---

### Task 4: Install and back up the complete Skill family

**Files:**
- Update: `<CODEX_HOME>/skills/step-by-step-coach/`
- Update: `<CODEX_HOME>/skills/step-by-step-git/`
- Update: `<CODEX_HOME>/skills/step-by-step-vercel/`
- Update: `<OBSIDIAN_VAULT>/AI赋能知识库/99_原始资料归档/Codex个人Skills备份/`
- Update: the next available capability card
- Update: the latest `Codex 个人 Skill 迁移说明`
- Update: `<OBSIDIAN_VAULT>/AI赋能知识库/更新日志.md`

**Interfaces:**
- Consumes: reviewed repository copies.
- Produces: synchronized installation, backup, capability card, migration instructions, and one log record.

- [ ] **Step 1: Read latest trees and knowledge files**

Inventory and hash all source, installed, and backup files. Read the latest capability-card directory, migration instructions, and update log. Stop on any source conflict.

- [ ] **Step 2: Install all three complete sibling trees**

Refresh only differing files; preserve all subdirectories. Request filesystem approval if required. Validate each installed Skill with `quick_validate.py`.

- [ ] **Step 3: Write Obsidian mirrors and documentation**

Use `obsidian-knowledge-write`. Update all three complete mirrors, the next capability card, migration instructions, and one deduplicated update-log record at `N+1`.

- [ ] **Step 4: Perform knowledge-only recovery**

Copy all three Skills from the knowledge backup to a fresh temporary directory, validate each, compare every relative path and SHA-256 with source/install/backup, then delete only that verified temporary recovery directory.

---

### Task 5: Final gate and restart handoff

**Files:**
- Verify: repository, installation, knowledge backup, recovery evidence, Git status.

**Interfaces:**
- Consumes: all task outputs.
- Produces: a clean branch and a truthful restart boundary.

- [ ] **Step 1: Run the complete static suite once**

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
git diff --check
git status --short
```

- [ ] **Step 2: Scan portability and secrets**

Inspect tracked files for credentials, personal absolute paths, broken local references, placeholder markers, and missing child directories.

- [ ] **Step 3: Report the restart boundary**

Report repository/install/backup/recovery hashes and behavior results. State that files are updated but the current Codex task cannot prove catalog refresh. Ask the user to restart Codex; after restart, verify the available Skill list contains both `step-by-step-git` and `step-by-step-vercel` before declaring runtime completion.

