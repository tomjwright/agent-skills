# Showing the change

The menu below is adapted from Dex Horthy's [`show-me`](https://github.com/humanlayer/humanlayer) skill, by way of Matt Pocock's `pr` skill. Pick the smallest view that makes the key point clear. One is usually enough, and two is plenty.

| The point is | Show it as |
|---|---|
| Logic or an algorithm | Pseudocode |
| What calls what at runtime | A call tree |
| Where code lives, or a broad refactor | A shallow file tree with a comment per line |
| Messages between parts | A Mermaid sequence diagram |
| What changed in an existing shape | A `diff` of the pseudocode, call tree or file tree |
| A new shape a reader will copy | The whole block |

Pseudocode:

```text
on(save)
  if content is unchanged
    return cached result
  write new content
```

A call tree, as a diff:

```diff
 run_agent
   memory.recall
+  memory.forget
   run_loop
```

A file tree:

```text
tomu/
├── memory.py    # facts, history and traces in one SQLite file
└── loop.py      # the reason, act, observe loop
```

Keep only the calls, files and states the reader needs for this PR. Put each one next to the sentence it supports.
