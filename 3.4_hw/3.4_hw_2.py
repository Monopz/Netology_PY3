# Вы собираетесь отправиться в путешествие и начинаете разрабатывать маршрут и выписывать цены на перелеты. Даны цены на билеты в местных валютах (файл currencies.txt). Формат данных в файле:

# <откуда куда>: <стоимость билета> <код валюты>
#Пример: MOSCOW-LONDON: 120 EUR

#Посчитайте, сколько вы потратите на путешествие денег в рублях (без копеек, округлить в большую сторону).

import osa
import re

URL = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
client = osa.client.Client(URL)

def read_curr():
    with    open('currencies.txt') as file_cost:
        for line in file_cost.readlines():
            departure, landing, cost, curr = (re.split('[ :-]+', line.strip()))
            yield cost, curr

def convert_to_rub(cost, curr):
    available_currencies = client.service.Currencies().split(';')
    response = client.service.ConvertToNum(fromCurrency=curr,toCurrency='RUB', amount = cost, rounding=True)

    print('Стоимость билетов состоит {} рублей'.format(int(response)))
    return

convert_to_rub()

price = sum(convert_to_rub(cost, curr)
    for cost, curr in read_curr())

print(price)
