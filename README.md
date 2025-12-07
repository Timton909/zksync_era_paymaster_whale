# zkSync Era — Paymaster Whale Tracker

Detects when a **paymaster covers ≥ 100 ETH** (~$300k+) in gas fees for another wallet in a single transaction.

On zkSync Era, paymasters can pay gas for users.  
Most pay 0.01 ETH.  
This script watches for gods who pay hundreds of ETH — for strangers.

## Run

```bash
python zksync_era_paymaster_whale.py
