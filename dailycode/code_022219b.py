# Given an array of integers, return a new array such that each 
# element at index i of the new array is the product of all the 
# numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected 
# output would be [120, 60, 40, 30, 24]. If our input was 
# [3, 2, 1], the expected output would be [2, 3, 6].


#global total 
#total = 1


import random

def input_size_of_list():
	
	global total
	total = 1
	
	my_list = []	
	while True:
		
		try:
			list_size = int(input("Input size of the list: "))
		except:
			print ("Interget please..")
		
		else:
			for x in range(0,list_size):
				my_list.append(random.randint(1,6))
				
				# calculate the lisk total
				total = total * my_list[x]
							
			print (f"This is the list {my_list}")
			return my_list
			



def list_multiper(the_list):
	#total = 1
	new_list =[]
	
	#print (type(the_list))
	
	#for y in range(0,len(the_list)):
		
	#	total = total * the_list[y]
		
	
	for z in range(0, len(the_list)):
		
		new_list.append(total//the_list[z])
		
		
	print (new_list)	



	
the_list = input_size_of_list()	
	
list_multiper(the_list)		