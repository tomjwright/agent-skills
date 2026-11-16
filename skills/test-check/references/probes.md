# Probes

Each probe is one small edit, made in the scratch copy and undone before the next one.

## Breaking a behaviour

Pick the edit that makes the most likely real bug for that behaviour. A caller must be able to see the difference.

| Kind | Edit |
|---|---|
| Condition | Flip it (`>=` to `>`, `and` to `or`, drop a `not`). |
| Boundary | Move a limit by one, or treat an empty input like a full one. |
| Return | Return a fixed value, an empty value, or the input unchanged. |
| Error path | Swallow the error, or raise a different one callers don't branch on. |
| Effect | Skip a write, request or message, or do it twice. |
| Constant | Change a threshold, default or key that the contract depends on. |
| Order | Do two dependent steps in the other order. |

A probe that breaks the code so badly that every test crashes on import tells you nothing. Make a smaller edit.

## Changing the internals

The refactor must keep every result a caller can see. Prove that with a test or script that checks only those results.

| Kind | Edit |
|---|---|
| Rename | Rename a private helper or internal variable. |
| Inline | Inline a helper into its one caller, or extract one. |
| Reorder | Reorder independent internal steps. |
| Swap | Replace an internal collaborator with an equivalent one (a loop for a comprehension, one data structure for another with the same contents). |
| Wording | Change an internal log or message string that no caller reads. |

## Patterns to read for

Taken from Matt Pocock's `tdd` skill and pstack's "test behavior, not implementation".

- **Tautological:** the expected value is computed the way the code computes it, or by calling the code. It can never disagree with the code.
- **Self-built data:** the assertion checks data the test built itself, not what the code returned.
- **Mocked internals:** the test mocks a module the repo owns, so it checks the mock, not the code. Mocking an outside service, the clock or randomness is fine.
- **Side channel:** the test checks a result by reaching past the interface (querying the database directly instead of reading it back through the code).
- **Exact wording:** the test pins a message no caller reads. The error type callers branch on is the contract, not its text.
- **Skipped or always green:** a skipped, empty or `expected failure` test, or one whose assertion can't fail.
- **Too loose:** the assertion accepts wrong answers (`is not None`, `len(x) > 0`) where the contract promises an exact one.
