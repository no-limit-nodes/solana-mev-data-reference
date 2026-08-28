# Solana MEV Data Reference

> Open-source reference for Solana MEV data, arbitrage, DEX activity, liquidity pools, token launches, wallet activity, and real-time blockchain streams.

[![Solana](https://img.shields.io/badge/Solana-MEV-blue)](https://solana.com/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Solana MEV systems require fast access to blockchain data to identify market opportunities, monitor DEX activity, detect new liquidity pools, track token launches, analyze wallet behavior, and evaluate trading opportunities.

This repository provides a practical reference for developers building **Solana MEV searchers, arbitrage systems, sniper infrastructure, market-making systems, indexers, and blockchain analytics platforms**.

---

## Table of Contents

- [What is Solana MEV Data?](#what-is-solana-mev-data)
- [Who Uses Solana MEV Data?](#who-uses-solana-mev-data)
- [What Data Does an MEV Searcher Need?](#what-data-does-an-mev-searcher-need)
- [Solana MEV Data Architecture](#solana-mev-data-architecture)
- [Solana Arbitrage Data](#solana-arbitrage-data)
- [Solana Sniper Data](#solana-sniper-data)
- [Solana DEX Data](#solana-dex-data)
- [Solana Liquidity Pool Data](#solana-liquidity-pool-data)
- [Solana Wallet Data](#solana-wallet-data)
- [Solana Migration Data](#solana-migration-data)
- [Real-Time Solana Data](#real-time-solana-data)
- [Normalized MEV Data Schema](#normalized-mev-data-schema)
- [Building a Solana MEV Data Pipeline](#building-a-solana-mev-data-pipeline)
- [Use Cases](#use-cases)
- [FAQ](#faq)
- [Production Data Infrastructure](#production-data-infrastructure)

---

# What is Solana MEV Data?

Solana MEV data is blockchain data used to identify, evaluate, and monitor market opportunities created by transactions, trading activity, liquidity changes, and state changes on the Solana network.

Common Solana MEV data includes:

- DEX swap events
- Liquidity pool creation
- Pool state
- Liquidity changes
- Token launches
- Token migrations
- Wallet activity
- Transaction data
- Program instructions
- Program events
- Slot information
- Trading volume
- Buy and sell activity

MEV searchers use these signals to build systems for arbitrage, market monitoring, automated trading, token discovery, and analytics.

---

# Who Uses Solana MEV Data?

## 1. Arbitrage Traders

Arbitrage traders monitor multiple Solana DEXs to identify price differences for the same asset.

Typical data requirements include:

- Real-time swaps
- Pool prices
- Pool liquidity
- Trading fees
- Token pairs
- DEX identification
- Slot information
- Transaction signatures

---

## 2. Sniper Bot Operators

Sniper infrastructure monitors new tokens, liquidity pools, migrations, and early trading activity.

Typical signals include:

- New token creation
- New liquidity pool
- Initial liquidity
- Pool initialization
- Token migration
- First trades
- Wallet activity

---

## 3. Market Makers and Professional Trading Desks

Professional trading systems require continuous visibility into:

- Trading volume
- Liquidity
- Buy/sell flow
- Pool state
- Price movement
- Market activity
- Wallet behavior

---

## 4. Indexers

Solana indexers transform blockchain transactions and program events into structured datasets.

An indexer may store:

```text
transactions
instructions
events
swaps
pools
tokens
wallets
liquidity_events
migrations
