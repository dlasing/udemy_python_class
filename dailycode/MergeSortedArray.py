# Given two sorted integer arrays nums1 and nums2, merge nums2 
# into nums1 as one sorted array.
#
# Note:
#
# The number of elements initialized in nums1 and nums2 are 
# m and n respectively.
# You may assume that nums1 has enough space (size that is 
# greater or equal to m + n) to hold additional elements from 
# nums2.
#
# Example:
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
import random

class Merge_array:
	
	def __init__(self, m, n):
		
		self.m = m
		self.n = n
		
	def build_merge(self):
		
		list_a = []
		list_b = []
		total_size = self.m + self.n
		
		for x in range(0, total_size):
			if x >= self.m:
				list_a.append(0)
			else:
				list_a.append(random.randint(1,101))
				
		for y in range(0, self.n):
			list_b.append(random.randint(1,101))
			
		print (f"List_a = {list_a}")
		print (f"List_b = {list_b}")
			
		# append list_b to list_a in reverse order
		for z in range(0, self.n):
			list_a[-1-z] = list_b[z]
		
		list_a.sort()		
		print (f"After merge = {list_a}")
			
	
			
case = Merge_array(3,4)
case.build_merge()

		
		