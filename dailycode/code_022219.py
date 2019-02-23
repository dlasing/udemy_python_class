# Date: 2/22/2019
# Program to input list of numbers and a number k.
# return any two numbers from teh list add up to k.
import random

try:
	size_of_list = int(input('Please enter the size of the list '))
except:
	print ('Enter number only')


K = int(input('Enter the number: '))


my_list = []
sort_list = []

for x in range(0, size_of_list):
	my_list.append(random.randrange(0,size_of_list))
	
sort_list = sorted(my_list)

print (f"This is the list {sort_list}")

head = 0
tail = size_of_list - 1

for y in range(0, size_of_list):
	
	print (f"Head: {sort_list[head]}.  Tail: {sort_list[tail]}")
	if sort_list[head] + sort_list[tail] == K:
		print (f"{sort_list[head]} , {sort_list[tail]}")
		break
				
	if sort_list[head] + sort_list[tail] > K:
		tail -= 1
	else:
		head += 1
		
		
		
		
	
	
	