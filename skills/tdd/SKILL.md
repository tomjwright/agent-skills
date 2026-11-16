---
name: tdd
description: Build a feature or fix a bug test-first, one failing test and one small change at a time, proving each test fails for the right reason before the code that passes it. Use when the user asks for TDD, test-first work, a failing test or a regression test, or to build behaviour with a clear, cheap test path.
---

Work in vertical slices: one test, then the least code that passes it, then the next. Each test must fail first, for the reason you expect, or it proves nothing. What makes a test worth keeping is in [references/tests.md](references/tests.md).

This skill changes code and tests. It never commits or pushes.

## Steps

1. **Load the `prove-it` skill with your skill tool.** Its rules decide what counts as proof below.
2. **Read the repo's rules.** Read `## Checks` and `## Standards` in `AGENTS.md`, `GLOSSARY.md` if it exists, and any ADR in `docs/adr/` the area touches. Use the glossary's words in test names. Find the command that runs one test file.
3. **Run the checks.** Run every command in `## Checks` and record what each printed. If they fail, report the failures and stop: a new failure can't be told apart from an old one.
4. **Agree the seams.** A seam is the public interface the tests call: a function, endpoint, command or page. Propose each one with a line on what testing there catches and misses, and ask the user to confirm. Skip the question only if the user already named them. Write no test at a seam the user hasn't agreed.
5. **List the slices.** Write each behaviour as one line, taken from the spec or the user's words, never from what the code does now. For a bug, the first slice is the bug. Put the riskiest first. Show the list.
6. **For each slice, in order:**
   1. **Red.** Write one test at an agreed seam, then run it. It must fail, and the failure must be the behaviour missing (a wrong value, an error the spec rules out), not a typo, an import error or a missing fixture. Quote the failing line. If it fails for the wrong reason, fix the test and run it again. If it passes, the behaviour already exists or the test checks nothing: break the code it should cover and run it again. Keep it only if it fails then, and record "already passed" for the slice.
   2. **Green.** Write the least code that makes that test pass. Nothing for later slices. Run the test, then every check. Quote the passing lines.
   3. **Stop if a test you didn't write fails.** Either the slice changed behaviour someone relies on or the old test was coupled. Show both and ask which is right. Never weaken an existing assertion to get green.
7. **Don't refactor inside the loop.** Once every slice is green, offer to load the `simplify` skill with your skill tool for the code you wrote.
8. **Report** in the Output format below. Leave the changes uncommitted.

## Output

```text
## TDD: <feature or bug>
Seams: <seam> (agreed)
Checks before: <command>: <passed line> (one per command)

S1. <behaviour>
Red: <test name>: "<the failing line>"
Green: <file>: <what changed>. <test command>: "<passed line>"
S2. <behaviour>
Red: already passed, then failed with <the break>: "<the failing line>"
Green: no change needed

Checks after: <command>: <passed line> (one per command)
No test: <behaviour>: <why>, checked with <command>: "<output>" | none
```
