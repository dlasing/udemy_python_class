# You are a professional robber planning to rob houses 
# along a street. Each house has a certain amount of 
# money stashed, the only constraint stopping you from 
# robbing each of them is that adjacent houses have 
# security system connected and it will automatically 
# contact the police if two adjacent houses were broken 
# into on the same night.
#
# Given a list of non-negative integers representing 
# the amount of money of each house, determine the 
# maximum amount of money you can rob tonight without 
# alerting the police.
#
# Example 2:
#
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) 
# and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.


class Rob_house:
	
	def __init__(self, house_list):
		self.house_list = house_list
		
	def max_rob(self):
		even_total = 0
		odd_total = 0
				
		for x in range(0, len(self.house_list), 2):
			even_total += self.house_list[x]
			#print (f"even total: {even_total}")
			
		for y in range(1, len(self.house_list),2 ):
			odd_total += self.house_list[y]		
			#print (f"odd total: {odd_total}")
			
		# compare the max house value
		if even_total > odd_total:
			return print(f"Max house value is: {even_total}")
		else:
			return print(f"Max house value is: {odd_total}")
						
	
case = Rob_house([1,2,3,1])	
case.max_rob()	
			
			