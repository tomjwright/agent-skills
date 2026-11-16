---
name: architecture-check
description: Check the code that changes most for shallow modules, leaked decisions and hand-synced lists, prove each finding, and suggest how to deepen it.
disable-model-invocation: true
---

Find where the design makes change hard, starting from the code that changes most, and suggest how to make each module deeper: more behaviour behind a smaller interface, with each decision in one place. The terms and red flags are in [references/design.md](references/design.md).

This is a checker: it reports and stops. It suggests a design for each finding but never applies one, and never edits, commits or pushes.

## Steps

1. **Load the `prove-it` skill with your skill tool.** Its rules decide what counts as proof for every finding below.
2. **Choose the scope.** If the user named an area or a pain point, use it. Otherwise find the hot spots and change coupling with the commands in [references/history.md](references/history.md), and scope to the top files and the pairs that keep changing together. Code that rarely changes costs little however it looks, so leave it out and list it under "Not checked".
3. **Read what's already decided.** Read `GLOSSARY.md`, every ADR in `docs/adr/`, and `## Standards` in `AGENTS.md`. Name modules with the glossary's terms. A finding that goes against an ADR is only reported when the evidence is strong enough to reopen it, and it says so.
4. **Look for red flags in the scope.** If your agent can start sub-agents, start one with a fresh context window and pass it the scope, the files from step 3 and [references/design.md](references/design.md). Otherwise do it yourself. Walk each hot spot as a new reader would and note where one idea means opening many files, where a change in one place needs a matching change in another, and where tests reach past an interface. Match each against the red flags.
5. **Gather evidence for each finding.** Cite every `file:line` involved and quote it. Add the change coupling count when the files keep changing together. Run the deletion test for anything that looks shallow or pass-through, and count its callers. Where it's cheap, prove that nothing catches drift: in a scratch copy (`git worktree add --detach <temp>/architecture-check-<short-sha> HEAD`), change one side only, such as one copy of a list or a repeated default, and run the commands in `## Checks`. If they all still pass, the drift is proven. Remove the copy with `git worktree remove --force <scratch>`.
6. **Check every finding before reporting it.** Open each `file:line` and rerun each command. Drop a finding you can't reproduce, or mark it unproven.
7. **Suggest a fix for each finding.** In plain English: which modules merge, which decision gets one owner, which list is derived from which, or what gets deleted. Say how the result would be tested through its interface, using the dependency kinds in [references/design.md](references/design.md). Don't design the new interface yet: that is for the conversation in step 9.
8. **Rate each finding.** **Strong:** proven, and the hot spot keeps paying the cost. **Worth exploring:** proven, but the cost is small or rare. **Speculative:** a judgement the evidence only partly supports.
9. **Report** in the format below, then ask which finding the user wants to explore. If they pick one, load the `grilling` skill with your skill tool and work out the new design with them. If they reject a finding for a lasting reason, offer the text of an ADR so later checks don't suggest it again. Don't write it into the repo unless they ask.

## Output

```text
## Architecture check: <scope>
Scope from: <the user | hot spots since <date>, <n> commits>. Glossary: <file | none>. ADRs: <n read | none>.

Hot spots
- <file>: <n> commits
- <file> + <file>: changed together in <n> of <n> commits

## Findings
A1. [Strong | Worth exploring | Speculative] <red flag>: <one-line finding>
Where: <file:line> "<quoted line>" (one line per place)
Evidence: <command> printed "<lines>" | <deletion test: n callers, what moves where>
ADR: none | goes against <file>, reopen because <reason>
Status: proven | unproven
Suggest: <the change>. Tested by: <what, through which interface>.

## Cleared
- <what was looked at and found fine>

## Not checked
- <areas left out, and why>

Summary: Findings <n> (<n> strong). Start with: A<n>, because <reason>.
Which of these would you like to explore?
```

Write "No findings." when there are none. Never pad.
