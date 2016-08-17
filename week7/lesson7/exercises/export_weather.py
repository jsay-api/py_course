#coding: utf-8
__author__='julia sayapina'

""" Яндекс.Погода (экспорт)

Сделать скрипт, экспортирующий данные из базы данных погоды, 
созданной скриптом weather.py. Экспорт происходит в формате CSV или JSON.

Скрипт запускается из коммандной строки и получает на входе:
export_weather.py --csv filename [<город>]
export_weather.py --json filename [<город>]

Экспорт происходит в файл filename.
Опционально можно задать в командной строке город. В этом случае 
экспортируются только данные по указанному городу. Если города нет в базе,
выводится соответствующее сообщение.


"""

import csv
import json
import sqlite3
import os
import sys 

csv.register_dialect('excel-semicolon', delimiter=';')
#f = open('weather.csv', 'rt')

def db_data(town): 
	data = None
	if town != None and (c.execute("SELECT * FROM Weather WHERE Town = ?", (town)))!= None:
		data = c.execute("SELECT * FROM Weather WHERE Town = ?", (town))	#выбираем все строки с городом, если задан
	else:
		data = c.execute("SELECT * FROM Weather")	#выбираем все, если город не задан
		print ('all data')
	return data

try:
    with sqlite3.connect('weather.db') as conn:
        c = conn.cursor()
        db_data(town)
except Exception as e:
    print ("DB Exception:", type(e), e)


def csv_export():
	with open('weather.csv', 'w', encoding='utf-8') as csvfile:
	    writer = csv.writer(csvfile, dialect='excel-semicolon')
	    writer.writerow( ('Town', 'Date', 'Day Temperature', 'Night Temperature') ) #пишем в csv выбранные из бд данные
	    print (town, data)
	    #writer.writerows(data)

def json_export():
	with open('weather.json', 'a', encoding='utf-8') as jsonfile:
		json_string = json.dumps(data)	#выбранные из бд данные конвертируем в json и пишем в файл
		jsonfile.write(json_string)





conn.close()

def main():
    if len(sys.argv) != 3:
        print('usage: python3 export_weather.py {--csv | --json} [town]')
        sys.exit(1)

    option = sys.argv[1]
    if len(sys.argv) == 3: 
    	town = sys.argv[2]
    else:
    	town = None
    print (town)
    if option == '--csv':
        csv_export()
    elif option == '--json':
        json_export()
    else:
        print('unknown option: ' + option)
    return town
    sys.exit(1)

if __name__ == '__main__':
    main()
