#!/usr/bin/python2
#coding: utf-8
#__author__='julia sayapina'

"""Упражнение "Количество слов"

Функция main() ниже уже определена и заполнена. Она вызывает функции 
print_words() и print_top(), которые вам нужно заполнить.

1. Если при вызове файла задан флаг --count, вызывается функция 
print_words(filename), которая подсчитывает, как часто каждое слово встречается 
в тексте и выводит:
слово1 количество1
слово2 количество2
...

Выводимый список отсортируйте в алфавитном порядке. Храните все слова 
в нижнем регистре, т.о. слова "Слон" и "слон" будут обрабатываться как одно 
слово.

2. Если задан флаг --topcount, вызывается функция print_top(filename),
которая аналогична функции print_words(), но выводит только топ-20 наиболее 
часто встречающихся слов, таким образом первым будет самое часто встречающееся 
слово, за ним следующее по частоте и т.д.

Используйте str.split() (без аргументов), чтобы разбить текст на слова.

Отсекайте знаки припинания при помощи str.strip() с знаками припинания 
в качестве аргумента.

Совет: не пишите всю программу сразу. Доведите ее до какого-то промежуточного 
состояния и выведите вашу текущую структуру данных. Когда все будет работать 
как надо, перейдите к следующему этапу.

Дополнительно: определите вспомогательную функцию, чтобы избежать дублирования 
кода внутри print_words() и print_top().

"""

import sys

# +++ваш код+++
# Определите и заполните функции print_words(filename) и print_top(filename).
# Вы также можете написать вспомогательную функцию, которая читает файл,
# строит по нему словарь слово/количество и возвращает этот словарь.
# Затем print_words() и print_top() смогут просто вызывать эту вспомогательную функцию.

words_dict = {}
def count_words(filename):
    f = open(filename).read().lower().translate(None, ".,()–!?/'#$@:;\"")
    print f.lower()
    words = f.split()
    words_set = set()
    for word in words:
        words_set.add(word)
    global words_dict
    words_dict = dict.fromkeys(words_set, 0)
    
    for word in words_dict:
        words_dict[word]=f.count(word, 0, len(f))
    return words_dict



def print_words(filename):
    count_words(filename)
    #print words_dict
    for k in sorted(words_dict):
        print k, words_dict[k]
    
    return words_dict

def print_top(filename):
    count_words(filename)
    i=0
    for k in sorted(words_dict, key=lambda k: words_dict[k], reverse=True):
        if i<20:
            print k, words_dict[k]
            i+=1
        
    return words_dict




###

# Это базовый код для разбора аргументов командной строки.
# Он вызывает print_words() и print_top(), которые необходимо определить.
def main():
    if len(sys.argv) != 3:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
    main()
