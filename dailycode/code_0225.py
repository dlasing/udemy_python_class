# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of 
# ways it can be decoded. For example, the message '111' would give 3, since it could be 
# decoded as 'aaa', 'ka', and 'ak'. You can assume that the messages are decodable. 
# For example, '001' is not allowed.

a = '122991111'
counter = 0

		
for y in range(0,len(a)):
	
	if int(a[y]) == 0:
		# if there is 0 in the string.. means per character
		# match does not valid. Reset counter
		counter = 0
	else:
		counter +=1

for z in range(0,(len(a)-1)):	
	
	if int(a[z:z+2]) <= 26:
		print (f"one match: {a[z:z+2]}")
		counter +=1
	
print (f"There are {counter} match")
		
		 

