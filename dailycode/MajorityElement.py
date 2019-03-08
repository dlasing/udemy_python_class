# Given an array of size n, find the majority element. The majority element 
# is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element 
# always exist in the array.
#
# Example 1:
#
# Input: [3,2,3]
# Output: 3
#
#
# Example 2:
#
# Input: [2,2,1,1,1,2,2]
# Output: 2


class MajorityElement:
	
	def __init__(self, mylist):
		self.mylist = mylist
		
	def find_majority(self):
		
		appear = 0
		print (f"List of: {self.mylist}")
		self.mylist.sort()
		
		
		for x in range(0, len(self.mylist)):
			
			if self.mylist[x] ==  self.mylist[x+1]:
				appear +=1
			else:
				appear = 0
				
			if appear+1 >= round(len(self.mylist)/2):
				
				return self.mylist[x]	
				
case = MajorityElement([9,9,9,1,1,1,9,9])
print (f"Return value of : {case.find_majority()}")