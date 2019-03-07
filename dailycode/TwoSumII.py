# Given an array of integers that is already sorted 
# in ascending order, find two numbers such that 
# they add up to a specific target number.
#
# The function twoSum should return indices of the 
# two numbers such that they add up to the target, where 
# index1 must be less than index2.

class TwoSum:
	
	def __init__(self, target, mylist):
		
		self.target = target
		self.mylist = mylist
		
	def find_index(self):
		
		head = 0
		tail = len(self.mylist)-1
		
		for x in range(0, len(self.mylist)):
			
			if self.mylist[head] + self.mylist[tail] > self.target:
				tail -= 1
				
			elif self.mylist[head] + self.mylist[tail] < self.target:
					head += 1
					
			elif self.mylist[head] + self.mylist[tail] == self.target:
					return print(f"[ {head+1}, {tail+1}]")		
				
				
				
case = TwoSum(18, [2,7,11,15])
case.find_index()
