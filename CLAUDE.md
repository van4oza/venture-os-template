# CLAUDE.md — {{SLUG}}

This is a venture-os instance for **{{SLUG}}**.
North star: **{{NORTH_STAR}}**.

## What this repo is

Markdown-first business operations repo for one venture. Holds thesis, market, offer,
sales, product specs, marketing, finance, ops, and operating rhythms. Product code lives
in **sibling repos** — see `05-product/apps-index.md`. This repo's lifetime tracks the
venture's lifetime.

## Layout (§3.4 of the newco-os proposal)

```
README.md  CLAUDE.md
CURRENT_FOCUS.md  NORTH_STAR.md  DECISIONS.md  SCOREBOARD.md
00-inbox/                # daily captures, one line per item
01-thesis/               # what we believe, why we're building this
02-market/               # customer voice, competitor briefs, pricing data
03-offer/                # what we sell, packaging, positioning
04-sales/                # pipeline, lessons, lost-deal analysis
05-product/
  apps-index.md          # pointer list for sibling code repos
  specs/  roadmap/  experiments/
06-marketing/            # channels, messaging, content
07-finance/              # P&L, runway, unit economics (raw data ignored)
08-ops/                  # internal processes, tooling, vendor list
09-rhythms/
  daily/ weekly/ monthly/ quarterly/
10-templates/            # local templates for recurring docs
11-archive/              # deprecated docs, kept for history
scripts/                 # bootstrap.sh, ad-hoc venture scripts
.claude/                 # subagents, skills, hooks, settings
```

## Subagents (§3.5)

Three custom subagents live in `.claude/agents/`:

- `research-synthesizer` — read-only synthesis of customer voice, competitor signal,
  market evidence. Tools: `Read, Glob, Grep, WebFetch, WebSearch`.
- `offer-architect` — drafts and revises offer/pricing/positioning docs in `03-offer/`.
  Tools: `Read, Write, Edit, Glob, Grep`.
- `growth-ops` — drafts marketing/sales experiments. Tools: `Read, Write, Edit,
  WebFetch, WebSearch`.

Skills are NOT auto-inherited into subagent contexts — list them explicitly when a
subagent should run a skill.

## Skills (§3.6, template-side only)

Four skills live in `.claude/skills/`:

- `customer-voice-synthesis` — extracts patterns from raw interviews/surveys.
  `context: fork` (forked read-only subagent).
- `competitor-brief` — quick competitive scan with web research. `context: fork`.
- `offer-and-pricing-review` — stress-test the current offer + pricing.
- `launch-readiness` — manual-only pre-launch checklist. `disable-model-invocation: true`.

(HQ-side skills like `inbox-to-actions`, `weekly-operating-review`, `decision-memo`,
`postmortem`, `promote-to-hq` live in `founder-hq`, not here.)

## Hooks (§3.7) — they nag, they don't decide

Three hooks live in `.claude/hooks/` and are wired in `.claude/settings.json`:

- `PreToolUse` — blocks writes / Bash commands touching sensitive paths
  (belt+suspenders with the deny list).
- `PostToolUse` — on writes to `00-inbox/*.md` adds missing markdown frontmatter; on
  writes to `DECISIONS.md` or `09-rhythms/weekly/*` emits a `promote-to-hq` reminder
  (no-op until `founder-hq` exists).
- `Stop` — if the session left rolling docs (`00-inbox/`, `09-rhythms/`, `DECISIONS.md`,
  `SCOREBOARD.md`, `CURRENT_FOCUS.md`) with uncommitted changes, reminds to update
  the weekly review.

## Sensitive paths — always denied

`clients/raw/**`, `finance/raw/**`, `secrets/**`, `.env*`, `data/private/**`. Triple-guarded:
`.gitignore`, `.claude/settings.json` deny rules, and the `PreToolUse` hook.

## Cross-repo links (§3.10–§3.11)

Product code lives in **sibling** repos at `~/projects/ventures/<slug>-<app>/`, never
nested here. The bridge is `05-product/apps-index.md` (YAML manifest of `slug + repo +
local_path + purpose + stack + ci`). On the code-repo side, each app's `CLAUDE.md`
references this venture-os by URL.

Avoid: filesystem nesting, submodules, central index databases.

## Don't

- Don't paste raw client interviews into `02-market/`. Drop them in `clients/raw/`
  (gitignored), then synthesise via the `customer-voice-synthesis` skill.
- Don't put career or personal-brand docs here — those belong in `founder-hq`.
- Don't try to auto-sync between this repo and `founder-hq`. Crossings are editorial via
  `promote-to-hq`.

## Source of truth for design

`docs/proposals/newco-os.md` in the resume-builder repo, §3.4–§3.12.
