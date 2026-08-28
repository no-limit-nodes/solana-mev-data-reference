# Solana MEV Data Reference

> Open-source reference for real-time Solana MEV data, DEX activity, arbitrage signals, liquidity pools, token launches, wallet activity, and trading infrastructure.

[![Solana](https://img.shields.io/badge/Solana-MEV-blue)](https://solana.com/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## What is Solana MEV?

Solana MEV refers to opportunities created by the ordering, execution, and state changes of transactions on the Solana network.

MEV strategies can include:

* DEX arbitrage
* Cross-market arbitrage
* New liquidity pool detection
* Token launch monitoring
* Liquidity migration detection
* Wallet and trader monitoring
* Market-making signals
* Liquidation monitoring
* Statistical trading signals
* On-chain analytics

MEV searchers need fast and reliable blockchain data to identify these opportunities before they disappear.

This repository provides an open-source reference for the data required to build those systems.

---

# Who is this repository for?

This repository is designed for:

### Arbitrage traders

Detect price differences between Solana DEXs and evaluate potential arbitrage opportunities.

### Sniper bot operators

Monitor token launches, liquidity pool creation, migrations, and early trading activity.

### Market makers and professional trading desks

Consume normalized real-time trading and liquidity data to monitor markets and manage strategies.

### Indexers

Build structured Solana datasets from raw blockchain events.

### Analytics teams

Track DEX volume, traders, liquidity, token activity, and market behavior.

### Solana developers

Build trading bots, monitoring systems, data pipelines, and blockchain applications.

---

# What data does a Solana MEV system need?

A useful MEV data pipeline typically needs several categories of information.

| Data            | Purpose                           |
| --------------- | --------------------------------- |
| Transactions    | Detect on-chain activity          |
| Instructions    | Identify program actions          |
| Events          | Extract structured trading events |
| Swaps           | Track token movement              |
| Pool creation   | Discover new markets              |
| Pool state      | Estimate market conditions        |
| Liquidity       | Measure available capital         |
| Token launches  | Discover new assets               |
| Wallet activity | Track traders                     |
| Migrations      | Detect market transitions         |
| Slot/timestamp  | Measure ordering and latency      |
| DEX identity    | Compare markets                   |

The important distinction is that raw transactions are not always enough.

Trading systems generally need **decoded, structured events** that can be consumed quickly.

---

# Solana MEV Data Pipeline

A typical architecture looks like this:

```text
                    Solana
                       │
                       ▼
               Blockchain Events
                       │
                       ▼
              Transaction Stream
                       │
                       ▼
               Instruction Decoder
                       │
                       ▼
                 Event Normalizer
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
        Swaps        Pools        Wallets
          │            │            │
          └────────────┼────────────┘
                       ▼
                 Signal Engine
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
    Arbitrage       Sniping       Analytics
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                  Execution
```

---

# Core MEV Data Signals

## 1. Swap Events

Swap events provide information about trades occurring on decentralized exchanges.

Typical fields include:

```json
{
  "dex": "example",
  "type": "swap",
  "wallet": "...",
  "pool": "...",
  "token_in": "...",
  "token_out": "...",
  "amount_in": 0,
  "amount_out": 0,
  "slot": 0,
  "timestamp": 0,
  "signature": "..."
}
```

Swap data can be used for:

* Price discovery
* Volume tracking
* Arbitrage detection
* Wallet monitoring
* Market-making signals
* Trade analytics
* Copy trading
* Token activity monitoring

---

# 2. Liquidity Pool Creation

New liquidity pools represent newly available trading markets.

A pool creation event can contain:

```json
{
  "dex": "pumpswap",
  "pool": "...",
  "base_mint": "...",
  "quote_mint": "...",
  "initial_liquidity": 0,
  "slot": 0,
  "timestamp": 0
}
```

Pool creation detection is useful for:

* New market discovery
* Token launch monitoring
* Sniper infrastructure
* Liquidity analysis
* Market-making systems
* Early token analytics

Major Solana DEX programs expose different pool creation instructions, so a multi-DEX system should normalize these events into one common schema.

---

# 3. Liquidity Events

Liquidity changes can reveal important market conditions.

Examples:

```text
ADD LIQUIDITY
REMOVE LIQUIDITY
POOL INITIALIZATION
POOL RESERVE CHANGE
LP POSITION CHANGE
```

A trading system can use these signals to estimate:

* Available liquidity
* Potential price impact
* Market depth
* Liquidity risk
* LP behavior

---

# 4. Token Launches

Token launch monitoring can be used to discover newly created markets.

A launch pipeline might look like:

```text
Token Creation
      │
      ▼
Bonding Curve
      │
      ▼
Trading Activity
      │
      ▼
Graduation / Migration
      │
      ▼
DEX Pool
      │
      ▼
Open Market
```

Launch monitoring is particularly important for automated token discovery systems.

---

# 5. Wallet Activity

Wallet-level data allows systems to identify trading behavior.

Example:

```json
{
  "wallet": "...",
  "dex": "pumpswap",
  "action": "buy",
  "token": "...",
  "amount": 1000,
  "slot": 123456789
}
```

Applications include:

* Wallet monitoring
* Copy trading
* Whale tracking
* Trader analytics
* Behavioral analysis
* Portfolio analytics

---

# 6. Migration Events

Migration events represent important state transitions.

For example:

```text
Token Launch
     ↓
Bonding Curve
     ↓
Graduation
     ↓
DEX Migration
     ↓
Liquidity Pool
     ↓
Open Trading
```

A migration-aware data pipeline should ideally correlate the migration and resulting pool creation rather than treating them as unrelated events.

---

# Solana DEX Coverage

MEV systems frequently need data from multiple venues.

This repository organizes data concepts around:

* Raydium
* PumpSwap
* Meteora
* Orca
* Jupiter

Different protocols expose different instruction and account structures.

The purpose of a normalized MEV data layer is to turn those protocol-specific events into a consistent representation.

---

# Building a Solana Arbitrage Detector

A basic arbitrage detector compares the effective price of the same asset across multiple venues.

```text
              SOL/USDC

        Raydium       Meteora
           │             │
           ▼             ▼
        Price A        Price B
           │             │
           └──────┬──────┘
                  ▼
             Price Delta
                  │
                  ▼
           Cost Estimation
                  │
                  ▼
            Profit Check
```

The basic calculation is:

```text
gross_spread =
    sell_price - buy_price

net_profit =
    gross_spread
    - trading_fees
    - priority_fees
    - execution_cost
    - MEV_tip
    - slippage
```

A price difference alone does not guarantee a profitable opportunity.

A production system must consider:

* Pool liquidity
* Slippage
* Fees
* Transaction size
* Priority fees
* Execution probability
* Bundle tips
* State changes
* Opportunity lifetime

---

# Building a New Pool Detector

A simple pool monitoring system can follow:

```python
def on_pool_created(pool):
    print("DEX:", pool.dex)
    print("Pool:", pool.pool)
    print("Base:", pool.base_mint)
    print("Quote:", pool.quote_mint)
    print("Liquidity:", pool.initial_liquidity)
```

The production version should normalize pool creation events from multiple DEX programs.

---

# Building a Swap Monitor

```python
def on_swap(event):
    print(
        event.dex,
        event.token_in,
        event.token_out,
        event.amount_in,
        event.amount_out
    )
```

This can be extended into:

```text
Swap Stream
     ↓
DEX Filter
     ↓
Token Filter
     ↓
Wallet Filter
     ↓
Price Calculation
     ↓
Signal Generation
```

---

# MEV Searcher Architecture

A professional searcher can be separated into five layers.

```text
┌───────────────────────────────┐
│       DATA INGESTION          │
│ RPC / gRPC / WebSocket        │
└───────────────┬───────────────┘
                ▼
┌───────────────────────────────┐
│       EVENT DECODING          │
│ swaps / pools / liquidity     │
└───────────────┬───────────────┘
                ▼
┌───────────────────────────────┐
│       OPPORTUNITY ENGINE      │
│ arbitrage / signals / flows   │
└───────────────┬───────────────┘
                ▼
┌───────────────────────────────┐
│       PROFIT SIMULATION       │
│ fees / slippage / execution   │
└───────────────┬───────────────┘
                ▼
┌───────────────────────────────┐
│       TRANSACTION EXECUTION   │
│ RPC / block engine / bundles  │
└───────────────────────────────┘
```

Data ingestion and transaction execution should be treated as separate components.

---

# Latency Matters

MEV opportunities can disappear quickly.

For this reason, systems should measure:

```text
event_timestamp
        ↓
ingestion_timestamp
        ↓
decode_timestamp
        ↓
signal_timestamp
        ↓
simulation_timestamp
        ↓
submission_timestamp
        ↓
landing_timestamp
```

A useful metric is:

```text
data_latency =
ingestion_timestamp - event_timestamp
```

Another important metric is:

```text
decision_latency =
submission_timestamp - ingestion_timestamp
```

And finally:

```text
landing_latency =
landing_timestamp - submission_timestamp
```

Do not optimize only for API response time.

Measure the complete path.

---

# Data Transport Options

Solana trading systems commonly use combinations of:

### RPC

Useful for:

* Account reads
* Transaction queries
* Historical data
* State inspection

### WebSockets

Useful for:

* Subscriptions
* Account changes
* Transaction notifications
* Lightweight streaming

### gRPC

Useful for:

* High-throughput streams
* Structured events
* Program-specific data
* Low-latency ingestion

### Shred-level infrastructure

Useful for systems that require extremely early blockchain data.

MEV infrastructure should choose its transport based on latency, completeness, operational complexity, and required data granularity.

---

# Example: MEV Data Normalization

Different DEXs may expose different event formats.

The goal is to convert:

```text
Raydium Swap
PumpSwap Buy
Meteora Swap
Orca Swap
```

into:

```json
{
  "type": "swap",
  "dex": "...",
  "pool": "...",
  "trader": "...",
  "token_in": "...",
  "token_out": "...",
  "amount_in": 0,
  "amount_out": 0,
  "slot": 0,
  "signature": "..."
}
```

This allows downstream systems to operate independently of the underlying protocol.

---

# Example: Arbitrage Signal

A normalized signal could look like:

```json
{
  "type": "arbitrage_signal",
  "base_mint": "...",
  "quote_mint": "...",
  "buy_venue": "raydium",
  "sell_venue": "pumpswap",
  "buy_price": 100.0,
  "sell_price": 101.2,
  "gross_spread_bps": 120,
  "estimated_slippage_bps": 25,
  "fees_bps": 15,
  "estimated_net_bps": 80
}
```

This repository focuses on the **data layer**.

It does not guarantee profitability.

---

# Market Maker Data

Market-making systems need more than price data.

Useful signals include:

```text
Trade flow
Liquidity
Pool reserves
Volume
Buy/sell imbalance
Price movement
Wallet concentration
Liquidity changes
```

A normalized market signal might look like:

```json
{
  "pool": "...",
  "volume_1m": 100000,
  "buy_volume_1m": 65000,
  "sell_volume_1m": 35000,
  "liquidity": 500000,
  "buy_sell_ratio": 1.86
}
```

---

# Indexer Architecture

A Solana DEX indexer can use:

```text
Blockchain
    ↓
Stream
    ↓
Decoder
    ↓
Normalizer
    ↓
Database
    ↓
Analytics
    ↓
API
```

Example database tables:

```text
tokens
pools
swaps
liquidity_events
wallets
trades
transactions
migrations
```

Recommended analytical fields include:

```text
slot
block_time
signature
program
instruction
dex
pool
trader
token_in
token_out
amount_in
amount_out
```

---

# Analytics Use Cases

Once events are normalized, teams can calculate:

### DEX volume

```text
Volume by DEX
Volume by token
Volume by pool
Volume by trader
```

### Trader analytics

```text
Number of trades
Buy volume
Sell volume
Average trade size
Trading frequency
```

### Liquidity analytics

```text
Pool liquidity
Liquidity additions
Liquidity removals
Liquidity velocity
```

### Token analytics

```text
Launch time
First trade
First pool
Volume
Unique traders
Liquidity
Migration
```

---

# NoLimitNodes Integration

For production applications, the same concepts can be implemented using real-time decoded Solana program streams.

NoLimitNodes provides program-level streaming infrastructure for Solana applications, including decoded instructions and events.

For example, PumpSwap's `CreatePoolEvent` exposes decoded fields including the pool, base mint, quote mint, initial liquidity, reserves, creator and related accounts.

NoLimitNodes also provides real-time pool-creation data across major Solana DEX programs including Raydium, Meteora, Orca and PumpSwap.

For PumpSwap specifically, available streams include buy, sell, create-pool, liquidity and migration-related activity.

### Production data flow

```text
NoLimitNodes
     │
     ▼
Decoded Program Stream
     │
     ▼
Your Application
     │
 ┌───┼───────────┐
 ▼   ▼           ▼
MEV Bot  Indexer  Analytics
```

Learn more:

* Solana Program Streams
* PumpSwap Data
* Solana Pool Creation Streams
* Solana RPC Infrastructure

---

# Example Production Subscription

```bash
grpcurl \
  -H "x-api-key: YOUR_API_KEY" \
  -import-path . \
  -proto program-streams.proto \
  -d '{
    "topic":"solana.pump_swaps.create_pool_event",
    "format":"JSON"
  }' \
  events.nln.clr3.org:443 \
  nln.stream.v1.StreamService/Subscribe
```

The exact topic and schema should always be checked against the current NoLimitNodes documentation.

---

# MEV Data Checklist

Before building a Solana MEV system, determine whether you need:

* [ ] Real-time transactions
* [ ] Decoded instructions
* [ ] Decoded events
* [ ] Pool creation
* [ ] Swap events
* [ ] Liquidity events
* [ ] Token launches
* [ ] Migration events
* [ ] Wallet activity
* [ ] Historical data
* [ ] Multiple DEXs
* [ ] Slot information
* [ ] Transaction signatures
* [ ] Low-latency transport
* [ ] High-throughput ingestion

---

# Common Solana MEV Questions

## What is Solana MEV?

Solana MEV is the value that can be captured by taking advantage of transaction execution, market-state changes, liquidity differences, and transaction ordering on Solana.

## What data does a Solana arbitrage bot need?

A Solana arbitrage system generally needs real-time swap data, pool state, liquidity, prices, fees, transaction information, and execution-related data.

## How do you detect Solana arbitrage opportunities?

A common approach is to monitor multiple DEXs, normalize their swap and pool data, calculate effective prices, compare venues, and estimate whether the price difference remains profitable after fees, slippage, and execution costs.

## How do you detect new Solana liquidity pools?

Monitor the pool-creation instructions or events emitted by the relevant DEX programs and normalize them into a common pool schema.

## What is Solana DEX data?

Solana DEX data includes swaps, pools, liquidity, token pairs, traders, transactions, prices, and related program events.

## What is a Solana MEV searcher?

A Solana MEV searcher is a system or trader that monitors blockchain activity to identify and potentially execute profitable transaction opportunities.

## What is the difference between RPC and gRPC for Solana data?

RPC is commonly used for request/response blockchain operations, while gRPC is well suited for structured high-throughput streaming workflows.

---

# Related Projects

### Solana Program Data

* Decoded Solana program instructions
* Decoded events
* Account schemas
* Multi-language examples

### Streaming

* Solana program streams
* gRPC examples
* WebSocket examples

### MEV

* Arbitrage detection
* Pool monitoring
* Swap monitoring
* Token launch monitoring
* Wallet monitoring

---

# Disclaimer

This repository provides educational and infrastructure-oriented examples.

An identified price difference does not necessarily represent a profitable arbitrage opportunity.

Production systems should account for:

* Trading fees
* Slippage
* Liquidity
* Priority fees
* Transaction failures
* Execution latency
* Competition
* Network conditions
* Block inclusion
* MEV tips

Always test strategies safely before deploying capital.

---

# Contributing

Contributions are welcome.

Useful contributions include:

* New DEX adapters
* Event schemas
* Data examples
* Language implementations
* Indexing examples
* Analytics queries
* Documentation improvements
* Performance benchmarks

See `CONTRIBUTING.md` for details.

---

# About

Built as an open-source reference for developers building Solana MEV, trading, indexing and analytics infrastructure.

For production-grade real-time Solana data infrastructure, see NoLimitNodes.
