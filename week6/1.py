import random
x = [1,2,3]
y = [4,5,6]




b = [[90, 72, 42, 20, 10, ' ', ' ', ' ', ' '], [50, 47, 59, 4, 33, ' ', ' ', ' ', ' '], [79, 11, 70, ' ', 56, ' ', ' ', 62, ' ']]



c = [90, 72, 42, 20, 10, ' ', ' ', ' ', ' ']
l = []
k = [[], [], []]
m = [[],[],[]]
for i in c:
    l.append(str(i))
j=(' '.join(l))



##for i in k,b:
##    while len(i)<9:
##        for n in j:
##            i.append(str(n))
##
##               
##print (k)    
##for i in k:
##    print (' '.join(i))
##
##for i in b,k:
##    print (i)

##for i in b:
##    print (' '.join(map(str, i)))
##def w_a():
##    raise ValueError('hello')
##    sys.exit(1)
##a=[90, 72, 42, 20, 10, ' ', ' ', ' ', ' ']
##a = [4 if x==' ' else x for x in a]
##print (a)
##for n in range(3):
##    b[n] = ['-' if x==' ' else x for x in b[n]]
##print (b)


##for i in range(3):
##    if i == 2:
##        w_a()
##    else: print (i)

u_ans = input('Want to cross out the number? y/n \n')
##if u_ans == 'y': print('hello')

if not any(int(u_ans) in j for j in b): print ('u lost)')
