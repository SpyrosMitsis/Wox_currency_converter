import requests

url = "https://currency-exchange.p.rapidapi.com/exchange"

querystring = {"from":"eur","to":"usd","q":"1.0"}

headers = {
    'x-rapidapi-key': "f68436e819mshabf74cd59d589ccp145898jsnbfa75c621668",
    'x-rapidapi-host': "currency-exchange.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
