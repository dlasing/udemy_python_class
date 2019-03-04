class Node():
	
	def __init__(self, data):
		
		self.data = data
		self.left = None
		self.right = None
		
		

def find_depth(node):
	global depth_level
	
	
	# if this is the end of the tree
	if node == None:
		return True
		
	left = find_depth(node.left)
	right = find_depth(node.right)
	
	if left and right == True:
		depth_level += 1
		print (f"The depth is...{depth_level}")
		
		
	return depth_level
	

depth_level = 0

# build the tree
#
#      	3
#      / \
#     9  20
#    	/  \
#      15   7
node = Node(3)
node.left = Node(9)
node.right = Node(20)
node.right.left = Node(15)
node.right.right = Node(7)


# find the tree depth
# passin value: node
print (f"Depth is:  {find_depth(node)}")