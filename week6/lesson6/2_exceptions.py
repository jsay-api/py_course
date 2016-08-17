# ошибки бывают 2 типов: ошибки синтаксиса и исключения

# while True print('Hello world')
# вызовет:
# SyntaxError: invalid syntax

# Если выражение синтаксически корректно, то ошибка может возникнуть во
# время выполнения. Такие ошибки называются "исключениями".

# >>> 10 * (1/0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in ?
# ZeroDivisionError: int division or modulo by zero
# >>> 4 + spam*3
# Traceback (most recent call last):
#   File "<stdin>", line 1, in ?
# NameError: name 'spam' is not defined
# >>> '2' + 2
# Traceback (most recent call last):
#   File "<stdin>", line 1, in ?
# TypeError: Can't convert 'int' object to str implicitly

# Ввод данных пользователем

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

# 


# В конструкции try может быть несколько except
import sys

# Создадим файл
f = open('myfile.txt', 'w')
f.write('111')
f.close()

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as err:
    print("I/O error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


# В конструкции try/except может присутствовать else
# Инструкции из else выполняются, если не возникло исключения

filename = 'somefile.txt'

# создадим файл
f = open(filename, 'w')
f.write('111\n222\n333')
f.close()

try:
    f = open(filename, 'r')
except IOError:
    print('cannot open', filename)
else:
    print(filename, 'has', len(f.readlines()), 'lines')
    f.close()


# При самостоятельном возбуждении исключений можно использовать переменные:

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # <class 'Exception'>
    print(inst.args)     # аргументы хранятся в .args
    print(inst)          # __str__ выводит .args
    x, y = inst.args     # распаковываем аргументы
    print('x =', x)
    print('y =', y)


# Создание собственных исключений
# Ислючения должны наследоваться от класса Exception или его потомков

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)


# Инструкция finally всегда выполняется при выходе из блока try, 
# не смотря на то, было исключение или нет.

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
divide(2, 1)
# result is 2.0
# executing finally clause
# divide(2, 0)
# division by zero!
# executing finally clause
# divide("2", "1")

# В реальных приложениях инструкцию finally удобно применять для освобождения
# ресурсов (таких как соединения по сети), не смотря на то, было ли успешным
# их использование или нет.


# Документация по встроенным исключениям:
# http://docs.python.org/3/library/exceptions.html#bltin-exceptions

