import requests
def get_tether_value():
    """
    gets the value of tether from the api
    """
    url = "https://api.coincap.io/v2/assets/tether"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload) #api request
    return response.json()["data"]["priceUsd"] #extracts the value of tether from the json response
