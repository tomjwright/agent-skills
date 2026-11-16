---
name: domain-modeling
description: Settle what the project's terms mean and record hard-to-reverse decisions, by challenging vague or conflicting words against the glossary and the code, then writing GLOSSARY.md and ADRs. Use when discussing what a term means, writing or editing GLOSSARY.md, or recording an ADR.
---

Make the project's language precise while you design, and write it down the moment it's settled. Reading `GLOSSARY.md` to pick the right word is a habit any skill can have. This skill is for changing the glossary and the decisions, not only reading them.

It writes only `GLOSSARY.md`, `GLOSSARY-MAP.md` and files in `docs/adr/`. It never edits code, and never commits.

## Steps

1. **Find the glossary.** If `GLOSSARY-MAP.md` exists at the root, the repo has several contexts: read it, then the `GLOSSARY.md` of the context the topic belongs to, and ask the user if that's unclear. Otherwise read the root `GLOSSARY.md` if there is one. Read every ADR in `docs/adr/` that the topic touches. If none of these exist, create them only when there is something to write.
2. **Challenge a conflicting term at once.** When the user uses a word in a way the glossary doesn't, quote the entry and ask which meaning wins: "`GLOSSARY.md:12` defines a fact as X, but you mean Y. Which is it?"
3. **Sharpen a vague term.** When one word could mean two things, name both and recommend one word for each: "By memory, do you mean the saved facts, or everything the `Memory` class stores?"
4. **Test it with a concrete case.** For each relationship between terms, invent a specific case at the edge and ask what happens: "The user says forget that I live in Singapore. The fact goes, but the message is still in the last 20 sent to the model. Is it forgotten?"
5. **Check the code agrees.** Load the `prove-it` skill with your skill tool. Before saying how the code works, read it and cite the `file:line`. When the code contradicts what the user said, show both and ask which is right. Don't change the code to match.
6. **Write each term as soon as the user agrees it.** Add or change the entry in `GLOSSARY.md` in the format in [references/glossary.md](references/glossary.md). Don't save them up for the end. Keep implementation out of it: no class names, tables or file paths. It's a glossary, not a spec.
7. **Offer an ADR only when a decision is hard to reverse, surprising without context, and the result of a real trade-off.** All three, or skip it. Show the text and write it to `docs/adr/` only after the user says yes, in the format in [references/adr.md](references/adr.md).

## Output

At the end of the session:

```text
Glossary: <file>
- added <term> | changed <term>: <old meaning> -> <new meaning>
ADRs: <file>: <title> | none
Code conflicts:
- <file:line> "<quoted line>" vs the user's "<quote>": settled as <which> | open
Open terms: <terms still unsettled> | none
```

Say "Glossary: no changes" when nothing was written. The files are left uncommitted for the user to review.
