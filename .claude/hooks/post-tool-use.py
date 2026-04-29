#!/usr/bin/env python3
"""PostToolUse hook for venture-os.

Two behaviours:
1. Writes/edits to 00-inbox/*.md → ensure markdown frontmatter (date + tags) exists.
2. Writes/edits to DECISIONS.md or 09-rhythms/weekly/* → emit a reminder to consider
   the promote-to-hq skill (HQ-side; reminder only, not actionable until founder-hq
   exists).

Output uses Claude Code's hookSpecificOutput.additionalContext to surface the reminder.
"""
import datetime as dt
import json
import re
import sys
from pathlib import Path

INBOX_PATTERN = re.compile(r"(^|/)00-inbox/.+\.md$")
DECISIONS_PATTERN = re.compile(r"(^|/)DECISIONS\.md$")
WEEKLY_PATTERN = re.compile(r"(^|/)09-rhythms/weekly/.+\.md$")
FRONTMATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)


def emit_context(text: str) -> None:
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "additionalContext": text,
                }
            }
        )
    )


def normalize_inbox_frontmatter(file_path: str) -> str | None:
    p = Path(file_path)
    if not p.exists():
        return None
    text = p.read_text()
    if FRONTMATTER_RE.match(text):
        return None
    today = dt.date.today().isoformat()
    p.write_text(f"---\ndate: {today}\ntags: []\n---\n\n{text}")
    return f"Added frontmatter to {file_path} (00-inbox normalisation)."


def main() -> None:
    raw = sys.stdin.read()
    if not raw:
        return
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return

    tool = data.get("tool_name", "")
    if tool not in ("Write", "Edit", "MultiEdit"):
        return

    fp = (data.get("tool_input", {}) or {}).get("file_path", "")
    if not fp:
        return

    messages: list[str] = []

    if INBOX_PATTERN.search(fp):
        msg = normalize_inbox_frontmatter(fp)
        if msg:
            messages.append(msg)

    if DECISIONS_PATTERN.search(fp) or WEEKLY_PATTERN.search(fp):
        messages.append(
            "Reminder: this write touched a rolling doc (DECISIONS.md or weekly review). "
            "Consider running the `promote-to-hq` skill once founder-hq exists, to lift "
            "any cross-cutting lessons out of this venture into HQ. (Skill is HQ-side; "
            "this reminder is a no-op until then.)"
        )

    if messages:
        emit_context("\n".join(messages))


if __name__ == "__main__":
    main()
