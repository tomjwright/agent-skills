# Changelog

## Unreleased

- Repo setup: conventions, repo contract, skill checker, plugin manifests and install script.
- Add `grilling` (model-invoked interview) and `grill-me` (user-invoked shortcut).
- Add `prove-it` (model-invoked evidence rules for claims and findings).
- Add `code-review` (model-invoked checker: standards, spec and bugs, each finding proven).
- Add `test-check` (model-invoked checker: breaks the code in a scratch copy to find weak, coupled and missing tests).
- `code-review` suggests a fix for each finding, and tries bug fixes in a scratch copy when it's cheap.
- Add `architecture-check` (user-invoked checker: shallow modules, leaked decisions and hand-synced lists in the hot spots, each finding proven).
- Add `simplify` (model-invoked: cuts layers and state a reader must hold, applying only what the user agrees to, with checks run after each change).
