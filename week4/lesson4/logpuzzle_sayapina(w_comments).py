#!/usr/bin/python3
#coding: utf-8
__author__='julia sayapina'

import os
import re
import sys
import urllib
import codecs

""" Logpuzzle
На сервере лежит 9 изображений, являющихся частями одного изображения 
(фото дикой природы).

Дан лог файл веб-сервера, в котором среди прочих запросов содеражатся запросы
к этим изображениям. Нужно вытащить из файла url всех изображений и скачать их.
Затем создать файл index.html и собрать с его помощью все изображения в одну
картинку.

Вот что из себя представляет строка лога:
101.237.66.11 - - [05/Jun/2013:10:44:02 +0400] "GET /images/animals_07.jpg HTTP/1.1" 200 13632 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"

Замечание: для создания html файла можно использовать самую простую разметку:
<html>
<body>
<img src="img0.jpg"><img src="img1.jpg">...
</body>
</html>

Подсказка: скачать файлы можно двумя способами:

1. Воспользоваться функцией, сохраняющей url по заданному пути file_name:
urllib.request.urlretrieve(url, file_name)

2. Скачать url и сохранить в файле:
import urllib.request
import shutil
...
with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

"""


def read_urls(filename):        # 2016.04.11_03:40:57 checked. prusanov
    """ 
    Возвращает список url изображений из данного лог файла,
    извлекая имя хоста из имени файла (apple-cat.ru_access.log). Вычищает
    дубликаты и возвращает список url, отсортированный по названию изображения.
    """
    img_urls = []
    if os.path.isfile(filename):            # можно еще:   if os.path.exists(filename)
        log = codecs.open(filename, encoding = 'utf-8').read()
    else:
        print 'Error 404: file not found. Choose another file'
        sys.exit(1)
    
    res = re.findall(r'\s/images/(animals.*?jpg)', log, re.DOTALL)
    for i in res:
        if i not in img_urls: 
            img_urls.append(i)
    img_urls = sorted(img_urls)
    return img_urls
  

def download_images(img_urls, dest_dir):    # 2016.04.11_03:42:39 checked. prusanov
    """
    Получает уже отсортированный спискок url, скачивает каждое изображение
    в директорию dest_dir. Переименовывает изображения в img0.jpg, img1.jpg и тд.
    Создает файл index.html в заданной директории с тегами img, чтобы 
    отобразить картинку в сборе. Создает директорию, если это необходимо.
    """
    # +++ваш код+++
    dest_dir = raw_input("Input the destination directory")
    pics = open('index.html', 'a+')         # имеет смысл открывать файл в режиме "w", иначе можно очень много лишнего надозаписывать
    pics.write('''<html>
<body>
''')
    if os.path.exists(dest_dir) == False: os.mkdir(dest_dir)            # 1. все же, читаемей - на разных строках
                                                                        # 2. не надо сравнивать с False (PEP-8):  if not os.path.exists(dest_dir)
    for i in img_urls:
        # urllib.urlretrieve('http://www.apple-cat.ru/images/'+i, dest_dir + '/' + i)
        pics.write('<img src="' + os.path.abspath(dest_dir + '/' + i) + '">')       # на счет abspath - сомнения. Лучше, все же, относительный путь. 
                                                                                    # Не всегда картинки могут подхватиться.
                                                                                    # Или же дополнительно в src перед полным путем указывать приставку file://
    pics.write('''
        </body>
</html>''')

    

  

def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))

if __name__ == '__main__':
    main()
