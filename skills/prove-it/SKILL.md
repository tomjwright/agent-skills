---
name: prove-it
description: Check a claim against the real code before stating it, by running it or citing the exact line, and label anything unchecked as unproven. Use before saying work is done or a bug is fixed, and whenever a checker reports a finding.
---

Prove a claim by checking the real thing, not a stand-in for it. A claim is anything you are about to tell the user is true: "the tests pass", "this is fixed", "nothing calls this function", "this test can't catch that bug".

## What counts as proof

Strongest first:

1. **A run.** A command the reader can rerun, and the output it printed. For a bug, a failing test or a repro script. For "it works", run the feature or the checks in the `## Checks` section of the repo's `AGENTS.md`.
2. **A citation.** An exact `file:line` with the line quoted. Use it only for what the code says, never for what it does when it runs.

These are not proof: "it compiles", a sub-agent's or tool's summary you haven't checked, file timestamps, old or cached output, what the code should do, and your memory of a file.

## Steps

1. **State the claim** in one sentence, and say what result would show it is false.
2. **Pick the strongest proof that fits.** A claim about behaviour needs a run. Script the check when you can, as a test or a short command, so the reader can rerun it. Keep scripts in the system temp folder unless the user wants them committed.
3. **Run it against the code as it is now**, in the working tree, and read the actual output.
4. **Compare the output with the claim.** If they disagree, the claim is wrong. If the check itself broke (a wrong path, a missing dependency), suspect the check before the code: fix the check and run it again.
5. **Label the claim** proven, disproven or unproven, and give the proof.

## Rules

- Reasoning never turns "unproven" into "proven". If you couldn't check it, say so.
- Before passing on a sub-agent's claim, rerun its command or open its citation.
- Proving changes nothing in the code being checked. Fixing is a separate step.
- Commands come from the repo's `AGENTS.md`. If they're missing, work them out from files like `package.json`, `pyproject.toml` or `Makefile`, label them "inferred", and tell the user the line to add.

## Output

One block per claim:

```text
Claim: <one sentence>
Status: proven | disproven | unproven
Proof: <command> printed <the lines that matter>
   or: <file:line> "<quoted line>"
```

For an unproven claim, replace `Proof:` with `Why unproven:` and `Would prove it:`.
