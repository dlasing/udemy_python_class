class GetProductOfAllOthers:
	
	def __init__(self, input_list):
		
		self.input_list = input_list
		
	def return_result(self):
		
		theresult=[]
		for i in range (0, len(self.input_list)):
		
			pointer = i + 1
			result = 1
		
			for j in range (0, len(self.input_list)-1):
			
				# make sure it loop back to the top of the list
				if pointer > len(self.input_list)-1:
					pointer = 0
					
				result = result * self.input_list[pointer]
				print(f"Check this... {result}")
				
				pointer = pointer +1
				
			theresult.append(result)
			print(f"The results so far... {theresult}")				
				
# The idea is use the i and j to console the logic. 
# Move the pointer along the list to get the result. 				


input_list = [4,3,2,1]
case = GetProductOfAllOthers(input_list)
case.return_result()