# Given a list of non negative integers, arrange them such that they form the largest number.
#
# Example 1:
#
# Input: [10,2]
# Output: "210"
# Example 2:
# 
# Input: [3,30,34,5,9]
# Output: "9534330"


class Largest_num:
	
	def __init__(self, num_list):
		
		self.num_list = num_list
		
	
	def find_largest(self):
		
		for x in range (0, len(self.num_list)):
			for y in range (-1, -(len(self.num_list))-x, -1):
				
				temp = 0
				# bubble sort
				if self.num_list [x] <  self.num_list[y]:
					temp = self.num_list[x]
					self.num_list[x] = self.num_list[y]
					self.num_list[y] = temp
					
					print (self.num_list)
		
			
case = Largest_num([32,30,34,50,91])
case.find_largest()