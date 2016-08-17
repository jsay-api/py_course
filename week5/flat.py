# coding: utf-8

""" Ремонт в квартире 

Есть квартира (2 комнаты и кухня). В квартире планируется ремонт: нужно 
поклеить обои, покрасить потолки и положить пол.

Необходимо рассчитать стоимость материалов для ремонта.

Из описания следуют следующие классы:
= Строительные материалы
  = Обои
  = Потолочная краска
  = Ламинат
= Комната
= Квартира

Подробнее, с методами (+) и атрибутами (-):


Необходимо создать стройматериалы, назначить им цены и размеры.
Создать комнаты, поклеить, покрасить и положить все на свои места.
Cоздать квартиру, присвоить ей комнаты и посчитать общую смету.

Подсказка: для округления вверх и вниз используйте:
import math
math.ceil(4.2)  # 5
math.floor(4.2) # 4

Примечание: Для простоты, будем считать, что обои над окном и над дверью 
не наклеиваются.
----------------

Дополнительно:
Сделать у объекта квартиры метод, выводящий результат в виде сметы:

[Комната: ширина: 3 м, длина: 5 м, высота: 2.4 м]
Обои        400x6=2400 руб.
Краска     1000x1=1000 руб.
Ламинат     800x8=6400 руб.
[Комната: ширина: 3 м, длина: 4 м, высота: 2.4 м]
Обои        400x5=2000 руб.
Краска     1000x1=1000 руб.
Ламинат     800x7=5600 руб.
[Кухня: ширина: 3 м, длина: 3 м, высота: 2.4 м]
Обои        400x4=1600 руб.
Краска     1000x1=1000 руб.
Ламинат     800x5=4000 руб.
---------------------------
Итого: 25000 руб.

"""

import math
import sys

reload(sys)
sys.setdefaultencoding('cp866')     # задаем читаемую кодировку для консоли


class Material(object):
    '''
    = Строительные материалы
      - площадь (кв. м)
      - цена за единицу (рулон, банку, упаковку)
    '''
    def __init__(self, name, one_cost):
        self.name = name
        self.square = 0.0           # площадь, которую нужно покрыть материалом
        self.one_cost = float(one_cost)
        
    def __str__(self):
        return u'Материал: {0} руб., {1} кв.м'.format(cost, square)              
        
    @property    
    def pack_square(self):
        ''' Площадь одной единицы материала (упаковки, банки, рулона)
            Необходимо переопределять у конкретного материала
        '''
        return 1
                 
    def estimate(self, square):
        ''' Смета за материал
        '''
        count = math.ceil(square / self.pack_square)        # количество единиц материала
        res = count * self.one_cost                         # стоимость данного материала        
        print u'{0:<15} {1:>5} x {2:>5} = {3:>7} руб.'.format(self.name, self.one_cost, count, res)
        return res 
        
        
class Wallpaper(Material):
    '''
      = Обои
        - ширина рулона
        - длина рулона    
    '''
    def __init__(self, width, length, one_cost):
        super(Wallpaper, self).__init__(u'Обои', one_cost)
        self.width = float(width)                  # ширина обоев
        self.length = float(length)                # длина рулона
        
    @property    
    def pack_square(self):
        ''' Площадь одной единицы материала (упаковки, банки, рулона)
        '''
        return self.width * self.length   
    
        
class Ceiling(Material):
    ''' Класс полочной краски
      = Потолочная краска
        - вес банки
        - расход краски
    '''
    def __init__(self, weight, consumtion, one_cost):
        super(Ceiling, self).__init__(u'Краска', one_cost)
        self.weight = float(weight)                  # вес банки
        self.consumtion = float(consumtion)          # расход краски (л. краски для окраски 1 кв.м. поверхности)
        
    @property    
    def pack_square(self):
        ''' Площадь покраски одной банкой
        '''
        return self.weight / self.consumtion
            
        
class Laminat(Material):
    ''' Класс ламината
      = Ламинат
        - длина доски
        - ширина доски
        - кол-во досок в упаковке    
    '''
    def __init__(self, length, width, count, one_cost):
        super(Laminat, self).__init__(u'Ламинат', one_cost)
        self.length = float(length)        # длина доски
        self.width = float(width)          # ширина доски
        self.count = count                 # количество досок в упаковке
        
    @property    
    def pack_square(self):
        ''' Площадь одной упаковки
        '''
        return self.width * self.length * self.count
            

class Room():
    '''
        = Комната
          - ширина
          - высота
          - длина
          - ширина окна
          - ширина двери
          + поклеить обои
          + покрасить потолок
          + положить пол
          + посчитать смету на комнату
          + при создании комнаты сразу передавать все атрибуты в конструктор __init__()    
    '''
    def __init__(self, name, width, height, length, w_window=120, w_door=90):
        self.name = name
        self.width = float(width)
        self.height = float(height)
        self.length = float(length)
        self.w_window = float(w_window)    # ширина окна
        self.w_door = float(w_door)        # ширина двери
        self.materials = []
    
    def __str__(self):    
        return u'[{0}: ширина: {1} м, длина: {2} м, высота: {3} м]'.format(self.name,self.width,self.length,self.height)
    
    def add_material(self, material):
        ''' Добавить материал для ремонта комнаты
        '''
        self.materials.append(material)
    
    def calc_material(self, material):         
        ''' Обобщенный метод для расчета материалов
        '''
        if isinstance(material, Wallpaper):
            square = (2 * (self.width + self.length) - self.w_door - self.w_window) * self.height
        elif isinstance(material, (Ceiling, Laminat)):   
            square = self.width * self.length
        else:
            square = 1
        return material.estimate(square)       
    
    @property
    def estimate(self):
        ''' Посчитать смету за комнату
        '''    
        res = 0
        print self
        
        for material in self.materials:
            res += self.calc_material(material)
        print    
        return res
    

class Flat():
    ''' Класс квартиры
    = Квартира
      - комнаты
      + добавить комнату
      + удалить комнату
      + посчитать смету на всю квартиру
      + при создании можно передать сразу все комнаты в конструктор
    '''
    def __init__(self, *args):
        if args:
            self.rooms = list(args)
        else:
            self.rooms = []
    
    def add_room(self, room):
        ''' Добавление комнаты в квартиру
        '''
        self.rooms.append(room)
        
    def add_rooms(self, *args):
        ''' Добавление комнат в квартиру
        '''
        self.rooms.extend(args)
        
    def del_room(self, room):
        ''' Удаление комнаты из квартиры
        '''
        if room in self.rooms:
            self.rooms.remove(room)
           
    def estimate(self):
        ''' Подсчет сметы за квартиру
        '''
        res = sum((room.estimate for room in self.rooms))
        print '-'*30
        print u'Итого: {0} руб.'.format(res)
        return res


def main():
    
    laminat = Laminat(1.5, 0.25, 8, 1500)
    wallpaper = Wallpaper(0.9, 10.0, 300)
    ceiling = Ceiling(3.0, 0.25, 320)
    
    my_kitchen = Room(u'Кухня', 3.4, 2.7, 4.2, 1.2, 0.9)    
    my_kitchen.add_material(ceiling)
    my_kitchen.add_material(wallpaper)
    my_kitchen.add_material(laminat)
    
    my_room1 = Room(u'Спальня', 3.5, 2.5, 4.0, 1.2, 0.9)   
    my_room1.add_material(wallpaper)
    
    my_room2 = Room(u'Детская', 3.0, 2.5, 3.4, 1.2, 0.9)
    my_room2.add_material(ceiling)
    my_room2.add_material(laminat)
        
    my_flat = Flat()
    my_flat.add_rooms(my_kitchen, my_room1, my_room2)
    
    my_flat.estimate()


if __name__ == '__main__':
    main()
