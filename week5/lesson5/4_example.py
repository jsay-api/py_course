# В языке Python существует соглашение, согласно которому имена модулей 
# начинаются со строчной буквы, а имена классов – с прописной. Точно так же, 
# в соответствии с соглашениями, первому аргументу методов присваивается 
# имя self. Эти соглашения не являются обязательными, но они получили настолько
# широкое распространение, что отказ от следования им может ввести в 
# заблуждение тех, кто позднее будет читать ваш код.

class Person:
    ''' Описание класса.
        строки документации автоматически извлекаются функцией help '''
    # __init__ — самая обычная функция, не смотря на странное название
    # она вызывается при создании объекта и принимает self в кач-ве 1го аргумента
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def last_name(self):
        return self.name.split()[-1]

    def raise_pay(self, percent):
        self.pay = int(self.pay * (1 + percent/100))

    def __str__(self):
        # return '[Person: %s, %s]' % (self.name, self.pay)
        # улучшаем вывод занных о пользователе:
        return '[%s: %s, %s]' % (self.__class__.__name__, self.name, self.pay)



class Manager(Person):
    '''Менеджер получает также бонусы'''
    def raise_pay(self, percent, bonus=10):
        # self.pay = int(self.pay * (1 + (percent + bonus)/100))
        # Правильнее будет вызвать оригинальную версию с новыми аргументами
        Person.raise_pay(self, percent+bonus)

    # переопределим конструктор, вызовем оригинальный конструктор, 
    # задав значение по умолчанию
    def __init__(self, name, pay):
        Person.__init__(self, name, 'Manager', pay)


class Department:
    def __init__(self, *args):
        self.members = list(args) 

    def addMember(self, person):
        self.members.append(person) 

    def raise_pays(self, percent):
        for person in self.members: 
            person.raise_pay(percent)

    def showAll(self):
        print('Department persons:')
        for person in self.members:
            print(person)


# __name__ - атрибут модуля. содержит __main__, если модуль запущет самостоятельно
if __name__ == '__main__':
    # запуск только тогда, когда файл запускается для тестирования
    ivan = Person('Ivan Ivanov', pay=50000)
    vasily = Person('Vasily Ivanovich', job='designer', pay=100000)

    print(ivan.name, ivan.pay)
    print(vasily.name, vasily.pay)

    vasily.raise_pay(10)
    print(vasily.last_name(), vasily.pay)

    print(vasily, ivan) # кастомный вывод названий объектов

    petr = Manager('Petr Petrovich', pay=150000)
    petr.raise_pay(10, 10)
    print(petr)

    # полиморфизм. в зависимости от типа объекта вызывается нужный метод 
    for p in (ivan, vasily, petr):
        p.raise_pay(10)

    print(ivan, vasily, petr)


    development = Department(ivan, vasily) # Встраивание объектов в составной объект 
    development.addMember(petr)
    development.raise_pays(10) # Вызов метода giveRaise вложенных объектов 
    development.showAll()


    import shelve
    db = shelve.open('persondb')
    for object in (ivan, vasily, petr): # В качестве ключа использовать атрибут name
        db[object.name] = object
    db.close()


    db = shelve.open('persondb')
    print(len(db))
    for key in db:
        print(key, '=>', db[key])





