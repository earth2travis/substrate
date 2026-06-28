#!/usr/bin/env bash
#
# substrate-commit.sh - Serialized git commit/push wrapper for concurrent multi-agent operations
#
# Redis: a dedicated staging directory for each SUBSTRATE_STAGING_DIR (defaults to
# - writes file(s) to the staging directory specified, or copies the named file
#   from the working directory to the staging area before taking the lock.
#
# During the critical section (while the flock is held):
#   1. git checkout main
#   2. git pull --ff-only origin main
#   3. mv files from staging into the main working tree (preserving top-level path)
#   4. git add (the moved files only)
#   5. git commit
#   6. git push origin main
#   7. git checkout - (return to whatever branch was active)
#
# Files that already exist in the repo top-level are NOT overwritten; the
# script exits 4 if a collision would occur. This prevents one agent from
# clobbering another's file published moments earlier in a different session.
#
# Lock semantics
#   flock(1) on .git/substrate-commit.lock, exclusive, blocking, 60-s timeout.
#   All file moves and git writes happen while the lock is held, so a second
#   agent that calls this script concurrently will block until the first
#   releases, then it will acquire the lock on a clean tree and proceed.
#
# If git pull --ff-only fails (likely a divergence), the script warns and
# attempts a rebase fallback. If the rebase hits conflicts it exits non-zero
# and leaves the repo on the rebasing branch for manual recovery.
#
# Exit codes
#   0  success, commit pushed
#   1  usage / env error
#   2  lock timeout (another writer held the lock > 60 s)
#   3  git pull --ff-only failed AND rebase fallback also failed
#   4  stewardship collision (target file already exists in repo working tree)
#   5  commit unnecessary (nothing to commit after staging)
#   6  push rejected by remote (manual push needed)
#
# Usage
#   substrate-commit.sh <relative-path-in-repo> [source-file]
#
#   <relative-path-in-repo>   path that the file SHOULD occupy in the repo top
#   [source-file]             local file to copy into staging; if omitted, the
#                             script assumes the file already exists at
#                             $SUBSTRATE_STAGING_DIR/<relative-path-in-repo>
#
# Environment
#   SUBSTRATE_REPO             repo path (default: /home/sivart/substrate)
#   SUBSTRATE_STAGING_DIR      per-agent staging dir (default: mktemp -d)
#   SUBSTRATE_COMMIT_LOCK      lock file path (default: $REPO/.git/substrate-commit.lock)
#   SUBSTRATE_LOCK_TIMEOUT_S   lock wait timeout (default: 60)
#
set -euo pipefail

REPO="${SUBSTRATE_REPO:-/home/sivart/substrate}"
LOCK_TIMEOUT="${SUBSTRATE_LOCK_TIMEOUT_S:-60}"
LOCK_FILE="${SUBSTRATE_COMMIT_LOCK:-$REPO/.git/substrate-commit.lock}"

if [[ $# -lt 1 ]]; then
  echo "usage: $0 <relative-path-in-repo> [source-file]" >&2
  exit 1
fi

DEST_PATH="$1"
SOURCE_FILE="${2:-}"

# Both caller paths validated before touching git. Because the script copies the
# caller's file into a private staging directory and only touches the repo while
# holding an exclusive flock, there is no window where another writer can be
# mid-operation.

STAGING_DIR="${SUBSTRATE_STAGING_DIR:-$(mktemp -d -t substrate-stage.XXXXXX)}"
export SUBSTRATE_STAGING_DIR="$STAGING_DIR"

if [[ "$DEST_PATH" == /* ]]; then
  echo "error: <relative-path-in-repo> must be relative, got '$DEST_PATH'" >&2
  exit 1
fi

# If a source file was supplied, copy it into the staging dir at the repo-relative path.
if [[ -n "$SOURCE_FILE" ]]; then
  if [[ ! -f "$SOURCE_FILE" ]]; then
    echo "error: source file '$SOURCE_FILE' not found" >&2
    exit 1
  fi
  mkdir -p "$STAGING_DIR/$(dirname "$DEST_PATH")"
  cp "$SOURCE_FILE" "$STAGING_DIR/$DEST_PATH"
fi

STAGED_FILE="$STAGING_DIR/$DEST_PATH"
if [[ ! -f "$STAGED_FILE" ]]; then
  echo "error: staged file not found at '$STAGED_FILE'" >&2
  exit 1
fi

if [[ ! -d "$REPO/.git" ]]; then
  echo "error: '$REPO' is not a git repo (no .git dir)" >&2
  exit 1
fi

# Remember the branch the caller was on, so we can return to it at the end.
ORIG_BRANCH="$(git -C "$REPO" rev-parse --abbrev-ref HEAD)"

(
  flock --exclusive --timeout "$LOCK_TIMEOUT" 200 || {
    echo "error: could not acquire lock within ${LOCK_TIMEOUT}s (another writer held it)" >&2
    exit 2
  }

  # From here on we hold the exclusive lock. Every git operation is serialized.
  set -e

  # 1. checkout main
  # If the repo has uncommitted changes (the race scenario), stash them so we
  # can checkout cleanly.
  if ! git -C "$REPO" diff-index --quiet HEAD --; then
    echo "warn: working tree dirty, auto-stashing before checkout main" >&2
    git -C "$REPO" stash push -u -m "substrate-commit auto-stash $(date -Iseconds)"
  fi

  git -C "$REPO" checkout main

  # 2. pull --ff-only
  if ! git -C "$REPO" pull --ff-only origin main; then
    echo "warn: pull --ff-only failed, attempting rebase fallback" >&2
    if git -C "$REPO" pull --rebase origin main; then
      echo "info: rebase fallback succeeded" >&2
    else
      echo "error: pull --ff-only and rebase both failed; repo left on main, manual recovery needed" >&2
      exit 3
    fi
  fi

  # 3. move staged files into the working tree
  TARGET="$REPO/$DEST_PATH"
  if [[ -e "$TARGET" ]]; then
    echo "error: target file '$DEST_PATH' already exists in repo; refusing to overwrite" >&2
    exit 4
  fi
  mkdir -p "$REPO/$(dirname "$DEST_PATH")"
  mv "$STAGED_FILE" "$TARGET"

  # 4. add the moved file
  git -C "$REPO" add "$DEST_PATH"

  # 5. commit
  if git -C "$REPO" diff-index --quiet --cached HEAD --; then
    echo "info: nothing to commit (file already present), cleaning up" >&2
    # the moved file is identical to what's already committed; remove the local copy
    rm -f "$TARGET"
    exit 5
  fi

  COMMIT_MSG="feat: ${DEST_PATH}"
  git -C "$REPO" commit -m "$COMMIT_MSG"

  # 6. push
  if ! git -C "$REPO" push origin main; then
    echo "error: push rejected by remote; manual push needed" >&2
    exit 6
  fi

  # 7. return to the original branch
  git -C "$REPO" checkout "$ORIG_BRANCH" 2>/dev/null || true

  echo "ok: committed and pushed $DEST_PATH"

) 200>"$LOCK_FILE"

# propagate the subshell exit code
exit $?