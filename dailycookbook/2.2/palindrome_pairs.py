# Problem 2.2
# Generate palindrome pairs


def palindrome_pair(compare_word):
	
	counter = 0
	for k in range(0, len(compare_word)):
		
		print (f"{compare_word[k]}   VS  {compare_word[-1 - k]}")
		if compare_word[k] != compare_word[-1 - k]:
			
			return "NOT"
			
	return "YES"

def search_string (word_list):
	result = []
	
	for i, first_word in enumerate(word_list):
	
		for j, second_word in enumerate(word_list):
		
			# In the case when they are checking the same word
			if i == j:
				continue
		
			print (first_word + second_word)
			if palindrome_pair(first_word + second_word) == "YES":
			
				result.append((i,j))
				
	return result		
	
	
	
	
word_list = ['code', 'edoc', 'da', 'd']
print(search_string(word_list))
	
				
