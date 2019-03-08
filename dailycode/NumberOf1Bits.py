# Write a function that takes an unsigned integer and return the 
# number of '1' bits it has (also known as the Hamming weight).

class HammingWeight:
	
	def __init__(self, input_value):
		
		self.input_value = input_value
		
	def num_of_1s(self):
		
		
		count = 0
		for x in range(0, len(self.input_value)):
			
			if self.input_value[x] == '1':
				count += 1
		
		print (f"Input: {self.input_value}")
		return count		
		
		

case = HammingWeight('11111111111111111111111111111101')
print (f"Output: {case.num_of_1s()}")

