import requests

ADDRESS = "t1MkgrZASAJbtNzEagDtUbapFKiS7sNQihm"
API_BASE = "https://api.blockchair.com/zcash"

def fetch_address_data(address):
    url = f"{API_BASE}/dashboards/address/{address}"
    resp = requests.get(url, params={"transactions": "true"})
    resp.raise_for_status()
    return resp.json()

def display_info(data, address):
    info = data["data"][address]
    addr_data = info["address"]

    balance = addr_data.get("balance", 0) / 1e8
    total_received = addr_data.get("received", 0) / 1e8
    total_sent = addr_data.get("sent", 0) / 1e8  # Fix here

    print(f"Address: {address}")
    print(f"  Balance:        {balance:.8f} ZEC")
    print(f"  Total received: {total_received:.8f} ZEC")
    print(f"  Total sent:     {total_sent:.8f} ZEC")

    txs = info.get("transactions", [])
    print(f"\nLast {len(txs)} transactions:")
    for tx in txs[:10]:
        print(f"  • TXID: {tx}")
    if not txs:
        print("  (No recent transactions)")


if __name__ == "__main__":
    data = fetch_address_data(ADDRESS)
    display_info(data, ADDRESS)
