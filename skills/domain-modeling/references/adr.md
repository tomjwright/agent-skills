# ADR format

Adapted from Matt Pocock's `domain-modeling` skill.

ADRs live in `docs/adr/`, numbered in order: `0001-slug.md`, `0002-slug.md`. To number a new one, find the highest number there and add one.

```md
# <Short title of the decision>

<One to three sentences: the situation, what was decided, and why.>
```

That is a whole ADR. Add these only when they help:

- **Status** (`proposed | accepted | superseded by 0007`), when the decision may be revisited.
- **Considered options**, when a rejected option will be suggested again.
- **Consequences**, when an effect elsewhere isn't obvious.

## What earns an ADR

All three must hold:

1. **Hard to reverse.** Changing your mind later costs real work.
2. **Surprising without context.** A new reader would ask "why did they do it this way?"
3. **A real trade-off.** There were real options and one was picked for a reason.

Good candidates: the shape of the system, how parts talk to each other, a technology that would take months to replace, who owns which data, a deliberate step away from the obvious approach, a constraint the code can't show, and an option rejected for a reason that isn't obvious.

When a checker such as `architecture-check` keeps suggesting something the user has rejected for a lasting reason, that rejection is an ADR.
