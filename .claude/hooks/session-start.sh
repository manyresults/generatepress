#!/bin/bash
#
# SessionStart hook: install the generateblocks-skills submodule's SKILL folders
# into ~/.claude/skills/ so future turns can invoke them (generateblocks-layouts,
# html-to-generateblocks, elementor-to-generateblocks, figma-to-generateblocks).
#
# Only runs in Claude Code on the web (the container is ephemeral and starts
# without ~/.claude/skills populated). Local sessions are skipped.
set -euo pipefail

# Skip on local dev; only run in a remote/web container.
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

REPO_ROOT="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)}"
cd "$REPO_ROOT"

# Populate the submodule if a fresh clone missed --recurse-submodules.
if [ -f .gitmodules ] && [ ! -f generateblocks-skills/install.sh ]; then
  git submodule update --init --recursive
fi

# Idempotent copy into ~/.claude/skills/<skill>/.
if [ -x generateblocks-skills/install.sh ]; then
  ./generateblocks-skills/install.sh claude
fi
