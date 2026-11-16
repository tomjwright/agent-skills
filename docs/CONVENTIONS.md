# Writing a skill

Every skill in this repo follows these rules. `scripts/check_skills.py` enforces the ones a script can check. Review enforces the rest.

The rules borrow from [Matt Pocock's skills](https://github.com/mattpocock/skills) (small skills that call each other) and [pstack](https://github.com/cursor/plugins/tree/main/pstack) (a finding counts only when a run proves it).

## Shape

- A skill is a folder `skills/<name>/` holding `SKILL.md`. The folder name is the skill's `name`: lowercase words joined by hyphens, at most 64 characters.
- `SKILL.md` starts with a frontmatter block holding `name` and `description`. Add nothing else, except `disable-model-invocation: true` for user-invoked skills (see below). Agents that don't know a field ignore it, so the skill stays portable.
- The body opens with one or two sentences on what the skill does. Then numbered steps, then a fixed **Output** section that says exactly what the skill hands back.
- A **shortcut** is a user-invoked skill whose body only loads other skills, like `grill-me`. Its body is just the load sentence plus what to apply it to: the steps and **Output** are the loaded skill's.
- Keep `SKILL.md` under about 150 lines. Move long detail into `references/<topic>.md` and link to it from the step that needs it, so the agent reads it only then. Reference files link to nothing else.
- Each skill also has `agents/openai.yaml`, which sets how Codex shows and starts it.

## One job per skill

A skill does one thing. When two skills need the same instructions, the instructions live in one of them and the other refers to it.

Refer to another skill with the exact phrase "Load the `<name>` skill with your skill tool." Most agents start skills through a tool, and naming it gets the skill loaded more reliably than a bare mention. To load two skills, say so: "Load the `grilling` skill and then the `domain-modeling` skill with your skill tool." Never link into another skill's folder: a skill may be installed without its neighbours' files.

## Who can start a skill

- **Model-invoked** (the default). The agent may load it by itself when the task fits. The `description` says what it does and when to use it ("Use when..."), because the agent decides from the description alone.
- **User-invoked.** Only a person can start it, by typing `/<name>`. Use this for long workflows the agent should never start uninvited, such as an interview. Set `disable-model-invocation: true` in the frontmatter **and** `allow_implicit_invocation: false` under `policy:` in `agents/openai.yaml`. The `description` is one short line for a person.

A skill may only refer to model-invoked skills. A user-invoked skill is a doorway for a person and nothing calls it.

## Works in any agent

- Never name one agent's tools. Say "your skill tool", "read the file", "run the command", not a specific tool call.
- Never name a model.
- Sub-agents are optional. Write: "If your agent can start sub-agents, give each one a fresh context window. Otherwise do the steps yourself, one after another." A fresh context window matters: some agents fork the current conversation by default, and a fork keeps the context the sub-agent was meant to escape.
- Files the skill writes for the user (reports, notes) go in the system temp folder, not the repo, unless the user asks otherwise.

## Repo facts come from the repo

A skill never hard-codes a repo's commands, paths or rules. It reads them from the files described in [REPO-CONTRACT.md](REPO-CONTRACT.md). If they're missing, it works them out, labels them "inferred", and tells the user the line to add.

## Proof

Checker skills (`code-review`, `test-check`, `architecture-check`) must:

- **Prove every finding.** Give a command the reader can rerun and the output it printed, or a real `file:line`. Anything else is labelled "unproven".
- **Report, never act.** A checker doesn't edit, commit or push. It hands back findings and stops. The user decides what to fix.
- **Say what was checked and cleared**, not only what failed, so the reader knows how far the check went.
- **Allow an empty result.** "No findings" is a valid answer. Never pad a report.

## Writing

- Plain English, short sentences, imperative steps ("Read the diff.").
- No em dashes. Rewrite the sentence with a comma, colon or full stop.
- One term per idea. If the skill says "finding", don't switch to "issue" halfway through.
- Say what to do, not how it feels: "run the tests" rather than "make sure things work".

## Changing a skill

One skill per PR. A shortcut ships in the same PR as the skill it loads. In the PR:

1. Run `python3 scripts/check_skills.py` and `python3 -m unittest discover -s tests`.
2. Try the skill on a real repo and paste what it produced.
3. Add a line to `CHANGELOG.md` and bump `version` in the plugin manifests when you release.
