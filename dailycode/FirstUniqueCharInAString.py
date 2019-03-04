s = 'loveleetcode'

class Solution():

	def __init__(self, source):
		
		self.source = source
		
	def finduniquechar(self):
		counter = 1		
		 		
		for x in range(0,len(self.source)):
			unique = True
			
			for y in range(counter,len(self.source)):
				
				# Debug code
				#print (f"{s[x]} is == {s[y]} ?")
				if s[x] == s[y]:
					unique = False
			
			# if the char is unique.. return the position of the
			# char. 		
			if unique == True:
				return x						
			counter += 1
			
			
			
leetcode = Solution(s)
print (f"Source is: {s}")
print (leetcode.finduniquechar())