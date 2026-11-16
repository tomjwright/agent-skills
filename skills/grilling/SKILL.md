---
name: grilling
description: Interview the user in rounds of numbered questions, each with a recommended answer, until every decision in a plan or design is settled. Use when the user wants to stress-test a plan, a design or an idea before building it, or says "grill me".
---

Interview the user until you both understand the plan the same way. Don't build anything during the interview.

## The design tree

Treat the plan as a tree of decisions. Each decision opens the decisions that depend on it. The **frontier** is every open decision whose prerequisites are already settled: the questions you can ask now without guessing at answers you haven't heard yet.

## Steps

1. **Gather the facts first.** Read the code, docs and `AGENTS.md` that the plan touches. Facts are your job, never the user's: don't ask anything you could look up. If your agent can start sub-agents, send one with a fresh context window to look up each fact you need, and carry on with questions that don't depend on it. Otherwise look it up yourself before the round that needs it.
2. **Ask the whole frontier in one round.** Number the questions. Give each a short title, the question, the options where there are some, and your recommended answer with a one-line reason. Word each question so that "yes" accepts your recommendation. Then stop and wait.
3. **Hold back dependent questions.** A question whose answer depends on another question in the same round belongs in a later round.
4. **Recompute after each answer.** Settled decisions open new ones. Ask the next round. If an answer contradicts an earlier one or a fact you found, say so plainly and ask which wins.
5. **Finish when the frontier is empty.** Every branch visited, nothing silently assumed. Then give the summary below and ask the user to confirm it. Don't act on the plan until they do.

## Round format

```
Q1. <title>
<question, with options if there are any>
Recommended: <answer>, because <one-line reason>.

Q2. <title>
...
```

## Output

When the frontier is empty:

- **Decisions:** each settled decision, one line each, in the order they depend on each other.
- **Facts used:** what you looked up, with `file:line` or the command you ran.
- **Assumptions:** anything still assumed rather than decided. Say "none" if there are none.
- **Out of scope:** what the user chose not to do.
