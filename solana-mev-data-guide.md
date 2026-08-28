# Solana MEV Data Guide

## Definition

Solana MEV data is transaction-level and event-level data used to identify value created or captured through transaction ordering, inclusion, timing, or execution. It combines raw ledger data with decoded instructions, token movements, fees, and protocol metadata.

## Data collection layers

### 1. Ledger and transaction layer

Capture the slot, block time, signature, recent blockhash, signers, account keys, instructions, inner instructions, logs, compute units, fee, and execution status. Preserve the raw transaction or a stable reference so derived claims can be audited.

### 2. Protocol and market layer

Decode swaps, liquidity changes, liquidations, oracle updates, and order events. Map program IDs to protocol names and identify token mints, decimals, pool addresses, market addresses, and venue types.

### 3. MEV classification layer

Add an event type such as `arbitrage`, `sandwich_candidate`, `backrun_candidate`, `sniper_candidate`, `liquidation`, or `unknown`. Store the evidence, confidence, estimated gross and net value, and assumptions used by the classifier.

## Recommended record design

Use one record per transaction or one record per detected opportunity. For multi-leg strategies, retain a stable `event_id` and list all related signatures. Never discard failed transactions: failed attempts are useful for measuring competition and execution risk.

## SEO and answer-engine guidance

For documentation and datasets, use descriptive field names, stable URLs, one concept per heading, short definitions before detail, examples near each definition, and explicit limitations. Keep facts separate from estimates. Include timestamps, chain scope, token decimals, data provenance, and confidence for derived metrics.

## Quality checklist

- Normalize timestamps to UTC.
- Store token mint addresses, not symbols alone.
- Record token decimals used for normalization.
- Distinguish transaction fees, priority fees, and tips.
- Mark whether profit is gross, net, realized, or estimated.
- Preserve failed and reverted execution outcomes.
- Link every derived event to source signatures.
- Document detection heuristics and false-positive risks.

## Common pitfalls

Symbol-only data is ambiguous because multiple tokens can share a symbol. Balance deltas can also be misleading when account creation, rent, fees, wrapped SOL, or aggregator routing are involved. A classifier should therefore combine instruction traces, account ownership, balance changes, and venue context.

## FAQ

### What is the best format for Solana MEV data?

JSON Lines is a practical default for streaming and analytics because each event is independently parseable. Pair it with a JSON Schema and a data dictionary so machines and people share the same contract.

### How should MEV profit be calculated?

Calculate gross value from the strategy legs, then subtract trading fees, priority fees, tips, rent effects, and other attributable costs. Label the result as estimated when prices or attribution are incomplete.

### Can this schema prove malicious intent?

No. Transaction data can support behavioral classifications and confidence scores, but intent generally requires additional context. Use labels such as `candidate` and preserve the evidence used.
