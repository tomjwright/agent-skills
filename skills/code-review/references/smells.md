# Smell list

Code smells from Martin Fowler's *Refactoring* (chapter 3). They apply even when a repo documents no standards. Each is a judgement call, never a hard violation, and a documented repo standard overrides it. Match each against the changed lines only.

| Smell | What it looks like | Usual fix |
|---|---|---|
| Mysterious name | A name that doesn't say what the thing does or holds | Rename it. If no honest name comes, the design is unclear |
| Duplicated code | The same logic in more than one place in the change | Pull it into one function and call it from both |
| Feature envy | A function that uses another object's data more than its own | Move it next to the data it uses |
| Data clump | The same few values always passed around together | Group them into one type |
| Primitive obsession | A string or number standing in for a domain idea | Give the idea its own small type |
| Repeated switch | The same `if`/`switch` on the same value in several places | One lookup table or one dispatch both sites share |
| Shotgun surgery | One logical change needs edits scattered across many files | Gather what changes together into one module |
| Divergent change | One file edited for several unrelated reasons | Split it so each part changes for one reason |
| Speculative generality | Parameters, hooks or layers for needs the spec doesn't have | Delete it until a real need appears |
| Message chain | `a.b().c().d()` that ties the caller to the whole path | One function on the first object that does the walk |
| Middle man | A function or class that only passes calls on | Call the real target directly |
| Refused bequest | A subclass that ignores or overrides most of what it inherits | Use composition instead of inheritance |
