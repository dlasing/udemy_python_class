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
		
		# Analysis
		# Based on the list returned from find_zero(),  we have "position" of 
		# all 0 found
		# For example:
		# 
		# [[0, 0], [0, 3]]
		#   A  B    C  D
		# 
		# convert the target row to 0
		# pick the zero_list[row][0]  which is A, C, then convert
		# the list to "0"
		# In this example, we convert row "0" to all 0
		for convert_row in range(len(zero_list)):
			for row in range(len(self.mylist[0])):
				self.mylist[zero_list[convert_row][0]][row] = 0
			
		# convert the target colum to 0
		# pick the zero_list[column][1] which is B, D, the convert
		# the list to "0"
		for convert_column in range(len(zero_list[0])):
			for column in range(len(self.mylist)):
				self.mylist[column][zero_list[convert_column][1]] = 0
			
		print (self.mylist)
		
		
				

#matrix_list = [ [1,1,1], [1,0,1], [1,1,1]]
matrix_list = [ [1,1,2,0], [3,4,0,2], [0,0,1,5]]

case = SetMatrixZeroes(matrix_list)
case.find_zero()

#case.set_zeroes(case.find_zero())
