# Задача №1

# Дано: семь значений температур по Фаренгейту в файле temps.txt. Необходимо вывести среднюю за неделю арифметическую температуру по Цельсию.

import osa
import re

def convert_temperature():
    # выводим среднюю температуру за неделю в цельсиях
    URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
    client = osa.client.Client(URL)

    with open('temps.txt', 'r') as text:
        temp = [
        int(line.split()[0]) for line in text.readlines()
        ]
        average_temp = sum(temp) / len(temp)

        response = client.service.ConvertTemp(Temperature=average_temp, FromUnit='degreeFahrenheit', ToUnit='degreeCelsius')

        return print('Средняя температура за неделю {} градусов по цельсию.'.format(int(response)))

convert_temperature()
