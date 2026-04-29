---
name: offer-and-pricing-review
description: Stress-test the current offer and pricing for {{SLUG}}. Reads 03-offer/, NORTH_STAR.md, recent customer-voice synthesis, and competitor briefs; produces a memo with proposed changes. Use before raising prices, launching a new offer, or quarterly.
---

# offer-and-pricing-review

Stress-test the active offer + pricing.

## When to use

- Quarterly offer review.
- Before a price change.
- Before launching a new offer or sunsetting an existing one.
- After a cluster of lost deals where price came up.

## What it produces

A dated review note at `03-offer/_reviews/YYYY-MM-DD-review.md`:

```
# Offer review — YYYY-MM-DD

## What we have today
<summary of current offer + pricing>

## Stress tests
- **Anchor test:** is the price anchored against the right alternative?
- **Packaging test:** does the bundle match how customers actually buy?
- **Win/loss test:** what did the last 5 wins and 5 losses say about price?
- **Competitor delta:** where are we above/below; can we defend it?
- **NS alignment:** does the offer push toward {{NORTH_STAR}}?

## Recommendations
1. <change 1> — why, expected impact, reversibility.
2. <change 2> — ...

## Decisions needed
- ...
```

## Inputs to read

- `03-offer/**` — current offer docs.
- `NORTH_STAR.md`, `CURRENT_FOCUS.md`.
- `02-market/customer-voice/**` — patterns from real customers.
- `02-market/competitors/**` — recent competitor briefs.
- `04-sales/lost-deals/**` — recent lost-deal log entries.

## Process

1. Read all inputs. Cap at the 6 most recent files per directory.
2. Run each stress test. Note pass / fail / unknown.
3. Draft 1–4 recommendations. Each must include:
   - **Why** — which stress test surfaced it.
   - **Expected impact** — gut estimate, not fake precision.
   - **Reversibility** — easy / medium / hard.
4. Save to `03-offer/_reviews/YYYY-MM-DD-review.md`. Do **not** edit live offer docs in
   this skill — recommendations route through `offer-architect`.

## Don't

- Don't skip stress tests because the answer is uncomfortable.
- Don't recommend price changes without evidence from win/loss or competitor delta.
- Don't mix recommendations with implementation. This skill produces a memo.
