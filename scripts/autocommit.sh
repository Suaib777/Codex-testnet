#!/bin/bash

set -e

echo "🔍 Checking repository..."

# Pastikan git repo
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "❌ Not a git repository"
  exit 1
fi

# Cek perubahan
if [[ -z $(git status --porcelain) ]]; then
  echo "✅ No changes detected. Nothing to commit."
  exit 0
fi

# Optional formatter
if command -v black >/dev/null 2>&1; then
  echo "🎨 Running black formatter..."
  black .
fi

echo "📦 Staging files..."
git add .

DATE=$(date "+%Y-%m-%d %H:%M")

MSG="chore: auto update $DATE"

echo "📝 Committing: $MSG"
git commit -m "$MSG"

echo "🚀 Pushing to remote..."
git push

echo "✅ Done."
