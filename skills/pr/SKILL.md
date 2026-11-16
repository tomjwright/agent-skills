---
name: pr
description: Write a pull request description that is small, plain English and proven, with a file-by-file walkthrough, a concrete example and the check output that shows it was tested. Use when opening a PR, writing or updating a PR description, or checking a branch is ready for review.
---

Write the description a reviewer who hasn't seen the diff can read in two minutes: what changed and why, each file in a sentence or two, one concrete example, and proof it was tested. Use the glossary's words, skip preambles, and keep sentences short.

This skill writes the description. It doesn't change code, and it opens or updates the PR only if the user asked for that.

## Steps

1. **Load the `prove-it` skill with your skill tool.** Its rules decide what counts as proof in **Tested**.
2. **Find the diff.** Use the base the user names, or the repo's default branch, and say which. Run `git log <base>..HEAD --oneline` and `git diff --merge-base <base> --stat`. Run `git status --short` too: if there is uncommitted work, ask whether it belongs in this PR before writing anything.
3. **Check it is one PR.** Read `## Standards` in `AGENTS.md` for the repo's rules on PR size and branches. Stop and tell the user, with the evidence, if:
   - the hand-written lines (not lock files, generated code or snapshots) go over the repo's limit, or about 300 if it sets none. Propose a split, one idea per PR, in the order to merge them.
   - the diff holds more than one idea. Name each one.
   - the branch contains commits from another branch that hasn't merged yet (`git branch -r --contains <sha>` for the oldest commit). Each PR should start from an up-to-date base.
4. **Run the checks.** Run every command in `## Checks` of `AGENTS.md`, and run what changed (the command, the endpoint, the page) the way a user would. Record each command and the line that shows its result. Whatever you couldn't run goes under **Not tested**, with the reason. Never write a command you didn't run.
5. **Use the repo's template.** If the repo has a PR template (`.github/pull_request_template.md`, `.github/PULL_REQUEST_TEMPLATE/`, `docs/pull_request_template.md`), fill its sections and fit the parts below into them. Otherwise use the Output below.
6. **Write it.**
   - **Summary:** what changed and why, in two or three sentences. Lead with the point. Add one view from [references/visuals.md](references/visuals.md) if it makes the change clearer than prose.
   - **Files:** each file the diff changes, with a sentence or two on what it does now and why. Group trivial ones (lock files, a README line) on one line.
   - **Example:** one concrete case: an input and what happens before and after, a request and its response, or the test that failed before and passes now.
   - **Risk:** say whether it is easy to undo (a revert puts everything back) or hard to undo (a data migration, a deleted file users rely on, a public interface or message format changed), and what else could break.
7. **Check the description against the diff.** Every file in `--stat` appears under **Files**, and every claim in **Summary** matches a line in the diff. Fix anything that doesn't.
8. **Report** the description in the Output format, ready to paste.

## Output

```markdown
## Summary
<what changed and why>

<optional: one view from references/visuals.md>

## Files
- `<file>`: <what it does now, and why>

## Example
<input, then before and after>

## Tested
- `<command>`: <the line that shows the result>

Not tested: <what, and why> | none

## Risk
<easy to undo | hard to undo, because ...>. Could affect: <what> | nothing outside this change.
```
