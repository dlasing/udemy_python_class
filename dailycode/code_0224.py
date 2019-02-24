# Given an array of integers, find the first missing positive integer 
# in lineartime and constant space. In other words, find the lowest 
# positive integer that does not exist in the array. The array can 
# contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] 
# should give 3.

my_list = [3,4,-1,1]
#my_list = [1, 2, 0]

my_list = sorted(my_list)

for x in range(0,len(my_list)):

	print (x)
	#print (len(my_list))
	
	if x == len(my_list)-1:
		print (f"The number is {my_list[x]+1}")
		break
		
	if my_list[x+1]	!= my_list[x]+1 and my_list[x]+1 > 0:		
		print (f"Yeah.. found the number... {my_list[x]+1}")		
		break	
			
 