#!/usr/bin/env python3
"""PreToolUse hook for venture-os: belt+suspenders sensitive-path guard.

Mirrors the .claude/settings.json deny list. Denies Write/Edit/MultiEdit/NotebookEdit
on sensitive paths and Bash commands that mention them. Output uses Claude Code's
hookSpecificOutput schema for PreToolUse.
"""
import json
import re
import sys

SENSITIVE = re.compile(
    r"(clients/raw/|finance/raw/|secrets/|\.env\b|data/private/)"
)


def deny(reason: str) -> None:
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": reason,
                }
            }
        )
    )
    sys.exit(0)


def main() -> None:
    raw = sys.stdin.read()
    if not raw:
        return
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return

    tool = data.get("tool_name", "")
    inp = data.get("tool_input", {}) or {}

    if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        fp = inp.get("file_path", "")
        if fp and SENSITIVE.search(fp):
            deny(
                f"venture-os PreToolUse hook: refused write to sensitive path "
                f"'{fp}' (clients/raw, finance/raw, secrets, .env*, data/private)"
            )
    elif tool == "Bash":
        cmd = inp.get("command", "")
        if cmd and SENSITIVE.search(cmd):
            deny(
                f"venture-os PreToolUse hook: refused Bash command touching sensitive "
                f"path. Command snippet: {cmd[:120]}"
            )


if __name__ == "__main__":
    main()
