#coding: utf-8
__author__='julia sayapina'

""" Яндекс.Погода

Есть публичный урл со списком городов:
http://weather.yandex.ru/static/cities.xml

Для этих городов можно получить данные о погоде, подставив id города в шаблон:
http://export.yandex.ru/weather-ng/forecasts/<id города>.xml

Необходимо написать скрипт, который:
1. Создает файл базы данных SQLite со следующей структурой данных (если файла 
   базы данных не существует):

    Погода
        id                  INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура днем    INTEGER
        Температура ночью   INTEGER

2. Скачивает и парсит XML со списком городов
3. Выводит список стран из файла и предлагает пользователю выбрать страну
4. Скачивает XML файлы погоды в городах выбранной страны
5. Парсит последовательно каждый из файлов и добавляет данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


Температура днем и температура ночью берется из 
forecast/day/day_part@day_short/temperature и 
forecast/day/day_part@night_short/temperature соответственно:

<forecast ...>
    <day date="...">
        <day_part typeid="5" type="day_short">
            <temperature>29</temperature> 
            ...
        </day_part>
        <day_part typeid="6" type="night_short">
            <temperature>18</temperature>
            ...
        </day_part>
    </day>
</forecast>

При повторном запуске скрипта:
- используется уже скачанный файл с городами
- используется созданная база данных, новые данные добавляются и обновляются

Важное примечание:

Доступ к данным в XML файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с простанствами имен, удобно пользоваться такими функциями:

# Получим пространство имен из первого тега:
def gen_ns(tag):
    if tag.startswith('{'):
        ns, tag = tag.split('}')
        return ns[1:]
    else:
        return ''

tree = ET.parse(f)
root = tree.getroot()

# Определим словарь с namespace
namespaces = {'ns': gen_ns(root.tag)}

# Ищем по дереву тегов
for day in root.iterfind('ns:day', namespaces=namespaces):
    ...

"""

import os
import sqlite3
import urllib.request
import shutil
import codecs
import lxml
from xml.etree import ElementTree as ET
from collections import OrderedDict, namedtuple

db_filename = 'weather.db'


# Создание или открытие файла базы данных и создание схемы

try:
    with sqlite3.connect(db_filename) as conn:
        c = conn.cursor()
        c.execute("""
            create table if not exists Weather  (
                id                  INTEGER PRIMARY KEY autoincrement,
                Town                VARCHAR(255),
                Date                DATE,
                Day_temperature     INTEGER,
                Night_temperature   INTEGER
        );
        """)
        c.execute('create unique index if not exists town_date on Weather(Town, Date)')

except Exception as e:
    print ("Exception 0:", type(e), e)

def download_file(url, filename, aswhat):
    success_flag = False
    while success_flag == False:
        try:
            with urllib.request.urlopen(url) as response, open(filename, 'wb') as aswhat:
                shutil.copyfileobj(response, aswhat)
                success_flag = True
        except Exception as e:
            print ("Exception 1:", type(e), e)
            success_flag = False


def db_insert(town, date, day_temp, night_temp):    #добавляет или апдейтит значения в БД
    with conn:
        try:
        #c.execute('''UPDATE Weather 
            #SET Day_temperature = ? AND Night_temperature = ?
            #WHERE EXISTS (SELECT * FROM Weather WHERE Town = ? AND Date = ?''', (day_temp, night_temp, town, date))
            conn.execute('INSERT OR REPLACE INTO Weather (Town, Date, Day_temperature, Night_temperature) VALUES (?,?,?,?)', (town, date, day_temp, night_temp))
            conn.commit()
        except Exception as e:
            print ("Exception 2:", type(e), e)

        

download_file('https://pogoda.yandex.ru/static/cities.xml', 'cities.xml', 'f')
# Получим пространство имен из первого тега:
def gen_ns(tag):
    if tag.startswith('{'):
        ns, tag = tag.split('}') 
        return ns[1:]
    else:
        return ''

countries = []
with codecs.open('cities.xml', 'r', encoding = 'utf-8') as f:    #парсим и получаем дерево стран
    tree = ET.parse(f)
    root = tree.getroot()
    for country in root.iterfind('country'):    #получаем список стран
        print (country.get('name'))
        countries.append(country.get('name'))
    user_country = input('Choose the country and type it in:')
    if user_country not in countries: 
        raise ValueError('Invalid Country')
    for town in root.findall('.//*[@country="%s"]' % user_country):
        town_id = town.get('id')    #получаем id городов страны пользователя
        town_name = town.text   #название города
        path = 'http://export.yandex.ru/weather-ng/forecasts/' + town_id + '.xml'   #путь, откуда скачивать xml для каждого города
        fname = town_id + '.xml'    #название файла, куда загружать xml города
        if not os.path.isfile(fname): 
            download_file(path, fname, 't')
            print ('file %s downloaded' % fname)
        with codecs.open(fname, 'r', encoding = 'utf-8') as t:
            town_tree = ET.parse(t)
            town_root = town_tree.getroot() #парсим и получаем дерево города
            # Определим словарь с namespace
            namespaces = {'ns': gen_ns(town_root.tag)}
            # Ищем даты по дереву тегов
            for day in town_root.iterfind('ns:day', namespaces):
                date = (day.get('date'))
                day_temp = day.find('.//*[@type="day_short"]/ns:temperature', namespaces).text  #ищем температуры за каждую дату
                night_temp = day.find('.//*[@type="night_short"]/ns:temperature', namespaces).text
                #print (town_name, date, day_temp, night_temp)
                db_insert(town_name, date, day_temp, night_temp) 
#надо ли куда-нибудь классы прикрутить??

conn.close()
