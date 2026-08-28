# Solana DEX Data

Solana DEX data contains decoded swaps, liquidity events, pool state, order-book events, routes, prices, and fees across decentralized exchanges.

## Canonical DEX event fields

Each event should identify the venue, program ID, pool or market, transaction signature, slot, trader or authority when available, token mints, raw and normalized amounts, price, fee, and status. Store raw integer quantities alongside decimal-normalized values.

## Why DEX data matters for MEV

DEX events are the market evidence used to detect arbitrage, backruns, sandwich candidates, launch sniping, and liquidation activity. Cross-venue comparisons are only meaningful when timestamps, decimals, and pool state are aligned.

## FAQ

### Which DEX data should be normalized first?

Normalize token mint addresses, decimals, direction, venue names, timestamps, and fee units first. Keep protocol-specific fields in an `attributes` object so normalization does not erase useful details.

### Should routed swaps be one event or many?

Keep both views: one strategy-level event for analytics and one leg-level event for execution tracing. Link them with a stable event identifier.
