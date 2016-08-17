#!/usr/bin/python3
#coding: utf-8
__author__='julia sayapina'

import math
import random



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
= Строительные материалы
  - площадь (кв. м)
  - цена за единицу (рулон, банку, упаковку)
  = Обои
    - ширина рулона
    - длина рулона
  = Потолочная краска
    - вес банки
    - расход краски
  = Ламинат
    - длина доски
    - ширина доски
    - кол-во досок в упаковке
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
= Квартира
  - комнаты
  + добавить комнату
  + удалить комнату
  + посчитать смету на всю квартиру
  + при создании можно передать сразу все комнаты в конструктор

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

class ConstrMaterials(object):
    '''Construction materials super class'''
    def __init__(self, length = random.randint(20, 100), width = random.randint(200, 1000), price = random.randint(400, 1500)):
        self.length = length
        self.width  = width
        self.price = price
    
    @property
    def square(self):
        return length*width

    # @staticmethod
    # def rand_price:
    #     price = random.randint(400, 1500)
    #     return ConstrMaterials(price)


class WallPaper(ConstrMaterials):
    '''When u need to cover ur walls with wallpapers'''
    def __init__(self, length, width, square, price):
        super(WallPaper, self).__init__(length, width, square, price)

    

class Paint(ConstrMaterials):
    '''For painting ceilings'''
    def __init__(self, price, can_weight = random.randint(500, 1000), expedenture = random.randint(1,3)):
        super(Paint, self).__init__(price)
        self.can_weight = can_weight
        self.expedenture = expedenture


class Laminate(ConstrMaterials):
    '''For floor'''
    def __init__(self, length, width, square, price, pack_quantity = random.randint(10,30)):
        super(Laminate, self).__init__(length, width, square, price)
        self.pack_quantity = pack_quantity
    
class Flat(object):
    '''the whole flat class'''

    @classmethod
    def count(cls):
        return cls.counter


class Room(Flat):
    '''for rooms defining'''
    counter = 0
    def __init__(self, room_width, room_length, room_height, window_width, window_height):
      self.room_width = room_width
      self.room_length = room_length
      self.room_height = room_height
      self.window_height = window_height
      self.window_width = window_width
      Room.counter += 1

    @property
    def wall_square(self):
        w_square = (self.room_width + self.room_length) * self.room_height - self.window_height * self.window_width
        return w_square

    @property
    def ceiling_square(self):
        c_square = self.room_length * self.room_width
        return c_square
    
    def wp_rolls_quantity(self):
        set_w = self.wall_square/WallPaper.square
        return set_w

    def paint_ceiling(self):
        paint_c = self.ceiling_square*Paint.expedenture
        return paint_c

    def f_boards_quantity(self):
        cover_f = ceiling_square/Laminate.square
        return cover_f

    def sum_per_room(self):
        sum_pr = self.wp_rolls_quantity()*Wallpaper.price + self.paint_ceiling()*Paint.can_weight + self.f_boards_quantity*Laminate.price
        return math.ceil(sum_pr)

kitchen = Room(3, 10, 3, 1, 2)
wp1 = WallPaper(6,3,18,250)
paint1 = Paint()
lam1 = Laminate()
print wp1.__dict__

print kitchen.sum_per_room()


