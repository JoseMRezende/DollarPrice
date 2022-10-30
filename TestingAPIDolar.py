import json

import requests

price = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
price =price.json()
price_dollar = price['USDBRL']["bid"]
print(price_dollar)