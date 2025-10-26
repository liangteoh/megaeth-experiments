import requests

def get_latest_block():
    response = requests.get("https://rpc.ankr.com/eth")
    if response.status_code == 200:
        print("Ethereum RPC connected successfully!")
    else:
        print("Failed to connect to Ethereum RPC.")

if __name__ == "__main__":
    get_latest_block()
