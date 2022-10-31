import json

import requests

price = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
price = price.json()
price_dollar = price['USDBRL']["bid"]
price_Euro = price['EURBRL']["bid"]
price_BTC = price['BTCBRL']["bid"]

dollar = float(price_dollar)
item1 = round(dollar,2)

Euro = float(price_Euro)
item2 = round(Euro,2)

Btc = float(price_BTC)
item3 = round(Btc,2)

print( "Dollar: ","R$:",item1)
print( "Euro: ","R$:",item2)
print( "Bitcoin: ","R$:",item3)