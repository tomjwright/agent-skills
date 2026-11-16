# What to simplify

Adapted from pstack's "minimize reader load" and "subtract before you add" principles. Reader load has two parts: **layers to trace** between a question and its answer, and **state to hold** in your head while reading. Each candidate below cuts one of them.

| Candidate | What it looks like | Evidence to cite | The change |
|---|---|---|---|
| One-caller wrapper | A function with one caller that only renames or reorders the call | The function, and its one caller | Inline it |
| Pass-through layer | A layer whose methods take the same arguments as the next layer down and forward them | Both signatures side by side | Call the lower layer directly |
| Callback detour | A function or lambda passed in so another function can call it back, where a direct call or a return value would do | The callback, where it's passed, and where it's called | Call it directly, or return the value |
| Adapter with one implementation | An interface or base class with a single implementation and no test double | The interface and its one implementation | Use the implementation directly |
| Dead code | A function, branch, flag or parameter nothing uses | A search showing no callers, and a probe showing no test reaches it | Delete it |
| Option nobody varies | A parameter every caller passes the same value for, or never passes | Every call site | Remove the parameter and use the value |
| Speculative guard | A check for a case the code can't reach, or a spec doesn't ask for | Why the case can't happen, with `file:line` | Delete the check |
| Copy of state | A value stored in two places and kept in sync, where one could be computed from the other | Both places, and the code that syncs them | Compute it when needed |
| Wide mutable scope | State kept in a global, a class field or a closure when a local or a return value would do | Where it's set and where it's read | Narrow it: pass it in or return it |
| Comment that restates code | A comment that says what the next line plainly does | The comment and the line | Delete the comment |

## The deletion test

Before cutting a layer, imagine inlining it into every caller. If the complexity disappears, cut it. If the same lines would appear in each caller, the layer earns its place: leave it.

## The 30-second test

After the change, a new reader should be able to answer "where does X come from?" and "what can change X?" for the code you touched in under 30 seconds. If the change doesn't help with that, it isn't a simplification.

## Not a simplification

- Renaming without cutting a layer or a piece of state.
- Moving code into a new helper "to make it cleaner". That adds a layer.
- Shortening code with tricks a reader has to decode (nested comprehensions, chained ternaries, clever one-liners).
- Changing what a caller outside the scope sees: its arguments, return values, errors or output.
