# Генератор это функция, которая возвращает итератор. 
# Она выглядит как обычная функция, за исключением того, что она содержит 
# оператор yield, возвращающий серию значений, используемых в цикле 
# или через функцию next(). Каждый оператор yield временно замораживает 
# процесс, запоминая позицию выполнения (включая внутренние переменные).

def simple_generator():
    yield 'first'
    yield 'second'
    yield 'third'

for i in simple_generator():
    print(i)

a = simple_generator()
print(next(a))

# генератор чисел Фибоначчи
def fibonacci(max):
    a, b = 1, 2
    while a < max:
        yield a
        a, b = b, a+b

print(list(fibonacci(4000000)))

