#Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
#Note:
#
#The number of elements initialized in nums1 and nums2 are m and n respectively.
#You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
#Example:
#
#Input:
#nums1 = [1,2,3,0,0,0], m = 3
#nums2 = [2,5,6],       n = 3
#
#Output: [1,2,2,3,5,6]



class merge_function:
	
	
	def __init__ (self, nums1_list, nums2_list):
		self.nums1_list = nums1_list
		self.nums2_list = nums2_list
		
		
		
	def merge_result(self):
		
		
		for i in range (0, len(self.nums2_list)):
			self.nums1_list.append(self.nums2_list[i])
			
			print (f"check this out... {self.nums1_list}")
			
		nums1_list.sort()
		print (f"check this out after sorted... {self.nums1_list}")
		
		
		
			
nums1_list = [1,88,3,4,5]
nums2_list = [99,100]

case = merge_function(nums1_list, nums2_list)
case.merge_result()
			
			
	
	