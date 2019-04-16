# Problem 1.4

class FindNumberOfSmallerOnTheRight:
		
	def __init__(self, input_list):
		
		self.input_list = input_list
		
	def solution(self):
		
		output_list = []
		
		for i in range (0, len(self.input_list)):
			
			smaller_found = 0
			
			for j in range (1, len(self.input_list)-i):
				
				if self.input_list[i+j] < self.input_list[i]:
					
					smaller_found += 1
					
					
					
			output_list.append(smaller_found)		
			#print (f"How many smaller found so far? {smaller_found}")	
		print (f"Output List: {output_list}")
			

mylist = [3,4,9,6,1]
case = FindNumberOfSmallerOnTheRight(mylist)
case.solution()



		
	