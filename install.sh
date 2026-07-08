#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_NAME="home-custom-recommender"
DEST="${CODEX_HOME:-$HOME/.codex}/skills/$SKILL_NAME"

mkdir -p "$(dirname "$DEST")"

if [ -e "$DEST" ]; then
  echo "Skill already exists: $DEST"
  echo "Remove it first or back it up before reinstalling."
  exit 1
fi

cp -R "$ROOT/skills/$SKILL_NAME" "$DEST"
echo "Installed $SKILL_NAME to $DEST"
echo "Restart Codex to pick up the new skill."
