# GLOSSARY.md format

Adapted from Matt Pocock's `domain-modeling` skill.

```md
# <Context name>

<One or two sentences: what this part of the project is for.>

## Language

**Fact**:
Something short and lasting about the user, worth knowing in a later conversation.
_Avoid_: memory, note

**Turn**:
One message from the user and everything the agent does to reply to it.
_Avoid_: request, run
```

## Rules

- **Pick one word.** When several words name one idea, choose the best and list the rest under `_Avoid_`.
- **One or two sentences.** Say what the term is, not how the code does it.
- **Project terms only.** Leave out general programming ideas (timeout, retry, cache) even when the project uses them a lot.
- **Group under subheadings** once clear clusters appear. A flat list is fine until then.
- **Keep it in sync.** When a term changes meaning, change its entry. Don't add a second one.

## Several contexts

When parts of the repo use the same word for different things, give each part its own `GLOSSARY.md` and list them in a `GLOSSARY-MAP.md` at the root:

```md
# Glossary map

- Agent, in `tomu/GLOSSARY.md`: the loop, tools and memory
- Page, in `web/GLOSSARY.md`: the step timeline and diagram

## Relationships

- **Agent -> Page**: the agent emits events, and the page draws one step per event
```
