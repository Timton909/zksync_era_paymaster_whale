import requests, time

def paymaster_whale():
    print("zkSync Era — Paymaster Whale Activated (> 100 ETH paid for others)")
    seen = set()
    while True:
        r = requests.get("https://block-explorer-api.zksync.io/transactions?limit=40&page=1")
        for tx in r.json().get("items", []):
            h = tx["hash"]
            if h in seen: continue
            seen.add(h)

            # Paymaster paid the fee for someone else
            if not tx.get("paymaster"): continue
            fee = int(tx.get("fee", "0"), 16) / 1e18

            if fee >= 100:  # paymaster covered ≥ 100 ETH in gas for a stranger
                user = tx["from"]
                paymaster = tx["paymaster"]
                print(f"PAYMASTER WHALE JUST PAID\n"
                      f"{fee:.2f} ETH gas covered for user\n"
                      f"User:      {user[:12]}...\n"
                      f"Paymaster: {paymaster[:12]}...\n"
                      f"Tx: https://explorer.zksync.io/tx/{h}\n"
                      f"→ Someone just gave away $300k+ in gas for free\n"
                      f"→ Usually exchange onboarding, airdrop, or silent god move\n"
                      f"{'-'*90}")
        time.sleep(2.1)

if __name__ == "__main__":
    paymaster_whale()
