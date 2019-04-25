# Linked List basic



class LinkedListNode:
	
	def __init__(self, value, nextNode = None):
		
		self.value = value
		self.nextNode = nextNode
		



node1 = LinkedListNode("3")
node2 = LinkedListNode("6")
node3 = LinkedListNode("9")


node1.nextNode = node2  # node1 -> node2, "3" -> "6"
node2.nextNode = node3  # node2 -> node3, "6" -> "9"




# The code to traversing the linked list..
# Need to assign the head node first

head = node1
# Regular Traversal

# Then assign a pointer to the current node. 
currentNode = head

while currentNode is not None:
		print (f"CurrentNode is {currentNode}, the value is {currentNode.value}")
		currentNode = currentNode.nextNode
		
		
		
		
	
	
