---
name: competitor-brief
description: One-page competitor brief — pulls public pricing, positioning, and recent moves; saves to 02-market/competitors/. Forks a read-only subagent. Use when a new competitor surfaces, a known competitor makes a visible move, or quarterly refresh.
context: fork
---

# competitor-brief

One-page competitor brief. Forked context. Web-research-heavy.

## When to use

- A new competitor surfaced in customer interviews.
- A known competitor made a visible move (pricing change, repositioning, big launch).
- Quarterly competitive refresh.

## What it produces

`02-market/competitors/<competitor-slug>.md`:

```
---
competitor: <name>
url: <homepage>
last_updated: YYYY-MM-DD
---

# <competitor>

## One-liner
<their own framing of what they do>

## Pricing
<table or bullets>

## Positioning
<who they're for; against whom>

## Recent moves
- <date> — <move> (source URL)

## What we beat them on
- ...

## Where they beat us
- ...

## Watchlist
- <thing to check next quarter>
```

## Process

1. Search for: `<competitor> pricing`, `<competitor> changelog`, `<competitor> g2 reviews`,
   `<competitor> hacker news`. Cap at 8 fetches per brief.
2. Read homepage + pricing page + (if obvious) blog index.
3. Fill the brief. Skip sections you can't fill — leave a `_no public evidence_`
   placeholder.
4. Date the brief. Briefs older than 90 days should be flagged for refresh during the
   quarterly review.

## Don't

- Don't copy their copy verbatim. Paraphrase.
- Don't fabricate pricing tiers. If pricing is "contact us," write that.
- Don't update an old brief in place — append a `## YYYY-MM-DD update` section so prior
  state is visible.
