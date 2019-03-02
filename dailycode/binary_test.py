# This is the program to print the binary tree level
# And try to add up all value in the tree. 
# Learn the structure of the binary Tree. 

class Node:
	
	def __init__(self, root):
		
		self.root  = root
		self.left  = None
		self.right = None
		
		
# The function to walk the binary tree top to bottom
def node_res(root):
	
	global call_level 
	global total
		
	# node_res() called, count the number of call
	call_level += 1
	
	
	
	# Return True if this is the end of the Tree. 
	if root == None:	
		print (f"This is level: {call_level}")
		print ("root is: None\n\n")
		return True
	else:
		print (f"This is level: {call_level}")
		print (f"root is: {root.root}")
		print (f"left is: {root.left}")
		print (f"right is: {root.right}")
		total = total + root.root
		print (f"total is.... {total}\n\n")
		
	# Check the node left and right leave.  
	#         root
	#         / \
	#  root.left root.right
	#
	left  = node_res(root.left)
	right = node_res(root.right)
	
	return total	
	
	
	
def node_total(root):
	
		return node_res(root)




# gloal value
call_level = 0	
total = 0



# Build the Nodes...	
root = Node(5)
root.left  = Node(4)
root.right = Node (3)
#root.left.left = Node(2)
#root.left.right = Node(9)




print (f"The total of the tree is... {node_total(root)}")