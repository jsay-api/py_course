#!/usr/bin/python3
# coding: utf-8

"""Лото

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random

user_card = [[], [], []]
comp_card = [[], [], []]
j = [[], [], []]


for i in user_card:	#сначала сделала класс, потом поняла, что нет смысла – разный код (немножко) для всего двух карточек, верно? или все же надо??
    while len(i)<5:
        number = random.randint(1,90)
        if not any(number in j for j in user_card):	#проверка на уникальность числа
            i.append(number) 
    i.sort() # сортируем по возрастанию
    while len(i)<9:
    	i.insert(random.randint(0,len(i)), ' ') #добавляем пустые клетки на случайные места
def print_ucard():
	print ('----- Your card ------') #как правильнее сделать здесь? тупо принтами??
	for i in user_card:
		print (' '.join(map(str, i)))
	print ('----------------------')

for i in comp_card:
    while len(i)<5:
        number = random.randint(1,90)
        if (not any(number in j for j in comp_card) and (not any(number in k for k in user_card))): #проверяем уникальность, чтобы число не встречалось ни в одной карточке
            i.append(number)
    i.sort()
    while len(i)<9:
    	i.insert(random.randint(0,len(i)), ' ')
def print_ccard():
	print ('-- Computer\'s card ---')
	for i in comp_card:
		print (' '.join(map(str, i)))
	print ('----------------------')

def new_num(n):
	j = 0
	for i in random.sample(range(1,n+1), n): 
		j += 1
		yield i,j

def  wrong_ans():
	raise ValueError('You lost! Game over')
	sys.exit(1)
	

num_q = 90 #количество бочонков
for i,j in new_num(num_q):
	print ("New number is %s (%d left)" % (i, (num_q-j)))
	print_ucard()
	print_ccard()
	for n in range(3):
		comp_card[n] = ['-' if x == i else x for x in comp_card[n]]
	for n in range(3):
		u_ans = input('Want to cross out the number? y/n \n')
		#print (u_ans)
		if u_ans == 'y':
			print ('hey')
			if not any(i in x for x in user_card): wrong_ans() 
			for n in range(3): 
				user_card[n] = ['-' if x == i else x for x in user_card[n]]
			break
		elif u_ans == 'n':
			for x in user_card:
				if i in x: wrong_ans()
			else: break
		else: 
			print ("Please answer y/n")
			continue
	else: print ("No more attempts left");wrong_ans()
	if all(item == '-' for item in user_card): 
		print ("Congrats, you won!")
		sys.exit(0)
	if all(item == '-' for item in comp_card):
		print ("Computer won, you lost! Game over")
		sys.exit(0)






