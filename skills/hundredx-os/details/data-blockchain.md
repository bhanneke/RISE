# Blockchain Data: Flipside and Allium SQL Patterns

## Purpose

This skill covers SQL patterns for querying blockchain data through Flipside Crypto
and Allium analytics platforms. Both provide structured, indexed blockchain data
accessible via SQL, but with different schemas, naming conventions, and capabilities.

---

## Common Table Structures

Blockchain data is organized around a set of core tables that appear across most
EVM-compatible chains and many non-EVM chains.

### Blocks

| Column | Description |
|--------|-------------|
| block_number | Sequential integer block identifier |
| block_timestamp | UTC timestamp of block production |
| block_hash | Unique hash of the block |
| miner / validator | Address that produced the block |
| gas_used | Total gas consumed in the block |
| gas_limit | Maximum gas allowed in the block |
| base_fee_per_gas | EIP-1559 base fee (post-London) |
| transaction_count | Number of transactions in the block |

### Transactions

| Column | Description |
|--------|-------------|
| tx_hash | Unique transaction hash |
| block_number | Block containing the transaction |
| block_timestamp | Timestamp of the containing block |
| from_address | Sender address |
| to_address | Recipient address (null for contract creation) |
| value | Native token value transferred (in wei/raw units) |
| gas_price | Gas price paid |
| gas_used | Gas consumed by the transaction |
| input_data | Encoded function call data |
| status | Success (1) or failure (0) |
| nonce | Sender's transaction sequence number |

### Events / Logs

| Column | Description |
|--------|-------------|
| tx_hash | Transaction that emitted the event |
| log_index | Position of the log within the transaction |
| contract_address | Address of the emitting contract |
| event_name | Decoded event name (if ABI is known) |
| topic0 | Event signature hash |
| topic1, topic2, topic3 | Indexed event parameters |
| data | Non-indexed event parameters (encoded) |
| decoded_log | Parsed event data (platform-specific format) |

### Token Balances / Transfers

| Column | Description |
|--------|-------------|
| from_address | Sender of the token transfer |
| to_address | Recipient of the token transfer |
| contract_address | Token contract address |
| amount / raw_amount | Transfer amount (raw or adjusted) |
| token_address | Same as contract_address in some schemas |
| symbol | Token symbol (e.g., USDC, WETH) |
| decimals | Token decimal places for conversion |

---

## SQL Patterns for DeFi Analysis

### Total Value Locked (TVL)

Track deposited assets in a protocol over time:

```sql
-- Daily TVL for a lending protocol (e.g., Aave-style)
WITH deposits AS (
    SELECT
        block_timestamp::date AS dt,
        SUM(CASE
            WHEN event_name = 'Deposit' THEN amount_usd
            WHEN event_name = 'Withdraw' THEN -amount_usd
            ELSE 0
        END) AS net_flow
    FROM protocol_events
    WHERE contract_address IN (/* pool addresses */)
    GROUP BY 1
)
SELECT
    dt,
    SUM(net_flow) OVER (ORDER BY dt) AS cumulative_tvl
FROM deposits
ORDER BY dt;
```

### Trading Volume

Aggregate DEX swap volume:

```sql
-- Daily swap volume on a Uniswap-style AMM
SELECT
    block_timestamp::date AS dt,
    pool_address,
    SUM(ABS(amount0_usd)) AS volume_usd,
    COUNT(*) AS swap_count
FROM dex_swaps
WHERE platform = 'uniswap-v3'
    AND block_timestamp >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY 1, 2
ORDER BY 1, 4 DESC;
```

### Yield / APY Calculation

Calculate realized yields from on-chain data:

```sql
-- Weekly yield for a staking protocol
WITH weekly_rewards AS (
    SELECT
        DATE_TRUNC('week', block_timestamp) AS week,
        SUM(reward_amount * token_price) AS rewards_usd,
        AVG(staked_amount * token_price) AS avg_tvl_usd
    FROM staking_events
    WHERE block_timestamp >= CURRENT_DATE - INTERVAL '90 days'
    GROUP BY 1
)
SELECT
    week,
    rewards_usd,
    avg_tvl_usd,
    (rewards_usd / NULLIF(avg_tvl_usd, 0)) * 52 AS annualized_apy
FROM weekly_rewards
ORDER BY week;
```

---

## SQL Patterns for On-Chain Governance

### Proposal Tracking

```sql
-- Governance proposals and their outcomes
SELECT
    proposal_id,
    proposer,
    description,
    start_block,
    end_block,
    for_votes / POWER(10, 18) AS for_votes,
    against_votes / POWER(10, 18) AS against_votes,
    CASE
        WHEN for_votes > against_votes AND quorum_reached THEN 'Passed'
        WHEN for_votes <= against_votes THEN 'Defeated'
        ELSE 'No Quorum'
    END AS outcome
FROM governance_proposals
ORDER BY start_block DESC;
```

### Voter Participation

```sql
-- Voter participation rates and delegation patterns
WITH votes AS (
    SELECT
        proposal_id,
        voter,
        voting_power / POWER(10, 18) AS voting_power,
        support  -- 0 = against, 1 = for, 2 = abstain
    FROM governance_votes
),
totals AS (
    SELECT
        proposal_id,
        COUNT(DISTINCT voter) AS unique_voters,
        SUM(voting_power) AS total_power_voted,
        SUM(CASE WHEN support = 1 THEN voting_power ELSE 0 END) AS for_power,
        SUM(CASE WHEN support = 0 THEN voting_power ELSE 0 END) AS against_power
    FROM votes
    GROUP BY 1
)
SELECT
    t.proposal_id,
    t.unique_voters,
    t.total_power_voted,
    t.total_power_voted / NULLIF(s.total_supply, 0) AS participation_rate,
    t.for_power / NULLIF(t.total_power_voted, 0) AS approval_rate
FROM totals t
LEFT JOIN token_supply s ON s.token_address = '0x...'
ORDER BY t.proposal_id DESC;
```

---

## Flipside-Specific Schemas and Conventions

Flipside organizes data by chain under a `<chain>.core` or `<chain>.defi` schema.

### Schema structure

```
ethereum.core.fact_transactions
ethereum.core.fact_event_logs
ethereum.core.dim_labels          -- address labels
ethereum.core.ez_token_transfers  -- simplified token transfer view
ethereum.defi.ez_dex_swaps        -- decoded DEX swaps
ethereum.defi.ez_lending_borrows  -- decoded lending events
ethereum.price.ez_prices_hourly   -- token prices

-- Same pattern for other chains:
polygon.core.fact_transactions
arbitrum.core.fact_event_logs
optimism.defi.ez_dex_swaps
solana.core.fact_transactions
```

### Flipside naming conventions

- `fact_` prefix: raw fact tables (immutable event records)
- `dim_` prefix: dimension tables (labels, metadata)
- `ez_` prefix: convenience views with decoded and enriched data
- Column names use snake_case
- Timestamps are in UTC
- Token amounts in `ez_` views are typically already decimal-adjusted
- Raw amounts in `fact_` tables require division by `POWER(10, decimals)`

### Flipside-specific patterns

```sql
-- Using Flipside's ez_ tables for quick analysis
SELECT
    block_timestamp::date AS dt,
    platform,
    SUM(amount_in_usd) AS volume_usd
FROM ethereum.defi.ez_dex_swaps
WHERE block_timestamp >= CURRENT_DATE - INTERVAL '7 days'
GROUP BY 1, 2
ORDER BY 1, 3 DESC;

-- Address labeling with dim_labels
SELECT
    t.from_address,
    l.label,
    l.label_type,
    COUNT(*) AS tx_count
FROM ethereum.core.fact_transactions t
LEFT JOIN ethereum.core.dim_labels l
    ON t.from_address = l.address
WHERE t.block_timestamp >= CURRENT_DATE - INTERVAL '1 day'
GROUP BY 1, 2, 3
ORDER BY 4 DESC
LIMIT 20;
```

---

## Allium-Specific Schemas and Conventions

Allium uses a `<chain>.raw` and `<chain>.assets` schema pattern with some differences
from Flipside.

### Schema structure

```
ethereum.raw.blocks
ethereum.raw.transactions
ethereum.raw.logs
ethereum.raw.traces
ethereum.assets.erc20_transfer
ethereum.assets.erc721_transfer
ethereum.dex.trades
ethereum.lending.events

-- Cross-chain unified tables:
cross_chain.address_labels
cross_chain.token_metadata
```

### Allium naming conventions

- `raw.` schema: minimally processed blockchain data
- `assets.` schema: token transfer events (ERC20, ERC721, ERC1155)
- `dex.` schema: decoded DEX trade events
- `lending.` schema: decoded lending protocol events
- Column names use snake_case
- Timestamps are `block_timestamp` in UTC
- Raw amounts require decimal adjustment using `token_metadata`
- Allium provides `unique_id` columns for deduplication

### Allium-specific patterns

```sql
-- Using Allium's unified cross-chain structure
SELECT
    chain,
    block_timestamp::date AS dt,
    COUNT(*) AS transfer_count,
    COUNT(DISTINCT from_address) AS unique_senders
FROM ethereum.assets.erc20_transfer
WHERE token_address = LOWER('0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48')  -- USDC
    AND block_timestamp >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY 1, 2
ORDER BY 2;

-- Trace-level analysis (Allium provides full trace data)
SELECT
    tx_hash,
    trace_address,
    from_address,
    to_address,
    value / POWER(10, 18) AS eth_value,
    call_type
FROM ethereum.raw.traces
WHERE block_number = 18000000
    AND status = 1
ORDER BY trace_address;
```

---

## Best Practices

### Time-series aggregation

- Always use `DATE_TRUNC` or `::date` for consistent time bucketing.
- Specify timezone explicitly when it matters: `AT TIME ZONE 'UTC'`.
- For hourly data, use `DATE_TRUNC('hour', block_timestamp)`.
- Fill gaps in time series with a date spine to avoid misleading charts:

```sql
WITH date_spine AS (
    SELECT generate_series(
        '2024-01-01'::date,
        CURRENT_DATE,
        '1 day'::interval
    )::date AS dt
),
daily_data AS (
    SELECT block_timestamp::date AS dt, SUM(amount_usd) AS volume
    FROM dex_swaps
    GROUP BY 1
)
SELECT
    s.dt,
    COALESCE(d.volume, 0) AS volume
FROM date_spine s
LEFT JOIN daily_data d ON s.dt = d.dt
ORDER BY s.dt;
```

### Address filtering

- Always lowercase addresses for comparison: `LOWER(address)`.
- Use `IN` clauses for multiple known addresses rather than multiple ORs.
- For contract vs. EOA distinction, check the `to_address` of creation transactions
  or use platform-provided labels.
- Be aware of proxy contracts: the address you interact with may differ from the
  implementation address.

### Token decimals

- Never display raw token amounts without decimal adjustment.
- Standard decimals: ETH/WETH = 18, USDC/USDT = 6, WBTC = 8, DAI = 18.
- Always join with token metadata to get the correct decimals:

```sql
SELECT
    t.from_address,
    t.to_address,
    t.raw_amount / POWER(10, m.decimals) AS amount,
    m.symbol,
    (t.raw_amount / POWER(10, m.decimals)) * p.price AS amount_usd
FROM token_transfers t
JOIN token_metadata m ON t.token_address = m.address
LEFT JOIN token_prices p ON t.token_address = p.token_address
    AND DATE_TRUNC('hour', t.block_timestamp) = p.hour
```

### Performance tips

- Filter on `block_timestamp` or `block_number` early -- these columns are typically
  partitioned and indexed.
- Avoid `SELECT *` on large tables; specify only needed columns.
- Use `LIMIT` during development to avoid scanning entire tables.
- For large aggregations, consider materializing intermediate results with CTEs
  rather than deeply nested subqueries.
- When joining large tables, ensure join keys are indexed (they usually are for
  `tx_hash`, `block_number`, `address` columns).
