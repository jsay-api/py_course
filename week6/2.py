import random

x = [[3, 1, 10, 0, 12], [4, 12, 0, 3, 15], [0, 0, 4, 8, 13]]

if any(0 in j for j in x): print 0



res = [[],[], []]
for i in res:
 
    
    while len(i)<9:
        number = random.randint(1,90)
        #print number
        if not any(number in j for j in res):
            i.append(number)
            #print True, res

print res


class createCard(object):
	def __init__(self):
		self.card = [[],[], []]
	def __call__(self):
		for i in self.card:
		    while len(i)<9:
		        number = random.randint(1,90)
		        if not any(number in j for j in self.card):
		            i.append(number)
		return self.card

card = createCard()
user_card = card()
new_card = createCard()
computer_card = new_card()
print  (user_card)
print (computer_card)
