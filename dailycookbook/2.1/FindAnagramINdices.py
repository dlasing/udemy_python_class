# Problem 2.1
# Find anagram indices


class FindAnagramIndices:
	
	def __init__(self, input_word, input_string):
		
		self.input_word = input_word
		self.input_string = input_string
		
	def find_indices(self):
		
		input_word_to_list = []
		return_list = []
		counter = 0
		
		# Put input_string to a list
		for i in range(0, len(input_string)):
			
			input_word_to_list.append(self.input_string[i])
			
			print (f"input_word_to_list is... {input_word_to_list[i]}")
			
		# Find the indices in left to right direction
		for j in range(0, len(input_word_to_list)-1):
		
				
			if input_word_to_list[j] + input_word_to_list[j+1] == self.input_word:
				
				print (f"Found it... ")
				return_list.append(j)
				print (f"return_list is... {return_list}")
				
				
		# Find the indices in right to left direction		
		for k in range(len(input_word_to_list)-1, 0, -1):
			
			if input_word_to_list[k] + input_word_to_list[k-1] == self.input_word:
				
				print (f"Found it... ")
				return_list.append(k)
				print (f"return_list is... {return_list}")

			
					
				
			
			
			
input_word = "ab"
input_string = "abxaba"
case = FindAnagramIndices( input_word, input_string)
case.find_indices()