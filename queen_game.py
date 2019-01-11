# Little game to enter a number N 
# Then print out N x N 
# The Queen (Q) on each row never openlap with each other

import random
n = input("Input a number:")
val = int(n)

mylist = list(range(val))
random.shuffle(mylist)
print ('The random list is:',mylist)


loop = 0
header = 'abcdefghijklmnopqrstuvwxyz'


while loop < val:
    loop2 = 0
    
    #print header first....
    print (header[loop], end="")
    
    while loop2 < val:
        if mylist[loop] == loop2:
            print ("Q", end="")
        else:
            print (".", end="")
        loop2+= 1
    print ("\n")
    loop+=1

print (" ",end="" )
for num in range (val):
    print (num, end="")
