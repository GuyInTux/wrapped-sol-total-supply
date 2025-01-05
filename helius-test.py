# Run at 2.25pm, 1/1/2025, ran 7 minutes
# 2nd run 2.41pm, 7 minutes
import requests

API_KEY = '9b0fdbd9-aa29-4bbb-a01e-8e603f7d8392'
HELIUS_RPC_URL = f"https://mainnet.helius-rpc.com/?api-key={API_KEY}"
# MINT_ADDRESS = "So11111111111111111111111111111111111111112"
MINT_ADDRESS = "jtojtomepa8beP8AuQc6eXt5FriJwfFMwQx2v2f9mCL"
TOKEN_PROGRAM_ID = "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"
TOKEN_DECIMALS = 9

def get_program_accounts():
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
    
    response = requests.post(HELIUS_RPC_URL, json=payload)
    return response.json()

response = get_program_accounts()
if 'result' in response:
    accounts = response['result']
    def calculate_total_lamports(accounts):
        total_lamports = 0
        for account in accounts:
            total_lamports += account['account']['lamports']
        return total_lamports

    total_lamports = calculate_total_lamports(accounts)
    wsol_total_supply = total_lamports / (10**TOKEN_DECIMALS)

    print(f"Wrapped SOL Total Supply: {wsol_total_supply}")
else:
    print("Error: ", response)