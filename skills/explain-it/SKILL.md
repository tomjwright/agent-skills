---
name: explain-it
description: Explain how a piece of code works by following one concrete input through the files, step by step, in plain words, with every step cited and checked.
disable-model-invocation: true
---

Explain code the way you'd show someone around it: pick one real input and follow it, file by file, until it comes out the other end. Say what happens to it at each step in plain words. A reader should finish able to answer "where does this come from?" and "what can change it?".

This skill only reads and runs code. It never edits the repo.

## Steps

1. **Load the `prove-it` skill with your skill tool.** Every step in the trace is a claim, and its rules apply.
2. **Pin the question.** Restate what the user wants explained in one line. If it could mean two things, say which you picked and why.
3. **Pick one concrete input.** A real message, request, row or command that a user would send, chosen to go down the interesting path. If the user named one, use it. If the path splits, pick the common branch and note the others at the end.
4. **Read the glossary.** If `GLOSSARY.md` exists, use its words. Otherwise use the names the code uses, and explain each the first time it appears.
5. **Follow the input.** Start where it enters (an endpoint, a CLI command, an event handler) and read each function it passes through, in the order it runs. For each step, write what the input looks like now and what this step decides or changes. Cite the `file:line` of the line that does it. Skip steps that only pass the value on unchanged, but say you skipped them.
6. **Check the trace by running it.** Where it's cheap, run the path with the same input and compare: an existing test that covers it, the CLI, a request to a running server, or a short script that calls the public functions with a temporary database or config. Never write to the user's real data. Mark each step checked (with the output) or read only.
7. **Name the surprises.** List anything a newcomer would trip on: a default that hides a decision, a branch that silently does nothing, a value set in one place and read far away.
8. **Report** in the Output format below. Keep it short: plain sentences, no jargon the glossary or code doesn't use, and no history of how the code got that way.

## Output

```text
## How <the question>
In one line: <the answer>
Input: <the concrete input>

1. <file:line> <function>: <what happens, in plain words>. Now: <what the input looks like>. (checked | read only)
2. ...

Checked with: <command>: "<the line that shows it>" | not run, because <why>
Other paths: <branch>: <one line on where it goes> | none
Surprises:
- <file:line>: <what would trip a newcomer>
```
