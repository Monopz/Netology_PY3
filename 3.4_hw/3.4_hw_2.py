# Вы собираетесь отправиться в путешествие и начинаете разрабатывать маршрут и выписывать цены на перелеты. Даны цены на билеты в местных валютах (файл currencies.txt). Формат данных в файле:

# <откуда куда>: <стоимость билета> <код валюты>
#Пример: MOSCOW-LONDON: 120 EUR

#Посчитайте, сколько вы потратите на путешествие денег в рублях (без копеек, округлить в большую сторону).

import osa
import re

URL = 'http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL'
client = osa.client.Client(URL)

file_path = 'currencies.txt'

def get_currency_cost(file_1):
    with open(file_1) as file_cost:
        for value in file_cost.readlines():
            dep, ar, cost, currency = re.split('[ :-]+', value.strip())
            yield cost, currency

def currency_exchange(cost, currency):
    available_currencies = client.service.Currencies().split(';')
    cost_in_rubles = client.service.ConvertToNum(fromCurrency=currency, toCurrency='RUB', amount=cost, rounding=True)
    return float(cost_in_rubles)

flight_cost_in_rubles = sum(
    currency_exchange(cost, currency)
    for cost, currency in get_currency_cost(file_path)
)

print('Цена всех билетов: ', int(flight_cost_in_rubles), 'руб')
