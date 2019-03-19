# Given a m x n matrix, if an element is 0, set its entire row and column to 0. 
# Do it in-place.
#
# Example 1:
#
#Input: 
# [
#	[1,1,1],
#	[1,0,1],
#	[1,1,1]
# ]
# Output: 
# [
# 	[1,0,1],
#	[0,0,0],
# 	[1,0,1]
# ]

class SetMatrixZeroes:
	
	def __init__(self,mylist):
		
		self.mylist = mylist
		
	def find_zero(self):
		
		zero_position = []
		for m in range(len(self.mylist)):
			for n in range(len(self.mylist[0])):
			
				if self.mylist[m][n] == 0:
					zero_position.append([m,n])
					
		print (zero_position)
		
		return zero_position
		
	
	def set_zeroes(self, zero_list):
		
		# convert the target row to 0
		for row in range(len(self.mylist[0])):
			self.mylist[zero_list[0][0]][row] = 0
			
		# convert the target colum to 0
		
		for column in range(len(self.mylist)):
			self.mylist[column][zero_list[0][1]] = 0
			
		print (self.mylist)
		
		
				

matrix_list = [ [1,1,1], [1,0,1], [1,1,1]]

case = SetMatrixZeroes(matrix_list)
case.set_zeroes(case.find_zero())
