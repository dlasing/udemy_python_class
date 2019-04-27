# 3.1 Reverse Linked list


# Define the linked list node

class LinkedListNode:
	
	def __init__ (self, value, nextNode = None):
		
		self.value = value
		self. nextNode = nextNode
		


def travel_link_list(head):
	
	currentNode = head
	
	while currentNode is not None:
		print (f"Node value = {currentNode.value}")
		currentNode = currentNode.nextNode
		
		
# Function to reverse the linked list
# ARG = head   # the head of the linked list	
def reverse_link_list(head):
	
	currentNode = head
	previousNode = None
	
	while currentNode is not None:
		
		currentNode = tmpNode
		currentNode.nextNode = previousNode
		previousNode = tmpNode
		
		
		
	

# Define the Node

node1 = LinkedListNode("100")
node2 = LinkedListNode("200")
node3 = LinkedListNode("300")
node4 = LinkedListNode("400")

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4


# define the head node
head = node1


travel_link_list(head)
		