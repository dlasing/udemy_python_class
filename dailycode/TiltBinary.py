# The tilt of a tree node is defined as the absolute difference between the sum 
# of all left subtree node values and the sum of all right subtree node values. 
# Null node has tilt 0.


class Node():
	
	def __init__(self, data):
		self.data  = data
		self.left  = None
		self.right = None
		
		
	
def calculate_tite(node):
		
	if node == None:
		return True
	else:
		
		print (f"Node is.... {node.data}")		
		sum = sum + node.data
		print (f"SUM is.. {sum}")
				
	left = calculate_tite(node.left)		
	right = calculate_tite(node.right)
	
	
	#print (f"{left}")
	#if left == False or right == False:
#		print (f"Node is...{node.data}")
		
		
	#print (f"Node {node.data} ")
	#print (f"Node {node.data} right is {node.right}")
	#print (f"Node {node.data} left is {node.left}")
	
	
node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
node.right.right = Node(6)
node.right.left = Node(7)

calculate_tite(node)