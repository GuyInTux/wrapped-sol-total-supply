import requests

RPC_URL = "https://api.mainnet-beta.solana.com"
MINT_ADDRESS = "So11111111111111111111111111111111111111112"
TOKEN_PROGRAM_ID = "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"

def get_program_accounts():
    headers = {
        "Content-Type": "application/json"
    }
    
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getProgramAccounts",
        "params": [
            TOKEN_PROGRAM_ID,
            {
                "filters": [
                    {"dataSize": 165},
                    {"memcmp": {"offset": 0, "bytes": MINT_ADDRESS}}
                ],
                "encoding": "jsonParsed"
            }
        ]
    }
    
    response = requests.post(RPC_URL, json=payload, headers=headers)
    return response.json()

def calculate_total_lamports(accounts):
    total_lamports = 0
    for account in accounts:
        total_lamports += account['account']['lamports']
    return total_lamports

response = get_program_accounts()
accounts = response['result']
total_lamports = calculate_total_lamports(accounts)
total_sol = total_lamports / 10**9

print(f"Total Supply for Wrapped SOL: {total_sol} wSOL")
