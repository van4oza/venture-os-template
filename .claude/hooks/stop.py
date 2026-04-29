#!/usr/bin/env python3
"""Stop hook for venture-os: nag about weekly review when rolling docs were touched.

Reads `git status` and, if any rolling doc has uncommitted changes, emits a reminder to
run / update the weekly operating review.
"""
import json
import os
import subprocess
import sys

ROLLING_PATTERNS = (
    "00-inbox/",
    "09-rhythms/",
    "DECISIONS.md",
    "SCOREBOARD.md",
    "CURRENT_FOCUS.md",
)


def emit_context(text: str) -> None:
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "Stop",
                    "additionalContext": text,
                }
            }
        )
    )


def repo_root() -> str | None:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            check=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None
    return out.stdout.strip()


def main() -> None:
    sys.stdin.read()  # consume the hook input; we don't use it

    root = repo_root()
    if not root:
        return
    os.chdir(root)

    try:
        out = subprocess.run(
            ["git", "status", "--short"],
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError:
        return

    touched = [
        line for line in out.stdout.splitlines()
        if any(pat in line for pat in ROLLING_PATTERNS)
    ]
    if not touched:
        return

    emit_context(
        "Reminder: this session touched rolling docs:\n"
        + "\n".join(touched[:8])
        + "\n\nConsider updating 09-rhythms/weekly/<this-week>.md before closing the loop."
    )


if __name__ == "__main__":
    main()
