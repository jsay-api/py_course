# наследуем один базовый класс - object
class Par1(object):                
    def name1(self): 
        return 'Par1'

class Par2(object):
    def name2(self): 
        return 'Par2'

# создадим класс, наследующий Par1, Par2 (и, опосредованно, object)
class Child(Par1, Par2):           
    pass

# экземпляру Child доступны методы из Par1 и Par2
x = Child()
print(x.name1(), x.name2())               


# Множественное наследование в Python применяется в основном для добавления 
# примесей (mixins) — специальных классов, вносящих некоторую черту поведения 
# или набор свойств.

class Printed:
    def __str__(self):
        return '[%s]' % self.__class__.__name__

class Animal:
    pass

class Cat(Animal, Printed):
    pass

class Dog(Animal, Printed):
    pass

a = Cat()
print(a)

b = Dog()
print(b)