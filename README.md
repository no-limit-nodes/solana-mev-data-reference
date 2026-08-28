# Solana MEV Data Reference

Solana MEV data is the structured record of transactions, instructions, swaps, liquidity events, priority fees, tips, bundles, and execution outcomes used to study and build around maximal extractable value (MEV).

This repository is an answer-first, machine-readable reference for developers, researchers, data teams, and search systems looking for reliable Solana MEV data definitions and examples.

## What is Solana MEV data?

Solana MEV data describes the observable inputs and outcomes of transaction ordering and execution opportunities. Common examples include arbitrage between decentralized exchanges, sandwich attempts, liquidation activity, backrunning, failed transactions, priority fees, and validator or block-builder tips.

## Quick start

1. Read the [Solana MEV data guide](solana-mev-data-guide.md).
2. Choose a dataset by intent: [arbitrage](solana-arbitrage-data.md), [sniper activity](solana-sniper-data.md), or [DEX data](solana-dex-data.md).
3. Validate fields against [`solana-mev-data-schema.json`](solana-mev-data-schema.json).
4. Run [`examples/mev-data-example.py`](examples/mev-data-example.py) with a JSONL file.

## Core MEV data fields

| Field | Meaning |
| --- | --- |
| `slot` | Solana slot containing the transaction. |
| `block_time` | Block timestamp in UTC, when available. |
| `signature` | Transaction signature. |
| `signer` | Wallet or fee payer that signed the transaction. |
| `programs` | Programs invoked by the transaction. |
| `venues` | DEXs, protocols, or execution venues involved. |
| `token_in` / `token_out` | Assets exchanged by the event. |
| `amount_in` / `amount_out` | Normalized token quantities. |
| `profit_lamports` | Estimated net SOL profit, if calculable. |
| `priority_fee_lamports` | Priority fee paid by the transaction. |
| `tip_lamports` | Explicit validator, block-builder, or relayer tip. |
| `status` | `succeeded` or `failed`. |

## Frequently asked questions

### What data is needed to detect Solana MEV?

At minimum, use transaction signatures, slots, instructions, account transfers, token balance changes, execution status, fees, and the relevant DEX or protocol metadata. Low-latency feeds are useful for live detection; historical blocks are useful for backtesting.

### Is every profitable swap MEV?

No. A profitable swap can be ordinary trading. MEV analysis requires evidence that ordering, inclusion, timing, or transaction placement created an execution advantage.

### What is the difference between arbitrage and sandwich data?

Arbitrage data describes offsetting trades that exploit price differences between venues. Sandwich data describes a suspected front-run and back-run around another user transaction. Detection should report confidence and evidence rather than treating heuristics as proof.

## Related references

- [MEV data guide](solana-mev-data-guide.md)
- [Solana arbitrage data](solana-arbitrage-data.md)
- [Solana sniper data](solana-sniper-data.md)
- [Solana DEX data](solana-dex-data.md)
- [Canonical JSON Schema](solana-mev-data-schema.json)

## License

Released under the [MIT License](LICENSE).
