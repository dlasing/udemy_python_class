# Return the index of the first occurrence of needle in haystack, or -1 if 
# needle is not part of haystack.
#
#  Example 1:
#
#  Input: haystack = "hello", needle = "ll"
#  Output: 2
#  Example 2:
#
#  Input: haystack = "aaaaa", needle = "bba"
#  Output: -1


haystack = "hello"
needle = "aa"


for x in range (0, len(haystack)):
	
	if haystack[x:(len(needle)+x)] == needle:
		
		print (f"position: {x}")
	
print ("postion: -1")