import datetime
import json
import time

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
layout = [  [sg.Text('Value Converted To Reais',font=font)],
            [sg.Text('Price of Dollar R$:',font=font),sg.Text(item1,size=(20, 1),key='-text-',font=font)],           # type: ignore
            [sg.Text('Price of Euro   R$:',font=font),sg.Text(item2,size=(20, 1),key='-text-',font=font)],           # type: ignore
            [sg.Text('Price of Coin   R$:',font=font),sg.Text(item3,size=(20, 1),key='-text-',font=font)],           # type: ignore
            [sg.Button('Close',size=(12, 1),font=font,button_color = 'Yellow'),sg.Button('Update',size=(12, 1),font=font,button_color = 'Blue')],
            [sg.Text(dt,size=(200, 1), key='-text-',justification='center')]  ]                                      # type: ignore 
window = sg.Window('Quote Table', layout,size=(300, 180), element_justification='center')                            # type: ignore
while True:
    event, values = window.read()  # type: ignore
    if event == sg.WIN_CLOSED or event == 'Close':
        print("Closed...")
        break
    if event == 'Update':
        window.close()
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
        print("")
        print("Update:")
        print( "Dollar: ","R$:",item1)
        print( "Euro: ","R$:",item2)
        print( "Bitcoin: ","R$:",item3)
        font = ("Arial", 12)
        sg.theme('DarkBlue')
        layout = [  [sg.Text('Value Converted To Reais',font=font)],
                    [sg.Text('Price of Dollar R$:',font=font),sg.Text(item1,size=(20, 1),key='-text-',font=font)],           # type: ignore
                    [sg.Text('Price of Euro   R$:',font=font),sg.Text(item2,size=(20, 1),key='-text-',font=font)],           # type: ignore
                    [sg.Text('Price of Coin   R$:',font=font),sg.Text(item3,size=(20, 1),key='-text-',font=font)],           # type: ignore
                    [sg.Button('Close',size=(12, 1),font=font,button_color = 'Yellow'),sg.Button('Update',size=(12, 1),font=font,button_color = 'Blue')],
                    [sg.Text(dt,size=(200, 1), key='-text-',justification='center')]  ]                                      # type: ignore 
        window = sg.Window('Quote Table', layout,size=(300, 180), element_justification='center')