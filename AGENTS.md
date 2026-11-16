# AGENTS.md

Rules for anyone changing this repo, human or coding agent.

## The project

Tool-agnostic agent skills, one folder per skill under `skills/`. [docs/CONVENTIONS.md](docs/CONVENTIONS.md) says how a skill is written and is the main rulebook. [docs/REPO-CONTRACT.md](docs/REPO-CONTRACT.md) says what other repos provide for the skills.

## How we work

1. Work on a feature branch cut from an up-to-date `main`. Never commit or push to `main`.
2. One skill per PR, roughly 200-300 lines. A shortcut ships with the skill it loads.
3. Explain the PR in plain English: what changed and why, each file in a sentence or two, and an example of the skill being used on a real repo.
4. Every skill is linked from `README.md` under **User-invoked** or **Model-invoked**.
5. Delete the branch after the PR merges.

## Checks

```bash
python3 scripts/check_skills.py
python3 -m unittest discover -s tests
```
