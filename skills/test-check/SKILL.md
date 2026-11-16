---
name: test-check
description: Judge whether a repo's tests would catch real bugs, by breaking the code in a scratch copy and seeing which tests notice. Finds weak tests, tests pinned to the implementation, and behaviour with no test. Reports only, never edits the repo. Use when the user asks if the tests are good enough, after tests are written for a change, or before trusting a passing suite.
---

Judge the tests by what they catch, not by how they look. Two probes decide it:

- **Break the behaviour.** Change the code so a caller would see a wrong result. A test that still passes is **weak**.
- **Change the internals.** Restructure the code so no caller sees a difference. A test that now fails is **coupled** to the implementation.

Behaviour that no test runs at all is **untested**.

This is a checker: it reports and stops. Every probe runs in a scratch copy, so the user's working tree, branch and commits are never touched.

## Steps

1. **Load the `prove-it` skill with your skill tool.** Its rules decide what counts as proof for every finding below.
2. **Pick the scope.** Use the files, module or feature the user named. If they named none, use the changes since the repo's default branch (`git diff <default>...HEAD --stat`, plus `git status --short` for uncommitted work) and say so. Stop and ask if that is empty too.
3. **Find the test command.** Use the test command in `## Checks` of the repo's `AGENTS.md`. If there is none, infer it as `prove-it` says and label it "inferred". Note the faster form that runs one file or one test, if the runner has one.
4. **Make the scratch copy.** Run `git worktree add --detach <temp>/test-check-<short-sha> HEAD` in the system temp folder. If the user's tree has uncommitted work in scope, carry it over: `git diff HEAD | git -C <scratch> apply`, and copy each untracked file (`??` in `git status --short`). Then run `git -C <scratch> add -A`, so restoring a file after a probe brings back that work, not `HEAD`. Set up dependencies inside the copy the way `AGENTS.md` or the README says. Every edit from here on happens only in the scratch copy.
5. **Run the baseline** in the scratch copy. It must pass. If it fails there but passes in the user's tree, the copy is wrong (a missing dependency, a path outside the copy): fix the copy and run it again. If it fails in both, report the failing tests and stop, because a probe against a red suite proves nothing.
6. **List the behaviours.** For each public function, endpoint, command or page in scope, write what its callers can observe: return values, errors they branch on, state they read back, effects outside the code (a row written, a request sent). Take the expected behaviour from the spec, docs and names, never from what the code happens to do. Put the risky ones first: conditions and boundaries, error paths, anything touching money, security or data loss.
7. **Break each behaviour** with one small edit from [references/probes.md](references/probes.md). Run the tests that cover it, then the whole suite. Record which tests failed and the line that shows it, or that every test passed. Restore the file (`git -C <scratch> checkout -- <file>`) before the next probe. When every test passed, search the tests for the name of the code you broke: no match means **untested**, a match means **weak**.
8. **Change the internals** for each test that looks pinned to them: it mocks code the repo owns, calls a private helper, asserts call order or counts on internal code, or matches exact wording no caller reads. Make one refactor from [references/probes.md](references/probes.md) that keeps every observable result the same, and show it does by running another test or script that checks those results. Run the test. If it fails, it is **coupled**. Restore the file.
9. **Read the tests in scope** for the patterns in [references/probes.md](references/probes.md) that no probe covers (an expected value computed by the code under test, an assertion on data the test built itself, a skipped test). Report each one as unproven unless a probe confirmed it.
10. **Clean up.** Run `git worktree remove --force <scratch>` and check that `git status --short` in the user's tree matches what it was in step 2.
11. **Report** in the format below.

Run at most about 15 probes per check, risky behaviours first, and list the rest under **Not probed**. If your agent can start sub-agents, you may give each a fresh context window, its own scratch copy and a share of the behaviours. Rerun each probe a sub-agent reports before passing it on. Otherwise do the probes yourself, one after another.

## Output

```text
## Test check: <scope>
Tests: <command> (inferred, if it was). Baseline: passed, "<the line that shows it>". Scratch copy: <path>, removed.

## Weak
W1. <what can break without any test noticing>
Probe: <file:line> "<original>" -> "<changed>"
Proof: <command> printed "<the line showing every test passed>"
Tests that run it: <test file:line, ...>
Status: proven

## Coupled
C1. <test name> fails when <internal detail> changes
Refactor: <file:line> <what changed>. Behaviour kept: <command> printed "<line>"
Proof: <command> printed "<the failure line>"
Status: proven | unproven

## Untested
U1. <behaviour> has no test
Where: <file:line>
Proof: <probe and passing run> and <search for the name in the tests> found nothing
Status: proven

## Patterns
T1. <test file:line> <pattern>: <one line>
Status: proven | unproven

## Cleared
- <file:line> <probe>: caught by <test>, "<the failure line>"

Not probed: <behaviours left out, and why>

Summary: Weak <n>, Coupled <n>, Untested <n>, Patterns <n>. Probes: <n> run, <n> caught. Worst: <one line, or "none">.
```

Write "No findings." under a heading that has none. Never pad.
