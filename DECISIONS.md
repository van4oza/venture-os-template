# Decisions — {{SLUG}}

> Append-only log of decisions that shape the venture's direction, ops, or stack.
> One entry per decision. Newest at the top.
>
> Format per entry:
>
> ```
> ## YYYY-MM-DD — <decision title>
>
> **Context:** what triggered the decision.
> **Options considered:** brief.
> **Choice:** what we picked.
> **Why:** the load-bearing reason.
> **Reversibility:** easy / medium / hard.
> ```
>
> A `PostToolUse` hook emits a `promote-to-hq` reminder when this file is edited — that
> skill is HQ-side and doesn't exist until `founder-hq` is built. Reminder is a no-op
> until then.

---

_(no decisions logged yet)_
