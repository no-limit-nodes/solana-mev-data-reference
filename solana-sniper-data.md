# Solana Sniper Data

Solana sniper data describes fast-entry trading behavior around token launches, liquidity creation, pool initialization, or other market-opening events.

## What to capture

Record the triggering event, first-observed slot, transaction signature, signer, token mint, pool or market address, entry timing, route, amount, outcome, and confidence. Add `detection_method` so readers can distinguish a programmatic heuristic from a confirmed relationship.

## Responsible classification

“Sniper” is a behavioral label, not proof of intent. Useful signals include unusually early entry, repeated launch participation, automated instruction patterns, and consistent low-latency execution. Avoid identifying people from wallet activity alone.

## FAQ

### How is sniper latency measured?

Measure the difference between the launch or liquidity event slot and the entry transaction slot, then report the slot-based measure separately from wall-clock latency.

### What causes false positives?

Validators, deployers, market makers, testers, and ordinary early buyers can resemble snipers. Use confidence scores and preserve the underlying evidence.
