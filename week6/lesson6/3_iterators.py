class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


print([c for c in Reverse('string')])


# Итерация по кастомным объектам

class Person:
    pass

class Department:
    def __init__(self, *members):
        self.members = members
        self.index = 0

    def __iter__(self):
        return iter(self.members)

    def __next__(self):
        if self.index == len(self.members):
            raise StopIteration
        ret = self.members[self.index]
        self.index += 1
        return ret

    # для простых случаев можно вернуть итератор от списка
    # def __iter__(self):
    #     return iter(self.members)


ivan, petr, vasily = Person(), Person(), Person()
department = Department(ivan, petr, vasily)

for person in department:
    print(person)

# print(next(department))
# print(next(department))
# print(next(department))
# print(next(department))



# Чтобы получить итератор из объекта к нему надо применить функцию iter:
# next() возвращает следующий объект итератора
i = iter(['a', 'b', 'c'])
print(next(i))









