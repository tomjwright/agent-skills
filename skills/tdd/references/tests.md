# What a test worth keeping looks like

Adapted from Matt Pocock's `tdd` skill and pstack's `tdd` and `principle-test-behavior-not-implementation`.

## Good

A good test calls a public interface, the way a real caller would, and checks what that caller can observe: a return value, an error, state read back through the same interface, a request sent at the boundary. Its name says what the code does, not how ("recall no longer finds a forgotten fact", not "forget deletes the row").

```python
def test_recall_no_longer_finds_a_forgotten_fact(tmp_path):
    memory = Memory(str(tmp_path / "tomu.db"))
    memory.remember("Tom lives in Singapore")
    memory.forget("Tom lives in Singapore")
    assert memory.recall("weather in Singapore?") == []
```

## Bad

| Pattern | The tell | Instead |
|---|---|---|
| Coupled to the implementation | Mocks code the repo owns, calls a private helper, asserts call counts or order on internal code | Test through the public interface |
| Checked through a side channel | Queries the database or reads a private field instead of using the interface | Read it back through the interface |
| Tautological | The expected value is computed the way the code computes it, so the test can never disagree | Use a literal from the spec or a worked example |
| Horizontal slicing | Every test written first, then all the code | One test, then the code for it, then the next |
| Asserting what the test built | The assertion checks data the test set up, not what the code returned | Assert on the code's output |

## Mocks

Mock only at the system boundary: external APIs, the clock, randomness, and sometimes the file system or database. Never mock the repo's own modules. If a test needs to, the seam is in the wrong place: say so instead of mocking.

## When not to add a test

Prefer no new test to a bad one. If the only test possible needs a large new harness, brittle mocks, slow infrastructure or production-only state, use the closest command that shows the behaviour (a script, a request, a CLI run), and say why there is no test.
