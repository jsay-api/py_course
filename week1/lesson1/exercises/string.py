#!/usr/bin/python3
#coding: utf-8
#__author__='julia sayapina'
# Строки

# Заполните код преведенных ниже функций. Функция main() уже настроена
# для вызова функций с несколькими различными параметрами,
# и выводит 'OK' в случае, если вызов функции корректен.
# Начальный код каждой функции содержит 'return'
# и является просто заготовкой для вашего кода.


# A. Пончики
# Дано количество пончиков (целое число);
# Нужно вернуть строку следующего вида:
# 'Количество пончиков: <count>', где <count> это количество,
# переданное в функцию как параметр.
# Однако, если количество 10 и более - нужно использовать слово
# 'много', вместо текущего количества.
# Таким образом, donuts(5) вернет 'Количество пончиков: 5'
# а donuts(23) - 'Количество пончиков: много'
def donuts(count):
    # +++ ваш код +++
    if (count >=10): count = 'a lot'
    return "Q: %s" % count


# B. Оба конца
# Дана строка s. 
# Верните строку, состоящую из первых 2
# и последних 2 символов исходной строки.
# Таким образом, из строки 'spring' получится 'spng'. 
# Однако, если длина строки меньше, чем 2 -
# верните просто пустую строчку.
def both_ends(s):
    # +++ ваш код +++
    if (len(s)<2): s=''
    else: s=s[:2]+s[-2:]
    return s


# C. Кроме первого
# Дана строка s.
# Верните строку, в которой все вхождения ее первого символа
# заменены на '*', за исключением самого этого первого символа.
# Т.е., из 'babble' получится 'ba**le'.
# Предполагается, что длина строки 1 и более.
# Подсказка: s.replace(stra, strb) вернет версию строки, 
# в которой все вхождения stra будут заменены на strb.
def fix_start(s):
    # +++ ваш код +++
    if (len(s)>=1):
        i=s[0]
        s=i+s[1:].replace(i, "*")
    return s


# D. Перемешивание
# Даны строки a и b.
# Верните одну строку, в которой a и b отделены пробелом '<a> <b>', 
# и поменяйте местами первые 2 символа каждой строки.
# Т.е.:
#   'mix', 'pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Предполагается, что строки a и b имеют длину 2 и более символов.
def mix_up(a, b):    
    # +++ ваш код +++
    x=b[0:2]+a[2:]
    y=a[0:2]+b[2:]
    return x+" "+y


# E. Хорош
# Дана строка.
# Найдите первое вхождение подстрок 'не' и 'плох'.
# Если 'плох' идет после 'не' - замените всю подстроку
# 'не'...'плох' на 'хорош'.
# Верните получившуюся строку
# Т.о., 'Этот ужин не так уж плох!' вернет:
# Этот ужин хорош!
def not_bad(s):
    # +++ ваш код +++ 
    if ('not' in s and 'bad' in s):
        n1=s.find('not')
        n2=s.find('bad')
        if n1<n2: s=s[:n1]+"good"+s[(n2+3):]
    return s


# F. Две половины
# Рассмотрим разделение строки на две половины.
# Если длина четная - обе половины имеют одинаковую длину.
# Если длина нечетная — дополнительный символ присоединяется к первой половине.
# Т.е., 'abcde', первая половина 'abc', вторая - 'de'.
# Даны 2 строки, a и b, верните строку вида:
# 1-половина-a + 1-половина-b + 2-половина-a + 2-половина-b
def front_back(a, b):
    # +++ ваш код +++

    if (len(a)%2==0): ah1=a[:(len(a)//2)]; ah2=a[(len(a)//2):]
    else: ah1=a[:(len(a)//2+1)]; ah2=a[(len(a)//2+1):]
    if (len(b)%2==0): bh1=b[:(len(b)//2)]; bh2=b[(len(b)//2):]
    else: bh1=b[:(len(b)//2+1)]; bh2=b[(len(b)//2+1):]
    return ah1+bh1+ah2+bh2



# Простая функция test() используется в main() для вывода
# сравнения того, что возвращает с функция с тем, что она должна возвращать.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s Получено: %s | Ожидалось: %s' % (prefix, repr(got), repr(expected)))


# Вызывает фунции выше с тестовыми параметрами.
def main():
    print('Пончики')
    # Каждая строка вызывает donuts() и сравнивает возвращаемое значение с ожидаемым.
    test(donuts(4), u'Q: 4')
    test(donuts(9), 'Q: 9')
    test(donuts(10), 'Q: a lot')
    test(donuts(99), 'Q: a lot')

    print()
    print('Оба конца')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

    print()
    print('Кроме первого')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print()
    print('Перемешивание')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')

    print()
    print('Хорош')
    test(not_bad('this movie is not so bad'), 'this movie is good')
    test(not_bad('the dinner was not bad!'), 'the dinner was good!')
    test(not_bad('the tea is not hot already'), 'the tea is not hot already')
    test(not_bad("This is bad, but not at all"), "This is bad, but not at all")

    print()
    print('Две половины')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


# Стандартный шаблон для вызова функции main().
if __name__ == '__main__':
    main()
