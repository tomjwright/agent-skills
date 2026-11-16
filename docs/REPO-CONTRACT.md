# What a repo provides

The skills are generic. Each repo tells them how it works through a few files at its root. A skill reads these instead of guessing.

## Required: `AGENTS.md`

Most coding agents read `AGENTS.md` already. (For Claude Code, add a `CLAUDE.md` that contains `@AGENTS.md`.) It needs two sections.

### `## Checks`

The exact commands that lint, type-check, test and build the repo, in a fenced block. Skills run these as written.

### `## Standards`

How code should be written here: rules in a list, or links to files such as `CONTRIBUTING.md`. `code-review` checks a change against these and treats them as overriding its own defaults.

## Optional

| File | Used by | Holds |
|---|---|---|
| `GLOSSARY.md` | `grill-with-docs`, `architecture-check` | The project's terms, one definition each |
| `docs/adr/NNNN-title.md` | `grill-with-docs`, `architecture-check` | Decisions that are hard to reverse, so they aren't argued again |
| `## Specs` in `AGENTS.md` | `code-review` | Where specs or issues live, so a change can be checked against what was asked for |

## When something is missing

The skill works out what it can from files like `pyproject.toml`, `package.json` or `Makefile`, labels it "inferred" in its output, and tells you the line to add. It never edits `AGENTS.md` without asking.

## Example

```markdown
## Checks

    uv run ruff check .
    uv run pytest
    cd web && npm run lint && npm run build

## Standards

- Python for the backend, Next.js only for the frontend.
- Prefer plain functions over callbacks and lambdas.
- PRs are small (200-300 lines) and explained in plain English.
```
