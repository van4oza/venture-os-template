---
name: launch-readiness
description: Manual-only pre-launch coherence check for {{SLUG}}. Verifies offer, pricing, ops, and customer-comms before a public launch. Disabled for model invocation — call explicitly.
disable-model-invocation: true
---

# launch-readiness

Manual pre-launch coherence check. Not auto-invoked — you call this explicitly when
you're 1–7 days from a launch.

## What it produces

A go/no-go checklist at `03-offer/_launches/YYYY-MM-DD-<launch-slug>.md`:

```
# Launch readiness — YYYY-MM-DD — <launch-slug>

## Offer coherence
- [ ] Pricing in `03-offer/` matches what marketing pages say.
- [ ] Packaging is documented; tier names match in offer doc, marketing, and billing.
- [ ] Inclusions and explicit exclusions are listed.

## Customer comms
- [ ] Existing customers warned about price/packaging changes (if any) ≥ 14 days out.
- [ ] Launch announcement drafted and queued.
- [ ] Support FAQ updated with new pricing/terms.

## Ops
- [ ] Billing system can issue the new SKUs.
- [ ] Refund / cancellation policy unchanged or explicitly updated.
- [ ] Onboarding doc reviewed against the new offer.

## Marketing
- [ ] Landing page reflects current pricing.
- [ ] Channel briefs updated in `06-marketing/`.

## Sales
- [ ] Sequences in `04-sales/` updated.
- [ ] Talk-track for the new offer rehearsed at least once.

## Roll-back plan
- [ ] What we revert if the launch is a flop in week 1.

## Sign-off
- [ ] Founder go/no-go: <name>, <date>.
```

## When NOT to use

- Mid-quarter offer tweaks. Use `offer-and-pricing-review` for those.
- Code-level launches. Those go through CI/CD in the sibling product repo.

## Don't

- Don't auto-invoke this. The whole point is the manual ritual.
- Don't sign off on the launch from inside Claude. The human signs off on their own line.
