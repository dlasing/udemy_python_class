# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
#
#      Example:
#
#Input: 5
#Output:
#[
#		 [1],
#		[1,1],
#	   [1,2,1],
#	  [1,3,3,1],
#    [1,4,6,4,1]
# ]


class PascelTriangle:
	
	def __init__(self, numRows):
		
		self.numRows = numRows
		
	def build_it(self):
		mylist = []
		counter = 0
		
		for x in range (0, self.numRows):
						
			for y in range (0,x+1):
				
				if y == 0 or y == x:					
					mylist.append(1)	
				else:
					mylist.append(mylist[counter-x-1] + mylist[counter-x])	
					
				counter += 1
			
			print (mylist)	
		
		
		
			
			
			


case = PascelTriangle(5)
case.build_it()
