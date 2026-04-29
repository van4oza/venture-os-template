# {{SLUG}} — apps index

> Pointer list for sibling code repos that implement {{SLUG}}'s product. Per §3.11 of the
> newco-os proposal: code lives in **sibling** repos, never nested in this venture-os.
> This file is the bridge between operating docs (here) and code (next door).
>
> Each entry is added by hand when a code repo is created. There is no auto-sync — by
> design.

```yaml
apps: []
# Example — replicate per app once one exists:
# apps:
#   - slug: {{SLUG}}-web
#     repo: github.com/van4oza/{{SLUG}}-web
#     purpose: "customer-facing web app"
#     stack: "Next.js, Postgres, Vercel"
#     ci: github.com/van4oza/{{SLUG}}-web/actions
#     specs: 05-product/specs/web/
#     status_links:
#       - 09-rhythms/weekly/
```

## Convention for code-side `CLAUDE.md`

Each app's repo should have a "Venture context" section in its `CLAUDE.md` like:

```
## Venture context

This repo is a product app for venture `{{SLUG}}`.
- Venture-os: github.com/van4oza/{{SLUG}}
- Product specs: 05-product/specs/ in the venture-os
- Customer voice: 02-market/ in the venture-os

This repo owns code, tests, CI, deploys. Do not copy venture operating docs here.
```

That short block keeps both sides aware of the cross-repo relationship without nesting.
