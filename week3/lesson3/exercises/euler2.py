#!/usr/bin/python3
# coding: utf-8
# __author__='julia sayapina'

from functools import reduce

# Заполните код приведенных ниже функций. Функция main() уже настроена
# для вызова функций с несколькими различными параметрами,
# и выводит 'OK' в случае, если вызов функции корректен.
# Начальный код каждой функции содержит 'return'
# и является просто заготовкой для вашего кода.


# A. Какова разность между суммой квадратов и квадратом суммы?
# Сумма квадратов первых десяти натуральных чисел
# 1**2 + 2**2 + ... + 10**2 = 385
# Квадрат суммы первых десяти натуральных чисел
# (1 + 2 + ... + 10)**2 = 55**2 = 3025
# Следовательно, разность между суммой квадратов и квадратом суммы первых
# десяти натуральных чисел составляет 3025 - 385 = 2640.
# Найдите разность между суммой квадратов и квадратом суммы первых 
# ста натуральных чисел.
# Решите задачу двумя способами: с помощью map и lambda 
# и с помощью генератора списка. 
def diff():
    # +++ ваш код +++
    #print 
    return sum(map(lambda x: x, range(101)))**2 - sum(map(lambda x: x**2, range(101)))


# B. Найдите наибольшее произведение пяти последовательных цифр в 
# 1000-значном числе.
string = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

def max_five():
    # +++ ваш код +++
    x = 0
    stringtolist = []
    mults = []
    for i in range(5, 1001, 5): 
        stringtolist.append(list(string.translate(None, "\n")[x:i])) #делим на массивы по 5 цифер
        x = i
    for i in stringtolist:
        mults.append(reduce(lambda x, y: x * y, map(int, i))) #перемножаем цифры внутри каждой пятерки
    return max(mults) #почему ответ не сходится? не могу найти ошибку((


# C. Какова сумма цифр числа 2**1000
# 2**15 = 32768, сумма цифр 3 + 2 + 7 + 6 + 8 = 26.
# Какова сумма цифр числа 2**1000?
def summm():
    # +++ ваш код +++
    return reduce(lambda x, y: x + y, map(int, str(2**1000)))


# D. Найдите сумму цифр в числе 100!
# n! означает n * (n-1) * ... * 3 * 2 * 1
# Найдите сумму цифр в числе 100!.
def factorial():
    # +++ ваш код +++
    return reduce(lambda x, y: x + y, map(int, str(reduce((lambda x, y: x * y), reversed(range(1, 100))))))


# Простая функция test() используется в main() для вывода
# сравнения того, что возвращает функция с тем, что она должна возвращать.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s Получено: %s | Ожидалось: %s' % (prefix, repr(got), repr(expected)))


# Вызывает фунции выше с тестовыми параметрами.
def main():
    print('A. Разность между суммой квадратов и квадратом суммы?')
    test(diff(), 25164150)

    print()
    print('B. Наибольшее произведение пяти последовательных цифр')
    test(max_five(), 40824)

    print()
    print('C. Сумма цифр числа 2**1000')
    test(summm(), 1366)

    print()
    print('D. Сумма цифр в числе 100!')
    test(factorial(), 648)

if __name__ == '__main__':
    main()
