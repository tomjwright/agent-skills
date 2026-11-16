#!/usr/bin/env bash
# Link every skill in this repo into each agent's user-level skills folder.
# The links point back here, so `git pull` updates every agent at once.
set -euo pipefail

repo="$(cd "$(dirname "$0")/.." && pwd)"
destinations=("$HOME/.claude/skills" "$HOME/.agents/skills" "$HOME/.cursor/skills")

for destination in "${destinations[@]}"; do
  mkdir -p "$destination"
  for skill in "$repo"/skills/*/; do
    [ -f "$skill/SKILL.md" ] || continue
    name="$(basename "$skill")"
    if [ -e "$destination/$name" ] && [ ! -L "$destination/$name" ]; then
      echo "skipped $name: $destination/$name exists and is not a link, remove it and re-run" >&2
      continue
    fi
    ln -sfn "${skill%/}" "$destination/$name"
    echo "linked $name into $destination"
  done
done
