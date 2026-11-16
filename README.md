# agent-skills

Skills I use with coding agents in every repo: interviews to sharpen a plan, and checkers for code, architecture and tests that prove every finding by running code.

A skill is a folder with a `SKILL.md`: plain Markdown instructions an agent loads when it needs them. They follow the open Agent Skills format, so the same files work in Devin, Claude Code, Cursor, Codex and other agents.

## Install

Install once per agent. Every repo you open then has the skills.

| Agent | How |
|---|---|
| Devin | Install `https://github.com/tomjwright/agent-skills` as a personal plugin |
| Claude Code | `claude plugin marketplace add tomjwright/agent-skills` then `claude plugin install agent-skills@tomjwright` |
| Cursor, Codex and others | `npx skills@latest add tomjwright/agent-skills -g` |
| From a clone | `scripts/install.sh` links every skill into `~/.claude/skills`, `~/.agents/skills` and `~/.cursor/skills`, so `git pull` updates them |

## Set up a repo

Skills read each repo's commands and rules from its `AGENTS.md`. See [docs/REPO-CONTRACT.md](docs/REPO-CONTRACT.md) for the two sections to add.

## Skills

### User-invoked

You start these by typing `/<name>`.

- [architecture-check](skills/architecture-check/SKILL.md): find shallow modules, leaked decisions and hand-synced lists in the code that changes most, and talk through a fix.
- [grill-me](skills/grill-me/SKILL.md): an interview that sharpens a plan or design before you build it.

### Model-invoked

The agent loads these by itself when the task fits, and you can also start them.

- [code-review](skills/code-review/SKILL.md): review a diff on three separate axes, standards, spec and bugs, and prove every finding.
- [grilling](skills/grilling/SKILL.md): rounds of numbered questions, each with a recommended answer, until every decision in a plan is settled.
- [prove-it](skills/prove-it/SKILL.md): check a claim against the real code before stating it, and label anything unchecked as unproven.
- [pr](skills/pr/SKILL.md): write a small, plain-English PR description with a file-by-file walkthrough, an example and proof it was tested.
- [test-check](skills/test-check/SKILL.md): break the code in a scratch copy to find weak tests, tests pinned to the implementation, and untested behaviour.

## Writing a skill

See [docs/CONVENTIONS.md](docs/CONVENTIONS.md).

## Credits

Adapted from [mattpocock/skills](https://github.com/mattpocock/skills) by Matt Pocock and [pstack](https://github.com/cursor/plugins/tree/main/pstack) by Lauren Tan, both MIT licensed.
