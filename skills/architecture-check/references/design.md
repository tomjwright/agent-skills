# Design vocabulary and red flags

The vocabulary is from Matt Pocock's `codebase-design` skill, and the red flags from pstack's design red flags. Use these terms exactly in every finding. Don't switch to "component", "service" or "boundary".

## Terms

- **Module:** anything with an interface and an implementation: a function, a class, a file, a package.
- **Interface:** everything a caller must know to use the module correctly: the signature, plus ordering rules, error modes, required config and invariants.
- **Depth:** how much behaviour a caller gets per unit of interface it must learn. **Deep** is a lot of behaviour behind a small interface. **Shallow** is an interface nearly as complex as what it hides.
- **Seam:** the place where a module's interface lives, where behaviour can change without editing the callers.
- **Leverage:** what callers gain from depth: one implementation serves many call sites and tests.
- **Locality:** what maintainers gain from depth: a change, a bug or a rule lives in one place.

## The deletion test

Imagine deleting the module and inlining it into its callers. If the complexity vanishes, the module was a pass-through. If the same complexity reappears in each caller, the module earns its place. Count the callers and say which.

## Red flags

| Red flag | What it looks like | Evidence to cite |
|---|---|---|
| Shallow module | Callers coordinate several calls to do one thing, or options expose internal stages | The interface and two or more callers doing the coordinating |
| Pass-through | A function or layer that forwards the same arguments to another with the same shape | The forwarding lines and the deletion test result |
| Information leakage | The same decision (a format, a default, a key, a protocol detail) written in more than one module | Every `file:line` that repeats it |
| Hand-synced list | Two or more places list the same items, and adding one means editing all of them | Each list, and the change coupling count for their files |
| Split ownership | More than one module writes the same state or keeps its own copy | Each writer |
| Two ways to do one task | More than one way to do the same job, each with callers | Both ways and a caller of each |
| Temporal decomposition | Modules split by when they run (load, validate, save) that each repeat one representation | The repeated representation in each |
| Importable internals | Callers outside a module import its private helpers | Each import from outside |
| Tested past the interface | Tests mock or call a module's internals because its interface can't be tested | The test lines |

## What a fix looks like

Suggest deepening, not layering: merge shallow modules behind one interface, give a decision one owner, derive the second list from the first, or delete the pass-through. Say how the module would then be tested, through its interface, by the kind of dependency it has:

- **In-process** (pure logic, memory): test the merged module directly.
- **Local stand-in** (a database with an in-memory version): test with the stand-in.
- **Owned remote service:** a port at the seam, with an in-memory adapter for tests.
- **Third-party service:** a port at the seam, with a fake adapter for tests.

A seam with one adapter is only indirection. Suggest a port only when two adapters (usually production and test) will use it.
