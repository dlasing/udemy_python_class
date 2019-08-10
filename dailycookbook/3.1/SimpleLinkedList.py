# Linked List basic



class LinkedListNode:
	
	def __init__(self, value, nextNode = None):
		
		self.value = value
		self.nextNode = nextNode
		
def travelNode(head):
	
	currentNode = head
	while currentNode is not None:
			print (f"The value is {currentNode.value}")
			currentNode = currentNode.nextNode
	print ("########################")
	


def inertNode (head, insertNodeValue):
	
	currentNode = head
	
	while currentNode is not None:
		if currentNode.nextNode is None:
			currentNode.nextNode = LinkedListNode(insertNodeValue)
			return head
		currentNode = currentNode.nextNode
		
		
def deleteNode (head, deleteNodeValue):
	
	currentNode = head
	previousNode = head
	
	while currentNode is not None:
		
		# Case 1: deleteNode is the head node
		if currentNode.value == deleteNodeValue and previousNode == currentNode:
			print (f"Head Node is the Node I want to delete. Value: {currentNode.value}")	
			head = currentNode.nextNode
			
		# Case 2: deleteNode is NOT the tail and NOT the head
		if currentNode.value == deleteNodeValue and currentNode.nextNode is not None and previousNode != currentNode:	
			print (f"This is the Node I want to delete. Value: {currentNode.value}")		
			previousNode.nextNode = currentNode.nextNode
				
		# Case 3: deleteNode is the tail node
		if currentNode.value == deleteNodeValue and currentNode.nextNode is None:
			print (f"Tail Node is the Node I want to delete. Value: {currentNode.value}")	
			previousNode.nextNode = None
			
		
		#print (f"current node: {currentNode.value}")
		# Save the node info. of the current node before travel to the next one
		previousNode = currentNode
		currentNode = currentNode.nextNode
		
	return head
	
		
		
		
		
		
		
		



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

travelNode(currentNode)


head = inertNode(head, "1000")	

travelNode(head)


head = deleteNode(head, "3")	
travelNode(head)	
	
