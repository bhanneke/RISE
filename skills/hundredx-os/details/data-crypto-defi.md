# Crypto & DeFi Data Skill

## On-Chain Data Sources

### Flipside Crypto
- SQL interface to decoded blockchain data
- Key schemas: `ethereum.core`, `ethereum.defi`, `solana.core`
- Authentication: `x-api-key` header
- Rate limits: vary by plan; cache aggressively

### Allium
- SQL interface via `https://mcp.allium.so`
- Authentication: `X-API-KEY` header
- Cross-chain coverage: Ethereum, Solana, Arbitrum, Optimism, Base, Polygon

### Dune Analytics
- SQL (DuneSQL, Trino-based) on decoded EVM data
- Public queries can be forked; API for programmatic access
- Good for quick exploration; Flipside/Allium better for large extracts

### CoinGecko
- Free API for token prices, market cap, volume
- `https://api.coingecko.com/api/v3/`
- Rate limit: 10-30 calls/min (free tier)

## Common DeFi Data Patterns

### DEX / AMM Data

```sql
-- Uniswap V2/V3 swap events
SELECT
    block_timestamp,
    tx_hash,
    pool_address,
    token_in,
    token_out,
    amount_in_usd,
    amount_out_usd,
    sender AS trader
FROM ethereum.defi.ez_dex_swaps
WHERE platform = 'uniswap-v3'
  AND block_timestamp >= '2023-01-01'
ORDER BY block_timestamp;

-- Liquidity provision (mint/burn events)
SELECT
    block_timestamp,
    action,  -- 'mint' or 'burn'
    pool_address,
    liquidity_provider,
    amount0_usd,
    amount1_usd,
    tick_lower,
    tick_upper  -- V3 concentrated liquidity range
FROM ethereum.defi.ez_lp_actions
WHERE platform = 'uniswap-v3';
```

### Lending Protocol Data

```sql
-- Aave/Compound borrow & supply events
SELECT
    block_timestamp,
    protocol_name,
    action,  -- 'deposit', 'withdraw', 'borrow', 'repay', 'liquidation'
    depositor_address,
    token_address,
    token_symbol,
    amount_usd
FROM ethereum.defi.ez_lending
WHERE protocol_name IN ('aave-v3', 'compound-v3')
  AND block_timestamp >= '2023-01-01';
```

### Token Transfers & Prices

```sql
-- ERC-20 token transfers
SELECT
    block_timestamp,
    tx_hash,
    from_address,
    to_address,
    contract_address AS token_address,
    symbol,
    amount,
    amount_usd
FROM ethereum.core.ez_token_transfers
WHERE contract_address = LOWER('0x...')  -- specific token
  AND block_timestamp BETWEEN '2023-01-01' AND '2024-01-01';

-- Hourly token prices
SELECT
    hour,
    token_address,
    symbol,
    price
FROM ethereum.price.ez_prices_hourly
WHERE symbol = 'WETH';
```

### MEV & Transaction Ordering

```sql
-- Sandwich attacks / MEV transactions
SELECT
    block_number,
    block_timestamp,
    tx_hash,
    mev_type,  -- 'sandwich', 'arbitrage', 'liquidation'
    profit_usd,
    victim_tx_hash
FROM ethereum.mev.ez_mev_transactions
WHERE mev_type = 'sandwich';
```

## Research-Relevant Variables

### Market Microstructure
- **Spread**: Bid-ask spread inferred from swap prices within same block
- **Depth**: Total liquidity at various price ticks (V3) or total reserves (V2)
- **Volume**: USD swap volume aggregated hourly/daily
- **Price impact**: Percentage price change per unit trade size
- **Slippage**: Difference between expected and executed price

### DeFi-Specific Measures
- **TVL (Total Value Locked)**: Sum of assets deposited in protocol
- **Utilization rate**: Borrowed / (borrowed + available) in lending protocols
- **Impermanent loss**: Divergence loss from providing liquidity vs. holding
- **Gas costs**: Transaction fees as a real friction in trade execution
- **Protocol revenue**: Fees collected by the protocol treasury

### Wallet-Level Panel Data
- **Active addresses**: Unique addresses transacting per period
- **Wallet age**: Blocks since first transaction
- **Portfolio concentration**: Herfindahl index of token holdings
- **Transaction frequency**: Trades per period per wallet
- **Net flow**: Inflows minus outflows to a protocol or wallet

## Data Quality Issues

1. **Bot / MEV activity**: A large fraction of DEX transactions are bots. Filter or control for:
   - Sandwich attack transactions
   - Arbitrage bots (high-frequency, small-profit trades)
   - Flash loan transactions (single-block round-trips)

2. **Pseudonymity ≠ one person**: One person can have many wallets; one wallet can represent a smart contract with many users. Address clustering is an open research problem.

3. **Block timestamps are imprecise**: Ethereum blocks are ~12 seconds. For intra-block ordering, use `transaction_index`. Do not treat `block_timestamp` as precise sub-second timing.

4. **USD pricing**: On-chain data is in token units. USD conversion depends on the price oracle used. Check whether your data provider uses DEX spot prices, Chainlink oracles, or CoinGecko. Discrepancies can be material during high volatility.

5. **Chain-specific quirks**:
   - Ethereum: EIP-1559 changed gas fee structure (base fee + priority fee)
   - L2s (Arbitrum, Optimism): Transaction ordering may differ from L1
   - Solana: Account model differs from EVM; different data schemas

## Natural Experiments in DeFi

DeFi is rich with natural experiments because protocol governance creates exogenous policy changes:

- **Fee changes**: Uniswap governance proposals changing fee tiers
- **Parameter updates**: Aave risk parameter changes (LTV, liquidation thresholds)
- **Protocol launches**: New protocols creating sudden competition
- **Exploits/hacks**: Exogenous shocks to trust and TVL
- **Regulatory events**: SEC enforcement actions, OFAC sanctions (Tornado Cash)
- **Token airdrops**: Wealth shocks with arguably exogenous timing
- **Gas price spikes**: Exogenous transaction cost variation (network congestion events)
- **Bridge failures**: Cross-chain bridge exploits as exogenous liquidity shocks

These provide identification strategies (DiD, RDD, event studies) that are often more credible than in traditional finance settings because the policy changes are transparent, timestamped, and immutable.
