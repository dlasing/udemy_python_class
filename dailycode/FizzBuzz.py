# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number and 
# for the multiples of five output “Buzz”. For numbers which are multiples of 
# both three and five output “FizzBuzz”.

class Fizzbuzz:
	
	def __init__(self, range):
		
		self.range = range
		
	def print_fizzbuzz(self):
		
		mylist = []
		for x in range(1, self.range+1):
			
			#print (f"At number {x}")
			if x%3 == 0:
				mylist.append("Fizz")
				
			elif x%5 == 0:
				mylist.append("Buzz")
				
			elif x%5 ==0 and x%3 == 0:
				mylist.append("FizzBuzz")
				
			else:
				mylist.append(x)
			
		print (f"The list is {mylist}")
			
			

solution = Fizzbuzz(20)
solution.print_fizzbuzz()