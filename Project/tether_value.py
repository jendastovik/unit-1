import requests
def get_tether_value():
    url = "https://api.coincap.io/v2/assets/tether"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()["data"]["priceUsd"]
