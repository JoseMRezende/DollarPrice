import datetime
import json

import PySimpleGUI as sg
import requests

dt = datetime.datetime.now()
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
font = ("Arial", 12)
sg.theme('DarkBlue')
layout = [  [sg.Text('Price of Dollar:', size=(200, 1), key='-text-', font=font)],
            [sg.Text(item1,size=(200, 1), key='-text-', font=font)],    # type: ignore
            [sg.Text('Price of Euro:', size=(200, 1), key='-text-', font=font)],
            [sg.Text(item2,size=(200, 1), key='-text-', font=font)],    # type: ignore
            [sg.Text('Price of Coin:', size=(200, 1), key='-text-', font=font)],
            [sg.Text(item3,size=(200, 1), key='-text-', font=font)],    # type: ignore
            [sg.Button('Close',size=(200, 1), key='-text-', font=font,button_color = 'Yellow')],
            [sg.Text(dt,size=(200, 1), key='-text-')] ] # type: ignore 
window = sg.Window('Quote Table', layout,size=(300, 240), element_justification='center')
while True:
    event, values = window.read()  # type: ignore
    if event == sg.WIN_CLOSED or event == 'Close':
        break
    print("Closed")
    window.close()