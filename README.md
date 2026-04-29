# {{SLUG}}

> {{NORTH_STAR}}

Venture-os repo for **{{SLUG}}**, cloned from
[`venture-os-template`](https://github.com/van4oza/venture-os-template). Holds business
operations — thesis, market, offer, sales, product specs, marketing, finance, ops, and
operating rhythms — for one venture. Product code lives in **sibling repos** (see
`05-product/apps-index.md`).

## First-time setup

If you cloned this from the template via `gh repo create ... --template ...`, the seed
files still contain `{{SLUG}}` and `{{NORTH_STAR}}` placeholders. Replace them in one
shot:

```bash
./scripts/bootstrap.sh <slug> "<north-star-oneliner>"
git add -A && git commit -m "bootstrap from venture-os-template"
```

`bootstrap.sh` rewrites the seed files in place and creates `docs/template-feedback.md`
for the live-fire friction log.

## Layout — quick reference

```
00-inbox/                # daily captures, one line per item
01-thesis/               # what we believe, why we're building this
02-market/               # customer voice, competitor briefs, pricing data
03-offer/                # what we sell, packaging, positioning
04-sales/                # pipeline, lessons, lost-deal analysis
05-product/              # specs, roadmap, experiments + apps-index.md
06-marketing/            # channels, messaging, content
07-finance/              # P&L, runway, unit economics
08-ops/                  # internal processes, tooling, vendor list
09-rhythms/              # daily / weekly / monthly / quarterly reviews
10-templates/            # local templates for recurring docs
11-archive/              # deprecated docs, kept for history
scripts/                 # bootstrap.sh + ad-hoc venture scripts
.claude/                 # subagents, skills, hooks, settings
```

`CLAUDE.md` is the long-form project brief and is what Claude reads first.

## Sensitive paths

`clients/raw/`, `finance/raw/`, `secrets/`, `.env*`, and `data/private/` are gitignored
**and** denied at `.claude/settings.json` level **and** rejected by a `PreToolUse` hook.
Belt + suspenders: never commit raw client interviews, raw P&L exports, or credentials.

## What this repo is not

- Not a code repo. Product code is in sibling repos cloned next to this one.
- Not a personal knowledge base. Career memory belongs in `founder-hq` (separate repo).
- Not a database. Markdown only; cross-repo links are pointers + copy-on-ingest.

## Source of truth for design

`docs/proposals/newco-os.md` in the resume-builder repo, sections §3.4–§3.12.
