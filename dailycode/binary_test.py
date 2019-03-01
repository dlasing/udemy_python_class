# This is the program to print the binary tree...
# Learn the structure of the binary Tree. 

class Node:
	
	def __init__(self, root):
		
		self.root  = root
		self.left  = None
		self.right = None
		
		
# The function to walk the binary tree top to bottom
def node_res(root):
	
	global call_level 
	
	# node_res() called, count the number of call
	call_level += 1
	
	print (f"This is level: {call_level}")
	print (f"root is : {root}")
	print ("\n")
	
	# Return True if this is the end of the Tree. 
	if root == None:
		
		return True
		
	# Check the node left and right leave.  
	#         root
	#         / \
	#  root.left root.right
	#
	left  = node_res(root.left)
	right = node_res(root.right)
	

# gloal value

call_level = 0	
	


	
root = Node(5)
root.left  = Node(4)
root.right = Node (3)

node_res(root)
