# Given a 32-bit signed integer, reverse digits of an integer.
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21


class ReverseInteger:
	
	def __init__(self, n):
		self.n = n
		
	def reverse_it(self):
		
		out_string = ""
		
		# Take care "-" case before reverse it
		if self.n < 0:
			out_string = out_string + "-"
			
		# convert the input integer as string
		# print out from reverse order
		# abs() the self.n 
		for x in range(-1, -len(str(abs(self.n)))-1, -1):
						
			# Take care "0" case
			if str(self.n)[x] == "0":
				out_string = out_string + ""
				
			else:
				out_string = out_string + str(self.n)[x]
				
		
		return out_string
			
			
	

case = ReverseInteger(100)
print(f"Output: {case.reverse_it()}")