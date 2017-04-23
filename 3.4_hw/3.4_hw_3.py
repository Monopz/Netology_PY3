# Дано: длина пути в милях, название пути (файл travel.txt) в формате:
#
# <название пути>: <длина в пути> <мера расстояния>
# Пример:
# MOSCOW-LONDON: 1,553.86 mi
#
# Необходимо посчитать суммарное расстояние пути в километрах с точностью до сотых.

import re
import osa

URL ='http://www.webservicex.net/length.asmx?WSDL'
client = osa.client.Client(URL)
FILE_PATH = 'travel.txt'

def open_travel(FILE_PATH):
    with open(FILE_PATH) as travel:
        for arr in travel.readlines():
            b, c, distance, unit = (re.split('[ :-]+', arr.strip()))
            yield float(distance.replace(',', ''))

def convert_to_kilometers(miles):
    url = 'http://www.webservicex.net/length.asmx?WSDL'
    kilometers = client.service.ChangeLengthUnit(
        LengthValue=miles,
        fromLengthUnit='Miles',
        toLengthUnit='Kilometers'
    )
    return kilometers
final = convert_to_kilometers(sum(open_travel(FILE_PATH)))
print('Суммароное расстояние',round(final, 2), 'км')
