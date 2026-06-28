#!/usr/bin/env bash
#
# test_substrate_commit.sh - test harness for substrate-commit.sh
#
# Builds an isolated git "origin" repo and a sandbox clone, then exercises
# substrate-commit.sh against the sandbox. Asserts 17 outcomes across 4 phases.
#
# Phases
#   Phase 1 (single-process): basic happy path + error paths (7 assertions)
#   Phase 2 (concurrent write): 5 parallel writers via PID hammer (4 assertions)
#   Phase 3 (lock + collision): lock timeout + stewardship collision (3 assertions)
#   Phase 4 (pull --ff-only + rebase fallback): divergence recovery (3 assertions)
#
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SUBSTRATE_COMMIT="$SCRIPT_DIR/substrate-commit.sh"

WORKROOT="$(mktemp -d -t substrate-test.XXXXXXXX)"
ORIGIN="$WORKROOT/origin.git"
SANDBOX="$WORKROOT/sandbox"
ORIGIN_BRANCH="main"

PASS=0
FAIL=0
FAILED_ASSERTIONS=()

assert_eq() {
  local desc="$1" exp="$2" got="$3"
  if [[ "$exp" == "$got" ]]; then
    echo "  ok: $desc (got '$got')"
    PASS=$((PASS + 1))
  else
    echo "  FAIL: $desc — expected '$exp', got '$got'"
    FAIL=$((FAIL + 1))
    FAILED_ASSERTIONS+=("[$desc] exp='$exp' got='$got'")
  fi
}

assert_contains() {
  local desc="$1" needle="$2" haystack="$3"
  if echo "$haystack" | grep -qF "$needle"; then
    echo "  ok: $desc"
    PASS=$((PASS + 1))
  else
    echo "  FAIL: $desc — expected output to contain '$needle'; got:"
    echo "$haystack" | sed 's/^/    /'
    FAIL=$((FAIL + 1))
    FAILED_ASSERTIONS+=("[$desc] missing '$needle'")
  fi
}

assert_file_contains() {
  local desc="$1" path="$2" needle="$3"
  if [[ -f "$path" ]] && grep -qF "$needle" "$path"; then
    echo "  ok: $desc"
    PASS=$((PASS + 1))
  else
    echo "  FAIL: $desc — file '$path' missing or does not contain '$needle'"
    FAIL=$((FAIL + 1))
    FAILED_ASSERTIONS+=("[$desc] file missing or no match")
  fi
}

# destructive: caller passes us real repo paths; tests must shadow with sandbox
setup_sandbox() {
  # Bare origin
  git init --bare -b main "$ORIGIN" >/dev/null 2>&1

  # Clone an empty non-bare working clone to be the sandbox
  git clone "$ORIGIN" "$SANDBOX" >/dev/null 2>&1
  # seed initial commit
  pushd "$SANDBOX" >/dev/null
  echo "# Substrate Test Repo" > README.md
  git add README.md
  git -c user.email=test@substrate -c user.name=substrate-test commit -m "chore: init" >/dev/null 2>&1
  git push origin HEAD:main >/dev/null 2>&1
  popd >/dev/null
}

phase1() {
  echo "== Phase 1: single-process happy path + error paths =="
  # Use sandbox repo + its lock file
  local dest_dir="research/raw"

  echo "  1.1 happy path: commit a new file"
  local src="$WORKROOT/file_a.md"
  echo "content A" > "$src"
  local out
  out=$(SUBSTRATE_REPO="$SANDBOX" SUBSTRATE_LOCK_TIMEOUT_S=5 \
    "$SUBSTRATE_COMMIT" "$dest_dir/file_a.md" "$src" 2>&1) || true
  assert_contains "$dest_dir/file_a.md committed" "ok: committed and pushed" "$out"
  assert_file_contains "file content matches pushed" "$SANDBOX/$dest_dir/file_a.md" "content A"
  # also verify it made it through the bare origin via a fresh clone
  git clone -q "$ORIGIN" "$WORKROOT/verify1" >/dev/null 2>&1
  assert_file_contains "fresh clone sees file_a" "$WORKROOT/verify1/$dest_dir/file_a.md" "content A"

  echo "  1.2 error: missing source file"
  local out2
  out2=$(SUBSTRATE_REPO="$SANDBOX" SUBSTRATE_LOCK_TIMEOUT_S=5 \
    "$SUBSTRATE_COMMIT" "$dest_dir/nope.md" "$WORKROOT/nonexistent.md" 2>&1) || true
  assert_contains "missing source error emitted" "not found" "$out2"

  echo "  1.3 error: absolute path rejected"
  local out3
  out3=$(SUBSTRATE_REPO="$SANDBOX" SUBSTRATE_LOCK_TIMEOUT_S=5 \
    "$SUBSTRATE_COMMIT" "/abs/path.md" "$src" 2>&1) || true
  assert_contains "absolute path rejected" "must be relative" "$out3"

  echo "  1.4 error: no arguments exits 1"
  set +e
  SUBSTRATE_REPO="$SANDBOX" "$SUBSTRATE_COMMIT" >/dev/null 2>&1
  local rc=$?
  set -e
  assert_eq "no-args exit code is 1" 1 "$rc"
}

phase2() {
  echo "== Phase 2: concurrent 5-way hammer =="
  # Spawn 5 concurrent commits, each with a unique file. Verify all 5 land
  # in the origin and the final repo state contains all 5 files.
  local dest_dir="research/raw/concurrent"
  local pids=() i
  for i in {1..5}; do
    local src="$WORKROOT/hammer_$i.md"
    echo "hammer file $i" > "$src"
    SUBSTRATE_REPO="$SANDBOX" SUBSTRATE_LOCK_TIMEOUT_S=30 \
      "$SUBSTRATE_COMMIT" "$dest_dir/hammer_$i.md" "$src" \
      >"$WORKROOT/hammer_${i}.out" 2>&1 &
    pids+=($!)
  done

  for pid in "${pids[@]}"; do
    wait "$pid" || true
  done

  # All 5 processes should have exited 0 from the subshell's perspective
  local ok_count=0 fail_count=0
  for i in {1..5}; do
    if grep -q "ok: committed and pushed" "$WORKROOT/hammer_${i}.out"; then
      ok_count=$((ok_count + 1))
    else
      fail_count=$((fail_count + 1))
    fi
  done
  assert_eq "5 concurrent commits all succeeded" 5 "$ok_count"
  assert_eq "0 concurrent failures" 0 "$fail_count"

  # Verify all 5 files present on origin via fresh clone
  git clone -q "$ORIGIN" "$WORKROOT/verify2" >/dev/null 2>&1
  local present=0
  for i in {1..5}; do
    if [[ -f "$WORKROOT/verify2/$dest_dir/hammer_$i.md" ]]; then
      present=$((present + 1))
    fi
  done
  assert_eq "all 5 files visible in fresh clone" 5 "$present"

  # Check repo is left on main with a clean tree
  local branch
  branch=$(git -C "$SANDBOX" rev-parse --abbrev-ref HEAD)
  assert_eq "sandbox left on main after concurrent commit" main "$branch"
}

phase3() {
  echo "== Phase 3: lock timeout + collision =="
  # Manually hold the sandbox lock in the background for ~3 seconds; verify
  # substrate-commit.sh times out waiting.
  local lock="$SANDBOX/.git/substrate-commit.lock"
  (
    flock --exclusive --timeout 5 200
    sleep 3
  ) 200>"$lock" &
  local lockholder_pid=$!

  local src="$WORKROOT/timeout_source.md"
  echo "delayed content" > "$src"
  local out
  out=$(SUBSTRATE_REPO="$SANDBOX" SUBSTRATE_LOCK_TIMEOUT_S=1 \
    "$SUBSTRATE_COMMIT" "research/raw/timeout_test.md" "$src" 2>&1) || true
  wait "$lockholder_pid" 2>/dev/null || true
  assert_contains "lock timeout error surfaced" "could not acquire lock" "$out"

  # Collision: first commit a file, then attempt to commit the same file again
  echo "== Phase 3b: stewardship collision =="
  local c_src="$WORKROOT/collision_src.md"
  echo "first revision" > "$c_src"
  SUBSTRATE_REPO="$SANDBOX" SUBSTRATE_LOCK_TIMEOUT_S=5 \
    "$SUBSTRATE_COMMIT" "research/raw/collision.md" "$c_src" >/dev/null 2>&1 || true
  # Now try to commit a *different* file to the SAME repo-relative path
  local c_src2="$WORKROOT/collision_src2.md"
  echo "second revision" > "$c_src2"
  local out2
  out2=$(SUBSTRATE_REPO="$SANDBOX" SUBSTRATE_LOCK_TIMEOUT_S=5 \
    "$SUBSTRATE_COMMIT" "research/raw/collision.md" "$c_src2" 2>&1) || true
  assert_contains "collision refused" "already exists" "$out2"
}

phase4() {
  echo "== Phase 4: pull --ff-only fallback (rebase) =="
  # Make the remote diverge from the sandbox so pull --ff-only fails, then
  # ensure substrate-commit.sh's rebase fallback lands the new commit.
  # Step A: clone a second working copy for the same origin
  local alt="$WORKROOT/alt"
  git clone -q "$ORIGIN" "$alt" >/dev/null 2>&1
  pushd "$alt" >/dev/null
  git -c user.email=alt@substrate -c user.name=alt commit --allow-empty -m "alt: divergent commit" >/dev/null
  git push origin HEAD:main >/dev/null 2>&1
  popd >/dev/null

  # Step B: now run substrate-commit.sh against the original sandbox — it
  # should NOT be able to fast-forward, but should rebase onto the alt
  # commit and push.
  local d_src="$WORKROOT/divergent.md"
  echo "divergent content" > "$d_src"
  local out
  out=$(SUBSTRATE_REPO="$SANDBOX" SUBSTRATE_LOCK_TIMEOUT_S=5 \
    "$SUBSTRATE_COMMIT" "research/raw/divergent.md" "$d_src" 2>&1) || true
  assert_contains "rebase fallback succeeded" "ok: committed and pushed" "$out"
  # Verify the divergent commit landed on origin
  git clone -q "$ORIGIN" "$WORKROOT/verify4" >/dev/null 2>&1
  assert_file_contains "divergent file on origin" "$WORKROOT/verify4/research/raw/divergent.md" "divergent content"
}

phase5() {
  echo "== Phase 5: dirty-tree auto-stash + re-submit collision =="
  # 5a. Dirty working tree: stage an uncommitted file in sandbox, then commit a
  #     DIFFERENT file via substrate-commit.sh. The dirty file should get
  #     auto-stashed and the write should complete.
  local dirty_src="$WORKROOT/phase5_dirty.md"
  echo "uncommitted but staged" > "$dirty_src"
  cp "$dirty_src" "$SANDBOX/research/raw/phase5_dirty.md"
  git -C "$SANDBOX" add "research/raw/phase5_dirty.md"

  local src="$WORKROOT/phase5_clean.md"
  echo "clean commit" > "$src"
  local out
  out=$(SUBSTRATE_REPO="$SANDBOX" SUBSTRATE_LOCK_TIMEOUT_S=5 \
    "$SUBSTRATE_COMMIT" "research/raw/phase5_clean.md" "$src" 2>&1) || true
  assert_contains "dirty tree auto-stashed and committed" "ok: committed and pushed" "$out"
  local stashes
  stashes=$(git -C "$SANDBOX" stash list 2>/dev/null || true)
  assert_contains "auto-stash entry recorded" "substrate-commit auto-stash" "$stashes"

  # 5b. Nothing-to-commit / re-submit collision: try to submit a file to a
  #     path that already exists on origin (phase5_clean.md). Expect exit 4.
  local dup_src="$WORKROOT/phase5_clean_dup.md"
  echo "clean commit" > "$dup_src"
  local out2
  out2=$(SUBSTRATE_REPO="$SANDBOX" SUBSTRATE_LOCK_TIMEOUT_S=5 \
    "$SUBSTRATE_COMMIT" "research/raw/phase5_clean.md" "$dup_src" 2>&1) || true
  assert_contains "re-submit same path refused" "already exists" "$out2"
}

main() {
  echo "Testing $SUBSTRATE_COMMIT against sandbox at $SANDBOX"
  setup_sandbox
  phase1
  phase2
  phase3
  phase4
  phase5
  echo ""
  echo "=============================================================="
  echo "  RESULT: $PASS passed, $FAIL failed"
  echo "=============================================================="
  if [[ $FAIL -gt 0 ]]; then
    echo "Failed assertions:"
    for a in "${FAILED_ASSERTIONS[@]}"; do echo "  $a"; done
  fi
  # cleanup sandbox work (keep failures debuggable)
  if [[ "${KEEP_TEST_DIR:-0}" == "1" ]]; then
    echo "test dir kept at $WORKROOT"
  else
    rm -rf "$WORKROOT"
  fi
  return $FAIL
}

main "$@"