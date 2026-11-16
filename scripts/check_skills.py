"""Check every skill in skills/ against docs/CONVENTIONS.md.

Run from the repo root:  python3 scripts/check_skills.py
Prints one line per problem and exits 1 if there are any.
"""

import re
import sys
from pathlib import Path

NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")
SKILL_REF = re.compile(r"the `([a-z0-9-]+)` skill")


def read_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with a --- frontmatter block")
    header, _, body = text[4:].partition("\n---\n")
    fields = {}
    for line in header.splitlines():
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip().strip('"')
    return fields, body


def is_user_invoked(fields: dict[str, str]) -> bool:
    return fields.get("disable-model-invocation") == "true"


def check_skill(folder: Path, user_invoked_names: set[str], all_names: set[str]) -> list[str]:
    where = f"skills/{folder.name}"
    fields, body = read_frontmatter((folder / "SKILL.md").read_text())
    problems = []

    name = fields.get("name", "")
    if name != folder.name:
        problems.append(f"{where}: name {name!r} must match the folder name")
    if not NAME.match(name) or len(name) > 64:
        problems.append(f"{where}: name must be lowercase words joined by hyphens, at most 64 characters")

    description = fields.get("description", "")
    if not description:
        problems.append(f"{where}: description is missing")
    elif len(description) > 1024:
        problems.append(f"{where}: description is longer than 1024 characters")

    codex = folder / "agents" / "openai.yaml"
    if not codex.exists():
        problems.append(f"{where}: agents/openai.yaml is missing")
    elif is_user_invoked(fields) != ("allow_implicit_invocation: false" in codex.read_text()):
        problems.append(f"{where}: disable-model-invocation and agents/openai.yaml policy disagree")

    for md in folder.rglob("*.md"):
        if "\u2014" in md.read_text():
            problems.append(f"{where}: {md.relative_to(folder)} uses an em dash")
        for target in LINK.findall(md.read_text()):
            if "://" not in target and not (md.parent / target).exists():
                problems.append(f"{where}: broken link {target!r} in {md.relative_to(folder)}")

    for ref in SKILL_REF.findall(body):
        if ref not in all_names:
            problems.append(f"{where}: refers to the `{ref}` skill, which does not exist")
        elif ref in user_invoked_names:
            problems.append(f"{where}: refers to the `{ref}` skill, but only a person can start it")

    return problems


def check_repo(root: Path) -> list[str]:
    folders = sorted(path.parent for path in (root / "skills").glob("*/SKILL.md"))
    problems, parsed, user_invoked = [], [], set()
    for folder in folders:
        try:
            fields, _ = read_frontmatter((folder / "SKILL.md").read_text())
        except ValueError as error:
            problems.append(f"skills/{folder.name}: {error}")
            continue
        parsed.append(folder)
        if is_user_invoked(fields):
            user_invoked.add(folder.name)

    all_names = {folder.name for folder in folders}
    readme = (root / "README.md").read_text()
    for folder in parsed:
        problems += check_skill(folder, user_invoked, all_names)
        if f"(skills/{folder.name}/SKILL.md)" not in readme:
            problems.append(f"skills/{folder.name}: not linked from README.md")
    return problems


if __name__ == "__main__":
    found = check_repo(Path.cwd())
    print("\n".join(found) or "All skills pass.")
    sys.exit(1 if found else 0)
