---
name: customer-voice-synthesis
description: Synthesise patterns from raw customer interviews, transcripts, or surveys into 02-market/customer-voice/. Use when fresh raw notes have landed and you need a structured pass over them. Forks a read-only subagent to keep the main session window clean.
context: fork
---

# customer-voice-synthesis

Forked, read-only synthesis pass over raw customer evidence.

## When to use

- New interview transcripts dropped into `clients/raw/<slug>/` (gitignored).
- Survey results landed in `02-market/_survey-runs/`.
- A weekly review noted "we should pull together what customers have been saying."

## What it produces

A new or updated file at `02-market/customer-voice/<topic>.md`:

```
---
date: YYYY-MM-DD
sources: [<paths or run IDs>]
n_interviews: <int>
---

# <topic>

## Patterns

- <pattern 1> — observed in <n> sources. Quote: "..."
- <pattern 2> — ...

## Outliers

- <outlier 1> — single source, but worth flagging.

## What this means

- <prescription 1>
- <prescription 2>

## Open questions
```

## Process

1. List the raw sources you'll read. Sources under `clients/raw/` are normally denied
   at the settings level. The forked subagent inherits those deny rules — if you cannot
   read a path, that is by design. Escalate to the human rather than working around it.
2. Tag each excerpt you cite with `path:line`.
3. Group excerpts into 3–7 patterns. Anything with < 3 sources stays an outlier, not a
   pattern.
4. Write to `02-market/customer-voice/<topic>.md`. Do not delete previous customer-voice
   files; topics may be revisited every few weeks.

## Don't

- Don't quote anything from `clients/raw/` *verbatim* into a tracked file unless the
  customer has explicitly cleared the quote for use. Paraphrase by default.
- Don't mix synthesis with prescription. Patterns first, prescriptions last, clearly
  separated.
