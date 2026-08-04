# Step-by-Step Coach

[English](README.md) | [简体中文](README.zh-CN.md)

> Calm, one-action-at-a-time Codex coaching for Git/GitHub and Vercel workflows.

Most tutorials give a whole checklist. This project instead gives one action, waits for the real result, then chooses the next action from that evidence. It is for Git beginners, occasional users, non-developers, and people starting with Vibe Coding who want to understand what happens before they change anything.

## Skills

This repository contains three sibling Codex Skills. Keep every directory and subdirectory intact when installing or copying them.

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

- `step-by-step-coach` owns context confirmation, the fixed one-action reply shape, waiting, and risk gates.
- `step-by-step-git` handles Git and GitHub state, errors, and safe repository operations.
- `step-by-step-vercel` handles Vercel deployment and configuration decisions after the parent has confirmed context.

Both child Skills explicitly allow implicit routing from the parent after you confirm the domain. Ordinary Git or Vercel questions do not enter coaching unless you ask for one-action-at-a-time guidance.

## Install

Clone this repository, then copy all three complete Skill directories into your personal Codex Skills directory.

### Windows PowerShell

```powershell
Copy-Item -Recurse -LiteralPath ".\skills\step-by-step-coach" -Destination "$env:USERPROFILE\.codex\skills"
Copy-Item -Recurse -LiteralPath ".\skills\step-by-step-git" -Destination "$env:USERPROFILE\.codex\skills"
Copy-Item -Recurse -LiteralPath ".\skills\step-by-step-vercel" -Destination "$env:USERPROFILE\.codex\skills"
```

### macOS or Linux

```bash
cp -R ./skills/step-by-step-coach ~/.codex/skills/
cp -R ./skills/step-by-step-git ~/.codex/skills/
cp -R ./skills/step-by-step-vercel ~/.codex/skills/
```

Restart Codex after installation.

Install all three complete Skill directories as siblings. Updating only the parent leaves its Git and Vercel dependencies incomplete. Codex builds the available-Skill catalog when a task starts, so restart Codex after every installation or update. If a child directory exists under your personal Skills directory but the current task says it is unavailable, do not provide a path: restart Codex and open a fresh task so the catalog can refresh.

## Use

Start a fresh Codex task and invoke:

```text
$step-by-step-coach
```

The parent Skill can read a user-selected source task when `list_threads` and `read_thread` are available, then asks you to confirm the context before it routes to Git/GitHub or Vercel. If the old task is unavailable, provide a summary, handoff file, or project note instead.

Every ordinary teaching response uses the equivalent Chinese fields for current purpose, one action, expected result, and requested evidence. It gives no next step until you reply with the result.

## Vercel Coverage

Vercel coaching supports the deployment lifecycle around your existing code: importing repositories from GitHub, GitLab, or Bitbucket; build settings; Preview, Production, and eligible Custom Environments; promoting or rolling back deployments; environment variables and secrets; Functions; domains, DNS, and SSL; logs; troubleshooting; deployment protection; and team or project access.

It is Dashboard-first. It uses one Vercel Dashboard action by default, and only uses one CLI command when the Dashboard cannot complete the task, you explicitly prefer CLI, or a reproducible local diagnostic is necessary.

It is Hobby-first. Before suggesting a plan-dependent capability such as retention, rollback, access, or team controls, it checks whether the project is on Hobby and what the Dashboard actually offers, then gives a free alternative when available. It never assumes plan capability.

## Safety Model

The coach pauses for an explicit confirmation before force push, history rewrite, destructive reset, branch deletion, PR merge, Production release or promotion, rollback, deleting or overwriting an environment variable, changing an environment-variable scope, redeployment that may affect users, DNS changes, deployment protection, or team/project access-control changes. Each confirmation authorizes exactly one imminent high-risk action; other requested risks remain pending until their own confirmation. The confirmation says what will change, who or what is affected, possible irreversible consequences, and a safer alternative; it does not include an executable production action.

For environment configuration, the coach never asks for, stores, or echoes real secret values, tokens, cookies, complete environment-variable values, or unredacted screenshots. It first identifies the one target environment or branch, distinguishes public client prefixes such as `NEXT_PUBLIC_` and `VITE_` from secrets, and reminds you that an environment-variable change needs a new deployment to take effect.

For domain and DNS work, it obtains the live record target from the current Vercel Dashboard instead of documenting a fixed target. It asks about existing mail dependencies and does not delete, overwrite, or clear MX records. DNS, nameserver, and certificate-delegation changes always receive their own confirmation round.

## Boundaries

The Skills teach one safe operational action at a time; they do not write your business code, execute the taught Git or Vercel actions for you, retain credentials, or guarantee that a third-party provider will accept a configuration. Docker and package publishing are not currently covered. When a domain has no configured child Skill, the parent says so instead of pretending to provide a full guided workflow.

## Examples

- [First local project upload](examples/first-upload.md)
- [Force-push safety gate](examples/force-push-safety.md)

## License

[MIT](LICENSE)
