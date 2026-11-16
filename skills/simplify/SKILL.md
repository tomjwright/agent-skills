---
name: simplify
description: Make code easier to read by cutting the layers to trace and the state to hold, such as one-caller wrappers, pass-through layers, callback detours and dead code, while proving behaviour stays the same. Use when code is hard to follow, when the user asks to simplify or clean up code, or before adding to a tangled area.
---

Make code take less effort to read: fewer layers between a question and its answer, and less state to keep in your head. Every change keeps behaviour the same, and the tests prove it. The candidates are in [references/candidates.md](references/candidates.md).

This skill changes code, but only what the user agrees to, and it never commits or pushes.

## Steps

1. **Load the `prove-it` skill with your skill tool.** Its rules decide what counts as proof below.
2. **Choose the scope.** Use the files, folder or diff the user names. If they named none, use the changes since the repo's default branch (`git diff --merge-base <default>`, plus `git status --short` for untracked files) and say so. If that's empty too, ask.
3. **Read the repo's rules.** Read `## Checks` and `## Standards` in `AGENTS.md`, and `GLOSSARY.md` if it exists. A standard overrides this skill: if the repo asks for a layer, keep it.
4. **Run the checks.** Run every command in `## Checks` and record what each printed. They must pass. If they fail, report the failures and stop: a change can't be proven safe against a red suite.
5. **Find candidates.** Read the scope as a new reader would, asking for each function "where does this come from?" and "what can change it?". Match what slows you down against [references/candidates.md](references/candidates.md). Count callers by searching the whole repo, and run the deletion test on every layer before you suggest cutting it.
6. **Check a test covers each one.** Put an error the code doesn't catch at the start of the code you'd change (`raise SystemExit("simplify reached")` or your language's equivalent) and run the tests. If they still pass, no test runs it, so nothing would catch a mistake. Mark the candidate "needs a test first". Undo the probe.
7. **Ask before changing anything.** List the candidates in the Proposed format below, then stop and ask which to apply. Apply only those. Skip this step only if the user already asked you to apply every candidate you find.
8. **Apply one at a time.** Make one change, run every check, and compare the output with step 4. The same tests must pass, with none skipped that weren't before. If anything differs, undo the change and record why. Then move to the next. Don't change a test's assertions to make it pass: a test that needs a new assertion means behaviour changed.
9. **Report** in the Output format below. Leave the changes uncommitted.

## Proposed

```text
## Simplify: <scope>
Checks: <command>: <passed line> (one per command)

C1. <candidate kind>: <one-line description>
Where: <file:line> "<quoted line>" (one line per place)
Evidence: <n callers found by search> | <deletion test result> | <other proof>
Covered: yes, <test that failed with the probe> | needs a test first
Change: <the change, as a short pseudo-diff or one sentence>
```

## Output

```text
## Simplify: <scope>
Applied
- C1. <file>: <what changed>. Checks: <command>: <passed line>, same as before.
Undone
- C2. <why: the check that changed and what it printed>
Not applied
- C3. <needs a test first | the user declined>
Lines: <before> -> <after> in the files touched.
```

Write "No candidates." when there are none. Never pad.
