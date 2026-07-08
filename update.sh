#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_NAME="home-custom-recommender"
DEST="${CODEX_HOME:-$HOME/.codex}/skills/$SKILL_NAME"

if command -v git >/dev/null 2>&1 && [ -d "$ROOT/.git" ]; then
  git -C "$ROOT" pull --ff-only
fi

rm -rf "$DEST"
mkdir -p "$(dirname "$DEST")"
cp -R "$ROOT/skills/$SKILL_NAME" "$DEST"

echo "Updated $SKILL_NAME at $DEST"
echo "Restart Codex to pick up the updated skill and vendor data."
