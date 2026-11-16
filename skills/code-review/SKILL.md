---
name: code-review
description: Review the changes since a fixed point (a branch, commit or tag) on three separate axes, Standards, Spec and Bugs, and prove every finding. Reports only, never edits. Use when the user wants a branch, PR or work in progress reviewed, asks to "review since X", or before opening a PR.
---

Review the diff between `HEAD` and a fixed point on three axes, each kept apart so one can't hide another:

- **Standards:** does the code follow this repo's documented standards?
- **Spec:** does it do what the issue or spec asked for, and nothing more?
- **Bugs:** does it do the wrong thing when it runs?

This is a checker: it reports and stops. It never edits, commits or pushes.

## Steps

1. **Load the `prove-it` skill with your skill tool.** Its rules decide what counts as proof for every finding below.
2. **Pin the fixed point.** Use what the user named (`main`, a SHA, `HEAD~3`). If they named nothing, use the repo's default branch and say so. Run `git rev-parse <fixed-point>`, then `git diff <fixed-point>...HEAD --stat` and `git log <fixed-point>..HEAD --oneline`. Run `git status --short` too: uncommitted changes are not in the three-dot diff. If there are any, ask whether to include them, and if so review `git diff <fixed-point>` instead, plus each untracked file (`??` in the status) read in full, since no diff shows it. Stop and tell the user if the ref doesn't resolve or there is nothing to review, committed or not.
3. **Run the checks.** Run every command in `## Checks` of the repo's `AGENTS.md` and keep the lines that show the result. If there is no `## Checks`, infer the commands as `prove-it` says and label them "inferred". A failing check is a Bugs finding.
4. **Find the standards.** Read `## Standards` in `AGENTS.md` and every file it links to, plus `CONTRIBUTING.md` or `CODING_STANDARDS.md` if they exist. Add the smell list in [references/smells.md](references/smells.md). A documented standard always beats a smell.
5. **Find the spec.** In order: a spec or issue the user named, issue references in the commit messages (`#12`, `Closes #12`), the PR description, the place `## Specs` in `AGENTS.md` points to. If there is none, ask the user once. If there still isn't one, skip the Spec axis and say "no spec found".
6. **Review each axis separately.** If your agent can start sub-agents, start one per axis, each with a fresh context window, and pass it the diff command, the commit list, the files from step 4 or 5, and its brief below. Otherwise do the axes yourself, one after another, finishing one before starting the next.
7. **Check every finding before reporting it.** Open each `file:line` and rerun each command a sub-agent reported. Drop a finding you can't reproduce, or mark it unproven. Never fix anything.
8. **Report** in the format below. Don't merge or rerank findings across axes.

## Axis briefs

**Standards.** For each place the diff breaks a documented standard, cite the changed line and the rule (`file:line` of the rule, quoted). Mark it **hard**. For each smell from the list, name it and cite the changed line. A smell is always **judgement**, never hard. Skip anything a linter in `## Checks` already enforces. Only review lines the diff changed.

**Spec.** Quote the spec line for each finding. Report (a) requirements that are missing or only partly done, (b) behaviour nobody asked for, (c) requirements that look done but are done wrong. Cite the changed line for (b) and (c).

**Bugs.** Look for inputs and states the changed code gets wrong: edge cases, error paths, wrong conditions, changed behaviour for existing callers. Prove each one with a run: a failing test or a short script in the system temp folder that calls the real code. A bug you can only argue for is reported as unproven, with the run that would prove it.

## Output

```text
## Code review: <fixed-point>..HEAD
<n> commits, <n> files. Standards from: <files>. Spec from: <source or "no spec found">.

Checks
- <command>: passed | failed, "<the line that shows it>"  (inferred, if it was)

## Standards
S1. [hard | judgement] <one-line finding>
Where: <file:line> "<quoted changed line>"
Rule: <file:line> "<quoted rule>" | smell: <name>
Status: proven | unproven

## Spec
P1. [missing | not asked for | wrong] <one-line finding>
Spec: "<quoted spec line>"
Where: <file:line> "<quoted changed line>"
Status: proven | unproven

## Bugs
B1. <one-line finding>
Where: <file:line>
Proof: <command> printed <the lines that matter>
Status: proven | unproven (Would prove it: <run>)

## Cleared
- <what each axis checked and found fine>

Summary: Standards <n> (<n> hard), Spec <n>, Bugs <n> (<n> proven). Worst per axis: <one line each, or "none">.
```

Write "No findings." under an axis that has none. Never pad.
