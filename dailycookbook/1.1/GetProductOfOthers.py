class GetProductOfAllOthers:
	
	def __init__(self, input_list):
		
		self.input_list = input_list
		
	def return_result(self):
				
		theresult = []
		for i in range(0,len(self.input_list)):
			
			counter = 1
			dummy = 1
			pointer = 0
			
			for j in range(0,len(self.input_list)-1):
				
				pointer = i + counter
				if pointer > len(self.input_list)-1:
					pointer = pointer - len(self.input_list)
					
				result = dummy * self.input_list[pointer]
				dummy = result
				counter = counter + 1
							
			theresult.append(result)	
			#print (f"output list is:{theresult}")	
			
		
		print (f"Result is {theresult}")
			
	
	
	
				
input_list = [3,2,1]
case = GetProductOfAllOthers(input_list)		
case.return_result()
					

				
			
			