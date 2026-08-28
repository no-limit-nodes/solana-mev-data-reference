# Solana Arbitrage Data

Solana arbitrage data records trades that seek to capture price differences for the same asset across DEXs, pools, order books, or routes.

## Minimum fields

Capture the transaction signature, slot, signer, ordered trade legs, input and output mints, normalized quantities, venues, fees, tips, and execution status. A multi-leg event should include the source signature and an `event_id` linking all legs.

## Detection model

An arbitrage candidate usually has two or more swaps, a coherent asset flow, and a positive end-to-end value after attributable costs. Compare prices using the same token decimals and a consistent valuation timestamp. Report candidates separately from confirmed opportunities.

## Useful metrics

- Gross spread and net profit
- Capital deployed
- Number of legs and venues
- Priority fee and tip paid
- Execution latency and failure rate
- Competition by slot
- Profit per compute unit

## FAQ

### What makes a Solana arbitrage candidate credible?

Credibility increases when all legs are linked to one transaction or strategy, token flows reconcile, venue prices are decoded correctly, and fees are included in the net result.

### Does arbitrage require a private relay?

No. Arbitrage can be submitted through public or private infrastructure. The dataset should record the submission path only when it is known, rather than assuming one.
