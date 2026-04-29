#!/usr/bin/env bash
# Bootstrap a freshly-cloned venture-os repo:
#   1. Replace {{SLUG}} and {{NORTH_STAR}} placeholders in seed files.
#   2. Create docs/template-feedback.md (the live-fire friction log).
#
# Usage:
#   scripts/bootstrap.sh <slug> "<north-star-oneliner>"
#
# Example:
#   scripts/bootstrap.sh halo-ai "give every job seeker an interview-ready resume in 10 min"
#
# Idempotent for the SAME args. Re-running with different args after the first run is a
# no-op for already-substituted files (placeholders are gone).

set -euo pipefail

if [ "${1:-}" = "" ] || [ "${2:-}" = "" ]; then
  echo "Usage: $0 <slug> \"<north-star-oneliner>\"" >&2
  echo "  <slug>         filesystem-safe identifier, e.g. halo-ai" >&2
  echo "  <north-star>   one-line statement of the venture's north star (in quotes)" >&2
  exit 64
fi

SLUG="$1"
NS="$2"

if ! printf '%s' "$SLUG" | grep -qE '^[a-z0-9][a-z0-9-]*$'; then
  echo "error: slug must match ^[a-z0-9][a-z0-9-]*\$ (lowercase, digits, hyphens). got: '$SLUG'" >&2
  exit 65
fi

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$repo_root"

files=(
  README.md
  CLAUDE.md
  CURRENT_FOCUS.md
  NORTH_STAR.md
  DECISIONS.md
  SCOREBOARD.md
  05-product/apps-index.md
)

python3 - "$SLUG" "$NS" "${files[@]}" <<'PYEOF'
import sys, pathlib
slug, ns, *files = sys.argv[1:]
for fp in files:
    p = pathlib.Path(fp)
    if not p.exists():
        continue
    text = p.read_text()
    new = text.replace("{{SLUG}}", slug).replace("{{NORTH_STAR}}", ns)
    if new != text:
        p.write_text(new)
PYEOF

mkdir -p docs
if [ ! -f docs/template-feedback.md ]; then
  cat > docs/template-feedback.md <<'EOF'
# Template feedback — observed friction

> Living log of friction encountered while live-firing this clone of `venture-os-template`.
> One bullet per friction. End-of-week-4 review distils these into template patches —
> see VAN-113 in Linear and §B.2 of the newco-os proposal.
>
> What counts as friction:
>   - missing skill, subagent, or hook
>   - awkward layout (a doc you keep wanting to put somewhere it doesn't fit)
>   - bad default in CLAUDE.md / settings.json / a seed file
>   - a hook that fires too often or not often enough
>   - confusion about cross-repo links

## Friction log

- _(no entries yet — add a bullet when something feels awkward, missing, or wrong)_
EOF
fi

cat <<MSG
Bootstrap complete for slug='$SLUG'.

Next steps:
  1. Review CURRENT_FOCUS.md and edit the 1–4 week focus.
  2. Review NORTH_STAR.md and add 'what this means in practice' if useful.
  3. Replace seed columns in SCOREBOARD.md with metrics you actually track.
  4. Commit the bootstrap result:
       git add -A && git commit -m "bootstrap from venture-os-template"
MSG
